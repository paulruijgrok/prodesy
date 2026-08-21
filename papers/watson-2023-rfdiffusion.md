---
type: source
title: De novo design of protein structure and function with RFdiffusion
authors: Watson, Juergens, Bennett et al. (Baker lab)
venue: Nature 2023
pdf: "../sources/ProteinDesign/WatsonBaker_Nature_2023_De novo design of protein structure and function with RFdiffusion.pdf"
supp: yes
tags: [diffusion, backbone-generation, binder-design, de-novo, foundational]
ingested: 2026-07-10
---

# RFdiffusion — De novo design of protein structure and function

The first broadly successful diffusion generative model for protein backbones, and the general-purpose engine behind much current de novo design.

**Problem.** Deep-learning design had advanced but lacked a single general framework spanning unconditional monomer generation, binder design, symmetric assemblies, and functional-site (motif) scaffolding. Diffusion models had struggled on proteins due to backbone-geometry and sequence–structure complexity.

**Approach.** [[rfdiffusion]] fine-tunes the **RoseTTAFold** structure-prediction network on a denoising task: starting from noised residue frames, the network iteratively denoises to a coherent backbone. Conditioning inputs steer generation — target hotspots for binders, symmetry operators for oligomers, fixed motif atoms for active-site scaffolding. Generated backbones are sequenced with [[proteinmpnn]] and filtered by AlphaFold2 self-consistency.

**Key results.**

- State-of-the-art on **unconditional** and topology-constrained monomer design, **symmetric oligomers**, **metal-binding** and **enzyme active-site scaffolding**, and de novo **binder design**.
- Hundreds of designs experimentally characterized; a cryo-EM structure of a designed assembly closely matches the design model, confirming atomic-level accuracy.
- Uses the "fold, then check" paradigm: [[jumper-2021-alphafold2]]-based in silico validation predicts success before any wet-lab work.

**Significance.** Establishes the modern pipeline: **RFdiffusion backbone → ProteinMPNN sequence → AlphaFold2 filter**. Made [[diffusion-generative-design]] the dominant approach and generalized [[binder-design]] beyond native motif grafting.

**Supplement:** [[watson-2023-rfdiffusion-supp]] — architecture, diffusion math (SO(3) rotations, self-conditioning), symmetry/motif/PPI conditioning recipes, external potentials, and the AF2-based *in silico* success criteria (pAE < 5, pLDDT > 90, RMSD < ~1 Å).

**Connections.**

- Built by fine-tuning [[rosettafold]] (structure-prediction sibling of [[jumper-2021-alphafold2]]).
- Pairs with [[dauparas-2022-proteinmpnn]] for sequencing.
- Same diffusion paradigm as [[ingraham-2023-chroma]] (independent, contemporaneous) and later [[abramson-2024-alphafold3]].
- Motivating engine for improved [[bennett-2023-binder-design-dl]].
- Core reference for [[diffusion-generative-design]] and [[binder-design]].
