# Prodesy — Index

Catalog of every wiki page. See `CLAUDE.md` for conventions, `overview.md` for the field synthesis, `log.md` for chronology. Pages are Obsidian wikilinks (resolve by basename).

_Last updated: 2026-08-14 — after batch 3 (symmetric assembly), the first `topics/` chapter, and the Anishchenko hallucination ingest._

**Status:** v1 · 20 sources + 13 supplements ingested · batch 1 (DL core) + batch 2 (generative-design expansion) + batch 3 (symmetric assembly). `topics/` now has its first chapter.

## Overview & meta

- [[overview]] — evolving synthesis of the field
- [[CLAUDE]] — schema & conventions (v1, synced with plasmoDX)
- [[log]] — chronological record

## Topics (chapter-like deep dives)

- [[symmetric-oligomer-design]] — an *Assemblies* chapter: point-group symmetric homo-oligomers from the coiled-coil era to conditional diffusion. Covers the three distinct mechanisms for imposing symmetry (exact-by-construction / rewarded / projected), the specificity axis, the validation ladder, and a flagged-reference list for the pre-2020 history. Promoted from [[symmetric-assembly-design]] in the 2026-08-14 batch-3 ingest, which took the page from 2 sources to 12.

**Promotion candidates** (a concept becomes a topic once it has enough material for a self-contained chapter):

- [[structure-prediction]] → a *Foundations* chapter covering the prediction lineages end-to-end (AF2/AF3, RoseTTAFold/RFAA, confidence metrics, their reuse as design oracles). Needs the base RoseTTAFold paper and the prediction-ecosystem batch (ColabFold, Foldseek, lDDT) first.
- [[diffusion-generative-design]] → a *Generative Design* chapter (the largest concept page; already covers four all-atom routes and reads chapter-like).
- [[binder-design]] → an *Interfaces* chapter (five sources, a clear historical progression, and the strongest wet-lab validation thread in the wiki).
- [[sequence-design]] → merges with a future Rosetta/physics-baseline section into a chapter once a Rosetta source is ingested.

## Concepts (reusable ideas)

- [[structure-prediction]] — sequence → 3D; the enabling substrate (4 sources)
- [[sequence-design]] — fixed-backbone / inverse folding (4 sources)
- [[diffusion-generative-design]] — backbone/all-atom generation by denoising (6 sources)
- [[binder-design]] — de novo binders from target structure (5 sources)
- [[motif-scaffolding]] — building proteins around functional sites (3 sources)
- [[symmetric-assembly-design]] — symmetric homo-oligomers, rings, cages (9 sources) — **promoted**; full treatment in [[symmetric-oligomer-design]]

## Tools / models

- [[alphafold]] — DeepMind structure predictor & design oracle (AF2, AF3)
- [[rosettafold]] — Baker-lab predictor; RFAA all-atom; backbone for RFdiffusion
- [[rfdiffusion]] — Baker-lab diffusion backbone generator
- [[rfdiffusion3]] — Baker-lab all-atom token+atom generator (efficient)
- [[proteinmpnn]] — Baker-lab sequence design network
- [[chroma]] — Generate Biomedicines programmable diffusion model
- [[protpardelle]] — Huang-lab all-atom (superposition) generative model

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

## Missing supplements

Batch 1 is complete — all seven main texts have their SI ingested. Outstanding from batch 2 (no `_supp` PDF present in `sources/ProteinDesign/`; all three are *Science* / *Nat Commun* papers that certainly have SI, so these are genuine gaps rather than papers without supplements):

- [[wang-2022-functional-site-scaffolding]] — `supp: missing-requested`
- [[wicky-2022-symmetric-assembly-design]] — `supp: missing-requested`
- [[anand-2022-learned-potential-seqdesign]] — `supp: missing-requested`

From batch 3 (both *Science* papers; in both cases the SI holds the actual method, so these are substantive gaps rather than formalities):

- [[thomson-2014-alpha-helical-barrels]] — `supp: missing-requested`; the SI carries the knowledge-based scoring function and sampling details for the barrels.
- [[boyken-2016-hydrogen-bond-network-oligomers]] — `supp: missing-requested`; the SI carries the HBNet algorithm description and the design scripts.

*Nice-to-have:* a clean, non-image main PDF for RFAA (current main text is OCR-recovered). The `..._checklist.pdf` beside the RFAA PDFs is a reproducibility checklist, not SI — not ingested.

## Flagged references to add

Specific external references that would close a real gap in an existing page. Supply the PDF into `sources/` and the gap can be filled without resorting to model priors (see the sourcing discipline in `CLAUDE.md`).

- **Base RoseTTAFold (Baek et al., *Science* 2021).** [[rosettafold]] and [[structure-prediction]] both describe the three-track architecture and call it the parallel lineage to AlphaFold, but only the all-atom successor ([[krishna-2024-rosettafold-all-atom]]) is ingested. The foundational claims are currently uncited.
- **A Rosetta design baseline.** [[sequence-design]] characterises classic Rosetta fixed-backbone design as "accurate but slow, with limited success on hard targets" with no ingested source. Candidates already in `sources/`: `Fleischman_Baker_PLoS_2011_RosettaScripts…`, `Huang_Baker_PLOSOne_2011_RosettaRemodel…`.
- **A protein-folding foundation for the "largely solved" framing.** [[structure-prediction]] opens on the folding problem and its resolution. Candidates already in `sources/Proteins/`: `Anfinsen_Science_1973…`, `Baker_Nature_2000_A surprising simplicity to protein folding`.
- **A benchmark/metric reference** for the in silico filters the wiki leans on (lDDT, pLDDT/pAE thresholds) beyond what the SIs state. Candidate already in `sources/ProteinDesign/`: `bioinformatics_2013_lDDT…`.

