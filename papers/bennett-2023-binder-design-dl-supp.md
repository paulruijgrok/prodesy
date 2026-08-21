---
type: source-supp
parent: "[[bennett-2023-binder-design-dl]]"
title: Improving de novo protein binder design with deep learning — Supplementary Information
pdf: "../sources/ProteinDesign/BennettDaker_NatureCommunications_2023_Improving de novo protein binder design with deep learning_supp.pdf"
tags: [binder-design, methods, filtering, benchmarks, validation]
ingested: 2026-07-13
---

# Improving de novo binder design with DL — Supplementary Information (companion)

Data/validation companion to [[bennett-2023-binder-design-dl]]. 19 pages, mostly supplementary figures — the retrospective analysis that establishes *which* AF2 metrics discriminate real binders and *how well*.

## What the SI contains (map)

- **Fig S1–S3** — AF2 vs RF2 prediction accuracy (Cα RMSD) for experimentally determined minibinder monomer and complex structures; complex predictions run with **target template + the Rosetta-design model as an initial guess** (an important practical setting), validated on FGFR2, IL-7Rα and others.
- **Fig S4** — retrospective experimental success rate (YSD **SC50 < 4 µM**) as a function of RMSD-agreement thresholds between Rosetta and AF2 monomer/complex structures.
- **Fig S5** — correlation of AF2 confidence (**pLDDT** monomer, **pAE_interaction** complex) with Rosetta↔AF2 RMSD; AF2 vs RF2 confidence agreement.
- **Fig S6** — ROC/true-positive-rate analysis of the **discriminatory power** of each metric to separate successful (SC50 < 4 µM) from failed designs.
- **Fig S7** — experimental success of libraries designed by **ProteinMPNN vs Rosetta FastDesign**, both under DL filtering, across three prospective targets.

## Key extracted details

- The operational success criterion throughout is **yeast-surface-display SC50 < 4 µM**; the ~10× improvement in the main text is defined against this bar.
- The two workhorse metrics are **monomer pLDDT** (does it fold as designed?) and **pAE_interaction** (does it dock as designed?); Fig S6 quantifies their discriminative TPR — the empirical justification for using them as go/no-go filters.
- Running AF2 on the complex **with a target template and the Rosetta model as an initial guess** is what makes the complex prediction reliable enough to filter on — a methodological detail absent from the main summary.
- Fig S7 shows [[proteinmpnn]] is not just cheaper than Rosetta FastDesign but at least comparable in prospective success once DL filtering is applied.

## Connections

- Parent: [[bennett-2023-binder-design-dl]]; concept [[binder-design]].
- Empirically grounds the AF2-as-oracle argument formalized in [[watson-2023-rfdiffusion-supp]] (§5.1) and the confidence heads defined in [[jumper-2021-alphafold2-supp]].
