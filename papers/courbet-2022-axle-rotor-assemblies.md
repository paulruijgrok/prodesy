---
type: source
title: Computational design of mechanically coupled axle-rotor protein assemblies
authors: Courbet, Hansen, Hsia et al. (Baker lab)
venue: Science 2022
pdf: "../sources/ProteinDesign/CourbetBaker_Science_2022_Computational design of mechanically coupled axle-rotor protein assemblies.pdf"
supp: yes
tags: [symmetry, oligomers, dihedral, nanomachines, cryo-em, rosetta]
ingested: 2026-08-14
---

# Mechanically coupled axle-rotor protein assemblies

Builds nanoscale **machines** out of designed cyclic and dihedral symmetric components, deliberately **mismatching the symmetries** of an axle and a rotor so that the coupled system retains an internal degree of freedom rather than locking into one rigid structure.

**Problem.** Natural molecular machines contain protein components that move relative to one another. Designed protein nanomaterials up to this point — the authors name **icosahedral nanocages** and **two-dimensional arrays** — are assemblies in which the components have **fixed orientations** relative to each other. Designing a mechanically constrained nanoscale architecture that has *internal degrees of freedom* was an outstanding challenge: the interface between the two rigid bodies must be low-energy enough to drive self-assembly while still permitting relative motion.

**Approach.** A three-step hierarchical design: (i) de novo design of stable, rigid components suitable for mechanical assembly, (ii) directed self-assembly of those components into hetero-oligomeric complexes, and (iii) shaping of the multistate energy landscape along the mechanical degrees of freedom. The blueprint is an **axle** inside a **rotor**, as in natural rotary systems, where the energy landscape is determined by the symmetry of the interacting components, their shape complementarity, and specific cross-interface interactions. Components are built by combining **parametric backbone generation** with **rigid helical fusion** (RosettaRemodel) of designed cyclic homo-oligomers, and interfaces are specified using **hydrogen-bond networks** (see [[courbet-2022-axle-rotor-assemblies-supp]]).

**Key results.**

- Designed a wide range of symmetric components: **C3, C4, C5 and C8 cyclic rotors** and **D2, D3, D4, D5 and D8 dihedral axles**, several converted from dihedral to cyclic symmetry by connecting termini.
- Structures confirmed by **cryo-EM** — a 6.0 Å map for the C3 rotor C3_R1 (28 Å internal diameter), 7.9 Å for the C4 rotor C4_1 (57 Å internal diameter), 4.2 Å for the D3 axle D3_3, and 7.4 Å for the D8 axle D8_1 — plus negative-stain reconstructions for others.
- Assembled **symmetry-mismatched machines**: **D3–C3** and **D3–C5** axle-rotor systems, which assemble both in vitro and in vivo as designed.
- Cryo-EM shows these systems **populate conformationally variable relative orientations** reflecting the symmetry of the coupled components and the designed interface energy landscape — the D3–C3 system is largely constrained along its degrees of freedom, whereas the symmetry-mismatched D3–C5 rotor can rotate and translate along the main symmetry axis.

**Significance.** For [[symmetric-oligomer-design]] this paper matters for two reasons. First, it is the clearest demonstration that **symmetry is a design variable with mechanical consequences**: matching the symmetries of two coupled components rigidifies the assembly, mismatching them (D3 against C5) leaves a shallow, periodic landscape along a rotational coordinate. Second, it is the high-water mark of the **pre-diffusion, Rosetta-plus-parametric** toolchain applied to symmetric assemblies — worth reading directly against [[watson-2023-rfdiffusion]], which reaches comparable symmetric architectures from noise with far less hand-built machinery. Published in the same year as [[wicky-2022-symmetric-assembly-design]], with overlapping authorship, it shows the two approaches running in parallel rather than in sequence.

**Connections.**

- Uses the parametric backbone generation of [[huang-2014-parametric-helical-bundles]] and the HBNet interface machinery of [[boyken-2016-hydrogen-bond-network-oligomers]].
- Contemporaneous with [[wicky-2022-symmetric-assembly-design]] (shared authors, same lab, same year, opposite methodology).
- Superseded as a *generation* method — though not as a mechanical-design idea — by [[watson-2023-rfdiffusion]].
- **Supplement:** [[courbet-2022-axle-rotor-assemblies-supp]] — parametric sampling ranges, fusion protocols, symmetry-docking machinery.
- Concept: [[symmetric-assembly-design]]; chapter: [[symmetric-oligomer-design]].
