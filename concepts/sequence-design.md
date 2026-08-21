---
type: concept
tags: [sequence-design, deep-learning]
sources: 4
updated: 2026-07-13
---

# Sequence design (fixed-backbone)

Given a target backbone, find an amino-acid sequence that folds to it — the "inverse folding" problem, and the second stage of the dominant de novo recipe.

**Shift from physics to learning.** Classic approach: Rosetta energy optimization over rotamers — accurate but slow, with limited success on hard targets. [[dauparas-2022-proteinmpnn]] replaced it with an autoregressive message-passing network conditioned on backbone geometry, raising native sequence recovery to ~52% (vs. ~33% for Rosetta) in seconds, and generalizing to interfaces, oligomers and nanoparticles. Independently, [[anand-2022-learned-potential-seqdesign]] (Huang lab) reached the same conclusion from the "learned energy" direction — a network learning the design potential directly from crystal structures with no human priors, generalizing to unseen topologies (incl. a de novo TIM-barrel) with crystal-validated designs.

**Toward codesign.** The next step folds sequence into structure generation: [[chu-2024-protpardelle]] codesigns all-atom structure and sequence (miniMPNN in the loop), blurring the line between this concept and [[diffusion-generative-design]].

**Role in pipelines.** Sequence design is the step *after* backbone generation: [[watson-2023-rfdiffusion]] (or [[ingraham-2023-chroma]]) produces a backbone, then ProteinMPNN assigns sequence, then a predictor filters. [[bennett-2023-binder-design-dl]] swapped Rosetta for ProteinMPNN specifically for this efficiency.

**Key model:** [[proteinmpnn]].

**Sources:** [[dauparas-2022-proteinmpnn]], [[anand-2022-learned-potential-seqdesign]], [[bennett-2023-binder-design-dl]], [[chu-2024-protpardelle]].
