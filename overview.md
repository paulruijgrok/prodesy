---
type: overview
tags: [synthesis]
sources: 13
updated: 2026-07-13
---

# Overview — Deep learning for protein design

Evolving synthesis of the Prodesy wiki. Current scope: the deep-learning core (batch 1) plus the generative-design expansion (batch 2). Will broaden as more of `sources/ProteinDesign/` is ingested.

## The through-line

A single pipeline now organizes the field:

> **generate a backbone → design its sequence → predict/filter before you build**

- **Generate** — [[diffusion-generative-design]]: [[watson-2023-rfdiffusion]] (fine-tuned RoseTTAFold) and, independently, [[ingraham-2023-chroma]] (bespoke polymer-aware diffusion) sample novel, steerable backbones.
- **Sequence** — [[sequence-design]]: [[dauparas-2022-proteinmpnn]] assigns a foldable sequence to a backbone in seconds, displacing Rosetta.
- **Filter** — [[structure-prediction]]: [[jumper-2021-alphafold2]] confidence scores decide, *in silico*, which designs are worth synthesizing.

[[bennett-2023-binder-design-dl]] shows the payoff concretely: dropping ProteinMPNN + AF2 filtering into the older Rosetta binder workflow raised success ~10×. [[binder-design]] is the clearest application of the whole stack.

## How the pipeline was built and where it's going (batch 2)

- **Precursors.** Before diffusion, the same goals were met by **network hallucination** and **inpainting**. [[anishchenko-2021-hallucination]] established the method — invert a structure predictor by optimizing a random sequence until the network's own prediction sharpens — and [[wang-2022-functional-site-scaffolding]] ([[motif-scaffolding]]) and [[wicky-2022-symmetric-assembly-design]] ([[symmetric-assembly-design]]) are the same engine under two additional loss terms. RFdiffusion later absorbed all of it as conditional-diffusion tasks: what was a bespoke objective becomes a conditioning input.
- **Symmetric assemblies are now a chapter.** [[symmetric-oligomer-design]] traces the longest continuous arc in the wiki, from [[harbury-1993-coiled-coil-oligomer-switch]] through the parametric era ([[huang-2014-parametric-helical-bundles]], [[thomson-2014-alpha-helical-barrels]], [[boyken-2016-hydrogen-bond-network-oligomers]], [[courbet-2022-axle-rotor-assemblies]]) to hallucination and conditional diffusion.
- **All-atom is the current frontier**, pursued by ≥3 distinct routes: atomize-in-predictor ([[krishna-2024-rosettafold-all-atom]]), intrinsic side-chain **superposition** ([[chu-2024-protpardelle]], Huang lab), and efficient **token+atom** generation ([[butcher-2025-rfdiffusion3]], ~10× cheaper, DNA binders). This mirrors, on the design side, AF3's all-atom move on the prediction side.
- **Sequence design is converging on codesign.** [[dauparas-2022-proteinmpnn]] and the learned-potential [[anand-2022-learned-potential-seqdesign]] (Huang lab) both showed learned energies beat Rosetta; Protpardelle now folds sequence *into* generation.
- **Applications reach harder targets.** [[vasquez-torres-2023-helical-peptide-binders]] extends [[binder-design]] to floppy peptide hormones via **partial diffusion**, and turns binders into biosensors.

## Cross-cutting observations

- **Prediction ⇄ design convergence.** Prediction models are reused as design oracles (AF2 filtering) and as generators (RoseTTAFold → RFdiffusion). Meanwhile prediction itself adopted diffusion in [[abramson-2024-alphafold3]]. The two problems are merging onto shared machinery.
- **Independent replication of the paradigm.** RFdiffusion (Baker lab) and Chroma (Generate Biomedicines) arrived at diffusion-based design separately — a sign the approach is robust rather than a single group's trick. A worthwhile open comparison: fine-tuned-predictor vs. purpose-built noise prior.
- **Validation discipline is the real unlock.** The recurring lesson across sources is not just better generators but cheap, reliable *in silico* filtering that collapses wet-lab search space.
- **Conditioning moved from the coordinates into the sampling process.** Symmetric design is the cleanest place to watch this happen: symmetry was first *built into* a coordinate generator ([[huang-2014-parametric-helical-bundles-supp]]), then *rewarded* in a loss against a predictor ([[wicky-2022-symmetric-assembly-design]]), then *projected* onto the state at every denoising step ([[watson-2023-rfdiffusion-supp]]). The wiki's reading, developed in [[symmetric-oligomer-design]], is that this shift traded a geometry bottleneck for an interface-quality bottleneck — coverage improved far faster than yield.
- **The pre-deep-learning literature is doing real work.** Batch 3 showed that the wiki's synthesis was resting on Baker-lab-2022-onward sources alone for a problem with a thirty-year history. Where a chapter's claims trace only to recent papers, that is worth treating as a gap rather than a summary.
- **Generative models inherit priors nobody asked for.** [[anishchenko-2021-hallucination]] modelled every design as a monomer and got homo-oligomers and soluble aggregates anyway, because trRosetta had learned the sequence signatures of native protein–protein interfaces and did not disfavour surface hydrophobics enough. The same bias shows up as adversarial surfaces in [[wicky-2022-symmetric-assembly-design]]. The wiki's reading is that a predictor-derived generator carries its training distribution's interface statistics into every design, which is sometimes the capability and sometimes the bug — see [[symmetric-oligomer-design]] §5.1.

## Open threads to pursue (next batches / queries)

- **Prediction ecosystem** (batch 3): ColabFold, Foldseek, lDDT, Boltz/Boltzgen — the tooling around the predictors used as design oracles.
- **Surface-fingerprint design** (MaSIF, Gainza Nature + Nature Methods) — a distinct, non-diffusion paradigm for interaction design to contrast with [[binder-design]].
- **Antibody-specific design** (Bennett RFdiffusion antibodies +supp, IgLM) as a sub-branch of [[binder-design]].
- **Remaining generative models**: Boltzgen, Protein Hunter, DidiKreis test-time compute — to keep [[diffusion-generative-design]] current.
- Add a `benchmarks/` thread (CASP, sequence recovery, binder success rates, the RFD3 PPI/DNA/small-molecule/AME suites) to make cross-paper numbers comparable.
- **Protein dynamics** (Kern lab papers already in folder) — a different lens (conformational ensembles) largely absent from the current design-centric synthesis.
