---
type: tool
tags: [binder-design, hallucination, diffusion, fine-tuning-free, all-atom]
sources: 2
updated: 2026-10-12
---

# ProteinHunter

A **fine-tuning-free** design framework that exploits the willingness of diffusion-based structure-prediction models to hallucinate plausible structures from an uninformative sequence. Introduced in [[cho-2025-protein-hunter]].

**Mechanism.** Start from an **all-X sequence** (every position the unknown-residue token), predict its structure with an AF3-style model, then cycle: redesign the sequence with ProteinMPNN or LigandMPNN, re-predict the complex, repeat. There is **no diffusion over coordinates, no gradient optimisation, and no training** — the generative capacity is borrowed from the predictor. The X token is chosen because AF3-style models encode unknown PDB residues as X, and because X-initiated designs empirically gave the highest ipTM and lowest loop fractions ([[cho-2025-protein-hunter]]).

**Capabilities.** Unconditional generation to 500–600 residues; binder design against proteins, cyclic peptides, small molecules, DNA and RNA; multi-motif scaffolding; partial redesign; antibody CDR redesign ([[cho-2025-protein-hunter]]).

**Results.** Higher ipTM than RFdiffusion on **9 of 11** protein targets with Boltz-2 as substrate (7 of 11 with Chai-1); higher small-molecule success rates than RFdiffusionAA, BoltzDesign2 and its own single-pass mode on all four ligands tested ([[cho-2025-protein-hunter]]).

**Substrate choice matters.** Boltz-2 outperformed Chai-1 and AlphaFold3 as the hallucination substrate, attributed to Boltz-2 encoding each non-canonical residue as a single learned token (so X behaves as one residue, where atom-level tokenisation increases sampling complexity) and to AlphaFold3 having been fine-tuned on distilled AF2 predictions, which encourages spaghetti-like low-confidence regions and so suppresses the hallucination the method depends on ([[cho-2025-protein-hunter]]).

**Stated limitation.** It inherits the predictor's prior including its biases: structures from AF3-style models showed **lower diversity than RFdiffusion's**, with a preference for α-helical topologies ([[cho-2025-protein-hunter]]).

**As operated in this project** ([[ruijgrok-2026-binder-pipeline-comparison]]). One of four local generative pipelines, and the only one that supplies **no target structure at all** — target as sequence plus MSA, conformation re-predicted every cycle, `--template_path` present but never passed, recorded there as "the sharpest representational difference in the project". Its hotspot enforcement is the project's strictest: a Boltz pocket constraint *plus* an explicit heavy-atom contact filter at cycle 0 and again at a promotion gate. Measured cost 510.2 GPU-hours over 1,255 tasks, 15.40 GPU-minutes per design, 2 GPUs per task on one node with 40 and 48 GB cards OOM-ing 100% of the time on the dimer target. Its interface gate is the richest of any pipeline there — an 11-criterion PyRosetta gate. Two cautions for any rate quoted from it: the **promotion gate sets the denominator before scoring**, losing 79% of tasks, and moving that gate from 0.8 to 0.7 shifted promotion from 14.1% to 43.8% on byte-matched generation; and a GPU OOM surfaces as a `KeyError` rather than an OOM error.

**Connections.** Completes the hallucination lineage [[anishchenko-2021-hallucination]] → [[wicky-2022-symmetric-assembly-design]] → [[frank-2024-relaxed-sequence-optimization]] → [[complexa]], by borrowing a prior rather than training one. Benchmarked against [[rfdiffusion]] and RFdiffusionAA ([[krishna-2024-rosettafold-all-atom]]); uses [[proteinmpnn]] and [[alphafold]]-class predictors. Faster-converging alternative to [[bindcraft]]. Concept [[binder-design]]; chapter [[de-novo-binder-design]] §8, §11.
