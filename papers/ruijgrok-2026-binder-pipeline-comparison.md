---
type: source
title: "Binder design pipelines — a comparison of computational approaches"
authors: Ruijgrok (dx_binder_design project, internal report)
venue: Internal technical report, 2026-10-12
pdf: "../sources/BinderDesignComparison/reports/pipeline_comparison.pdf"
supp: no
tags: [binder-design, pipelines, compute, benchmarks, comparability, engineering, first-party]
ingested: 2026-10-12
---

# Binder design pipelines — a comparison of computational approaches

A first-party, machine-generated comparison of nine binder-design pipelines as operated in the `dx_binder_design` project, covering generative formulation, atomic representation, target and epitope conditioning, test-time search, scoring, measured compute, and — its distinctive contribution — a **comparability ledger** stating for each pipeline why its headline pass rate cannot be placed beside another's.

**Status note.** This is an internal engineering report, not peer-reviewed literature. It is citable under the `CLAUDE.md` standard because it carries a per-claim `source` column pointing at the config or source file each statement was read from, and because every compute figure is derived from Slurm accounting rather than copied from a journal. Its claims are about *this project's pipelines*, not about the field; the distinction is maintained wherever this page is cited.

**Problem.** Nine pipelines were stood up or evaluated against the same target class (*Plasmodium falciparum* LDH and a benchmark set), and their reported pass rates are not comparable — because each rate is a fraction of a different denominator. The report refuses to rank them and instead documents the *reasons* comparison fails.

**Approach.** A TSV-backed database (`pipelines.tsv`, `schema.tsv` with 39 questions, `attributes.tsv` with 218 answers, `stages.tsv` with 43 stage rows) rendered to Markdown and PDF by `build_pipeline_comparison.py`; compute harvested from `sacct` by `harvest_compute.py` over the project's whole history. Unanswered schema fields are printed as *not established* rather than dropped, and counted in a coverage section.

## Key results

**The three pipeline kinds.** Four **generative** pipelines sampled locally (Protpardelle-1c, Proteína-Complexa, ProteinHunter, RFdiffusion3); two **evaluation-only** deliveries scored but not generated here (DiffuseBio — a vendor whose method is undisclosed; BoltzGen); three **planned** comparators not yet stood up (RFdiffusion, BindCraft, Chroma), carried explicitly so the coverage gaps are visible at 27% answered.

**Measured compute, whole project.** 21,707 Slurm tasks; **10,376.1 total GPU-hours** (7,418.0 generation, 2,956.8 scoring) and 127,987.1 CPU-hours. Per pipeline: Complexa 8,587.2 GPU-h over 11,810 tasks, Protpardelle 1,229.7 over 8,544, ProteinHunter 510.2 over 1,255, RFD3 14.3 over 45. **303.7 GPU-hours were charged to failed tasks** (OOMs, timeouts, cancellations) — reported because it is large enough to matter in planning.

**Cost per design** (median task walltime × GPUs, at one design per task for all four): Protpardelle 8.40 GPU-min, ProteinHunter 15.40, RFD3 20.00, Complexa 54.60. The report is explicit that this is the cost of producing a *candidate*, not a usable one.

**Atomic representation as a first-class axis.** Each pipeline's stages are tabulated by what they can see — all-atom, backbone, CA-only, sequence-only — on the argument that "a stage that sees only backbone cannot evaluate packing, and a stage that rebuilds sidechains is making them up from a sequence rather than observing them," and that reading a packing number off a backbone-only stage is the most common way to over-read a result. Stage counts: Protpardelle 8 stages (6 all-atom), Complexa 6 (2 all-atom, 1 CA-only, 1 mixed), ProteinHunter 8 (5 all-atom), RFD3 6 (4 all-atom), DiffuseBio 8 (7), BoltzGen 7 (6). Two exceptions are named exhaustively:
- **Complexa / `evaluate_af2`** — `<name>_updated.pdb` is CA-only, and it is the file `get_interface_residues()` reads, so **every contact and interface-residue count in the Complexa record is CA-only** while SolubleMPNN receives the all-atom file.
- **RFD3 / `mpnn_redesign`** — the generator's own co-designed sequence is **discarded** here, because ProteinMPNN is backbone-only by construction.

**Conditioning mechanisms differ more than the method families suggest.** Protpardelle pins the target as a *motif to scaffold* (contig `A1-316;/;B1-316;/;60-120`) with a `ca_motif_sample_rmsd` placement diagnostic (~0.030 Å on working runs); Complexa supplies the target as *context* with `binder_gen_only: True` and **re-generates rather than copies** the target chains, which is the origin of an antigen-copying defect; ProteinHunter supplies **no target structure at all** — sequence plus MSA only, with the target conformation re-predicted every cycle; RFD3 uses **atom-level** hotspots mapping each residue to specific sidechain atoms (e.g. `{"A13": "SD,CE"}`). Hotspot conditioning is soft guidance, not a constraint, in all four. Protpardelle's `binder_sse_prop` (a global [helix, strand, loop] proportion quantised to 0.1) is recorded as the project's one confirmed fold lever, with no counterpart in any other pipeline.

**Test-time search is the thesis of one pipeline and absent from another.** Complexa runs verifier-guided beam search in production (n_branch 4, beam_width 8, 5 step checkpoints, AlphaFold2-multimer i_pAE as reward with every other reward term zeroed); ProteinHunter's 7-cycle greedy hill-climb on ipTM *is* the method; Protpardelle scales by embarrassingly parallel replication up to 2,048 independent draws — and **tripling n on the h80 recipe added zero new folds**; RFD3 has no search machinery at all.

