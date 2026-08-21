---
type: source-supp
parent: "[[ingraham-2023-chroma]]"
title: Illuminating protein space with a programmable generative model — Supplementary Information
pdf: "../sources/ProteinDesign/IngrahamGregoryan_Nature_2023_Illuminating protein space with a programmable generative model_supp.pdf"
tags: [diffusion, methods, architecture, polymer-prior, conditioners, sampling]
ingested: 2026-07-13
---

# Chroma — Supplementary Information (companion)

Theory/methods companion to [[ingraham-2023-chroma]]. 123 pages — the mathematical core behind Chroma's distinctive design choices (correlated-noise diffusion, sub-quadratic graph network, programmable conditioners).

## What the SI contains (map)

- **A. Overview & Conditioners** — the modular conditioning system (symmetry, substructure, shape, semantic class, natural-language/ProCap).
- **B. Diffusion with structured correlations** — key trick: **correlated diffusion reframed as uncorrelated diffusion in a transformed space**; noise scheduling to balance signal/noise; sampling via the **reverse-time SDE** and the **probability-flow ODE**; **conditional sampling from the posterior under auxiliary constraints** (design = Bayesian inference).
- **C. Low-temperature sampling** for diffusion models (sharpening samples toward high-density regions).
- **D. Polymer-structured diffusions** — the **covariance models** that make noised structures behave like real chains: *Ideal Chain*, *Rg-confined Globular Polymer*, and the *Residue Gas* alternative; analysis of how diffusion predictably affects inter-residue distances.
- **E. Random Graph Neural Networks** — random graph generation giving **sub-quadratic** scaling for long-range reasoning over large systems.
- **F. Structure from inter-residue geometry** — **equivariant structure updates via convex optimization**; equivariant prediction of backbone atoms.
- **G. Architecture / H. Training / Sampling** — full model spec and protocols.

## Key extracted details

- **The polymer prior is the signature idea.** Instead of independent Gaussian noise per atom (which would inflate the chain to implausible extension), Chroma diffuses under a **covariance that matches polymer statistics** (ideal-chain / Rg-confined globular). This keeps intermediate states realistic and is the principled contrast to [[rfdiffusion]]'s fine-tuned-predictor approach — see [[diffusion-generative-design]].
- **Correlated → uncorrelated transform (B.1)** is what makes training/sampling under that structured covariance tractable.
- **Design as Bayesian inference (B.7):** conditioners enter as likelihood/constraint terms on the diffusion posterior, giving a unified way to impose symmetry, shape, substructure or a text prompt.
- **Sub-quadratic random-graph attention (E)** is the efficiency enabler for whole-complex generation; the equivariant convex-optimization step (F) synthesizes 3D coordinates from predicted inter-residue geometry.

## Connections

- Parent: [[ingraham-2023-chroma]]; concept [[diffusion-generative-design]].
- Its polymer-covariance prior is the concrete axis of contrast with [[watson-2023-rfdiffusion-supp]] (fine-tuned RoseTTAFold vs bespoke prior).
- Shares the diffusion-sampling toolkit (reverse-time SDE / probability-flow ODE) with [[abramson-2024-alphafold3-supp]].
