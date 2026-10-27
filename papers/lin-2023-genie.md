---
type: source
title: Generating Novel, Designable, and Diverse Protein Structures by Equivariantly Diffusing Oriented Residue Clouds
authors: Lin & AlQuraishi (Columbia)
venue: ICML 2023 (PMLR 202); arXiv:2301.12485v3, 6 June 2023
pdf: "../sources/ProteinDesign/LinAlQurashi_arXiv_2023_Generating Novel, Designable, and Diverse Protein Structures by Equivariantly Diffusing Oriented Residue Clouds.pdf"
supp: no
tags: [diffusion, se3-equivariance, backbone-generation, designability, diversity, novelty, foundational]
ingested: 2026-10-20
---

# Genie — diffusing oriented residue clouds

The founding paper of the Genie lineage. Its contribution is a deliberate **asymmetry**: represent a protein as a plain point cloud of Cα coordinates in the *forward* (noising) process, and as a cloud of **oriented reference frames** in the *reverse* (generation) process.

**Reference.** Lin, Y. & AlQuraishi, M. *Generating Novel, Designable, and Diverse Protein Structures by Equivariantly Diffusing Oriented Residue Clouds.* Proceedings of the 40th International Conference on Machine Learning, PMLR 202 (2023). Preprint arXiv:2301.12485. This is the "Genie 1" that [[lin-2026-genie3]] cites as `Lin & AlQuraishi (2023)`. `supp: no` — appendices A–D are inside the same 25-page PDF.

## Problem

Evolution has explored only a small subregion of foldable protein space, which is the opening argument for designing proteins unlike any in nature. Historically design optimised natural proteins by directed evolution or designed sequences hewing closely to known structural motifs, which confined exploration to regions adjacent to natural proteins. The then-new alternative was to invert a structure predictor: [[anishchenko-2021-hallucination]] performed Monte Carlo sampling in sequence space guided by trRosetta and did discover novel structures, but the paper's stated objection is the **reliance on sampling**, which "can be computationally expensive and difficult to steer toward desirable design goals". Generative models offer the alternative of implicitly learning the space of structures instead of searching it.

The paper frames the design target as three simultaneous criteria — **designable** (realisable by some sequence), **novel** (geometrically dissimilar from natural proteins), **diverse** (spanning a wide range of geometries) — and situates diffusion models against a **generative trilemma** between quality, mode coverage and sampling time, with GANs and VAEs making different trade-offs.

## Approach

**The asymmetry is the idea.** Invariant Point Attention from AlphaFold2 reasons over reference frames rather than points, which retains angular information between residues and so accounts for chirality. Anand & Achim (2022) had already combined IPA with diffusion, but Genie introduces a **geometric asymmetry**: residues are a point cloud of Cα coordinates in the forward process and a cloud of **Frenet–Serret reference frames** in the reverse process, each frame giving a residue's position and orientation relative to the global frame. The payoff is stated plainly — this "yields a simple and cheap process for noising structures while retaining the full expressivity of IPA during generation, without violating the Gaussian assumption of DDPMs".

Discrete-time DDPM with **T = 1,000** diffusion steps on a cosine variance schedule; isotropic Gaussian noise added to Cα coordinates in the forward process; the loss follows Ho et al. in predicting the noise ε rather than the reverse-process mean. FS frames are constructed from the noised backbone geometry at each step, so IPA can reason about relative orientations. An implementation detail recorded because it recurs in the lineage: the frames of the second and second-to-last residues are assigned to the first and last residues.

Sampling draws Cα coordinates from an isotropic Gaussian and runs the reverse process to step 0. For the long models, sampling noise is scaled by a constant η — low-temperature sampling — following RFdiffusion and FrameDiff.

## Training data — where the 256-residue ceiling begins

Two datasets, and both caps matter for the lineage:

- **SCOPe** — domains filtered so no two share >40% sequence identity, with multi-chain domains and those missing backbone atoms removed. **8,766 domains**, of which **3,942 have at most 128 residues and 7,249 have at most 256**.
- **AlphaFold-SwissProt** — filtered at **pLDDT > 80**, giving **195,214 structures having at most 256 residues**.

The trained models use **maximum sequence length 128** for the "short" comparisons and **256** for the "long" comparisons. So the 256-residue ceiling that [[lin-2026-genie3]] still carries, and that it cites as the basis of its out-of-domain generalisation claim, originates here — and in this paper it is a property of the evaluation design rather than a stated computational constraint (the constraint is made explicit in [[lin-2024-genie2]]).

## Key results

**Against short models** (ProtDiff, FoldingDiff; 10 proteins per length from 50 to 128 residues; designability by **scTM** — ProteinMPNN at temperature 0.1 generating 8 sequences per structure, then OmegaFold prediction, then TM-score back to the generated structure, with OmegaFold substituted for AlphaFold2 because it outperforms it on single-sequence prediction):

