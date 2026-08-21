---
type: source
title: Scaffolding protein functional sites using deep learning
authors: Wang, Lisanza, Juergens et al. (Baker lab)
venue: Science 2022
pdf: "../sources/ProteinDesign/WangBaker_Science_2022_Scaffolding protein functional sites using deep learning.pdf"
supp: missing-requested
tags: [motif-scaffolding, hallucination, inpainting, functional-site, de-novo]
ingested: 2026-07-13
---

# Scaffolding protein functional sites using deep learning

Introduces the two deep-learning routes to **motif scaffolding** — building a protein around a fixed functional site — that RFdiffusion later generalized. The conceptual bridge from prediction networks to functional de novo design.

**Problem.** Protein function usually lives in a small **functional site** (enzyme active site, metal or ligand/peptide binding site). Given a site's geometry and identities (from quantum chemistry, fragment docking, or extracted from a native protein), the design task is to build a full protein that holds that site in place — the "scaffolding" step.

**Approach.** Two complementary methods built on the RoseTTAFold/trRosetta networks:

- **Constrained hallucination** — "partially constrained hallucination with a multiobjective loss": optimize a sequence (by MCMC / gradient) so the network both confidently folds it and places the fixed motif at the target geometry. Flexible but compute-intensive.
- **Inpainting (RFjoint)** — start from the functional site and let a single network forward pass **complete/"inpaint"** the missing sequence and structure around it. Much faster; one pass instead of an optimization loop.

**Key results.**

- Successfully scaffolds diverse sites — metal-binding, enzyme active sites, small-molecule and protein-binding motifs, viral epitopes — with crystal and NMR structures confirming the designs fold as intended and present the site.
- Establishes the "motif in → scaffold out" formulation and the pairing of a generator with an AF2-style self-consistency check.

**Significance.** [[watson-2023-rfdiffusion]] directly generalizes both ideas (its conditional training for motif scaffolding is the diffusion successor to inpainting/hallucination). This paper defines the [[motif-scaffolding]] concept the wiki now tracks, and the hallucination idea reappears in [[symmetric-assembly-design]].

**Connections.**

- Direct precursor to [[watson-2023-rfdiffusion]] (motif scaffolding) — see [[watson-2023-rfdiffusion-supp]] §3.2.
- Hallucination engine inherited from [[anishchenko-2021-hallucination]]; shared with [[wicky-2022-symmetric-assembly-design]]. The three papers are the same method under three different loss functions — confidence alone, confidence + motif, confidence + symmetry.
- Sequences finalized with [[proteinmpnn]]; filtered with [[alphafold]]2. Concept: [[motif-scaffolding]].
