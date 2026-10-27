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

## [2026-08-24] ingest | Batch 4 — repeat proteins, parametric design, relaxed-sequence hallucination (4 sources + 1 supplement)

User asked for repeat-protein design and parametric helical-bundle design. Most of the parametric theme was already in from batch 3 (Harbury 1993, Huang 2014 + SI, Thomson 2014), so the batch was scoped to what was genuinely missing, plus two additions the user directed.

**[[brunette-2015-repeat-protein-universe]]** (*Nature* 2015) — 83 de novo designed helical repeat proteins from a helix–loop–helix–loop unit; 53 monomeric and stable at 95 °C, 43 SAXS-consistent, 15 crystal structures at 0.7–2.5 Å. Symmetry is imposed on the *search*: every Monte Carlo move at the equivalent position in each repeat, every substitution applied identically across units. Supplement absent → `missing-requested`.

**[[wood-2018-ccbuilder]]** (*Protein Sci.* 2018) — CCBuilder 2.0. Ingested less for the tool than for its problem statement, which supplies a bridge the wiki was missing: parameterization of a 3D fold is possible **only for repeat proteins**, because a shape built by repeating one rigid-body transform is described by that transform's few parameters. That single claim is why [[parametric-design]] and [[repeat-protein-design]] are two views of one idea. Tool page [[ccbuilder]] added.

**[[yeates-2002-supramolecular-assemblies]]** (*Curr. Opin. Struct. Biol.* 2002) — user-directed, and explicitly noted by them as **a review, not original work**; tagged and framed accordingly. Its value is that it is a review by the *authors of the design it describes*, so the nanohedra account (symmetry-axis geometry, α-helical linker control, the tetrahedral cage of twelve 49 kDa bromoperoxidase/M1 subunits) is first-party rather than third-party paraphrase.

**[[frank-2024-relaxed-sequence-optimization]]** + **[[frank-2024-relaxed-sequence-optimization-supp]]** (*Science* 2024) — user-supplied. RSO: hallucination by gradient descent through AF2 in a **relaxed** (continuous, PSSM-like) sequence space, staying non-discrete during optimization and handing only the backbone to ProteinMPNN. Scales to 1000-residue single chains (median TM 0.89) where RFdiffusion struggles past ~600; >100 proteins characterized, 3 crystal structures, 2 cryo-EM maps.

New concept pages: [[parametric-design]], [[repeat-protein-design]]. New tool page: [[ccbuilder]]. Wiki now: 24 sources + 14 supplements, 8 concepts, 8 tools, 1 topic.

## [2026-08-24] revise | symmetric-oligomer-design — a fourth mechanism, a first-party §2, and a sharper failure diagnosis

**Three substantive changes, not just added citations.**

**1. A fourth way to impose symmetry.** The chapter's organising claim was that symmetry has been imposed three ways — exact by construction, rewarded, projected. [[frank-2024-relaxed-sequence-optimization-supp]] forces a fourth: ColabDesign's `copies` option **copies the input logits** across protomers with a residue-index shift of 50, then adds interface pAE and contact losses. That splits what the other three bundle: *sequence* symmetry is exact by construction (the protomers are literally one optimization variable) while *interface geometry* is rewarded. §7 retitled "Four ways…", the opening thesis amended, and the new mechanism related to the tied-position decoding of [[dauparas-2022-proteinmpnn-supp]].

**2. §2 is no longer second-hand.** The symmetric-fusion origin was previously reachable only through [[luo-2016-protein-assembly-review]]. It now rests on [[yeates-2002-supramolecular-assemblies]], with Luo retained only for the post-2002 extensions it actually covers (the KDPGal–FkpA cube, symmetry-matching fusions). Flagged reference #1 downgraded from "highest value on this list" to "substantially upgraded"; #2 (the crystallographically resolved 12-subunit cage) is now the most valuable outstanding item.

