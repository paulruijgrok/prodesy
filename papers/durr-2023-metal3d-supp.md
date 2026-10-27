---
type: source-supp
parent: "[[durr-2023-metal3d]]"
title: "Metal3D: a general deep learning framework for accurate metal ion location prediction in proteins — Supplementary information"
pdf: "../sources/ProteinDesign/DurrRotlisBerger_NatComm_2023_Metal3D- a general deep learning framework for accurate metal ion location prediction in proteins_Supp.pdf"
tags: [metalloprotein-design, zinc, benchmarks, datasets, methods, training-data]
ingested: 2026-10-21
---

# Metal3D — Supplementary information (companion)

Methods and benchmark companion to [[durr-2023-metal3d]]. Its most consequential content, read retrospectively, is the **dataset characterisation** — because [[elnesr-2026-zero-shot-metalloenzyme]] later used exactly these properties to explain why designs built on this model bound metal weakly.

## What the SI contains (map)

- **Supplementary Table 1** — the atoms used as reference points for each amino acid in Metal1D.
- **Supplementary Table 2** — atom selections used for voxelization with moleculekit, i.e. what the 3D CNN actually sees.
- **Supplementary Tables 3 and 4** — mean absolute deviation and median on the zinc test set, reported twice: for **all zinc sites (n = 189)** and separately for **zinc sites with at least 2 protein ligands**. Splitting the metric this way is the SI's own acknowledgement that coordination number changes the problem.
- **Supplementary Table 5** — the main parameter for each compared method, with arrows indicating the direction of higher quality, which is what makes the cross-method comparison in the main text interpretable.
- **Supplementary Figs. 1–3** — Jaccard indices under different edge-trimming cutoffs; MAD and probability distributions **restricted to sites with 3+ unique protein ligands and occupancy filtering**.
- **Supplementary Fig. 4** — MAD for **2+ residue coordinated zincs with occupancy > 0.5** in the test set.
- **Supplementary Fig. 5** — a named false positive: at p = 0.9 in **PDB 4JJJ, a calcium site is misclassified as zinc**. Metal selectivity is therefore imperfect at high confidence, which bears directly on using the model as a design objective.
- **Supplementary Figs. 9–12, 14, 16** — the **distribution of zinc sites, metal counts, multicore Zn²⁺ sites and occupancy values** across the training and test biological assemblies.

## Key extracted details

**The dataset is characterised by coordination number and occupancy, repeatedly.** Multiple figures and both MAD tables stratify by "3+ unique protein ligands", "2+ residue coordinated", and "occupancy > 0.5". The implication, visible here and acted on three years later, is that the corpus contains a substantial population of **low-coordination, low-occupancy zinc sites** — and that performance is reported both with and without them. [[elnesr-2026-zero-shot-metalloenzyme]] took the further step of excluding sites with fewer than three coordinating residues within 3.0 Å on the grounds that they likely reflect crystallisation additives or soaking agents, retraining as **Metal3D-Clean**, and found the expected trade-off: substantially lower confidence assigned to exactly those sites.

**Metal selectivity has a documented failure mode** (Fig. S5): a calcium site called as zinc at p = 0.9. Since the model is trained on zinc alone, a high-confidence prediction is evidence of a *metal-shaped* environment rather than specifically a zinc one.

**Occupancy is tracked explicitly** (Figs. S14, S16), which matters because a partially occupied crystallographic zinc is weaker evidence of a genuine site than a fully occupied one — and the headline 0.70 ± 0.64 Å accuracy is computed over a test set whose composition these figures describe.

## Connections

- Parent: [[durr-2023-metal3d]]; the training-data audit and retraining are in [[elnesr-2026-zero-shot-metalloenzyme]].
- The pattern — a predictor's training-set artefacts surfacing only when the model is used generatively — parallels the interface-prior findings in [[anishchenko-2021-hallucination]] and [[anishchenko-2021-hallucination-supp]].
- Chapter: [[enzyme-design]] §6.
