---
type: source
title: De novo design of protein interactions with learned surface fingerprints
authors: Gainza, Wehrle, Van Hall-Beauvais, Marchand et al. (Correia lab, EPFL)
venue: Nature 2023
pdf: "../sources/ProteinDesign/GainzaCorreia_Nature_2023_De novo design of protein interactions with learned surface fingerprints.pdf"
supp: missing-requested
tags: [binder-design, surface-fingerprints, geometric-deep-learning, independent-lineage, ppi, validation]
ingested: 2026-10-12
---

# De novo design of protein interactions with learned surface fingerprints

De novo binder design driven not by hotspot conditioning or backbone generation but by **matching complementary descriptors of molecular surfaces** — the only non-Baker-lab de novo binder lineage in the wiki, and the methodological alternative that makes the field's dominant approach legible as a choice rather than a necessity.

**Problem.** The molecular determinants of protein–protein interactions remain hard to understand even as structural data accumulates, and this gap has been the major obstacle to de novo design of protein binders ([[gainza-2023-surface-fingerprint-binders]]). The design problem is stringent: subtle atomic-level changes — a misplaced methyl group, an uncoordinated interfacial water, incompatible charges — are sufficient to disrupt a PPI.

**Approach.** A geometric-deep-learning framework operating on protein *surfaces* rather than residue graphs or backbones (the method itself is [[gainza-2020-masif]]). Surfaces are decomposed into overlapping radial patches of 12 Å radius, capturing on average nearly 400 Å² of surface area — chosen to be consistent with the buried surface areas of real interfaces. **MaSIF-site** predicts which surface patches have a high propensity to be engaged by a protein; **MaSIF-seed** then evaluates fingerprint complementarity between a chosen target patch and a large library of candidate binding motifs ("seeds"), both α-helical and β-strand, harvested from the PDB. Selected seeds are grafted onto scaffolds by Rosetta MotifGraft against a database of 1,300 monomeric scaffolds plus designed-miniprotein and AF2-proteome databases, and the remaining interface is designed with Rosetta.

The conceptual inversion is worth stating precisely: hotspot-conditioned diffusion ([[watson-2023-rfdiffusion]]) tells a generator *where* to bind and asks it to invent a binder; MaSIF-seed *searches* for what is complementary to a given patch, then builds a scaffold around the hit.

## Key results

**Benchmark against docking.** Recovering the native binder in the correct conformation (interface RMSD < 3 Å) from co-crystal structures among 1,000 decoys:

| Method | Helical set (top 1 of 31) | Non-helical set (top 1 of 83) | Average time (min) |
|---|---|---|---|
| MaSIF-seed | **18** | **41** | 15 / 118 |
| ZDock | 3 | 7 | 2,715 / 2,206 |
| ZDock + ZRank2 | 6 | 21 | 2,946 / 2,400 |

So a roughly three- to sixfold gain in top-1 recovery at **one to two orders of magnitude less compute** ([[gainza-2023-surface-fingerprint-binders]]).

**SARS-CoV-2 RBD.** MaSIF-site predicted a binding site on the RBD distinct from the ACE2 footprint but overlapping it enough to inhibit; MaSIF-seed returned **7,713 binding seeds** for that site. The initial design DBR3_01 bound at **K_D 4.6 µM** by SPR; after optimization DBR3_03 reached **80 nM**, folded and stable. A **cryo-EM structure at 2.9 Å local resolution** showed one DBR3_03 bound per RBD on the trimeric spike, agreeing with the AlphaFold prediction at **1.4 Å iRMSD**. The design engages the RBD with a buried interface area of **1,452 Å²**, smaller than the ~2,071 ± 456 Å² typical of antibodies, through small residues. Fc–DBR3_03 neutralized most variants of concern except those carrying L452R, with potency comparable to the clinical antibody imdevimab, and the binding mode was near-identical (1.4 Å backbone RMSD) between WT and Omicron RBD complexes.

