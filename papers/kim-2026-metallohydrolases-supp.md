---
type: source-supp
parent: "[[kim-2026-metallohydrolases]]"
title: Computational design of metallohydrolases — Supplementary information
pdf: "../sources/ProteinDesign/KimBaker_Nature_2026_Computational design of metallohydrolases_Supp.pdf"
tags: [enzyme-design, metalloenzyme, filtering, PLACER, methods, theozyme, benchmarks]
ingested: 2026-10-21
---

# Computational design of metallohydrolases — Supplementary information (companion)

86-page companion to [[kim-2026-metallohydrolases]]. It is unusually useful because its Extended Discussion is written explicitly as **guidance for building better filters**, not just as a record.

## What the SI contains (map)

- **§1 Nomenclature.**
- **§2 Extended Discussion**, split by campaign (2.1 and 2.2), with a stated purpose: detailed analyses of design models and computational metrics "should guide future strategies for metallohydrolase design, while the computational metric patterns provide valuable insights for **developing effective filters to enrich and select for active designs**", including the authors' hypotheses on why the top performers excelled in each campaign.
- **§3 General materials**, **§4 Methods** — computational design (§4.1), **what changed in the second campaign (§4.2)**, and experimental biology and biochemistry (§4.3).
- **§5 Supplemental Figures**, including: a detailed flow chart of the design and experimental pipeline (Fig. S1); **theozyme input generation for RFdiffusion2 and "the challenge of enumerative catalytic motif scaffolding"** (Fig. S2); the structural panel of all **96 ordered designs spanning 96 unique backbones** (Fig. S3); SDS–PAGE for all 96 (Fig. S4); the initial activity screen (Fig. S5); ESI-MS for ZETA_1 (Fig. S7); the **total-turnover lower-bound experiment** behind the 1,000-turnover claim (Fig. S8); **in silico metric distributions for the ordered designs** (Fig. S9); **a direct comparison of AlphaFold2 metrics against PLACER and Chai-1 metrics** (Fig. S10); the **ZETA_1-versus-other-sequences-on-the-same-backbone comparison** (Fig. S11); and knockout kinetics with the proposed role of N17 (Figs. S12–S13).

## Key extracted details

**Fig. S10 is the one to cite on oracle choice.** It compares AlphaFold2 metrics against PLACER metrics against Chai-1 metrics for the same ordered designs — i.e. it asks directly which filter carries the signal. The main text's claim that global structure prediction plus active-site PLACER modelling together make a powerful selection approach rests on this comparison, and it is the enzyme-design counterpart of the ROC analysis in [[bennett-2023-binder-design-dl-supp]].

**Fig. S11 isolates sequence from backbone.** Comparing ZETA_1 against the other sequences identified for *that same backbone* during design separates "this backbone is good" from "this sequence on it is good" — the control that makes the retrospective seven-design PLACER test in the main text interpretable.

**Fig. S2 names the problem RFD2 solves.** "The challenge of enumerative catalytic motif scaffolding" is the inverse-rotamer and sequence-index enumeration that [[ahern-2025-rfdiffusion2]] was built to eliminate; having it drawn out alongside the theozyme input is the clearest illustration in either paper of why the unindexed atomic motif representation matters.

**§4.2 documents the campaign-to-campaign change** — the second round's theozymes contained the catalytic base with Zn(II) coordinated through His Nε and Cβ explicitly modelled — so the round-1 to round-2 jump from 16,000 to 53,000 M⁻¹ s⁻¹ can be attributed to a specific theozyme revision rather than to generic iteration.

**96 designs span 96 unique backbones** (Fig. S3), which is worth noting against campaigns where multiple designs share a scaffold: here the denominator is 96 independent attempts, so the 5-hit round-1 rate is not inflated by backbone replication.

## Connections

- Parent: [[kim-2026-metallohydrolases]]; method paper [[ahern-2025-rfdiffusion2]] (+ [[ahern-2025-rfdiffusion2-supp]]).
- Its filter-comparison figure (S10) parallels the per-state threshold tables in [[chen-2026-metalloproteases-supp]] and the metric-discrimination analysis in [[bennett-2023-binder-design-dl-supp]].
- Chapter: [[enzyme-design]] §5, §6.
