---
type: source-supp
parent: "[[courbet-2022-axle-rotor-assemblies]]"
title: Computational design of mechanically coupled axle-rotor protein assemblies — Supplementary Materials
pdf: "../sources/ProteinDesign/CourbetBaker_Science_2022_Computational design of mechanically coupled axle-rotor protein assemblies_supp.pdf"
tags: [symmetry, dihedral, parametric-design, rosetta, methods]
ingested: 2026-08-14
---

# Axle-rotor assemblies — Supplementary Materials (companion)

Methods companion to [[courbet-2022-axle-rotor-assemblies]]. Figs. S1–S22, Tables S1–S3, Movies S1–S5, Data S1–S5. This page extracts the design protocol for symmetric components, which is the part most reusable outside the paper's specific machines.

## Key extracted details

- **Three routes to symmetric axle parts.** *Approach 1* designs short (30–50 residue) single α-helical monomers that self-assemble into **high-aspect-ratio dihedral homo-oligomers**, then rigidly fuses those to cyclic wheel-shaped homo-oligomers to make a complete axle.
- **Parametric sampling ranges.** Backbones are generated with the **Crick generating equations** using ideal values for supercoil twist ω0 and helical twist ω1 — the same parameterization documented in [[huang-2014-parametric-helical-bundles-supp]]. For D3 helical bundles, the **interdigitated** geometry needed to pack a hole-free core is obtained by sampling **two different starting superhelical radii per helix (6 Å and 12 Å)**, joined by a variable number of linker residues, over a ~5 Å range in 0.5 Å bins. Helical phase Δφ1 is sampled 0°–90° in 10° steps; the *z*-offset from −1.51 Å to +1.51 Å in 0.1 Å steps; supercoil phases Δφ0 are fixed at **0° for D3** and **30° for D2**.
- **Interface specificity via HBNet.** After parametric backbone generation, Rosetta design optimizes side-chain identities and rotamers, importantly using the **HBNet protocol** of [[boyken-2016-hydrogen-bond-network-oligomers]] to build extended hydrogen-bond networks *across* subunits — the mechanism that enforces both specificity of interaction and a symmetric binding mode.
- **Fusion machinery.** Dihedral building blocks are rigidly fused to previously designed cyclic homo-oligomers with short structured helical linkers built by **RosettaRemodel**, sampling the rotation and separation between *z*-aligned cyclic and dihedral components, followed by a second round of Rosetta design across the fusion. **Rosetta SymDofMover** is used for the D8 axle.

## Why this matters for the chapter

The supplement makes explicit how much bespoke geometric engineering the pre-diffusion route required to reach a D8 or D3–C5 assembly: hand-chosen radius pairs, hand-tuned phase grids, per-symmetry linker design. [[symmetric-oligomer-design]] uses this as the concrete measure of what [[watson-2023-rfdiffusion]] replaced when it reduced symmetric generation to applying point-group operators to noise and resymmetrizing during denoising (see [[watson-2023-rfdiffusion-supp]] §3.1).

## Connections

- Parent: [[courbet-2022-axle-rotor-assemblies]].
- Shares its parametric core with [[huang-2014-parametric-helical-bundles-supp]] and its interface protocol with [[boyken-2016-hydrogen-bond-network-oligomers]].
