# Prodesy Wiki — Log

Append-only. Entry prefix: `## [YYYY-MM-DD] <op> | <subject>` (`<op>` ∈ {ingest, query, lint, scaffold, revise}). Recent: `grep "^## \[" log.md | tail`.

## [2026-07-10] scaffold | wiki initialized

Created `wiki/` structure per [[CLAUDE]]: sources/, concepts/, tools/, plus index/log/overview. Schema is v0 — page format and conventions to be iterated with the user.

## [2026-07-10] ingest | Batch 1 — deep-learning protein design core (6 sources)

Ingested 6 tightly-interconnected landmark papers from `sources/ProteinDesign/`:
[[jumper-2021-alphafold2]], [[abramson-2024-alphafold3]], [[dauparas-2022-proteinmpnn]], [[watson-2023-rfdiffusion]], [[bennett-2023-binder-design-dl]], [[ingraham-2023-chroma]].

Created concept pages ([[structure-prediction]], [[sequence-design]], [[diffusion-generative-design]], [[binder-design]]) and tool pages ([[alphafold]], [[rfdiffusion]], [[proteinmpnn]], [[chroma]]). Wrote [[overview]] synthesis. Updated [[index]].

Notes:
- RoseTTAFold All-Atom (Krishna 2024) was in the intended batch but its PDF is image-based; swapped in [[ingraham-2023-chroma]] and **queued RFAA for OCR**.
- Grounding via `pdftotext` of first ~12 pages per paper (abstracts + key results verified).
- Time-boxed run (20-min cap).

## [2026-07-13] ingest | RoseTTAFold All-Atom (Krishna 2024) — OCR-recovered

Main PDF had a broken text layer (`pdftotext` → watermarks only). Recovered via `pdftoppm -gray -r 200` + `tesseract`. Wrote [[krishna-2024-rosettafold-all-atom]] and added [[rosettafold]] tool page. Updated [[structure-prediction]], [[diffusion-generative-design]], [[binder-design]] (RFdiffusionAA small-molecule binders: digoxigenin, heme, bilin). SI not in folder → flagged missing-requested. A fresh clean main PDF would also help.

## [2026-07-13] schema | supplementary-companion workflow added

Updated [[CLAUDE]]: for every source, check for a `_supp`/`_Supp`/`_sm`/`_Appendix` companion. If present, ingest as `type: source-supp` linked to parent. If absent, set `supp: missing-requested`, list in [[index]], and ask the user. Added OCR instructions and a `supp:` frontmatter field.

## [2026-07-13] ingest | RFdiffusion Supplementary Information (companion)

Ingested the 129-page RFdiffusion SI as [[watson-2023-rfdiffusion-supp]] (mapped sections + extracted the AF2-based in silico success criteria, SO(3) rotation diffusion, self-conditioning, symmetry/motif/PPI conditioning, external potentials, noise-scaled diversity). Linked both ways with [[watson-2023-rfdiffusion]].

## [2026-07-13] note | batch-1 supplements audited

Only RFdiffusion had a local `_supp`. Flagged missing SI for AF2, AF3, ProteinMPNN, Bennett binder, Chroma, RFAA (see [[index]] → Missing supplements).

## [2026-07-13] ingest | AlphaFold2 + AlphaFold3 Supplementary Information (companions)

User supplied the AF2 (62 pp) and AF3 (45 pp) SIs. Ingested both as companions: [[jumper-2021-alphafold2-supp]] (Evoformer/triangle ops, IPA, FAPE, pLDDT/pTM, self-distillation, recycling, CASP14, ablations) and [[abramson-2024-alphafold3-supp]] (unified tokenization, Pairformer, diffusion module + conditioning, atom attention, confidence-on-samples + clash ranking, cross-distillation vs hallucinated disorder). Linked both ways to parents; set `supp: yes`. Remaining missing SIs: ProteinMPNN, Bennett binder, Chroma, RFAA.

## [2026-07-13] ingest | Remaining 4 SIs — ProteinMPNN, Bennett, Chroma, RFAA (companions)

User supplied all four. Ingested as companions: [[dauparas-2022-proteinmpnn-supp]] (edge-only GNN features, encoder edge updates, random-order decoding, ablations, pseudocode), [[bennett-2023-binder-design-dl-supp]] (pLDDT/pAE_interaction vs RMSD, ROC discrimination of SC50<4µM, MPNN-vs-Rosetta prospective tests), [[ingraham-2023-chroma-supp]] (polymer-covariance diffusion prior, correlated→uncorrelated transform, SDE/ODE sampling, Bayesian conditioners, sub-quadratic random-graph net), [[krishna-2024-rosettafold-all-atom-supp]] (atomized/bond/chirality featurization, sequence/ligand-similarity generalization, RFdiffusionAA bilin/heme/digoxigenin protocols). Linked both ways; set `supp: yes`. **Batch 1 now complete: 7 sources + 7 supplements.** No SIs outstanding (RFAA clean main PDF still nice-to-have).

