---
type: concept
tags: [parametric-design, coiled-coils, repeat-proteins, crick-equations, rosetta]
sources: 7
updated: 2026-08-24
---

# Parametric design

Generating protein backbones from a **closed-form geometric description** — a handful of numbers fed to a set of equations — rather than by sampling fragments, docking known structures, or denoising noise.

**Why it works only for some folds.** The challenge is reducing a 3D fold to parametric equations that still capture its salient features, and that is currently possible for a **subset of proteins: repeat proteins** ([[wood-2018-ccbuilder]]). The reason is structural rather than technical — a shape built by applying one rigid-body transform repeatedly is fully described by the few parameters of that transform. This is the conceptual link between [[parametric-design]] and [[repeat-protein-design]], and it is why the α-helical coiled coil, a repeat class making up an estimated 3–5% of protein-encoding DNA, has been the fold where the approach has paid off ([[wood-2018-ccbuilder]]).

**The parameters.** For a coiled coil the description is **Crick's, from 1953**: supercoil radius R0 and twist ω0, superhelical phase φ0, helical radius R1, twist ω1, phase φ1, axial offset Δz, and pitch angle α = arcsin(R0ω0/*d*). In practice *d* and R1 are **fixed at ideal α-helix values (2.26 and 1.51)** and the rest are sampled, which is what keeps the search low-dimensional ([[huang-2014-parametric-helical-bundles-supp]]). Supercoil and helical twist are coupled: successive Cα atoms rotate by ≈ (ω0 + ω1), and the backbone is strained when that departs from the ~100° of an ideal helix ([[huang-2014-parametric-helical-bundles]]).

**Symmetry is free.** For an *n*-helix bundle the superhelical phase simply takes the values {0, 2π/n, 4π/n, … 2(n−1)π/n}. **Cyclic symmetry is therefore exact by construction** — a property of the coordinate generator, never optimized for and never verified afterwards ([[huang-2014-parametric-helical-bundles-supp]]). This is the sharpest contrast in the wiki with symmetry as a rewarded objective ([[wicky-2022-symmetric-assembly-design]]) or as a projection applied during sampling ([[watson-2023-rfdiffusion]]); see [[symmetric-oligomer-design]] §7.

**The workflow.** Sample the parameters on a grid, generate backbones, run Rosetta sequence design at each grid point, refine the grid near the lowest-energy parameter sets, connect helices with loop modelling for monomeric targets, and filter with structure prediction before synthesis ([[huang-2014-parametric-helical-bundles]]). Interfaces can be given specificity independently, by installing buried hydrogen-bond networks into the repeating cross-section ([[boyken-2016-hydrogen-bond-network-oligomers]]).

**What it delivered.** Hyperstable designs with **extrapolated ΔG_fold > 60 kcal/mol** and crystal structures matching in core packing, including a C5 bundle ([[huang-2014-parametric-helical-bundles]]); α-helical barrels at **C5, C6 and C7** with chemically defined channels whose diameters track oligomer state ([[thomson-2014-alpha-helical-barrels]]); and, pushed to its limit, the D2–D8 axles and C3–C8 rotors of [[courbet-2022-axle-rotor-assemblies]].

**Its two limits.** Expressivity — only folds the parameterization can write down, in practice helical bundles and barrels ([[wicky-2022-symmetric-assembly-design]] notes parametric bundles were the sole exception to the rule that protomer structure had to be specified in advance). And labour — reaching a D3 axle required hand-chosen dual superhelical radii (6 Å and 12 Å) over a ~5 Å range in 0.5 Å bins, phase swept 0°–90° in 10° steps, *z*-offsets in 0.1 Å steps, and per-symmetry linker design ([[courbet-2022-axle-rotor-assemblies-supp]]).

**It is not obsolete.** [[wood-2018-ccbuilder]] makes the approach browser-accessible with force-field optimization, extending to α-helical barrels and collagen triple helices, and notes the parameterization also runs *backwards* — fitting Crick parameters to solved structures. Parametric generation remains the only route here where the symmetry error is identically zero.

**Related:** [[repeat-protein-design]] (why parameterization is possible at all) · [[symmetric-assembly-design]] · tool [[ccbuilder]] · chapter [[symmetric-oligomer-design]].

**Sources:** [[harbury-1993-coiled-coil-oligomer-switch]], [[huang-2014-parametric-helical-bundles]], [[thomson-2014-alpha-helical-barrels]], [[boyken-2016-hydrogen-bond-network-oligomers]], [[wood-2018-ccbuilder]], [[courbet-2022-axle-rotor-assemblies]], [[brunette-2015-repeat-protein-universe]].
