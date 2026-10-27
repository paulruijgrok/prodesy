---
type: source
title: De novo design of cysteine proteases
authors: Choi, Bauer, Coventry, Venkatesh, Chen et al. (Baker lab, with Hilvert)
venue: Nature 2026 (doi 10.1038/s41586-026-11143-w; received 14 Oct 2025, accepted 9 Sep 2026)
pdf: "../sources/ProteinDesign/ChoiBaker_Nature_2026_De novo design of cysteine proteases.pdf"
supp: yes
tags: [enzyme-design, protease, catalytic-triad, oxyanion-hole, preorganization, crystallography, mammalian-cells, validation]
ingested: 2026-10-21
---

# De novo design of cysteine proteases

De novo enzymes that hydrolyse the **peptide backbone itself** using a Cys–His–Asp catalytic triad, with sequence specificity, on folds unlike any natural protease — and that work inside living mammalian cells.

## Problem

The paper states the difficulty in thermodynamic terms, which is what makes it a landmark rather than an increment. **Amide bonds have half-lives of hundreds of years in neutral aqueous solution**, so cleaving them requires substantial activation. De novo enzyme design "has been largely limited to low-energy-barrier model reactions", and the closest prior achievement — designed **serine hydrolases** — acted on "small non-polar ester substrates that are much more activated than the amides of proteins and easier to bind than polar protein substrates". Combined, "the chemical stability of protein substrates and the complex architecture required to recognize and cleave them has made the de novo design of proteases a formidable design challenge that has remained unsolved for decades."

The natural solution being imitated has three parts: a hydrogen-bonded **aspartate–histidine–cysteine catalytic triad** that activates the cysteine nucleophile; an **oxyanion hole** stabilising multiple high-energy intermediates and transition states across a multistep pathway; and a **peptide-binding cleft with sequence specificity** that positions the scissile bond next to the nucleophile. Cysteine was chosen over serine because the mechanism is well studied, triad-based cleavage of activated esters had been shown, and **cysteine is more readily activated than serine**.

## Approach

**Motif.** A minimal active site taken from the yeast cysteine protease **Ulp1 (PDB 1EUV)**: the catalytic triad (Cys580, His514, Asp531), the oxyanion hole (Gln574 plus backbone), and **four residues of the substrate backbone**. Ulp1 was chosen because its oxyanion hole consists of a backbone N–H group and a side chain, a geometry reachable by design.

**Generator.** **RFdiffusion2 for molecular interfaces (RFD2-MI)** — a version of RFD2 optimised for both enzyme and protein–protein interface design, because "the de novo design of proteases requires solving both challenges". RFD2 conditions diffusion trajectories on active-site atom positions **without specifying the sequence positions of the catalytic residues**.

**The substrate is designed too.** Being "agnostic about the exact sequence being cleaved", the authors allowed **both the conformation and the sequence of the substrate to be freely sampled** alongside the enzyme, starting from fully random Gaussian placements of enzyme and peptide. Outputs frequently formed **parallel and antiparallel strand-pairing interactions** with the substrate. Sequences were designed with [[proteinmpnn]], **simultaneously optimising enzyme and substrate sequences** to promote binding and selectivity.

**Filtering, with a failure mode named.** Large substrate-binding sites "are susceptible to collapse in the absence of substrate", so iterative rounds filtered on **AlphaFold3 apo-state** self-consistency (active-site r.m.s.d. < 1.2 Å), keeping designs where **both apo and complex** AF3 models were close to the design model (Cα r.m.s.d. < 0.8 Å, pLDDT > 90, correct catalytic geometry).

**Assay.** The cognate substrate is fused to the design's C terminus followed by **mScarlet** and a His6 tag; active designs self-cleave during *E. coli* expression, releasing free mScarlet, read out by SDS–PAGE and SEC.

## Key results

**Headline: 13 of 69 designs active (19%), from 3 of 12 unique backbones.** The three successful backbone families are named **Gawi, Kal and Dokki**. Dokki and Kal gave complete substrate cleavage, Gawi ~95%. **LC–MS confirmed all 13 active designs cleaved precisely at the intended site.**

**Mechanism is the designed one.** Mutating the catalytic **Cys or His to Ala abolished activity**. Notably, mutating the Gln/Asn oxyanion side chain **did not uniformly inactivate** the designs — the authors suggest ordered waters may compensate, and in the optimised variants the oxyanion knockout cost only **1.9–3.8-fold**. That is a genuine partial dissociation between the designed mechanism and the observed one.

**In trans, and the activity ladder.** Of the 13, the Gawi family was too weak on FRET substrates to characterise and Kal failed on solubility; **Dokki** was measurable. Initial turnover numbers were modest — k_cat ≈ 10⁻⁶ s⁻¹ (Gawi) and ≈ 10⁻⁴ s⁻¹ (Dokki). ProteinMPNN redesign produced **21 Gawi and 89 Dokki variants, of which 7 and 24 improved, by 1.2- to 31-fold**. Steady-state kinetics then gave:

