---
type: source-supp
parent: "[[chu-2024-protpardelle]]"
title: An all-atom protein generative model (Protpardelle) — Supplementary Information
pdf: "../sources/ProteinDesign/ChuHuang_PNAS_2024-An-all-atom-protein-generative-model_Supp.pdf"
tags: [diffusion, all-atom, methods, architecture, huang-lab]
ingested: 2026-07-13
---

# Protpardelle — Supplementary Information (companion)

Theory/architecture companion to [[chu-2024-protpardelle]]. 30 pages (Tables S1–S9). Formalizes the superposition scheme and specifies the networks — the detail needed to understand *why* all-atom codesign works here.

## What the SI contains (map)

- **A. EM formulation** — recasts superposition-based generation as **Expectation-Maximization**: during denoising, fix residue types r and learn coordinate transitions p_θ(x_{t−1}|x_t, r); during sequence prediction, fix coordinates and learn the residue distribution q(r|x_t). All-atom generation alternates: **E-step** uses **miniMPNN** to predict residue types from the current backbone, then **collapses** the superposition to the corresponding atoms; the collapse is a form of **coordinate descent** on the structure superposition.
- **B. Network architectures** — structure network is a **U-ViT** (hidden dim 256; 512 for the AFDB-trained model) with 6–8 noise-conditional transformer layers; details of the self-attention and conditioning.
- Training, sampling (varying step sizes across noise levels), hyperparameters, and evaluation tables (S1–S9).

## Key extracted details

- **Superposition + collapse is the core mechanism:** all side-chain possibilities coexist during diffusion; miniMPNN-driven residue prediction picks identities, and "collapse" selects the matching atoms — the trick that reconciles continuous coordinates with discrete residue identity in one all-atom model.
- **EM/coordinate-descent view** explains the alternating structure/sequence updates as a principled optimization, not an ad-hoc pipeline — the conceptual contrast with Baker-lab "backbone then ProteinMPNN" designs.
- **U-ViT** (vision-transformer U-Net) is the structure backbone; a separate variant is trained on the AlphaFold Database (AFDB).

## Connections

- Parent: [[chu-2024-protpardelle]]; concept [[diffusion-generative-design]].
- The miniMPNN residue step is a compact relative of [[proteinmpnn]] ([[sequence-design]]).
- Contrast the intrinsic side-chain generation here with the atomize-in-predictor approach of [[krishna-2024-rosettafold-all-atom-supp]].
