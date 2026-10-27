---
type: source
title: Zero-shot design of a de novo metalloenzyme
authors: El Nesr, Dürr, Mathews, Wen, Zhao, Sarangi, Rothlisberger, Sunden & Huang (Stanford / EPFL / SLAC)
venue: bioRxiv 2026 (doi 10.64898/2026.04.23.720277; v posted 18 June 2026)
pdf: "../sources/ProteinDesign/ElNesrHuang_biorxvi_2026.04.23_Zero-shot design of a de novo metalloenzyme.pdf"
supp: no
tags: [enzyme-design, metalloenzyme, zinc, multi-objective, evolutionary-algorithm, second-shell, oracle-failure, xas, crystallography, huang-lab]
ingested: 2026-10-21
---

# dEVA — zero-shot design of a de novo metalloenzyme

A metalloenzyme designed **without a catalytic motif**, by multi-objective optimisation of the metal coordination sphere itself — reaching the **highest rate enhancement reported for any de novo designed hydrolase**. It is also the wiki's most damaging documented case of a structure-prediction oracle confidently endorsing a design that does not work.

**Non-Baker-lab.** Huang lab (Stanford) with Rothlisberger (EPFL) and SLAC; the methodological counterweight in [[enzyme-design]] to the motif-scaffolding stack that otherwise dominates it. `supp: no` — the SI figures and tables (S1–S24) are referenced throughout but not supplied as a separate PDF.

## Problem

The paper's objection to the prevailing approach is precise and is the reason it belongs in the chapter. Current methods use **motif scaffolding**: a set of residues believed to facilitate catalysis is extracted from a natural enzyme or generated, then placed in a designed backbone. "While this workflow is intended to preserve the motif geometry to hopefully recapitulate catalytic function, **optimizing for the motif alone does not guarantee catalytic competence**."

The reason is second-shell. "Enzyme activity is well established to extend beyond the catalytic motif. **Second-shell residues around the motif play an important role in mediating affinity, specificity, and reactivity.** These contributions are well documented in natural enzymes but are largely" absent from motif-centric design. Metalloenzymes impose an additional constraint, since the metal's coordination geometry and electronic environment govern reactivity.

## Approach

**dEVA (design by EVolutionary Algorithm)** is a multi-objective design framework built on **NSGA-II**, the non-dominated sorting genetic algorithm. Given a structure and a set of objective functions, it explores sequence space and returns solutions on the **Pareto front**, selecting the **knee point** rather than optimising any single score. It is **zero-shot**: "it imposes no requirement for structure prediction, natural templates, or evolutionary information."

For metal-site design, two objectives are paired:

- **p(sequence | metal, structure)** — **LigandMPNN**, trained to consider non-protein atoms, proposes mutations and side-chain conformations.
- **p(metal | sequence, structure)** — **[[durr-2023-metal3d]]** predicts metal location from the local chemical environment.

Each iteration alternates the two until the population reaches the Pareto front. Scaffolds came from a diverse library of **non-all-helical backbones generated with [[protpardelle]]**, and full sequences were initialised with **ensemble Caliby**, a Potts-based sequence design model conditioned on synthetic structural ensembles to remove non-structural sequence bias.

## Key results

### Metal-binding sites, designed without templates

Eight designs spanning lengths, topologies and coordination motifs were characterised; **all eight expressed well in *E. coli* as soluble monomers**.

- **desH2C2** — an immunoglobulin-like fold with a **His₂Cys₂ site designed without a motif template**. Binds zinc at **K_d = 37 ± 4 nM** with 1:1 stoichiometry by ICP-MS; zinc confers thermal stability absent in the apo form. **EXAFS** established **2 Zn–N and 2 Zn–S** coordination, and the normalised Zn K-edge shows whiteline differences from canonical zinc fingers — evidence of "a de novo coordination geometry, distinct from structurally characterized, zinc-containing proteins in the PDB".
- **Three crystal structures** confirm backbone fidelity on complex folds: **desHE2**, a de novo asymmetric β-propeller at **1.48 Å (PDB 12WO)**, with the zinc resolved **within 0.90 Å of the designed location**; **desE2D**, a de novo half-open TIM barrel at **1.55 Å (PDB 12WN)**; and **desDEH (PDB 12WM)**. In the latter two the metal site was ambiguous in density, but XAS confirmed protein-bound zinc with first-shell distances shorter than free ZnCl₂.

### The oracle failure, stated as a negative control

**desD1** was chosen deliberately far from the Pareto knee point: its designed site **contains only a single ligand within binding distance**, which cannot chelate a metal. Experimentally it shows **no detectable zinc binding** — null by MagFura-2 competition titration and by ICP-MS.

Then the finding that matters. Post hoc, **AlphaFold3 predicted desD1 with excellent overall structural agreement and assigned the metal high confidence — Zn pLDDT 86.55 — placing it exactly where the low-confidence design had put it.** The authors state the consequence outright: **"By standard computational metrics and filtering criteria, this design would have been classified as a success."**

### Why: the training data

The ambiguity prompted an audit of what the models had learned. Analysing the training sets of LigandMPNN and Metal3D, the authors found zinc sites with **fewer than three coordinating residues within 3.0 Å** — environments that "may reflect crystallization additives or soaking agents rather than biologically" meaningful sites. They retrained as **Metal3D-Clean**, excluding those, and found the expected trade-off on a held-out test set: **Metal3D-Clean assigns substantially lower confidence** to such sites. The conclusion is that dEVA's designs are "sensitive to the data its models are trained on" — and the same must be true of any method built on these predictors. Most designs had **weak affinity** despite dEVA's second-shell consideration, which the authors attribute to this.

