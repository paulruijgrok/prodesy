---
type: source
title: "BoltzGen: Toward Universal Binder Design"
authors: Stark, Faltings, Choi, Xie et al. (MIT / Boltz, with DeGrado, Liu, Sabatini labs)
venue: bioRxiv 2025 (preprint, 2025-11-20)
pdf: "../sources/ProteinDesign/StarkJaakola_Boltzgen_bioRvix_2025.pdf"
supp: no
tags: [binder-design, all-atom, modalities, nanobodies, peptides, small-molecules, disordered, validation, open-source]
ingested: 2026-10-12
---

# BoltzGen — toward universal binder design

A single all-atom generative model for designing binders **across modalities and target classes**, validated in eight wet-lab campaigns over 26 targets — the broadest experimental validation of any source in the wiki, and the strongest available evidence on how binder design behaves against targets with no structural precedent.

**Problem.** Binder-design methods have been tailored to specific modality classes (nanobodies, miniproteins, peptides) and evaluated accordingly, and real discovery campaigns impose requirements those methods do not address. The paper's framing target is **universality**: one model, any binder modality, any biomolecular target.

**Approach.** Design and structure prediction are **unified in one model**, so that the generator carries structural reasoning about target–binder interactions rather than delegating it to a separate oracle; the same model reaches state-of-the-art folding performance. Generation is controlled by a **design specification language** over covalent bonds, structure constraints, binding sites and more — so a cyclic peptide is specified by declaring a covalent bond, and a nanobody by fixing a framework's structure and sequence while replacing the three CDRs with loops of random length. Four default nanobody scaffolds are provided. Model weights, data, training and inference code are released under the MIT License.

## Key results

**The novelty control, which is the paper's most important methodological choice.** Nine targets were selected for which **no protein with >30% sequence identity exists in a bound context anywhere in the PDB**. Against each, 60,000 nanobodies were generated *without specifying any binding site*, and 15 selected for testing; separately 60,000 proteins of length 80–140 per target, again 15 tested.

- **Nanobodies: nM-affinity binders for 6 of 9 targets (66%)** by SPR and BLI.
- **Protein binders: nM binders for 6 of 9 targets (66%)** — the same rate, from the same 15-design budget.

**Benchmark targets** (TNFα, PD-L1, IL-7Rα and others with known high-affinity binders): testing at most 20 designed proteins and 15 nanobodies gave **nM binders against 80% (4 of 5)** of targets for both modalities.

**Across modalities.**

- **Bioactive peptides** (protegrin — a disulfide-rich β-hairpin; melittin — intrinsically unfolded in dilute solution; indolicidin): testing only 6 binders per target gave nM binders for two and µM for the third. Melittin binders mel2 and mel3 measured **0.41 µM and 4.4 µM** K_D.
- **Disordered targets.** 20,000 peptide designs of 40–80 residues against the **disordered region of NPM1**, specified to engage the disordered region while avoiding its structured β-sheet — i.e. the model is tasked with predicting how the disordered region will *become* structured in the presence of the designed binder. Five designs tested; the paper reports evidence of de novo designs binding disordered proteins **in live cells**, while explicitly cautioning that the in-cell experiment does not confirm that binding occurs specifically at the disordered region.
- **Disulfide-cyclized peptides** against the RagA:RagC dimer: 50,000 ranked designs of size 10–18 with two covalently bonded cysteines separated by six designed residues. Binders found, but affinities are weak — **80 µM highest, 164 µM second** of the eight resolved by SPR.
- **Linear peptides** to RagC: 7 binders from 29 tested, best **3.5 µM**.
- **Nanobodies to two recently deposited monomer targets** (Penguinpox cGAMP phosphodiesterase, Bordetella filamentous hemagglutinin): 7 designs each by yeast surface display; 1 hit on Penguinpox and 7 on hemagglutinin, with affinity **at best 2 µM** (the assay cannot resolve it further).
- **Small molecules.** Rucaparib (10,000 designs, 6 tested, 5 bound at **50–150 µM**) and a rhodamine derivative (20,000 designs, 4 tested, all **30–250 µM**). The paper is candid that prior specialist work reached low-nanomolar on rucaparib through an expert-guided approach, and claims only that a general-purpose model achieves moderate affinity with simpler customization.
- **Antimicrobial peptides** against GyrA: **19.5%** of designs inhibited cell growth by more than 4×.

