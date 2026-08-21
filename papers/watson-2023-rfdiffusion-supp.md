---
type: source-supp
parent: "[[watson-2023-rfdiffusion]]"
title: De novo design of protein structure and function with RFdiffusion — Supplementary Information
pdf: "../sources/ProteinDesign/WatsonBaker_Nature_2023_De novo design of protein structure and function with RFdiffusion_supp.pdf"
tags: [diffusion, methods, benchmarks, symmetry, motif-scaffolding, potentials]
ingested: 2026-07-13
---

# RFdiffusion — Supplementary Information (companion)

Methods/data companion to [[watson-2023-rfdiffusion]]. 129 pages. This page maps the SI and extracts the concrete details the main summary omits — architecture, diffusion math, training/conditioning recipes, and the *in silico* success criteria that define "success" throughout the paper.

## What the SI contains (map)

1. **RoseTTAFold architecture (§1)** — backbone-frame representation; MSA→MSA, MSA→Pair, Pair→Pair, Structure→Structure update blocks; structure refinement; recycling; losses; training.
2. **Diffusion model (§2)** — probabilistic-diffusion background; separate **forward/reverse transitions for residue translations and rotations** (rotations diffused on SO(3)); **self-conditioning** in reverse sampling; **MSE loss on residue frames**; geometric invariances.
3. **Design methods (§3)** — generating oligomers with **point-group symmetries**; **conditional training for functional-motif scaffolding**; fine-tuning & architecture modifications; **guiding inference with external potentials**; **tuning diversity by scaling noise at inference**.
4. **Task-specific setups (§4)** — base model; enzyme active-site scaffolding by fine-tuning on **minimal motifs**; PPI-design architecture (interface **hotspots**, secondary-structure & block-adjacency conditioning, PPI fine-tuning); potentials for symmetric oligomers and pocket design.
5. **Benchmarking & in silico metrics (§5)** — justification for **AlphaFold2 as the in silico oracle**; ProteinMPNN + AF2 settings; **in silico success-rate definitions**; unconditional, conditional, and diversity benchmarks; loss ablations; fold-conditioned and symmetric-oligomer design.

## Key extracted details

- **In silico "success" criteria** (recurring thresholds): AF2 self-consistency with **pAE < 5**, **pLDDT > 90** (motif cases often pLDDT > 80), and backbone/full-atom **RMSD to design or motif < ~1.0–1.5 Å**. These thresholds — not wet-lab data — define the success rates quoted in the main text. (See [[structure-prediction]] on prediction models used as design oracles.)
- **Sequencing + filtering settings:** designs are sequenced with [[proteinmpnn]] and evaluated with [[alphafold]]2 under fixed settings specified here — the concrete instantiation of the "generate → sequence → filter" loop.
- **Diversity control:** design diversity is tuned by **scaling the noise added at inference**; motif-scaffold diversity is compared by pairwise TM-score against RFjoint Inpainting and RF Hallucination (RFdiffusion yields more diverse scaffolds; inpainting's diversity comes only from scaffold-length sampling).
- **Symmetry:** oligomers generated under explicit **point-group symmetry** (C, D, and higher groups; examples up to large C-symmetries and >750-aa subunits); SI characterizes them experimentally by SEC with per-symmetry success rates.
- **Conditioning machinery:** motif scaffolding via conditional training on minimal motifs; PPI design adds interface hotspot, secondary-structure and block-adjacency conditioning; **external potentials** guide inference for symmetric assemblies and ligand/metal pocket design (e.g., square-planar Ni²⁺ site scaffolding).

## Connections

- Parent: [[watson-2023-rfdiffusion]].
- Grounds the metric definitions used across [[binder-design]] and [[diffusion-generative-design]].
- The AF2-as-oracle justification (§5.1) is the formal basis for the filtering discipline described in [[bennett-2023-binder-design-dl]].