**3. The adversarial-sequence diagnosis sharpened again.** §8 previously ended on Wicky's overfitting account, extended on 2026-08-14 by Anishchenko's surface-hydrophobics account. [[frank-2024-relaxed-sequence-optimization]] ran the controlled version — its own relaxed sequences, used directly, still failed experimentally despite improved in silico scores — and names the cause as **AF2's high tolerance to mutation**, which limits its ability to separate valid from adversarial sequences. The chapter now argues that this is a better account than "overfitting": the oracle is not fooled so much as insensitive in the direction that matters, so an optimizer that only queries the oracle has no gradient toward biophysical realism.

**A third sighting of the same bias.** Frank's heterodimers designed *without* the homo-oligomer filter independently formed homo-oligomers. With [[anishchenko-2021-hallucination]] and [[wicky-2022-symmetric-assembly-design]] that makes three independent observations, now stated as a chapter-level reading in §10: self-association is the default output of a PDB-trained generator, and every method in the chapter is a way of *aiming* a propensity that is already there.

**Also.** §2 gains the repeat-protein basis of parametric design and the Brunette DHR library; §4 notes that Courbet's axle-rotor components *are* DHRs, making [[repeat-protein-design]] upstream of point-group assembly design; §10 retitled "After RFdiffusion — and the return of hallucination"; two new Open questions (whether the gradient route reaches the cubic groups; whether size scaling in chain *length* implies scaling in chain *count*). Chapter frontmatter 13 → 17 sources.

**Pages touched.** New: the four batch-4 paper pages, one supplement, [[parametric-design]], [[repeat-protein-design]], [[ccbuilder]]. Revised: [[symmetric-oligomer-design]], [[index]], [[overview]], [[symmetric-assembly-design]], [[diffusion-generative-design]], [[anishchenko-2021-hallucination]], [[rfdiffusion]], `book/glossary.md`.

## [2026-08-24] lint | Duplicate PDFs in sources/Proteins

Noted while surveying, not yet acted on — `sources/` is immutable by convention, so this is a report rather than a fix. Same paper present twice under different filenames: `Huang_Baker_PLOSOne_2011_v6_pe24109_RosettaRemodel.PDF` / `Huang_Baker_POne_2011_0024109__RosettaRemodel-…`; `Conrad_Crane_NatBioChem_2014…` / `Conrad_Crane_NatureChemBiol_2014…`; `Yao_Gardner_NatChemBiol_2008…` / `Yao_Gardner_NatureChemBiol_2008…`; `Ashkenazy_BenTal_NuclAcidRes_2016…` (one copy lacking a `.pdf` extension); `Zayner_Sosnick_BiophysJ_2013…` / `…_withSupp`. Also `HenzlerWildManKern_Nature_2007_Intrinsic motions…` and `HenzlerWildmannKern_Nature_2007_Dynamic personalities…` are *different* papers with near-identical filename stems — worth care when citing.

## [2026-10-12] ingest | Batch 5 — binder design (6 sources + 1 supplement + 1 first-party report)

**Trigger.** User asked to restart development of a full chapter on binder design, and supplied a new first-party source: a nine-pipeline comparison report generated in the sibling `dx_binder_design` project, dropped into `sources/BinderDesignComparison/`.

**Ingested.**

- [[ruijgrok-2026-binder-pipeline-comparison]] — the supplied report. Internal, not peer-reviewed, but citable under the schema because every qualitative claim carries a source column pointing at the config or source file it was read from, and every compute figure is derived from Slurm accounting rather than from a journal. Nine pipelines across three kinds (generative / evaluation-only / planned), measured compute (21,707 tasks, 10,376.1 GPU-hours, 303.7 of them charged to failed tasks), a stage-by-stage audit of atomic representation, and a comparability ledger.
- [[halperin-2004-interface-hot-spots]] — closes the wiki's largest conceptual gap. "Hotspot" was used on four pages and defined on none. Supplies the ΔΔG ≥ 1.9 kcal/mol definition and the r² = 0.94 correlation between occupied volume and binding energy.
- [[gainza-2020-masif]] (+ [[gainza-2020-masif-supp]]) and [[gainza-2023-surface-fingerprint-binders]] — the surface-fingerprint lineage; the only non-Baker-lab de novo binder stack in the wiki.
- [[cho-2025-protein-hunter]], [[stark-2025-boltzgen]], [[didi-2026-complexa-scaling]] — the post-RFD3 frontier: fine-tuning-free hallucination, modality-specified universal design, and generative pretraining plus test-time compute.

