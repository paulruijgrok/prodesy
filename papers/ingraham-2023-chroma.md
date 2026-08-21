---
type: source
title: Illuminating protein space with a programmable generative model
authors: Ingraham et al. (Generate Biomedicines)
venue: Nature 2023
pdf: "../sources/ProteinDesign/IngrahamGregoryan_Nature_2023_Illuminating protein space with a programmable generative model.pdf"
supp: yes
tags: [diffusion, backbone-generation, de-novo, programmable, conditioning]
ingested: 2026-07-10
---

# Chroma — A programmable generative model for proteins

A diffusion generative model for proteins and complexes developed independently of the Baker lab (Generate Biomedicines), notable for programmable conditioning — including natural-language and geometric constraints.

**Problem.** The space of possible proteins vastly exceeds the space of functional ones; sampling novel structures that are expressible, foldable and steerable toward desired properties is hard for both computation and experiment.

**Approach.** [[chroma]] introduces a diffusion process that respects **polymer-ensemble conformational statistics** (a correlated-noise prior matching realistic chain behavior), a sub-quadratic-scaling neural architecture for long-range reasoning over molecular systems, and layers that synthesize 3D structure from predicted inter-residue geometries. Design is framed as **Bayesian inference under external constraints**: symmetry, substructure, shape, semantic class, even natural-language prompts steer sampling.

**Key results.**

- Experimental characterization of **310 proteins**: sampled designs are highly expressed, fold, and show favorable biophysical properties.
- Crystal structures of two designs show atomistic agreement (~backbone RMSD on the order of an ångström) with the Chroma samples.
- Demonstrates conditioning on shape and text, illustrating "programmable" design.

**Significance.** A contemporaneous, independent confirmation that [[diffusion-generative-design]] works for proteins, from a different lineage than [[watson-2023-rfdiffusion]] — evidence the paradigm is robust, not method-specific. Its correlated-noise prior is a distinctive architectural choice worth contrasting with RFdiffusion's fine-tuned-predictor approach.

**Supplement:** [[ingraham-2023-chroma-supp]] — the theory: polymer-covariance diffusion prior (ideal-chain / Rg-confined), correlated→uncorrelated transform, reverse-time SDE & probability-flow ODE sampling, Bayesian conditioners, sub-quadratic random-graph network, equivariant convex-optimization structure step.

**Connections.**

- Diffusion sibling / independent counterpart to [[watson-2023-rfdiffusion]].
- Shares the generative diffusion paradigm now also in [[abramson-2024-alphafold3]].
- Core reference for [[diffusion-generative-design]].
