# Prodesy Wiki — Schema & Conventions

This file tells the LLM how the **Prodesy** wiki is structured and how to maintain it. It is the config that makes each session a disciplined wiki maintainer rather than a generic chatbot. Co-evolve it with the user. **Status: v1 — synced with the sister plasmoDX schema on 2026-08-06.**

**Domain:** protein design — structure prediction (AlphaFold, RoseTTAFold), generative backbone and all-atom design (RFdiffusion, Chroma, Protpardelle), sequence design / inverse folding (ProteinMPNN, learned potentials), binder and interface design, motif scaffolding, symmetric assemblies, and the underlying protein biophysics (folding, stability, dynamics, interfaces) that determines whether a designed sequence actually behaves as intended. Also the experimental scaffolds and reagents that designs get built into — nanobodies, monobodies, coiled coils, fluorescent proteins, LOV/optogenetic domains, covalent tags.

Sister project: **plasmoDX** (malaria diagnostics) — same llm-wiki pattern, different domain. plasmoDX was forked from this schema, developed further, and its refinements were merged back here. Keep the two schemas in sync; when one diverges deliberately, say so explicitly in both files.

## Layers (from `llm-wiki.md`)

- **Raw sources** — `sources/` (immutable). PDFs of papers, organised into topical subfolders (`ProteinDesign/`, `Proteins/`, …). Never modify.
- **Wiki** — the LLM-owned markdown at project root: `index.md`, `log.md`, `overview.md`, and the `topics/`, `concepts/`, `papers/`, `tools/` folders. You write it; the user reads it.
- **Schema** — this file.

## Directory layout

```
Prodesy/
  CLAUDE.md      ← this file (conventions)
  llm-wiki.md    ← the idea file (reference; do not edit)
  index.md       ← catalog of every page (content-oriented)
  log.md         ← append-only chronological record
  overview.md    ← evolving synthesis of the field
  sources/       ← raw PDFs (immutable), in topical subfolders
  topics/        ← chapter-like deep dives (see below)
  concepts/      ← idea pages (many sources → one concept)
  papers/        ← one summary page per ingested source (the summary layer)
  tools/         ← entity pages for methods, models, software
  book/          ← the PDF-book builder skill (see below)
```

The Obsidian vault root is the project root, so the raw `sources/` PDFs are visible in the vault alongside the wiki pages.

More page types (people, datasets, benchmarks) can be added as the collection grows.

### `topics/` vs `concepts/` — the key distinction

- **`topics/`** are **chapters**: a deep, self-contained dive into one delimited part of protein design that can be read on its own. A topic pulls together everything the wiki knows about its subject — the biophysics, the models, the benchmarks, the wet-lab validation, the failure modes — into a long, structured narrative. A topic is a hub: it links out to the concept pages, tool pages and paper pages that supply its details.
- **`concepts/`** are **reusable ideas** that recur across many topics and sources: e.g. `motif-scaffolding.md`, `symmetric-assembly-design.md`. A concept page is the canonical home for one idea; topics, tools and papers link to it rather than re-explaining it.

Rule of thumb: if it's a *thing you'd write a book chapter about*, it's a topic. If it's *an idea you'd want a single canonical page for and cite from many places*, it's a concept. When in doubt, start it as a concept; promote to a topic once it has accumulated enough material to justify a chapter. Record promotions in `log.md` as a `revise` entry.

## Page conventions

- **Filenames:** lowercase, hyphenated, descriptive. Source pages: `firstauthor-year-topic.md` (e.g. `watson-2023-rfdiffusion.md`). The first-author surname leads, then the year, then a short topic slug. Topic/concept/tool pages: the entity name (e.g. `rfdiffusion.md`, `sequence-design.md`).
- **Links:** Obsidian wikilinks `[[filename-without-extension]]`. Obsidian resolves by basename across the vault, so the subfolder is not needed in the link. Always link the first mention of any entity/concept/topic/source that has (or should have) its own page.
- **Frontmatter:** every page starts with YAML for Dataview. Fields below.
- **Tone:** dense and factual. Capture claims, numbers, and methods — not marketing. Note contradictions between sources explicitly. Cite in prose by wikilinking the source page.
- **No hard-wrapping.** Write one paragraph (and one list item) per physical line — do **not** wrap prose at a fixed column. Obsidian's default renders a single newline as a visible line break, so mid-paragraph wraps show up as broken lines in Reading view. Let the editor soft-wrap. (Alternatively a reader can enable Settings → Editor → "Strict line breaks", but the files should not rely on it.)