- **58.3% of Genie domains are "confidently designable"** (scTM > 0.5 and predicted pLDDT > 70), against **3.2% for ProtDiff and 17.7% for FoldingDiff**.
- Novelty: **98 of 455 (21.5%)** confidently designable Genie structures are novel (max TM-score to the training set < 0.5), against 4% (1/25) for ProtDiff and 20.3% (28/138) for FoldingDiff.

**Against long models** (FrameDiff and RFdiffusion; Chroma excluded because its source was not public; 5 proteins per length from 50 to 256; designability by **scRMSD < 2 Å and pLDDT > 70** via the ProteinMPNN–ESMFold pipeline, chosen for consistency with RFdiffusion and FrameDiff; diversity as clusters per generated structure under single-linkage TM-score 0.6; F1 as the harmonic mean of designability and diversity):

| Method | Params | Designability | Diversity | F1 | Novelty |
|---|---|---|---|---|---|
| FrameDiff | 17.4 M | 0.483 | 0.590 | 0.531 | 0.006 |
| RFdiffusion | 59.8 M | **0.951** | 0.667 | **0.784** | **0.170** |
| Genie-SCOPe | **4.1 M** | 0.586 | **0.738** | 0.654 | 0.039 |
| Genie-SwissProt | **4.1 M** | 0.790 | 0.642 | 0.708 | 0.041 |

The honest summary the paper gives of its own position: Genie **outperforms FrameDiff on sampling quality even when trained on the smaller SCOPe dataset, but underperforms RFdiffusion**, and increasing the training set markedly improves quality while RFdiffusion "retains an edge". It wins on diversity. It also notes the trade-off directly — with a larger dataset Genie gains designability "at the cost of reduced diversity, likely due to small model size".

**The parameter count is the result that ages best.** Genie reaches 0.790 designability and 0.642 diversity with **4.1 M parameters** against RFdiffusion's 59.8 M — a model roughly **14.6× smaller**. That is the data- and parameter-efficiency argument for SE(3)-equivariance, made here as a passing observation and revived three years later as the central thesis of [[lin-2026-genie3]], after the field had spent the interval moving the other way.

**Diversity is measured against RFdiffusion's own protocol**, including the TM-score 0.6 single-linkage clustering, so the diversity comparison is like-for-like. On secondary-structure diversity the paper concedes that FrameDiff and RFdiffusion "show greater SSE diversity, particularly for beta sheets".

## Significance / relation to the field

Three things this page supplies that the wiki did not have.

1. **The origin of the representation that [[lin-2026-genie3]] generalises.** Genie 3's branched-polymer treatment is described there as retaining "the frame-based representation of Genie 2 but generalis[ing] it to the branched polymer nature of proteins", and Genie 2's frames are these frames. Genie 3 defers to this paper and [[lin-2024-genie2]] for the architectural details it does not restate, so without this page that chapter section rests on a citation the wiki could not follow.
2. **A contemporaneous, independent arrival at diffusion for proteins.** [[overview]] already notes that RFdiffusion and [[ingraham-2023-chroma]] arrived at diffusion-based design separately. Genie is a third, from a third group, with a fourth mechanism — and it is the only one of the four that is SE(3)-equivariant end to end while diffusing coordinates.
3. **The scTM-to-scRMSD transition, documented.** The paper uses scTM for short models and switches to the stricter scRMSD for long ones, explaining that RMSD's sensitivity to small structural differences makes it more suitable for more capable models. Any comparison of designability numbers across the 2022–2023 literature has to know which metric was in play; this is the wiki's clearest statement of the distinction.

**For the binder chapter**, this page matters mainly as lineage: Genie 1 has no binder or motif capability at all, which is what makes the conditional machinery of [[lin-2024-genie2]] and the interface conditioning of [[lin-2026-genie3]] legible as two successive additions rather than a single design.

## Connections

- Succeeded by [[lin-2024-genie2]] (motif scaffolding, AFDB data augmentation) and [[lin-2026-genie3]] (atomistic SE(3)-equivariance, binder design); tool page [[genie]].
- Builds the IPA machinery of [[jumper-2021-alphafold2]] into a generative model; positions itself against the sampling cost of [[anishchenko-2021-hallucination]].
- Contemporaneous with and benchmarked against [[watson-2023-rfdiffusion]]; names [[ingraham-2023-chroma]] as a parallel approach it could not benchmark because the code was not public at the time.
- Uses [[dauparas-2022-proteinmpnn]] for inverse folding in both evaluation pipelines.
- Concepts: [[diffusion-generative-design]], [[structure-prediction]].
