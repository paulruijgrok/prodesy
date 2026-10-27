---
type: source-supp
parent: "[[gainza-2020-masif]]"
title: Deciphering interaction fingerprints from protein molecular surfaces using geometric deep learning — Supplementary Information
pdf: "../sources/ProteinDesign/GainzaCorreia_NatureMethods_2023_Deciphering interaction fingerprints from protein molecular surfaces using geometric deep learningSupp.pdf"
tags: [surface-fingerprints, geometric-deep-learning, methods, benchmarks, datasets, interface-prediction]
ingested: 2026-10-12
---

# MaSIF — Supplementary Information (companion)

Methods and benchmark companion to [[gainza-2020-masif]]. Twelve supplementary figures and nine supplementary notes; the notes carry the dataset construction, the train/test splitting discipline and the competitor-method setups that the main text only names.

## What the SI contains (map)

- **Fig S1** — the geodesic-vs-Euclidean demonstration, on trypsin (PDB 1PPE). A 12 Å *Euclidean* patch centred in the interface pocket reaches points on a different face of the protein entirely; the 12 Å *geodesic* patch stays on the interacting face. This is the figure that justifies the whole parameterization.
- **Fig S2** — MaSIF-ligand confusion matrices and a feature-importance analysis on the hard NAD-vs-NADP discrimination.
- **Fig S3** — MaSIF-site score distributions and depth ablation: **ROC AUC 0.77 with one convolutional layer, 0.86 with three** (n = 2,192,870 test-set surface points).
- **Fig S4** — MaSIF-site vs. **SPPIDER** and **PSIVER** on 53 proteins involved in *transient* interactions, per-protein ROC AUC distributions.
- **Fig S5** — the shape-complementarity stratification and the feature-inversion trick: descriptor performance split by high/low complementarity class, and ROC AUCs for GIF descriptors vs. MaSIF trained on geometry only, chemistry only, or both. Networks trained *with* input-feature inversion outperform those without (ROC computed on 13,338 positive and 13,338 negative patch pairs).
- **Fig S6** — the MaSIF-search complex-generation protocol in full: fingerprint the target site, retrieve the K most similar fingerprints from a precomputed database, align by **RANSAC** (selecting the alignment with the most points within 1.5 Å), then score the transformation with a neural network taking a **200 × 3** input matrix of per-correspondence 3D distance, fingerprint distance and normal product.
- **Fig S7** — the hybrid MaSIF-search/MaSIF-site protocol on PD-L1, and the clearest single result in the SI: scanning a database of nearly **11,000 proteins**, keeping patches with MaSIF-site score > 0.9 and descriptor distance < 1.7, the **top-ranked predicted complex was PD-L1:mouse PD-1 (3BIK) at 0.6 Å RMSD**, with PD-L1:human PD-1 (4ZQK) ranked #8 at 0.3 Å. Total runtime ≈ **26 minutes**, excluding descriptor precomputation.
- **Fig S8** — the splitting-rigour control. Test sets were split from training sets by hierarchical clustering on TM-score matrices (interface TM-score for MaSIF-search), but some test structures still retained TM-score > 0.5 to a training member. A **stricter split** removing all such cases **did not affect performance**: MaSIF-site 359 proteins / 2,191,879 patches → 169 / 1,042,951; MaSIF-search 957 proteins / 13,338 interacting pairs → 635 / 7,135.
- **Figs S9–S11** — the three network architectures. MaSIF-ligand: 32 sampled pocket patches → conv → FC80 → an 80×80 covariance matrix → FC64, FC7, softmax cross-entropy. MaSIF-site: conv → FC5, FC4, FC2 → sigmoid cross-entropy. MaSIF-search: target patch and its true binder patch or a random patch → conv → FC80, trained to **minimize** L2 descriptor distance to the binder and **maximize** it to the random patch.
- **Fig S12** — total computation time by chain length (50–500 residues). The headline: **GPU time is a small fraction of wall time, 4 s for a 50-residue protein to 12 s for a 500-residue protein**; the rest is surface computation and I/O.
- **Notes 1–9** — dataset construction and competitor setups.

## Key extracted details

- **Ligand dataset (Note 1).** All PDB structures as of **16 October 2018** containing a protein chain, no DNA/RNA, and one of seven cofactor identifiers: 1,853 ADP, 490 CoA, 2,020 FAD, 4,448 HEM, 1,269 NAD, 1,212 NADP, 393 SAM. Redundancy filtered using the PDB's precomputed **30% sequence-identity** clusters.
- **PPI datasets (Note 4).** Interfaces drawn from the **PRISM** database of non-redundant PPIs from crystal structures, plus **3,536 non-obligate (transient)** interactions — the transient subset matters because transient interfaces are the ones binder design is trying to imitate.
- **Splitting is structural, not sequence-based (Note 5/Fig S8).** Splits are performed on structural alignments of interface atoms rather than sequence identity, and the strict-split control above shows the result survives it. For a wiki that repeatedly asks whether a design method has merely memorized the PDB, this is the strongest such control in any ingested source.
- **Competitor setups (Note 8).** GIF descriptors, PatchDock (default settings, Geometric Score), and ZDock → ZRank2. ZDock generates 2,000 docking results per pair by default and had to be run **10,000 times** for the bound benchmark on a 96-vCPU / 360 GB cloud server; reported times are CPU user time. This is the provenance of the one-to-two-orders-of-magnitude speed gap quoted in [[gainza-2023-surface-fingerprint-binders]], and it is a CPU-vs-GPU comparison, which the main text does not make explicit.

## Connections

- Parent: [[gainza-2020-masif]]; applied to design in [[gainza-2023-surface-fingerprint-binders]].
- The 30%-identity and strict-TM-score splitting discipline is the methodological counterpart of the >30%-identity novelty control in [[stark-2025-boltzgen]].
- Chapter: [[de-novo-binder-design]] §6; also relevant to §10 on what an oracle or scorer has actually been tested against.
