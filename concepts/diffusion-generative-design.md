---
type: concept
tags: [diffusion, generative, de-novo]
sources: 6
updated: 2026-07-13
---

# Diffusion generative design

Generating novel protein backbones (and complexes) by learning to reverse a noising process — the paradigm that now dominates de novo structure generation.

**Two independent demonstrations (2023).** [[watson-2023-rfdiffusion]] fine-tunes the RoseTTAFold predictor into a backbone denoiser, excelling at monomers, symmetric assemblies, motif scaffolding and binders. [[ingraham-2023-chroma]] builds a from-scratch diffusion model with a polymer-statistics-aware noise prior and programmable (including natural-language) conditioning. Different lineages, same conclusion: diffusion works for proteins.

**Convergence with prediction.** [[abramson-2024-alphafold3]] adopts a diffusion coordinate head for *prediction*, so prediction and design increasingly share machinery.

**Going all-atom.** [[krishna-2024-rosettafold-all-atom]]'s denoising fine-tune (RFdiffusionAA) diffuses protein backbones *around* a small-molecule ligand — extending diffusion design from protein-only to ligand-conditioned [[binder-design]] (validated for digoxigenin, heme, bilin).

**Conditioning is the point.** The value is steerability — hotspots for binders, symmetry operators, fixed functional motifs, shape/semantic constraints. Backbones are then sequenced by [[sequence-design]] ([[proteinmpnn]]) and filtered by [[structure-prediction]].

**All-atom generation — three routes.** The field is now pushing past backbone-only generation: [[krishna-2024-rosettafold-all-atom]] atomizes ligands inside a predictor (RFdiffusionAA); [[chu-2024-protpardelle]] (Huang lab) makes side-chain generation intrinsic via a "superposition + collapse" scheme, codesigning sequence; and [[butcher-2025-rfdiffusion3]] uses a token+atom sparse architecture to hit prior quality at ~10× less compute across ligand/nucleic-acid/enzyme tasks.

**Open contrast to file:** fine-tuned-predictor (RFdiffusion) vs. bespoke correlated-noise prior (Chroma) vs. superposition all-atom (Protpardelle) vs. token+atom sparse (RFD3) — tradeoffs not yet resolved in these sources.

**Sources:** [[watson-2023-rfdiffusion]], [[ingraham-2023-chroma]], [[abramson-2024-alphafold3]], [[krishna-2024-rosettafold-all-atom]], [[chu-2024-protpardelle]], [[butcher-2025-rfdiffusion3]].
