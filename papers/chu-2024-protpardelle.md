---
type: source
title: An all-atom protein generative model (Protpardelle)
authors: Chu, Kim, Cheng, El Nesr, Xu, Shuai, Huang (Huang lab, Stanford)
venue: PNAS 2024
pdf: "../sources/ProteinDesign/ChuHuang_PNAS_2024-An-all-atom-protein-generative-model.pdf"
supp: yes
tags: [diffusion, all-atom, sidechains, codesign, huang-lab]
ingested: 2026-07-13
---

# Protpardelle — An all-atom protein generative model

A Huang-lab all-atom diffusion model that generates backbone **and** side chains together, via a novel "superposition" trick for handling the mixed continuous/discrete nature of proteins. An independent, distinct approach to all-atom generation from the Baker-lab line.

**Problem.** Protein function is mediated by **side-chain** chemistry, but most generative models produce backbones only (side chains added afterward by a separate sequence-design step). Building a truly all-atom generative model is hard because structure is continuous while sequence/residue identity is discrete.

**Approach.** [[protpardelle]] is an all-atom diffusion model that represents **all possible side-chain states at once as a "superposition"**; during sampling the superposition is **collapsed** into specific residue identities and conformations. Sequence is predicted with a **miniMPNN** in an EM-like scheme (denoise coordinates conditioned on residue types; predict residue types from structure), enabling **codesign** of all-atom structure and sequence. Motifs can be scaffolded **backbone- and rotamer-free**.

**Key results.**

- Generated proteins score well on standard **quality, diversity and novelty** metrics; side chains reproduce the chemical features/behavior of natural proteins.
- Demonstrates all-atom motif scaffolding without pre-committing to a backbone or rotamers.
- Architecture (SI): a **U-ViT** structure network with noise-conditional transformer layers; separate AFDB-trained variant.

**Significance.** Offers a fundamentally different answer to all-atom design than [[krishna-2024-rosettafold-all-atom]] / [[abramson-2024-alphafold3]]: rather than atomizing ligands within a predictor, it makes **side-chain generation intrinsic** to the diffusion process and codesigns sequence. Strengthens the "independent labs converge on diffusion" theme in [[diffusion-generative-design]].

**Connections.**

- Huang-lab counterpart to Baker-lab [[watson-2023-rfdiffusion]]; all-atom peer of [[krishna-2024-rosettafold-all-atom]].
- Uses a miniMPNN (kin to [[proteinmpnn]]) for the residue step; relates to [[sequence-design]] via codesign.
- Concept: [[diffusion-generative-design]]. **Supplement:** [[chu-2024-protpardelle-supp]].
