---
type: source
title: De novo design of protein homo-oligomers with modular hydrogen-bond network–mediated specificity
authors: Boyken, Chen, Groves et al. (Baker lab)
venue: Science 2016
pdf: "../sources/Proteins/De novo design of protein homo-oligomers with modular hydrogen-bond network–mediated specificity.pdf"
supp: missing-requested
tags: [symmetry, oligomers, coiled-coils, hydrogen-bonds, specificity, rosetta, historical]
ingested: 2026-08-14
---

# Homo-oligomers with hydrogen-bond-network-mediated specificity

Introduces **HBNet** and uses it to design cyclic homo-oligomers whose **interaction specificity** is set by modular arrays of buried hydrogen-bond networks — the protein analogue of Watson–Crick base pairing — rather than by hydrophobic packing alone.

**Problem.** In DNA, specificity comes from modular hydrogen bonds in the core of the double helix; in proteins it comes largely from **buried hydrophobic packing** complemented by irregular peripheral polar interactions. Two things make polar interfaces hard to design: the partially covalent hydrogen bond restricts donors and acceptors to narrow ranges of orientation and distance, and nearly all buried polar atoms must find a hydrogen-bonding partner or incur a considerable desolvation penalty. Consequently, designed symmetric oligomers of the parametric era ([[huang-2014-parametric-helical-bundles]], [[thomson-2014-alpha-helical-barrels]]) achieve the right *structure* but offer no modular handle on *which* protomer pairs with which — a problem once you want several orthogonal assemblies in the same cell.

**Approach.** **HBNet** enumerates all side-chain hydrogen-bond networks available in an input backbone. Conventional design algorithms are poorly suited to this because they express system energy as a sum of *pairwise* residue interactions, whereas a network is an inherently many-body object; HBNet instead precomputes hydrogen bonds and traverses the resulting graph to find all networks of **three or more residues** connected by low-energy hydrogen bonds, **rejecting any network with buried donors or acceptors left unsatisfied**. The networks are hosted in coiled-coil oligomers, chosen because they are abundant, well studied, **generatable parametrically**, and have repeating geometric cross sections — so a network can be reused at equivalent positions around the ring.

**Key results.**

- Designed **dimers, trimers and tetramers** built as **two concentric rings of helices**, including **triangular, square and supercoiled topologies not previously seen**.
- **Ten crystal structures** determined, spanning the design range. The structures — and the hydrogen-bond networks in particular — are nearly identical to the design models; left-handed trimers match at **sub-ångström RMSD**, and dimer network RMSDs as low as **0.39 Å** (0.92 Å across all network atoms; 1.16 Å over all Cα) are reported. Where deviations occur, they are traced to **water displacing designed network side chains**.
- The designed networks **confer interaction specificity in vivo**, i.e. they act as an addressable code, not merely a structural decoration.
- Demonstrates, in the authors' framing, that **fundamentally new modes of interaction remain to be discovered in proteins** despite the diversity already present in nature.

**Significance.** This is where symmetric-oligomer design acquires a second, orthogonal design axis: valency and geometry from the parametric backbone, **specificity from the polar core**. For [[symmetric-oligomer-design]] it marks the transition from "can we build a ring" to "can we build a *set* of rings that do not cross-talk" — the prerequisite for multi-component assemblies and for the symmetry-mismatched machines of [[courbet-2022-axle-rotor-assemblies]], whose interfaces are designed with the HBNet protocol introduced here.

**Connections.**

- Hosts its networks in the parametric coiled coils of [[huang-2014-parametric-helical-bundles]].
- HBNet is used directly in the axle design of [[courbet-2022-axle-rotor-assemblies]] (see [[courbet-2022-axle-rotor-assemblies-supp]]).
- Represents the Rosetta-era peak that the learned methods of [[wicky-2022-symmetric-assembly-design]] and [[watson-2023-rfdiffusion]] are measured against in [[symmetric-oligomer-design]].
- Concept: [[symmetric-assembly-design]]; relates to [[sequence-design]] (the pairwise-energy limitation HBNet works around).
- **Supplement:** not present in `sources/` — the *Science* supplementary materials contain the HBNet method description and the design scripts, which this page summarizes only from the main text.
