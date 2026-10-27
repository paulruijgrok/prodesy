---
type: source
title: Scaling Atomistic Protein Binder Design with Generative Pretraining and Test-Time Compute
authors: Didi, Zhang, Zhou, Reidenbach, Cao, Cha et al. (NVIDIA, Oxford, Mila, SNU)
venue: ICLR 2026
pdf: "../sources/ProteinDesign/DidiKreis_ICLR_2026 SCALING ATOMISTIC PROTEIN BINDER DESIGN WITHGENERATIVE PRETRAINING_AND_TEST_TIMECOMPUTE.pdf"
supp: no
tags: [binder-design, test-time-compute, flow-matching, hallucination, pretraining, benchmarks, all-atom]
ingested: 2026-10-12
---

# Proteína-Complexa — scaling atomistic binder design with generative pretraining and test-time compute

The paper that dissolves the field's central methodological split. Its claim is that **generative modelling and hallucination are not alternatives but the training-time and inference-time halves of one procedure**, and that treating them as such — a pretrained generative prior plus inference-time search inside it — beats either alone under equal compute.

**Problem.** Modern binder design falls into two classes. **Generative** methods ([[watson-2023-rfdiffusion]], [[ingraham-2023-chroma]]) treat design as conditional generation, training on binder–target complexes and sampling candidates for unseen targets. **Hallucination** methods — exemplified by **BindCraft** (Pacesa et al. 2025), building on Goverde et al. 2023 — optimize binder sequences against the confidence and alignment scores of a structure predictor by gradient feedback. The paper's argument is by analogy to language and vision, where a pretrained base model is combined with adaptive inference-time compute in a single framework: current binder methods resemble *either* pure training-time optimization (generative) *or* pure inference-time optimization with no generative prior (hallucination), and the dichotomy is false.

**Approach.** Three components.

1. **Teddymer** — a new large-scale synthetic dataset of binder–target pairs, constructed by treating the **domain–domain interactions of computationally predicted monomeric structures** as surrogate binder–target complexes, then filtering. Combined with high-quality experimental multimers for a stagewise training recipe: pretrain on the synthetic and AFDB-derived data, then post-train on experimental complexes.
2. **A partially latent architecture.** Flow matching over a representation that is part explicit coordinate, part latent: a Cα-only coordinate variable plus per-residue local latents decoded to all-atom structure *and sequence* by a separate autoencoder. Chosen for scalability because binder design requires generating many candidates, especially when scaling inference compute.
3. **Inference-time optimization** adapted from the diffusion literature, using interface confidence from structure predictors as the reward: **best-of-N**, **beam search**, **Feynman–Kac steering** (importance sampling of a tilted distribution p(x)·exp{βR(x)}), and **MCTS**. The paper also shows BindCraft-style hallucination can be *accelerated* by initializing it from a generative-model sample.

**Success criteria** (worth recording, because they are the units of every number below). Protein targets, following Zambaldi et al. 2024, use AlphaFold2-Multimer via ColabDesign: a sequence succeeds if **pLDDT > 90, interface pAE < 7.0, and binder RMSD < 1.5 Å**. Small-molecule targets, following Cho et al. 2025, use an AF3-like model (RoseTTAFold-3) with **min-interface-pAE < 2, binder RMSD < 2 Å, ligand RMSD < 5 Å**. Interface hydrogen-bond energies are computed by Rosetta conventions and detected with HBPlus.

## Key results

