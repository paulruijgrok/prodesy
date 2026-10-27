---
type: concept
tags: [diffusion, generative, de-novo]
sources: 6
updated: 2026-07-13
---

# Diffusion generative design

Generating novel protein backbones (and complexes) by learning to reverse a noising process — the paradigm that now dominates de novo structure generation.

**Two independent demonstrations (2023).** [[watson-2023-rfdiffusion]] fine-tunes the RoseTTAFold predictor into a backbone denoiser, excelling at monomers, symmetric assemblies, motif scaffolding and binders. [[ingraham-2023-chroma]] builds a from-scratch diffusion model with a polymer-statistics-aware noise prior and programmable (including natural-language) conditioning. Different lineages, same conclusion: diffusion works for proteins.

**Convergence with prediction.** [[abramson-2024-alphafold3]] adopts a diffusion coordinate head for *prediction*, so prediction and design increasingly share machinery.

**Going all-atom.** [[krishna-2024-rosettafold-all-atom]]'s denoising fine-tune (RFdiffusionAA) diffuses protein backbones *around* a small-molecule ligand — extending diffusion design from protein-only to ligand-conditioned [[binder-design]] (validated for digoxigenin, heme, bilin).

**The non-diffusion alternative did not go away.** [[frank-2024-relaxed-sequence-optimization]] revives predictor inversion by running gradient descent through AlphaFold2 in a **relaxed** (continuous, PSSM-like) sequence space rather than MCMC over discrete sequences, handing only the converged backbone to [[proteinmpnn]]. It matches or beats [[watson-2023-rfdiffusion]] on designability and reaches **1000-residue** single chains with median TM 0.89, where RFdiffusion "faced challenges with producing viable backbones beyond 600 amino acids", at comparable GPU cost per success ([[frank-2024-relaxed-sequence-optimization]]). Diffusion still has the broader demonstrated coverage of point-group symmetries; the gradient route currently has the size advantage.

**Conditioning is the point.** The value is steerability — hotspots for binders, symmetry operators, fixed functional motifs, shape/semantic constraints. Backbones are then sequenced by [[sequence-design]] ([[proteinmpnn]]) and filtered by [[structure-prediction]].

**All-atom generation — three routes.** The field is now pushing past backbone-only generation: [[krishna-2024-rosettafold-all-atom]] atomizes ligands inside a predictor (RFdiffusionAA); [[chu-2024-protpardelle]] (Huang lab) makes side-chain generation intrinsic via a "superposition + collapse" scheme, codesigning sequence; and [[butcher-2025-rfdiffusion3]] uses a token+atom sparse architecture to hit prior quality at ~10× less compute across ligand/nucleic-acid/enzyme tasks. Its published successor [[butcher-2026-rfdiffusion3-science]] reframes the same model around **free-atom diffusion for atomic functional site scaffolding**, and backs it with zero-shot experimental enzymes — phosphotriesterases carrying a carbamylated lysine bridging two metals, and transthyretin-cleaving zinc proteases at 56/96 in-cis success.

**Open contrast to file:** fine-tuned-predictor (RFdiffusion) vs. bespoke correlated-noise prior (Chroma) vs. superposition all-atom (Protpardelle) vs. token+atom sparse (RFD3) — tradeoffs not yet resolved in these sources.

**Sources:** [[watson-2023-rfdiffusion]], [[ingraham-2023-chroma]], [[abramson-2024-alphafold3]], [[krishna-2024-rosettafold-all-atom]], [[chu-2024-protpardelle]], [[butcher-2025-rfdiffusion3]].

**A fourth independent arrival, and the only fully SE(3)-equivariant one.** [[lin-2023-genie]] diffuses Cα coordinates as a point cloud in the forward process and reasons over a cloud of **oriented Frenet–Serret frames** in the reverse process, an asymmetry chosen so that IPA's expressivity is available during generation without violating the Gaussian assumption of DDPMs. It reached 0.790 designability with **4.1 M parameters** against RFdiffusion's 0.951 at 59.8 M ([[lin-2023-genie]]). [[lin-2024-genie2]] then added SE(3)-invariant motif conditioning via Cα pairwise distance matrices — insensitive to initial motif placement, unlike fixed-coordinate conditioning — and was the first protein diffusion model trained on the AlphaFold Database, matching RFdiffusion's designability at 0.96 while far more diverse (0.91 vs 0.63) and novel (0.41 vs 0.26 PDB novelty). [[lin-2026-genie3]] extends the frames to sidechains. See [[genie]].
