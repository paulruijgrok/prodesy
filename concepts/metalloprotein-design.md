---
type: concept
tags: [metalloprotein-design, zinc, enzyme-design, coordination, xas, prediction]
sources: 8
updated: 2026-10-21
---

# Metalloprotein design

Designing proteins that bind a metal ion in a specified coordination geometry — structurally, or to do chemistry. Treated in depth in [[enzyme-design]] §7.

**Why metals.** They are "biologically abundant, tether to the protein using strong interactions, and have favorable catalytic properties"; zinc in particular is an excellent Lewis acid, serves structural roles (zinc fingers) and catalytic ones in sites up to trinuclear, and **about 10% of all enzyme-catalysed reactions use zinc** ([[durr-2023-metal3d]]).

**Why it is hard.** Computational design "is hampered by the complex electronic structure of many biologically relevant metals": classical force fields treat metals poorly, and quantum-mechanical treatment is too expensive for design-scale work, usable only to verify selected candidates ([[durr-2023-metal3d]]).

**Two routes, with different premises.**

1. **Transplant a native metal site, or derive one from first principles.** [[chen-2026-metalloproteases]] takes a Zn(II) centre of two histidines and a glutamate from aminopeptidase N, with water as the fourth ligand, and scaffolds it. [[kim-2026-metallohydrolases]] instead derives the theozyme from **DFT** — the transition-state geometry for Zn(II)-hydroxide attack on an ester — copying no native enzyme, and reaches **53,000 M⁻¹ s⁻¹**, against 3–60 M⁻¹ s⁻¹ for previously designed metallohydrolases. In that design the **Zn(II) ion itself serves as the oxyanion hole**, with no nearby side-chain hydrogen-bond donors, sidestepping the many-body buried-polar problem entirely. [[butcher-2026-rfdiffusion3-science]] goes further, scaffolding a di-metal site bridged by a **post-translationally carbamylated lysine** — and shows the modification matters, since removing it costs 11-fold in k_cat. [[wang-2022-functional-site-scaffolding]] and [[watson-2023-rfdiffusion]] established metal-binding sites as a scaffoldable motif class.
2. **Design the coordination sphere directly.** [[elnesr-2026-zero-shot-metalloenzyme]] pairs LigandMPNN with [[durr-2023-metal3d]] in a multi-objective evolutionary search, producing a **His₂Cys₂ site with no motif template** binding zinc at K_d 37 ± 4 nM, and — after retraining the metal predictor on catalytic zincs only — a **binuclear zinc hydrolase** with no structural-motif, sequence or fold neighbour containing a bi-zinc site.

**Prediction as a design objective.** [[durr-2023-metal3d]] predicts zinc location from a voxelized local environment to **0.70 ± 0.64 Å**, template-independently, and emits a per-residue density usable inside a design loop — which is what makes route 2 possible at all.

**The training-data caveat, which is now a documented failure.** Metal3D is trained on zinc alone, and its supplement stratifies performance by coordination number and occupancy throughout ([[durr-2023-metal3d-supp]]), including a named false positive where a calcium site is called as zinc at p = 0.9. [[elnesr-2026-zero-shot-metalloenzyme]] audited the training corpus, found zinc sites with fewer than three coordinating residues within 3.0 Å that "may reflect crystallization additives or soaking agents", retrained **Metal3D-Clean** excluding them, and separately **Metal3D-Cat** on catalytic zincs from MAHOMES-II. The lesson: a model trained on *zinc appears here in a crystal* learns something different from *zinc is functionally bound here*, and the difference only became consequential once the model was used generatively.

**Validation specific to metals.** Beyond crystallography: **ICP-MS** for stoichiometry, **chelation** for activity dependence, competition titration for affinity, and **XAS/EXAFS** for the solution-state coordination shell — the last unique in this wiki to [[elnesr-2026-zero-shot-metalloenzyme]], and the only method here that reports on the metal site in the state the protein actually works in.

**Zinc affinity is a persistent weak point.** [[kim-2026-metallohydrolases]] measures **K_D = 41 ± 5 nM** for its best design, similar to previous designed zinc enzymes but weaker than native zinc hydrolases, which are "typically below 10 nM"; [[elnesr-2026-zero-shot-metalloenzyme]] reports 37 ± 4 nM for a template-free His₂Cys₂ site and could not determine K_d for its bi-zinc enzyme because chelation destabilises the protein. Designed metal sites bind, and bind more weakly than evolved ones.

**Mechanism is often only partly confirmed.** In [[kim-2026-metallohydrolases]], the triple-histidine knockout inactivates as expected, but **H130A costs only 13-fold and the proposed general base D67A barely affects k_cat/K_M while increasing zinc affinity** — consistent with competing zinc-binding configurations rather than the designed one. Designed metalloenzymes work; the residue-by-residue account of why is frequently incomplete.

**Sources:** see §12 of [[enzyme-design]].
