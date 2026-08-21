---
name: prodesy-book
description: Compile the Prodesy protein-design wiki into a single book-style PDF with a clickable table of contents and live internal cross-references — intro (overview) → topic chapters grouped into Parts → a concept lookup section → a glossary → an annotated reference list. Use whenever the user asks to (re)generate the wiki PDF / book / handbook, export the wiki to PDF, or refresh the compiled book after ingesting new sources. Draft skill — refine as the wiki grows.
---

# Prodesy → book-style PDF

This skill turns the Prodesy Obsidian wiki (a folder of Markdown with `[[wikilinks]]`) into one navigable PDF book where every cross-reference is a clickable internal link. It is the sister of the `plasmodx-book` skill in the plasmoDX repo; keep the two builders in sync.

## When to use

- "Regenerate / rebuild the wiki PDF (book / handbook)."
- "Export the wiki to a PDF."
- "Refresh the compiled book" after new sources or chapters were ingested.

## Prerequisites

- `pandoc` and `xelatex` on PATH.
- A Unicode serif font (default **DejaVu Serif**; override with `--font`).

Quick check: `pandoc --version && which xelatex && fc-list | grep -i "DejaVu Serif"`.

## How to run

From the wiki repo:

```
python3 book/build_book.py                 # writes ./Prodesy-wiki.pdf
python3 book/build_book.py --out /path/to/out.pdf
python3 book/build_book.py --wiki /path/to/wiki --font "Noto Serif"
```

The script reads `overview.md`, `topics/`, `concepts/`, `papers/`, `tools/`, and this folder's `glossary.md`. It writes its scratch files to a temp dir, so the repo stays clean.

## What it produces (structure)

1. **Title page + Contents** (auto TOC, chapter level, with page numbers).
2. **Introduction** — the wiki `overview.md`.
3. **Topic chapters**, grouped into Parts (see `PART_LAYOUT` in the script). Parts with no matching topic file are skipped, so the book is valid even while `topics/` is still being populated.
4. **Concepts — a lookup section** — every `concepts/` page as a short chapter.
5. **Glossary** — from `glossary.md` (edit that file to change terms).
6. **References** — an annotated, anchored list of every `papers/` (and `tools/`) source; all in-text citations link here.

## How cross-references are made active

`build_book.py` rewrites every `[[target]]` / `[[target|alias]]` into a Markdown link `[label](#target)`, gives each page's title an explicit `{#basename}` anchor, and anchors each reference entry with a `{#basename}` span. Pandoc + hyperref then render these as clickable PDF links (coloured via a `_colors.tex` header generated at build time). Wikilinks to pages **not** included in the book are de-linked to plain text so nothing dangles.

Paper link labels are derived from the filename, which is why the `firstauthor-year-topic` convention matters: `watson-2023-rfdiffusion` → "Watson 2023", `vasquez-torres-2023-helical-peptide-binders` → "Vasquez-Torres 2023", and a three-plus-token author prefix becomes "Firstauthor et al. YEAR". Supplement pages get "(suppl.)". Concept/topic/tool labels use the page's own title.

## Customizing

- **Chapter order / Parts:** edit `PART_LAYOUT` at the top of `build_book.py`. Any topic not listed is appended under "Further Topics" (nothing is silently dropped); any listed topic that does not exist yet is skipped.
- **Glossary:** edit `book/glossary.md` (a pandoc definition list).
- **Fonts / colours:** `--font` flag; link colour in the `_colors.tex` block inside the script.
- **Missing glyph in the PDF** (a character the font lacks): add it to the `SANITIZE` map in the script, mapping it to a LaTeX-math equivalent (e.g. `"⇌": r"$\rightleftharpoons$"`).

## Verify after building

- `pdfinfo Prodesy-wiki.pdf | grep Pages`
- Dead-link check: every `](#x)` target should have a matching `{#x}` anchor (the script's design guarantees this; the intermediate `_book.md` in the temp dir can be re-checked if needed).

## Note on installing this as a Cowork skill

These files (`SKILL.md`, `build_book.py`, `glossary.md`) are a **draft skill kept in the repo**. To make it an installed/available skill, add it via **Settings → Capabilities** (skills can't be registered from within a working session). Until then, just run `build_book.py` directly as above.
