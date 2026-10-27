---
type: source
title: "Fast and Ultra-Capable Protein Design: Advancing the Frontier Through Atomistic SE(3)-Equivariance with Genie 3"
authors: Lin, Lee, Vermani, Jiang, De Cooman, Špeťko & AlQuraishi (Columbia)
venue: bioRxiv 2026 (posted 2026-05-05; doi 10.64898/2026.05.01.722168)
pdf: "../sources/ProteinDesign/LinAlqurashi_bioRxiv2026_Fast and Ultra-Capable Protein Design- Advancing the Frontier Through Atomistic SE(3)-Equivariance with Genie 3.pdf"
supp: no
tags: [binder-design, diffusion, se3-equivariance, all-atom, motif-scaffolding, hotspots, benchmarks, compute, validation]
ingested: 2026-10-17
---

# Genie 3 — atomistic SE(3)-equivariance, and a generative model that beats hallucination

A diffusion model that **reverses two of the field's recent consensus moves at once** — it keeps SE(3)-equivariance where others abandoned it, and it beats hallucination with generation — then validates the claim with a 92 nM binder designed in a blind competition against a target with almost no structural characterisation.

**Appendices note.** `supp: no` because there is no separate SI file: Appendices A–E (architecture, training details, benchmarks, evaluation pipelines, per-problem results) are inside the same 48-page PDF, and the training-data figures below come from Appendix A.3.

## Problem

Two prevailing directions are both framed here as costly trade-offs.

- **All-atom models abandoned equivariance.** The field shifted toward non-SE(3)-equivariant architectures to capture sidechain conformations atomistically, "mirroring the evolution of AlphaFold2 to AlphaFold3" — paying away a data-efficient inductive bias to get all-atom detail.
- **Hallucination replaced generation.** Methods that directly optimise the *in silico* oracle in sequence space improve success rates but "reduce computational efficiency". The paper names **BindCraft** (Pacesa et al. 2024) as the current state of the art for binder design and states its two limitations plainly: the oracle it optimises "does not necessarily reflect experimental reality", and iterating an expensive structure predictor gives "possibly intractable generation times for difficult targets".

## Approach

**Branched-polymer frames.** The frame-based representation of [[lin-2024-genie2]] is retained and generalised to the branched-polymer nature of a protein. Backbone: Frenet–Serret frames anchored at Cα atoms relative to the FS frames of preceding Cα atoms. Sidechains: starting from the backbone FS frame, subsequent sidechain FS frames are constructed in the predefined `atom14` ordering. This is what buys atomistic detail *without* giving up equivariance.

**Partial atomization.** All-atom representations for *known* segments (motif residues) and backbone-only for scaffold residues — so the model is all-atom exactly where sidechain information exists and backbone-only elsewhere. During training, motif sidechain atoms are occasionally masked and the model must reconstruct them from the motif sequence and, optionally, motif Cα coordinates.

**Denoiser.** An SE(3)-invariant input embedder supporting optional sequence and structure conditions, a trunk, and an **SE(3)-equivariant structural decoder** using Invariant Point Attention to update single representations and thence the input reference frames; noise vectors are the displacement between updated and input frame translations. Variance schedule T = 1000.

**Low-temperature sampling by directional scaling.** Genie 2 moderated the reverse process through the noise scale γ (controlling variance); Genie 3 moderates it through a **direction scale η** (controlling the reverse mean), with σ̄²_t = σ²_t, γ = 1 and **Δt = 10**. Setting Δt = 10 cuts sampling from 1,000 steps to **100 — a 10× reduction in sampling time with negligible impact on generative quality**. This directly answers the limitation [[lin-2024-genie2]] stated against itself: 1,000 denoising iterations against 100 for FrameFlow, 500 for Chroma and 50 for RFdiffusion. The paper also offers a hypothesis for why protein models need low temperatures at all, which no other ingested source addresses: many PDB and AFDB structures are "too flexible—owing to their evolved origins—to be reliably designed by current generative models", so lowering the temperature selects for more rigid and therefore more predictable proteins.