All seven PDFs except the Bennett 2025 antibody main text were already sitting un-ingested in `sources/`; six were flagged as Tier-1 gaps by the survey of 2026-10-11.

**New pages.** `topics/de-novo-binder-design.md` (the chapter, 15 sections). Tools: [[masif]], [[boltzgen]], [[complexa]], [[proteinhunter]], [[bindcraft]].

**Touched.** [[binder-design]] (demoted to a lookup page), [[watson-2023-rfdiffusion]] and [[vasquez-torres-2023-helical-peptide-binders]] (deepened, see the revise entry below), [[index]], [[overview]], `book/build_book.py` (PART_LAYOUT key).

**Three contradictions recorded rather than resolved**, per the schema's instruction to note them explicitly:

1. [[didi-2026-complexa-scaling]] concludes that Complexa's self-generated sequences make ProteinMPNN redesign unnecessary; [[ruijgrok-2026-binder-pipeline-comparison]] finds the co-designed sequence unusable on PfLDH because of antigen copying (48 contiguous target residues in a 79-mer, ρ +0.54 with the reward) and computes the project's headline on MPNN redesigns instead. Same model, opposite conclusion. Treated in the chapter as a benchmark-versus-operation gap, not adjudicated.
2. The same paper states RFdiffusion and Protpardelle generate backbones only; the comparison report records RFD3 output as observed all-atom at 6.4 atoms/residue — while noting RFD3's own QC comments call it backbone-only. Unresolved in both sources.
3. [[stark-2025-boltzgen]] reports binders for "14 of 28" tested disulfide-bonded designs in its summary and 14 of 24 in its §2.6.

## [2026-10-12] revise | Concept promoted: binder-design → topics/de-novo-binder-design

**What changed.** `concepts/binder-design.md` (1,985 bytes, 5 sources) became a short cited lookup page; the full treatment is the new chapter [[de-novo-binder-design]] at 24 sources.

**Why the topic is not named `binder-design`.** `build_book.py` keys topics, concepts and tools by basename into one anchor map (line 134), so a `binder-design.md` in both `topics/` and `concepts/` would emit two chapters sharing the `{#binder-design}` anchor and make every inbound wikilink ambiguous. Followed the precedent set on 2026-08-14, where the concept [[symmetric-assembly-design]] was kept and the chapter took the distinct name [[symmetric-oligomer-design]]. `PART_LAYOUT` was updated from `binder-design` to `de-novo-binder-design`; the reserved `interface-design` slot is left in place and is still empty.

**Defect fixed in passing.** The 2026-08-06 citation audit, item B, flagged the concept page's closing paragraph — "**The discipline.** Both rely on 'predict-then-order'…" — as both uncited and stale, "Both" referring to a two-item list that had grown to five. That paragraph is gone; the replacement page cites every claim. Audit item B updated in [[index]].

**Chapter framing.** Organised around what each generation of method stopped requiring the designer to supply — binding mode, then scaffold, then chemistry — with the epitope as the one surviving manual input, and with a second argument running throughout: the field's reported success rates are fractions of different denominators measured by different assays against different bars, and the chapter states each in its own units rather than averaging them. §14 carries the flagged-reference list, mirrored into [[index]].

**Known incomplete.** §8.2 (antibodies and CDR loops) is a placeholder, because `sources/ProteinDesign/` holds the Bennett 2025 antibody **supplement** and not its main text. Writing that section from an SI alone would not meet the citation standard.

## [2026-10-12] revise | watson-2023-rfdiffusion and vasquez-torres-2023 deepened with their binder numbers

**Own the error.** Both pages were written in July 2026 at concept-page granularity and then cited as if they carried evidence. `watson-2023-rfdiffusion.md` asserted "state-of-the-art on … de novo binder design" with **no binder figure of any kind**, and `vasquez-torres-2023-helical-peptide-binders.md` claimed "high-affinity, high-specificity binders" with no affinity, no count and no denominator. Under the review-article citation standard those were defects, and any chapter sentence resting on them would have been uncitable.

