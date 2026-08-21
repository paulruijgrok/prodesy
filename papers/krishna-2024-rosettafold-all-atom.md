---
type: source
title: Generalized biomolecular modeling and design with RoseTTAFold All-Atom
authors: Krishna, Wang, Ahern et al. (Baker lab)
venue: Science 2024
pdf: "../sources/ProteinDesign/KrishnaBaker_Science_2024_Generalized biomolecular modeling and design with RoseTTAFold All-Atom.pdf"
supp: yes
tags: [structure-prediction, all-atom, small-molecule, diffusion, binder-design, foundational]
ingested: 2026-07-13
---

# RoseTTAFold All-Atom (RFAA) — Generalized biomolecular modeling and design

Extends structure prediction and design beyond protein-only systems to full biomolecular assemblies — proteins with nucleic acids, small molecules, metals and covalent modifications — and, via a diffusion variant, designs proteins around small-molecule ligands.

> *Main text recovered by OCR (the source PDF is a Science first-release with a broken text layer; see [[log]]). The Supplementary Information — clean, text-based — is now ingested: [[krishna-2024-rosettafold-all-atom-supp]]. A clean main PDF remains nice-to-have but is no longer blocking.*

**Problem.** [[jumper-2021-alphafold2]] and RoseTTAFold predict protein structure from sequence, but proteins rarely act alone — they bind DNA/RNA, small molecules, metals and carry covalent modifications. Modeling such heterogeneous assemblies was an outstanding challenge; bolt-on classical docking of non-protein parts is hard to evaluate and optimize.

**Approach.** [[rosettafold]] All-Atom combines a **residue-based** representation (for amino acids and DNA/RNA bases) with an **atomic** representation for everything else (arbitrary small molecules, metals, covalent groups), within the RoseTTAFold framework — so one network handles diverse chemistry given sequences plus chemical structures. Fine-tuning RFAA on denoising yields **RFdiffusionAA**, which builds protein backbones directly around a target small molecule, starting from randomly placed residues.

**Key results.**

- **Protein–small-molecule** prediction: ~42% of complexes predicted successfully on their benchmark vs. ~38% for DiffDock; competitive-to-better than AutoDock Vina servers (which succeed on ~32% of the cases benchmarked). Higher accuracy on stringent/low-similarity splits (e.g., 19% vs. 14% at <0.5 Tanimoto).
- Handles **covalent modifications** and predicts **glycan** conformations on N-linked sites; improved overall protein accuracy vs. RF2.
- **RFdiffusionAA** de novo small-molecule binder design experimentally validated by crystallography and binding measurements for three ligands: the cardiac therapeutic **digoxigenin**, the cofactor **heme**, and the light-harvesting **bilin**.

**Significance.** Generalizes the Baker-lab prediction/design stack to all-atom, ligand-aware territory — the design-side counterpart to [[abramson-2024-alphafold3]]'s all-atom prediction. RFdiffusionAA pushes [[diffusion-generative-design]] into small-molecule [[binder-design]], a capability the protein-only [[watson-2023-rfdiffusion]] lacked.

**Connections.**

- All-atom extension of RoseTTAFold, the prediction sibling of [[jumper-2021-alphafold2]] and the network fine-tuned in [[watson-2023-rfdiffusion]].
- Design-side parallel to [[abramson-2024-alphafold3]] (all-atom prediction); both migrate the field to all-atom modelling.
- RFdiffusionAA extends [[diffusion-generative-design]] to ligand-conditioned [[binder-design]].
- **Supplement:** [[krishna-2024-rosettafold-all-atom-supp]] — featurization (atomized groups, bonds, chirality, metals), training/benchmark details, RFdiffusionAA binder protocols (bilin/heme/digoxigenin), diversity/novelty analyses.
