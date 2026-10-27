---
type: source
title: Deciphering interaction fingerprints from protein molecular surfaces using geometric deep learning
authors: Gainza, Sverrisson, Monti, Rodolà, Boscaini, Bronstein, Correia
venue: Nature Methods 2020 (17, 184–192; published online 9 December 2019)
pdf: "../sources/ProteinDesign/GainzaCorreia_NatureMethods_2023_Deciphering interaction fingerprints from protein molecular surfaces using geometric deep learning.pdf"
supp: yes
tags: [surface-fingerprints, geometric-deep-learning, interface-prediction, representation, methods]
ingested: 2026-10-12
---

# MaSIF — molecular surface interaction fingerprinting

The representation paper underneath [[gainza-2023-surface-fingerprint-binders]]: a geometric-deep-learning framework that learns **fingerprints of protein molecular surfaces** predictive of what a patch will interact with, without explicit use of sequence or fold.

**Filename note.** The PDF in `sources/ProteinDesign/` is named `…NatureMethods_2023…`, but the paper is *Nature Methods* **17**, 184–192 (February 2020 issue; online 9 December 2019; DOI 10.1038/s41592-019-0666-6). The filename year is wrong; flagged for the next lint sweep. The page follows the publication year.

**Problem.** Predicting interactions purely from structure remains a central challenge. Existing methods largely exploit evolutionary signatures and therefore require knowledge of homologous proteins. Earlier surface-based descriptors (3D Zernike, geometric invariant fingerprints) were **handcrafted** — manually optimized feature vectors — and the paper's objection is structural rather than empirical: it is hard to determine a priori which features matter for a given prediction task, so the feature set should be learned.

**Approach.** The central hypothesis is that proteins **with no sequence homology** that undergo similar biomolecular interactions display similar surface patterns, too subtle for visual analysis but learnable at scale. Mechanically:

- Compute a discretized solvent-excluded molecular surface and assign features to every vertex.
- Decompose the surface into **overlapping radial patches of fixed geodesic radius** (9 Å or 12 Å, application-dependent; the smaller radius is used where multiple geodesic convolutional layers make memory the constraint).
- Per vertex, two **geometric** features plus **chemical** features (hydropathy index, continuum electrostatics, and others).
- Assign each vertex **geodesic polar coordinates** within its patch — radial coordinate as geodesic distance, i.e. distance walked *along* the surface. This is the load-bearing choice: on irregular surfaces with deep pockets, geodesic distances can be much larger than Euclidean ones, so a geodesic parameterization describes a pocket as a pocket.
- Learn to embed each patch's input features into a vector descriptor via geodesic convolutional layers, trained **end-to-end per task** — so descriptors are task-specific, not universal.

Three applications are demonstrated: **MaSIF-ligand** (pocket–ligand similarity), **MaSIF-site** (predicting protein-binding surface sites) and **MaSIF-search** (ultrafast scanning of surfaces to predict protein–protein complex configurations). The binder-design extension MaSIF-seed in [[gainza-2023-surface-fingerprint-binders]] is built on MaSIF-site plus MaSIF-search.

## Key results

The input features are explicitly **precomputed, not learned** — chemistry and geometry are given, and only their embedding is trained. The networks share reusable building blocks (geodesic convolutional layers) across the three tasks, which is the sense in which MaSIF is described as a conceptual framework rather than a single model.

## Significance / relation to the field

This is the wiki's only source for the proposition that a protein's *surface* is a sufficient representation for predicting what it binds — as against the residue-graph representation of [[dauparas-2022-proteinmpnn]] or the backbone-frame representation of [[watson-2023-rfdiffusion]]. For the chapter, it is the answer to "why would anyone represent a binder problem this way", and it is what makes the independent lineage in §6 of [[de-novo-binder-design]] a genuine methodological alternative rather than a different training run.

The homology-independence claim also matters for binder design specifically: a method that does not need homologues is a method that can be pointed at a target with no bound structure in the PDB — the regime [[stark-2025-boltzgen]] later tests explicitly.

**Supplement:** [[gainza-2020-masif-supp]].

## Connections

- Applied to de novo binder design in [[gainza-2023-surface-fingerprint-binders]].
- Supplement: [[gainza-2020-masif-supp]].
- Representational contrast with [[dauparas-2022-proteinmpnn]] (residue graph), [[watson-2023-rfdiffusion]] (backbone frames) and [[krishna-2024-rosettafold-all-atom]] (all-atom tokens).
- Concept: [[binder-design]], [[structure-prediction]].
