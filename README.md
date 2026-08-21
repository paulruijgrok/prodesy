# Prodesy

A working knowledge base on **protein design**, maintained as an LLM-written wiki. It covers structure prediction, generative backbone and all-atom design, sequence design and inverse folding, binder and interface design, motif scaffolding, symmetric assemblies, and the underlying biophysics that decides whether a designed sequence actually behaves as intended.

This is a personal synthesis of published literature, not original research. Nothing here is unpublished work.

## Start here

- **[`index.md`](index.md)** — catalog of every page, plus what's missing and why.
- **[`overview.md`](overview.md)** — the current synthesis of the field, in one page.
- **[`topics/symmetric-oligomer-design.md`](topics/symmetric-oligomer-design.md)** — the first full chapter, and the best sample of what this wiki is for: point-group symmetric homo-oligomers from the coiled-coil era to conditional diffusion.
- **[`Prodesy-wiki.pdf`](Prodesy-wiki.pdf)** — the whole wiki compiled into a single hyperlinked 33-page book.

## How it's organised

The wiki is a layered structure, not a flat pile of notes. Each layer answers a different question.

| Layer | Question it answers | Contents |
|---|---|---|
| `papers/` | *What did this specific paper claim?* | One page per ingested source. 20 main sources + 13 supplementary companions. |
| `concepts/` | *What is this idea, canonically?* | Short reusable pages — `symmetric-assembly-design`, `motif-scaffolding`, `sequence-design`, `binder-design`, `diffusion-generative-design`, `structure-prediction`. Cited from everywhere else. |
| `topics/` | *What's the whole story here?* | Chapter-length deep dives that pull concepts, tools and papers into one narrative. |
| `tools/` | *What is this model/software?* | Entity pages — AlphaFold, RoseTTAFold, RFdiffusion, RFdiffusion3, ProteinMPNN, Chroma, Protpardelle. |
| `overview.md`, `index.md`, `log.md` | *Where does it all stand?* | Synthesis, catalog, and an append-only chronological record of every ingest and revision. |

Pages link to each other with Obsidian-style `[[wikilinks]]`; the vault root is the repository root, so cloning this and opening it in Obsidian gives you the graph view.

## The conventions are the point

[`CLAUDE.md`](CLAUDE.md) is the schema — the file that makes each session a disciplined wiki maintainer rather than a general-purpose chatbot. It specifies page templates, frontmatter fields, the ingest workflow, the log format, and a periodic lint checklist. Two rules do most of the work:

**Source-grounded by default.** Pages are built from ingested PDFs, not from model priors or unrequested web search. When a page has a real gap, it gets *flagged* — named explicitly in the page's Open questions and in the "Flagged references to add" section of `index.md` — rather than quietly filled in. See §12 of the symmetric-oligomer chapter for what that looks like in practice.

**A review-article citation standard.** Every sentence asserting a fact that can't be verified from the text itself must wikilink the source page it came from. Numbers especially: every RMSD, success rate and threshold should be traceable to a paper page. Internal links between concept pages count as navigation, not citation. Where the wiki draws a conclusion its sources don't state outright, it says so ("taken together…", "the wiki's reading is…") rather than dressing inference up as a sourced fact.

## Note: `sources/` is not in this repository

The wiki is built from a local library of ~134 PDFs (~930 MB) in a `sources/` directory, deliberately excluded via `.gitignore`. Those are publisher PDFs and aren't mine to redistribute.

This means **the `pdf:` paths in page frontmatter resolve only on the original machine.** They're kept because they're load-bearing for the maintenance workflow, not because they'll work for you. Every page identifies its source by title, authors and venue, so the underlying papers are straightforward to find.

## Rebuilding the book

```bash
python3 book/build_book.py          # writes ./Prodesy-wiki.pdf
```

Requires `pandoc` and `xelatex`. The script re-reads the wiki on every run, rewrites every `[[wikilink]]` into a clickable internal PDF link, and assembles a title page, contents, the overview as an introduction, topic chapters grouped into Parts, a concept lookup section, a glossary and an anchored reference list. Chapter grouping lives in `PART_LAYOUT` at the top of the script; glossary terms live in `book/glossary.md`. See [`book/SKILL.md`](book/SKILL.md).

## Status

Twenty sources and thirteen supplements ingested across three batches — the deep-learning core, a generative-design expansion, and the symmetric-assembly history. One topic chapter written; the promotion candidates for the next chapters are listed in `index.md`, along with the specific references that would close known gaps.

## Licence

- **Wiki text** (`*.md`, `Prodesy-wiki.pdf`) — [CC BY 4.0](LICENSE). Reuse it, quote it, build on it; just credit it.
- **Code** (`book/build_book.py`) — [MIT](LICENSE-CODE).
- **Not covered:** the source PDFs, which aren't in this repository and remain under their publishers' terms.
