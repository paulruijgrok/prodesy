# Prodesy — Index

Catalog of every wiki page. See `CLAUDE.md` for conventions, `overview.md` for the field synthesis, `log.md` for chronology. Pages are Obsidian wikilinks (resolve by basename).

_Last updated: 2026-10-21 — after batch 7b (RFD2, metallohydrolases, the independent enzyme lineage, and de novo antibodies)._

**Status:** v1 · 43 sources + 24 supplements ingested · batches 1 (DL core), 2 (generative-design expansion), 3 (symmetric assembly), 3b (hallucination foundation), 4 (repeat + parametric + RSO), 5 (binder design), 6 (Genie lineage), 7 (enzyme design), 7b (RFD2 + antibodies + independent lineage). Three `topics/` chapters, 10 concepts, 15 tools.

## Overview & meta

- [[overview]] — evolving synthesis of the field
- [[CLAUDE]] — schema & conventions (v1, synced with plasmoDX)
- [[log]] — chronological record

## Topics (chapter-like deep dives)

- [[symmetric-oligomer-design]] — an *Assemblies* chapter: point-group symmetric homo-oligomers from the coiled-coil era to conditional diffusion and back to gradient-based hallucination. Covers the four distinct mechanisms for imposing symmetry (exact-by-construction / rewarded / projected / tied), the specificity axis, the validation ladder, and a flagged-reference list for the pre-2020 history. Promoted from [[symmetric-assembly-design]] on 2026-08-14 at 12 sources; now at 17.
- [[enzyme-design]] — a *Catalysis* chapter: designing proteins that catalyse reactions. Organised around the field's defining barrier — amide-bond hydrolysis, which three independent 2026 campaigns cleared by three different chemistries — and around the diagnosis all of them share: the crystal structures match the design models to ~1 Å and the activity is still 1–4 orders of magnitude below native, because catalysis is a property of a conformational ensemble while design and filtering operate on single structures. Also covers the chapter's most transferable finding, that *what you model is what you get*: including the catalytic water in the filtered complex moved a hit rate from 3/89 to 31/38 at unchanged thresholds. Created 2026-10-21 at 16 sources.
- [[de-novo-binder-design]] — an *Interfaces* chapter: designing a protein to bind a chosen target. Organised around what each generation of method stopped requiring the designer to supply (binding mode → scaffold → chemistry), with the epitope as the one surviving manual input. Covers interface biophysics and hot spots, the four lineages (grafting, filter-first, hotspot-conditioned generation, surface fingerprints), the oracle's failure modes (adversarial overfitting, circularity, gates that deplete the signal they select for), the compute-and-search axis, and a comparability argument for why the field's success rates cannot be placed side by side. Promoted from [[binder-design]] on 2026-10-12 at 24 sources.

**Promotion candidates** (a concept becomes a topic once it has enough material for a self-contained chapter):

- [[structure-prediction]] → a *Foundations* chapter covering the prediction lineages end-to-end (AF2/AF3, RoseTTAFold/RFAA, confidence metrics, their reuse as design oracles). Needs the base RoseTTAFold paper and the prediction-ecosystem batch (ColabFold, Foldseek, lDDT) first.
- [[diffusion-generative-design]] → a *Generative Design* chapter (the largest concept page; already covers four all-atom routes and reads chapter-like).
- ~~[[binder-design]]~~ → **promoted 2026-10-12** to [[de-novo-binder-design]].
- [[sequence-design]] → merges with a future Rosetta/physics-baseline section into a chapter once a Rosetta source is ingested.

## Concepts (reusable ideas)

- [[structure-prediction]] — sequence → 3D; the enabling substrate (4 sources)
- [[sequence-design]] — fixed-backbone / inverse folding (4 sources)
- [[diffusion-generative-design]] — backbone/all-atom generation by denoising (6 sources)
- [[binder-design]] — de novo binders from target structure (24 sources) — **promoted**; full treatment in [[de-novo-binder-design]]
- [[motif-scaffolding]] — building proteins around functional sites (3 sources)
- [[symmetric-assembly-design]] — symmetric homo-oligomers, rings, cages (10 sources) — **promoted**; full treatment in [[symmetric-oligomer-design]]
- [[parametric-design]] — backbones from closed-form geometry; Crick equations (7 sources)
- [[repeat-protein-design]] — tandem modular units; helical symmetry within one chain (4 sources)

## Tools / models