**What was added.** For Watson: the hotspot / secondary-structure / block-adjacency conditioning and the separate PPI fine-tune; the five targets and 95 designs per target; the 19% BLI success rate at 10 µM with its ≥50%-of-positive-control bar and the two-orders-of-magnitude comparison to Rosetta; ~30 nM HA and IL-7Rα binders; and the p53/MDM2 arm (55/95 binding, 0.5 and 0.7 nM against 600 nM native, +31% interface area). For Vázquez Torres: the three-generation affinity ladder (8/12 at micromolar parametric → 44/192 and 6.1 nM inpainted → 2.7 nM secretin and 7 nM Bid de novo), the partial-diffusion results (25/96 and 20/96; 5.6 nM NPY, picomolar GCG), two crystal structures at 1.95 and 1.81 Å, the Bim binder below 500 pM, and the lucCagePTH biosensor at a 10 nM limit of detection with serum mass-spec enrichment. Both pages gained an `updated:` field.

**One control worth flagging** from the Vázquez Torres extraction, because it cuts against a common assumption: ProteinMPNN redesign of the *original* interface did not measurably improve affinity. The three-orders-of-magnitude gain came from extending the interface, not from better sequence design.

## [2026-10-12] lint | Two filing errors in sources/

- `ProteinDesign/GainzaCorreia_NatureMethods_2023_…` is *Nature Methods* **17**, 184–192, February 2020 (online 9 December 2019; DOI 10.1038/s41592-019-0666-6). The filename year is wrong by three years. The page is filed as [[gainza-2020-masif]], following the publication year; the PDF was left untouched, since `sources/` is immutable.
- `ProteinDesign/RocklinBaker_Science_2027_sm.pdf` — the year is a typo for 2017 (*Science* **357**, 168). Also note this file is the supplementary materials only; the main text is absent.

## [2026-10-17] ingest | Batch 6 — Genie 3 (1 source)

**Trigger.** User supplied `sources/ProteinDesign/LinAlqurashi_bioRxiv2026_…Genie 3.pdf` and asked, specifically, whether any training structures exceed 256 residues.

**Answer to the question, since it is the kind of thing that should survive in the record: no.** Both training datasets are capped at 256 residues. Monomeric/motif-scaffolding data is the Genie 2 dataset — FoldSeek-clustered AFDB representative clusters filtered to **20–256 residues inclusive** at pLDDT ≥ 80, giving 587,479 structures, with no experimentally determined monomeric structures used at all. Multimeric/binder data is the Pinder 2024-02 training split with missing-atom structures removed and **the whole complex capped at 256 residues**, giving 135,745 structures across 5,331 interface clusters — so the cap covers target plus binder together, putting individual chains well below 256. The main text states the consequence twice, in both cases using the ceiling as evidence of out-of-domain generalisation. One residue of ambiguity recorded: Appendix A.3.2 says the complex cap is "to 256" (inclusive) while §4.4 says "shorter than 256".

**Ingested as** [[lin-2026-genie3]]. `supp: no` — Appendices A–E are inside the same 48-page PDF, so this is not a `missing-requested` case.

**New page.** Tool [[genie]].

**Why this source matters more than its page count suggests.** It reverses two recent consensus positions at once — it keeps SE(3)-equivariance where the all-atom literature abandoned it, reaching atomistic detail through a branched-polymer frame construction with partial atomization; and it beats hallucination with plain generation, best on 7 of 10 AlphaProteo problems against BindCraft, RFdiffusion, BoltzGen and Proteína-Complexa at a fixed 200-structure budget, with the margin widening under runtime normalisation. It is also the wiki's first five-method, one-protocol, fixed-budget binder comparison, which is the nearest thing to the cross-method benchmark [[de-novo-binder-design]] §12 argues does not exist.

**Touched.** [[de-novo-binder-design]] — §5 gained the hotspot-compliance contrast between generation and hallucination plus the extended/convergent hotspot heuristics; §7 gained the SE(3)-equivariant fourth route to all-atom design; §10 gained the 12% oracle-precision ceiling and the off-target-passing finding that produced the AF2M+ constraint; §11 gained Genie 3 as a third answer to the generative/hallucination question and a revised wiki reading; §12.2 gained two rows and §12.3 a named partial counterexample; §13 gained two open questions (how far a 256-residue ceiling generalises, and whether dropping equivariance was a mistake); §14's BindCraft entry updated. Also [[binder-design]], [[bindcraft]], [[complexa]], [[boltzgen]], [[index]], [[overview]].

