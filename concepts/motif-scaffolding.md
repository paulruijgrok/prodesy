---
type: concept
tags: [motif-scaffolding, functional-site, de-novo]
sources: 3
updated: 2026-07-13
---

# Motif scaffolding (functional-site design)

Building a full protein *around* a fixed functional site — an enzyme active site, a metal/ligand pocket, a binding or epitope motif — so the site is held in its active geometry. The second half of functional de novo design (the first half being: obtain the motif geometry).

**Two generations of method.**

1. **Hallucination & inpainting** — [[wang-2022-functional-site-scaffolding]] introduced both: *constrained hallucination* (optimize a sequence until the network folds it to contain the motif) and *inpainting/RFjoint* (one forward pass fills sequence+structure around the motif). Flexible vs. fast. The unconstrained hallucination engine both build on comes from [[anishchenko-2021-hallucination]], which anticipated this application — noting that because the network hallucinates plausible structures from scratch, no scaffold blueprint need be specified in advance, and the loss can be generalized to include binding motifs or catalytic sites.
2. **Conditional diffusion** — [[watson-2023-rfdiffusion]] generalizes these: conditional training scaffolds motifs by denoising (see [[watson-2023-rfdiffusion-supp]] §3.2), with higher success and diversity. [[butcher-2025-rfdiffusion3]] extends to **atomic** motifs (tip-atom conditioning; the AME enzyme benchmark), and [[chu-2024-protpardelle]] scaffolds motifs **backbone- and rotamer-free** in all-atom space.

**Common pattern.** Motif in → scaffold out → sequence with [[proteinmpnn]] → filter with [[alphafold]]2/self-consistency.

**Sources:** [[wang-2022-functional-site-scaffolding]], [[watson-2023-rfdiffusion]], [[butcher-2025-rfdiffusion3]] (and all-atom variant [[chu-2024-protpardelle]]).

**Conditioning without fixing coordinates.** [[lin-2024-genie2]] encodes a motif as one-hot sequence features plus the **pairwise distance matrix of its Cα atoms**, which is SE(3)-invariant and therefore — unlike the fixed-coordinate conditioning of [[watson-2023-rfdiffusion]] and FrameFlow — insensitive to the motif's initial placement. Specifying intra-motif but not inter-motif distances yields **multi-motif scaffolding** as an inference-time choice: Genie 2 solves 4 of 6 curated multi-motif tasks without ever training on one. On the 24-task single-motif benchmark it equals or beats RFdiffusion in unique successes on 22 tasks. That paper also argues *success rate* is the wrong metric, because mode collapse inflates it, and reports **unique successes** after TM-score 0.6 clustering instead ([[lin-2024-genie2]]).

**Atomic motifs, and the sequence-position problem.** The step that made de novo proteases possible is conditioning on **active-site atoms without specifying where along the sequence the catalytic residues sit** — the contribution of [[ahern-2025-rfdiffusion2]], which does it two ways: residues may be represented as a frame *or* as atomized heavy atoms (so rotamers are inferred rather than enumerated), and **unindexed residues**, whose sequence position is withheld, are learned with no auxiliary loss to superimpose onto generated residues. It solves **all 41 cases of the AME benchmark it introduces, against 16 for prior methods**. Used via its molecular-interfaces variant RFD2-MI in [[choi-2026-cysteine-proteases]] and [[chen-2026-metalloproteases]].

**The enumerative alternative.** [[braun-2026-riff-diff]] solves the same problem without retraining a generator: embed each catalytic residue in a helical fragment, **invert rotamers** to fix functional groups while varying backbone positions, search all non-clashing fragment combinations, and rank by rotamer probability and PDB abundance — then scaffold the resulting artificial motif with plain [[rfdiffusion]]. It also adds a **placeholder helix** at the pocket position, which the denoising trajectory is centred on and which is deleted afterwards, because RFdiffusion's substrate potential "failed to promote the formation of well-defined substrate binding pockets" ([[braun-2026-riff-diff]]). On the one shared theozyme, the enumerative route reached ~45× the catalytic efficiency. [[butcher-2026-rfdiffusion3-science]] then moved to **free-atom diffusion**, where conditioning tokens correspond only to the atoms actually fixed rather than to whole catalytic residues, and reports outperforming RFD2 on **37 of 41 (90%)** atomic motif enzyme benchmark tasks from the M-CSA, with better Dunbrack rotamer quality. Full treatment in [[enzyme-design]] §3.

**A standing objection.** [[elnesr-2026-zero-shot-metalloenzyme]] argues that scaffolding a motif is not sufficient for function: "optimizing for the motif alone does not guarantee catalytic competence", because second-shell residues mediate affinity, specificity and reactivity. Its alternative — optimising the coordination environment directly — produced the highest rate enhancement reported for a de novo hydrolase. See [[enzyme-design]] §7.