| Design | k_cat (s⁻¹) | K_M (µM) | k_cat/K_M (M⁻¹ s⁻¹) |
|---|---|---|---|
| Gawi-09 | (0.8 ± 0.1) × 10⁻⁵ | 34 ± 4 | 0.24 ± 0.03 |
| Dokki-15 | (1.1 ± 0.1) × 10⁻³ | 89 ± 10 | 12 ± 2 |
| **Dokki-v2** (Y41T/S44V/P67V/T99F) | **0.064 ± …** | — | **413 ± 50** |

**Rate enhancement.** Designs **before optimisation** reach **k_cat/k_uncat up to 3 × 10⁷**. Compared against the measured uncatalysed peptide hydrolysis rate (**k_uncat = 3.6 × 10⁻¹¹ s⁻¹ at 25 °C, pH 6.8**), optimised **Dokki-v2 accelerates amide cleavage by 1.8 × 10⁹-fold** — and the paper is careful that the improvement from Dokki-15 "arises entirely from" effects on the intrinsic chemical step at the active site.

**Biophysics.** Dokki-15 shows a **bell-shaped pH–rate profile peaking at pH 7.0 (pK_a1 = 6.0, pK_a2 = 8.0)**, consistent with ionisation of the catalytic cysteine and histidine. The cysteine pK_a is **shifted down from the free-thiol value of ~8–8.5 to 6.0** — thiolate stabilisation by the neighbouring histidine — **but not as far as native enzymes, where values of 2.5–4.0 are reported**. Dokki-15 has a **melting temperature above 80 °C**.

**Structural validation.** **Six crystal structures**, all within **Cα r.m.s.d. < 1.2 Å** of the design models, including Gawi-09 apo, Dokki apo, Dokki-15 apo and a **Dokki-15(C100A)–substrate complex at 3.38 Å** showing the substrate-binding site. The folds are **unlike natural proteases: TM-score < 0.50**.

**Where the remaining gap lives — the paper's most useful analysis.** Dokki-v2's k_cat "falls at the lower end of the native range, approximately one to two orders of magnitude below the most active native enzymes" (benchmarked against Ulp1, Mpro, TEV and HRV3C). Two diagnoses, both supported:

- **Active-site preorganization is imperfect.** PLACER ensembles across the catalytic cycle (TS1, acyl–enzyme and others) show that in Dokki and Dokki-15, **His45 samples a non-productive interaction with Ser44**; the S44V substitution in Dokki-v2 suppresses that state and improves dyad preorganization, while P67V and T99F improve positioning of the oxyanion Gln65. The fraction of productive PLACER conformations (defined by Cys–His < 4.2 Å) **tracked activity across the series**, consistent with initial nucleophilic attack being rate-limiting.
- **Substrate positioning is imperfect.** Native proteases such as Mpro, TEV and HRV3C form well-defined substrate-binding interfaces with key hydrophobic contacts, while **Ulp1 engages the folded SUMO domain over a large surface** to position its scissile bond. The designs reproduce Ulp1's triad and oxyanion geometry on entirely different scaffolds **but have no auxiliary folded domain positioning the substrate** — and a control measuring Ulp1 on peptide substrates lacking SUMO makes that comparison fair. **MD simulations** of the Michaelis complex found productive conformations sampled more frequently in Dokki-v2.

**Function in cells.** Using a nuclear-localised reporter (sfGFP–substrate–mScarlet fused to histone H2B with an NLS), cells expressing the Dokki series — **including the original designs straight out of the computer** — showed clear relocalisation of mScarlet away from the nucleus, while Cys-to-Ala mutants retained nuclear colocalisation.

## Significance / relation to the field

**It closes the amide-bond problem that defines the field's difficulty ceiling.** Taken with [[chen-2026-metalloproteases]] and the TTR proteases in [[butcher-2026-rfdiffusion3-science]], three independent routes to designed peptide-bond hydrolysis appeared essentially simultaneously, by three different mechanisms — an activated cysteine nucleophile here, a water-activating zinc centre there, and both again in the RFD3 campaign.

**It is the wiki's best source on *why* designed enzymes underperform.** The preorganization analysis — PLACER ensembles showing a specific non-productive His rotamer, suppressed by a specific mutation, with the productive fraction tracking activity — is a mechanistic account, not a hand-wave. It is also the clearest statement that the gap is **geometric rather than conceptual**: the crystal structures confirm the active site was built as designed, and the activity is still 1–2 orders of magnitude short.

**And it shows the co-design of substrate and enzyme.** Letting the substrate sequence and conformation be sampled freely alongside the enzyme is a different design problem from scaffolding a fixed motif, and it is what makes the sequence specificity designed rather than inherited.

**Supplement:** [[choi-2026-cysteine-proteases-supp]].

## Connections

- Built on **RFD2-MI**, the same generator as [[chen-2026-metalloproteases]]; RFD2 itself is not ingested (see flagged references in [[enzyme-design]]). Superseded as a method by [[butcher-2026-rfdiffusion3-science]].
- Uses [[dauparas-2022-proteinmpnn]] for sequence design and [[abramson-2024-alphafold3]] for apo/complex filtering.
- Its oxyanion-hole and buried-polar reasoning connects to [[boyken-2016-hydrogen-bond-network-oligomers]]; its substrate-positioning analysis to the interface packing results in [[halperin-2004-interface-hot-spots]].
- Chapter: [[enzyme-design]] §2, §4, §5, §7, §8. Concepts: [[motif-scaffolding]], [[catalytic-site-design]].
