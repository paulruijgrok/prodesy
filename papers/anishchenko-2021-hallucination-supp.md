---
type: source-supp
parent: "[[anishchenko-2021-hallucination]]"
title: De novo protein design by deep network hallucination — Supplementary Information
pdf: "../sources/ProteinDesign/AnischenkoBaker_Nature_2021_De novo protein design by deep network hallucination_supp.pdf"
tags: [hallucination, oligomers, methods, failure-modes, trrosetta]
ingested: 2026-08-14
---

# Hallucination — Supplementary Information (companion)

Companion to [[anishchenko-2021-hallucination]]. A short SI: one table and seven figures. It is unusually load-bearing for its length, because **most of it documents the method's failure modes** rather than its successes — in particular the unintended oligomerization that matters to [[symmetric-oligomer-design]].

## What the SI contains (map)

- **Table 1** — comparison of the three structurally resolved hallucinated proteins (0217, 0515, 0738_mod) against the closest known PDB structures, split into the closest structure *within the training set* and the closest *in the PDB as a whole*, plus the closest sequence.
- **Figure 1** — representative SEC traces from screening the 129 hallucinated sequences chosen for experimental characterization.
- **Figure 2** — experimental analysis of hallucinated protein 0217 (the design that crystallized as a dimer).
- **Figure 3** — **surface redesign** of selected hallucinated proteins: overlays of original and modified designs with the substituted residues, and SEC traces of original versus modified sequences.
- **Figure 4** — overlays of the crystal structures with their closest PDB matches.
- **Figure 5** — network-generated **β-sandwich** structures with surface hydrophobics shown explicitly.
- **Figure 6** — examples of **core overpacking** in models 0515, 0217 and 0738.
- **Figure 7** — comparison of reference Cβ–Cβ distributions collected from the PDB against those produced by the **background network** for proteins of different length.

## Key extracted details

- **Novelty is quantified two ways, and the distinction matters.** Table 1 separates the closest match *in the training set* from the closest match *in the PDB overall*. Restricted to the training set, TM-scores to the closest structure are **0.627 (0217), 0.693 (0515) and 0.547 (0738_mod)**; against the whole PDB they rise to **0.822, 0.909 and 0.765**. Closest sequence matches in the PDB are weak throughout — E-values **0.22, 0.021 and 0.31**. The designs are therefore closer to structures the network never trained on than to ones it did, which is a stronger anti-memorization argument than a single PDB-wide number.
- **Top7 again.** Figure 4 confirms the closest PDB match to chain B of 0738_mod is **PDB 1QYS — Top7**, the canonical Rosetta de novo design. The convergence of a learned generator onto the same idealized region of fold space that expert designers reached is one of the paper's central claims, and this figure is the evidence for it.
- **The surface-hydrophobic diagnosis is demonstrated, not asserted.** Figure 3 pairs the substituted-residue overlays with before/after SEC traces, showing directly that replacing exposed hydrophobics with polar residues converts oligomeric designs to monomers. Figure 5 shows the β-sandwich designs with their surface hydrophobics as sticks, which is why that class had a low success rate.
- **Core overpacking is a separate, unresolved defect.** Figure 6 localizes it in all three solved designs. It follows from trRosetta operating without explicit side-chain or packing representation, and is the limitation the paper suggests fixing by complementing hallucination with all-atom design.
- **The background network is validated empirically** (Figure 7) against reference Cβ–Cβ distributions from the PDB across protein lengths — relevant because the *entire* hallucination objective is a divergence from that background, so a miscalibrated background would silently distort every design.

## Why this matters for the chapter

[[symmetric-oligomer-design]] treats hallucination's tendency to produce sequences with aberrant surface properties as a recurring characteristic rather than a one-off. This SI is where that claim is grounded for the *first* hallucination paper: the oligomerization is documented, attributed to learned native-interface features, and shown to be reversible by surface redesign. When [[wicky-2022-symmetric-assembly-design]] later found the same class of pathology at far greater severity — and solved it with [[dauparas-2022-proteinmpnn]] rather than manual substitution — it was hitting a known weakness of the method, not a surprise.

## Connections

- Parent: [[anishchenko-2021-hallucination]].
- The failure modes here anticipate the adversarial-sequence analysis in [[wicky-2022-symmetric-assembly-design]].
- The core-overpacking limitation is one of the motivations for all-atom generative design ([[chu-2024-protpardelle]], [[butcher-2025-rfdiffusion3]]).
