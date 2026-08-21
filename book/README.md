# book/ — compile the Prodesy wiki into a PDF

Turns the wiki (Markdown + `[[wikilinks]]`) into one book-style PDF with a clickable
table of contents and live internal cross-references.

```
python3 book/build_book.py        # -> ./Prodesy-wiki.pdf
```

Files:

- `build_book.py` — the builder (wikilink → internal-link conversion, assembly, pandoc+xelatex).
- `glossary.md` — the glossary chapter (edit to change terms).
- `SKILL.md` — reusable-skill definition (how/when to run; install via Settings → Capabilities).

Requires `pandoc`, `xelatex`, and a Unicode serif font (DejaVu Serif by default).
Structure and customization are documented in `SKILL.md`.

Sister builder: `book/build_book.py` in the plasmoDX repo. Keep the two in sync.
