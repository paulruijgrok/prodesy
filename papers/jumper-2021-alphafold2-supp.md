---
type: source-supp
parent: "[[jumper-2021-alphafold2]]"
title: Highly accurate protein structure prediction with AlphaFold — Supplementary Information
pdf: "../sources/ProteinDesign/JumperHaasbis_Nature_2021_Highly accurate protein structure prediction with AlphaFold_supp.pdf"
tags: [structure-prediction, methods, architecture, evoformer, ipa, fape, benchmarks]
ingested: 2026-07-13
---

# AlphaFold2 — Supplementary Information (companion)

Methods/architecture companion to [[jumper-2021-alphafold2]]. 62 pages, largely pseudocode-level algorithm specifications — the canonical reference for how AF2 actually works.

## What the SI contains (map)

1. **Data pipeline (§1.2)** — parsing; genetic (MSA) search; template search; training data; filtering; **MSA block deletion**; **MSA clustering**; residue cropping; featurisation/model inputs.
2. **Self-distillation (§1.3)** — "noisy student" training on a large set of unlabelled sequences whose structures AF2 itself predicted (high-confidence only).
3. **Inference & embeddings (§1.4–1.5)**.
4. **Evoformer blocks (§1.6)** — MSA row-wise gated self-attention **with pair bias**; MSA column-wise attention; **triangle multiplicative updates** (outgoing/incoming edges); **triangle self-attention** (starting/ending node); the pair-representation machinery that enforces geometric consistency.
5. **Structure module (§1.8)** — backbone **frames** (residue gas); **Invariant Point Attention (IPA)**; torsion-angle prediction; **Amber relaxation** post-processing to remove clashes.
6. **Losses & auxiliary heads (§1.9)** — **FAPE (Frame Aligned Point Error)** and its chiral/metric properties; torsion-angle loss; **structural-violation** losses; **pLDDT** confidence head; **pTM**.
7. **Recycling (§1.10)** — iterative refinement passes (embedder + training/inference procedures).
8. **CASP14 assessment (§1.12)** and **ablation studies (§1.13)**.

## Key extracted details

- **FAPE** is the core structural loss: error between predicted and true atom positions computed in every local residue frame, then averaged — SE(3)-invariant, sensitive to chirality (distinguishes mirror images, unlike plain dRMSD). SI proves its metric properties and shows an ablation where training on **dRMSD instead of FAPE** degrades accuracy.
- **IPA** lets the structure module attend in 3D using both scalar and point (coordinate) queries/keys, invariant to global rotation/translation — the mechanism that turns pair/MSA representations into coordinates.
- **Confidence heads:** **pLDDT** (per-residue, predicts lDDT-Cα) and **pTM** (global, from predicted aligned error) — the scores now repurposed as design filters (see [[bennett-2023-binder-design-dl]], and RFdiffusion's use of them in [[watson-2023-rfdiffusion-supp]]).
- **Ablations quantify what matters:** accuracy scales with **MSA depth**; self-distillation, recycling, and the triangle operations each contribute measurably.
- **CASP14 training protocol** and the **median all-atom RMSD95** evaluation are specified here (the basis for the headline atomic-accuracy claim).

## Connections

- Parent: [[jumper-2021-alphafold2]].
- The Evoformer/IPA/FAPE machinery is the architecture that [[rosettafold]] parallels and that [[watson-2023-rfdiffusion]] fine-tunes for generation.
- Its confidence metrics underpin the *in silico* filtering discipline across [[binder-design]] and [[structure-prediction]].
- Superseded/generalized architecture in [[abramson-2024-alphafold3-supp]] (Evoformer → Pairformer + diffusion).
