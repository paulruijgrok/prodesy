---
type: source-supp
parent: "[[krishna-2024-rosettafold-all-atom]]"
title: Generalized biomolecular modeling and design with RoseTTAFold All-Atom — Supplementary Information
pdf: "../sources/ProteinDesign/KrishnaBaker_Science_2024_Generalized biomolecular modeling and design with RoseTTAFold All-Atom_supp.pdf"
tags: [structure-prediction, all-atom, methods, featurization, benchmarks, binder-design]
ingested: 2026-07-13
---

# RoseTTAFold All-Atom — Supplementary Information (companion)

Methods/benchmark companion to [[krishna-2024-rosettafold-all-atom]]. 107 pages (Figs S1–S34). This is the clean, text-based counterpart to the OCR-recovered main PDF — the authoritative source for RFAA's featurization, training, benchmarks, and the RFdiffusionAA binder-design protocols.

## What the SI contains (map)

- **Featurization (§1)** — protein–small-molecule complexes; **atomized protein examples**; **covalently bound ligands**; **metal ions**; **CSD small-molecule crystals**; **bond embedding**; **bond-geometry losses**; **chirality input angles** (how the atomic representation encodes stereochemistry).
- **Datasets** — small-molecule training/benchmark datasets; computing **sequence similarity** and **ligand similarity** to the training set; evaluating how those similarities affect accuracy (the generalization analysis behind the low-Tanimoto success numbers).
- **Training (§ RFAA)** — structure-prediction training details and hyperparameters.
- **RFdiffusionAA (§2)** — training details; **in silico design methods**; **small-molecule binder design benchmark**; per-target protocols for **bilin**, **heme**, **digoxigenin** binders; **diversity** and **novelty** analyses of generated binders.
- **Prediction analyses** — metal-ion prediction; recent-PDB protein–small-molecule complexes; comparison of showcased structures to training data (memorization check).

## Key extracted details

- **Two-representation featurization** is spelled out here: residues (amino acids, DNA/RNA bases) vs **atomized** groups (ligands, metals, covalent mods, glycans), tied together by **bond embeddings** and trained with **bond-geometry losses** and explicit **chirality angles** — the machinery that lets one network span heterogeneous chemistry.
- **Generalization is measured, not assumed:** accuracy is reported as a function of **sequence and ligand similarity to the training set** (e.g., the stringent <0.5-Tanimoto split), with a memorization check comparing predictions to nearest training structures.
- **RFdiffusionAA binder benchmark + per-ligand protocols** (bilin/heme/digoxigenin) give the concrete design/filtering recipe, plus **diversity and novelty** quantification of the generated binders — the experimental backbone of the main text's validated designs.

## Connections

- Parent: [[krishna-2024-rosettafold-all-atom]]; tool [[rosettafold]].
- The atomized/bond featurization is the design-side analogue of the unified tokenization in [[abramson-2024-alphafold3-supp]].
- RFdiffusionAA protocols extend the diffusion pipeline of [[watson-2023-rfdiffusion-supp]] to ligand-conditioned [[binder-design]].
- Supersedes the interim note on the OCR'd main page: **SI now ingested; a clean main PDF remains nice-to-have but no longer blocking.**
