---
type: source
title: High thermodynamic stability of parametrically designed helical bundles
authors: Huang, Oberdorfer, Xu et al. (Baker lab)
venue: Science 2014
pdf: "../sources/Proteins/Huang_Baker_Science_2014_v346_p481_High_thermodynamic_stability_of_parametrically_designed_helical_bundles.pdf"
supp: yes
tags: [symmetry, oligomers, coiled-coils, parametric-design, rosetta, historical]
ingested: 2026-08-14
---

# Parametrically designed helical bundles

Designs protein backbones by **varying the parameters of the Crick coiled-coil equations** rather than by sampling fragments, yielding hyperstable bundles — including a symmetric pentamer — whose crystal structures match the design models with nearly identical core packing.

**Problem.** Coiled coils of two or more α helices supercoiled around a central axis are simple and regular enough to have driven peptide-design efforts for decades, but most of that work was **sequence-based** — choosing optimal amino acids at the core positions of the heptad repeat, in the tradition of [[harbury-1993-coiled-coil-oligomer-switch]]. The few structure-based efforts had used the parametric equations first derived by Francis Crick to design right-handed coiled coils or nanotube binders. What was missing was a way to generate *arbitrary* bundle geometries as backbones and then design sequences onto them.

**Approach.** Backbones are generated directly from the **Crick coiled-coil equations**. For a bundle of *n* helices the parameters are the supercoil twist ω0, the α-helical twist ω1, the supercoil radius R0, the per-helix phases φ1…φn, and the axial offsets z2…zn relative to the first helix. Successive Cα atoms rotate about the helical axis by approximately (ω0 + ω1), so supercoil and helical twist are coupled and the backbone is strained when their sum departs from the ~100° of an ideal helix. The parameters are sampled on a grid; **Rosetta** combinatorial sequence design finds low-energy sequences for each helix-supercoil arrangement; the lowest-energy arrangements are connected by loop building for monomeric targets; and Rosetta *ab initio* structure prediction is used as an in silico filter before synthesis. For symmetric oligomers, the helices are arrayed symmetrically about the *z* axis, so for an *n*-helix bundle φ0 takes the values {0, 2π/n, 4π/n, … 2(n−1)π/n} — symmetry enters as a **constraint on the parameter set** rather than as a search objective (see [[huang-2014-parametric-helical-bundles-supp]]).

**Key results.**

- Three designs reported: an antiparallel monomeric untwisted **three-helix bundle** with 80-residue helices, an antiparallel monomeric right-handed **four-helix bundle**, and a **pentameric parallel left-handed five-helix bundle** — the last a C5 symmetric homo-oligomer.
- The designs are **extremely stable**, with extrapolated ΔG_fold **> 60 kcal/mol**.
- Crystal structures are close to the design models with **nearly identical core packing** between helices (PDB 4TQL, 4UOS, 4UOT).
- Demonstrates custom design of hyperstable proteins with **fine-tuned geometries** — the backbone is a continuous function of a handful of numbers.

**Significance.** Parametric generation is the answer the field gave, pre-deep-learning, to the question *where do symmetric backbones come from?* Its strength is exactness and stability; its limitation is that it only covers folds the parameterization can express, which in practice means helical bundles. [[wicky-2022-symmetric-assembly-design]] explicitly notes that parametrically designed helical bundles were the **exception** to the otherwise universal requirement that the protomer structure be specified in advance — making this paper the key baseline against which the hallucination and diffusion approaches are measured in [[symmetric-oligomer-design]].

**Connections.**

- Published back-to-back with [[thomson-2014-alpha-helical-barrels]], which applies a related parametric logic to higher-order barrels.
- The parametric backbone machinery is reused for the axle components of [[courbet-2022-axle-rotor-assemblies]].
- Provides the coiled-coil scaffolds that [[boyken-2016-hydrogen-bond-network-oligomers]] decorates with hydrogen-bond networks.
- **Supplement:** [[huang-2014-parametric-helical-bundles-supp]] — the explicit Crick equations, the sampling protocol, and the design/characterization methods.
- Concept: [[symmetric-assembly-design]]; chapter: [[symmetric-oligomer-design]].
