---
type: source-supp
parent: "[[choi-2026-cysteine-proteases]]"
title: De novo design of cysteine proteases — Supplementary information
pdf: "../sources/ProteinDesign/ChoiBaker_Nature_2026_De novo design of cysteine proteases_Supp.pdf"
tags: [enzyme-design, protease, crystallography, kinetics, foldseek, methods]
ingested: 2026-10-21
---

# De novo design of cysteine proteases — Supplementary information (companion)

Short companion (13 pages) to [[choi-2026-cysteine-proteases]], carrying the comparison data the main text's claims rest on rather than additional method description.

## What the SI contains (map)

- **Supplementary Table 2** — LC–MS data, the evidence that all 13 active designs cleave precisely at the intended target site.
- **Supplementary Table 3** — crystallography data collection and refinement statistics for the six structures.
- **Supplementary Table 4** — **Foldseek analysis for the crystal structures**, the basis for the main text's claim that the designed folds differ from natural proteases at TM-score < 0.50. This is structural-novelty evidence computed on the *experimental* structures rather than the design models, which is the stronger form of the claim.
- **Supplementary Table 5** — **kinetics summary of sequence-specific cysteine proteases**: the native benchmark set (Ulp1, Mpro, TEV, HRV3C) against which Dokki-v2's k_cat is said to fall "approximately one to two orders of magnitude below the most active native enzymes".
- **Supplementary Fig. 2** — **gel-based kinetic analysis of Ulp1 cleavage activity**, the control that makes the design-versus-native comparison fair: Ulp1 measured on peptide substrates lacking the SUMO domain, since Ulp1 natively uses a large folded-domain interface to position its substrate and the designs have no equivalent.
- **Supplementary Fig. 1 and 3** — full SDS–PAGE gel images and the raw cell-based reporter assay images.
- **Supplementary information 1 and 2** — pCool6 and ZJ101 plasmid DNA sequences.

## Key extracted details

- The novelty claim is **experimentally grounded**: Foldseek is run on the solved structures (Table S4), so "folds very different from proteases in nature" is not a statement about models.
- The **native comparison set is explicit** (Table S5), which is unusual in this literature and is what permits the paper's unusually specific "one to two orders of magnitude" framing rather than a vague gap claim.
- The **Ulp1-without-SUMO control** (Fig. S2) is the methodological heart of the substrate-positioning argument in the parent page's §4: without it, comparing a designed protease acting on a peptide against Ulp1 acting on a folded SUMO domain would confound catalysis with substrate engagement.

## Connections

- Parent: [[choi-2026-cysteine-proteases]].
- Its Foldseek novelty analysis parallels the structural-novelty controls in [[gainza-2020-masif-supp]] and [[lin-2024-genie2]].
- Chapter: [[enzyme-design]] §5 and §8.
