---
type: source
title: "Metal3D: a general deep learning framework for accurate metal ion location prediction in proteins"
authors: Dürr, Levy & Rothlisberger (EPFL)
venue: Nature Communications 2023 (14:2713; doi 10.1038/s41467-023-37870-6)
pdf: "../sources/ProteinDesign/DurrRotlisBerger_NatComm_2023_Metal3D- a general deep learning framework for accurate metal ion location prediction in proteins.pdf"
supp: yes
tags: [metalloprotein-design, zinc, 3d-cnn, prediction, enzyme-design, methods]
ingested: 2026-10-21
---

# Metal3D — predicting metal ion locations in proteins

A 3D convolutional neural network that predicts **where a zinc ion sits** given a protein structure and a set of residues — the model that supplies the **p(metal | sequence, structure)** objective in [[elnesr-2026-zero-shot-metalloenzyme]], and the reason that paper could design a coordination sphere without a motif template.

## Problem

Metals are attractive for design because they are "biologically abundant, tether to the protein using strong interactions, and have favorable catalytic properties" — **about 10% of all enzyme-catalysed reactions use zinc**, which is an excellent Lewis acid and serves structural roles (zinc fingers) and catalytic ones in sites up to trinuclear. But computational design of metalloproteins "is hampered by the complex electronic structure of many biologically relevant metals such as zinc": classical force fields handle metals poorly, and quantum-mechanical treatment is too expensive for design-scale work, usable only to verify select candidates.

Existing predictors had specific limitations the paper names. **MIB** combines structural and sequence information but searches for homologous sites in a database and **excludes metal sites with fewer than two coordinating residues**. **BioMetAll** is a geometric predictor based on backbone preorganization that is template-free but "provides many possible locations for putative" sites — high recall, poor precision.

## Approach

Two tools, deliberately contrasting:

- **Metal3D** — a **fully convolutional 3D CNN** operating on a **voxelized representation** of the environment around each input residue, trained to predict metal density. Metal positions are then placed using the **weighted average of voxels above a cutoff**.
- **Metal1D** — a purely geometric predictor that extracts zinc coordination motifs from **LINK records** in the training structures and scans all residues for compatibility with the resulting probability map, placing metals at the geometric centre of high-scoring residues.

**Training data:** experimental high-resolution crystal structures containing zinc sites — **2,085 structures giving 252,324 voxelized environments**. Both tools are trained **solely on zinc**, with performance and selectivity evaluated for zinc; the framework "is readily extensible to other metals by modifying the training data".

## Key results

- **Metal3D is the most accurate zinc location predictor reported, placing metals within 0.70 ± 0.64 Å of experimental locations.**
- It outputs a **confidence metric per predicted site** and "works on proteins with few homologues in the protein data bank" — the template-independence that makes it usable inside a design loop rather than only as an annotation tool.
- Against MIB (t = 1.25) and BioMetAll, Metal3D at probability cutoff **p = 0.75 identifies more sites (85) than MIB** while predicting **only 9 false positives**, where BioMetAll produces 134. Metal1D at t = 0.5 offers similar detection capability, with higher recall but reduced precision at low thresholds.
- It produces two distinct outputs with different uses: a **global zinc density** for annotating computationally predicted structures, and a **per-residue zinc density** usable inside protein design workflows.

## Significance / relation to the field

**It is the enabling component of a distinct design philosophy.** [[elnesr-2026-zero-shot-metalloenzyme]] pairs Metal3D with LigandMPNN in a two-objective evolutionary search, using Metal3D as the term that asks whether a sequence actually *makes* a metal site rather than whether it resembles one. Without a model of this kind, metalloenzyme design has to proceed by transplanting a native motif, which is what every Baker-lab source in [[enzyme-design]] does.

**Its training data became a finding in its own right.** [[elnesr-2026-zero-shot-metalloenzyme]] audited this paper's training set and found zinc sites with **fewer than three coordinating residues within 3.0 Å** — environments that "may reflect crystallization additives or soaking agents rather than biologically" meaningful sites — and retrained **Metal3D-Clean** excluding them, plus **Metal3D-Cat** on catalytic zincs only from MAHOMES-II. Metal3D's own paper anticipates part of this: it notes that metals are often present in crystallization buffers because they help overcome the enthalpic cost of protein surface association. The wiki's reading is that a predictor trained on "zinc appears here in a crystal structure" learns a different thing from "zinc is functionally bound here", and that the distinction only became consequential once the model was used generatively.

**A caveat for the chapter.** Trained and evaluated on zinc alone. Claims about metalloenzyme design generality through this component are claims about zinc.

**Supplement:** [[durr-2023-metal3d-supp]].

## Connections

- Supplies the metal-location objective in [[elnesr-2026-zero-shot-metalloenzyme]], whose Metal3D-Clean and Metal3D-Cat retrainings are the critical follow-up.
- Contrasts with the motif-transplant approach to zinc sites in [[chen-2026-metalloproteases]] and the carbamylated-lysine di-metal site in [[butcher-2026-rfdiffusion3-science]].
- Chapter: [[enzyme-design]] §2 and §6. Concept: [[metalloprotein-design]].
