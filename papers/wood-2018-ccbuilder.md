---
type: source
title: "CCBuilder 2.0: Powerful and accessible coiled-coil modeling"
authors: Wood & Woolfson
venue: Protein Science 2018
pdf: "../sources/Proteins/Wood_Woolfson_ProteinSci_2018_v27_p103_CCBuilder 2.0- Powerful and accessible coiled‐coil modeling.pdf"
supp: no
tags: [parametric-design, coiled-coils, tools, repeat-proteins, software]
ingested: 2026-08-24
---

# CCBuilder 2.0

A web application that turns [[parametric-design]] of coiled coils into something anyone can do in a browser — and, in its framing of *why* parametric modeling works at all, the clearest statement of the link between coiled coils and repeat proteins.

**Problem.** More accessible computational tools would widen the reach of biomolecular design. For protein modeling specifically, the key challenge is **reducing 3D folds to sets of parametric equations that still capture the salient structural features**. The paper is explicit that this is currently possible only for a subset of proteins — **namely, repeat proteins** — of which the α-helical coiled coil is the exemplar, representing an estimated **3–5% of all known protein-encoding regions of DNA**.

**The parametric lineage it summarizes.** The original parameterization is Crick's, from **1953**. It was extended in 1995, applied by Harbury and colleagues to design a right-handed coiled-coil tetramer (the design line that begins with [[harbury-1993-coiled-coil-oligomer-switch]]), and **generalized in 2002** to cover further coiled-coil types. Alongside model *building*, tools were developed for **fitting Crick parameters to structural data**, i.e. running the parameterization backwards from a solved structure.

**Approach.** CCBuilder 2.0 generates models from a small set of Crick parameters and then **optimizes** them, scoring with two all-atom force fields — **BUDE** (Bristol University Docking Engine) and **BUFF** — with the underlying general parametric model-building machinery provided by the **ISAMBARD** package. Coverage extends beyond classical bundles to **α-helical barrels** (more than four helices, of the kind designed in [[thomson-2014-alpha-helical-barrels]]) and to **polyproline-based collagen triple helices**. Accuracy was previously validated by recreating known coiled-coil structures.

**Key results / capabilities.**

- Free, open-source, browser-based: `http://coiledcoils.chm.bris.ac.uk/ccbuilder2`.
- Applications the authors name: generating models to aid **molecular replacement** in X-ray crystallography, in silico model building and engineering of natural and designed assemblies, and creating **completely de novo "dark matter" protein structures** — the regions of fold space not represented in the PDB.

**Significance.** Two reasons this is worth a page. First, it makes the parametric approach *usable* — the counterweight to the observation in [[symmetric-oligomer-design]] that the pre-diffusion route demanded bespoke engineering per design. Second, its problem statement supplies the conceptual bridge this wiki was missing: **parametric design is possible precisely for repeat proteins**, because a structure built by applying one transform repeatedly is describable by the few parameters of that transform. That is the same reason the DHR architectures of [[brunette-2015-repeat-protein-universe]] collapse onto three helical parameters, and the reason [[huang-2014-parametric-helical-bundles]] can specify a bundle with a handful of numbers. See [[parametric-design]] and [[repeat-protein-design]].

**Connections.**

- Tool page: [[ccbuilder]].
- Implements the Crick-equation machinery documented concretely in [[huang-2014-parametric-helical-bundles-supp]].
- From the same lab as [[thomson-2014-alpha-helical-barrels]]; models the barrel class that paper designed.
- Concepts: [[parametric-design]], [[repeat-protein-design]], [[symmetric-assembly-design]].
