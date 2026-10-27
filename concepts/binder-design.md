---
type: concept
tags: [binder-design, de-novo, therapeutics, diagnostics]
sources: 29
updated: 2026-10-21
---

# Binder design

De novo design of a protein that binds a chosen target with high affinity and specificity, starting from the target's structure — or, latterly, its sequence alone — rather than from immunization or library selection ([[bennett-2023-binder-design-dl]], [[watson-2023-rfdiffusion]]).

**Promoted 2026-10-12.** This page is now the short lookup entry; the full treatment is the chapter [[de-novo-binder-design]], which covers the biophysics of interfaces and hot spots, the four methodological lineages, the oracle and its failure modes, the compute and search axis, and the comparability of success rates.

**The lineages, in one line each.**

1. **Grafting** — transplant a binding mode that already exists and scaffold it ([[wang-2022-functional-site-scaffolding]]); see [[motif-scaffolding]]. Still the highest-affinity route when a natural mode is available: scaffolding the p53 helix against MDM2 gave 0.5 and 0.7 nM binders against a 600 nM native interaction ([[watson-2023-rfdiffusion]]).
2. **Filter-first** — keep the pipeline, add a structure predictor in front of the ordering decision. Monomer pLDDT plus interface pAE raised experimental success roughly tenfold with the generator unchanged ([[bennett-2023-binder-design-dl]], [[bennett-2023-binder-design-dl-supp]]).
3. **Hotspot-conditioned generation** — diffuse a binder backbone against named target residues ([[watson-2023-rfdiffusion]]), then all-atom and ligand-conditioned ([[krishna-2024-rosettafold-all-atom]], [[butcher-2025-rfdiffusion3]]), then modality-specified ([[stark-2025-boltzgen]]), then **antibody-format** with a fixed framework supplied global-frame-invariantly so the rigid-body placement is designed ([[bennett-2026-de-novo-antibodies]]).
4. **Surface fingerprints** — the independent lineage: match learned descriptors of molecular surfaces to find a complementary binding seed, then graft it ([[gainza-2020-masif]], [[gainza-2023-surface-fingerprint-binders]]).

Hallucination, which optimises a sequence against a predictor's confidence, is treated in the chapter as the inference-time half of lineage 3 rather than a fifth family, following [[didi-2026-complexa-scaling]] and [[cho-2025-protein-hunter]]. [[lin-2026-genie3]] complicates that: a pure generative model with no oracle optimisation in the loop beats the hallucination state of the art on 7 of 10 benchmark problems, and by a wider margin once runtime is normalised.

**What the designer still supplies.** The epitope. Every method in the chapter takes hotspot residues as input, and the physical reason that is a coherent instruction is that interface binding energy concentrates in densely packed regions — occupied volume around a residue correlates with its alanine-scanning ΔΔG at r² = 0.94 ([[halperin-2004-interface-hot-spots]]).

**The standing caution.** Reported success rates across this literature are fractions of different denominators measured by different assays against different bars — a yeast-display SC50 < 4 µM hit rate ([[bennett-2023-binder-design-dl-supp]]), a single-point BLI response at 10 µM ([[watson-2023-rfdiffusion]]), nanomolar by SPR from 15 designs out of 60,000 generated ([[stark-2025-boltzgen]]), an AlphaFold2 self-consistency pass rate ([[didi-2026-complexa-scaling]]) — and they should not be placed side by side. The nearest thing to a sound comparison is the five-method, one-protocol, fixed-budget benchmark in [[lin-2026-genie3]], which is *in silico* and whose own oracle tops out at 12% precision. [[ruijgrok-2026-binder-pipeline-comparison]] documents the same problem within a single project and six pipelines.

**Sources:** see §15 of [[de-novo-binder-design]] for the full annotated list.