## [2026-07-13] ingest | Batch 2 — generative-design expansion (6 sources + 3 supplements)

Ingested: [[wang-2022-functional-site-scaffolding]] (hallucination + inpainting motif scaffolding), [[wicky-2022-symmetric-assembly-design]] (hallucinating symmetric assemblies), [[vasquez-torres-2023-helical-peptide-binders]] + supp (peptide-hormone binders, partial diffusion, biosensors), [[chu-2024-protpardelle]] + supp (Huang-lab all-atom superposition generative model), [[anand-2022-learned-potential-seqdesign]] (Huang-lab learned-potential sequence design), [[butcher-2025-rfdiffusion3]] + supp (all-atom token+atom generator, ~10× cheaper, DNA binders).

New concept pages: [[motif-scaffolding]], [[symmetric-assembly-design]]. New tool pages: [[protpardelle]], [[rfdiffusion3]]. Updated [[diffusion-generative-design]] (now covers 4 all-atom routes), [[sequence-design]] (learned potentials + codesign), [[binder-design]] (peptide + nucleic-acid branches), [[rfdiffusion]] tool (lineage), [[overview]], [[index]].

Two Huang-lab papers included (user's lab). All main PDFs text-extractable. **Wiki now: 13 sources + 10 supplements.**

## [2026-08-06] scaffold | Schema sync with the sister plasmoDX wiki

Merged the conventions that plasmoDX developed after being forked from this schema back into Prodesy, so one set of standards now serves both wikis. `CLAUDE.md` goes to v1.

**Layout (breaking).** Dropped the `wiki/` wrapper — `index.md`, `log.md`, `overview.md`, `CLAUDE.md`, `concepts/` and `tools/` now live at the project root, and the Obsidian vault root is the project root. Per-paper summaries moved from `wiki/sources/` to `papers/`, freeing `sources/` to mean *raw PDFs only* (it already held them). Added an empty `topics/` for chapter-like deep dives. Frontmatter `pdf:` paths (`../sources/<Subfolder>/…`) resolve unchanged after the move — all 23 verified.

**Filenames (breaking).** Adopted plasmoDX's `firstauthor-year-topic` source-page convention. Renamed all 23 paper and supplement pages (e.g. `rfdiffusion-watson-2023` → [[watson-2023-rfdiffusion]], `helical-peptide-binders-vasquez-torres-2023` → [[vasquez-torres-2023-helical-peptide-binders]]) and rewrote every wikilink across 40 files. Link check: 0 dead links, 0 orphans.

**Standards ported into `CLAUDE.md`.** The `topics/` vs `concepts/` distinction and a topic page template; the no-hard-wrapping rule; source-grounded sourcing discipline with a "Flagged references to add" list in `index.md`; the **review-article citation standard** (every non-internally-verifiable factual sentence must wikilink a source page; internal wikilinks are navigation, not citations); the `revise` log op for discussion-driven corrections; an expanded lint checklist; a domain statement and a reciprocal sister-project note. plasmoDX's `CLAUDE.md` was updated in the same pass to record the merge-back and to document its book builder.

**Book builder.** Ported `book/` from plasmoDX (`build_book.py`, `glossary.md`, `SKILL.md`, `README.md`), retitled for Prodesy, gave `PART_LAYOUT` protein-design Parts, replaced the malaria-specific author-label branch with the generic rule, and made empty Parts skip so the book is valid while `topics/` is still empty. Wrote a ~45-term protein-design glossary. Test build: 18 pp, 116 internal links, 0 dead, 0 residual wikilinks. The empty-Part guard was ported back to plasmoDX for parity.

**Lint findings fixed.** [[wang-2022-functional-site-scaffolding]], [[wicky-2022-symmetric-assembly-design]] and [[anand-2022-learned-potential-seqdesign]] carried `supp: no`; all three are *Science*/*Nat Commun* papers that do have SI, and the PDFs are simply absent from `sources/`. Corrected to `supp: missing-requested` and listed under Missing supplements in [[index]].

**Deferred, awaiting approval.** A citation-standard audit of the pre-standard pages is written up in [[index]] (five groups: uncited numbers on tool pages, uncited generalisations, unmarked wiki inference, claims with no ingested source, housekeeping). No page content was rewritten. Four flagged references were added to [[index]] — base RoseTTAFold (Baek 2021), a Rosetta design baseline, a folding-problem foundation, and an lDDT/metrics reference — three of which have candidate PDFs already sitting in `sources/`.

## [2026-08-14] ingest | Batch 3 — symmetric assembly (6 sources + 2 supplements)

Ingested the pre-deep-learning symmetric-assembly literature, all of it already present but untouched in `sources/`: [[harbury-1993-coiled-coil-oligomer-switch]] (oligomeric state encoded in core residue geometry), [[huang-2014-parametric-helical-bundles]] + supp (Crick-equation parametric backbones), [[thomson-2014-alpha-helical-barrels]] (designed C5/C6/C7 barrels with defined channels), [[boyken-2016-hydrogen-bond-network-oligomers]] (HBNet; specificity as a design axis), [[luo-2016-protein-assembly-review]] (Chem. Rev. survey, ingested specifically as the historical reference for the symmetry-by-fusion lineage), and [[courbet-2022-axle-rotor-assemblies]] + supp (symmetry-mismatched machines).

Motivation was a hard constraint, not completeness: the review-article citation standard made a chapter-length treatment of symmetric oligomers impossible on the two sources the wiki had ([[wicky-2022-symmetric-assembly-design]] and [[watson-2023-rfdiffusion]]). Rather than fill the history from model priors, the batch was scoped to what could be sourced from disk.

Two supplements were present and ingested as companions: [[huang-2014-parametric-helical-bundles-supp]] (the explicit Crick equations; the fact that cyclic symmetry is exact by construction because φ0 is *set* to {0, 2π/n, …}) and [[courbet-2022-axle-rotor-assemblies-supp]] (parametric sampling ranges, HBNet interfaces, RosettaRemodel fusion — the concrete measure of how much hand-engineering the pre-diffusion route required per symmetry group). Two supplements are absent and flagged `missing-requested`: [[thomson-2014-alpha-helical-barrels]] and [[boyken-2016-hydrogen-bond-network-oligomers]], in both cases the SI holding the actual method.

Wiki now: 19 sources + 12 supplements.

## [2026-08-14] revise | Concept promoted: symmetric-assembly-design → topics/symmetric-oligomer-design

**What changed.** [[symmetric-assembly-design]] was promoted to the wiki's first `topics/` chapter, [[symmetric-oligomer-design]]. The concept page was rewritten as a short canonical stub that defines the idea and points to the chapter; per `CLAUDE.md` the concept remains the thing other pages cite, the topic is the thing that is read.

**Why.** It was listed in [[index]] as a promotion candidate only implicitly (the four named candidates were structure-prediction, diffusion-generative-design, binder-design and sequence-design). The batch-3 ingest took the page from 2 sources to 9, which clears the bar, and the user asked for the deep dive directly.

**The chapter's organising claim** — flagged here because it is wiki synthesis rather than any source's stated thesis: symmetric oligomer design has been solved three times by genuinely different mechanisms, which the chapter labels *exact by construction* (parametric — symmetry is a property of the coordinate generator, per [[huang-2014-parametric-helical-bundles-supp]]), *rewarded* (hallucination — symmetry is a term in a loss, per [[wicky-2022-symmetric-assembly-design]]), and *projected* (diffusion — point-group operators applied to the state at every denoising step, per [[watson-2023-rfdiffusion-supp]] §3.1). The corollary drawn in §7, also wiki synthesis, is that as symmetry moved from the coordinates into the sampling process the binding constraint moved from geometry to interface quality — which is the chapter's reading of why RFdiffusion's symmetric coverage (C/D/T/I) so far outruns its yield (87 of 608 designs SEC-consistent).

**Pages touched.** New: [[symmetric-oligomer-design]] and the six batch-3 paper pages plus two supplements. Rewritten: [[symmetric-assembly-design]]. Updated: [[index]] (status line, Topics section, concept source count, batch-3 paper list, supplements, missing supplements, flagged references), [[overview]] (symmetric assembly now a chapter; the three-mechanisms reading added to cross-cutting observations), `book/build_book.py` (`PART_LAYOUT` gains an *Assemblies* Part so the chapter is placed rather than auto-appended).

**Flagged, not written.** Six historical references the chapter cannot cite from primary literature are listed in §12 of the chapter and mirrored in [[index]] — Padilla/Yeates 2001 (currently second-hand via [[luo-2016-protein-assembly-review]]), King 2012 and 2014, Bale 2016, and Anishchenko 2021 for the hallucination lineage. Three further PDFs already in `sources/` (Shen 2018 filaments, Brunette 2015 repeat proteins, Schneider 2005 SymmDock) sit just outside the chapter's point-group scope and were deliberately not ingested.

## [2026-08-14] ingest | Anishchenko 2021 — de novo design by deep network hallucination (+ supplement)

User supplied the main text and SI, closing the highest-priority *deep-learning* gap flagged the same day in [[symmetric-oligomer-design]] §12 and [[index]]. Ingested as [[anishchenko-2021-hallucination]] and [[anishchenko-2021-hallucination-supp]].

**Method, now on a primary source.** Random sequence → MCMC simulated annealing in sequence space → accept/reject on the change in Kullback–Leibler divergence between trRosetta's predicted inter-residue distance/orientation distributions and generic length- and separation-dependent background distributions. The objective is pure *contrast*, with no target structure specified; the authors' analogy is DeepDream. 2,000 proteins generated; 129 tested; 27 SEC-positive with consistent CD; 21 thermostable above 70 °C; three structures solved (NMR 1.82 Å; X-ray 2.53 Å; X-ray 3.68 Å overall, 1.32/2.17 Å per half). Closest PDB structure to design 0738_mod is Top7.

**The finding that changed the chapter.** Every sequence was modelled as a **monomer**, yet many hallucinated proteins formed homo-oligomers in solution — design 0217 crystallized as a dimer, corroborated by SEC-MALS and NMR relaxation. The authors attribute this to trRosetta having been trained on native structures including many homo- and hetero-oligomers, so it never learned to disfavour surface hydrophobics enough for soluble monomers; the SI demonstrates the diagnosis by converting oligomers to monomers with polar substitutions and paired before/after SEC traces.

## [2026-08-14] revise | symmetric-oligomer-design §5 rewritten around the hallucination primary source

**What changed.** §5 was split. New **§5.1** grounds hallucination in [[anishchenko-2021-hallucination]] — the KL-divergence-against-background objective, the trRosetta oracle, the validation numbers — and then makes the unintended-oligomerization result a load-bearing part of the chapter rather than a footnote. **§5.2** is the former §5 on [[wicky-2022-symmetric-assembly-design]], now framed as *adding a symmetry term to an existing engine and swapping trRosetta for AlphaFold2* rather than as a novel method.

**Why it mattered more than a citation fix.** The previous draft treated Wicky's mass expression failure as a self-contained discovery. With Anishchenko ingested, it reads as a much more severe instance of an already-documented pathology — hallucinated sequences carrying exposed surface hydrophobics learned from native interfaces. The chapter now argues (marked as wiki synthesis) that a cyclic-symmetry objective *rewards* inter-protomer contact and therefore amplifies exactly that tendency; what differs between the two papers is the remedy, manual polar substitution versus wholesale redesign with [[dauparas-2022-proteinmpnn]].

**A second reframing, also marked as synthesis.** The first predictor-inverted generator produced homo-oligomers unprompted, because interface-forming sequence patterns are what it had learned from the PDB. So eliciting an oligomer was never the hard part — *specifying which one* was. That is now the chapter's framing of what Wicky contributed, and it is a sharper claim than the previous "hallucination extended to symmetry".

**Pages touched.** New: [[anishchenko-2021-hallucination]], [[anishchenko-2021-hallucination-supp]]. Revised: [[symmetric-oligomer-design]] (contents, §5 split and rewritten, §7 "rewarded" entry, two new/rewritten Open questions, §12 entry closed, §13 sources, frontmatter 12→13 sources), [[symmetric-assembly-design]] (new "symmetry was a byproduct" paragraph; 9→10 sources), [[wicky-2022-symmetric-assembly-design]] (approach restated as a modification of Anishchenko; new failure-mode note), [[wang-2022-functional-site-scaffolding]] (the three papers as one engine under three losses), [[motif-scaffolding]], [[rfdiffusion]] (lineage), [[overview]] (precursors bullet rewritten; new cross-cutting observation on inherited priors), [[index]] (status, batch 3b, supplements, flagged-reference entry struck through).

**Correcting an earlier session's framing.** The 2026-08-14 chapter draft asserted in Open questions that "the Wicky adversarial-sequence analysis is the only mechanistic failure account in the chapter". That was true only because the wiki was missing Anishchenko; the claim has been replaced rather than merely supplemented, and a new open question added about whether the learned native-interface prior helps or hurts symmetric diffusion.
