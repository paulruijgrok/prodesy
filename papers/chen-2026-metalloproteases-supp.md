---
type: source-supp
parent: "[[chen-2026-metalloproteases]]"
title: Computational design of metalloproteases — Supplementary information
pdf: "../sources/ProteinDesign/ChenBaker_Nature_2026_Computational design of metalloproteases_Supp.pdf"
tags: [enzyme-design, metalloenzyme, filtering, thresholds, methods, crystallography, qm]
ingested: 2026-10-21
---

# Computational design of metalloproteases — Supplementary information (companion)

94-page methods companion to [[chen-2026-metalloproteases]], and the page to read for **the actual filter thresholds** behind that paper's headline result.

## What the SI contains (map)

- **§1, the computational pipeline**, in eight steps: theozyme generation → **RFD2-MI** → **iterated EnhancedMPNN-constrained relax sequence design** → AF3 modelling of the apo protease → **partial diffusion** → AF3 modelling of the protease–Zn(II)–substrate complex → AF3 modelling of the protease–Zn(II)–**transition-state-analogue** complex → filtering.
- **§2 and §3**, two distinct routes to a TDP-43-targeting protease: **redesign** of an existing de novo metalloprotease (identify starting docks and a substrate window, then partial diffusion with the catalytic motif *and* a polar interface motif held fixed) versus **direct design** by motif scaffolding. The main text notes direct de novo design for the TDP-43 peptide was the harder path.
- **§4, experimental methods** — 13 subsections covering the cis and trans screens, per-residue catalytic knockouts, zinc-binding assessment, cross-reactivity, kinetics, substrate selectivity of TDPn3 and TDPr3, and cleavage of full-length human TDP-43.
- **Supplementary Discussions** — six, including **"Representation of the water molecule in the prediction of the ES complex using the Zn(II)-water strategy"**, which is the methodological heart of the parent paper's filtering result; the theozyme choice; **limitations of the machine-learning force-field QM activation-barrier calculations**; and two negative results (below).
- **Supplementary Figs. S1–S21** and Tables, including gel images for the full cis screen of 135 designs, the trans screen of 40, zinc-binding isotherms, and the ML force-field activation-barrier calculations.

## Key extracted details

**The filter thresholds, stated per modelled state.** All three states must pass, before and after a refinement round:

- **Apo models** — AF3 pLDDT > 86, catalytic-residue side-chain RMSD < 1.5 Å, all-residue Cα RMSD < 1.8 Å.
- **Enzyme–substrate complex** — pLDDT > 92, **mean interface PAE < 5**, **minimum interface PAE < 1.2**, catalytic side-chain RMSD < 1.5 Å, Cα RMSD < 1.8 Å.
- **TSA complex** — pLDDT > 92, mean interface PAE < 5, catalytic side-chain RMSD < 1.5 Å, Cα RMSD < 1.8 Å.

Backbones from RFD2-MI are pre-filtered for **low loop content and ideal geometry**; sequence design runs with **`--omit_AA C`** (cysteine excluded) at temperature 0.1, and earlier rounds use looser bars (pLDDT > 82–85, Cα RMSD < 2 Å).

Note what these thresholds *are*: AF3 confidence and geometry. The main text's finding is that **two design sets passing the same numerical bars had hit rates of 3/89 and 31/38** depending only on whether the catalytic water was present in the modelled complex. The thresholds did not change; what the model was asked to place did.

**Two negative results worth preserving**, both in the Supplementary Discussions:

- **"Introduction of substrate-stabilizing residues by MPNN reduces activity."** Sequence design aimed at better substrate binding made the enzymes *worse* — the enzyme-design counterpart of the binder-design finding that a gate can select against the property it targets.
- **"Predictability of AF3 and MPNN in the mutagenesis space of Zn45-S_ZnO36"** — an explicit assessment of how far the oracle can be trusted for point mutations around a designed active site.

**Limitations are stated for the QM work.** The ML force-field activation barriers that put Zn45 and ZnO7 3.6 and 15.1 kcal mol⁻¹ above native astacin come with their own discussion of limitations, so the chapter cites that gap as indicative rather than definitive.

## Connections

- Parent: [[chen-2026-metalloproteases]].
- Its three-state filtering (apo / ES / TSA) is a stricter discipline than the apo-plus-complex filtering in [[choi-2026-cysteine-proteases]]; the TSA state has no counterpart in the binder literature.
- Partial diffusion as a refinement operator is the same device introduced in [[vasquez-torres-2023-helical-peptide-binders]].
- Chapter: [[enzyme-design]] §5 and §6.
