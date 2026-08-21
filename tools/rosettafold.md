---
type: tool
tags: [structure-prediction, all-atom, baker-lab]
sources: 2
updated: 2026-07-13
---

# RoseTTAFold

Baker-lab protein structure predictor — the parallel lineage to DeepMind's [[alphafold]], and the backbone repurposed for generative design.

**Lineages.**

- **RoseTTAFold / RF2** — three-track (1D sequence / 2D pair / 3D structure) prediction network.
- **RoseTTAFold All-Atom (RFAA)** ([[krishna-2024-rosettafold-all-atom]]) — adds an atomic representation so one model covers proteins + nucleic acids + small molecules + metals + covalent mods; its denoising fine-tune is **RFdiffusionAA** for small-molecule binder design.

**Design significance.** Fine-tuning the RoseTTAFold network on structure denoising produced [[rfdiffusion]] ([[watson-2023-rfdiffusion]]) — i.e. the predictor *is* the generator's starting point. RoseTTAFold is also used alongside [[alphafold]]2 as an *in silico* filter in [[bennett-2023-binder-design-dl]].

See [[structure-prediction]], [[diffusion-generative-design]].