### Frontmatter fields

Source page (`papers/`):
```yaml
---
type: source
title: <full paper title>
authors: <first author et al.>
venue: <journal year>
pdf: "../sources/<Subfolder>/<exact filename>.pdf"
supp: <yes | no | pending-ocr | missing-requested>   # state of the companion SI
tags: [structure-prediction, ...]
ingested: <YYYY-MM-DD>
---
```

Supplement (companion) page:
```yaml
---
type: source-supp
parent: "[[<main-source-page>]]"
title: <paper title> — Supplementary Information
pdf: "../sources/<Subfolder>/<exact _supp filename>.pdf"
tags: [...]           # inherit parent tags + methods/data specifics
ingested: <YYYY-MM-DD>
---
```

Topic / concept / tool page:
```yaml
---
type: topic   # or: concept | tool
tags: [...]
sources: <count>   # number of ingested sources touching this page
updated: <YYYY-MM-DD>
---
```

## Source page template (`papers/`)

1. Frontmatter
2. `# Title` + one-line what-it-is
3. **Problem** — what gap it addresses
4. **Approach** — method, in a few sentences
5. **Key results** — bulleted, with numbers where available
6. **Significance / relation to the field** — cross-links to topics, concepts & tools
7. **Connections** — explicit `[[links]]` to related sources (builds on / used by / contradicts)

## Topic page template (`topics/`)

Flexible — it's a chapter — but generally: frontmatter; a one-paragraph orientation; a table of contents / section list; then structured sections. End with **Open questions** and a **Sources** section listing the `papers/` pages that feed the chapter. Link concepts and tools inline.

## Ingest workflow

When a new source is dropped in `sources/` and the user asks to ingest:

1. Extract text (`pdftotext`; OCR only if needed — see below).
2. Read; identify the paper's core claim, method, results.
3. Write/refresh its `papers/` page.
4. **Check for a supplementary companion** (see next section) and ingest or flag it.
5. Update every relevant `topics/`, `concepts/` and `tools/` page (create if missing). A single source may touch 5–15 pages.
6. Add cross-references in both directions.
7. Update `index.md`.
8. Append a `log.md` entry.
9. Refresh `overview.md` if the source shifts the synthesis.

Prefer small, coherent batches so the graph stays connected. Batches are often organised around a theme or a `sources/` subfolder (e.g. the prediction-ecosystem batch).

### Sourcing discipline (current default)

Default is **source-grounded**: build pages from the ingested PDFs, not from model priors or un-requested web search. When a page has a genuine gap that a specific external reference would fill (a benchmark paper, a follow-up study, a newer model), **flag it** in the page's Open questions and in the "Flagged references to add" section of `index.md` so the user can supply the PDF manually. Do not silently fill gaps from the web unless the user asks.

### Review-article citation standard (hard rule)

The wiki must meet the standard of a **scientific review article**: **every sentence that asserts a fact or claim which cannot be verified from within the text itself must carry a citation to a reliable source.** In practice:

- **What needs a citation.** Any specific empirical claim — numbers (success rates, RMSDs, pLDDT/pAE thresholds, affinities, sequence-recovery percentages, parameter counts, runtimes, dataset sizes, dates), named methods and architectures, results, mechanisms, attributions ("X showed…"). Each such statement must wikilink the `papers/` (or `source-supp`) page it comes from. Quantitative claims especially: every number must be traceable to a source page.
- **What does not.** Sentences that are *internally verifiable* — definitions, restatements, or a synthesis that only combines claims already cited earlier on the same page. Pure connective or framing sentences that assert no new fact.
- **Internal wikilinks are navigation, not citations.** A link to another `topics/`, `concepts/` or `tools/` page does **not** by itself satisfy the standard — the reader must be able to reach a primary source. If a claim rests on a concept or tool page, either cite the underlying `papers/` page here too, or ensure the claim is uncontroversially grounded on the linked page and the link makes that traceable. When in doubt, cite the source directly.
- **No uncited factual sentences in the body.** A factual sentence that is neither cited nor internally verifiable is a **defect**, not acceptable prose. Fix it by (a) sourcing it, (b) rewriting it as an explicit synthesis of already-cited claims, or (c) moving it to *Open questions* / the "Flagged references to add" list. Do not paper over a gap with model priors.
- **Well-known textbook background** still needs a source under this standard; if none is ingested, flag it rather than asserting it bare.
- **Distinguish source from inference.** When the wiki draws a conclusion the sources do not state outright, mark it as the wiki's synthesis (e.g. "taken together, …") rather than phrasing it as a sourced fact.