- [[alphafold]] — DeepMind structure predictor & design oracle (AF2, AF3)
- [[rosettafold]] — Baker-lab predictor; RFAA all-atom; backbone for RFdiffusion
- [[rfdiffusion]] — Baker-lab diffusion backbone generator
- [[rfdiffusion3]] — Baker-lab all-atom token+atom generator (efficient)
- [[proteinmpnn]] — Baker-lab sequence design network
- [[chroma]] — Generate Biomedicines programmable diffusion model
- [[protpardelle]] — Huang-lab all-atom (superposition) generative model
- [[ccbuilder]] — Woolfson-lab parametric coiled-coil modelling web app
- [[masif]] — Correia-lab surface-fingerprint framework (site / search / seed)
- [[boltzgen]] — all-atom universal binder generator, modality-specified
- [[complexa]] — Proteína-Complexa; generative prior + test-time search
- [[proteinhunter]] — fine-tuning-free hallucination inside a folding model
- [[bindcraft]] — hallucination against AlphaFold2 — **no primary source ingested**
- [[genie]] — the Genie lineage (1/2/3); SE(3)-equivariant diffusion, now atomistic
- [[rfdiffusion2]] — atomization + unindexed motifs; the generator behind the 2026 enzymes and antibodies

## Papers (source summaries)

### Batch 1 — deep-learning core

- [[jumper-2021-alphafold2]] — AlphaFold2, atomic-accuracy structure prediction · Nature 2021
- [[abramson-2024-alphafold3]] — AlphaFold3, complexes via diffusion · Nature 2024
- [[dauparas-2022-proteinmpnn]] — ProteinMPNN sequence design · Science 2022
- [[watson-2023-rfdiffusion]] — RFdiffusion de novo design · Nature 2023
- [[bennett-2023-binder-design-dl]] — DL-improved binder design · Nat Commun 2023
- [[ingraham-2023-chroma]] — Chroma programmable generative model · Nature 2023
- [[krishna-2024-rosettafold-all-atom]] — RoseTTAFold All-Atom + RFdiffusionAA · Science 2024 *(OCR-recovered)*

### Batch 2 — generative-design expansion

- [[wang-2022-functional-site-scaffolding]] — motif scaffolding by hallucination/inpainting · Science 2022
- [[wicky-2022-symmetric-assembly-design]] — hallucinating symmetric assemblies · Science 2022
- [[vasquez-torres-2023-helical-peptide-binders]] — binders of helical peptide hormones · Nature 2023
- [[chu-2024-protpardelle]] — all-atom generative model (Protpardelle) · PNAS 2024
- [[anand-2022-learned-potential-seqdesign]] — sequence design with a learned potential · Nat Commun 2022
- [[butcher-2025-rfdiffusion3]] — RFdiffusion3 all-atom interaction design · bioRxiv 2025

### Batch 3 — symmetric assembly (the pre-deep-learning history)

Ingested to give [[symmetric-oligomer-design]] primary sources for the parametric and Rosetta eras. All six PDFs were already sitting un-ingested in `sources/`.

- [[harbury-1993-coiled-coil-oligomer-switch]] — oligomeric state switches with core residue geometry · Science 1993
- [[huang-2014-parametric-helical-bundles]] — parametric backbones from the Crick equations · Science 2014
- [[thomson-2014-alpha-helical-barrels]] — designed C5/C6/C7 barrels with defined channels · Science 2014
- [[boyken-2016-hydrogen-bond-network-oligomers]] — HBNet; specificity via buried H-bond networks · Science 2016
- [[luo-2016-protein-assembly-review]] — review; the symmetric-fusion lineage · Chem. Rev. 2016
- [[courbet-2022-axle-rotor-assemblies]] — symmetry-mismatched axle-rotor machines · Science 2022

### Batch 3b — the hallucination foundation (user-supplied, 2026-08-14)

- [[anishchenko-2021-hallucination]] — de novo design by deep network hallucination; the method [[wang-2022-functional-site-scaffolding]] and [[wicky-2022-symmetric-assembly-design]] both build on · Nature 2021

### Batch 4 — repeat proteins, parametric design, relaxed-sequence hallucination (2026-08-24)

- [[brunette-2015-repeat-protein-universe]] — 83 de novo designed helical repeat proteins · Nature 2015
- [[wood-2018-ccbuilder]] — CCBuilder 2.0; parameterization works because coiled coils are repeat proteins · Protein Sci. 2018
- [[yeates-2002-supramolecular-assemblies]] — **review**; first-party account of the nanohedra symmetric-fusion strategy · Curr. Opin. Struct. Biol. 2002
- [[frank-2024-relaxed-sequence-optimization]] — RSO; hallucination by gradient descent in relaxed sequence space, to 1000 aa · Science 2024

### Batch 5 — binder design (2026-10-12)

Ingested to give [[de-novo-binder-design]] its biophysics foundation, an independent methodological lineage, the post-RFD3 frontier, and a first-party comparability source. Five of the seven PDFs were already sitting un-ingested in `sources/`.

