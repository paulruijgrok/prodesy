---
type: tool
tags: [enzyme-design, motif-scaffolding, flow-matching, atomic-motif, baker-lab]
sources: 6
updated: 2026-10-21
---

# RFdiffusion2

Baker-lab generative model for **atom-level functional site scaffolding**, introduced in [[ahern-2025-rfdiffusion2]]. It is the generator behind every de novo protease and metallohydrolase in [[enzyme-design]], and — fine-tuned — behind the de novo antibodies in [[bennett-2026-de-novo-antibodies]].

**What it changed.** [[watson-2023-rfdiffusion]] represents motifs as **indexed backbone frames**: each motif residue's N, Cα, C atoms as an element of SE(3), with a **prespecified sequence index**. That is adequate for scaffolding a contiguous domain and wrong for a theozyme, whose functional groups have unknown sequence positions and whose rotamers must be inferred — forcing **inverse rotamer sampling** as a workaround ([[ahern-2025-rfdiffusion2]]).

**Two mechanisms.**

- **Atomization.** Residues may be represented as a frame *or* as heavy atoms, so catalytic residues can be atomized and the network learns the distribution of their side-chain poses — which is how it can "forgo inverse rotamer sampling" ([[ahern-2025-rfdiffusion2]]).
- **Unindexed residues.** Modifying the index features yields residues whose sequence position is not revealed; with **no auxiliary losses** the network learns to superimpose them onto residues of the generated protein, so conditioning on an **unindexed motif** samples proteins containing the motif without being told where it sits. The supplement shows this is trained in by exposure — each residue is annotated unindexed with probability `P_IS_UNINDEXED` during training-example construction ([[ahern-2025-rfdiffusion2-supp]]).

Trained by **flow matching** rather than denoising diffusion, over a representation containing both atoms in ℝ³ and backbone frames in SE(3), with the SE(3) component following FrameFlow ([[ahern-2025-rfdiffusion2]]). Training filters out common solvents and crystallisation additives.

**Benchmark.** Introduced the **AME benchmark** — 41 active sites curated from PDB structures where all reactants and cofactors were present. **RFD2 solves all 41; previous methods solved 16** ([[ahern-2025-rfdiffusion2]]). AME is now the shared evaluation reported by [[butcher-2025-rfdiffusion3]], [[butcher-2026-rfdiffusion3-science]], [[didi-2026-complexa-scaling]] and [[lin-2026-genie3]].

**Experimental track record** ([[ahern-2025-rfdiffusion2]], each campaign under 96 designs): a retroaldolase at k_cat/K_M 6.34 ± 0.92 M⁻¹ s⁻¹ from the RA95.5-8F tetrad; a cysteine esterase at 248 ± 34 M⁻¹ s⁻¹ with a **helix-dipole-stabilised oxyanion hole** designed by including backbone atoms that force a helix terminus; and metallohydrolases detailed in [[kim-2026-metallohydrolases]], reaching 53,000 ± 5,000 M⁻¹ s⁻¹.

**RFD2-MI — a variant with no methods paper.** Both 2026 Nature protease campaigns use "RFD2 for molecular interfaces", optimised for enzyme *and* protein–protein interface design ([[choi-2026-cysteine-proteases]], [[chen-2026-metalloproteases]]). It is cited inconsistently: [[choi-2026-cysteine-proteases]] points to a phospho-tyrosine peptide binder preprint, [[butcher-2026-rfdiffusion3-science]] to the metalloprotease preprint. The wiki records this as a finding — the variant is described only in passing by its applications.

**Superseded, but not replaced in practice.** [[butcher-2026-rfdiffusion3-science]] moves from mixed frame/atom to **fully free-atom** diffusion and beats RFD2 on **37 of 41 (90%)** AME tasks with better Dunbrack rotamer quality. RFD2 nonetheless remains the generator of record for the published protease work, and a fine-tuned RFD2 is what designs antibodies in [[bennett-2026-de-novo-antibodies]].

**A cross-method caution.** [[braun-2026-riff-diff]] scaffolds the *same* RA95.5-8F retroaldolase tetrad by an enumerative artificial-motif-library route built on top of plain [[rfdiffusion]], and reaches **290 M⁻¹ s⁻¹** — roughly 45× RFD2's efficiency on that theozyme, from 36 designs rather than 96. Recorded as an open question in [[enzyme-design]] §10.

**Connections.** Successor to [[rfdiffusion]] and [[watson-2023-rfdiffusion]]; predecessor to [[rfdiffusion3]]. Pairs with [[proteinmpnn]] for sequence design and [[alphafold]]-family models plus PLACER for filtering. Concepts [[motif-scaffolding]], [[catalytic-site-design]]; chapters [[enzyme-design]], [[de-novo-binder-design]].