**A third-party result on a standing contradiction.** The 2026-10-12 log entry recorded [[didi-2026-complexa-scaling]] and [[ruijgrok-2026-binder-pipeline-comparison]] disagreeing on whether Complexa's co-designed sequences make ProteinMPNN redesign unnecessary. [[lin-2026-genie3]] now reports independently that without inference-time search, Complexa "performs better using ProteinMPNN-based sequence redesign than using its own sequence co-generation feature" — siding with the operational finding against the paper's own conclusion. Recorded on [[complexa]]; the open question in §13 stands, but it is now two sources to one.

## [2026-10-20] ingest | Batch 6b — Genie 1 and Genie 2 (2 sources)

**Trigger.** User asked for the Genie 1 reference, then supplied both predecessor PDFs after the answer surfaced that neither was in `sources/`.

**References, for the record.** Genie 1: Lin, Y. & AlQuraishi, M. *Generating Novel, Designable, and Diverse Protein Structures by Equivariantly Diffusing Oriented Residue Clouds.* ICML 2023, PMLR 202; preprint arXiv:2301.12485. Genie 2: Lin, Y., Lee, M., Zhang, Z. & AlQuraishi, M. *Out of Many, One: Designing and Scaffolding Proteins at the Scale of the Structural Universe with Genie 2.* arXiv:2405.15489, 2024. Both `supp: no` — appendices are inside the respective PDFs.

**Ingested as** [[lin-2023-genie]] and [[lin-2024-genie2]].

**Why these were worth ingesting rather than leaving as lineage citations.** Three load-bearing elements of the [[lin-2026-genie3]] coverage traced to an un-ingested predecessor: Genie 3's frame representation is described as Genie 2's "generalised to the branched polymer nature of proteins", its motif selection is "the same motif selection algorithm detailed in Algorithm 1 of Genie 2", and its entire monomeric training set is Genie 2's. The wiki was describing Genie 3's representation and training data through a paper that defers to a source we did not hold.

**What ingesting them changed, beyond filling the citation.**

1. **The 256-residue ceiling runs the whole lineage, and now has a reason.** [[lin-2023-genie]] trained its long models at a 256 maximum (SCOPe 8,766 domains, 7,249 of them ≤256; AlphaFold-SwissProt at pLDDT > 80, 195,214 structures all ≤256). [[lin-2024-genie2]] states the cause outright — "due to computational constraints, we limit sequence length to 256 during training; however, Genie 2 is capable of generating proteins longer than 256 residues" — and attributes it to the O(N³) triangular multiplicative update layers inherited from AlphaFold2. So the out-of-domain generalisation claim the user asked about last session is the **third iteration of a standing house argument**, not a Genie 3 finding. §13 of [[de-novo-binder-design]] updated to say so.
2. **Genie 3's headline efficiency gain is an answer to a self-stated limitation.** Genie 2 reported needing 1,000 denoising iterations against 100 for FrameFlow, 500 for Chroma and 50 for RFdiffusion, and named sampling efficiency as future work. Genie 3's 1,000→100 step reduction is that future work, which the Genie 3 page alone did not convey.
3. **A dataset discrepancy across the lineage.** [[lin-2024-genie2]] reports **588,570** AFDB structures; [[lin-2026-genie3]] describes "the same training dataset as Genie 2" and gives **587,479**. A difference of 1,091 structures (0.19%), unexplained in either paper. Recorded on all three pages and on [[genie]].
4. **A third independent arrival at protein diffusion.** [[overview]]'s cross-cutting note that RFdiffusion and [[ingraham-2023-chroma]] arrived separately now has a third case with a fourth mechanism, and the only end-to-end SE(3)-equivariant one — at 4.1 M parameters against RFdiffusion's 59.8 M.
5. **Synthetic-structure training as a settled direction.** Genie 2 was "the first protein diffusion model to train on AFDB", and the designability/diversity/novelty gains it reports are the wiki's cleanest demonstration that predicted structures work as training data. Added to [[overview]] alongside [[didi-2026-complexa-scaling]]'s Teddymer, with the open question of where the ceiling is — [[lin-2026-genie3]] uses no experimentally determined monomeric structures at all.
6. **A metric argument worth reusing.** [[lin-2024-genie2]] rejects success rate for motif scaffolding because mode collapse inflates it, and reports **unique successes** after TM-score 0.6 clustering. It also notes that designability alone can be gamed by mode collapse and that diversity is sample-size dependent. This is the same class of reasoning as the comparability ledger in [[ruijgrok-2026-binder-pipeline-comparison]], arriving from the methods side.

