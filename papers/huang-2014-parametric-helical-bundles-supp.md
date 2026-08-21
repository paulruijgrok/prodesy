---
type: source-supp
parent: "[[huang-2014-parametric-helical-bundles]]"
title: High thermodynamic stability of parametrically designed helical bundles — Supplementary Materials
pdf: "../sources/Proteins/Huang_Baker_Science_2014_v346_p481_High_thermodynamic_stability_of_parametric_designed_helical_bundles_supp.pdf"
tags: [symmetry, coiled-coils, parametric-design, methods, crick-equations]
ingested: 2026-08-14
---

# Parametric helical bundles — Supplementary Materials (companion)

Methods companion to [[huang-2014-parametric-helical-bundles]]. This page maps the supplement and extracts the parameterization itself, which the main text states only in summary.

## What the supplement contains (map)

1. **Computational modeling** — the Crick coiled-coil equations; the computational design protocol.
2. **Experimental materials and methods** — reagents; cloning and expression; peptide synthesis; cell lysis and purification; circular dichroism; native molecular-weight determination; differential scanning calorimetry; crystallography; negative-stain electron microscopy.
3. **Figures S1–S12, Tables S1–S2.**
4. **Input files and command lines** for the computations — i.e. the design protocol is released in runnable form.

## Key extracted details

- **The Crick equations as used.** For a helix in a coiled coil with supercoil axis along *z*, the Cα coordinates of residue *t* are given in closed form in terms of R0 and ω0 (superhelical radius and twist), φ0 (superhelical phase) and the decoupled phase φ0′ = φ0 + Δz·tan(α)/R0, together with R1, ω1, φ1 and Δz (helical radius, twist, phase and axial offset) and the pitch angle α = arcsin(R0ω0/d), where *d* is the rise per residue along the helical axis.
- **Fixed versus sampled parameters.** In all calculations *d* and R1 were held **fixed at ideal α-helix values (2.26 and 1.51)**; the remaining parameters were sampled. This is what makes the search low-dimensional.
- **How symmetry is imposed.** Helices are arrayed symmetrically around the *z* axis, so for an *n*-helix bundle the superhelical phase φ0 takes the values {0, 2π/n, 4π/n, … 2(n−1)π/n}. **Cyclic symmetry is therefore exact by construction** — it is a property of the coordinate generator, not something optimized for or checked afterwards. This is the sharpest available contrast with the objective-based symmetry of [[wicky-2022-symmetric-assembly-design]] and the operator-based resymmetrization of [[watson-2023-rfdiffusion]] (see [[watson-2023-rfdiffusion-supp]] §3.1).
- **Search strategy.** Grid sampling of the Crick parameters, Rosetta sequence design at each grid point, then finer grid searches in the neighbourhood of the lowest-energy parameter sets.

## Connections

- Parent: [[huang-2014-parametric-helical-bundles]].
- The same parametric generator, extended to sample two superhelical radii per helix, produces the interdigitated dihedral axles of [[courbet-2022-axle-rotor-assemblies]] (see [[courbet-2022-axle-rotor-assemblies-supp]]).
- Chapter: [[symmetric-oligomer-design]].
