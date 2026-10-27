---
type: source
title: Atomic functional site scaffolding in biopolymers with RFdiffusion3
authors: Butcher, Krishna, Mitra, Woodbury, Kim et al. (Baker lab)
venue: Science 2026 (first release 15 October 2026; doi 10.1126/science.aeh2982)
pdf: "../sources/ProteinDesign/ButcherBaker_Science_2026_Atomic functional site scaffolding in biopolymers withRFdiffusion3.pdf"
supp: yes
tags: [enzyme-design, motif-scaffolding, all-atom, diffusion, rna-design, metalloenzyme, protease, validation]
ingested: 2026-10-21
---

# RFdiffusion3 — atomic functional site scaffolding in biopolymers

The **published** RFdiffusion3 paper, and a substantially different work from the preprint already in the wiki. Where [[butcher-2025-rfdiffusion3]] was framed as "de novo design of all-atom biomolecular interactions", this is framed around **atomic functional site scaffolding** and carries the experimental enzyme validation the preprint lacked: zero-shot phosphotriesterases with a carbamylated lysine bridging two metals, and zinc proteases that cleave transthyretin.

**Relation to the preprint.** Both are retained. The bioRxiv version ([[butcher-2025-rfdiffusion3]]) remains the wiki's source for the benchmark suite and the efficiency claim; this page is the citable published version and the source for everything experimental. Where the two disagree or differ in emphasis, this page is authoritative.

## Problem

Catalytic and other sophisticated biomolecular functions "arise from the placement of many atoms in three-dimensional space", and the paper's argument is that the field's representations have not matched that requirement. Most methods, including RFdiffusion ([[watson-2023-rfdiffusion]]) and BindCraft ([[bindcraft]]), **represent proteins at the amino-acid level**, which "suffices for designing protein monomers, assemblies, and protein-binding proteins, but lacks the resolution to specify enzyme active sites and other functional sites at the atomic level". RFdiffusion2 partly addressed this by conditioning residue-level diffusion on a few catalytic side-chain atoms, but because diffusion remained at the residue level it "is incapable of creating additional side chain interactions with ligands".

## Approach

**Free-atom diffusion.** RFD3 diffuses at the atomic level throughout, in a single unified framework covering proteins, RNA and small molecules. Architecturally it uses **168 M trainable parameters** (against ~350 M for a named comparator), and introduces **recycling at each diffusion step** — inspired by the AlphaFold recycling mechanism in the Pairformer — to increase effective compute without increasing parameter count. Training uses the **AtomWorks** dataloading framework and supplements experimental structures with high-quality AlphaFold2 and RoseTTAFold3-predicted RNA structures.

**Unindexed atomic motif scaffolding.** For catalytic sites, the backbone coordinates and sequence positions of catalytic residues "are generally not specified in advance", so the method must **jointly infer the scaffold structure, the catalytic side-chain rotamers, and the sequence positions** from minimal atomic constraints. RFD2 did this by representing the *full* catalytic residue in order to identify backbone positions; in RFD3 an extra token is appended per catalytic residue and **the atomic motif conditioning tokens correspond only to the atoms actually being fixed**, with the model trained to overlap a diffused protein or RNA atom with each atom in the provided motif.

## Key results

**Atomic motif enzyme (AME) benchmark**, drawn from the **Mechanism and Catalytic Site Atlas (M-CSA)**, where difficulty rises with the number of catalytic motif islands:

- RFD3 **outperforms RFD2 on 37 of 41 (90%) tasks**, with the improvement concentrated on the harder problems.
- On four six-residue active sites — an aldolase, ornithine decarboxylase, glycosidase and phosphotriesterase — RFD3 generated **more designs whose active-site residues were recapitulated to within 1.25 Å after refolding**, in all four cases.
- Rotamer quality, scored by a **backbone-dependent Dunbrack rotamer probability loss** (loss < 1 meaning more native-like), is **consistently better for RFD3 than RFD2**.

**Symmetric enzyme complexes.** Because many native enzymes are obligate oligomers whose symmetry is catalytically relevant, symmetry was enforced during generation and tested on **15 C2-symmetric AME cases**. RFD3 produced physically plausible symmetric designs with consistent catalytic-residue alignment across subunits in all 15, "even in challenging cases involving up to seven catalytic residues per subunit" — connecting this chapter to [[symmetric-oligomer-design]].

**Mixed protein/RNA active sites.** Because RFD3 generates both nucleic acid and protein structure, atomic motif scaffolding extends to active sites with catalytic contributions from both — demonstrated on the RNase P RNA-cleaving active site, which uses amino-acid side chains and RNA bases together.

### The two experimental campaigns, both zero-shot at 96 constructs

**Phosphotriesterases (ZAPP series).** The target is organophosphate hydrolysis; native phosphotriesterases use **six catalytic residues coordinating two metal ions, including a post-translationally carbamylated lysine that bridges the metals** — an unusually demanding active site because it requires a post-translational modification to be installed correctly. Histidine variants of a phosphotriesterase theozyme were enumerated and scaffolded by RFD3.

