---
type: tool
tags: [parametric-design, coiled-coils, software, web-app, woolfson]
sources: 1
updated: 2026-08-24
---

# CCBuilder 2.0

Woolfson-lab **web application for parametric modelling and optimization of coiled coils**, and the most accessible entry point to [[parametric-design]] ([[wood-2018-ccbuilder]]).

**What it does.** Builds coiled-coil models from a small set of Crick parameters and then optimizes them, scoring with two all-atom force fields — **BUDE** (Bristol University Docking Engine) and **BUFF** — on top of the **ISAMBARD** package, which provides the general parametric model-building machinery ([[wood-2018-ccbuilder]]).

**Coverage.** Classical coiled-coil bundles; **α-helical barrels** (more than four helices, the class designed in [[thomson-2014-alpha-helical-barrels]]); and **polyproline-based collagen triple helices** ([[wood-2018-ccbuilder]]).

**Stated uses.** Generating models to aid **molecular replacement** in X-ray crystallography, in silico model building and engineering of natural and designed assemblies, and creating de novo **"dark matter"** structures outside the PDB's coverage ([[wood-2018-ccbuilder]]).

**Availability.** Free and browser-based at `http://coiledcoils.chm.bris.ac.uk/ccbuilder2`, with open-source code available for download ([[wood-2018-ccbuilder]]).

**Why it's here.** The wiki's other symmetric-design tools ([[rfdiffusion]], [[chroma]], [[protpardelle]]) are learned generative models. CCBuilder is the counterexample still standing: a purely geometric generator, with zero symmetry error by construction, for the fold class where a closed-form description exists. Its own framing of *why* that is possible — parameterization works for **repeat proteins** — supplies the bridge between [[parametric-design]] and [[repeat-protein-design]].

**Lineage.** Crick's 1953 parameterization → extended 1995 → applied by Harbury and colleagues to a right-handed tetramer ([[harbury-1993-coiled-coil-oligomer-switch]] is the start of that design line) → generalized in 2002 → CCBuilder, then CCBuilder 2.0 ([[wood-2018-ccbuilder]]). The concrete equations as used in design are set out in [[huang-2014-parametric-helical-bundles-supp]].

**Source:** [[wood-2018-ccbuilder]].
