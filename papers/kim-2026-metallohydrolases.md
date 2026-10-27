---
type: source
title: Computational design of metallohydrolases
authors: Kim, Woodbury, Ahern, Tischer, Kang et al. (Baker lab, with Kalvet & Hilvert)
venue: Nature 2026 (649, 246–253; online 3 December 2025; doi 10.1038/s41586-025-09746-w)
supp: yes
pdf: "../sources/ProteinDesign/KimBaker_Nature_2026_Computational design of metallohydrolases.pdf"
tags: [enzyme-design, metalloenzyme, zinc, esterase, DFT, PLACER, preorganization, crystallography, validation]
ingested: 2026-10-21
---

# Computational design of metallohydrolases

The companion paper to [[ahern-2025-rfdiffusion2]], and the one that made **PLACER a validated design filter rather than a post-hoc explanation**. De novo zinc esterases designed from quantum-chemistry active-site geometries, reaching catalytic efficiencies orders of magnitude above previous designed metallohydrolases **without any experimental optimisation**.

## Problem

Metallohydrolases "catalyse some of the most difficult hydrolysis reactions in biology by using their bound metal ions to activate a water molecule positioned adjacent to the substrate bond to be cleaved", and engineering new ones matters for degrading human-made pollutants "for which there has not been sufficient time for efficient hydrolytic enzymes to evolve". Prior de novo metallohydrolases "have had relatively low activity and efficiency, and have required extensive directed evolution to match the activity and efficiency of native enzymes".

The method constraint is stated crisply: RFdiffusion "requires specifying both the sequence position and backbone coordinates for each catalytic residue, limiting sampling". RFD2 removes both — it scaffolds **arbitrary atom-level** motifs rather than backbone-level ones, needing only the functional groups contacting the transition state rather than full side-chain and backbone conformations, and it is **sequence-position-agnostic**.

## Approach

**Target reaction:** hydrolysis of the fluorogenic ester **4-methylumbelliferyl phenylacetate (4MU-PA)**.

**Theozyme from DFT, not from nature.** Density functional theory identified the transition-state geometry for Zn(II)-hydroxide nucleophilic attack on the 4MU-PA ester. This is the paper's quiet methodological point: the active site is derived from first principles, so there is no native enzyme whose geometry is being copied.

**Pipeline.** RFD2 builds scaffolds housing the DFT-generated minimal active site → sequences designed per scaffold → **AlphaFold2** prediction filters for designs adopting the target structure → designs with a **proposed general base positioned to activate the water** and appropriate transition-state oxyanion treatment → **PLACER** characterisation of active-site preorganization. **96 designs selected** for experimental testing.

## Key results

### Round 1

**86 of 96 designs expressed and were soluble.** On zinc supplementation and 4MU-PA fluorescence, **5 designs (A1, A8, B9, C4, F7) had activity well above background**. Michaelis–Menten characterisation gave **k_cat/K_M = 16,000 ± 2,000 M⁻¹ s⁻¹ for A1** and 35–140 M⁻¹ s⁻¹ for the other four. For comparison, **previously designed metallohydrolases ranged from 3 to 60 M⁻¹ s⁻¹** — so A1 is two to three orders of magnitude beyond the prior art, out of the computer.

A1 — renamed **ZETA_1** (zinc metalloesterase 1) — retains activity for **at least 1,000 turnovers**, and differs substantially from known proteins: closest TM-alignment matches in the PDB and AFDB score **0.41 and 0.49** with no analogous catalytic-residue arrangements.

**Active site:** a primarily hydrophobic pocket with **three histidines binding Zn(II) through their Nε atoms**, an aspartate as potential general base, and an asparagine hydrogen-bonding the coumarin ring. Notably, **the Zn(II) ion itself acts as the oxyanion hole**, stabilising developing negative charge at the transition state, with no nearby side-chain hydrogen-bond donors.

**Zinc dependence and mutagenesis.** Chelation with 1,10-phenanthroline eliminated activity, restored by adding zinc. **K_D for Zn(II) = 41 ± 5 nM**, similar to previous designed zinc enzymes but weaker than native zinc hydrolases, which are typically below 10 nM. N17A cost **8.1-fold** in k_cat/K_M; the triple histidine knockout and two of three single His-to-Ala substitutions **completely inactivated**; but **H130A cost only 13-fold** and **D67A — the proposed general base — had little effect on k_cat/K_M and increased Zn(II) affinity**, suggesting competing zinc-binding configurations. The designed mechanism is therefore partly confirmed and partly not, which the paper states rather than smooths.

