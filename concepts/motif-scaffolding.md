---
type: concept
tags: [motif-scaffolding, functional-site, de-novo]
sources: 3
updated: 2026-07-13
---

# Motif scaffolding (functional-site design)

Building a full protein *around* a fixed functional site — an enzyme active site, a metal/ligand pocket, a binding or epitope motif — so the site is held in its active geometry. The second half of functional de novo design (the first half being: obtain the motif geometry).

**Two generations of method.**

1. **Hallucination & inpainting** — [[wang-2022-functional-site-scaffolding]] introduced both: *constrained hallucination* (optimize a sequence until the network folds it to contain the motif) and *inpainting/RFjoint* (one forward pass fills sequence+structure around the motif). Flexible vs. fast. The unconstrained hallucination engine both build on comes from [[anishchenko-2021-hallucination]], which anticipated this application — noting that because the network hallucinates plausible structures from scratch, no scaffold blueprint need be specified in advance, and the loss can be generalized to include binding motifs or catalytic sites.
2. **Conditional diffusion** — [[watson-2023-rfdiffusion]] generalizes these: conditional training scaffolds motifs by denoising (see [[watson-2023-rfdiffusion-supp]] §3.2), with higher success and diversity. [[butcher-2025-rfdiffusion3]] extends to **atomic** motifs (tip-atom conditioning; the AME enzyme benchmark), and [[chu-2024-protpardelle]] scaffolds motifs **backbone- and rotamer-free** in all-atom space.

**Common pattern.** Motif in → scaffold out → sequence with [[proteinmpnn]] → filter with [[alphafold]]2/self-consistency.

**Sources:** [[wang-2022-functional-site-scaffolding]], [[watson-2023-rfdiffusion]], [[butcher-2025-rfdiffusion3]] (and all-atom variant [[chu-2024-protpardelle]]).
