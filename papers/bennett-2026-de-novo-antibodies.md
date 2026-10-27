---
type: source
title: Atomically accurate de novo design of antibodies with RFdiffusion
authors: Bennett, Watson, Ragotte, Borst, See, Weidle, Biswas, Yu et al. (Baker lab, with Liu, Melnyk, Sgourakis, Maris)
venue: Nature 2026 (649, 185–…; online 5 November 2025; doi 10.1038/s41586-025-09721-5)
pdf: "../sources/ProteinDesign/Bennett_Baker_Nature_2026_Atomically accurate de novo design of antibodies with RFdiffusion.pdf"
supp: yes
tags: [binder-design, antibodies, nanobodies, VHH, scFv, CDR, epitope-specific, cryo-em, affinity-maturation, orthorep, validation]
ingested: 2026-10-21
---

# Atomically accurate de novo design of antibodies with RFdiffusion

De novo antibodies — VHHs, scFvs and full IgGs — designed against **user-specified epitopes** entirely in silico, with cryo-EM confirming the designed conformations of **all six CDR loops** in one case. This is the paper whose absence made §8.2 of [[de-novo-binder-design]] a placeholder.

## Problem

Stated as a two-stage gap. Antibody development proceeds by (1) discovering antibodies that bind a specific epitope and (2) affinity maturation. Methods for **stage 1** "do not exist", so discovery relies on "animal immunization" or "screening of antibody libraries to identify candidate molecules that bind to a desired target, **followed by subsequent epitope mapping**" — i.e. the epitope is discovered after the fact rather than chosen. The consequence is that it is hard to obtain antibodies against the therapeutically relevant epitope.

Prior deep-learning work either sampled alternative *native* CDR loops to improve affinities, or used vanilla RFdiffusion, which was not built for the **loop-mediated, often β-strand-poor** interactions antibodies make with their epitopes. The paper lists the three requirements an ideal method must meet: target **any specified epitope on any target**; focus sampling on the **CDR loops while keeping the framework fixed** — so designs inherit a therapeutic framework; and sample **alternative rigid-body placements** of the antibody relative to the epitope.

## Approach

**A fine-tuned RFdiffusion, trained predominantly on antibody complexes.** During training the antibody structure is corrupted while the **framework sequence and structure are provided as conditioning**, so the framework can be specified at inference. Critically, the framework structure is supplied in a **global-frame-invariant** manner — via the RF2/RFdiffusion **template track** as a 2D matrix — so the framework and target templates **do not encode their relative positions**. That is what allows the rigid-body placement of the antibody against the epitope to be designed rather than assumed, while the framework's internal structure stays fixed. Target residues the CDRs should contact are specified as hotspots ("epitopes"). After diffusion, **ProteinMPNN** designs the CDR loop sequences.

**A separately fine-tuned RoseTTAFold2 as the filter.** Vanilla predictors were inadequate; RF2 was fine-tuned so that, given the target structure and epitope, it "must still correctly model the CDRs and find the correct" pose. The fine-tuned RF2 outperformed the models then available, "especially at CDR H3" — the longest and most variable loop, and the usual failure point.

**Framework:** the humanised VHH framework **h-NbBcII10FGLA** for the VHH campaigns.

## Key results

### VHH campaigns — and the success rate

Six targets: *C. difficile* **TcdB**, influenza **H1 haemagglutinin**, **RSV sites I and III**, **SARS-CoV-2 RBD** and **IL-7Rα**. Two screening modes — **9,000 designs per target by yeast surface display** (RSV I/III, RBD, haemagglutinin), or **95 designs per target** by *E. coli* expression and single-concentration SPR (TcdB, IL-7Rα, haemagglutinin, the last by both).

**Success rates against each target range from 0% to 2%.** That is the number [[de-novo-binder-design]] §12 needs, and it is an order of magnitude below the 19% that hotspot-conditioned miniprotein design achieves in [[watson-2023-rfdiffusion]] — a direct measure of how much harder loop-mediated interface design is.

Affinities from the initial computational designs are **tens to hundreds of nanomolar**:

- **Haemagglutinin:** best **K_d = 78 nM**, with others at 546, 698 and 790 nM.
- **TcdB:** the target epitope was the **Frizzled interface, for which no antibody or VHH exists in the PDB** — the cleanest possible test of epitope-directed design. Best VHH **K_d = 260 nM**; it **neutralised TcdB toxicity in CSPG4-knockout cells with EC50 = 460 nM**, and showed **no binding to the 70%-homologous *Paeniclostridium sordellii* toxin TcsL**.
- **SARS-CoV-2 RBD:** best **K_d = 5.5 µM**.

