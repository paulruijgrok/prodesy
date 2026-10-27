---
type: tool
tags: [binder-design, flow-matching, test-time-compute, latent, pretraining]
sources: 3
updated: 2026-10-17
---

# Proteína-Complexa

A fully atomistic binder generator built to **unify conditional generation with inference-time optimisation**, on the argument that the field's generative-versus-hallucination split is a false dichotomy. Introduced in [[didi-2026-complexa-scaling]].

**Three components** ([[didi-2026-complexa-scaling]]).

1. **Teddymer** — a large-scale synthetic pretraining dataset built by treating the **domain–domain interactions of computationally predicted monomeric structures** as surrogate binder–target complexes, then filtering. Used in a stagewise recipe: pretrain on synthetic and AFDB-derived data, post-train on high-quality experimental multimers.
2. **A partially latent architecture** — flow matching over a representation that is part explicit coordinate, part latent: a **Cα-only coordinate variable plus per-residue local latents**, decoded to all-atom structure *and* sequence by a separate autoencoder. Chosen for scalability, because binder design means generating many candidates.
3. **Inference-time optimisation** — best-of-N, beam search, **Feynman–Kac steering** (importance sampling of a tilted distribution), and MCTS, with AlphaFold2-Multimer interface pAE as the reward.

**Reported performance.** Without any test-time optimisation: 9.10 unique successes on self-generated sequences and 14.4 with ProteinMPNN redesign, against 4.68 for RFdiffusion and 0.73 for Protpardelle-1c under redesign, at 15.6 s per sample. With test-time search: beats the hallucination baselines [[bindcraft]] and BoltzDesign under **normalised compute budgets** measured in test-time GPU-hours. Also extended to interface hydrogen-bond optimisation, fold-class-guided generation, small-molecule targets and an enzyme-design benchmark ([[didi-2026-complexa-scaling]]).

**As operated in this project** ([[ruijgrok-2026-binder-pipeline-comparison]]) — and this is where the tool page earns its keep, because the operational record and the paper disagree.

- **Test-time search is on in production**: beam search with n_branch 4 and beam_width 8 over partial trajectories at five step checkpoints, AlphaFold2-multimer i_pAE as the sole reward with every other term zeroed. It is the only project pipeline with genuine verifier-guided search.
- **It is by far the most expensive**: 8,587.2 GPU-hours over 11,810 tasks — 83% of the project's entire generation+scoring budget — at **54.60 GPU-minutes per design**, roughly 6.5× the cheapest pipeline there.
- **The target is context, not a motif**: `binder_gen_only: True`, with target conditioning all-atom but the target chains **re-generated rather than copied** — the origin of an antigen-copying defect.
- **The co-designed sequence is unusable on that target.** The defect is 48 contiguous target residues reproduced inside a 79-residue binder, correlating with the search reward at ρ +0.54, which is why the project's headline metric is computed on MPNN redesigns. [[didi-2026-complexa-scaling]] concludes the opposite — that self-generated sequences make MPNN redesign "unnecessary". The wiki's reading is that these measure different things (an *in silico* benchmark versus an operated pipeline on a hard target) and the gap between them is the most instructive single fact in [[de-novo-binder-design]]; see §9 and §13 there.
- **Its gate selects against its own objective.** Placement and pass/fail are read off different structures and agree at chance (Cohen's κ +0.006 and −0.091), and the AF2 gate **depletes** epitope contact rather than enriching it.
- **Watch the representation**: the evaluation stage writes a **Cα-only** file, and that is what interface-residue and contact counts are read from, while the sequence designer receives the all-atom file.
- **It degrades silently**: a JAX preallocation failure drops the AF2 reward to 0.0000 for a whole run and the job still exits 0.

**An independent evaluation is less flattering.** [[lin-2026-genie3]] ran Complexa against four other methods on ten AlphaProteo problems at a fixed 200-structure budget and found it "substantially" behind both Genie 3 and BindCraft. On inference-time scaling across the same problems Complexa won 1, tied 2 and lost 7, and **in four cases exhibited no scaling behaviour at all** while Genie 3 improved robustly with compute — the gains concentrated in multimeric targets. That paper also reports that without inference-time search, Complexa "performs better using ProteinMPNN-based sequence redesign than using its own sequence co-generation feature" — a third-party result siding with [[ruijgrok-2026-binder-pipeline-comparison]] against [[didi-2026-complexa-scaling]]'s own conclusion on this point.

**Connections.** Unifies the generative lineage ([[rfdiffusion]], [[rfdiffusion3]], [[chroma]], [[protpardelle]]) with the hallucination lineage ([[anishchenko-2021-hallucination]], [[wicky-2022-symmetric-assembly-design]], [[frank-2024-relaxed-sequence-optimization]]); contrast [[proteinhunter]], which reaches the same unification with no training at all, and [[genie]], which declines the unification and wins anyway. Concept [[binder-design]]; chapter [[de-novo-binder-design]] §9, §11.