**The comparability ledger** — the report's core. Each pipeline's denominator is named, and the reason it cannot sit beside another's:
- **Protpardelle** — denominator is designs generated, the cleanest here, with no pre-scoring gate; but the metric (complex-level scRMSD from the model's own sequence) asks "is this self-consistent", not "does it bind".
- **Complexa** — denominator is finalists surviving `filter`, capped by `filter_samples_limit: 1000`, so campaigns at n=16 and n=512 have incomparable denominators; and the rate is computed on MPNN-redesigned sequences, measuring the redesign pathway rather than the generator.
- **ProteinHunter** — denominator is designs *promoted* by a generation-stage gate; **79% of 4b7u tasks are lost before any validation runs**, and lowering the gate from 0.8 to 0.7 moved promotion from 14.1% to 43.8% on byte-matched generation, meaning the old gate was discarding on-epitope designs.
- **RFD3** — clean denominator at n=64, but a different target set (only the five Table S6 benchmark targets, never a scored PfLDH campaign).
- **DiffuseBio and BoltzGen** — pass rate is **banned by preregistration**: both deliveries are post-filter selections with the pool withheld, so any rate would describe the vendor's or the generator's own selection rule. Comparison is made instead as *paired deltas* within each design across two target contexts, which is immune to selection because each design is its own control.

**Known invalidities, stated rather than buried.** Complexa's placement and pass/fail are measured on *different structures* and agree at chance (Cohen's κ +0.006 and −0.091), and the AF2 gate **depletes** epitope contact rather than enriching it; antigen copying affects the co-designed `self` sequence (48 contiguous target residues in a 79-mer, ρ +0.54 with reward). RFD3's 0/64 on three of five benchmark targets is **unmeasurable rather than undesignable**, because ESMFold cannot rebuild those targets (median target_pred_rmsd 2.18, 9.54, 17.68 Å), and those rows carry binder-only scRMSD at 84–94% instead. BoltzGen's tier-2 Boltz-2 metric is **declared circular** because Boltz-2 is a component of BoltzGen's own pipeline — "a BG advantage here is not evidence; a BG deficit would be" — so AlphaFold2, sharing no weights, is the primary binding tier for that arm. Several BoltzGen axes are inflated because `rank000NN` is BoltzGen's own weighted rank.

**Engineering failure modes** are recorded per pipeline: silent degradation (Complexa's JAX preallocation failure drops AF2 reward to 0.0000 for a whole run and still exits 0); GPU OOM surfacing as a `KeyError` in ProteinHunter; RFD3 writing non-standard PDBx `_atom_site` column order; four — then five — incompatible residue-numbering frames across the project, with the trap having fired twice. Chain conventions are inverted between pipelines (ProteinHunter and RFD3 put the binder first).

## Significance / relation to the field

Three contributions this wiki has no published source for:

1. **It operationalises the incommensurability of binder success rates.** Where [[watson-2023-rfdiffusion]] quotes 19% by BLI and [[bennett-2023-binder-design-dl]] quotes a ~10× improvement against a yeast-display SC50 < 4 µM bar, this report shows that even *within one project, on one target*, six pipelines' rates are fractions of six different denominators — and documents what would have to be held fixed to make a fair comparison. See [[de-novo-binder-design]].
2. **It treats atomic representation per pipeline stage as a measurable property.** No ingested published source audits which stages of a design pipeline can actually see sidechains; this one does, and finds two places where interface numbers are being read off CA-only or backbone-only stages.
3. **It supplies measured compute for the test-time-scaling argument** that [[didi-2026-complexa-scaling]] makes theoretically — and from the same codebase, since the "Complexa" pipeline here *is* Proteína-Complexa.

**A direct contradiction with the published literature, worth stating plainly.** [[didi-2026-complexa-scaling]] reports that Complexa's self-generated sequences outperform all baselines including ProteinMPNN re-design, concluding that "such additional steps [are] unnecessary". This report finds the opposite in operation: the project's headline Complexa metric is computed on `mpnn_fixed` redesigns precisely *because* the co-designed `self` sequence carries an antigen-copying defect severe enough that it cannot be substituted (48 contiguous target residues copied into a 79-mer binder, correlating with the reward at ρ +0.54). The two claims are about the same model. The wiki's reading is that this is the clearest available illustration of the gap between an in-silico benchmark and an operated pipeline, and it is treated as such in [[de-novo-binder-design]] rather than resolved.

A second, smaller tension: [[didi-2026-complexa-scaling]]'s Table 2 states that "RFDiffusion and Protpardelle only generate backbones and not their own sequences", while this report records RFD3's output as *observed* all-atom at 6.4 atoms/residue with a low-entropy co-designed sequence — and notes that RFD3's own `qc_outputs.py` comments describe the same output as "backbone-only diffusion output". The discrepancy is unresolved in the report and listed there as an open question.

## Connections

- The pipelines it compares: [[protpardelle]], [[chroma]], [[rfdiffusion]], [[rfdiffusion3]], [[bindcraft]], [[boltzgen]], [[proteinhunter]], [[complexa]].
- The published counterparts of four of them: [[didi-2026-complexa-scaling]] (Complexa), [[butcher-2025-rfdiffusion3]] (RFD3), [[chu-2024-protpardelle]] (Protpardelle), [[cho-2025-protein-hunter]] (ProteinHunter), [[stark-2025-boltzgen]] (BoltzGen).
- The scoring oracles it audits: [[jumper-2021-alphafold2]], [[abramson-2024-alphafold3]], [[dauparas-2022-proteinmpnn]].
- Chapter: [[de-novo-binder-design]] §2, §10, §11 and §12 all rest on this page.
- Contradicts [[didi-2026-complexa-scaling]] on the value of MPNN redesign (see above).
