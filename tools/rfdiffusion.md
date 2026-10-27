---
type: tool
tags: [diffusion, backbone-generation, baker-lab]
sources: 1
updated: 2026-07-10
---

# RFdiffusion

Baker-lab diffusion generative model for protein backbones, made by fine-tuning the RoseTTAFold predictor on a structure-denoising task. Introduced in [[watson-2023-rfdiffusion]].

**Capabilities.** Unconditional and topology-constrained monomers, symmetric oligomers, metal-binding and enzyme active-site (motif) scaffolding, and de novo binder design against target hotspots.

**Pipeline role.** Stage 1 (backbone) of: **RFdiffusion → [[proteinmpnn]] (sequence) → [[alphafold]]2 (filter)**. Belongs to [[diffusion-generative-design]]; applied heavily to [[binder-design]].

**Lineage.** Precursors — unconstrained hallucination ([[anishchenko-2021-hallucination]]), then hallucination/inpainting with motif constraints ([[wang-2022-functional-site-scaffolding]]) and symmetric hallucination ([[wicky-2022-symmetric-assembly-design]]) — are generalized by RFdiffusion's conditional diffusion; each precursor's bespoke loss term becomes a conditioning input.

**Competition.** The hallucination line it superseded has since returned: [[frank-2024-relaxed-sequence-optimization]] reports better designability than RFdiffusion for large proteins and viable designs to 1000 residues, against RFdiffusion's difficulty beyond ~600, at comparable GPU cost per success. Successors — the all-atom RFdiffusionAA ([[krishna-2024-rosettafold-all-atom]]) and the efficient token+atom [[rfdiffusion3]] ([[butcher-2025-rfdiffusion3]]).

**Contrast:** [[chroma]] reaches similar ends via a bespoke correlated-noise prior; [[protpardelle]] via all-atom superposition — rather than fine-tuning a predictor.
