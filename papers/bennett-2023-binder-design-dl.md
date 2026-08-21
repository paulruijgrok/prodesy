---
type: source
title: Improving de novo protein binder design with deep learning
authors: Bennett, Coventry et al. (Baker lab)
venue: Nature Communications 2023
pdf: "../sources/ProteinDesign/BennettDaker_NatureCommunications_2023_Improving de novo protein binder design with deep learning.pdf"
supp: yes
tags: [binder-design, deep-learning, filtering, sequence-design]
ingested: 2026-07-10
---

# Improving de novo protein binder design with deep learning

Shows that inserting deep-learning models into the classic Rosetta binder pipeline — as sequence designer and as *in silico* filter — raises success rates roughly ten-fold.

**Problem.** De novo design of high-affinity binders from target structure alone had become possible (Rosetta-based, motif-grafting) but success rates were low, so large numbers of candidates had to be screened experimentally.

**Approach.** Two deep-learning augmentations to the [[binder-design]] workflow: (1) use [[proteinmpnn]] instead of Rosetta for [[sequence-design]], greatly cutting compute; (2) use [[jumper-2021-alphafold2]] (and RoseTTAFold) to score two probabilities — that the designed sequence folds to the intended monomer, and that it binds the target in the designed pose — as a filter before ordering.

**Key results.**

- The AlphaFold2/RoseTTAFold self-consistency filter increases experimental success rate **~10×**.
- ProteinMPNN sequence design substantially reduces computational cost relative to Rosetta while maintaining or improving quality.
- Establishes AF2 confidence (pae_interaction and monomer pLDDT) as a practical, quantitative go/no-go metric for binder campaigns.

**Significance.** Codifies the "predict-then-order" discipline that makes de novo [[binder-design]] tractable at scale; the same filtering logic is baked into downstream [[watson-2023-rfdiffusion]] binder workflows.

**Supplement:** [[bennett-2023-binder-design-dl-supp]] — retrospective analysis defining the metrics: pLDDT / pAE_interaction vs RMSD, ROC discrimination of SC50 < 4 µM success, ProteinMPNN-vs-Rosetta prospective tests, AF2-with-template complex-prediction setup.

**Connections.**

- Uses [[jumper-2021-alphafold2]] as a filter and [[dauparas-2022-proteinmpnn]] for sequence design.
- Bridges classic Rosetta binder design and the generative [[watson-2023-rfdiffusion]] era.
- Anchor reference for the [[binder-design]] concept.
