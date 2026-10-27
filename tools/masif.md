---
type: tool
tags: [surface-fingerprints, geometric-deep-learning, interface-prediction, binder-design, correia-lab]
sources: 3
updated: 2026-10-12
---

# MaSIF

**Molecular Surface Interaction Fingerprinting** — a geometric-deep-learning framework that learns descriptors of protein *molecular surfaces* predictive of what a surface patch will bind, without explicit use of sequence or fold. Introduced in [[gainza-2020-masif]]; extended to de novo binder design in [[gainza-2023-surface-fingerprint-binders]].

**Representation.** A discretized solvent-excluded surface is decomposed into **overlapping radial patches of fixed geodesic radius** (9 Å or 12 Å, application-dependent); each vertex carries precomputed geometric and chemical features — hydropathy index, continuum electrostatics among them — and **geodesic polar coordinates** within its patch. Geodesic convolutional layers learn to embed each patch into a vector descriptor, trained end-to-end per task, so descriptors are task-specific rather than universal ([[gainza-2020-masif]]).

The geodesic parameterisation is the load-bearing choice: on trypsin, a 12 Å *Euclidean* patch centred in an interface pocket reaches points on a different face of the protein entirely, while the 12 Å *geodesic* patch stays on the interacting face ([[gainza-2020-masif-supp]]).

**The four variants.**

- **MaSIF-ligand** — pocket–ligand similarity and cofactor specificity.
- **MaSIF-site** — predicts which surface patches have a high propensity to be engaged by a protein. ROC AUC **0.86** with three convolutional layers against 0.77 with one, over 2,192,870 test-set surface points ([[gainza-2020-masif-supp]]).
- **MaSIF-search** — ultrafast surface scanning to predict protein–protein complex configurations: fingerprint a target site, retrieve the K most similar fingerprints from a precomputed database, align by RANSAC, score with a small network ([[gainza-2020-masif-supp]]).
- **MaSIF-seed** — the design variant: evaluate fingerprint complementarity between a chosen target patch and a library of α-helical and β-strand binding motifs, then graft hits onto scaffolds with Rosetta MotifGraft ([[gainza-2023-surface-fingerprint-binders]]).

**Pipeline role.** MaSIF-site nominates the epitope → MaSIF-seed retrieves complementary seeds → Rosetta grafts and designs the surrounding interface → yeast display with deep sequencing selects. Note the inversion relative to the dominant stack: hotspot-conditioned diffusion tells a generator *where* to bind and asks it to invent a binder, whereas MaSIF **searches for what is complementary** and builds a scaffold around the hit.

**Validated performance.** Top-1 recovery of the native binder (<3 Å interface RMSD) among 1,000 decoys: **18/31** helical and **41/83** non-helical, against 3/31 and 7/83 for ZDock, at 15 and 118 minutes against 2,206–2,946 ([[gainza-2023-surface-fingerprint-binders]]) — though the supplement records ZDock times as CPU user time on a 96-vCPU server, so the speed gap is partly GPU-versus-CPU ([[gainza-2020-masif-supp]]). Designed binders reached 80 nM (SARS-CoV-2 RBD, cryo-EM confirmed at 1.4 Å iRMSD), 120–256 nM (PD-L1, crystal structures at 0.8 Å RMSD), and **4.2 ± 2 µM for PD-1 with no experimental optimisation at all** ([[gainza-2023-surface-fingerprint-binders]]).

**Why it is the chapter's control.** It is the only non-Baker-lab de novo binder lineage in the wiki, it is homology-free by construction ([[gainza-2020-masif]]), and its evaluation splits are the strictest ingested anywhere: removing every test structure with TM-score > 0.5 to any training member did not affect performance ([[gainza-2020-masif-supp]]).

**Connections.** Representational contrast with [[proteinmpnn]] (residue graph), [[rfdiffusion]] (backbone frames) and [[rfdiffusion3]] (all-atom tokens). Its hotspot placement, validated by site-saturation mutagenesis, is the experimental counterpart of [[halperin-2004-interface-hot-spots]]. Grafting route shared with [[motif-scaffolding]]. Concept [[binder-design]]; chapter [[de-novo-binder-design]] §6.
