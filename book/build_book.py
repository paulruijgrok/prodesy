#!/usr/bin/env python3
"""
build_book.py — Compile the Prodesy Obsidian wiki into a single book-style PDF
with a clickable table of contents and live internal cross-references.

Pipeline: read the wiki markdown -> strip YAML frontmatter -> convert Obsidian
[[wikilinks]] into internal anchor links -> assemble an ordered book (intro,
topic chapters grouped into Parts, a concept lookup section, a glossary, and an
annotated reference list) -> render with pandoc + xelatex (hyperref) so every
cross-reference is a clickable PDF link.

Usage:
    python3 build_book.py [--wiki WIKI_DIR] [--out OUT.pdf]

Defaults: WIKI = parent dir of this script; OUT = WIKI/Prodesy-wiki.pdf.
Requires: pandoc, xelatex, and a Unicode serif font (DejaVu Serif by default).
"""
import argparse, os, re, subprocess, sys, glob, tempfile

# ----------------------------------------------------------------------------- config
# Which topics go in which Part, and in what order. Any topic file not listed
# here is appended to a final "Further topics" Part so nothing is silently lost.
PART_LAYOUT = [
    ("Foundations", ["protein-biophysics", "structure-prediction"]),
    ("Generative Design", ["generative-backbone-design", "all-atom-design", "motif-scaffolding"]),
    ("Sequence and Interfaces", ["sequence-design", "binder-design", "interface-design"]),
    ("Assemblies, Scaffolds and Validation",
     ["symmetric-oligomer-design", "scaffolds-and-reagents", "benchmarking-and-validation"]),
]

SANITIZE = {  # glyphs xelatex+DejaVu may lack -> safe LaTeX math equivalents
    "⇌": r"$\rightleftharpoons$",  # ⇌
    "→": r"$\rightarrow$",          # →
    "←": r"$\leftarrow$",           # ←
    "↔": r"$\leftrightarrow$",      # ↔
    "″": '"',
    "₁": "$_{1}$", "₂": "$_{2}$", "₃": "$_{3}$", "₄": "$_{4}$",
    "₅": "$_{5}$", "₆": "$_{6}$", "₇": "$_{7}$", "₈": "$_{8}$",
    "₉": "$_{9}$", "₀": "$_{0}$",
    "⁰": "$^{0}$", "¹": "$^{1}$", "²": "$^{2}$", "³": "$^{3}$",
    "⁴": "$^{4}$", "⁵": "$^{5}$", "⁶": "$^{6}$", "⁷": "$^{7}$",
    "⁸": "$^{8}$", "⁹": "$^{9}$",
    "⁺": "$^{+}$", "⁻": "$^{-}$", "ⁿ": "$^{n}$",
    "™": r"\textsuperscript{TM}",  # ™
}

WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
H1 = re.compile(r"^#\s+(.*?)\s*$", re.M)

# ----------------------------------------------------------------------------- helpers
def strip_frontmatter(text):
    if text.startswith("---"):
        m = re.match(r"^---\n.*?\n---\n", text, re.S)
        if m:
            return text[m.end():]
    return text

def parse_frontmatter(text):
    fm = {}
    if text.startswith("---"):
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if m:
            for line in m.group(1).splitlines():
                mm = re.match(r"^(\w+):\s*(.*)$", line)
                if mm:
                    fm[mm.group(1)] = mm.group(2).strip().strip('"')
    return fm

def first_paragraph(body):
    """First non-empty paragraph after the H1 title (the wiki's one-liner)."""
    lines = body.splitlines()
    i = 0
    while i < len(lines) and not lines[i].startswith("# "):
        i += 1
    i += 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    para = []
    while i < len(lines) and lines[i].strip() and not lines[i].startswith("#"):
        para.append(lines[i].strip())
        i += 1
    return " ".join(para)

def title_of(body):
    m = H1.search(body)
    return m.group(1).strip() if m else ""

def paper_label(bn):
    toks = bn.split("-")
    yi = next((i for i, t in enumerate(toks) if re.fullmatch(r"\d{4}", t)), None)
    if yi and yi >= 1:
        authors, year = toks[:yi], toks[yi]
        if len(authors) > 2:
            lab = f"{authors[0].capitalize()} et al. {year}"
        else:
            lab = "-".join(a.capitalize() for a in authors) + f" {year}"
        if bn.endswith("-supp"):
            lab += " (suppl.)"
        return lab
    return bn.replace("-", " ").title()

