---
type: source-supp
parent: "[[butcher-2026-rfdiffusion3-science]]"
title: Atomic functional site scaffolding in biopolymers with RFdiffusion3 — Supplementary Materials
pdf: "../sources/ProteinDesign/ButcherBaker_Science_2026_Atomic functional site scaffolding in biopolymers withRFdiffusion3_Supp.pdf"
tags: [enzyme-design, methods, benchmarks, rotamers, theozyme, tokenization, training]
ingested: 2026-10-21
---

# RFdiffusion3 (Science 2026) — Supplementary Materials (companion)

109-page methods and benchmark companion to [[butcher-2026-rfdiffusion3-science]]: Materials and Methods, Figs. S1–S21, Tables S1–S13, an MDAR reproducibility checklist and a Data S1 archive.

## What the SI contains (map)

- **Notation and tokenization** — the definitional section that makes the architecture legible. Standard amino-acid and nucleotide residues are **single tokens**, while **modified residues, all ligands, and unindexed conditions are tokenized per-atom**. Tokens are **indexed** (global residue index revealed) or **unindexed** (not revealed) — the distinction that makes "unindexed atomic motif scaffolding" a precise rather than an informal claim, since a catalytic motif supplied without sequence positions is exactly a set of unindexed tokens.
- **Tensor shapes and feature dimensionalities** — including Table S6, the summary of 1D token-level and atom-level input features.
- **Training conditions** — Tables S1, S5 and S11 give the **probability configurations for different training conditions**, i.e. how often each conditioning mode (motif, hotspot, secondary structure, hydrogen bonding, base pairing) is presented during training, plus meta-conditioning features and training augmentations. Table S13 covers training-data composition and base-pair conditioning hyperparameters across epochs.
- **Efficiency** — Table S7, protein monomer generation efficiency.
- **Benchmarks** — Table S8 details the PPI benchmark, with residue indices following prior work.
- **Active site preparation and configuration** — the provenance of every active site used in the AME comparisons (below).
- **Rotamer probability loss** — the definition behind the main text's rotamer-quality claim (below).
- **Figs. S6–S11** — AME cumulative score distributions for the four principal design cases, rotamer probability loss, symmetric enzyme design success rates on the C2 AME subset, and the ZAPP-1 round-1 eluate screen with Michaelis–Menten kinetics.

## Key extracted details

**Where the four benchmark active sites come from**, which matters because the AME comparison is only as meaningful as its inputs:

- **Aldolase** — AF3 predictions of the DERA sequence from PDB 1P1X, in complex with the substrate analogue or substrate.
- **Ornithine decarboxylase** — AF3 predictions from PDB 2OO0.
- **Glycosidase** — glycosidic bond hydrolysis with a **custom ligand**; the active-site theozyme extracted from a natural glycosidase crystal structure.
- **Phosphotriesterase** — **the theozyme from which ZAPP-1 originated**, derived from a **quantum chemistry calculation**. So the benchmark case and the experimental campaign share an active-site definition, and that definition is QM-derived rather than extracted from a structure.

**Rotamer probability loss, defined.** Side-chain rotamer quality uses the **Dunbrack backbone-dependent rotamer library**. For each non-trivial residue — **excluding Gly, Ala and Pro** — the backbone dihedral angles retrieve probabilities across chi angles, with **residue-type-specific normalization constants given in Table S10**. This is the metric behind the main text's claim that RFD3 generates more native-like rotamers than RFD2, and the exclusions matter: three residue types contribute nothing to the score.

**Symmetric enzyme design** (Fig. S10) reports in-silico success rates separately for **complex backbones** on the C2 AME subset, which is the quantitative backing for the main text's qualitative claim that symmetry-aware diffusion generalises atomic motif scaffolding to multimeric enzymes.

## Connections

- Parent: [[butcher-2026-rfdiffusion3-science]]. Compare the preprint's companion, [[butcher-2025-rfdiffusion3-supp]], whose benchmark definitions (PPI, DNA-binder, small-molecule, AME) this supersedes and extends.
- The per-atom tokenization of ligands and modified residues is the mechanism by which a **carbamylated lysine** can be specified at all — see the ZAPP campaign in the parent page.
- Chapter: [[enzyme-design]] §3 and §6; concept [[motif-scaffolding]].
