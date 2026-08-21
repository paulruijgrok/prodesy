---
type: tool
tags: [sequence-design, message-passing, baker-lab]
sources: 2
updated: 2026-07-10
---

# ProteinMPNN

Baker-lab message-passing network for fixed-backbone [[sequence-design]]. Introduced in [[dauparas-2022-proteinmpnn]].

**What it does.** Autoregressive N→C sequence prediction from backbone geometry only (Cα distances, frame orientations, dihedrals). ~52% native sequence recovery vs. ~33% for Rosetta, in seconds. Handles monomers, cyclic oligomers, nanoparticles, interfaces; supports tied/symmetric positions.

**Pipeline role.** Stage 2 (sequence) after backbone generation by [[rfdiffusion]] or [[chroma]]. Adopted in [[bennett-2023-binder-design-dl]] to replace Rosetta sequence design.
