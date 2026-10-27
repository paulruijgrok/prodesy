---
type: source-supp
parent: "[[frank-2024-relaxed-sequence-optimization]]"
title: Scalable protein design using optimization in a relaxed sequence space — Supplementary Materials
pdf: "../sources/ProteinDesign/FrankDietz_Science_2024_Scalable protein design using optimization in a relaxed sequence space_Supp.pdf"
tags: [hallucination, gradient-descent, methods, oligomers, colabdesign, loss-functions]
ingested: 2026-08-24
---

# RSO — Supplementary Materials (companion)

Companion to [[frank-2024-relaxed-sequence-optimization]]. Figs. S1–S17, Tables S1–S11, Movies S1–S4. Unusually practical for a supplement: the loss weights and the ColabDesign calls are given verbatim, so the method is reproducible from this document alone.

## Key extracted details

- **The optimization setup.** Hallucinations run in the **ColabDesign** framework. The relaxed sequence is initialized with **Gumbel noise** and optimized by **normalized gradient descent**. The entry point is `design_logits()` on a model made with `mk_afdesign_model(protocol="hallucination")`, restarted in `["gumbel", "soft"]` mode.
- **The standard loss, with weights.** pLDDT **0.5**, pAE **0.5**, helix **−0.2**, contacts **1.0**, radius of gyration **0.1**. For chains longer than 600 residues the confidence terms are doubled to **1.0** each, the helix penalty is halved to **−0.1**, and the radius-of-gyration weight is dropped to **0.01** (0.001 above 900 residues). The **negative helix weight** is what counters the model's bias toward all-α outputs; the length-dependent reweighting is what makes 1000-residue design work.
- **How symmetry/multimers are imposed.** Homo-oligomers use ColabDesign's **`copies` option**, which **copies the input logits** and introduces an **index shift of 50** at the breakpoint between copies, with the loss upgraded to include **interface PAE and contact terms**. Heterodimers use the same index offset of 50 but add a heterodimer loss that keeps two separate domains while staying globular overall. This is a distinct mechanism from anything else in [[symmetric-oligomer-design]]: sequence identity between protomers is **exact by construction** (they are literally the same logits), while the *geometry* of the interface is **rewarded** through interface losses.
- **The filtering cascade for interfaces.** Design a sequence with [[proteinmpnn]] → predict both protomers as separate monomers → require mean **pLDDT > 80** → predict the heterodimeric complex → require mean **pLDDT > 85** and **RMSD to target backbone < 2.0 Å** → then homodimer-filter by copying each sequence and predicting it as a homodimer, requiring **normalized homodimer I_PAE above 0.8** to pass. The homo-oligomer filter is therefore an explicit *negative* design step, which is what makes its omission (and the resulting unintended homo-oligomers) an interpretable result rather than an accident.
- **What the movies show.** Movies S1 and S3 visualize the prediction of the relaxed sequence beside the prediction of its argmax one-hot counterpart at each iteration — the direct demonstration that the relaxed representation and its discretization are not predicting the same structure, which is the paper's central methodological claim.
- **Supplementary Figure 17** collects the oligomer characterization: AF2 predictions plus SEC traces for the designed homo-oligomers, and SEC overlays of individual monomers against mixed heterodimers.

## Connections

- Parent: [[frank-2024-relaxed-sequence-optimization]].
- The `copies`-with-tied-logits mechanism is the counterpart to the tied-position decoding in [[dauparas-2022-proteinmpnn-supp]] and to point-group operators in [[watson-2023-rfdiffusion-supp]] §3.1.
- Chapter: [[symmetric-oligomer-design]] §7.
