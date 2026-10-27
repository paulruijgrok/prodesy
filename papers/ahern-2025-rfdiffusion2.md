---
type: source
title: Atom-level enzyme active site scaffolding using RFdiffusion2
authors: Ahern, Yim, Tischer, Salike, Woodbury, Kim et al. (Baker lab, with Barzilay & Jaakkola)
venue: Nature Methods 2025 (23, 96–105, January 2026 issue; online 3 December 2025; doi 10.1038/s41592-025-02975-x)
pdf: "../sources/ProteinDesign/AhernBaker_NatureMethods_2025_Atom-level enzyme active site scaffolding using RFdiffusion2.pdf"
supp: yes
tags: [enzyme-design, motif-scaffolding, flow-matching, atomic-motif, AME-benchmark, retroaldolase, esterase, metallohydrolase, foundational]
ingested: 2026-10-21
---

# RFdiffusion2 — atom-level enzyme active site scaffolding

The method paper the enzyme chapter was describing second-hand. RFD2 removes the two constraints that had bounded de novo enzyme design: it designs **directly from functional group geometries without specifying residue order and without inverse rotamer generation**.

**Closes the wiki's highest-priority enzyme gap.** [[choi-2026-cysteine-proteases]], [[chen-2026-metalloproteases]] and [[kim-2026-metallohydrolases]] all use RFD2 or its molecular-interfaces variant as their generator, and [[butcher-2026-rfdiffusion3-science]] defines its own contribution against RFD2's limitations. Until now [[enzyme-design]] §3 described the pivotal capability through papers that merely used it.

## Problem

De novo enzyme design starts from a **theozyme** — a description of protein functional groups placed around the reaction transition state(s) and any cofactors — and the task is to generate scaffolds that accommodate it. The paper's account of the prior state is precise and is the chapter's best statement of what the field was stuck on:

- **Pre-deep-learning**, RosettaMatch searched existing native or designed scaffolds for placements of the catalytic residues. Many enzymes were designed this way, but the approach "was restricted to theozyme geometries that could be matched to the input scaffold set".
- **Diffusion models** removed the scaffold-library requirement for many substructures, but existing motif-scaffolding methods represent motifs as **backbone frames**, parameterising each residue's N, Cα, C atoms as an element of SE(3) — and **each motif frame requires a prespecified sequence index** giving its location along the backbone. That representation suffices for scaffolding large contiguous domains, but a theozyme is not that: it is a handful of functional groups whose sequence positions are unknown and whose rotamers must be inferred.
- The workaround was **inverse rotamer sampling**: enumerate backbone placements consistent with each side-chain geometry. The paper's objection is that this is expert-intensive and limits sampling.

## Approach

**Mixed frame/atom representation.** Input and output residues can be represented **either as a frame or as heavy atoms**, so the model can keep some residues as frames and **atomize** others. For each atomized residue the network learns the distribution of side-chain poses. Representing *atoms* rather than whole residues is what lets the method "forgo inverse rotamer sampling", because the network infers an appropriate rotamer and scaffold jointly.

**Unindexed residues — the key trick.** By modifying the index features the model is given **"unindexed residues"**, whose sequence position is not revealed. With **no auxiliary losses**, the network learns that unindexed residues are always superimposed on some residue of the generated protein; conditioning on a set of unindexed residues — an **"unindexed motif"** — therefore makes the model sample proteins conditioned on the motif *without* being told where along the chain it sits. The paper shows the mechanism directly, tracking the distance between the Cα of each unindexed residue and the Cα of the protein residue it converges onto over the trajectory.

**Flow matching rather than denoising diffusion.** Given the complexity of unindexed atomic motif scaffolding, a more stable training framework was wanted: flow matching interpolates a training example toward a noise sample and trains the network to denoise. The data representation contains **both atoms (ℝ³) and backbone frames (SE(3))**, with flow matching on ℝ³ following the Gaussian probability-path derivation and the SE(3) component following the FrameFlow formulation. Training filters out "common solvents and crystallization" additives, and each residue is featurized as frame-or-atomized and as indexed-or-unindexed, with ligands included where present.

## Key results

### The AME benchmark, introduced here

The paper notes that the pre-existing enzyme motif-scaffolding benchmark "does not" reflect the real problem, and builds a new one: PDB crystal structures where **all reactants and cofactors were present**, curated down to **41 active sites** spanning a diverse set of reactions. 100 structures were sampled per benchmark case. This is the **atomic motif enzyme (AME)** benchmark, released with the paper, and it is the shared evaluation that [[butcher-2026-rfdiffusion3-science]], [[didi-2026-complexa-scaling]] and [[lin-2026-genie3]] all later report against.