- [[halperin-2004-interface-hot-spots]] — hot spots defined by ΔΔG ≥ 1.9 kcal/mol; packing density correlates with binding energy at r² = 0.94 · Structure 2004
- [[gainza-2020-masif]] — MaSIF; molecular surfaces as a learnable, homology-free representation · Nature Methods 2020
- [[gainza-2023-surface-fingerprint-binders]] — MaSIF-seed; the independent binder lineage; nanomolar binders to spike, PD-1, PD-L1, CTLA-4 · Nature 2023
- [[cho-2025-protein-hunter]] — Protein Hunter; fine-tuning-free hallucination inside a diffusion predictor · bioRxiv 2025
- [[stark-2025-boltzgen]] — BoltzGen; universal binder design; 26 targets; 66% against structurally novel targets · bioRxiv 2025
- [[didi-2026-complexa-scaling]] — Proteína-Complexa; generative pretraining + test-time compute; the false dichotomy dissolved · ICLR 2026
- [[ruijgrok-2026-binder-pipeline-comparison]] — **first-party internal report**; nine-pipeline comparison, measured compute, the comparability ledger · 2026

### Batch 6 — the Genie lineage (2026-10-17, completed 2026-10-20)

All three generations from the AlQuraishi lab, now complete. Appendices are inside each PDF, so all three are `supp: no` rather than `missing-requested`.

- [[lin-2023-genie]] — Genie; the forward/reverse asymmetry (Cα point cloud noising, oriented Frenet–Serret frames for generation); 4.1 M parameters against RFdiffusion's 59.8 M · ICML 2023 (PMLR 202) / arXiv:2301.12485
- [[lin-2024-genie2]] — Genie 2; SE(3)-invariant motif conditioning via Cα distance matrices, multi-motif scaffolding as an inference-time choice, and the first protein diffusion model trained on AFDB (588,570 structures) · arXiv:2405.15489
- [[lin-2026-genie3]] — Genie 3; atomistic SE(3)-equivariance via a branched-polymer representation; 10× faster sampling; best on 7 of 10 AlphaProteo binder problems against BindCraft, RFdiffusion, BoltzGen and Proteína-Complexa; a 92 nM Nipah Glycoprotein G binder at a 1/8 hit rate in a blind competition · bioRxiv 2026

**Why 6b mattered.** Three load-bearing elements of the Genie 3 coverage traced to un-ingested predecessors: its frame representation is Genie 2's generalised, its motif selection is "Algorithm 1 of Genie 2", and its entire monomeric training set is Genie 2's. Ingesting the predecessors also revealed that the 256-residue training ceiling runs the whole lineage with a stated computational reason, and surfaced a **1,091-structure discrepancy** in the AFDB dataset count between Genie 2 (588,570) and Genie 3 (587,479).

### Batch 7 — enzyme design (2026-10-21)

The chapter-founding batch for [[enzyme-design]]. Four of the five are from 2026, three published within a week of each other.

- [[durr-2023-metal3d]] — Metal3D; zinc location to 0.70 ± 0.64 Å from a voxelized environment; the p(metal | sequence, structure) objective · *Nat. Commun.* 2023
- [[elnesr-2026-zero-shot-metalloenzyme]] — **Gina El Nesr, Huang lab**; dEVA multi-objective design with no motif template; a binuclear zinc hydrolase at 3 × 10¹³ rate enhancement, the highest reported for a de novo hydrolase; and the desD1 negative control that AlphaFold3 endorsed at pLDDT 86.55 · bioRxiv 2026
- [[choi-2026-cysteine-proteases]] — de novo cysteine proteases; 13/69 = 19%; six crystal structures < 1.2 Å on folds with TM-score < 0.5 to natural proteases; active in mammalian cells; preorganization diagnosed by PLACER · *Nature* 2026
- [[chen-2026-metalloproteases]] — de novo zinc proteases; 36% of 135, concealing a 3/89 vs 31/38 split between two filters; >10⁸-fold acceleration, >10¹⁰ after four substitutions; TDP-43, SAA and Aβ targets; caged cytokines and antagonists · *Nature* 2026
- [[butcher-2026-rfdiffusion3-science]] — **the published RFD3**, reframed around atomic functional site scaffolding; free-atom diffusion; 90% of AME tasks beat RFD2; zero-shot phosphotriesterases with a carbamylated lysine and TTR-cleaving zinc proteases at 56/96 · *Science* 2026

Note that [[butcher-2025-rfdiffusion3]] (the bioRxiv preprint) is **retained alongside** the published version: different title, framing and content. A reconciliation pass is flagged in [[enzyme-design]] §11.

