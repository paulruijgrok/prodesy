---
type: source-supp
parent: "[[abramson-2024-alphafold3]]"
title: Accurate structure prediction of biomolecular interactions with AlphaFold 3 — Supplementary Information
pdf: "../sources/ProteinDesign/AmbramsonJumper_Nature_2024_Accurate structure prediction of biomolecular interactions with AlphaFold 3_supp.pdf"
tags: [structure-prediction, methods, architecture, diffusion, pairformer, tokenization, benchmarks]
ingested: 2026-07-13
---

# AlphaFold3 — Supplementary Information (companion)

Methods/architecture companion to [[abramson-2024-alphafold3]]. 45 pages of pseudocode-level specs. Best read against the [[jumper-2021-alphafold2-supp]] to see exactly what changed from AF2.

## What the SI contains (map)

1. **Data pipeline (§2)** — parsing; genetic search; **MSA processing**; template search; **training data** (**Weighted PDB dataset**, distillation datasets, clustering, filtering); **tokenization**; **cropping** (contiguous / spatial / spatial-interface); featurisation.
2. **Architecture (§3)** — **atom attention** encoder/decoder + **Atom Transformer** (sequence-local); **MSA Module** (lighter than AF2, `MSAPairWeightedAveraging`); template embedder; **Pairformer stack** (the Evoformer successor); **Diffusion Module** + **Diffusion Conditioning** + **Diffusion Transformer**; diffusion training.
3. **Inference (§4)** — **mini diffusion rollout**; **model confidence prediction** and **confidence-head architecture** (confidence trained on diffusion samples).
4. **Evaluation & ranking (§5–6)** — **confidence measures and sample ranking** (alignment-based measures, **clash** penalties, ranking); training details; **evaluation metrics**.

## Key extracted details

- **Unified tokenization** is the central idea: a "token" is the fundamental unit entering the Pairformer — one per residue for polymers, one per **atom** for ligands/ions/modified residues — so proteins, nucleic acids, small molecules and metals share one representation. This is what lets a single model span biomolecular space (vs. AF2's residue-only view).
- **Architecture swap:** AF2's Evoformer + IPA structure module → **Pairformer** + a **diffusion module** that predicts raw atom coordinates directly, removing much stereochemical special-casing (no frames/torsions/Amber-relax pipeline).
- **Atom attention** (local) feeds a coarser token-level trunk, then decodes back to atoms — an efficiency pattern for all-atom systems.
- **Confidence on samples + ranking:** confidence heads are trained against generated diffusion samples; final selection uses alignment-based confidence plus **clash** filtering (§5.9) — the practical fix for picking good rollouts.
- **Hallucinated disorder mitigation:** disordered regions can be drawn as spurious compact/ordered structure; the SI documents **cross-distillation** (training on AF2/AF-Multimer outputs) and ranking to suppress this — the known failure mode noted in the main summary.
- **Weighted PDB dataset + spatial-interface cropping** are the data-side enablers of the interaction-accuracy gains (protein–ligand, protein–nucleic-acid, antibody–antigen).

## Connections

- Parent: [[abramson-2024-alphafold3]].
- Direct architectural evolution of [[jumper-2021-alphafold2-supp]] (Evoformer→Pairformer, structure module→diffusion).
- Its diffusion coordinate head is the same paradigm as [[watson-2023-rfdiffusion-supp]] and [[ingraham-2023-chroma]] — see [[diffusion-generative-design]] on prediction⇄design convergence.
- All-atom, ligand-aware scope parallels [[krishna-2024-rosettafold-all-atom]] on the design side.
