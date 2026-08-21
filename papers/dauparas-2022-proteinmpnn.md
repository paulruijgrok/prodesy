---
type: source
title: Robust deep learning–based protein sequence design using ProteinMPNN
authors: Dauparas et al. (Baker lab)
venue: Science 2022
pdf: "../sources/ProteinDesign/Dauparas_Baker_Science_2022_Robust deep learning–based protein sequence design using ProteinMPNN.pdf"
supp: yes
tags: [sequence-design, deep-learning, message-passing, foundational]
ingested: 2026-07-10
---

# ProteinMPNN — Deep learning–based protein sequence design

The workhorse sequence-design model: given a backbone, find an amino-acid sequence that folds to it. Replaced Rosetta as the default for the fixed-backbone [[sequence-design]] step in most modern pipelines.

**Problem.** Physically based design (Rosetta) treats sequence design as expensive energy optimization over side-chain rotamers. It is slow and its success rate for challenging targets is limited.

**Approach.** [[proteinmpnn]] is a message-passing neural network (3 encoder + 3 decoder layers, 128 hidden dims) that predicts sequence **autoregressively** from N to C terminus, conditioned on backbone geometry only — Cα–Cα distances, relative frame orientations, and backbone dihedrals. An order-agnostic decoding scheme and small Gaussian noise on backbone coordinates improve robustness. Handles monomers, cyclic oligomers, nanoparticles and protein–protein interfaces, including tied/symmetric positions.

**Key results.**

- **Sequence recovery** on native backbones rises to ~52.4% vs. ~32.9% for Rosetta, at a tiny fraction of the compute (seconds, no explicit rotamer search).
- Experimentally rescues previously failed Rosetta designs: soluble expression and folding of designs that had failed, and improved success across nanoparticles and assemblies.
- Robust to imperfect/predicted backbones, which is what makes it composable with generative backbone models.

**Significance.** ProteinMPNN is the second stage of the dominant two-step de novo recipe — *generate a backbone, then design its sequence*. It is the sequence-design engine paired with [[watson-2023-rfdiffusion]] and used in the improved [[bennett-2023-binder-design-dl]] pipeline.

**Supplement:** [[dauparas-2022-proteinmpnn-supp]] — GNN internals (edge-only Gaussian-RBF features, encoder edge updates), random-order decoding, tied/interface masking, training data, ablations, pseudocode.

**Connections.**

- Standard sequence-design step downstream of [[watson-2023-rfdiffusion]] backbones.
- Adopted in [[bennett-2023-binder-design-dl]] to replace Rosetta sequence design for efficiency.
- Central reference for [[sequence-design]].
