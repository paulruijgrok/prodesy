---
type: source
title: Computational enzyme design by catalytic motif scaffolding
authors: Braun, Tripp, Chakatok, Kaltenbrunner, Fischer et al.; Hall & Oberdorfer (TU Graz / Univ. Graz)
venue: Nature 2026 (649, 237–245; online 3 December 2025; doi 10.1038/s41586-025-09747-9)
pdf: "../sources/ProteinDesign/BraunOberdorfer_Nature_2026_Computational enzyme design by catalytic motif scaffolding.pdf"
supp: yes
tags: [enzyme-design, retroaldolase, morita-baylis-hillman, stereoselectivity, binding-pocket, crystallography, independent-lineage, oberdorfer-lab]
ingested: 2026-10-21
---

# Riff-Diff — computational enzyme design by catalytic motif scaffolding

The **independent lineage** the enzyme chapter lacked: a non-Baker-lab enzyme-design method, from the Oberdorfer lab, published back-to-back with [[kim-2026-metallohydrolases]] in the same issue of *Nature*. Its headline is not a new reaction but a new activity bar — **de novo catalysts "rivalling those optimized by in vitro evolution"**, with **exquisite stereoselectivity** and six high-resolution structures.

## Problem

The paper's complaint is about *rates*, not scope, and it names it as the field's underemphasised failure: "an often underemphasized limitation of current approaches to enzyme design is the **low initial catalytic rates** of the designed biocatalysts. Even with recent advances, the current paradigm for generating efficient biocatalysts is to **compensate for low initial efficiencies with high-throughput screening and directed evolution**." Current methods "require testing a large number of designs and mostly produce de novo enzymes with low catalytic activities", so they "require costly experimental optimization and high-throughput screening to be industrially viable".

It also states the mechanistic premise the method is built on: "the achievable catalytic effect of an array depends on **how precisely it can be reproduced** in the designed active site", supported by the observation that active designs show catalytic side-chain RMSDs **below 1 Å** between theozyme and experimental structure while **inactive designs show unproductive** geometries.

## Approach — two distinct engineering contributions

**Riff-Diff** (rotamer inverted fragment finder–diffusion) is a hybrid machine-learning and atomistic-modelling pipeline built *on top of* [[watson-2023-rfdiffusion]] rather than replacing it — which is the methodological contrast with [[ahern-2025-rfdiffusion2]], where the generator itself was retrained to accept atomic motifs.

1. **Artificial motif libraries.** Each amino acid of the input catalytic array is **embedded into a helical fragment**, with rotamers selected for compatibility with that fragment backbone so the preferential catalytic rotamer carries minimal energetic penalty. Because arbitrary fragment arrangements can be physically implausible, a script **inverts rotamers of the catalytic array** — fixing functional groups in space while varying backbone atom positions — selects rotamers compatible with the fragment backbones' phi–psi combinations, searches all **non-sterically-clashing** fragment combinations, and ranks assemblies by **rotamer probability and PDB abundance**. The result is a library of high-quality artificial motifs to sample from, used as RFdiffusion input. This is an explicit, enumerative solution to the same inverse-rotamer problem [[ahern-2025-rfdiffusion2]] solved by learning it away.

2. **The placeholder helix — enforcing a binding pocket.** Substrate specificity requires a well-defined asymmetric pocket. From **PDBbind**, the authors measured that in natural enzymes an average of **7.1 α-carbons lie within 8 Å of the substrate**, normalised by ligand heavy atoms, and used this as the burial metric. RFdiffusion's substrate auxiliary potential "decreased the number of clashes between ligand and backbone but **failed to promote the formation of well-defined substrate binding pockets**", producing a trade-off. The fix: add an **α-helix as an entry-channel placeholder** at the pocket position, with a custom auxiliary potential centring the denoising trajectory on that helix and constraining all backbone atoms' distance to it. **The placeholder helix is removed after diffusion, leaving a vacant binding pocket.** Plus iterative backbone refinement cycles.

## Key results

### Retro-aldolases — matching evolved enzymes

Starting from the catalytic tetrad of the **highly evolved retroaldolase RA95.5-8F (PDB 5AN7)** — the same starting point as [[ahern-2025-rfdiffusion2]]'s retroaldolase campaign, which makes this one of the few genuine cross-method comparisons available.

**36 designs ordered, 35 produced, 29 of 35 correctly folded.** The two best, **RAD29 and RAD35**, cleaved rac-methodol at **k_cat = 3.6 × 10⁻² s⁻¹ and 3.1 × 10⁻² s⁻¹** — a roughly **5 × 10⁶-fold rate acceleration** over the uncatalysed reaction. Context the paper provides:

