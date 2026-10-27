---
type: source-supp
parent: "[[braun-2026-riff-diff]]"
title: Computational enzyme design by catalytic motif scaffolding — Supplementary information
pdf: "../sources/ProteinDesign/BraunOberdorfer_Nature_2026_Computational enzyme design by catalytic motif scaffolding_Supp.pdf"
tags: [enzyme-design, methods, kinetics, stereoselectivity, molecular-dynamics, crystallography]
ingested: 2026-10-21
---

# Riff-Diff — Supplementary information (companion)

49-page companion to [[braun-2026-riff-diff]], carrying the Supplementary Methods for the pipeline plus the biophysical characterisation the main text summarises.

## What the SI contains (map)

- **Supplementary Methods** — the artificial-motif library generation, the custom auxiliary potential and placeholder-helix implementation, and the iterative backbone refinement cycles.
- **Fig. S1** — computational metrics of the selected RAD models.
- **Fig. S2** — **active-site lysine to alanine knockouts**, the mechanism control for the retro-aldolases.
- **Figs. S3, S4, S9** — CD spectra, dimensionless **Kratky plots** (SAXS-based compactness), and chemical denaturation of the RAD designs.
- **Figs. S5, S7, S13** — Michaelis–Menten kinetics for the RADs, RAD variants, and the MBH designs.
- **Fig. S6, S11** — proposed reaction mechanisms for the RA95.5-8F-catalysed retro-aldol reaction and for the MBH reaction.
- **Fig. S8** — pH profiles of the RADs.
- **Fig. S10** — individual correlations of the computational metrics used for the denaturation model.
- **Fig. S12** — computational metrics for the designed MBHases.
- **Fig. S15** — circular dichroism of MBH48, behind the ~85 °C unfolding onset.
- **Fig. S16** — electron density for the RAD catalytic residues, i.e. the evidence that the modelled catalytic geometry is actually observed.
- **Fig. S17** — **HPLC determination of methodol absolute configuration and enantiomeric excess**, the primary data behind the 99% ee stereoselectivity claim.
- **Fig. S18** — backbone Cα RMSDs across all MD trajectories.
- **Supplementary Tables 5, 7, 8** — comparison tables of catalytic rates for **past designed and evolved retro-aldolases**, per-design MBH conversions, and Michaelis–Menten parameters for previously reported designed and evolved MBH enzymes.

## Key extracted details

**Supplementary Table 5 is the comparison the chapter should cite for context.** It tabulates catalytic rates of past designed *and evolved* retro-aldolases, which is what licenses the main text's claim that these designs are "orders of magnitude faster than previous computationally designed retro-aldolases" and approach RA95.5-5. Equivalent tables exist for the MBH reaction (Table 8). Very few sources in this wiki supply the native/evolved comparison set explicitly — [[choi-2026-cysteine-proteases-supp]] is the other.

**Stereoselectivity has primary data.** Fig. S17's HPLC determination of absolute configuration and enantiomeric excess is the only such measurement in the wiki's enzyme coverage, and it is what distinguishes a designed catalyst from a designed accelerator.

**Electron density for catalytic residues** (Fig. S16) matters because the main text's central mechanistic claim is about sub-1 Å catalytic geometry; density maps rather than refined coordinates are the appropriate evidence for that.

**The denaturation model has its own metric correlations** (Fig. S10), i.e. the authors attempted to predict stability from computational metrics and report the individual correlations rather than only a combined model.

## Connections

- Parent: [[braun-2026-riff-diff]].
- Its explicit native-and-evolved comparison tables parallel [[choi-2026-cysteine-proteases-supp]]'s native-protease kinetics set.
- Chapter: [[enzyme-design]] §5, §8.
