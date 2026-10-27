---
type: tool
tags: [binder-design, all-atom, modalities, nanobodies, peptides, open-source]
sources: 3
updated: 2026-10-17
---

# BoltzGen

An all-atom generative model for binder design **across modalities and target classes**, unifying design and structure prediction in one network. Introduced in [[stark-2025-boltzgen]]; weights, data, training and inference code released under the MIT License.

**Capabilities.** Protein binders, nanobodies, linear peptides, disulfide-cyclised peptides, antimicrobial peptides; targets spanning folded proteins, bioactive peptides, intrinsically disordered regions, and small molecules. Generation is controlled by a **design specification language** over covalent bonds, structure constraints and binding sites — so a cyclic peptide is requested by declaring a covalent bond and a nanobody by fixing a framework's structure and sequence while replacing its three CDRs with random-length loops, sampled from four default nanobody scaffolds ([[stark-2025-boltzgen]]).

**Headline validation.** Eight wet-lab campaigns over 26 targets. Against nine targets with **no >30%-identity homologue in a bound context anywhere in the PDB**, generating 60,000 candidates per target and testing 15 gave nanomolar binders for **6 of 9 (66%)** for both nanobodies and protein binders; on five benchmark targets with known high-affinity binders, **80%** ([[stark-2025-boltzgen]]).

**Pipeline role.** Self-contained: generation, inverse folding and refolding in one model, with refolding quality and (for small-molecule targets) affinity estimation used for ranking and filtering ([[stark-2025-boltzgen]]). In this project it is used **evaluation-only** — designs delivered, not generated locally ([[ruijgrok-2026-binder-pipeline-comparison]]).

**Two cautions, both load-bearing.**

1. **Its own ranking is what produces hits.** An earlier version "suffered from a serious flaw resulting in close-to-random ranking and filtering", and for designs from that version **no hits were found** — the generator being substantially the same ([[stark-2025-boltzgen]]). Taken with the 4,000:1 generate-to-test ratio, the wiki's reading is that BoltzGen's reported rates are properties of the generator *and* its ranker together, inseparably.
2. **Boltz-2 cannot be used to score it.** Because Boltz-2 is a component of BoltzGen's own pipeline, a Boltz-2 scoring tier reports the generator's objective back to it; [[ruijgrok-2026-binder-pipeline-comparison]] declares that tier **circular** for the BoltzGen arm — "a BG advantage here is not evidence; a BG deficit would be" — and promotes AlphaFold2, which shares no weights or training pipeline, to primary binding tier. That report also finds the delivered coordinates are a **Boltz-2 refold rather than a generated structure** (0.68–1.27 Å binder Cα from the pre-refolding copy, with B-factor × 100 recovering per-residue pLDDT), and that several axes are inflated because the delivery's rank ordering is BoltzGen's own weighted rank.

**Independent evaluation.** [[lin-2026-genie3]] places BoltzGen "substantially" behind Genie 3 and BindCraft on ten AlphaProteo problems at a fixed 200-structure budget, and reports an aggregate hit rate of **2/288** for BoltzGen submissions in the blind AdaptyvBio Nipah competition, against 1/8 for Genie 3 — with the caveat that competition rates reflect diverse procedures by groups of varying expertise.

**Connections.** The modality successor to [[rfdiffusion3]] ([[butcher-2025-rfdiffusion3]]); shares the unify-design-and-prediction thesis with [[complexa]] ([[didi-2026-complexa-scaling]]) and [[proteinhunter]] ([[cho-2025-protein-hunter]]). Overlaps [[rfdiffusion]] and [[masif]] on PD-L1 and IL-7Rα. Concept [[binder-design]]; chapter [[de-novo-binder-design]] §8.3, §10, §12.