# ----------------------------------------------------------------------------- main
def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", default=os.path.dirname(here))
    ap.add_argument("--out", default=None)
    ap.add_argument("--font", default="DejaVu Serif")
    args = ap.parse_args()
    WIKI = os.path.abspath(args.wiki)
    OUT = args.out or os.path.join(WIKI, "Prodesy-wiki.pdf")

    def rd(p):
        with open(p, encoding="utf-8") as f:
            return f.read()

    # --- gather pages
    topics = {os.path.basename(p)[:-3]: rd(p) for p in glob.glob(f"{WIKI}/topics/*.md")}
    concepts = {os.path.basename(p)[:-3]: rd(p) for p in glob.glob(f"{WIKI}/concepts/*.md")}
    papers = {os.path.basename(p)[:-3]: rd(p) for p in glob.glob(f"{WIKI}/papers/*.md")}
    tools = {os.path.basename(p)[:-3]: rd(p) for p in glob.glob(f"{WIKI}/tools/*.md")}
    overview = rd(f"{WIKI}/overview.md")
    glossary = rd(f"{here}/glossary.md")

    # --- bodies (frontmatter stripped) and title map
    def body(txt):
        return strip_frontmatter(txt).strip()
    topic_b = {k: body(v) for k, v in topics.items()}
    concept_b = {k: body(v) for k, v in concepts.items()}
    tool_b = {k: body(v) for k, v in tools.items()}
    overview_b = body(overview)

    title_map = {}
    for k, b in {**topic_b, **concept_b, **tool_b}.items():
        title_map[k] = title_of(b)
    title_map["overview"] = "Introduction — the field at a glance"

    known = set(topic_b) | set(concept_b) | set(papers) | set(tool_b) | {"overview"}

    # --- wikilink -> internal link converter
    def link_text(target, alias):
        if alias:
            return alias
        if target in papers:
            return paper_label(target)
        if target in title_map:
            return title_map[target]
        return target.replace("-", " ")

    def convert(text):
        def repl(m):
            inner = m.group(1)
            target, alias = (inner.split("|", 1) + [None])[:2]
            target = target.split("#")[0].strip()
            alias = alias.strip() if alias else None
            if target in known:
                return f"[{link_text(target, alias)}](#{target})"
            return link_text(target, alias)  # de-link unknown targets
        return WIKILINK.sub(repl, text)

    def anchor_title(b, bn, force_title=None):
        """Ensure the page's H1 carries an explicit {#bn} id (and optional retitle)."""
        def repl(m):
            t = force_title if force_title else m.group(1)
            return f"# {t} {{#{bn}}}"
        return H1.sub(repl, b, count=1)

    # ----------------------------------------------------------------- assemble
    date = subprocess.run(["date", "+%Y-%m-%d"], capture_output=True, text=True).stdout.strip()
    out = []
    out.append(f"""---
title: "Prodesy"
subtitle: "An LLM-maintained wiki on protein design — book edition"
author: "Compiled from the Prodesy wiki"
date: "{date}"
---

""")

    # Introduction (overview)
    intro = anchor_title(overview_b, "overview", force_title="Introduction — the field at a glance")
    out.append(convert(intro))
    out.append("\n\n")

    placed = set()
    def part(name):
        out.append(f'\n\n```{{=latex}}\n\\part{{{name}}}\n```\n\n')

    def emit_chapter(bn, b):
        out.append(convert(anchor_title(b, bn)))
        out.append("\n\n")
        placed.add(bn)

    # Topic Parts
    for pname, keys in PART_LAYOUT:
        present = [k for k in keys if k in topic_b]
        if not present:
            continue          # don't emit empty Parts
        part(pname)
        for k in present:
            emit_chapter(k, topic_b[k])
    extras = [k for k in sorted(topic_b) if k not in placed]
    if extras:
        part("Further Topics")
        for k in extras:
            emit_chapter(k, topic_b[k])

    # Concepts (lookup)
    part("Concepts — a lookup section")
    for k in sorted(concept_b):
        emit_chapter(k, concept_b[k])

    # Reference part: glossary + annotated bibliography
    part("Reference")
    out.append(convert(glossary))
    out.append("\n\n")

    # Annotated references (papers + tools), anchored, not TOC-heading-heavy
    out.append("# References {#references}\n\n")
    out.append("Every source ingested into the wiki, with a one-line description. "
               "In-text citations throughout the book link here.\n\n")
    for bn in sorted(papers):
        fm = parse_frontmatter(papers[bn])
        b = body(papers[bn])
        authors = fm.get("authors", "")
        venue = fm.get("venue", "")
        title = fm.get("title", title_of(b))
        one = convert(first_paragraph(b))
        cite = ". ".join(x for x in [authors, title, venue] if x)
        out.append(f"[**{paper_label(bn)}.**]{{#{bn}}} {cite}. — {one}\n\n")
    for bn in sorted(tool_b):
        b = tool_b[bn]
        one = convert(first_paragraph(b))
        out.append(f"[**{title_of(b)}.**]{{#{bn}}} {one}\n\n")

    md = "".join(out)
    for k, v in SANITIZE.items():
        md = md.replace(k, v)

    workdir = tempfile.mkdtemp(prefix="prodesy-book-")
    tmp_md = os.path.join(workdir, "_book.md")
    with open(tmp_md, "w", encoding="utf-8") as f:
        f.write(md)

    header = os.path.join(workdir, "_colors.tex")
    with open(header, "w", encoding="utf-8") as f:
        f.write(r"""\definecolor{linkblue}{HTML}{1A5FB4}
\hypersetup{colorlinks=true,linkcolor=linkblue,urlcolor=linkblue,%
  citecolor=linkblue,filecolor=linkblue,anchorcolor=linkblue}
\usepackage{sectsty}
""")

    cmd = [
        "pandoc", tmp_md, "-o", OUT,
        "--pdf-engine=xelatex", "--toc", "--toc-depth=1",
        "-H", header,
        "-V", "documentclass=report", "-V", "geometry:margin=1in",
        "-V", "colorlinks=true",
        "-V", f"mainfont={args.font}", "-V", "monofont=DejaVu Sans Mono",
        "--metadata", "lang=en",
    ]
    print("Running:", " ".join(cmd))
    r = subprocess.run(cmd, capture_output=True, text=True)
    sys.stderr.write(r.stderr)
    if r.returncode != 0:
        sys.exit(r.returncode)
    print("Wrote", OUT)

if __name__ == "__main__":
    main()