### For [[symmetric-oligomer-design]] (added 2026-08-14)

The chapter's §12 lists these with full reasoning. Summary — nothing here is currently asserted from model priors; the chapter either cites a review second-hand or leaves the gap open.

- **Padilla, Colovos & Yeates, *PNAS* 2001 — "Nanohedra".** The founding symmetric-fusion paper. Currently reachable only through [[luo-2016-protein-assembly-review]]. **Highest value of anything on this list.**
- **King et al., *Science* 2012 — self-assembling protein nanomaterials with atomic-level accuracy.** Named as prior art by [[courbet-2022-axle-rotor-assemblies]] ("icosahedral nanocages"); no primary source ingested, so the chapter cannot say how those cages were designed.
- **King et al., *Nature* 2014 — co-assembling multi-component protein nanomaterials.** The two-component branch; needed to close an open question in the chapter.
- **Bale et al., *Science* 2016 — megadalton-scale two-component icosahedral complexes.** The scale demonstration and the bridge to the vaccine-platform framing that [[watson-2023-rfdiffusion]] invokes.
- ~~Anishchenko et al., *Nature* 2021~~ — **supplied and ingested 2026-08-14** as [[anishchenko-2021-hallucination]] (+ [[anishchenko-2021-hallucination-supp]]). The deep-learning side of the chapter's history is now on primary sources; the four entries above are all pre-2020.

**Already in `sources/`, un-ingested, adjacent to the chapter's scope:** `Proteins/Shen_Baker_Science_2018_…self-assembling helical protein filaments` (+supp) — helical rather than point-group symmetry; `Proteins/Brunette_Baker_Nature_2015_…repeat protein universe` — repeat symmetry, relevant to the LRR-like protomers of the giant HAL rings; `ProteinDesign/SchneiderDuhovnik_NAR_2005_PatchDock and SymmDock` — would give the "dock-and-design era" a primary method citation.

## Citation-standard audit (2026-08-06)

The review-article citation standard was adopted in the 2026-08-06 schema sync; the pages below predate it. Findings, grouped by kind — **no content was rewritten yet**, this is the approval list.

**A. Numbers stated without a citation at the claim (tool pages).** Every tool page cites its source once in the opening line, then states quantitative results in later paragraphs with no link. Under the standard, each number must carry the wikilink itself. Affected: [[chroma]] ("310 designs experimentally validated; two crystal structures at ~ångström backbone RMSD"), [[proteinmpnn]] ("~52% native sequence recovery vs. ~33% for Rosetta"), [[rfdiffusion3]] ("~10× less compute"), [[rfdiffusion]] (the capabilities list), [[protpardelle]] (superposition/collapse, miniMPNN, U-ViT), [[rosettafold]] (three-track architecture). Fix is mechanical: add the source wikilink to each claim.

**B. Uncited generalisations presented as fact.** [[binder-design]] — "The discipline. Both rely on 'predict-then-order'…" (also stale: "Both" refers to a two-item list that has since grown to five). [[diffusion-generative-design]] — "Conditioning is the point. The value is steerability…". [[motif-scaffolding]] — "Common pattern. Motif in → scaffold out → sequence with ProteinMPNN → filter with AlphaFold2" (the wikilinks here are navigation, not citations) and the framing claim "the second half of functional de novo design". [[symmetric-assembly-design]] — "Symmetry multiplies a single designed interface into a large ordered assembly, giving access to structures far outside the natural PDB". [[alphafold]] — "the field-defining model and, in practice, the standard design oracle". Fix: cite, or rewrite as explicit synthesis.

**C. Wiki inference not marked as such.** [[overview]] — "a sign the approach is robust rather than a single group's trick"; "Validation discipline is the real unlock"; [[diffusion-generative-design]] — "Different lineages, same conclusion: diffusion works for proteins"; [[structure-prediction]] — "Prediction and design are converging on shared diffusion machinery". These are defensible readings across sources but are phrased as sourced facts. Fix: prefix with "taken together" / "the wiki's reading is…".

**D. Claims with no ingested source at all.** [[structure-prediction]] — "now largely solved for single chains and increasingly for complexes"; the RoseTTAFold three-track description on [[rosettafold]]; the Rosetta baseline characterisation on [[sequence-design]]. These map onto the flagged references above; fix by ingesting a source or moving the claim to Open questions.

**E. Housekeeping.** `updated:` frontmatter on [[structure-prediction]] (2026-07-10) predates batch-2 content added to the page. No page yet carries an *Open questions* section, which the topic template expects.

## Queued (in sources/, not yet ingested)

- ~37 further PDFs in `sources/ProteinDesign/`. Candidate **batch 3** themes: prediction ecosystem (ColabFold, Foldseek, lDDT, Boltz/Boltzgen), surface-fingerprint interaction design (MaSIF — Gainza Nature + Nature Methods, has supp), antibody design (Bennett antibodies + supp, IgLM), FAMPNN / newer sequence design, protein dynamics (Kern), and the field reviews (Listgarten 2026, "AI reengineering protein engineering"). Several ship with `_supp` files already present — ingest main + companion together.
- A large second collection in `sources/Proteins/` — protein biophysics and experimental scaffolds/reagents (folding and stability, coiled coils, LOV/optogenetic domains, nanobodies and monobodies, fluorescent proteins, SpyTag/SpyCatcher and other covalent tags, binding-affinity datasets). Largely untouched; this is the natural source pool for a *Foundations* topic and a *scaffolds-and-reagents* topic.
