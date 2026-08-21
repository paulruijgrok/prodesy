---
type: source
title: Hallucinating symmetric protein assemblies
authors: Wicky, Milles, Courbet et al. (Baker lab)
venue: Science 2022
pdf: "../sources/ProteinDesign/WickyBaker_Science_2022_Hallucinating symmetric protein assemblies.pdf"
supp: missing-requested
tags: [symmetry, hallucination, oligomers, nanomaterials, de-novo]
ingested: 2026-07-13
---

# Hallucinating symmetric protein assemblies

Uses deep-network **hallucination** to design symmetric homo-oligomers from almost nothing — just the number of protomers and their length — producing assemblies unlike anything in the PDB.

**Problem.** Symmetric protein assemblies (rings, cages) are building blocks for nanomachines and biomaterials, but designing novel ones — especially large, high-symmetry rings — was hard with fragment/parametric methods.

**Approach.** Deep-network **hallucination**, the method established by [[anishchenko-2021-hallucination]], with two changes: the oracle is AlphaFold2 rather than trRosetta, and a **cyclic-symmetry objective** — the standard deviation of center-of-mass distances between adjacent protomers in the predicted structure — is added to the confidence terms (pLDDT, pTM). Inputs are only chain length L and protomer count; trajectories converge to cyclic homo-oligomers with no template.

**Key results.**

- **Seven crystal structures** match the computational models at **median RMSD 0.6 Å**.
- **Three cryo-EM structures** of giant ~10-nm rings, up to **1550 residues and C33 symmetry** — all differing considerably from previously solved structures (generalization well beyond the PDB/CATH/SCOP training set).
- Demonstrates deep learning can access a rich diversity of new assembly topologies.

**Significance.** The hallucination-for-symmetry idea is the precursor to [[watson-2023-rfdiffusion]]'s symmetric-oligomer generation (which replaces the slow optimization with conditional diffusion). Defines the [[symmetric-assembly-design]] concept; treated at length in [[symmetric-oligomer-design]] §5.2.

**Note on the failure mode.** The wholesale expression failure of the original hallucinated sequences is a severe instance of a pathology already documented in [[anishchenko-2021-hallucination]], where unconstrained hallucination produced unintended homo-oligomers and soluble aggregates traced to **exposed surface hydrophobics** learned from native oligomeric structures in the PDB ([[anishchenko-2021-hallucination-supp]]). The chapter's reading is that a symmetry objective *rewards* inter-protomer contact and so amplifies precisely that tendency; what differs between the papers is the remedy — manual polar substitution there, wholesale redesign with [[dauparas-2022-proteinmpnn]] here.

**Connections.**

- Builds directly on [[anishchenko-2021-hallucination]] — the same MCMC-against-a-predictor engine, plus a symmetry term.
- Shares the hallucination engine with [[wang-2022-functional-site-scaffolding]].
- Symmetric design generalized by [[watson-2023-rfdiffusion]] (see [[watson-2023-rfdiffusion-supp]] §3.1 point groups).
- Concept: [[symmetric-assembly-design]]; uses [[alphafold]]-style confidence as the hallucination signal.
