---
type: source
title: Exploring the repeat protein universe through computational protein design
authors: Brunette, Parmeggiani, Huang et al. (Baker lab)
venue: Nature 2015
pdf: "../sources/Proteins/Brunette_Baker_Nature_2015_v528_p580_Exploring_the_repeat_protein_universe_through_computational_protein_design.pdf"
supp: missing-requested
tags: [repeat-proteins, parametric-design, helical-symmetry, rosetta, de-novo, historical]
ingested: 2026-08-24
---

# Exploring the repeat protein universe

Designs **83 de novo repeat proteins** from a single helix–loop–helix–loop motif and shows that natural repeat proteins occupy only a small fraction of the structures the fold can support.

**Problem.** A central question in protein evolution is how much of the accessible folded-structure space natural proteins actually sample. Repeat proteins — multiple tandem copies of a modular structural unit — are widespread, important in molecular recognition and signalling, and have been re-engineered for recognition and modular scaffolding. But all designed repeat protein structures to that point had been **based on naturally occurring repeat proteins**. The question was whether the fold class is intrinsically limited or whether nature has simply not explored it.

**Approach.** Entirely de novo, with no natural template. A helix–loop repeat unit yields only straight rods, so the work uses the **helix–loop–helix–loop** unit, from which a wide diversity of curvatures is reachable. Helix lengths were varied from **10 to 28 residues** and turn lengths from **1 to 4**, giving **5,776 (19 × 19 × 4 × 4)** independent combinations; four tandem repeats of each were built with ideal helical torsions for helices and extended values for loops. Rosetta Monte Carlo fragment assembly then compacted the structures, **with each move made at the equivalent position in every repeat to preserve symmetry**, and Rosetta design assigned sequences, again applying **identical substitutions in each unit** to maintain sequence identity between repeats. Exposed hydrophobics in the terminal repeats were switched to polar residues in a second round to improve solubility. Candidates were screened by Rosetta de novo folding from an extended chain, keeping designs whose model was much lower in energy than any alternative sampled. The whole process ran without manual intervention.

**The geometric insight.** Because the rigid-body transform relating adjacent repeat units is **identical throughout each design by construction**, and repeated application of one rigid-body transform generates a helical array, every design is **globally helical**. Architectures are therefore classified by three helical parameters: radius *r*, twist between adjacent repeats *ω*, and translation along the axis *z*. These are coupled — the arc length spanned by a repeat is ≈ *rω* and the unit length ≈ √((*rω*)² + *z*²) — so the radius–twist distribution is **hyperbolic**, with highly twisted structures having smaller radii. High-*r*/high-*ω* models fail to form a continuous core and are discarded; *z* above ~16 Å prevents adjacent helices from packing.

**Key results.**

- **761 designed helical repeat proteins (DHRs)** passed all in silico filters; **83** were experimentally characterized.
- **53 are monomeric and stable at 95 °C.**
- **43** have solution X-ray scattering (SAXS) spectra consistent with the design models.
- **Crystal structures of 15 designs**, spanning a broad range of curvatures, agree with the models at **0.7 to 2.5 Å RMSD**.
- Conclusion: existing repeat proteins occupy **only a small fraction** of the possible repeat-protein sequence and structure space.

**Significance.** This is the wiki's anchor for [[repeat-protein-design]] and an important second instance of the [[parametric-design]] logic. It is *not* Crick-equation parametric design in the sense of [[huang-2014-parametric-helical-bundles]] — the backbone comes from fragment assembly, not a closed-form generator — but it shares the essential move: **impose the symmetry on the search rather than discover it**, by making every Monte Carlo move and every sequence substitution at equivalent positions in all repeats. The three-parameter (*r*, *ω*, *z*) classification that falls out is the same kind of low-dimensional description of a repeating structure that the Crick parameters provide for coiled coils. The DHR library it produced became a standard component set: the axles and rotors of [[courbet-2022-axle-rotor-assemblies]] are built from designed helical repeat proteins.

**Connections.**

- Supplies the DHR building blocks used in [[courbet-2022-axle-rotor-assemblies]].
- Methodological sibling of [[huang-2014-parametric-helical-bundles]] — same lab, same year-adjacent period, symmetry imposed on the search in both, but fragment assembly rather than closed-form parametric generation.
- Relevant to [[wicky-2022-symmetric-assembly-design]], whose giant hallucinated rings have protomers with LRR-like (repeat-protein) topology.
- Concepts: [[repeat-protein-design]], [[parametric-design]], [[symmetric-assembly-design]].
- **Supplement:** not present in `sources/` — the *Nature* Extended Data and Methods hold the filtering criteria and the full DHR table.