**PD-L1 — a deliberately flat target.** The PD-1-engaged site on PD-L1 is "extremely flat at the structural level", the class of surface that resists small molecules. Designs reached **2 µM** (DBL1_03, comparable to the native PD-1–PD-L1 interaction at K_D 8.2 µM), then **256 nM** (DBL1_04) and **374 nM** / **120 nM** (DBL2 series) after library and SSM optimization. **Crystal structures** of DBL1_03 and DBL2 designs in complex with PD-L1 matched the computational models at **0.8 Å RMSD** and 1.0–1.9 Å iRMSD. Site-saturation mutagenesis confirmed that the four hotspot residues placed by MaSIF-seed were crucial — any other residue at those positions abolished binding.

**One-shot design with native affinities.** The limitation the paper names in its own earlier results is that designs still required in vitro evolution to reach characterizable affinity. Addressing this with a structurally more diverse seed library (helical *and* β-sheet) and biased design for polar interface contacts, the top **2,000** designed sequences per target were screened by yeast display with deep sequencing against PD-L1, PD-1 and CTLA-4. Binders were obtained for **all three targets**. The best PD-1 binder, **DBP13_01, bound at K_D 4.2 ± 2 µM with no experimental optimization at all** — comparable to the native PD-L1–PD-1 interaction (8.2 µM) — improving to submicromolar with two mutations identified from SSM data. Specificity controls: the native scaffold and predicted knockout mutants abolished binding; nivolumab competed as expected; no binding to porcine PD-1. A β-sheet-mediated PD-L1 binder (DBL3_02) reached an **apparent K_D of 21.8 nM** on yeast, and adopts a backbone conformation different from the native PD-1–PD-L1 interaction — direct evidence that the method generalizes beyond interactions found in nature.

**A result that cuts against AlphaFold-as-oracle.** For DBP13_01 the AF2-Multimer prediction agreed with the MaSIF model (3.3 Å backbone, 2.9 Å interface full-atom RMSD), and for DBL3_01 at 0.97 Å. But the paper states plainly that **"for several of these binders, the AlphaFold predictions were not in agreement with our models"** while competition and mutagenesis nevertheless established that the designed interfaces were the ones being used. The paper is also careful that AF2 agreement is "a predictive exercise and cannot be interpreted as absolute evidence that the designed binding mode is occurring, which will ultimately require an experimental structure."

## Significance / relation to the field

The independent-lineage result. Everything else in the wiki's binder coverage descends from one lab's hotspot-conditioning-plus-oracle-filtering stack; this work reaches nanomolar affinities on four therapeutically serious targets by a different representation (surfaces), a different search (descriptor matching), and a different success criterion (specificity controls and crystal structures rather than *in silico* self-consistency). That makes it the chapter's control on the question of whether the field's progress reflects the method or the target choices — see [[de-novo-binder-design]] §6.

It is also the wiki's only source in which a **flat** target is attacked deliberately and a **buried-area-efficient** interface is achieved and crystallographically confirmed, both of which bear on the biophysics of what makes an epitope designable.

**Supplement:** `supp: missing-requested` — the Supplementary Information holds Supplementary Table 4 (the per-target design and binder counts), Supplementary Figs. 17–22 (seed clustering, SSM data, AF2 comparisons) and the seed-library construction details. Without it the one-shot campaign's denominators cannot be stated beyond "top 2,000 per target".

## Connections

- Method paper: [[gainza-2020-masif]] (MaSIF-site / MaSIF-search / MaSIF-ligand) and its supplement [[gainza-2020-masif-supp]].
- The methodological alternative to [[watson-2023-rfdiffusion]]'s hotspot conditioning; contrast the specification of *where* to bind.
- Its hotspot placement is validated by SSM, which is the experimental counterpart of the packing/ΔΔG argument in [[halperin-2004-interface-hot-spots]].
- Uses Rosetta MotifGraft, i.e. the grafting lineage [[wang-2022-functional-site-scaffolding]] generalized with deep learning.
- Provides a counterexample to the AF2-as-filter discipline codified in [[bennett-2023-binder-design-dl]] and [[bennett-2023-binder-design-dl-supp]].
- Targets PD-L1, which is also a benchmark target in [[watson-2023-rfdiffusion]] and [[stark-2025-boltzgen]] — one of the few genuine cross-method comparisons available to the chapter.
- Concept: [[binder-design]]; chapter: [[de-novo-binder-design]].