**Touched.** [[genie]] (rewritten with a three-generation table and lineage results), [[lin-2026-genie3]] (lineage citations now resolve), [[de-novo-binder-design]] §7, §13 and §15, [[binder-design]], [[diffusion-generative-design]], [[motif-scaffolding]], [[index]], [[overview]].

**Note on scope.** Neither predecessor has binder capability — that is what Genie 3 adds — so both enter [[de-novo-binder-design]] as lineage and method provenance rather than as binder results. Genie 2's PD-1 and IL-2Rβγc/IL-2Rα multi-motif tasks are scaffolding problems posed on binder targets, not binder design.

## [2026-10-21] ingest | Batch 7 — enzyme design (5 sources + 4 supplements)

**Trigger.** User asked to ingest the RFD3 papers and the new enzyme-design papers (cysteine proteases, metalloproteases, "Gina's preprint") and to prepare a chapter on enzyme design. "Gina's preprint" resolved to `ElNesrHuang_biorxvi_2026.04.23_Zero-shot design of a de novo metalloenzyme.pdf` — Gina El Nesr, Huang lab — found by scanning author lists rather than filenames.

**Ingested.**

- [[butcher-2026-rfdiffusion3-science]] (+ [[butcher-2026-rfdiffusion3-science-supp]]) — the **published** RFD3, *Science* 2026, retitled "Atomic functional site scaffolding in biopolymers". Free-atom diffusion; beats RFD2 on 37/41 AME tasks; zero-shot phosphotriesterases with a carbamylated lysine bridging two metals and TTR-cleaving zinc proteases at 56/96 in cis.
- [[choi-2026-cysteine-proteases]] (+ supp) — *Nature* 2026. 13/69 = 19%; k_cat/k_uncat to 3 × 10⁷ pre-optimisation and 1.8 × 10⁹ for Dokki-v2; six crystal structures < 1.2 Å on folds at TM-score < 0.5 to natural proteases; active in mammalian cells.
- [[chen-2026-metalloproteases]] (+ supp) — *Nature* 2026. 36% of 135; >10⁸-fold, >10¹⁰ after four substitutions; TDP-43, SAA and Aβ targets; caged cytokines and an EGFR antagonist.
- [[elnesr-2026-zero-shot-metalloenzyme]] — bioRxiv 2026, Huang lab with Rothlisberger and SLAC. dEVA multi-objective design; binuclear zinc hydrolase at 3 × 10¹³ rate enhancement.
- [[durr-2023-metal3d]] (+ supp) — *Nat. Commun.* 2023, the metal-location predictor dEVA is built on.

**New pages.** `topics/enzyme-design.md` (12 sections), concepts [[catalytic-site-design]] and [[metalloprotein-design]]. `PART_LAYOUT` gained a **Catalysis** part.

**Decision recorded: both RFD3 papers retained.** [[butcher-2025-rfdiffusion3]] (bioRxiv, "De novo Design of All-atom Biomolecular Interactions") and [[butcher-2026-rfdiffusion3-science]] (Science, "Atomic functional site scaffolding in biopolymers") differ in title, framing and content — the published version carries experimental enzyme campaigns the preprint lacks, and a 109-page rather than 48-page supplement. Treating them as one source would lose material either way. The preprint page remains the source for the benchmark suite and the efficiency claim; the published page is authoritative for everything experimental. A deliberate reconciliation pass is flagged in [[enzyme-design]] §11 and [[index]].

