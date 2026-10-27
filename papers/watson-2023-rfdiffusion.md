---
type: source
title: De novo design of protein structure and function with RFdiffusion
authors: Watson, Juergens, Bennett et al. (Baker lab)
venue: Nature 2023
pdf: "../sources/ProteinDesign/WatsonBaker_Nature_2023_De novo design of protein structure and function with RFdiffusion.pdf"
supp: yes
tags: [diffusion, backbone-generation, binder-design, de-novo, foundational]
ingested: 2026-07-10
updated: 2026-10-12
---

# RFdiffusion — De novo design of protein structure and function

The first broadly successful diffusion generative model for protein backbones, and the general-purpose engine behind much current de novo design.

**Problem.** Deep-learning design had advanced but lacked a single general framework spanning unconditional monomer generation, binder design, symmetric assemblies, and functional-site (motif) scaffolding. Diffusion models had struggled on proteins due to backbone-geometry and sequence–structure complexity.

**Approach.** [[rfdiffusion]] fine-tunes the **RoseTTAFold** structure-prediction network on a denoising task: starting from noised residue frames, the network iteratively denoises to a coherent backbone. Conditioning inputs steer generation — target hotspots for binders, symmetry operators for oligomers, fixed motif atoms for active-site scaffolding. Generated backbones are sequenced with [[proteinmpnn]] and filtered by AlphaFold2 self-consistency.

**Key results.**

- State-of-the-art on **unconditional** and topology-constrained monomer design, **symmetric oligomers**, **metal-binding** and **enzyme active-site scaffolding**, and de novo **binder design**.
- Hundreds of designs experimentally characterized; a cryo-EM structure of a designed assembly closely matches the design model, confirming atomic-level accuracy.
- Uses the "fold, then check" paradigm: [[jumper-2021-alphafold2]]-based in silico validation predicts success before any wet-lab work.

## The binder-design campaign (extracted 2026-10-12)

The paper's binder results were previously summarized here without figures; this section supplies them, because the [[de-novo-binder-design]] chapter rests on them.

**How binders are specified.** Binder diffusion is conditioned on **"interface hotspots"** — the residues on the target chain the binder should contact. A separately fine-tuned model adds coarse-grained control over **binder scaffold topology**, so a particular fold can be requested alongside the hotspots. Binder design required its own **PPI fine-tune** of the base model; it was not a free capability of unconditional RFdiffusion.

**Five targets, chosen to match the prior Rosetta method's benchmark:** Influenza A H1 haemagglutinin (HA), Interleukin-7 receptor-α (IL-7Rα), Programmed death-ligand 1 (PD-L1), insulin receptor (InsR) and tropomyosin receptor kinase A (TrkA). Designs were produced both with and without fold conditioning, filtered by AF2 confidence in the interface and in the monomer, and **95 designs were selected per target** for experimental characterization.

**Results.** Binding was assessed by single-point biolayer interferometry at 10 µM binder.

- **Overall experimental success rate 19%**, defined as binding at or above 50% of the maximal response of the positive control — described by the authors as a conservative estimate, since some designs that bound had insufficient material to screen at 10 µM.
- That is **roughly two orders of magnitude above the previous Rosetta-based method on the same targets**.
- Binders were identified for **all five targets**, with **fewer than 100 designs tested per target against thousands in previous studies** — the throughput claim that matters more than the rate itself.
- Full BLI titrations on a subset gave **nanomolar affinities with no experimental optimization**, including HA and IL-7Rα binders at **roughly 30 nM**.

**Motif-scaffolded binders are the stronger result.** Scaffolding the p53 helix that binds MDM2, with an RFdiffusion model fine-tuned on complexes, produced designs making **on average 31% more interface surface area** than the native helix. **55 of 95 designs bound MDM2** at above 50% of maximum response, 32 of those monomeric, and BLI gave **0.7 nM (p53_design_89) and 0.5 nM (p53_design_53) against a native affinity of 600 nM** — three orders of magnitude tighter than the natural interaction.

**Multivalency.** C3-symmetric oligomer scaffolding was used to display the AHB2 SARS-CoV-2 binder rigidly, on the argument that flexible linkage pays an entropic cost that a rigid symmetric fusion avoids.

**Significance.** Establishes the modern pipeline: **RFdiffusion backbone → ProteinMPNN sequence → AlphaFold2 filter**. Made [[diffusion-generative-design]] the dominant approach and generalized [[binder-design]] beyond native motif grafting. The 19% figure is in **BLI single-point units at 10 µM**, which is not the same denominator as the yeast-display SC50 < 4 µM bar used by [[bennett-2023-binder-design-dl]] or the AF2 self-consistency rates used by [[didi-2026-complexa-scaling]] — see the comparability argument in [[ruijgrok-2026-binder-pipeline-comparison]].

**Supplement:** [[watson-2023-rfdiffusion-supp]] — architecture, diffusion math (SO(3) rotations, self-conditioning), symmetry/motif/PPI conditioning recipes, external potentials, and the AF2-based *in silico* success criteria (pAE < 5, pLDDT > 90, RMSD < ~1 Å).

**Connections.**

- Built by fine-tuning [[rosettafold]] (structure-prediction sibling of [[jumper-2021-alphafold2]]).
- Pairs with [[dauparas-2022-proteinmpnn]] for sequencing.
- Same diffusion paradigm as [[ingraham-2023-chroma]] (independent, contemporaneous) and later [[abramson-2024-alphafold3]].
- Motivating engine for improved [[bennett-2023-binder-design-dl]].
- Core reference for [[diffusion-generative-design]] and [[binder-design]].
- Its hotspot conditioning is given a biophysical foundation by [[halperin-2004-interface-hot-spots]]; the methodological alternative is [[gainza-2023-surface-fingerprint-binders]].
- Its PD-L1 and IL-7Rα rows overlap [[stark-2025-boltzgen]] and [[gainza-2023-surface-fingerprint-binders]] — one of the chapter's few cross-method comparisons.
- Used as a baseline by [[didi-2026-complexa-scaling]] and [[cho-2025-protein-hunter]].
- `updated: 2026-10-12` — binder campaign numbers extracted; see the revise entry in [[log]].
