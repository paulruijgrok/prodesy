---
type: source-supp
parent: "[[dauparas-2022-proteinmpnn]]"
title: Robust deep learning–based protein sequence design using ProteinMPNN — Supplementary Information
pdf: "../sources/ProteinDesign/Dauparas_Baker_Science_2022_Robust deep learning–based protein sequence design using ProteinMPNN_supp.pdf"
tags: [sequence-design, methods, architecture, gnn, ablations]
ingested: 2026-07-13
---

# ProteinMPNN — Supplementary Information (companion)

Methods companion to [[dauparas-2022-proteinmpnn]]. 25 pages (Figs S1–S12, Table S1). Documents the network internals, the ablation experiments that produced the final design, and training-data construction — with pseudocode for the encoder/decoder layers.

## What the SI contains (map)

- **Input features** — edges only (no node features); using dihedral angles as node features gave no gain. Edge features are inter-residue distances encoded with **16 Gaussian radial basis functions**; a **virtual Cβ** is added, giving 25×16 = 400 edge features per pair.
- **Architecture** — encoder–decoder **message-passing GNN**, 3 encoder + 3 decoder layers, MLPs with layer norm, dropout, residual connections; decoder is a "vanilla MPNN" that also consumes the (autoregressively masked) encoded sequence. Pseudocode for both layers is given.
- **Ablation experiments** (the design search):
  - *Exp 1* — extra input edge features (the 400-dim Gaussian RBF set).
  - *Exp 2* — **edge updates** in the encoder (E_ij updated from V_i, V_j, E_ij).
  - *Exp 4* — **random decoding order** during training (valid because the GNN is permutation-equivariant), enabling flexible/partial and tied decoding at inference.
- **Training data** — high-res PDB chains (X-ray/cryo-EM better than 3.5 Å), clustered; homo-oligomer detection via TM-align sequence identity; interface/chain masking rules for assemblies.
- **Training curves** — validation loss/perplexity vs optimizer steps (Fig S3D).

## Key extracted details

- The **edge-only, distance-based** featurization (no explicit node/dihedral features) is a deliberate robustness choice — it makes the model tolerant of imperfect/generated backbones, which is why it composes with [[rfdiffusion]].
- **Random-order autoregressive decoding** is the mechanism enabling tied positions (symmetric homo-oligomers, repeat proteins) and partial redesign — capabilities the main text uses but doesn't derive.
- **Sampling temperature** trades sequence recovery for diversity; low temperature ≈ argmax (high recovery), higher temperature broadens candidates.

## Connections

- Parent: [[dauparas-2022-proteinmpnn]]; concept [[sequence-design]].
- Edge-only robustness is what lets it sit downstream of [[watson-2023-rfdiffusion]] / [[ingraham-2023-chroma]] backbones.
- The tied-decoding machinery underlies symmetric design in [[watson-2023-rfdiffusion-supp]].