**Three findings that shaped the chapter rather than just filling it.**

1. **The hit rate is set by what is modelled, not by the thresholds.** [[chen-2026-metalloproteases]] ran two filtering strategies differing only in whether the **catalytic water** was present in the modelled enzyme–substrate complex: **3/89 versus 31/38** at one hour, same generator, same designers, and — per [[chen-2026-metalloproteases-supp]] — the same numerical filter thresholds. The published 36% headline pools the two arms, so it simultaneously understates the better filter and overstates the worse one. This is the enzyme analogue of the binder chapter's "the filter sets the hit rate", but more specific: it names *what* the better filter knows.
2. **A confident oracle endorsing a physically impossible site.** [[elnesr-2026-zero-shot-metalloenzyme]] published its own negative control: desD1, with a single coordinating ligand, binds no zinc by two assays — and AlphaFold3 assigned the metal **pLDDT 86.55**, placing it exactly as designed. The authors' own sentence: "By standard computational metrics and filtering criteria, this design would have been classified as a success." Traced to crystallisation-additive zinc sites in the Metal3D/LigandMPNN training corpora, and acted on by retraining Metal3D-Clean. Added as a fifth oracle-failure mode in [[enzyme-design]] §6, alongside the four catalogued in [[de-novo-binder-design]] §10.
3. **Preorganization is the convergent diagnosis.** All three protease campaigns report crystal structures matching design models to ~1 Å and activities 1–4 orders of magnitude below native. [[choi-2026-cysteine-proteases]] supplies the mechanism via PLACER ensembles — a non-productive His45/Ser44 interaction suppressed by S44V, with the **fraction of productive conformations tracking activity across the series**. The chapter's thesis follows: designs optimise a single structure while catalysis depends on a distribution. Marked as the wiki's synthesis, with the experiment that would test it recorded in §10.

**Also recorded:** a second hypothesis about the origin of catalytic competence. [[elnesr-2026-zero-shot-metalloenzyme]] rejects motif scaffolding on the grounds that "optimizing for the motif alone does not guarantee catalytic competence" and optimises the coordination sphere instead, arriving at a binuclear zinc site nature uses without being shown one. On n = 3 Pareto-optimal designs, so weighed carefully in §7 — but it holds the highest rate enhancement in the chapter.

**Two senses of "zero-shot" now in circulation** and kept apart in the chapter: no experimental optimisation ([[butcher-2026-rfdiffusion3-science]]) versus no template, predictor or evolutionary information ([[elnesr-2026-zero-shot-metalloenzyme]]).

**Touched.** [[index]], [[overview]], [[motif-scaffolding]], [[diffusion-generative-design]], `book/build_book.py`.

## [2026-10-21] ingest | Batch 7b — RFD2, metallohydrolases, the independent lineage, and de novo antibodies (4 sources + 4 supplements)

**Trigger.** User asked for the RFD2 and PLACER references, then supplied the Oberdorfer and Kim papers, the de novo antibody paper — and, unprompted, **RFdiffusion2 itself**, which was the enzyme chapter's highest-priority flagged reference.

**Ingested.** [[ahern-2025-rfdiffusion2]], [[kim-2026-metallohydrolases]], [[braun-2026-riff-diff]], [[bennett-2026-de-novo-antibodies]], each with its supplement.

**Two flagged gaps closed.**

1. **RFD2 is now primary.** [[enzyme-design]] §3 was rewritten around [[ahern-2025-rfdiffusion2]] rather than describing its capability through three papers that merely used it. The mechanism it names is the chapter's hinge: prior motif scaffolding used **indexed backbone frames**, requiring a prespecified sequence index per motif residue, which is adequate for a contiguous domain and wrong for a theozyme — forcing inverse rotamer sampling as a workaround. RFD2 answers with **atomization** (residues as frames *or* heavy atoms, so rotamers are inferred) and **unindexed residues** (position withheld; the network learns with no auxiliary loss to superimpose them onto generated residues). It solves **all 41 AME cases against 16** for prior methods, and it introduced that benchmark. The supplement shows unindexing is a sampled training augmentation (`P_IS_UNINDEXED`), not an inference device.
2. **§8.2 of [[de-novo-binder-design]] is written.** The antibody placeholder is replaced by a full section. The number that matters: **0–2% success per target** against 19% for miniprotein design from the same lab, which is the clearest measure in the wiki of what the antibody format costs.

