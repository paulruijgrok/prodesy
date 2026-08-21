---
type: source
title: De novo design of high-affinity binders of bioactive helical peptides
authors: Vázquez Torres, Leung, Venkatesh et al. (Baker lab)
venue: Nature 2023
pdf: "../sources/ProteinDesign/VasquesTorres_Baker_Nature_2023_De novo design of high-affinity binders of bioactive helical peptides.pdf"
supp: yes
tags: [binder-design, peptides, partial-diffusion, biosensors, application]
ingested: 2026-07-13
---

# De novo design of high-affinity binders of bioactive helical peptides

Applies the generative design stack to a hard, high-value target class: **flexible α-helical peptide hormones** (parathyroid hormone, glucagon, secretin, neuropeptide Y, GLP1, GIP, BH3 peptides), producing high-affinity binders and turning them into biosensors.

**Problem.** Many peptide hormones fold into an α-helix only upon binding their receptor; free in solution they are floppy. Designing binders to such conformationally heterogeneous targets — and detecting these hormones sensitively — was an unmet challenge that general binder design hadn't cracked.

**Approach.** Combines parametric generation with [[watson-2023-rfdiffusion]] and **partial diffusion** (noise an existing design partway, then denoise to refine/diversify while preserving the fold), then sequences with [[proteinmpnn]] and filters with [[alphafold]]2. Binders are built to clamp the peptide in its helical conformation.

**Key results.**

- High-affinity, high-specificity binders across a panel of helical peptide hormones — a target class previously out of reach.
- Binders converted into **biosensors** (e.g., luminescent split-reporter / NanoBiT-style readouts) for detecting the hormones.
- Extensive experimental validation (yeast-surface display, SPR, biochemistry — see the SI).

**Significance.** A capstone *application* of the batch-1 stack: shows the generate→sequence→filter pipeline plus **partial diffusion** extends [[binder-design]] to flexible, biomedically important targets, and that designed binders are directly useful as diagnostics.

**Connections.**

- Built on [[watson-2023-rfdiffusion]] (+ partial diffusion), [[proteinmpnn]], [[alphafold]]2 filtering.
- Application within [[binder-design]]; contrast with ligand-conditioned [[krishna-2024-rosettafold-all-atom]].
- **Supplement:** [[vasquez-torres-2023-helical-peptide-binders-supp]] — experimental methods (yeast display, SPR, biosensor assays).