### Batch 7b — RFD2, the ester precedent, the independent lineage, and antibodies (2026-10-21)

Closes two of the wiki's highest-priority gaps and adds the enzyme chapter's first non-Baker-lab source.

- [[ahern-2025-rfdiffusion2]] (+ supp) — **RFdiffusion2**; atomization and unindexed motifs remove inverse-rotamer sampling and sequence-index specification; introduces the AME benchmark and solves **all 41 cases against 16** for prior methods · *Nature Methods* 23, 96–105 (2026)
- [[kim-2026-metallohydrolases]] (+ supp) — RFD2's companion; DFT theozymes; zinc esterases at **53,000 M⁻¹ s⁻¹** against 3–60 for prior designed metallohydrolases; **PLACER validated as a prospective filter** · *Nature* 649, 246–253 (2026)
- [[braun-2026-riff-diff]] (+ supp) — **the independent lineage** (Oberdorfer lab); artificial motif libraries and a deletable placeholder helix built on plain RFdiffusion; retro-aldolases at **290 M⁻¹ s⁻¹ against an evolved enzyme's 320** with **99% ee**; MBHases for a reaction with no natural enzyme · *Nature* 649, 237–245 (2026)
- [[bennett-2026-de-novo-antibodies]] (+ supp) — de novo epitope-specific VHHs, scFvs and IgGs from a fine-tuned RFD2; **0–2% success per target**; cryo-EM confirming **all six CDR loops** · *Nature* 649 (2026)

**Two gaps closed.** RFD2 was the enzyme chapter's highest-priority flagged reference — three ingested papers described its pivotal capability second-hand. The antibody main text turns [[de-novo-binder-design]] §8.2 from a placeholder into a written section.

**Still open on RFD2-MI.** The molecular-interfaces variant used by both 2026 protease campaigns has **no methods paper**: [[choi-2026-cysteine-proteases]] cites a phospho-tyrosine binder preprint for it, [[butcher-2026-rfdiffusion3-science]] cites the metalloprotease preprint. Recorded as a finding rather than a gap.

### Supplements (companion pages)

- [[jumper-2021-alphafold2-supp]] — AF2 SI: Evoformer, IPA, FAPE, confidence, ablations (62 pp)
- [[abramson-2024-alphafold3-supp]] — AF3 SI: tokenization, Pairformer, diffusion module, ranking (45 pp)
- [[dauparas-2022-proteinmpnn-supp]] — ProteinMPNN SI: GNN internals, ablations, pseudocode (25 pp)
- [[watson-2023-rfdiffusion-supp]] — RFdiffusion SI: methods, diffusion math, in silico metrics (129 pp)
- [[bennett-2023-binder-design-dl-supp]] — Bennett SI: metric discrimination, SC50 validation (19 pp)
- [[ingraham-2023-chroma-supp]] — Chroma SI: polymer-prior diffusion theory, conditioners (123 pp)
- [[krishna-2024-rosettafold-all-atom-supp]] — RFAA SI: featurization, RFdiffusionAA protocols (107 pp)
- [[vasquez-torres-2023-helical-peptide-binders-supp]] — SI: yeast display, biosensor assays (32 pp)
- [[chu-2024-protpardelle-supp]] — SI: EM formulation, superposition/collapse, U-ViT (30 pp)
- [[butcher-2025-rfdiffusion3-supp]] — SI: tokenization, DiffusionModule, benchmarks (48 pp)
- [[huang-2014-parametric-helical-bundles-supp]] — SM: the explicit Crick equations, sampling protocol, how symmetry is imposed
- [[courbet-2022-axle-rotor-assemblies-supp]] — SM: parametric sampling ranges, HBNet interfaces, helical-fusion protocols
- [[anishchenko-2021-hallucination-supp]] — SI: SEC screening, the 0217 dimer analysis, surface-redesign rescue, β-sandwich failures, core overpacking
- [[frank-2024-relaxed-sequence-optimization-supp]] — SM: loss weights, ColabDesign calls, tied-logits oligomer protocol, interface filtering cascade
- [[ahern-2025-rfdiffusion2-supp]] — SI (67 pp): the training-example construction algorithm, `P_IS_UNINDEXED` as a sampled augmentation, stochastic centring, crystallisation-additive filtering
- [[kim-2026-metallohydrolases-supp]] — SI (86 pp): an Extended Discussion written as filter-design guidance, a head-to-head of AlphaFold2 vs PLACER vs Chai-1 metrics (Fig. S10), and the same-backbone sequence control (Fig. S11)
- [[braun-2026-riff-diff-supp]] — SI (49 pp): Supplementary Methods for the artificial-motif library and placeholder helix, HPLC enantiomeric-excess determination, and comparison tables of past designed **and evolved** retro-aldolase and MBH rates
- [[bennett-2026-de-novo-antibodies-supp]] — SI (129 pp): the three training datasets (SAbDab, TCR/MHC-peptide, loop-mediated PDB interactions), framework target-templating, and filter calibration — 80.3% within 2 Å at mean pAE < 10 **when 100% of hotspots are satisfied**
- [[butcher-2026-rfdiffusion3-science-supp]] — SM (109 pp): tokenization and indexed/unindexed definitions, training condition probabilities, active-site provenance for the four AME cases, the Dunbrack rotamer probability loss (which excludes Gly/Ala/Pro)
- [[choi-2026-cysteine-proteases-supp]] — SI: Foldseek novelty on the *experimental* structures, the native-protease kinetics benchmark set, and the Ulp1-without-SUMO control
- [[chen-2026-metalloproteases-supp]] — SI (94 pp): the per-state filter thresholds, the Zn(II)-water representation discussion, and two negative results (MPNN substrate-stabilizing residues reduce activity; AF3/MPNN predictability in mutagenesis space)
- [[durr-2023-metal3d-supp]] — SI: dataset stratification by coordination number and occupancy, and a calcium-called-as-zinc false positive at p = 0.9
- [[gainza-2020-masif-supp]] — SI: the geodesic-vs-Euclidean figure, MaSIF-site ROC AUC 0.86, RANSAC alignment protocol, strict TM-score split control, PRISM/transient datasets