**Epitope targeting was verified competitively, not just by prediction.** For the best RBD and TcdB VHHs, binding was **completely abolished by addition of a previously characterised de novo binder to that epitope** — AHB2 (PDB 7UHB) for RBD, FZD48 (PDB 9CM5) for TcdB. The CDR loops are "distinct from VHHs observed in nature, indicating substantial generalization beyond the training dataset".

### Structural accuracy

**Cryo-EM of VHH_flu_01 bound to natively glycosylated trimeric influenza haemagglutinin** (A/USA:Iowa/1943 H1N1), at **3.0 Å**. One of four tested designs bound. Roughly **66% of haemagglutinin particles carried up to two VHHs per trimer** — partial occupancy attributed to the **N296 glycan**, which partially occludes the epitope in unbound subunits and reorients on binding.

The accuracy numbers: VHH approach angle closely matching the predicted model, **backbone RMSD 1.45 Å** to the RFdiffusion design, and **CDR3 RMSD 0.8 Å** — with specific designed residues (V100, V101, S103, F108) seen interacting with the haemagglutinin stem epitope as designed. The design is "highly dissimilar from the closest antibody–VHH binding to this epitope in the PDB".

### Affinity maturation, and scFvs

**OrthoRep** — orthogonal error-prone DNA replication for continuous in vivo hypermutation — was used to mature VHHs against TcdB, haemagglutinin and RBD, **improving affinities by approximately two orders of magnitude** and yielding single-digit nanomolar binders that retain the intended epitope selectivity. Cryo-EM of the *parent* design VHH_TcdB_H2 confirmed it engages the target Frizzled epitope.

**scFvs** were built by combining designed heavy- and light-chain CDRs into **combinatorial libraries of ~10 million theoretical complexity** (which worked, where fixed-pairing libraries did not). Results: **scFv5 K_d 460 nM** (380 nM as full-length IgG1) and **scFv6 K_d 72 nM** (68 nM as IgG1) against TcdB. Cryo-EM confirmed the binding pose for two distinct TcdB scFvs, with high-resolution data for one **verifying the atomically accurate design of the conformations of all six CDR loops**. A **PHOX2B peptide–MHC** complex was also targeted, giving modest affinity (400 nM by SPR).

## Significance / relation to the field

**It closes the hardest modality gap in the binder chapter**, and does so with the specificity controls that chapter says are usually missing: a target epitope with no prior antibody in the PDB, competition against a structurally characterised binder to the same site, non-binding to a 70%-homologous toxin, and functional neutralisation in a receptor-knockout cell line.

**The 0–2% success rate is the chapter's most important new number.** It quantifies the cost of the modality: the same lab's hotspot-conditioned miniprotein campaigns reached 19% ([[watson-2023-rfdiffusion]]), and [[stark-2025-boltzgen]] reports 66% of targets yielding nanomolar nanobodies from 15 tested — but from **60,000 generated**, a 4,000:1 ratio that this paper's 9,000-per-target display screening makes comparable in spirit. Read together, the three sources say that antibody-format design works and that its yield per design is roughly an order of magnitude below miniprotein design.

**It also shows what affinity maturation is still for.** Designs land at tens-to-hundreds of nanomolar; OrthoRep buys two orders of magnitude. So de novo design has replaced stage 1 (epitope-specific discovery) and not stage 2 (maturation) — which is precisely the division of labour the paper's opening sets up.

**Supplement:** [[bennett-2026-de-novo-antibodies-supp]].

**Filing note.** `sources/ProteinDesign/` also holds `Bennett_Baker_Nature_2025_…_supp.pdf`, an earlier copy of this paper's supplement from before publication. The 2026 main text and supplement supersede it; flagged for the next lint sweep.

## Connections

- Generator is a fine-tuned **RFdiffusion2** ([[ahern-2025-rfdiffusion2]]); filter is a fine-tuned RoseTTAFold2 ([[krishna-2024-rosettafold-all-atom]] lineage); CDR sequences by [[dauparas-2022-proteinmpnn]].
- The modality complement to [[stark-2025-boltzgen]]'s nanobody campaigns, which fix a framework and randomise CDR lengths; and to the CDR redesign capability noted in [[cho-2025-protein-hunter]].
- Its haemagglutinin and IL-7Rα targets overlap [[watson-2023-rfdiffusion]]; its RBD epitope overlaps [[gainza-2023-surface-fingerprint-binders]].
- Chapter: [[de-novo-binder-design]] §8.2 and §12. Concept: [[binder-design]].