### The PLACER result — a filter validated both ways

**ZETA_1 was the top-ranked design in the in silico ranking.** PLACER — described here as a network that, given a backbone containing a substrate, **fully randomises the substrate and all side chains within a 600-atom sphere and regenerates their coordinates**, with repeated trajectories giving an ensemble — predicted ZETA_1's active site to be highly preorganized, with catalytic side chains fixed and the substrate held in its designed position. ZETA_1 "stood out from the other designs" on both axes: catalytic-site preorganization and substrate positioning. In the inactive designs H7 and H8, the substrate "fluctuated considerably".

Then the retrospective test that makes this more than a correlation: **seven designs from the same ZETA_1 backbone family had been filtered out during design selection for suboptimal PLACER metrics. They were expressed and purified retrospectively and found to have very low or no activity.** Same backbone family, same campaign — separated only by a PLACER score. The conclusion drawn is that combining global structure prediction with detailed PLACER modelling of the active site "provides a powerful approach to assessing the catalytic machinery and substrate binding geometry for design selection".

### Round 2

A second 96-design round, with theozymes **containing the catalytic base** and Zn(II) coordinated by His Nε atoms with Cβ explicitly modelled, yielded **3 more highly active enzymes**: **ZETA_2 at k_cat/K_M = 53,000 ± 5,000 M⁻¹ s⁻¹ with k_cat = 1.5 ± 0.1 s⁻¹**, ZETA_3 at 19,000 ± 2,000, and ZETA_4 at 1,100 ± 200. The four most active designs differ from known structures **and from each other**.

### Structure

**ZETA_2 apo at 3.5 Å (PDB 9PYJ)**: backbones nearly superimposable with the design model at **Cα r.m.s.d. 1.1 Å**, catalytic residues preorganized in the designed geometry, binding pocket complementary to the superimposed transition state. **Zn(II)-soaked at 2.1 Å (PDB 9PYL)**: Cα r.m.s.d. **0.8 Å**, zinc present at **100% occupancy** at the designed location (1.7 Å r.m.s.d.) — though one coordinating histidine (H110) was flipped out to a surface-bound zinc, attributed to the **250 mM** zinc in the soaking buffer.

## Significance / relation to the field

**It is the chapter's strongest evidence that filtering on an ensemble works.** [[enzyme-design]] §5 argues the field's residual gap is that designs are specified as single structures while catalysis depends on a distribution. This paper filters on a distribution — PLACER ensembles — prospectively, gets its best design ranked first, and then shows that same-backbone designs rejected by that filter are inactive. [[choi-2026-cysteine-proteases]] later uses PLACER to *explain* a gap retrospectively; here it is used to *select*, and it worked.

**It is the activity benchmark the 2026 protease papers are measured against.** Both [[choi-2026-cysteine-proteases]] and [[chen-2026-metalloproteases]] cite this work as the metallohydrolase precedent, and [[choi-2026-cysteine-proteases]] positions amide hydrolysis as the step beyond it. The numbers make the framing concrete: 53,000 M⁻¹ s⁻¹ on an **ester** here, against 413 M⁻¹ s⁻¹ on an **amide** in the cysteine protease work — roughly two orders of magnitude, which is the cost of the substrate change rather than of the method.

**And the Zn-as-oxyanion-hole design is unusual.** Rather than building a hydrogen-bond donor network to stabilise the oxyanion — the hard, many-body problem of [[boyken-2016-hydrogen-bond-network-oligomers]] — the metal does that work. That is a design simplification worth noting against the oxyanion-hole difficulties reported in [[choi-2026-cysteine-proteases]].

**Supplement:** [[kim-2026-metallohydrolases-supp]].

## Connections

- Direct companion to [[ahern-2025-rfdiffusion2]], which summarises these campaigns and refers here for detail.
- The precedent both [[chen-2026-metalloproteases]] and [[choi-2026-cysteine-proteases]] position against; shares the zinc-activated-water mechanism with the former.
- PLACER, used prospectively here and retrospectively in [[choi-2026-cysteine-proteases]], remains un-ingested — see the flagged references in [[enzyme-design]].
- Uses [[jumper-2021-alphafold2]] for structure filtering and Chai-1 for protein–Zn(II)–substrate prediction.
- Contrast [[elnesr-2026-zero-shot-metalloenzyme]], which designs the coordination sphere rather than scaffolding a DFT theozyme, and [[durr-2023-metal3d]] on predicting metal location.
- Chapter: [[enzyme-design]] §2, §4, §5, §6, §8. Concepts: [[metalloprotein-design]], [[catalytic-site-design]].