**Generative performance without any test-time optimization** (unique successes across targets; "Self" = the model's own co-generated sequence, "MPNN" = full backbone-based redesign, "MPNN-FI" = redesign with interface residues fixed):

| Model | Self | MPNN-FI | MPNN | Time (s) | Novelty |
|---|---|---|---|---|---|
| RFdiffusion | – | – | 4.68 | 70.8 | 0.87 |
| Protpardelle-1c | – | – | 0.73 | 8.13 | 0.77 |
| APM | 0.31 | 1.52 | 3.15 | 73.1 | 0.86 |
| **Complexa** | **9.10** | **13.6** | **14.4** | 15.6 | 0.80 |

Complexa wins on most targets in every column, and is the best method on 14 of the counted targets under all three sequence settings. The paper draws the conclusion that **even Complexa's self-generated sequences outperform all baselines including those relying on ProteinMPNN redesign, "making such additional steps unnecessary."**

**Test-time scaling.** Against hallucination baselines **BindCraft** and **BoltzDesign**, viewed as brute-force optimization, Complexa's search strategies are compared at **normalized compute budgets** measured in test-time GPU-hours. For easy targets, even best-of-N already outperforms the baselines; the more elaborate search methods pay off as targets harden. The paper states this is, to its knowledge, the first systematic exploration of test-time scaling for protein design.

**Extensions.** Interface hydrogen-bond optimization as an explicit reward; fold-class-guided binder generation; small-molecule targets (ligands including OQO, FAD, IAI), again surpassing the baseline; and a recent **enzyme design benchmark**, where it also outperforms prior work.

## Significance / relation to the field

This is the chapter's §11 — the compute-and-search axis — and it reframes two earlier sections retrospectively. Hallucination's history in this wiki runs through [[anishchenko-2021-hallucination]] (MCMC against trRosetta), [[wicky-2022-symmetric-assembly-design]] (MCMC against AF2, with adversarial overfitting as the failure) and [[frank-2024-relaxed-sequence-optimization]] (gradient descent in relaxed sequence space). The diagnosis there was that optimizing against an oracle produces adversarial sequences. This paper's answer is that the problem was never the optimization but the **absence of a prior to optimize inside** — search within a generative prior is constrained to the manifold the prior has learned, so the adversarial region is harder to reach. Whether that is the right reading of the overfitting failure is left as an open question in [[de-novo-binder-design]].

**It is also, uniquely in the wiki, a paper with a first-party operational counterpart.** The "Complexa" pipeline in [[ruijgrok-2026-binder-pipeline-comparison]] *is* Proteína-Complexa, run on *Plasmodium falciparum* LDH, and the two sources disagree on a load-bearing point.

**The contradiction, stated plainly.** This paper concludes that Complexa's self-generated sequences are good enough that MPNN redesign is unnecessary. [[ruijgrok-2026-binder-pipeline-comparison]] reports that in operation the headline metric is computed on `mpnn_fixed` redesigns **because** the co-designed `self` sequence carries an **antigen-copying defect** — 48 contiguous target residues reproduced inside a 79-residue binder, correlating with the search reward at ρ +0.54 — severe enough that the self sequence cannot be substituted. The same report finds that the AF2 gate **depletes** epitope contact rather than enriching it, and that placement and pass/fail, being read off different structures, agree at chance (Cohen's κ +0.006 and −0.091). The wiki's reading is that these are not contradictory measurements of one quantity but measurements of two different things — an *in silico* benchmark success rate and an operated pipeline's behaviour on a hard real target — and that the gap between them is the most instructive single fact available to this chapter.

A second, minor tension: Table 2 states that "RFDiffusion and Protpardelle only generate backbones and not their own sequences", while [[ruijgrok-2026-binder-pipeline-comparison]] records RFD3's output as observed all-atom at 6.4 atoms/residue with a low-entropy co-designed sequence (while noting RFD3's own QC comments call it backbone-only). Unresolved in both sources.

## Connections

- Unifies the generative lineage ([[watson-2023-rfdiffusion]], [[butcher-2025-rfdiffusion3]], [[ingraham-2023-chroma]], [[chu-2024-protpardelle]]) with the hallucination lineage ([[anishchenko-2021-hallucination]], [[wicky-2022-symmetric-assembly-design]], [[frank-2024-relaxed-sequence-optimization]]).
- Names BindCraft (Pacesa et al. 2025) and BoltzDesign as its hallucination baselines — currently the wiki's only citable reference for either; see [[bindcraft]] and the flagged references in [[de-novo-binder-design]].
- Contrasts with [[cho-2025-protein-hunter]], which reaches a similar unification by hallucinating *inside* a diffusion-based structure predictor with no fine-tuning at all.
- Benchmarks against [[chu-2024-protpardelle]] and [[watson-2023-rfdiffusion]]; uses [[jumper-2021-alphafold2]] confidence as reward.
- Contradicted on MPNN redesign by [[ruijgrok-2026-binder-pipeline-comparison]] (see above); tool page [[complexa]].
- Chapter: [[de-novo-binder-design]] §10, §11.