## Missing supplements

Batch 1 is complete — all seven main texts have their SI ingested. Outstanding from batch 2 (no `_supp` PDF present in `sources/ProteinDesign/`; all three are *Science* / *Nat Commun* papers that certainly have SI, so these are genuine gaps rather than papers without supplements):

- [[wang-2022-functional-site-scaffolding]] — `supp: missing-requested`
- [[wicky-2022-symmetric-assembly-design]] — `supp: missing-requested`
- [[anand-2022-learned-potential-seqdesign]] — `supp: missing-requested`

From batch 3 (both *Science* papers; in both cases the SI holds the actual method, so these are substantive gaps rather than formalities):

- [[thomson-2014-alpha-helical-barrels]] — `supp: missing-requested`; the SI carries the knowledge-based scoring function and sampling details for the barrels.
- [[boyken-2016-hydrogen-bond-network-oligomers]] — `supp: missing-requested`; the SI carries the HBNet algorithm description and the design scripts.

From batch 4:

- [[brunette-2015-repeat-protein-universe]] — `supp: missing-requested`; the *Nature* Extended Data and Methods hold the in silico filtering criteria and the full DHR table.

From batch 5:

- [[gainza-2023-surface-fingerprint-binders]] — `supp: missing-requested`; the SI holds **Supplementary Table 4** (per-target design and binder counts), Supplementary Figs. 17–22 (seed clustering, SSM data, AF2 comparisons) and the seed-library construction. Without it the one-shot campaign's denominators cannot be stated beyond "top 2,000 per target".
- [[halperin-2004-interface-hot-spots]] — `supp: missing-requested`; the Supplemental Data identifies the 8 alanine-scanned complexes (Table B) and carries the per-residue neighbour and volume data (Appendices C–D). §2 of [[de-novo-binder-design]] rests on a 53-hot-spot sample whose membership the wiki cannot list.

**Two orphaned supplements** — the reverse of the usual problem, where the SI is present and the main text is not:

- **Bennett et al., *Nature* 2025, antibodies with RFdiffusion** — `sources/ProteinDesign/Bennett_Baker_Nature_2025_…_supp.pdf` is present; the main text is absent. §8.2 of [[de-novo-binder-design]] is a placeholder because of this.
- **Rocklin et al., *Science* 2017, massively parallel folding** — `RocklinBaker_Science_2027_sm.pdf` is present (filename year is a typo for 2017); the main text is absent.

*Nice-to-have:* a clean, non-image main PDF for RFAA (current main text is OCR-recovered). The `..._checklist.pdf` beside the RFAA PDFs is a reproducibility checklist, not SI — not ingested.

## Flagged references to add

Specific external references that would close a real gap in an existing page. Supply the PDF into `sources/` and the gap can be filled without resorting to model priors (see the sourcing discipline in `CLAUDE.md`).

