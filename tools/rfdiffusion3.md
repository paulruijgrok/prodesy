---
type: tool
tags: [diffusion, all-atom, baker-lab, frontier]
sources: 1
updated: 2026-07-13
---

# RFdiffusion3 (RFD3)

Baker-lab all-atom diffusion generator for proteins in the context of ligands, nucleic acids and metals — the efficiency-focused successor to [[rfdiffusion]] and RFdiffusionAA. Introduced in [[butcher-2025-rfdiffusion3]].

**Architecture.** Dual **token + atom** representation with **sparse attention** between them; a token-wise sparse transformer plus an **upsampling module** that predicts coordinate updates, jointly sampling backbone and side chains. Delivers prior-method quality at **~10× less compute**.

**Capabilities.** PPI, DNA-binder, small-molecule and atomic-motif-enzyme design; dedicated symmetric-design loop; tip-atom / atom-level conditioning for functional sites. See [[butcher-2025-rfdiffusion3-supp]]; concept [[diffusion-generative-design]].