**Hotspot expansion heuristics**, both new here. *Extended hotspots*: treat any target **surface** residue within 6 Å (Cβ–Cβ) of any user hotspot as interface, where surface means relative solvent accessibility ≥ 0.25 and SASA ≥ 10 Å². *Convergent hotspots*: start from the user's hotspots, then add interface residues found in the **intersection of all successful designs** from previous design cycles. Extended is used for monomeric targets, convergent for multimeric (seeded by a first round of 100 structures).

## Training — and the 256-residue ceiling

Multi-task, **9:1 motif-scaffolding to binder-design**. 48 × Nvidia A100 40 GB for ~15 days, **600,000 steps**, per-GPU batch size 1 for an effective batch of 48, Adam at lr 1e-4.

**Nothing in training exceeds 256 residues.** Both datasets are capped, and the main text states the consequence twice.

- **Monomeric / motif-scaffolding data** — the same dataset as [[lin-2024-genie2]]: FoldSeek-clustered AlphaFold Database representative clusters, filtered to sequences **between 20 and 256 residues inclusive** with minimum pLDDT 80, giving **587,479 structures** (note: Genie 2 reports 588,570 for the same dataset — a 1,091-structure discrepancy neither paper explains). Note also that **"we do not use any experimentally determined monomeric structures"** — the monomer half of training is entirely predicted structures. Three motif-scaffolding task variants by how much motif information is conditioned on: sequence + backbone + sidechain (ratio 0.4), sequence + backbone (0.4), sequence only (0.2); motif selection follows Algorithm 1 of [[lin-2024-genie2]].
- **Multimeric / binder data** — the training split of **Pinder 2024-02**, further filtered to remove structures with missing residues and atoms, and with **the maximum number of residues in a complex capped at 256**. Result: **135,745 structures across 5,331 interface clusters**. Sampling is interface-cluster-first then within-cluster, to equalise representation at the interface level; one chain is randomly designated target and the other the ground-truth binder; interface is Cβ–Cβ within 8 Å, with the interface mask randomly masked at 50%. Five binder-design task variants by how much target and binder information is conditioned on.

The cap on the multimeric side is on the **complex**, target plus binder together, so individual chains in binder training are necessarily well below 256 residues.

**The ceiling is inherited, not new.** [[lin-2023-genie]] already trained its long models at a 256-residue maximum, and [[lin-2024-genie2]] states the reason — "due to computational constraints, we limit sequence length to 256 during training; however, Genie 2 is capable of generating proteins longer than 256 residues" — attributing the cost to the O(N³) triangular multiplicative update layers inherited from AlphaFold2. All three generations are capped at 256 and all three claim generalisation past it.

**The paper leans on this ceiling as evidence, in two places.** On long monomers: *"Genie 3 is only trained on structures up to 256 residues in length; its long monomer performance thus demonstrates out-of-domain generalization."* On large complexes: *"Combined with the fact that Genie 3's multimeric training dataset is restricted to complexes shorter than 256 residues, our architectural changes appear to be critical for generalization to larger complexes."*

**A small internal inconsistency**, recorded not resolved: Appendix A.3.2 says the cap is applied by "cap[ping] the maximum number of residues in complexes **to** 256" (i.e. 256 inclusive), while §4.4's discussion says the dataset is "restricted to complexes **shorter than** 256 residues". One residue of ambiguity; the monomeric filter is unambiguously inclusive of 256.

## Key results

**Unconditional generation.** Lengths 50–250 (short) and **300–800 (long)**, 100 structures per length per method, successful designs structurally clustered at TM-score 0.5 to count unique clusters. Genie 3 is comparable to or better than Ambient and La-Proteina below 300 residues and **exceeds them above 300** — the out-of-domain claim, given the 256-residue training ceiling. The ablation locates the credit: sampling modifications give the largest gains across all lengths, while the architectural and training modifications "only impact designs longer than 700 residues in length".

**Motif scaffolding (MotifBench).** Genie 3 **solves as many problems as the best other method (Protpardelle-1c) while achieving a higher MotifBench score** — the benchmark's diminishing-returns scoring favours models that solve harder problems. The problems it solves are *not* the same ones other methods solve, which the authors read as complementarity rather than dominance.

