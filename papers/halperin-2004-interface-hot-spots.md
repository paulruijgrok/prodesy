---
type: source
title: "Protein-Protein Interactions: Coupling of Structurally Conserved Residues and of Hot Spots across Interfaces. Implications for Docking"
authors: Halperin, Wolfson & Nussinov
venue: Structure 2004 (12, 1027–1038)
pdf: "../sources/Proteins/Halperin_Nussinov_Structure_2004_Protein-Protein Interactions- Coupling of Structurally Conserved Residues and of Hot Spots across Interfaces. Implications for Docking.pdf"
supp: missing-requested
tags: [interfaces, hot-spots, biophysics, packing, conservation, docking, foundations]
ingested: 2026-10-12
---

# Coupling of structurally conserved residues and of hot spots across interfaces

The wiki's foundation page for **binding hot spots** — what they are, how they are defined operationally, and the physical property that distinguishes them from the rest of an interface.

**Why it matters here.** "Hotspot conditioning" is the mechanism by which every modern binder-design method is told where to bind ([[watson-2023-rfdiffusion]], [[ruijgrok-2026-binder-pipeline-comparison]]), and until this source was ingested the term was *used* on four wiki pages and **defined on none**.

**Problem.** A priori prediction of binding sites and of protein–protein interactions. Binding sites had been characterized by size, shape, hydrophobicity, electrostatics and residue composition, and were known to be relatively well conserved evolutionarily — but both the conservation analyses and the hot-spot analyses had been performed **on one side of the interface only**. Coupling *across* an interface had never been shown systematically, for want of data.

**Approach.** Two datasets, newly large enough for the question. (1) A structurally non-redundant set of protein–protein interfaces, grown from 1,629 interfaces / 351 clusters in 1996 to **21,686 interfaces / 3,799 clusters**, used to find *structurally conserved* residues. (2) The **Alanine Scanning Energetics database (ASEdb)**, screened for pairs of proteins where both partners were alanine-scanned, each contained at least one hot spot, and the pair had been crystallized as a complex — yielding **8 complexes, 429 alanine mutations and 53 hot spots**. Observed coupling counts are compared against two null models: Model 1 (random distribution) and Model 2 (which additionally conditions on the number of cross-interface neighbours).

**The operational definition.** A **hot spot is a residue whose mutation to alanine causes a significant drop in binding affinity**, measured as the change in free energy of binding (ΔΔG). The threshold used here is **≥ 1.9 kcal/mol**.

## Key results

**Hot spots are more densely packed than the rest of the interface, and the packing tracks the energetics.**

- Hot spots have on average **4.2 neighbours across the interface**; non-hot-spot interface residues have **2.3**. The difference is significant at p = 0.01, a distance of 2.9 SD units (53 hot spots vs 551 non-hot-spot interface residues).
- Occupied volume in the vicinity of a residue: **69.2 Å³ (SD 42.5) around hot spots** versus **38.1 Å³ (SD 17.1) around non-hot spots**, significant at the 0.99 confidence level.
- **Occupied volume correlates with ΔΔG at r² = 0.94** — the single most useful number on this page, because it converts "hot spot" from a mutagenesis label into a geometric property a design method could in principle optimize.
- The effect is **not** a residue-size artefact: correlation between amino-acid volume and hot-spot propensity is r² = 0.01, and between number of neighbours and residue volume r² = 0.03.

**Hot spots and conserved residues couple across the interface.** Both occur in cross-interface contact more often than random distribution predicts, and the trends are *stronger* for experimental hot spots than for structurally conserved residues. Expected hot-spot couples average 2.6 (SD 4.0) under Model 1 and 5.4 (SD 6.0) under Model 2, so the elevated neighbour count accounts for a relatively large part of the observed coupling.

**Composition preferences.** Among conserved couples: strong Cys–Cys conservation; **glycine** preferentially couples with aromatics, polar and charged residues and with small hydrophobics (Ala, Val) but is disfavoured next to larger ones (Met, Pro, Leu, Ile) — read by the authors as glycine's lack of a side chain letting it pack tightly while its backbone hydrogen-bonds across the interface; aromatic–aromatic and hydrophobic–hydrophobic couplings are preferred, though not involving Ile or Leu. **Charged–charged couples are underrepresented**, and polar–polar less so.

**The synthesizing claim.** "Overall, protein-protein interactions appear to consist of regions of high and low packing density, with the hot spots organized in the former. The high local packing density in binding interfaces is reminiscent of protein cores." An interface is therefore not uniform: it has a core-like dense region carrying the energetics and a looser periphery.

**Application.** Using conserved-residue couples or hot-spot couples as interest-point constraints noticeably improved **PatchDock** docking results on two test cases.

## Significance / relation to the field

This page supplies three things the binder chapter cannot otherwise source:

1. **The definition and the threshold.** A hot spot is an alanine-scanning ΔΔG ≥ 1.9 kcal/mol residue, not an informal "important residue".
2. **The physical reason hotspot conditioning is a sensible instruction.** If packing density around a residue correlates with its ΔΔG at r² = 0.94, then telling a generative model to contact specified residues is telling it to build into the part of the surface where binding energy is concentrated. It also explains why *soft* hotspot conditioning can still work: the model is being pointed at a region, and the region is physically distinctive.
3. **Why affinity and specificity are different axes.** The composition result — charged–charged couples underrepresented, aromatics and glycine favoured — is about *which* chemistry appears at a dense interface core, and is the natural counterpart to the buried-polar-satisfaction argument in [[boyken-2016-hydrogen-bond-network-oligomers]].

**Caveat the chapter must carry.** The hot-spot dataset is **8 complexes and 53 hot spots**. These are robust effects on a small sample, and the "O-ring" picture of hot spots occluded from solvent, which this paper cites to Bogan & Thorn, is **not** ingested primarily — see the flagged references in [[de-novo-binder-design]].

**Supplement:** `supp: missing-requested`. The Supplemental Data holds Table A (interface cluster representatives), Table B (the 8 alanine-scanned complexes) and Appendices C–D (the per-residue hot-spot and non-hot-spot neighbour and volume data). Without it the identity of the 8 complexes cannot be stated.

## Connections

- The missing foundation of the hotspot conditioning in [[watson-2023-rfdiffusion]] and [[watson-2023-rfdiffusion-supp]]; of the atom-level hotspot specification recorded for RFD3 in [[ruijgrok-2026-binder-pipeline-comparison]]; and of the MaSIF-placed hotspot residues validated by site-saturation mutagenesis in [[gainza-2023-surface-fingerprint-binders]].
- Complements [[boyken-2016-hydrogen-bond-network-oligomers]] on buried polar satisfaction; together they are the chapter's biophysics section.
- The docking application connects to `ProteinDesign/SchneiderDuhovnik_NAR_2005_PatchDock and SymmDock…` (in `sources/`, un-ingested), which would give PatchDock a primary citation.
- Chapter: [[de-novo-binder-design]] §2.