### The enzyme: desB

To get catalysis rather than binding, they trained **Metal3D-Cat** on only **annotated catalytic zincs from MAHOMES-II**, approximating **p(catalytic metal | sequence, structure)**. dEVA explored catalytic zinc configurations within a TIM-barrel cavity and returned **only three Pareto-optimal solutions** — desA, desB, desC — screened against phospho-ester substrates, the reaction class best represented in Metal3D-Cat's training data.

**desB** is the hit, and it has a **binuclear zinc site** — "the same bi-zinc site that underlies the exceptional efficiency of many naturally occurring metallohydrolases", which dEVA was not told to build.

- **Novelty.** The zinc site is "an entirely de novo motif": **Folddisco** and **RCSB Structure Motif Search** returned no structural motif neighbours, **BLAST** no sequence homologues, and **Foldseek** structural neighbours contain no bi-zinc sites.
- **Site dependence.** EDTA chelation reduces activity (though it also destabilises the protein, precluding a K_d); alanine scanning of **first- and second-shell** residues reduced activity; **ICP-MS confirms two zinc ions per monomer**; pH profiling shows alkaline optimum, consistent with two proximal zincs lowering the pK_a of metal-bound water to ~7.
- **XAS with orthophosphate** as a ground-state analogue: **Zn–Zn distance ~4.3 Å in solution**, within the range of catalytically competent binuclear zinc hydrolases; EXAFS fits **4 Zn–N, 1 Zn–P, 1 Zn–Zn**, the Zn–P contribution indicating direct phosphate coordination. Phosphate inhibits with **K_i,app = 1.0 ± 0.2 µM**, similar to natural alkaline phosphatases.
- **Catalysis.** **Phosphomonoester** hydrolysis — uncatalysed half-life **>500,000 years** — with **k_cat/K_M = 1300 ± 400 and 1500 ± 700 M⁻¹ s⁻¹** for 4-MUP and DiF-MUP. Rate enhancement **(k_cat/K_M)/k_w = 3 × 10¹³** for 4-MUP, "**the highest reported rate enhancement for any de novo designed hydrolase to date**", and within the range of natural phosphomonoesterases. Multiple turnover confirmed at sub-stoichiometric enzyme.
- **Promiscuity.** desB also hydrolyses **phosphodiesters** — uncatalysed half-lives **>13 million years**, a different charge state and transition-state geometry — with rate enhancements of **3 × 10¹¹ (me-pNPP)** and **6 × 10¹² (bis-pNPP)** and k_cat/K_M of 1.2 ± 0.3 and 1.5 ± 0.3 M⁻¹ s⁻¹, again comparable to natural phosphodiesterases.
- **Structure.** X-ray at **2.29 Å (PDB 36BS)** confirming the TIM-barrel fold (**Cα-RMSD 2.37 Å**) with the binuclear zinc site resolved and the designed first-shell ligand chemistry intact. The **Zn–Zn separation is 5.9 Å**, matching the design model's 5.8 Å but contrasting with the **compressed 4.3 Å** seen on phosphate binding — supporting a mechanism in which desB has an open, solvent-exposed resting state that closes on substrate.

## Significance / relation to the field

**It is the chapter's counter-argument to motif scaffolding.** Every other enzyme source in the wiki starts from a native catalytic motif. dEVA starts from a scaffold and an objective, designs the coordination sphere directly, and arrives at a binuclear zinc site that nature also uses — without being shown one. That is a different claim about where catalytic competence comes from, and the rate enhancement makes it hard to dismiss.

**The desD1 result should be read alongside the binder chapter's §10.** [[de-novo-binder-design]] catalogues four ways an oracle misleads; this is a fifth and the most specific — **a structure predictor assigning pLDDT 86.55 to a metal in a site that physically cannot bind one**, with the authors tracing it to crystallisation artefacts in the training data. It is also a rare instance of a group publishing the design their own filters would have passed and experiment rejected.

**And it reframes "zero-shot".** [[butcher-2026-rfdiffusion3-science]] uses the term for campaigns with no experimental optimisation; dEVA uses it for a method requiring no structure prediction, no natural template and no evolutionary information. The chapter keeps the two senses distinct.

**Caveats the chapter carries.** The enzyme result rests on **three Pareto-optimal designs**, one of which worked; the substrate class was chosen because it dominates Metal3D-Cat's training data, so the demonstration is in-distribution for the objective model even if out-of-distribution for the PDB; and K_d could not be determined for desB because chelation destabilises it.

## Connections

- Built on **[[durr-2023-metal3d]]** (and its retrained Metal3D-Clean and Metal3D-Cat variants), LigandMPNN — the ligand-aware successor to [[dauparas-2022-proteinmpnn]] — and scaffolds from [[protpardelle]] ([[chu-2024-protpardelle]]).
- The methodological opposite of the motif-scaffolding route in [[chen-2026-metalloproteases]], [[choi-2026-cysteine-proteases]] and [[butcher-2026-rfdiffusion3-science]]; same metal, different premise.
- Its multi-objective Pareto search is a distinct third option alongside the generative and hallucination families discussed in [[de-novo-binder-design]] §11; compare the test-time search of [[didi-2026-complexa-scaling]].
- The desD1 oracle failure bears on [[abramson-2024-alphafold3]] used as a design filter.
- Chapter: [[enzyme-design]] §2, §4, §5, §6, §7. Concepts: [[metalloprotein-design]], [[catalytic-site-design]].