- **96 designs expressed in *E. coli*; 4 active, all from the same base RFD3-generated scaffold.**
- The most active, **ZAPP-1**, performs **multiple-turnover catalysis** with **k_cat = 0.015 ± 0.003 s⁻¹** and **k_cat/K_M = 2.0 ± 0.6 M⁻¹ s⁻¹**.
- Carbamylation is load-bearing and was tested: its removal gave an **11-fold decrease in k_cat and a 4-fold decrease in k_cat/K_M**, confirming the designed modification participates in catalysis.
- A second round characterised the top 7 hits across **4 distinct scaffolds**; **ZAPP-2** reached k_cat = 0.023 ± 0.006 s⁻¹, k_cat/K_M = 4 ± 3 M⁻¹ s⁻¹ and a rate enhancement **k_cat/k_uncat of (5 ± 2) × 10⁵**. ZAPP-1 through ZAPP-5 span distinct scaffolds and catalytic-residue arrangements.

**Transthyretin-cleaving zinc proteases (TTRg series).** The substrate is **PAINVAVHVF**, the sequence forming the longest β-strand in the core of the TTR amyloid fibril (PDB 8GBR); TTR misfolding causes systemic amyloidosis with polyneuropathy, cardiomyopathy and renal failure. The theozyme merged catalytic residues from **aminopeptidase N (PDB 4QHP)** with substrate backbone atoms at P1 and P1′ plus stabilising protease backbone atoms taken from an AF3 prediction of the astacin–substrate complex. RFD3 simultaneously scaffolded the catalytic residues, **determined the substrate conformation**, and generated a customised active-site cleft for the prescribed sequence.

- **96 designs; 56 (58%) showed >10% cleavage in cis** after 18 h at 37 °C by SDS–PAGE.
- The best, **TTRg11**, cleaved the majority of substrate within 1 hour in a FRET assay, with mass spectrometry confirming cleavage at the designed site.
- **Specificity:** tested against six further β-amyloidogenic sequences all with substantial β-strand propensity, TTRg11 was much more active on its cognate substrate.
- **Zn(II)-dependent**, with kinetics **k_cat 0.072 ± 0.008 s⁻¹, K_M 70 ± 10 µM, k_cat/K_M 1100 ± 300 M⁻¹ s⁻¹** — as a one-shot design with no experimental optimisation, placing it "within the range (although at the low end) of native proteases with well-characterized biological functions".

The paper states the advance over RFD2-era protease design in two parts: **the very high in-cis success rate (56 of 96)** and **activity on natural peptide-derived substrates** rather than synthetic substrates optimised for cleavability by two-sided design.

## Significance / relation to the field

**This is the paper that makes enzyme design a chapter rather than a section.** Together with [[choi-2026-cysteine-proteases]] and [[chen-2026-metalloproteases]] it establishes that de novo amide-bond hydrolysis works, and it supplies the *method* half of that story where the other two supply the biochemistry.

**It also makes an architectural argument the wiki should hold alongside [[lin-2026-genie3]]'s.** Both papers published within days of each other claim that representation choice is what gates functional design, and reach opposite conclusions about equivariance: RFD3 abandons it for free-atom diffusion; Genie 3 keeps it via branched-polymer frames. Neither benchmarks against the other on enzymes. See §13 of [[enzyme-design]].

**The two campaigns are the wiki's cleanest demonstrations of two different hard things.** The phosphotriesterase work shows a **post-translational modification** can be designed into an active site and shown to matter. The TTR protease work shows an enzyme can be designed against a **sequence-specified macromolecular substrate** chosen for disease relevance rather than assay convenience — and that the substrate's conformation can be co-determined by the generator rather than assumed.

**Supplement:** [[butcher-2026-rfdiffusion3-science-supp]] — 109 pages covering active-site preparation and configuration, the rotamer probability loss, the AME benchmark construction, and the experimental methods for both campaigns.

## Connections

- The published version of [[butcher-2025-rfdiffusion3]] (+ [[butcher-2025-rfdiffusion3-supp]]), substantially reframed and extended.
- Successor to [[watson-2023-rfdiffusion]] (residue-level) and to RFD2, whose residue-level motif conditioning it supersedes; RFD2 is itself not ingested — see the flagged references in [[enzyme-design]].
- Its AME benchmark is the shared evaluation that [[didi-2026-complexa-scaling]] and [[lin-2026-genie3]] also report on; the M-CSA is its source.
- The zinc-protease campaign is the method counterpart of [[chen-2026-metalloproteases]], which uses RFD2-MI on the same chemistry.
- Symmetric enzyme complexes connect to [[symmetric-oligomer-design]].
- Chapter: [[enzyme-design]] §3, §4, §6, §7. Concepts: [[motif-scaffolding]], [[diffusion-generative-design]]. Tool: [[rfdiffusion3]].