- **Base RoseTTAFold (Baek et al., *Science* 2021).** [[rosettafold]] and [[structure-prediction]] both describe the three-track architecture and call it the parallel lineage to AlphaFold, but only the all-atom successor ([[krishna-2024-rosettafold-all-atom]]) is ingested. The foundational claims are currently uncited.
- **A Rosetta design baseline.** [[sequence-design]] characterises classic Rosetta fixed-backbone design as "accurate but slow, with limited success on hard targets" with no ingested source. Candidates already in `sources/`: `Fleischman_Baker_PLoS_2011_RosettaScripts…`, `Huang_Baker_PLOSOne_2011_RosettaRemodel…`.
- **A protein-folding foundation for the "largely solved" framing.** [[structure-prediction]] opens on the folding problem and its resolution. Candidates already in `sources/Proteins/`: `Anfinsen_Science_1973…`, `Baker_Nature_2000_A surprising simplicity to protein folding`.
- **A benchmark/metric reference** for the in silico filters the wiki leans on (lDDT, pLDDT/pAE thresholds) beyond what the SIs state. Candidate already in `sources/ProteinDesign/`: `bioinformatics_2013_lDDT…`.

### For [[symmetric-oligomer-design]] (added 2026-08-14)

The chapter's §12 lists these with full reasoning. Summary — nothing here is currently asserted from model priors; the chapter either cites a review second-hand or leaves the gap open.

- **Padilla, Colovos & Yeates, *PNAS* 2001 — "Nanohedra".** The founding symmetric-fusion paper. *Substantially upgraded 2026-08-24* — [[yeates-2002-supramolecular-assemblies]] is now ingested and gives a first-party account by the same authors, so §2 of the chapter no longer rests on a third party's paraphrase. The primary paper would still add the linker-design details and the full geometric derivation.
- **King et al., *Science* 2012 — self-assembling protein nanomaterials with atomic-level accuracy.** Named as prior art by [[courbet-2022-axle-rotor-assemblies]] ("icosahedral nanocages"); no primary source ingested, so the chapter cannot say how those cages were designed.
- **King et al., *Nature* 2014 — co-assembling multi-component protein nanomaterials.** The two-component branch; needed to close an open question in the chapter.
- **Bale et al., *Science* 2016 — megadalton-scale two-component icosahedral complexes.** The scale demonstration and the bridge to the vaccine-platform framing that [[watson-2023-rfdiffusion]] invokes.
- ~~Anishchenko et al., *Nature* 2021~~ — **supplied and ingested 2026-08-14** as [[anishchenko-2021-hallucination]] (+ [[anishchenko-2021-hallucination-supp]]). The deep-learning side of the chapter's history is now on primary sources; the four entries above are all pre-2020.

**Already in `sources/`, un-ingested, adjacent to the chapter's scope:** `Proteins/Shen_Baker_Science_2018_…self-assembling helical protein filaments` (+supp) — helical rather than point-group symmetry; `Proteins/Brunette_Baker_Nature_2015_…repeat protein universe` — repeat symmetry, relevant to the LRR-like protomers of the giant HAL rings; `ProteinDesign/SchneiderDuhovnik_NAR_2005_PatchDock and SymmDock` — would give the "dock-and-design era" a primary method citation.

### For [[de-novo-binder-design]] (added 2026-10-12)

The chapter's §14 lists these with full reasoning. Nothing in the chapter is asserted from model priors; each entry below is a gap the chapter leaves open or cites second-hand.

**Acquisitions required (not in `sources/`):**

- **BindCraft (Pacesa et al. 2025)** — the most widely used open binder pipeline in practice, and the baseline both [[didi-2026-complexa-scaling]] and [[cho-2025-protein-hunter]] measure themselves against. [[bindcraft]] is entirely secondary-sourced and [[ruijgrok-2026-binder-pipeline-comparison]] carries it at 27% coverage with 16 open questions. **Highest priority.**
- **Fleishman et al., *Science* 2011** — influenza HA binders; the founding de novo binder paper. §3 has no origin without it. *Distinct from* the on-disk `Fleischman_Baker_PloS_2011_RosettaScripts…`.
- **Chevalier et al., *Nature* 2017** — massively parallel minibinder design; the origin of the "minibinder" the chapter discusses throughout.
- **Cao et al., *Nature* 2022** — "Design of protein-binding proteins from the target structure alone"; the direct precursor to [[bennett-2023-binder-design-dl]], cited inside [[stark-2025-boltzgen]].
- **AlphaProteo (DeepMind 2024)** — the other major non-Baker pipeline with published hit rates on shared targets; one of the few remaining cross-method comparison opportunities.
- **Bogan & Thorn** — the "O-ring" account of hot spots and the alanine-scanning database, currently reachable only through [[halperin-2004-interface-hot-spots]].
- **Chao et al., *Nature Protocols* 2006** — yeast surface display; every display-based rate in §12 is in units of an assay no ingested source describes.
- **A source on designed-binder specificity / off-target cross-reactivity** — §13's open question has no literature behind it. This may be a gap in the field rather than in the wiki.

