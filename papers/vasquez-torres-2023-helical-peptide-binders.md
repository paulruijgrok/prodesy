---
type: source
title: De novo design of high-affinity binders of bioactive helical peptides
authors: Vázquez Torres, Leung, Venkatesh et al. (Baker lab)
venue: Nature 2023
pdf: "../sources/ProteinDesign/VasquesTorres_Baker_Nature_2023_De novo design of high-affinity binders of bioactive helical peptides.pdf"
supp: yes
tags: [binder-design, peptides, partial-diffusion, biosensors, application]
ingested: 2026-07-13
updated: 2026-10-12
---

# De novo design of high-affinity binders of bioactive helical peptides

Applies the generative design stack to a hard, high-value target class: **flexible α-helical peptide hormones** (parathyroid hormone, glucagon, secretin, neuropeptide Y, GLP1, GIP, BH3 peptides), producing high-affinity binders and turning them into biosensors.

**Problem.** Many peptide hormones fold into an α-helix only upon binding their receptor; free in solution they are floppy. Designing binders to such conformationally heterogeneous targets — and detecting these hormones sensitively — was an unmet challenge that general binder design hadn't cracked.

**Approach.** Combines parametric generation with [[watson-2023-rfdiffusion]] and **partial diffusion** (noise an existing design partway, then denoise to refine/diversify while preserving the fold), then sequences with [[proteinmpnn]] and filters with [[alphafold]]2. Binders are built to clamp the peptide in its helical conformation.

**Key results** (figures extracted 2026-10-12; this section previously carried no numbers).

**The design problem, as the paper states it.** Peptide hormones such as PTH, NPY, glucagon (GCG) and secretin (SCT) adopt α-helical structure only on binding their receptors. Designing binders to them is hard for two compounding reasons: the picomolar-affinity hyper-stable 50–65-residue minibinders that work against folded proteins have shapes suited to convex or concave protein surfaces rather than to an extended helix; and peptides have **fewer residues available to interact with**.

**Three design generations, and the affinity they bought.**

1. **Parametric groove scaffolds.** 12 designs screened per target gave **8/12 binders each for PTH, GCG and NPY** — but at **micromolar** affinity only. Groove-shaped scaffolds can bind helical peptides; that alone is not enough.
2. **RFjoint Inpainting + ProteinMPNN redesign.** Extending the binder interface and redesigning it: of **192 designs tested, 44 bound PTH**; the best measured **6.1 nM** by fluorescence polarisation — about **three orders of magnitude** better than the parametric starting point, with the model showing 19% greater interface surface area. Specificity was high: little binding to PTHrP, a related peptide sharing 34% identity and the same receptor. A control matters here — **sequence redesign of the original interface with ProteinMPNN alone did not measurably increase affinity**, so the gain came from extending the interface, not from better sequence design. The same strategy gave **231 nM for GCG** and **3.5 µM for NPY** from 96 designs screened.
3. **De novo RFdiffusion from noise**, sequenced with [[proteinmpnn]] and predicted with AF2 using initial guess: sub-micromolar across the board, with **2.7 nM for SCT**, and **K_D < 100 nM for GLP1 and GIP**. A **7 nM** binder was obtained for the apoptosis-related **Bid BH3** peptide — which is unstructured in isolation — a *higher* affinity than Bid's native partner Mcl-1.

**Partial diffusion as a refinement operator.** Noising an existing design partway and re-denoising diversifies the fold by an amount set by the noise level, and "regularises" backbones so that ProteinMPNN sequence design on partially diffused backbones is more designable. Applied to the 231 nM GCG and 3.5 µM NPY inpainted binders, it gave **25/96 designs binding GCG and 20/96 binding NPY at 10 nM peptide** — and final affinities of **5.6 nM for NPY** and, for GCG, **below the limit of detection in the picomolar range**. The NPY binder showed **no cross-reactivity to peptide YY (PYY)**.

**Structural validation.** Crystal structures of the inpainted GCG binder at **1.95 Å** (0.72 Å RMSD to the design model) and the partially diffused GCG binder at **1.81 Å** (0.6 Å RMSD). A **Bim binder at K_D < 500 pM** — described by the authors as, to their knowledge, the highest-affinity designed peptide binders reported.

**Biosensors and diagnostics.** The 6.1 nM PTH binder was grafted into a luminescent caged-reporter architecture, giving **lucCagePTH with a 10 nM limit of detection and ~21-fold luminescence activation**. The picomolar PTH and GCG binders were conjugated to beads and used for **immunoaffinity enrichment of peptide hormones from human serum followed by mass-spectrometric detection**.

**Significance.** A capstone *application* of the batch-1 stack: shows the generate→sequence→filter pipeline plus **partial diffusion** extends [[binder-design]] to flexible, biomedically important targets, and that designed binders are directly useful as diagnostics.

**Connections.**

- Built on [[watson-2023-rfdiffusion]] (+ partial diffusion), [[proteinmpnn]], [[alphafold]]2 filtering.
- Application within [[binder-design]]; contrast with ligand-conditioned [[krishna-2024-rosettafold-all-atom]].
- **Supplement:** [[vasquez-torres-2023-helical-peptide-binders-supp]] — experimental methods (yeast display, SPR, biosensor assays).
- The flexible-target problem is pushed further, to intrinsically disordered regions, by [[stark-2025-boltzgen]].
- A modified RFdiffusion was trained here to design binders **to targets from sequence alone**, which is the capability [[cho-2025-protein-hunter]] later obtains without fine-tuning.
- Affinities here are by fluorescence polarisation, a third set of units alongside the BLI rates in [[watson-2023-rfdiffusion]] and the yeast-display SC50 bar in [[bennett-2023-binder-design-dl]]; see [[ruijgrok-2026-binder-pipeline-comparison]].
- `updated: 2026-10-12` — affinities, screening denominators and crystal structures extracted; see the revise entry in [[log]].