**The ranking result, and why it belongs in a chapter about filtering.** Similar experiments were run on designs from an earlier BoltzGen version that "suffered from a serious flaw resulting in close-to-random ranking and filtering." For those designs, **no hits were found**. The generator was substantially the same; the ranking and filtering were not. This is the cleanest available natural experiment on the proposition that a modern binder pipeline's hit rate is a property of its filter at least as much as of its generator.

**An internal inconsistency to note.** The executive summary states that disulfide-bonded peptide design against RagA:RagC "yields binders for **14 of 28** tested designs", while §2.6 states "we test **24** designs in a binding affinity assay and find 14 binders." The denominator differs between the two statements; the numerator does not. Recorded, not resolved.

## Significance / relation to the field

Three things no other ingested source provides:

1. **A generation-to-test ratio stated outright.** 60,000 designs generated per target, 15 tested — a **4,000:1** ratio. Every success rate in the binder literature is a rate *after* a filter of roughly this severity, and this paper makes the magnitude explicit. See [[de-novo-binder-design]] §10 and §12.
2. **Performance against structurally unprecedented targets,** under a >30%-identity-in-bound-context exclusion. The 66% figure is the wiki's only evidence about generalization as opposed to interpolation, and it is the number the chapter's novelty discussion rests on.
3. **A modality sweep in one model** — nanobodies, miniproteins, linear and cyclized peptides, small molecules, disordered regions — which is what makes "universal" an empirical claim rather than a slogan. The affinity gradient across those modalities is itself informative: nanomolar for protein targets, micromolar for peptides and small molecules.

**Relation to this project.** BoltzGen appears in [[ruijgrok-2026-binder-pipeline-comparison]] as an **evaluation-only delivery**: 100 complexes scored but not generated locally, with the generated pool withheld. That report finds the delivered coordinates are a **Boltz-2 refold rather than a generated structure** (differing from the `before_refolding/` copy by 0.68–1.27 Å binder Cα, with B-factor × 100 recovering per-residue pLDDT), and declares the project's Boltz-2 scoring tier **circular for that arm** because Boltz-2 is a component of BoltzGen's own pipeline — so AlphaFold2 is used as the primary binding tier instead. Read together, the paper's own ranking-flaw experiment and the project's circularity finding make the same point from opposite directions: the scorer inside the pipeline cannot also be the independent judge of it.

## Connections

- The modality and target-class successor to [[butcher-2025-rfdiffusion3]]'s all-atom unification; both design protein, nucleic-acid and small-molecule interfaces, and the chapter treats them as one lineage.
- Shares the unify-prediction-and-design thesis with [[didi-2026-complexa-scaling]] and [[cho-2025-protein-hunter]], by three different mechanisms.
- Its disordered-target campaign extends the flexible-target problem opened by [[vasquez-torres-2023-helical-peptide-binders]] past peptides to intrinsically disordered regions.
- Its benchmark targets (PD-L1, IL-7Rα) overlap [[watson-2023-rfdiffusion]] and [[gainza-2023-surface-fingerprint-binders]] — one of the chapter's few cross-method comparison opportunities.
- Its novelty control is methodologically the counterpart of the strict TM-score splits in [[gainza-2020-masif-supp]].
- Operated as an evaluation-only arm in [[ruijgrok-2026-binder-pipeline-comparison]]; tool page [[boltzgen]].
- Concept [[binder-design]]; chapter [[de-novo-binder-design]].