**Already in `sources/`, un-ingested, each closing a named gap:**

- `Proteins/Hoare_2001_Analyzing Kinetic Binding Data` — the kinetics half of §2; every affinity in the chapter is an equilibrium constant.
- `Proteins/Vreden_JMolBiol_2015_…Docking Benchmark v5 / Affinity Benchmark v2`, `Proteins/LiuFan_ScientificData_2024_PPB-Affinity`, `Proteins/LiuWang_Bioinformatics_2014_PDBbind` — would answer §13's benchmark question and are the natural first content for a `benchmarks/` page type.
- `ProteinDesign/QianBaker_bioRxiv_2025_Accelerating protein design by scaling experimental characterization` (+supp) — §12's thesis that the bottleneck moved from generation to characterisation has no source that *states* it.
- `Proteins/PassowFordayce_biorxiv_2026_Amplicon:Protein Bead Display…` — quantitative high-throughput binding measurement.
- `ProteinDesign/ShuarHie_BioRxiv_FAMPNN` — full-atom sequence design, the successor to ProteinMPNN for §9.
- `ProteinDesign/ShuaiGrey_CellSystems_2023_IgLM` — antibody sequence language modelling; would partly mitigate the §8.2 block.
- Scaffold/modality sources for §1 and §8.3: `Proteins/ShaKoide_ProteinScience_2017_Monobodies…`, `Proteins/Koide_Koide_JMB_1998_…fibronectin type III…`, `ProteinDesign/Missonmindrebo_Jardine_PNAS_2023…nanobody…` (+supp), `Proteins/Kubala_Collins_2010_…GFP-nanobody complex`, `Proteins/KeebleHowarth_2019_Approaching infinite affinity`, `Proteins/ZakeriHowarth_2012_SpyTag…`.
- `ProteinDesign/SchneiderDuhovnik_NAR_2005_PatchDock and SymmDock…` — would give the docking application in [[halperin-2004-interface-hot-spots]] a primary method citation.

### For [[enzyme-design]] (added 2026-10-21)

The chapter's §11 gives full reasoning. Nothing in the chapter is asserted from model priors.

**Highest priority — PLACER:**

- **PLACER** — Anishchenko, I. et al. *Modeling protein–small molecule conformational ensembles with PLACER.* **PNAS 122, e2427161122 (2025)**. It carries the preorganization diagnosis in [[choi-2026-cysteine-proteases]] *and* the prospective filtering in [[kim-2026-metallohydrolases]], so it now underwrites two sections of [[enzyme-design]]. Citation identified from Choi's reference list; paper not in `sources/`.

**Closed 2026-10-21:**

- ~~RFdiffusion2~~ — supplied and ingested as [[ahern-2025-rfdiffusion2]]. **RFD2-MI remains unsourced and appears to have no methods paper of its own** (see batch 7b above); recorded as a finding.
- ~~Designed serine hydrolases~~ — citation identified: **Lauko, A. et al., *Computational design of serine hydrolases*, Science 388, eadu2454 (2025)**, from [[butcher-2026-rfdiffusion3-science]]'s reference list. Not yet in `sources/`.
- ~~M-CSA~~ — **Ribeiro, A. J. M. et al., *Nucleic Acids Res.* 46, D618–D623 (2018)**; the AME benchmark is curated from it in [[ahern-2025-rfdiffusion2]].

**Prior art the chapter's framing depends on:**

- **Designed serine hydrolases** — the step [[choi-2026-cysteine-proteases]] positions itself past, and therefore the basis of the claim that amide hydrolysis is the real barrier.
- **The classical Rosetta enzyme-design era** (Kemp eliminases, retro-aldolases, and the directed-evolution campaigns that followed), alluded to by [[elnesr-2026-zero-shot-metalloenzyme]] but otherwise unsupported. Without it §1 has no account of what the field tried for twenty years.

**Tools and databases carrying load without a primary source:**

- **PLACER** — the ensemble predictor behind the entire preorganization analysis in [[choi-2026-cysteine-proteases]], and therefore the chapter's central diagnosis in §5.
- **LigandMPNN** — one of dEVA's two objectives in [[elnesr-2026-zero-shot-metalloenzyme]]; the wiki holds [[dauparas-2022-proteinmpnn]] but not its ligand-aware successor.
- **MAHOMES-II** — the catalytic-metal annotation set Metal3D-Cat is trained on.
- **Mechanism and Catalytic Site Atlas (M-CSA)** — source of the AME benchmark, and the nearest thing enzyme design has to a shared benchmark.
- **Caliby** — the ensemble Potts sequence-design model used to initialise dEVA sequences; also an optional scorer in [[ruijgrok-2026-binder-pipeline-comparison]].