**Binder design — 10 problems from the AlphaProteo set** ([[didi-2026-complexa-scaling]] uses the same Zambaldi et al. 2024 convention), 6 monomeric and 4 multimeric, from BH3 helix (easy) to TNFα (hard). Fixed budget of **200 generated structures per model per problem**, 8 ProteinMPNN sequences each, with inference-time search disabled for Proteína-Complexa.

- **Genie 3 produces the most successful designs on 7 of 10 problems; BindCraft on the remaining 3.** Both "substantially outperform RFDiffusion, BoltzGen, and Proteina-Complexa".
- *"Despite training only on dimers, Genie 3 solves multimeric design problems as well as it does monomeric ones, suggesting generalization beyond its training set."*
- **Normalised by per-sample runtime, the gap over BindCraft widens** — the paper's central efficiency claim, that a generative model can outperform "a far more expensive hallucination-based model".
- **Inference-time scaling against Proteína-Complexa** across the same 10 problems: Complexa wins 1, ties 2, loses 7; **in 4 instances Complexa exhibits no scaling behaviour at all** while Genie 3 improves robustly with compute. The gains are concentrated in multimeric targets (3 of 4).
- **Hotspot heuristics both help**, and convergent hotspots are substantially better for multimeric targets (VEGF-A, H1, IL-17A, TNFα). Applied iteratively to TNFα — the hardest target — success rate climbs **nearly monotonically with design round**, which the paper offers as inference-time scaling in Genie 3.

**Two findings about oracles that belong in any discussion of filtering.**

1. **The oracle's precision ceiling is 12%.** "All evaluation pipelines exhibit low precision (maximum of 12%) and completely fail to identify binders against H3, TGFβ, and TIE2." The authors state the implication directly: this "place[s] a low ceiling on the efficiency of binder design using *in silico* oracles as filters."
2. **Standard oracles are blind to *where* a binder binds.** Two designs passed the AF2M Benchmark while binding an **off-target site**. The fix is the **AF2M+ Benchmark**, which adds the constraint that **≥80% of user-specified interface residues lie within 5 Å of the binder** (by closest heavy atoms) for interfaces of 4 or more residues, and 100% for interfaces of 3 or fewer. All downstream analyses use it.

**Hotspot fidelity separates generation from hallucination.** For H1 and IL-17A, "a sizable proportion of otherwise successful BindCraft designs fail to bind the specified interface." The mechanism offered is architectural rather than incidental: in hallucination, hotspot compliance is "an additional ad hoc loss term that is optimized during hallucination", whereas in generation hotspots "are provided as inputs to the model during training and generation, resulting in a shift in the underlying distribution of the generative process towards compliant designs."

**The Nipah competition — a blind, third-party-scored result.** Entered into AdaptyvBio's challenge to design binders against **Nipah virus Glycoprotein G (NiV-G)**, a tetramer with minimal structural or biophysical characterisation. The interface was constrained using the NiV-G:Ephrin-B2 crystal structure (**PDB 2VSM**) to residues within 8 Å of Ephrin-B2. From **200 designs**, AF2M+ selected **34 successes spanning 33 unique structural clusters** (TM-score > 0.6); candidates were ranked by **Boltz-2 ipSAE** and the top **8** submitted. **All 8 expressed, and one gave a measurable K_D of 92 nM — a 1/8 (12.5%) hit rate.** Measurement was SPR, with Twin-Strep-tagged designs made by cell-free expression, immobilised on Strep-Tactin XT chips, against recombinant NiV-G residues 71–620.

For reference, aggregate hit rates in the same competition were **RFdiffusion 3/60, BindCraft 1/100, BoltzGen 2/288** — though the authors caveat that these "encompass diverse generation and filtering procedures performed by groups with varying levels of expertise, and may thus not be representative of their corresponding models' performance in a controlled experimental setting."

**Stated limitations.** The assessments depend on *in silico* pipelines that depend on imperfect predictors whose inability to score protein–protein complexes is "well known". And Genie 3, like other generative binder models, "assume[s] that target structures accurately reflect the conformation of the bound state, which ignores induced fit effects" — with designing against unknown conformations named as a key future direction, possibly via MSA subsampling, BioEmu or ConforNets.

## Significance / relation to the field

