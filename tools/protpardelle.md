---
type: tool
tags: [diffusion, all-atom, huang-lab]
sources: 1
updated: 2026-07-13
---

# Protpardelle

Huang-lab all-atom protein diffusion model that generates backbone and side chains together. Introduced in [[chu-2024-protpardelle]].

**Key idea.** Represents all side-chain states as a **"superposition"** that is **collapsed** to specific residue identities/conformations during sampling; sequence is set by a **miniMPNN** in an EM-like loop, giving **all-atom structure+sequence codesign**. Scaffolds motifs backbone- and rotamer-free. Architecture: **U-ViT** noise-conditional transformer (SI).

**Context.** Independent, non-Baker-lab route to all-atom [[diffusion-generative-design]]; contrast with atomize-in-predictor [[krishna-2024-rosettafold-all-atom]] and token/atom [[rfdiffusion3]]. See [[chu-2024-protpardelle-supp]].
