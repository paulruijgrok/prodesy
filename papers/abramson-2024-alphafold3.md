---
type: source
title: Accurate structure prediction of biomolecular interactions with AlphaFold 3
authors: Abramson et al. (DeepMind / Isomorphic Labs)
venue: Nature 2024
pdf: "../sources/ProteinDesign/AmbramsonJumper_Nature_2024_Accurate structure prediction of biomolecular interactions with AlphaFold 3.pdf"
supp: yes
tags: [structure-prediction, deep-learning, diffusion, complexes, foundational]
ingested: 2026-07-10
---

# AlphaFold3 — Structure prediction of biomolecular interactions

Generalizes [[jumper-2021-alphafold2]] from single proteins to the joint structure of complexes spanning proteins, nucleic acids, small molecules, ions and modified residues, within one unified model.

**Problem.** AF2 predicted protein (and, via Multimer, protein–protein) structures, but biology runs on heterogeneous complexes — protein–ligand, protein–DNA/RNA, covalent modifications — which previously required separate specialized tools.

**Approach.** [[alphafold]] 3 replaces the AF2 structure module with a **diffusion-based** generative head that predicts raw atom coordinates directly, removing much stereochemical special-casing and allowing arbitrary chemical entities. The MSA machinery is simplified (a lighter "Pairformer" replaces much of the Evoformer). A diffusion rollout at inference generates the structure; a confidence head is trained on top.

**Key results.**

- Substantially higher accuracy than specialized tools: better than state-of-the-art docking for **protein–ligand**, better than nucleic-acid-specific predictors for **protein–nucleic-acid**, and markedly better **antibody–antigen** accuracy than AlphaFold-Multimer v2.3.
- One model covers most of biomolecular space, showing unified deep-learning modelling across chemistry is feasible.
- Known limitation: occasional **hallucinated order** in disordered regions and chirality/overlap errors, mitigated with cross-distillation and ranking.

**Significance.** Marks the migration of the structure-prediction field itself onto [[diffusion-generative-design]] machinery — the same generative paradigm driving de novo design — hinting at convergence between prediction and design models.

**Supplement:** [[abramson-2024-alphafold3-supp]] — unified tokenization (atoms + residues), Pairformer (Evoformer successor), diffusion module/conditioning, atom attention, confidence-on-samples + clash ranking, cross-distillation to suppress hallucinated disorder.

**Connections.**

- Direct successor to [[jumper-2021-alphafold2]].
- Shares the diffusion paradigm with [[watson-2023-rfdiffusion]] and [[ingraham-2023-chroma]].
- Relevant to [[structure-prediction]] and to all-atom modelling (cf. RoseTTAFold All-Atom, queued).
