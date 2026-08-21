---
type: source-supp
parent: "[[vasquez-torres-2023-helical-peptide-binders]]"
title: De novo design of high-affinity binders of bioactive helical peptides — Supplementary Information
pdf: "../sources/ProteinDesign/VasquesTorres_Baker_Nature_2023_De novo design of high-affinity binders of bioactive helical peptides_supp.pdf"
tags: [binder-design, methods, experimental, yeast-display, biosensors]
ingested: 2026-07-13
---

# Helical peptide binders — Supplementary Information (companion)

Methods companion to [[vasquez-torres-2023-helical-peptide-binders]]. 32 pages, heavily **experimental** — the wet-lab protocols behind the designs, which the main text compresses.

## What the SI contains (map)

- **Computational design methods** — parametric generation + [[rfdiffusion]] + partial-diffusion refinement; [[proteinmpnn]] sequence design; [[alphafold]]2 filtering settings; identification of weak binder hits from parametric designs.
- **Experimental methods** — E. coli expression optimization; DNA eBlocks cloned into **pETcon3 yeast-display** vector; yeast transformation and **FACS sorting** of design libraries; protein purification.
- **Binding & biosensor assays** — split-luciferase (**smBiT/NanoBiT**) lysate assays in microplates; binding-curve titrations; SPR/affinity measurements.

## Key extracted details

- **Yeast surface display + FACS** is the screening workhorse: designs are displayed on yeast and sorted for peptide binding, the empirical funnel that turns filtered designs into validated binders.
- **Split-luciferase (smBiT) reporter** assays are how binders are converted into **biosensors** — the mechanism behind the diagnostic application in the main text.
- **Partial diffusion** is used as a refinement/diversification operator on parametric or initial designs (noise partway, denoise) — the concrete recipe for improving weak parametric hits.

## Connections

- Parent: [[vasquez-torres-2023-helical-peptide-binders]]; concept [[binder-design]].
- Shares the generate→sequence→filter machinery detailed in [[watson-2023-rfdiffusion-supp]] and the metric logic of [[bennett-2023-binder-design-dl-supp]].
