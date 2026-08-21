---
type: concept
tags: [structure-prediction, deep-learning]
sources: 4
updated: 2026-07-10
---

# Structure prediction

Predicting 3D structure from sequence — historically the "protein folding problem." Now largely solved for single chains and increasingly for complexes, and the enabling substrate for modern design.

**State of the art.** [[jumper-2021-alphafold2]] reached atomic accuracy at CASP14 using MSA + pair reasoning (Evoformer) and an explicit structure module. [[abramson-2024-alphafold3]] extends this to protein–ligand, protein–nucleic-acid and antibody–antigen complexes with a diffusion coordinate head. [[rosettafold]] (Baker lab) is the parallel lineage whose network is repurposed for generation in [[watson-2023-rfdiffusion]]; its all-atom extension [[krishna-2024-rosettafold-all-atom]] brings small molecules, nucleic acids and metals into a single model — the design-side counterpart to AlphaFold3.

**Why it matters for design.** Prediction models double as **design oracles**: their confidence scores (pLDDT, PAE, pTM) filter designs *in silico* before synthesis — see [[bennett-2023-binder-design-dl]] and the RFdiffusion→MPNN→AF2 loop. Prediction and design are converging on shared diffusion machinery.

**Key models:** [[alphafold]] · RoseTTAFold.

**Sources:** [[jumper-2021-alphafold2]], [[abramson-2024-alphafold3]], [[krishna-2024-rosettafold-all-atom]], [[bennett-2023-binder-design-dl]].