### Image-based / bad-font PDFs (OCR)

If `pdftotext` returns near-empty text (watermarks only), the PDF is image-based or has a broken font map. Recover with OCR: `pdftoppm -gray -r 200 <pdf> /tmp/pg` then `tesseract /tmp/pg-NN.pgm out`. Set frontmatter `supp`/status accordingly. Only ask the user for a fresh PDF if OCR quality is poor.

## Supplementary companions (important in this field)

In protein-design papers, a large share of the methodological detail and extra data lives in the **Supplementary Information**, not the main text. Treat SI as a first-class, ingestable source.

**Convention.** For every source, check its `sources/` subfolder for a companion — usually the same stem with a `_supp`, `_Supp`, `_sm`, `_checklist` or `_Appendix` suffix.

- **If present:** ingest it as a separate `type: source-supp` page named `<main-stem>-supp.md`, with `parent:` linking back to the main page, and a reciprocal "Supplement: [[…]]" link on the main page. The companion page should *map* the SI (its structure/sections) and pull out the concrete methods, thresholds, hyperparameters, benchmark definitions and datasets the main summary omits — not re-summarize the main text.
- **If absent:** set the main page's frontmatter to `supp: missing-requested`, list it in the "Missing supplements" section of `index.md`, and tell the user.

The main-text summary stays the conceptual page; the companion is the detail/reference page. Link them both ways.

## Log format

Append-only. Each entry starts with a parseable prefix:

```
## [YYYY-MM-DD] <op> | <subject>
```

where `<op>` ∈ {ingest, query, lint, scaffold, revise}. `grep "^## \[" log.md | tail` gives recent activity.

**Log discussion-driven corrections as `revise`.** When a conversation with the user leads to a *substantive* change to existing content — a factual correction, a reframed section, a claim withdrawn, a concept promoted to a topic — record it as a `revise` entry even though no new source was ingested. The point is to keep the *reasoning* behind the change in the durable record rather than only in chat. Each `revise` entry should note **what changed, why, and which pages were touched**, and should flag if the correction was to something an earlier session had introduced (own the error in the record). Threshold: log corrections that change a claim or its framing; **skip** trivial edits (typos, formatting, link fixes). `revise` differs from `lint`, which is for self-initiated periodic hygiene sweeps (see below) rather than user-prompted content fixes.

## Lint checklist (periodic)

Contradictions across pages · stale claims superseded by newer sources · orphan pages (no inbound links) · concepts/topics mentioned but lacking a page · missing cross-references · misfiled source PDFs (wrong subfolder) · duplicate PDFs of the same paper · uncited factual sentences (see the citation standard) · data gaps fillable by a flagged reference.

## The book builder (`book/`)

`book/build_book.py` renders the whole wiki as a single hyperlinked PDF (title page, clickable contents, introduction from `overview.md`, topic chapters grouped into Parts, a concept lookup section, a glossary, and an anchored reference list). It re-reads the current wiki on every run, so rebuild after each ingest:

```
python3 book/build_book.py
```

Requires `pandoc` + `xelatex`. Chapter grouping lives in the `PART_LAYOUT` list at the top of the script; any topic not listed is auto-appended so nothing is dropped. Terms live in `book/glossary.md`. See `book/SKILL.md` for details.

## Open format questions (iterating)

- Which of the current `concepts/` pages have grown enough to be promoted to `topics/` chapters (candidates flagged in `index.md`).
- Page granularity for tools vs. concepts (e.g. "diffusion generative design" is a concept, RFdiffusion a tool — current split).
- Whether `papers/` should mirror the `sources/` subfolder structure or stay flat (currently flat).
- Whether to add `people/` (Baker lab, DeepMind, Huang lab) and `benchmarks/` (CASP, PDB test sets, binder-design benchmark suites) page types.