**One gap re-characterised rather than closed.** **RFD2-MI**, the molecular-interfaces variant both 2026 protease campaigns depend on, has no methods paper: [[choi-2026-cysteine-proteases]] cites Bauer et al. (phospho-tyrosine peptide binders, bioRxiv 2025.09.29.678898) while [[butcher-2026-rfdiffusion3-science]] cites the metalloprotease preprint for the same thing. Recorded as a finding — the variant is described only in passing by its applications.

**Three findings that changed the enzyme chapter's argument, not just its coverage.**

1. **A new §4b, and a reframed ceiling.** [[braun-2026-riff-diff]] is the chapter's first non-Baker-lab source, and it is the only case where two independent pipelines attack the *same* theozyme — the RA95.5-8F retroaldolase tetrad. Riff-Diff reaches **290 M⁻¹ s⁻¹ from 36 designs** against RFD2's **6.34 M⁻¹ s⁻¹ from 96**, approaching the extensively evolved RA95.5-5 at 320, with **99% ee** and six high-resolution structures. §5's diagnosis — a 1–4 order-of-magnitude gap from imperfect preorganization — holds across the Baker-lab campaigns, but this result says the ceiling is a pipeline property rather than a method property. Added as an open question, and the chapter no longer asserts the gap as general.
2. **PLACER has been used prospectively, and validated retrospectively.** [[kim-2026-metallohydrolases]] filtered on PLACER ensembles, ranked its best design first, and then expressed **seven same-backbone designs it had rejected for suboptimal PLACER metrics** and found them inactive. §6 previously argued that *what you model* sets the hit rate; it can now also say that the **ensemble is filterable**, demonstrated once. The §10 open question was narrowed accordingly — what is still missing is a split-arm comparison of ensemble versus single-structure filtering within one campaign.
3. **The ester/amide gap is now sized.** [[kim-2026-metallohydrolases]] reaches 53,000 M⁻¹ s⁻¹ on an ester; [[choi-2026-cysteine-proteases]] reaches 413 M⁻¹ s⁻¹ on an amide. Roughly two orders of magnitude, attributable to substrate rather than to method — which is what makes the 2026 protease papers' framing of amide hydrolysis as *the* barrier quantitative rather than rhetorical.

**Two engineering details worth preserving.** Kim's design uses **Zn(II) itself as the oxyanion hole**, with no nearby side-chain hydrogen-bond donors, sidestepping the many-body buried-polar problem that [[choi-2026-cysteine-proteases]] struggles with. And Ahern's cysteine esterase includes backbone atoms specifically to **force a helix terminus whose dipole stabilises the oxyanion hole** — a designed second-shell electrostatic effect, which is a direct counterexample to [[elnesr-2026-zero-shot-metalloenzyme]]'s claim that motif scaffolding neglects the second shell. Both the criticism and its counterexample are now in the chapter.

**New page.** Tool [[rfdiffusion2]].

**Touched.** [[enzyme-design]] (§3 rewritten, new §4b, §6 extended, three new open questions, §11 updated), [[de-novo-binder-design]] (§8.2 written, §12.2 table, §9 specificity question revised), [[catalytic-site-design]], [[metalloprotein-design]], [[motif-scaffolding]], [[binder-design]], [[index]], [[overview]].

## [2026-10-21] lint | Superseded antibody supplement in sources/

`ProteinDesign/Bennett_Baker_Nature_2025_Atomically accurate de novo design of antibodies with RFdiffusion_supp.pdf` is a pre-publication copy of the supplement for what is now [[bennett-2026-de-novo-antibodies]], whose 2026 main text and supplement are both present. The 2025 file is superseded. Flagged rather than removed, since `sources/` is immutable. This also resolves the "two orphaned supplements" note recorded on 2026-10-12; **Rocklin 2017 remains orphaned** (`RocklinBaker_Science_2027_sm.pdf`, main text absent, filename year a typo for 2017).
