---
type: source
title: Computational design of metalloproteases
authors: Chen, Wu, Choi, Venkatesh, Pellock et al. (Baker lab, with Hilvert and Hyman)
venue: Nature 2026 (doi 10.1038/s41586-026-11167-2; received 14 Oct 2025, accepted 15 Sep 2026)
pdf: "../sources/ProteinDesign/ChenBaker_Nature_2026_Computational design of metalloproteases.pdf"
supp: yes
tags: [enzyme-design, metalloenzyme, protease, zinc, preorganization, filtering, therapeutics, crystallography, validation]
ingested: 2026-10-21
---

# Computational design of metalloproteases

De novo zinc proteases that cleave peptide bonds at designed scissile sites, reaching **>10⁸-fold rate acceleration** out of the computer and **>10¹⁰-fold** after four substitutions — and, separately, the wiki's clearest demonstration that **how you model the active site during filtering determines the hit rate**.

## Problem

Amide hydrolysis is harder than the ester chemistry prior de novo metallohydrolase work addressed: "amides are less reactive than esters due to stronger resonance stabilization, and peptide cleavage requires departure of an intrinsically poor amine leaving group", with the pK_a for deprotonating amines to amine anions **above 35**. Metalloproteases solve this by using a metal ion to activate a water molecule as the nucleophile, which is a different strategy from the activated-nucleophile route of [[choi-2026-cysteine-proteases]].

## Approach

**Active site.** Taken from **aminopeptidase N (PDB 4QHP)**, where **two histidines and a glutamate** form a Zn(II) centre and the fourth zinc ligand is water. Catalytic residue positions and orientations came from a cocrystal structure with a **transition-state analogue**; **AlphaFold3** was used to predict the native **astacin**–substrate complex as a structural guide for substrate placement.

**Generator.** **RFD2-MI** — the same molecular-interfaces variant of RFdiffusion2 used by [[choi-2026-cysteine-proteases]] — to build scaffolds around the constructed active site, with sequence design to simultaneously encode the fold, preorganize the catalytic residues, and position the substrate in the cleft.

**Three modelled states per design:** the **apo** protease (to confirm folding), the **enzyme–substrate complex**, and the **transition-state-analogue complex** (to evaluate transition-state stabilisation, using a phosphonamidate TSA chosen because many crystal structures exist for it, making it better represented in ML training data than the actual transition state).

## Key results

### The filtering result, which is the paper's most transferable finding

Two filtering strategies were used, differing **only in whether the catalytic water was modelled** in the enzyme–substrate complex. Synthetic genes were ordered for **95 designs from the Zn(II)-only strategy and 40 from the Zn(II)-water strategy** (135 total). Cleavage was assessed by SDS–PAGE at 37 °C ± Zn(II):

| Filtering strategy | >10% cleavage at 1 h | >10% cleavage at 12 h |
|---|---|---|
| **Zn(II)-only models** | **3 of 89** (3.4%) | 14 of 89 (16%) |
| **Zn(II)-water models** | **31 of 38** (82%) | 35 of 38 (92%) |

A roughly **24-fold difference in 1-hour hit rate from a modelling choice**, not a generator change. The mechanism is shown directly on a matched pair: in Zn(II)-only models, the inactive design Zn56 and the active design ZnO7 both place substrate in their clefts, "providing no basis for differentiating active and inactive designs". In Zn(II)-water models, **the water in Zn56 clashes with substrate binding, displacing the target amide bond by several ångströms**, while ZnO7's substrate binds productively for nucleophilic attack. The authors state plainly that Zn(II)-water modelling "would have eliminated" the inactive design.

The paper's headline — **36% of 135 designs** cleave their cognate substrate at the targeted scissile bond — is therefore an average across two very different filters, and the **36% understates what the better filter achieves and overstates what the worse one does**. Of 135 fusions, 131 were soluble and 127 migrated at the expected molecular weight.

### Activity, selectivity and structure

**Kinetics** (FRET, GFP–substrate–mScarlet reporters):

- **ZnO7** on its cognate substrate: k_cat = 0.0010 ± 0.0001 s⁻¹, K_M = 4.9 ± 1.2 µM, **k_cat/K_M = 210 ± 60 M⁻¹ s⁻¹**.
- **Zn45** on the ZnO36 substrate: k_cat = 0.025 ± 0.002 s⁻¹, K_M = 26 ± 5 µM, **k_cat/K_M = 900 ± 200 M⁻¹ s⁻¹** — a **>10⁸-fold rate acceleration** over uncatalysed peptide hydrolysis.
- An optimised variant reached k_cat = 0.75 ± 0.04 s⁻¹, K_M = 24 ± 3 µM, **k_cat/K_M = 31,000 ± 5,000 M⁻¹ s⁻¹**, a **30-fold improvement in both k_cat and k_cat/K_M**, taking acceleration past **10¹⁰-fold** — attributed to improved active-site preorganization.