- **Orders of magnitude faster than previous computationally designed retro-aldolases**, and faster than the evolved catalytic antibody **38C2 (k_cat = 1.1 × 10⁻² s⁻¹)**.
- **RAD29's catalytic efficiency of 290 M⁻¹ s⁻¹ (K_M ≈ 100 µM) approaches the extensively evolved RA95.5-5 at 320 M⁻¹ s⁻¹.**
- For comparison, [[ahern-2025-rfdiffusion2]]'s retroaldolase from the same theozyme reached **6.34 ± 0.92 M⁻¹ s⁻¹** — roughly 45-fold lower efficiency, from 96 designs rather than 36.

**Stereoselectivity, which no other ingested enzyme source reports.** Assessed in the aldol direction: **RAD29 was modestly selective (E-value 4, 60% ee for (R)-methodol)** while **RAD35 showed E-value over 200 and 99% enantiomeric excess for (R)-methodol**. Mechanism confirmed by lysine-to-alanine knockouts. The paper is candid that **22 designs had k_cat below 10⁻³ s⁻¹, "within the range achievable by an isolated lysine in a hydrophobic pocket"** — i.e. most designs are not doing designed catalysis, and the authors say so.

**Dynamics.** 20 replicates of 20 ns apo-state MD per design, using root-mean-square fluctuation: in **five designs the catalytic lysine drifted out of the active site**. Apo MD alone did not correlate with activity, prompting prediction of enzyme–substrate complexes directly, where substrate positioning and hydrogen bonding did distinguish designs.

### Morita–Baylis–Hillman — a non-biological reaction

The MBH reaction has **no known natural enzyme**; prior computational designs based on an artificial cofactor gave low activity, and directed evolution of one produced highly active variants. Two evolved catalytic arrays were used as inputs — **BH32.14** and **BH1.8** — for the reaction between 2-cyclohexen-1-one and 4-nitrobenzaldehyde.

**18 designs from BH32.14 and 45 from BH1.8 (23 unique backbones).** Product formation in **17 of 18 (94%)** and **42 of 45 (93.3%)** respectively — a remarkable in-vitro hit rate, though the paper notes median conversions were similar between sets and the highest-conversion designs came from one of them. **MBH48**, the best, has **k_cat = 0.025 min⁻¹, 1.5× higher than BH32.8**, with **minimal by-product formation** and an unfolding onset around **85 °C**.

### Structures — six, at high resolution

Four RAD crystal structures (**PDB 9GBT, 9FW5, 9FW7, 9FWA**) with **Cα RMSD below 1.2 Å** and active-site residues agreeing with design models. **MBH2 at 1.13 Å (PDB 9QDP), Cα RMSD 0.53 Å**; **MBH48 (PDB 9R7F), Cα RMSD 0.78 Å**. In MBH2 a tryptophan adopts a different rotamer in the crystal, pointing away from the active site — consistent with that design's low activity. The paper states its own limit plainly: understanding the rate enhancement "will require more than the two crystal structures presented here".

## Significance / relation to the field

**It is the control [[enzyme-design]] needed.** Every other source in that chapter is Baker-lab or Baker-lab-adjacent. This is an independent group, an independently built pipeline, different reactions, and an explicit decision to build *on* RFdiffusion rather than retrain it — and it reaches activities the Baker-lab campaigns do not, on the reaction where a head-to-head is possible.

**It reframes what counts as success.** The 2026 protease papers report hit rates and rate enhancements against uncatalysed baselines; this paper reports **approach to evolved-enzyme efficiency** and **stereoselectivity**, which are the metrics an industrial biocatalyst is judged on. The chapter's §8 comparability argument gains a fourth axis: not just assay, bar and denominator, but *what quantity the paper considers the point*.

**The placeholder helix is a transferable trick.** It solves a problem RFdiffusion's own auxiliary potential demonstrably does not — pocket formation as distinct from clash avoidance — and it does so by adding a structure that is then deleted. No ingested source does anything comparable.

**And it supports the preorganization thesis from the outside.** Its opening mechanistic claim — sub-1 Å catalytic side-chain RMSD in active designs, unproductive geometries in inactive ones — is the same finding [[choi-2026-cysteine-proteases]] reaches by PLACER and [[kim-2026-metallohydrolases]] uses as a filter, arrived at independently.

**Supplement:** [[braun-2026-riff-diff-supp]].

## Connections

- Built on [[watson-2023-rfdiffusion]] with custom auxiliary potentials; the methodological alternative to retraining the generator, as in [[ahern-2025-rfdiffusion2]].
- Shares the RA95.5-8F retroaldolase theozyme with [[ahern-2025-rfdiffusion2]] — the chapter's only direct cross-method activity comparison on one reaction.
- Its emphasis on second-shell precision and pocket definition aligns with the critique in [[elnesr-2026-zero-shot-metalloenzyme]].
- Published alongside [[kim-2026-metallohydrolases]] in *Nature* 649.
- Chapter: [[enzyme-design]] §4, §5, §7, §8. Concepts: [[catalytic-site-design]], [[motif-scaffolding]].
