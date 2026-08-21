---
type: concept
tags: [binder-design, de-novo, therapeutics]
sources: 5
updated: 2026-07-13
---

# Binder design

De novo design of proteins that bind a chosen target with high affinity and specificity, from the target structure alone — a route to therapeutics, diagnostics and imaging reagents that bypasses immunization and library screening.

**Progression captured so far.**

1. **DL-augmented Rosetta** — [[bennett-2023-binder-design-dl]]: keep the Rosetta/motif pipeline but swap in [[proteinmpnn]] for sequence design and use [[jumper-2021-alphafold2]] self-consistency as an *in silico* filter → ~10× higher success rate.
2. **Generative (protein targets)** — [[watson-2023-rfdiffusion]]: diffuse binder backbones directly against target hotspots, then sequence + filter with the same tools.
3. **Ligand-conditioned** — [[krishna-2024-rosettafold-all-atom]] (RFdiffusionAA): diffuse a binder backbone *around* a small molecule; experimentally validated for digoxigenin, heme and bilin. Extends de novo binding beyond protein targets to small-molecule ligands.
4. **Flexible/peptide targets** — [[vasquez-torres-2023-helical-peptide-binders]]: binders to floppy α-helical peptide hormones (PTH, glucagon, GLP1, secretin, NPY, BH3) via RFdiffusion + **partial diffusion**, then converted into biosensors. Pushes binder design to conformationally heterogeneous targets.
5. **Nucleic-acid & efficient all-atom** — [[butcher-2025-rfdiffusion3]]: one all-atom model designs protein–protein, protein–DNA and protein–small-molecule interfaces at ~10× less compute.

**The discipline.** Both rely on "predict-then-order": score fold probability and binding-pose probability before any synthesis, converting a low hit-rate wet-lab search into a filtered shortlist.

**Sources:** [[bennett-2023-binder-design-dl]], [[watson-2023-rfdiffusion]], [[krishna-2024-rosettafold-all-atom]], [[vasquez-torres-2023-helical-peptide-binders]], [[butcher-2025-rfdiffusion3]].