**RFdiffusion2 finds solutions to all 41 benchmark cases; previous methods solved 16.** Benchmark difficulty correlates with motif complexity. An ablation separates the two contributions — atomization and unindexed motif scaffolding — by comparing three rotamer-resolution approaches including naive inverse rotamer sampling.

### Three experimental campaigns, each under 96 designs

The paper's framing is that functional enzymes were obtained "when screening less than 96 designs", and that the most active design for each reaction is **structurally distinct from everything in the PDB**.

**Retroaldolase.** Theozyme taken from the evolved retroaldolase **RA95.5-8F (PDB 5AN7)**. 96 designs expressed in an in vitro transcription/translation system and assayed on racemic Methodol: **4 variants showed detectable activity**, and the best purified design gave **k_cat/K_M = 6.34 ± 0.92 M⁻¹ s⁻¹**.

**Cysteine esterase.** A **Cys–His–Asn** catalytic triad with a **helix-dipole-stabilised oxyanion hole** formed by the cysteine backbone nitrogen plus a glutamine. The minimal motif comprised the functional groups of Cys, His, Asn and Gln **plus 3–4 backbone atoms of residues abutting the cysteine, included specifically to force the local backbone into the region of Ramachandran space corresponding to a helix terminus oriented so its dipole stabilises the oxyanion hole** — an unusually explicit statement of designing a *second-shell* electrostatic feature. Geometry from a papaya cysteine hydrolase (**PDB 1PPN**), substrate 4MU-butyrate. Of **48 designs screened**, several were active; the best showed multiple-turnover activity at **k_cat/K_M = 248 ± 34 M⁻¹ s⁻¹** for the acylation step, better than previous designed cysteine esterases on the same leaving group.

**Metallohydrolases**, done in detail in the companion paper [[kim-2026-metallohydrolases]] and summarised here. Theozyme from **DFT** rather than from a native enzyme — finding the transition-state geometry in which hydroxide bonds the carbonyl carbon, simulating Zn(II), imidazole metal-coordinating groups, reactant and hydroxide. 96 designs per substrate gave **3 functional enzymes for 4MU-butyrate and 5 for 4MU-phenylacetate**; best k_cat/K_M **77 ± 10 M⁻¹ s⁻¹** and **16,000 ± 2,000 M⁻¹ s⁻¹** respectively, the latter "several orders of magnitude higher than previously designed zinc hydrolases". A second set of 96 designs **including a general base to activate the water** gave **11 functional enzymes**, best at **53,000 ± 5,000 M⁻¹ s⁻¹**.

### What the authors say remains

RFD2 "removes expert intuition necessary with prior backbone motif-scaffolding and scaffold library methods" — but "the enzymes designed by RFdiffusion2 are not as active as native" enzymes.

## Significance / relation to the field

**It names the constraint the whole chapter turns on.** The distinction between an *indexed backbone frame* and an *unindexed atomized residue* is what separates "scaffold this domain" from "build a protein that happens to present these four functional groups in this geometry". Every 2026 protease campaign depends on it.

**It supplies the field's shared benchmark.** AME is introduced here with an explicit rationale for why its predecessor was inadequate, and the 41-case curation — all reactants and cofactors present — is the reason later papers can report comparable numbers at all. The jump from 16 to 41 solved cases is the single clearest before/after in [[enzyme-design]].

**The helix-dipole oxyanion hole deserves attention.** Including backbone atoms specifically to force a helix terminus whose dipole stabilises the oxyanion is a designed second-shell electrostatic effect, which is exactly the property [[elnesr-2026-zero-shot-metalloenzyme]] argues motif scaffolding neglects. So the criticism and a counterexample to it are both in the 2025–26 literature.

**Supplement:** [[ahern-2025-rfdiffusion2-supp]].

## Connections

- The generator behind [[choi-2026-cysteine-proteases]] and [[chen-2026-metalloproteases]] (via RFD2-MI) and [[kim-2026-metallohydrolases]] (direct companion paper); superseded by [[butcher-2026-rfdiffusion3-science]], which moves from mixed frame/atom to fully free-atom diffusion.
- Successor to [[watson-2023-rfdiffusion]], whose indexed backbone-frame motif representation it diagnoses as the limiting constraint; also generalises [[wang-2022-functional-site-scaffolding]].
- Introduces the AME benchmark used by [[butcher-2025-rfdiffusion3]], [[butcher-2026-rfdiffusion3-science]], [[didi-2026-complexa-scaling]] and [[lin-2026-genie3]].
- Its SE(3) flow-matching formulation follows FrameFlow, the lineage [[lin-2024-genie2]] also benchmarks against.
- A fine-tuned RFD2 is the generator for de novo antibodies in [[bennett-2026-de-novo-antibodies]].
- Chapter: [[enzyme-design]] §3, §4. Concepts: [[motif-scaffolding]], [[catalytic-site-design]]. Tool: [[rfdiffusion2]].
