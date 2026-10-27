---
type: source-supp
parent: "[[bennett-2026-de-novo-antibodies]]"
title: Atomically accurate de novo design of antibodies with RFdiffusion — Supplementary Information
pdf: "../sources/ProteinDesign/Bennett_Baker_Nature_2026_Atomically accurate de novo design of antibodies with RFdiffusion_Supp.pdf"
tags: [binder-design, antibodies, methods, training, datasets, filtering, benchmarks]
ingested: 2026-10-21
---

# De novo antibodies with RFdiffusion — Supplementary Information (companion)

129-page companion to [[bennett-2026-de-novo-antibodies]]. It is the wiki's most detailed account of **how a generative design model is fine-tuned for one modality**, and of the filtering thresholds that modality needs.

## What the SI contains (map)

**§1 — Datasets for training RFdiffusion and RoseTTAFold2:**

- **SAbDab**, the structural antibody database.
- A **TCR/MHC-peptide set** of crystal and AlphaFold2-predicted structures — notable because it is not antibody data, and because the paper's PHOX2B peptide–MHC campaign depends on it.
- **Loop-mediated interactions in the PDB** — a third, non-antibody dataset, which is the SI's clearest statement of what the model is actually being taught: not "antibodies" but *interfaces mediated by loops*.

**§2 — RFdiffusion fine-tuning:** noising and denoising, losses, **structure self-conditioning**, training procedure, dataset, a review of vanilla RFdiffusion fine-tuned on complexes (the baseline), **target templating**, and **hotspots**.

**§3 — RoseTTAFold2 fine-tuning:** datasets, **template provision**, losses, **sequence self-conditioning**, and **interface hotspots**.

**Supplementary figures** covering RF2 pAE-versus-RMSD calibration for VHH designs, ipTM distributions for design libraries across the four display targets, library structural analysis, the epitope-competition assays, and per-target success rates.

## Key extracted details

**The three training datasets are the design decision.** Training on SAbDab plus a TCR/MHC-peptide set plus general loop-mediated PDB interactions means the model's prior is over loop-mediated recognition broadly, not over antibodies specifically. That is why the same network can be pointed at a peptide–MHC complex, and it is a different generalisation claim from "fine-tuned on antibodies".

**Filter calibration is reported, with a threshold.** The SI gives an RF2 pAE-versus-RMSD comparison for VHH designs and states that at **mean pAE < 10, 80.3% of structures are within 2 Å when 100% of hotspots** are satisfied — i.e. the filter's precision is conditioned on hotspot satisfaction, not on confidence alone. This is the antibody-specific counterpart of the pLDDT/pAE_interaction ROC analysis in [[bennett-2023-binder-design-dl-supp]], and of the on-target constraint [[lin-2026-genie3]] had to add to its own benchmark after finding designs that passed while binding off-target.

**Framework conditioning is global-frame-invariant by construction.** §2's target-templating subsection is where the main text's key architectural claim is implemented: the framework is provided through the template track as a 2D matrix so that framework and target templates carry no relative position, leaving rigid-body placement to be designed. Supplementary Fig. 1a is the evidence that the framework is nonetheless accurately recapitulated.

**Both networks use self-conditioning, of different kinds** — structure self-conditioning in the generator (§2.3), sequence self-conditioning in the predictor (§3.4).

**Per-target success rates are tabulated** (Supplementary Methods Table 6), which is the source of the main text's "0% to 2%" range; and Supplementary Methods Table 10 carries the cryo-EM statistics for the 3.0 Å haemagglutinin complex.

## Connections

- Parent: [[bennett-2026-de-novo-antibodies]]; generator [[ahern-2025-rfdiffusion2]].
- Its hotspot-conditioned filter calibration is the direct analogue of [[bennett-2023-binder-design-dl-supp]] and of the AF2M+ on-target constraint in [[lin-2026-genie3]].
- Chapter: [[de-novo-binder-design]] §8.2, §10, §12.
