---
type: tool
tags: [diffusion, se3-equivariance, binder-design, motif-scaffolding, all-atom, alquraishi-lab]
sources: 3
updated: 2026-10-20
---

# Genie 3

The AlQuraishi-lab lineage of SE(3)-equivariant protein diffusion models, now fully ingested across three generations.

| Version | Source | What it added |
|---|---|---|
| **Genie** | [[lin-2023-genie]] · ICML 2023 | The founding asymmetry: Cα point cloud in the forward process, **oriented Frenet–Serret reference frames** in the reverse process, so IPA's full expressivity is available during generation without violating the Gaussian assumption of DDPMs. Unconditional only. 4.1 M parameters. |
| **Genie 2** | [[lin-2024-genie2]] · arXiv 2024 | **Motif scaffolding**, conditioned on one-hot motif sequence plus the motif's **Cα pairwise distance matrix** — SE(3)-invariant, so unlike fixed-coordinate conditioning it is insensitive to initial placement, and leaving inter-motif distances unspecified yields **multi-motif** scaffolding for free. Plus **AFDB data augmentation**: the first protein diffusion model trained on the AlphaFold Database. |
| **Genie 3** | [[lin-2026-genie3]] · bioRxiv 2026 | **Atomistic** detail via a branched-polymer frame construction with partial atomization; **binder design** with interface conditioning; 10× faster sampling. |

The current model is **Genie 3**; the sections below describe it unless stated otherwise.

**Representation.** The frame-based backbone representation of [[lin-2023-genie]] and [[lin-2024-genie2]], generalised to sidechains: backbone Frenet–Serret frames anchored at Cα relative to the preceding Cα, then sidechain FS frames constructed from the backbone frame in `atom14` ordering. **Partial atomization** means all-atom for known segments (motif residues) and backbone-only for scaffold residues ([[lin-2026-genie3]]).

**Denoiser.** SE(3)-invariant input embedder with optional sequence and structure conditions → trunk → SE(3)-equivariant structural decoder using Invariant Point Attention, with noise predicted as the displacement between updated and input frame translations ([[lin-2026-genie3]]).

**Sampling.** Low-temperature sampling by **directional scaling**: the reverse process is moderated through a direction scale η on the mean rather than Genie 2's noise scale γ on the variance, and Δt = 10 cuts sampling from 1,000 steps to **100 — 10× faster with negligible quality loss** ([[lin-2026-genie3]]). This is a direct answer to a limitation Genie 2 had stated against itself: 1,000 denoising iterations against 100 for FrameFlow, 500 for Chroma and 50 for RFdiffusion ([[lin-2024-genie2]]).

**Capabilities.** Unconditional generation (validated 50–800 residues), single- and multi-motif scaffolding, and binder design with hotspot conditioning.

**Training ceiling — the number to remember, and it is inherited.** Nothing in Genie 3's training exceeds **256 residues**. Monomeric data is FoldSeek-clustered AFDB representative clusters filtered to 20–256 residues inclusive at pLDDT ≥ 80 (587,479 structures, no experimentally determined monomeric structures at all); multimeric data is Pinder 2024-02 with the **whole complex** capped at 256 residues (135,745 structures, 5,331 interface clusters). Trained 9:1 motif-scaffolding to binder-design on 48 × A100 40 GB for ~15 days, 600,000 steps ([[lin-2026-genie3]]).

The ceiling runs the length of the lineage. [[lin-2023-genie]] trained its long models at a 256-residue maximum (SCOPe: 8,766 domains, 7,249 of them ≤256; AlphaFold-SwissProt at pLDDT > 80: 195,214 structures all ≤256). [[lin-2024-genie2]] states the reason — *"due to computational constraints, we limit sequence length to 256 during training; however, Genie 2 is capable of generating proteins longer than 256 residues"* — and attributes the O(N³) cost to AlphaFold2's triangular multiplicative update layers. So **all three generations are capped at 256 and all three claim length generalisation past it**; Genie 3's version of the claim is the third iteration of a standing house argument, not a new finding.

**A dataset discrepancy across the lineage**, recorded not resolved: [[lin-2024-genie2]] reports **588,570** structures for the AFDB training set, while [[lin-2026-genie3]] describes using "the same training dataset as Genie 2" and gives **587,479** — a difference of 1,091 structures. Neither paper explains it.

**Results across the lineage.** On unconditional generation (designability / diversity / F1 / PDB novelty), Genie 1 trailed RFdiffusion on designability — 0.790 vs 0.951, though at 4.1 M parameters against 59.8 M, roughly 14.6× smaller ([[lin-2023-genie]]) — while Genie 2 **matched** it at 0.96 and beat it substantially on diversity (0.91 vs 0.63) and PDB novelty (0.41 vs 0.26) ([[lin-2024-genie2]]). On single-motif scaffolding Genie 2 equalled or beat RFdiffusion in unique successes on 22 of 24 benchmark tasks and solved 5WN9, which RFdiffusion does not; it solved 4 of 6 curated multi-motif tasks, all out-of-distribution ([[lin-2024-genie2]]).

**Genie 3's results.** Best on **7 of 10** AlphaProteo binder problems, with BindCraft best on the other 3 and RFdiffusion, BoltzGen and Proteína-Complexa substantially behind; the margin over BindCraft widens once per-sample runtime is normalised. Ties Protpardelle-1c on MotifBench problems solved while scoring higher. In AdaptyvBio's blind Nipah challenge: 200 designs → 34 AF2M+ successes → top 8 by Boltz-2 ipSAE submitted → all 8 expressed, one at **K_D 92 nM**, a 1/8 hit rate, against aggregate 3/60, 1/100 and 2/288 for RFdiffusion, BindCraft and BoltzGen in the same competition ([[lin-2026-genie3]]).

**Two contributions to the tooling around oracles**, from the same paper. The **AF2M+ Benchmark** adds an on-target constraint to AlphaFold-Multimer filtering — ≥80% of user-specified interface residues within 5 Å of the binder (100% for interfaces of ≤3 residues) — introduced because designs were passing the unmodified benchmark while binding an off-target site. And the **extended** and **convergent** hotspot expansion heuristics, the latter defining the interface as the intersection of interface residues across successful designs from previous rounds, which applied iteratively to TNFα produced a nearly monotone climb in success rate with design round.

**Caution for use on large targets.** The project's PfLDH system is a 632-residue target in a 711-residue complex ([[ruijgrok-2026-binder-pipeline-comparison]]) — roughly 2.8× the largest complex in Genie 3's training set. Its demonstrated out-of-domain generalisation covers unconditional monomers to 800 residues and the AlphaProteo multimers, not targets of that size, so applying it there is an extrapolation past what the paper shows.

**A methodological contribution worth citing on its own.** [[lin-2024-genie2]] rejects *success rate* as the motif-scaffolding metric because "it is possible to achieve high success rates by repeatedly generating only one or a few successful designs, i.e., while suffering from mode collapse", and reports the **number of unique successes** after TM-score 0.6 clustering instead — the convention MotifBench later formalises and that [[lin-2026-genie3]] uses. The same paper notes that designability alone can be gamed by mode collapse, and that diversity is itself sample-size-dependent.

**Connections.** The only all-atom route in the wiki that retains SE(3)-equivariance; contrast [[krishna-2024-rosettafold-all-atom]], [[protpardelle]], [[rfdiffusion3]]. Direct competitor of [[bindcraft]], [[complexa]] and [[boltzgen]]. Uses [[proteinmpnn]] for inverse folding and [[alphafold]]-family models as oracles. Concept [[binder-design]]; chapter [[de-novo-binder-design]].
