---
type: concept
tags: [repeat-proteins, helical-symmetry, parametric-design, de-novo]
sources: 4
updated: 2026-08-24
---

# Repeat protein design

Designing proteins built from **multiple tandem copies of one modular structural unit**. The repeat is the design object; the overall shape is whatever repeated application of a single rigid-body transform produces.

**Why the fold class matters.** Repeat proteins are widespread in nature and carry out molecular recognition, signalling and other essential functions; natural ones have been re-engineered as recognition and scaffolding platforms ([[brunette-2015-repeat-protein-universe]]). Coiled coils are themselves a repeat class, and account for an estimated **3–5% of all known protein-encoding regions of DNA** ([[wood-2018-ccbuilder]]).

**Repetition implies global helical symmetry.** If the rigid-body transform relating adjacent units is identical throughout — which it is, by construction, in a designed repeat protein — then repeated application of that transform generates a **helical array**. Every such design is therefore globally helical and can be classified by three coupled parameters: radius *r*, twist between adjacent repeats *ω*, and axial translation *z*. The coupling is geometric: a repeat spans arc length ≈ *rω* and has total unit length ≈ √((*rω*)² + *z*²), so the radius–twist distribution is hyperbolic, with highly twisted structures having smaller radii ([[brunette-2015-repeat-protein-universe]]).

**Symmetry is imposed on the search, not discovered.** In [[brunette-2015-repeat-protein-universe]] every Rosetta Monte Carlo move is made at the equivalent position in each repeat, and every sequence substitution is applied identically across units. This is the same move that defines [[parametric-design]] — reduce the search to one unit and let symmetry replicate it — implemented through fragment assembly rather than a closed-form generator.

**Nature has barely explored the space.** From a single helix–loop–helix–loop unit with helix lengths 10–28 and turn lengths 1–4 (5,776 combinations), 761 designs passed in silico filters and 83 were tested: **53 monomeric and stable at 95 °C**, 43 SAXS-consistent, and **15 crystal structures at 0.7–2.5 Å RMSD** across a broad range of curvatures. The conclusion is that existing repeat proteins occupy only a small fraction of the accessible sequence and structure space ([[brunette-2015-repeat-protein-universe]]).

**Why this matters downstream.** The resulting designed helical repeat proteins (DHRs) became a standard component library — the cyclic rotors and dihedral axles of [[courbet-2022-axle-rotor-assemblies]] are built by fusing DHRs. And repeat topology recurs on the generative side: the giant hallucinated rings of [[wicky-2022-symmetric-assembly-design]] have protomers with LRR-like repeat topology, though their closed cyclic assemblies differ considerably from the open horseshoe folds of natural leucine-rich repeats.

**Boundary with [[symmetric-assembly-design]].** Repeat proteins have *helical* symmetry within a single chain; symmetric assemblies have *point-group* symmetry across several chains. The two meet when a repeat protein closes into a ring — which is what makes DHRs natural building blocks for C*n* components.

**Sources:** [[brunette-2015-repeat-protein-universe]], [[wood-2018-ccbuilder]], [[courbet-2022-axle-rotor-assemblies]], [[wicky-2022-symmetric-assembly-design]].