**It reopens a question the chapter had treated as settled.** [[de-novo-binder-design]] §11 presents the generative-versus-hallucination split as dissolved by [[didi-2026-complexa-scaling]] and [[cho-2025-protein-hunter]], both of which answer it by *combining* the two. Genie 3 answers it differently and more bluntly: a pure generative model, with no inference-time oracle optimisation in the loop, beats the hallucination state of the art on 7 of 10 problems and widens the gap once runtime is accounted for. Taken together with its SE(3) result, the wiki's reading is that the field's recent architectural consensus — drop equivariance, adopt hallucination — was adopted faster than it was tested.

**It is the chapter's first head-to-head of five binder methods under one protocol.** Genie 3, BindCraft, RFdiffusion, BoltzGen and Proteína-Complexa, at a fixed 200-structure budget on a shared 10-problem set with a shared evaluation pipeline. §12 of [[de-novo-binder-design]] argues that no cross-method comparison of binder success rates is currently sound; this is the closest thing to a counterexample the wiki holds, and it is still an *in silico* comparison with a 12%-precision oracle.

**It gives BindCraft a second secondary source, with numbers.** [[bindcraft]] remains primary-sourceless, but this paper supplies its competitive position (best on 3 of 10 problems, beaten on 7), its cost disadvantage under runtime normalisation, its named weakness (hotspot infidelity on H1 and IL-17A), and a competition hit rate of 1/100.

**And it supplies the chapter's sharpest statement of the oracle ceiling.** A maximum precision of 12% with complete failure on three targets is a more damaging number than anything in [[bennett-2023-binder-design-dl-supp]]'s ROC analysis, and the AF2M+ on-target constraint is the first ingested instance of a filter being fixed *because* it was found to pass off-target binders — the published counterpart of the gate pathologies measured in [[ruijgrok-2026-binder-pipeline-comparison]].

**Relation to this project.** Genie 3 is not among the nine pipelines in [[ruijgrok-2026-binder-pipeline-comparison]], and its 256-residue training ceiling is directly relevant to that project's targets: the PfLDH 4b7u system is recorded there as a 632-residue target in a 711-residue complex, i.e. **roughly 2.8× the largest complex Genie 3 ever saw in training**. The paper's own out-of-domain claims are about unconditional monomers to 800 residues and the AlphaProteo multimers, not about targets of that size, so the generalisation would be an extrapolation beyond what it demonstrates.

## Connections

- Third in the lineage: [[lin-2023-genie]] (the founding frame asymmetry) → [[lin-2024-genie2]] (motif scaffolding, AFDB augmentation, the training set reused here) → this paper. Its 10× sampling speed-up answers a limitation Genie 2 stated against itself.
- The direct competitor of [[bindcraft]] and the paper that measures it; also benchmarks against [[watson-2023-rfdiffusion]], [[stark-2025-boltzgen]] and [[didi-2026-complexa-scaling]].
- Shares the AlphaProteo 10-problem evaluation convention with [[didi-2026-complexa-scaling]]; both derive success criteria from Zambaldi et al. 2024.
- Its partial atomization is a third route to all-atom design alongside [[krishna-2024-rosettafold-all-atom]] (atomize-in-predictor), [[chu-2024-protpardelle]] (superposition) and [[butcher-2025-rfdiffusion3]] (token+atom) — and the only one that keeps SE(3)-equivariance.
- Beats [[chu-2024-protpardelle]] on MotifBench score while tying on problems solved; relates to [[motif-scaffolding]].
- Uses [[dauparas-2022-proteinmpnn]] for inverse folding and [[jumper-2021-alphafold2]]-family predictors as oracles; its hotspot machinery extends the conditioning of [[watson-2023-rfdiffusion]] and is grounded biophysically by [[halperin-2004-interface-hot-spots]].
- Its 12% oracle-precision ceiling and off-target-passing finding bear on the filtering discipline of [[bennett-2023-binder-design-dl]] and the gate pathologies in [[ruijgrok-2026-binder-pipeline-comparison]].
- Concept [[binder-design]]; chapter [[de-novo-binder-design]] §5, §7, §10, §11, §12. Tool page [[genie]].
