---
type: source
title: Computational design of water-soluble α-helical barrels
authors: Thomson, Wood, Burton et al. (Woolfson lab)
venue: Science 2014
pdf: "../sources/Proteins/Thomson_Woolfson_Science_v246_p48_Computational_design_of_water_soluble_alpha_helical_barrels.pdf"
supp: missing-requested
tags: [symmetry, oligomers, coiled-coils, parametric-design, channels, historical]
ingested: 2026-08-14
---

# Computational design of water-soluble α-helical barrels

Designs **cyclic homo-oligomers of five, six and seven parallel identical helices** with open central channels, by combining coiled-coil geometry, knowledge-based scoring and atomistic modeling — the Woolfson-lab counterpart to the Baker-lab parametric work published in the same issue.

**Problem.** Defining sequences that fold to a specified structure — the inverse folding problem — has mostly been applied to *mimic existing folds*. Coiled coils are a promising exception because their backbone conformations are unusually well described geometrically, and proteins with **cyclic symmetry** permit systematic variation of repeating elements to produce whole families. Classical coiled coils comprise bundles of two to four helices and account for **more than 98% of known coiled-coil structures**, with well-understood sequence-to-structure rules. **α-Helical barrels** — assemblies with more than four helices and accessible central channels — are the sparsely populated remainder: many of the possible structures remain unobserved, and the few known examples include natural parallel pentamers and hexamers.

**Approach.** The design logic works from the **interface type** implied by the heptad repeat. Classical coiled coils have repeats `(hxxhxxx)n`, labelled *abcdefg*, placing hydrophobic residues at **a** and **d**; the resulting hydrophobic seam mediates helix association, buttressed by polar interactions at **e** and **g** (a *type-N* interface), and the "gade" residues determine oligomer state and partner selection. In an α-helical barrel, by contrast, **each helix interacts with two neighbours through two independent hydrophobic seams**. The authors enumerate the ways to achieve this within a heptad repeat (seams sharing one residue give type-I interfaces, and so on), score candidate sequences with a knowledge-based fitness function, and build atomistic models of the surviving designs.

**Key results.**

- Delivered **discrete, water-soluble assemblies with five to seven parallel and identical helices** — cyclic C5, C6 and C7 homo-oligomers.
- **High-resolution X-ray crystal structures** match the in silico models: CC-Pent (PDB 4pn8), CC-Hex2 (4pn9), CC-Hex3 (4pnb), CC-Hept (4pna). Oligomeric states were assigned independently by analytical-ultracentrifugation sedimentation equilibrium.
- **CC-Pent is the first crystal structure of a designed pentameric α-helical barrel**, and **CC-Hept the first heptamer** of this class.
- The **channels are chemically defined and their diameters track the oligomer state** — pore diameters measured with PoreWalker — which the authors present as a route to designing function into the lumen.

**Significance.** Together with [[huang-2014-parametric-helical-bundles]] this establishes the **parametric/geometric era** of [[symmetric-oligomer-design]]: symmetric oligomers of specified valency, built to atomic accuracy, from an explicit geometric description. It also introduces the theme that a cyclic ring's **central pore is itself a designable feature** — the property that later makes rings attractive as channels, pores and catalytic scaffolds. The corresponding limitation is equally clear: the method is confined to what the coiled-coil parameterization can express.

**Connections.**

- Companion to [[huang-2014-parametric-helical-bundles]] (same *Science* issue, same underlying Crick-equation description of coiled-coil backbones).
- Builds directly on the sequence→oligomer-state relations established by [[harbury-1993-coiled-coil-oligomer-switch]].
- The "rings have designable lumens" idea recurs in the giant β-sheet-lumen rings of [[wicky-2022-symmetric-assembly-design]] and the expanded TIM-barrel-like oligomers of [[watson-2023-rfdiffusion]].
- Concept: [[symmetric-assembly-design]]; chapter: [[symmetric-oligomer-design]].
- **Supplement:** not present in `sources/` — the *Science* supplementary materials (Materials and Methods, Figs. S1–S12, Tables S1–S2) would supply the scoring function and sampling details, which this page currently states only qualitatively.
