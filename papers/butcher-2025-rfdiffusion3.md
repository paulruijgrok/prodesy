---
type: source
title: De novo Design of All-atom Biomolecular Interactions with RFdiffusion3
authors: Butcher, Krishna, Mitra et al. (Baker lab)
venue: bioRxiv 2025 (preprint)
pdf: "../sources/ProteinDesign/ButcherBaker_bioRxiv_2025_De novo Design of All-atom Biomolecular Interactions with RFdiffusion3.pdf"
supp: yes
tags: [diffusion, all-atom, nucleic-acids, small-molecule, efficiency, frontier]
ingested: 2026-07-13
---

# RFdiffusion3 (RFD3) — All-atom biomolecular interaction design

The current frontier of the Baker-lab diffusion line: one all-atom model that designs proteins in the context of ligands, nucleic acids and arbitrary non-protein atoms, at **~10× lower compute** than its predecessors.

**Problem.** Designing proteins that interact with the full range of biomolecules (small molecules, DNA/RNA, metals) previously needed distinct models/heuristics ([[watson-2023-rfdiffusion]] for proteins, RFdiffusionAA in [[krishna-2024-rosettafold-all-atom]] for small molecules). A single efficient all-atom generator was missing.

**Approach.** [[rfdiffusion3]] represents systems with combined **token-level and atom-level** features and a three-part network: (i) a module encoding the noised structure, (ii) a **sparse transformer** over token-wise information, and (iii) an **upsampling module** that modulates atomic features with token features and predicts coordinate updates — jointly sampling backbone and side-chain coordinates. Sparse attention between atomic and token features keeps it efficient.

**Key results.**

- **Matches or beats prior methods on in silico benchmarks at ~one-tenth the computational cost** (PPI, DNA-binder, small-molecule, and atomic-motif-enzyme benchmarks per the SI).
- Designs and **experimentally characterizes DNA-binding proteins**, demonstrating genuine all-atom, nucleic-acid-aware design.
- Generalizes the "all-atom" idea from RFAA into the diffusion generator itself.

**Significance.** Consolidates the fragmented generative toolset into one efficient all-atom model — the design-side parallel to [[abramson-2024-alphafold3]] unifying prediction. Its efficiency gains matter for the "generate many, filter cheaply" discipline. Newest node in [[diffusion-generative-design]].

**Connections.**

- Successor to [[watson-2023-rfdiffusion]] (RFD2) and the RFdiffusionAA of [[krishna-2024-rosettafold-all-atom]].
- All-atom design counterpart to all-atom prediction in [[abramson-2024-alphafold3]] and to [[chu-2024-protpardelle]].
- **Supplement:** [[butcher-2025-rfdiffusion3-supp]] — training regimen, tokenization, benchmarks (PPI / DNA / small-molecule / AME).