**Selectivity emerges without being asked for.** Cross-reactivity was tested across five scaffold families: **four of five were selective for their cognate substrates even though selectivity was not explicitly enforced**. The fifth, **Zn45**, was promiscuous — active against all tested substrates — and this was **predicted by the AF3 screening metrics**. Quantified: Zn45 almost completely digested ZnO36's cognate substrate, turning over roughly **200 molecules per enzyme overnight** at the highest substrate concentration.

**Crystal structures.** Zn5–Zn(II) at **3.41 Å (PDB 11CE)** and the ZnO7–Zn(II)–substrate complex at **2.37 Å (PDB 11CM)**, matching design models at Cα r.m.s.d. **0.82 Å and 1.35 Å**. In Zn5 the five catalytic residues match the design model at 0.9 Å r.m.s.d. with **zinc clearly resolved at the intended site at full occupancy**; the ZnO7 structure resolves the **catalytic water**.

**Energetics.** Machine-learning force-field calculations put the activation barriers for Zn45 and ZnO7 **3.6 and 15.1 kcal mol⁻¹ higher** than native astacin — a quantitative statement of the remaining gap, and one that locates it in reaction energetics rather than binding.

### Disease targets and conditional biologics

Proteases were designed against **TDP-43** (a C-terminal segment, residues 320–350), **serum amyloid A** and **amyloid-β**, with rate enhancements up to **10⁹-fold**. The TDP-43 protease **TDPn3** showed k_cat = 0.033 ± 0.003 s⁻¹, K_M = 52 ± 9 µM, k_cat/K_M = 640 ± 130 M⁻¹ s⁻¹, was **more active towards TDP-43 than other substrates**, and cleaved **full-length human TDP-43** in both monomeric and oligomeric forms — though more slowly than the peptide, which the authors attribute to liquid–liquid phase separation or precipitation.

The designs were then used as **triggers for conditional biologics**: a masked IL-2 mimic (**Neo2-M-Z**) and a masked **EGFR antagonist** (EGFRmb-M-Z) were selectively activated by the designed proteases, inhibiting EGFR signalling downstream — "bioorthogonal control of cell state".

### What the authors say is missing

Catalytic efficiencies "straight out of the computer are still 10³–10⁴-fold lower than those of" native enzymes, with four named deficits: **more precise active-site placement; incorporation of energetic alongside geometric design criteria; improved preorganization; and the active-site environment**. They note that "increasing preorganization with a few mutations" recovered a large fraction of the gap — the same conclusion [[choi-2026-cysteine-proteases]] reaches by a different route. On specificity: designs bind **8–13-residue substrates**, "creating an extended recognition interface that can encode substantial sequence and conformational selectivity".

## Significance / relation to the field

**The filtering result generalises past enzymes.** [[de-novo-binder-design]] §10 argues from three independent demonstrations that the *filter*, not the generator, sets the hit rate. This is a fourth, and the cleanest: same generator, same designer, same assay, two filters, 3/89 versus 31/38. It also identifies *what* the better filter knows — the position of a catalytic water — which is a far more specific lesson than "use a better oracle".

**Selectivity as an emergent property is new to the wiki.** Four of five scaffold families were substrate-selective without selectivity being a design objective, and the one exception was flagged in advance by the screening metrics. [[de-novo-binder-design]] §13 records as open whether specificity is ever designed or only observed; this is the first ingested source where it is *predicted* and then confirmed.

**Supplement:** [[chen-2026-metalloproteases-supp]].

## Connections

- The water-activation counterpart to the activated-nucleophile strategy of [[choi-2026-cysteine-proteases]]; both use **RFD2-MI**, and share authors.
- The same chemistry as the TTR zinc proteases in [[butcher-2026-rfdiffusion3-science]], reached with the earlier generator — a direct RFD2-MI versus RFD3 comparison the wiki can make only indirectly, since no source runs both.
- Its metal-site design problem is approached from an entirely different direction by [[elnesr-2026-zero-shot-metalloenzyme]], which optimises the coordination sphere directly rather than scaffolding a native motif.
- Uses [[abramson-2024-alphafold3]] for state modelling and screening metrics.
- Its masked-cytokine application connects to the biosensor and prodrug applications in [[vasquez-torres-2023-helical-peptide-binders]].
- Chapter: [[enzyme-design]] §2, §4, §5, §6, §8. Concepts: [[catalytic-site-design]], [[metalloprotein-design]], [[motif-scaffolding]].
