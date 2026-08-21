---
type: source
title: Protein sequence design with a learned potential
authors: Anand, Eguchi, Mathews, Perez, Derry, Altman, Huang (Huang lab, Stanford)
venue: Nature Communications 2022
pdf: "../sources/ProteinDesign/AnandHuang_NatCommun_2022_Protein sequence design with a learned potential.pdf"
supp: missing-requested
tags: [sequence-design, deep-learning, learned-energy, sidechains, huang-lab]
ingested: 2026-07-13
---

# Protein sequence design with a learned potential

A Huang-lab deep-learning model for fixed-backbone [[sequence-design]] that learns entirely from crystal-structure data with **no human-specified energy terms** — an early demonstration that learned potentials can replace hand-crafted ones.

**Problem.** Classical fixed-backbone design specifies an energy function and searches sequence space for a minimum-energy solution; enormous effort has gone into modeling and parameterizing those energy functions. Can a network learn the potential directly from structures instead?

**Approach.** A deep neural network designs sequence onto a backbone, learned directly from crystal structures without human priors. It models residue identities together with **side-chain conformations** (autoregressive/iterative refinement), effectively acting as a learned energy over sequence-structure compatibility.

**Key results.**

- Generalizes to **native topologies not seen in training**, producing experimentally **stable** designs.
- Tested on a challenging **de novo TIM-barrel** scaffold: produces novel sequences, and high-resolution **crystal structures of two designs** agree closely with the in silico models.
- Establishes that an entirely learned sequence-design method is tractable and physically reasonable.

**Significance.** A contemporary of [[dauparas-2022-proteinmpnn]] from a different lab (Huang), reaching the same conclusion from the "learned energy" direction — evidence that learned potentials, not hand-tuned Rosetta energies, are the future of [[sequence-design]]. Its explicit side-chain modeling foreshadows all-atom generation in [[chu-2024-protpardelle]].

**Connections.**

- Learned-potential counterpart to [[dauparas-2022-proteinmpnn]]; concept [[sequence-design]].
- Side-chain focus links to the all-atom codesign in [[chu-2024-protpardelle]] (same lab).
