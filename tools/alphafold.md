---
type: tool
tags: [structure-prediction, deep-learning, deepmind]
sources: 3
updated: 2026-07-10
---

# AlphaFold

DeepMind's protein structure predictor; the field-defining model and, in practice, the standard design oracle.

- **AF2** ([[jumper-2021-alphafold2]]) — MSA + pair (Evoformer) + structure module; atomic accuracy at CASP14; confidence via pLDDT/pTM/PAE.
- **AF3** ([[abramson-2024-alphafold3]]) — diffusion coordinate head; predicts protein/nucleic-acid/ligand/ion complexes in one model.

**As a design tool.** AF2 self-consistency (does the sequence fold to the intended structure? does it bind as designed?) is used as an *in silico* filter in [[bennett-2023-binder-design-dl]] and in the [[watson-2023-rfdiffusion]] pipeline.

**Related:** RoseTTAFold (parallel predictor, Baker lab; fine-tuned into [[rfdiffusion]]). See [[structure-prediction]].
