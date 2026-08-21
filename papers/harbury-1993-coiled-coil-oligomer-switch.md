---
type: source
title: A Switch Between Two-, Three-, and Four-Stranded Coiled Coils in GCN4 Leucine Zipper Mutants
authors: Harbury, Zhang, Kim, Alber
venue: Science 1993
pdf: "../sources/Proteins/HarburyAlber_Science_1993_A Switch Between Two-, Three-, and Four-stranded Coiled Coils in GCN4 Leucine Zipper Mutants.pdf"
supp: no
tags: [symmetry, oligomers, coiled-coils, biophysics, historical]
ingested: 2026-08-14
---

# A switch between two-, three-, and four-stranded coiled coils

The experiment that showed **oligomeric state is encodable in sequence** — that the number of chains in a symmetric assembly can be dialled by changing which hydrophobic residues sit at the core positions of a heptad repeat.

**Problem.** A then-influential simplifying hypothesis held that a protein's three-dimensional structure is determined largely by the *pattern* of hydrophobic (H) and polar (P) residues and is largely independent of the geometric properties of the side chains making up that pattern. Coiled coils are a direct counterexample: they share the characteristic seven-residue repeat `(a b c d e f g)n` with hydrophobic residues at **a** and **d**, yet coiled-coil sequences are observed as dimers, trimers and antiparallel tetramers. If the HP pattern alone determined structure, that variation would be unexplained.

**Approach.** The authors systematically mutagenized the hydrophobic core of the dimeric GCN4-p1 leucine-zipper peptide, changing the **a** and **d** positions in a concerted fashion rather than one at a time, and then characterized the resulting oligomeric states and structures. Because supercoiled α helices have approximately 3.5 residues per turn, the three-and-four spacing of **a** and **d** places the hydrophobic residues on one face of the helix; in the GCN4-p1 dimer, the five **a** residues and four **d** leucines of each monomer form the apolar interface.

**Key results.**

- Concerted substitution at the core **a** and **d** positions produced peptides forming **two-, three- and four-stranded** structures — the oligomerization state switches with core residue identity, not with the HP pattern.
- Establishes that the **geometry of buried apolar side chains**, not just their hydrophobicity, selects among symmetric oligomeric states.
- Provides the sequence→oligomer-state rule that later parametric design work builds on.

**Significance.** This is the origin point for the wiki's [[symmetric-oligomer-design]] chapter: the first clean demonstration that a designer could, in principle, *specify* the valency of a symmetric homo-oligomer through sequence. Later parametric approaches ([[huang-2014-parametric-helical-bundles]], [[thomson-2014-alpha-helical-barrels]]) turn this observation into a systematic design procedure by making the backbone itself a function of a small number of geometric parameters, and [[boyken-2016-hydrogen-bond-network-oligomers]] adds a second, orthogonal specificity channel on top of the apolar core.

**Connections.**

- Foundational for [[symmetric-assembly-design]] and the parametric era of [[symmetric-oligomer-design]].
- Cited as prior art by [[thomson-2014-alpha-helical-barrels]] in motivating α-helical barrels with more than four helices.
- Contrasts with the deep-learning route of [[wicky-2022-symmetric-assembly-design]], where oligomeric state is specified as an input to a generative objective rather than encoded by hand.
