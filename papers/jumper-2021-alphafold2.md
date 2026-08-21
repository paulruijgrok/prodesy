---
type: source
title: Highly accurate protein structure prediction with AlphaFold
authors: Jumper et al. (DeepMind)
venue: Nature 2021
pdf: "../sources/ProteinDesign/JumperHaasbis_Nature_2021_Highly accurate protein structure prediction with AlphaFold.pdf"
supp: yes
tags: [structure-prediction, deep-learning, msa, foundational]
ingested: 2026-07-10
---

# AlphaFold2 — Highly accurate protein structure prediction

The paper that effectively solved single-chain protein structure prediction from sequence, the founding result of the modern deep-learning era in [[structure-prediction]].

**Problem.** Predicting 3D structure from amino-acid sequence — the structure-prediction half of the protein-folding problem — had been open for 50+ years. Prior methods fell far short of atomic accuracy when no homologous template existed.

**Approach.** [[alphafold]] (AF2) is an end-to-end neural network built around two ideas: the **Evoformer**, which jointly reasons over a multiple-sequence alignment (MSA) and a residue–residue pair representation, and a **structure module** that produces explicit 3D atomic coordinates using invariant point attention and a frame ("residue gas") representation. Trained end-to-end on PDB structures with self-distillation on unlabelled sequences; recycling refines predictions iteratively.

**Key results.**

- At **CASP14**, AF2 achieved a median backbone accuracy of ~0.96 Å RMSD_95 on the domain set, far ahead of all competitors — a step change to atomic accuracy even without templates.
- Produces a calibrated per-residue confidence score (**pLDDT**) and a global measure (**pTM**) that reliably flag which predictions to trust.
- Generalizes across fold space; the released method enabled proteome-scale structure databases.

**Significance.** AF2 is the substrate on which much of modern protein design now rests: its confidence metrics are repurposed as *in silico* filters for design (see [[bennett-2023-binder-design-dl]]), and its network weights/architecture seeded generative models via fine-tuning of the sibling RoseTTAFold network (see [[watson-2023-rfdiffusion]]).

**Supplement:** [[jumper-2021-alphafold2-supp]] — the canonical architecture spec: Evoformer (triangle updates/attention), IPA structure module, FAPE loss, pLDDT/pTM confidence, recycling, self-distillation, CASP14 protocol, ablations.

**Connections.**

- Extended to complexes and other biomolecules by [[abramson-2024-alphafold3]].
- Used as a design oracle/filter in [[bennett-2023-binder-design-dl]].
- Conceptual/architectural sibling of RoseTTAFold, the backbone that [[watson-2023-rfdiffusion]] fine-tunes.
- Core reference for the [[structure-prediction]] concept.
