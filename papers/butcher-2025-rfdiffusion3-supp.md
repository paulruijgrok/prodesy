---
type: source-supp
parent: "[[butcher-2025-rfdiffusion3]]"
title: De novo Design of All-atom Biomolecular Interactions with RFdiffusion3 — Supplementary Information
pdf: "../sources/ProteinDesign/ButcherBaker_bioRxiv_2025_De novo Design of All-atom Biomolecular Interactions with RFdiffusion3_Supp.pdf"
tags: [diffusion, all-atom, methods, architecture, benchmarks]
ingested: 2026-07-13
---

# RFdiffusion3 — Supplementary Information (companion)

Methods/benchmark companion to [[butcher-2025-rfdiffusion3]]. 48 pages. Specifies the training regimen, tokenization, the DiffusionModule, and the four benchmarks behind the efficiency and capability claims.

## What the SI contains (map)

- **§1 Training regimen** — diffusion training & inference; **tokenization pipeline**; **atom-level conditions**; conditioning sampling; training conditions; **tip-atom sampling** (functional-atom conditioning for motifs/active sites).
- **§2 Architecture & inference** — **main inference loop**; **inference loop for symmetric design**; **token initializers**; the **DiffusionModule** spec (sparse attention between atom- and token-level features + upsampling to coordinate updates).
- **Benchmarks** — **protein–protein interaction (PPI)**, **DNA-binder**, **small-molecule**, and **atomic-motif enzyme (AME)** benchmarks — the in silico suite where RFD3 matches/beats predecessors at ~10× less compute.

## Key extracted details

- **Token + atom dual representation** with **sparse attention** between them is the efficiency lever: coarse token-level reasoning modulates fine atom-level features via an upsampling module, avoiding dense all-atom attention.
- **Tip-atom sampling** and **atom-level conditions** are how functional sites / ligand contacts are imposed — the RFD3 analogue of RFdiffusion's motif conditioning and RFAA's ligand featurization.
- **Symmetric design** has its own inference loop (token initializers + symmetry handling), carrying forward the symmetry capability from [[watson-2023-rfdiffusion-supp]].
- The **AME benchmark** targets enzyme active-site atomic motifs — a stringent test of all-atom functional scaffolding.

## Connections

- Parent: [[butcher-2025-rfdiffusion3]]; concept [[diffusion-generative-design]].
- Efficiency/architecture successor to [[watson-2023-rfdiffusion-supp]] and the RFAA featurization in [[krishna-2024-rosettafold-all-atom-supp]].
- Its unified atom/token scheme parallels the tokenization in [[abramson-2024-alphafold3-supp]].