**Missing supplement:** [[elnesr-2026-zero-shot-metalloenzyme]] is `supp: no` — Figs. S1–S24 and Tables S1–S10 are cited throughout but not supplied, so the eight-design characterisation set, the Metal3D-Clean comparison and the kinetics fits cannot be inspected.

**Open housekeeping:** [[butcher-2025-rfdiffusion3]] and [[butcher-2026-rfdiffusion3-science]] are both retained with different titles and framings; a deliberate reconciliation of what the published version dropped, added or revised has not been done.

## Citation-standard audit (2026-08-06)

The review-article citation standard was adopted in the 2026-08-06 schema sync; the pages below predate it. Findings, grouped by kind — **no content was rewritten yet**, this is the approval list.

**A. Numbers stated without a citation at the claim (tool pages).** Every tool page cites its source once in the opening line, then states quantitative results in later paragraphs with no link. Under the standard, each number must carry the wikilink itself. Affected: [[chroma]] ("310 designs experimentally validated; two crystal structures at ~ångström backbone RMSD"), [[proteinmpnn]] ("~52% native sequence recovery vs. ~33% for Rosetta"), [[rfdiffusion3]] ("~10× less compute"), [[rfdiffusion]] (the capabilities list), [[protpardelle]] (superposition/collapse, miniMPNN, U-ViT), [[rosettafold]] (three-track architecture). Fix is mechanical: add the source wikilink to each claim.

**B. Uncited generalisations presented as fact.** ~~[[binder-design]] — "The discipline. Both rely on 'predict-then-order'…" (also stale: "Both" refers to a two-item list that has since grown to five).~~ **Fixed 2026-10-12** on promotion to [[de-novo-binder-design]]; the page was rewritten as a cited lookup entry. [[diffusion-generative-design]] — "Conditioning is the point. The value is steerability…". [[motif-scaffolding]] — "Common pattern. Motif in → scaffold out → sequence with ProteinMPNN → filter with AlphaFold2" (the wikilinks here are navigation, not citations) and the framing claim "the second half of functional de novo design". [[symmetric-assembly-design]] — "Symmetry multiplies a single designed interface into a large ordered assembly, giving access to structures far outside the natural PDB". [[alphafold]] — "the field-defining model and, in practice, the standard design oracle". Fix: cite, or rewrite as explicit synthesis.

**C. Wiki inference not marked as such.** [[overview]] — "a sign the approach is robust rather than a single group's trick"; "Validation discipline is the real unlock"; [[diffusion-generative-design]] — "Different lineages, same conclusion: diffusion works for proteins"; [[structure-prediction]] — "Prediction and design are converging on shared diffusion machinery". These are defensible readings across sources but are phrased as sourced facts. Fix: prefix with "taken together" / "the wiki's reading is…".

**D. Claims with no ingested source at all.** [[structure-prediction]] — "now largely solved for single chains and increasingly for complexes"; the RoseTTAFold three-track description on [[rosettafold]]; the Rosetta baseline characterisation on [[sequence-design]]. These map onto the flagged references above; fix by ingesting a source or moving the claim to Open questions.

**E. Housekeeping.** `updated:` frontmatter on [[structure-prediction]] (2026-07-10) predates batch-2 content added to the page. No page yet carries an *Open questions* section, which the topic template expects.

## Queued (in sources/, not yet ingested)

- ~30 further PDFs in `sources/ProteinDesign/`. **Done in batch 5:** surface-fingerprint design (MaSIF, both papers + supp), Protein Hunter, BoltzGen, Didi test-time compute. **Still queued:** prediction ecosystem (ColabFold, Foldseek, lDDT), antibody design (IgLM; the Bennett antibodies main text must be acquired), FAMPNN / newer sequence design, the benchmark and affinity datasets, Qian 2025 experimental scaling, protein dynamics (Kern), and the field reviews (Listgarten 2026). Several ship with `_supp` files already present — ingest main + companion together.
- `sources/BinderDesignComparison/` — a first-party report directory (markdown, PDF, HTML, sidecar TSVs and the generating code). Ingested as [[ruijgrok-2026-binder-pipeline-comparison]] from the PDF; the three sidecar TSVs (`…_stages.tsv`, `…_compute.tsv`, `…_attributes.tsv`) hold full-width data the report's printed tables narrow, and are not yet mined.
- A large second collection in `sources/Proteins/` — protein biophysics and experimental scaffolds/reagents (folding and stability, coiled coils, LOV/optogenetic domains, nanobodies and monobodies, fluorescent proteins, SpyTag/SpyCatcher and other covalent tags, binding-affinity datasets). Largely untouched; this is the natural source pool for a *Foundations* topic and a *scaffolds-and-reagents* topic.
