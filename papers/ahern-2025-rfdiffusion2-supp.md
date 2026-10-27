---
type: source-supp
parent: "[[ahern-2025-rfdiffusion2]]"
title: Atom-level enzyme active site scaffolding using RFdiffusion2 — Supplementary Information
pdf: "../sources/ProteinDesign/AhernBaker_NatureMethods_2025_Atom-level enzyme active site scaffolding using RFdiffusion2_Supp.pdf"
tags: [enzyme-design, methods, flow-matching, training, atomization, unindexed-motif, benchmarks]
ingested: 2026-10-21
---

# RFdiffusion2 — Supplementary Information (companion)

67-page methods companion to [[ahern-2025-rfdiffusion2]]. Its value is the **training-example construction algorithm**, which is where the indexed/unindexed and frame/atom choices are actually made and sampled.

## What the SI contains (map)

- **The training data pipeline, as a numbered algorithm.** Each training example is built by: (1) sampling a biomolecule category by probability; (2) sampling a cluster within that category, by computed cluster weight; (3) sampling a biomolecule from the cluster uniformly; (4) cropping each feature to fixed size; (5) **sampling which substructures are motifs and the representations of all residues**; (6) **processing the unindexed and atomized residues** using the masks from the previous step; (7) **stochastic centering**; (8) sampling a noise time t uniformly in [0, 1] and noising the structure; (9) computing features; (10) returning the ground-truth biomolecule, the noised biomolecule, and the conditioning.
- **The motif and representation sampling sub-procedure.** A function is selected depending on training mode, then called to sample the motif and representations; **each residue is annotated as unindexed with probability `P_IS_UNINDEXED`**, and a Bernoulli(0.5) draw governs a further representational choice before the specification passes downstream.
- Flow-matching formulation details for the mixed ℝ³ / SE(3) data representation, loss definitions, and the AME benchmark construction and per-case results.

## Key extracted details

**Unindexing is a sampled training augmentation, not an inference-time hack.** The probability `P_IS_UNINDEXED` is applied per residue during training-example construction, which is why the model can be conditioned on an unindexed motif at inference "without any auxiliary losses" — the behaviour was trained in by exposure, not imposed by a penalty. This is the mechanistic answer to the question the main text raises and does not fully settle: how the network comes to superimpose unindexed residues onto generated ones.

**Representation is sampled per residue, every example.** Because step 5 samples *which* substructures are motifs *and* the representation of *all* residues, a single training run covers the whole product space of frame/atomized × indexed/unindexed. That breadth is what makes one checkpoint usable for domain scaffolding and for four-functional-group theozymes alike.

**Crystallisation additives are filtered.** The main text notes training "filters out common solvents and crystallization" additives — the same class of contamination that [[elnesr-2026-zero-shot-metalloenzyme]] later found uncorrected in the Metal3D and LigandMPNN corpora, where it produced a confidently-predicted but non-binding metal site. Worth recording that this generator's authors filtered it and that generator's did not.

**Stochastic centering** (step 7) is listed as its own algorithm, which matters for a model mixing absolute atom positions with SE(3) frames, since the two have different translation behaviour.

## Connections

- Parent: [[ahern-2025-rfdiffusion2]]. Compare the tokenization and conditioning-probability tables in [[butcher-2026-rfdiffusion3-science-supp]], which serve the same role for the free-atom successor.
- Chapter: [[enzyme-design]] §3.
