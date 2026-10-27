---
type: topic
tags: [enzyme-design, catalysis, protease, metalloenzyme, preorganization, motif-scaffolding, filtering, validation, de-novo]
sources: 20
updated: 2026-10-21
---

# De novo enzyme design

A chapter on designing proteins that catalyse chemical reactions from scratch. It is a late chapter in this wiki for a reason: until 2026 the field's honest summary was that de novo enzymes worked on easy reactions and that the hard ones — the reactions biology actually cares about — remained out of reach. That changed within a single year, and the chapter's first job is to record how.

The defining difficulty is stated most clearly by [[choi-2026-cysteine-proteases]]: **amide bonds have half-lives of hundreds of years in neutral aqueous solution**, so cleaving one requires substantial activation, and de novo enzyme design "has been largely limited to low-energy-barrier model reactions". The closest prior achievement, designed serine hydrolases, acted on "small non-polar ester substrates that are much more activated than the amides of proteins and easier to bind than polar protein substrates" ([[choi-2026-cysteine-proteases]]). [[chen-2026-metalloproteases]] puts the same barrier in chemical terms: amides are less reactive than esters because of stronger resonance stabilisation, and peptide cleavage requires departure of an intrinsically poor amine leaving group, with a pK_a above 35. Amide-bond hydrolysis is therefore the field's benchmark not by convention but by physics.

**The chapter's argument.** De novo enzyme design has largely solved the problem of *building* an active site and has largely not solved the problem of *preorganizing* one. Three independent campaigns cleared the amide barrier in 2026, by three different chemistries, and all three report the same pair of facts: the crystal structures match the design models to within roughly an ångström, and the catalytic efficiency is still one to four orders of magnitude below native enzymes. The gap is not that the designs were built wrong. It is that catalysis is a property of an **ensemble of conformations across a multi-step reaction coordinate**, while the design and filtering apparatus is built around **single predicted structures** — and the two are not the same object.

A second thread runs through §6 and is the chapter's most transferable finding: **what you model is what you get**. The single largest effect on hit rate anywhere in this chapter comes not from changing the generator but from changing what was present in the modelled active site during filtering.

## Contents

1. What counts as de novo enzyme design
2. What an active site has to do
3. The method lineage: from functional sites to free atoms
4. 2026 — the amide barrier falls, three times
4b. The ester precedent, and an independent lineage
5. Preorganization — the diagnosis everyone converges on
6. What you model is what you get
7. The alternative premise — designing the coordination sphere
8. What actually gets validated
9. Specificity, and designing against disease
10. Open questions
11. Flagged references — the history this chapter cannot yet cite
12. Sources

## 1. What counts as de novo enzyme design

The object is a protein that accelerates a chosen reaction, designed from a specification of the chemistry rather than evolved from a natural enzyme. In practice the specification is a **theozyme** — a geometric arrangement of catalytic groups around a substrate or transition state — and the design problem is to build a protein that holds that arrangement.

Where the theozyme comes from varies, and the variation matters. [[chen-2026-metalloproteases]] took catalytic residue positions and orientations from a cocrystal structure of **aminopeptidase N with a transition-state analogue** and used an AlphaFold3 prediction of the native astacin–substrate complex as a guide for substrate placement. [[choi-2026-cysteine-proteases]] took the catalytic triad, oxyanion hole and four substrate backbone residues from the yeast protease **Ulp1 (PDB 1EUV)**. [[butcher-2026-rfdiffusion3-science]] used a mix: for its phosphotriesterase campaign the theozyme was **derived from a quantum chemistry calculation** ([[butcher-2026-rfdiffusion3-science-supp]]), while its transthyretin protease theozyme merged catalytic residues from aminopeptidase N with substrate backbone atoms and stabilising protease backbone atoms taken from an AF3 prediction. [[elnesr-2026-zero-shot-metalloenzyme]] uses no theozyme at all, which is §7.

Three capabilities distinguish enzyme design from the binder design of [[de-novo-binder-design]], and each is a reason the methods had to change:

- **Sub-ångström placement of several specific atoms**, not a complementary surface. [[butcher-2026-rfdiffusion3-science]] frames the entire method around this: catalytic function "arises from the placement of many atoms in three-dimensional space", and residue-level representations "lack the resolution to specify enzyme active sites".
- **Unknown sequence positions.** The backbone coordinates and sequence positions of catalytic residues "are generally not specified in advance", so a method must **jointly infer the scaffold, the catalytic side-chain rotamers, and the sequence positions** from minimal atomic constraints ([[butcher-2026-rfdiffusion3-science]]).
- **A substrate that must be bound *and* oriented.** A binder needs affinity; an enzyme needs the scissile bond presented to the nucleophile in a particular geometry. [[choi-2026-cysteine-proteases]] handles this by letting **both the conformation and the sequence of the substrate be freely sampled** alongside the enzyme, and [[chen-2026-metalloproteases]] by modelling the enzyme–substrate complex as a separate filtered state.

## 2. What an active site has to do

A catalytic site is not a binding site with extra steps. The sources identify four requirements, and designs now routinely satisfy the first two and struggle with the last two.

**Activate a nucleophile.** The cysteine protease family uses a hydrogen-bonded **aspartate–histidine–cysteine catalytic triad** in which the histidine deprotonates the cysteine, and cysteine was chosen over serine in [[choi-2026-cysteine-proteases]] partly because it "is more readily activated". The metalloprotease family instead uses a **metal ion to activate a water molecule**, with two histidines and a glutamate forming the Zn(II) centre and water as the fourth ligand ([[chen-2026-metalloproteases]]). That the designs achieve this is measurable: Dokki-15's cysteine pK_a is shifted from the free-thiol value of ~8–8.5 down to **6.0**, and its bell-shaped pH–rate profile with pK_a1 = 6.0 and pK_a2 = 8.0 matches ionisation of the catalytic cysteine and histidine ([[choi-2026-cysteine-proteases]]). That the shift is incomplete is equally measurable: native enzymes reach cysteine pK_a values as low as **2.5–4.0**.

**Stabilise high-energy intermediates.** The **oxyanion hole** stabilises "multiple high-energy intermediates and transition states along the multistep reaction pathway" ([[choi-2026-cysteine-proteases]]). This is where the designs are most clearly partial. Mutating the designed Gln/Asn oxyanion side chain to alanine **did not uniformly inactivate** the designs, costing only 1.9- to 3.8-fold in the optimised variants, with the authors suggesting ordered waters may compensate ([[choi-2026-cysteine-proteases]]). A designed feature that can be deleted at a cost of twofold is not doing what the equivalent native feature does.

**Bind and orient the substrate.** Designed proteases bind **8–13-residue substrates, creating an extended recognition interface that can encode substantial sequence and conformational selectivity** ([[chen-2026-metalloproteases]]). The contrast with native enzymes is instructive: [[choi-2026-cysteine-proteases]] notes that Mpro, TEV and HRV3C form well-defined substrate-binding interfaces with key hydrophobic contacts, while **Ulp1 engages the entire folded SUMO domain** over a large surface to position its scissile bond — and the designs, which copy Ulp1's catalytic geometry, have **no auxiliary folded domain** doing that work.

**Hold all of this in the right geometry across the whole reaction.** This is preorganization, it is §5, and it is where the field now is.

The biophysics the chapter can cite is thinner than the chemistry. Buried polar satisfaction — why an oxyanion hole is hard to build — is grounded in [[boyken-2016-hydrogen-bond-network-oligomers]], which establishes that a hydrogen bond is partially covalent and so restricts donors and acceptors to narrow ranges of orientation and distance, that nearly all buried polar atoms must find a partner or incur a desolvation penalty, and that such networks are inherently **many-body** and therefore badly handled by pairwise energy functions. For metals, [[durr-2023-metal3d]] supplies the design-relevant framing: metals are attractive because they "tether to the protein using strong interactions and have favorable catalytic properties", **about 10% of all enzyme-catalysed reactions use zinc**, and computational design "is hampered by the complex electronic structure" of such metals — classical force fields handle them poorly and quantum treatment is too expensive for design-scale work.

## 3. The method lineage: from functional sites to free atoms

**Scaffolding a functional site** is the ancestral formulation, and the wiki's source for it is [[wang-2022-functional-site-scaffolding]]: given a site's geometry and residue identities — "from quantum chemistry, fragment docking, or extracted from a native protein" — build a protein that holds it. The concept page is [[motif-scaffolding]]. [[anishchenko-2021-hallucination]] had already anticipated the application, noting its loss could be generalised to include binding motifs or catalytic sites, and arguing that because the network hallucinates plausible structures from scratch, no scaffold blueprint need be specified in advance.

**Conditional diffusion** generalised this. [[watson-2023-rfdiffusion]] reports state-of-the-art on metal-binding and enzyme active-site scaffolding among its tasks, achieved by fine-tuning on **minimal motifs** ([[watson-2023-rfdiffusion-supp]]). [[krishna-2024-rosettafold-all-atom]] made the generator ligand-aware.

**RFdiffusion2 — the step that unlocked everything in §4.** [[ahern-2025-rfdiffusion2]] diagnoses the limiting constraint precisely. Existing motif-scaffolding methods represent motifs as **backbone frames**, parameterising each residue's N, Cα, C atoms in SE(3), and **each motif frame requires a prespecified sequence index** giving its position along the chain. That is adequate for scaffolding a contiguous domain and wrong for a theozyme, which is a handful of functional groups whose sequence positions are unknown and whose rotamers must be inferred. The prior workaround was **inverse rotamer sampling** — enumerating backbone placements consistent with each side-chain geometry — which the paper objects to as expert-intensive and sampling-limiting. Before that, RosettaMatch searched existing scaffolds for placements, "restricted to theozyme geometries that could be matched to the input scaffold set".

RFD2's answer has two parts. Residues may be represented **either as a frame or as heavy atoms**, so the model can atomize a catalytic residue and learn the distribution of its side-chain poses — which is how it can "forgo inverse rotamer sampling". And modifying the index features yields **unindexed residues**, which — with **no auxiliary losses** — the network learns to superimpose onto residues of the generated protein, so conditioning on an **unindexed motif** samples proteins containing the motif without being told where it sits ([[ahern-2025-rfdiffusion2]]). The supplement shows this is a trained behaviour rather than an inference-time device: each residue is annotated unindexed with probability `P_IS_UNINDEXED` during training-example construction ([[ahern-2025-rfdiffusion2-supp]]). Training uses **flow matching** rather than denoising diffusion, over a data representation containing both atoms in ℝ³ and frames in SE(3).

The measured effect is the clearest before/after in this chapter: **RFD2 solves all 41 AME benchmark cases where previous methods solved 16** ([[ahern-2025-rfdiffusion2]]).

Both 2026 Nature protease campaigns use **RFD2-MI**, a variant optimised for enzyme *and* protein–protein interface design, "as the de novo design of proteases requires solving both challenges" ([[choi-2026-cysteine-proteases]], [[chen-2026-metalloproteases]]). RFD2-MI has no methods paper of its own; [[choi-2026-cysteine-proteases]] cites a phospho-tyrosine peptide binder preprint for it and [[butcher-2026-rfdiffusion3-science]] cites the metalloprotease preprint — see §11.

**Free-atom diffusion.** [[butcher-2026-rfdiffusion3-science]] identifies RFD2's remaining limitation precisely: because diffusion remains at the residue level, it "is incapable of creating additional side chain interactions with ligands". RFD3 diffuses at the atomic level throughout. For catalytic sites, an extra token is appended per catalytic residue, and crucially **the atomic motif conditioning tokens correspond only to the atoms actually being fixed**, where RFD2 had to represent the full catalytic residue in order to locate a backbone position. The supplement makes the mechanism exact: standard residues are single tokens, while **modified residues, all ligands and unindexed conditions are tokenized per-atom**, and tokens are *indexed* or *unindexed* by whether residue index is revealed ([[butcher-2026-rfdiffusion3-science-supp]]) — so "scaffolding an unindexed atomic motif" is a precise statement about the representation.

The AME benchmark is itself a contribution of [[ahern-2025-rfdiffusion2]], which built it after finding the pre-existing enzyme motif-scaffolding benchmark inadequate: PDB crystal structures **where all reactants and cofactors were present**, curated to **41 active sites** across diverse reactions, 100 structures sampled per case ([[ahern-2025-rfdiffusion2]]). The measured benefit of free-atom diffusion on it: on **atomic motif enzyme (AME)** problems drawn from the **Mechanism and Catalytic Site Atlas**, where difficulty rises with the number of catalytic motif islands, **RFD3 outperforms RFD2 on 37 of 41 (90%) tasks**, with improvement concentrated on the harder problems; on four six-residue active sites it recapitulated active-site residues to within 1.25 Å after refolding more often in all four cases; and rotamer quality, scored by a **Dunbrack backbone-dependent rotamer probability loss**, is consistently better ([[butcher-2026-rfdiffusion3-science]]). The metric's definition carries a caveat worth holding: it **excludes Gly, Ala and Pro** ([[butcher-2026-rfdiffusion3-science-supp]]).

Two further capabilities arrive with the atomic representation. **Symmetric enzyme complexes**: tested on 15 C2-symmetric AME cases, RFD3 produced designs with consistent catalytic-residue alignment across subunits "even in challenging cases involving up to seven catalytic residues per subunit" ([[butcher-2026-rfdiffusion3-science]]) — connecting this chapter to [[symmetric-oligomer-design]]. And **mixed protein/RNA active sites**, demonstrated on the RNase P site which uses amino-acid side chains and RNA bases together.

## 4. 2026 — the amide barrier falls, three times

Three campaigns, three chemistries, one year. They are best read as independent replications of the claim that de novo amide hydrolysis is now possible, because they share a lab lineage but not a mechanism.

### 4.1 An activated cysteine nucleophile

[[choi-2026-cysteine-proteases]] scaffolded the Ulp1 triad and oxyanion hole with RFD2-MI, letting substrate sequence and conformation sample freely, designing sequences with [[proteinmpnn]] to optimise enzyme and substrate together, and filtering on AlphaFold3 **apo-state** self-consistency — a deliberate guard, since large substrate-binding sites "are susceptible to collapse in the absence of substrate".

**13 of 69 designs were active (19%), from 3 of 12 unique backbones** ([[choi-2026-cysteine-proteases]]) — the families Gawi, Kal and Dokki. LC–MS confirmed **all 13 cleaved precisely at the intended site**. Cys-to-Ala and His-to-Ala abolished activity. After ProteinMPNN redesign (21 Gawi and 89 Dokki variants, of which 7 and 24 improved by 1.2- to 31-fold), steady-state kinetics gave **k_cat/K_M of 0.24 ± 0.03 M⁻¹ s⁻¹ for Gawi-09 and 12 ± 2 M⁻¹ s⁻¹ for Dokki-15**, rising to **413 ± 50 M⁻¹ s⁻¹ for Dokki-v2**. Rate enhancements reach **3 × 10⁷ before optimisation** and **1.8 × 10⁹** for Dokki-v2 against the measured uncatalysed rate of 3.6 × 10⁻¹¹ s⁻¹ ([[choi-2026-cysteine-proteases]]).

Two results beyond the kinetics. **Six crystal structures within Cα r.m.s.d. < 1.2 Å of the design models**, on folds with **TM-score < 0.50 to natural proteases** — with the novelty computed on the experimental structures by Foldseek, not on models ([[choi-2026-cysteine-proteases-supp]]). And the designs **work in living mammalian cells**: in a nuclear-localised sfGFP–substrate–mScarlet reporter, cells expressing the Dokki series, "including the original Dokki designs straight out of the computer", relocalised mScarlet out of the nucleus, while Cys-to-Ala mutants did not ([[choi-2026-cysteine-proteases]]).

### 4.2 A water-activating zinc centre

[[chen-2026-metalloproteases]] took the opposite chemical route — metal-activated water rather than an activated protein nucleophile — on the same generator. Each design was modelled in **three states**: apo, enzyme–substrate complex, and a **transition-state-analogue complex** using a phosphonamidate TSA, chosen because many crystal structures exist for it and it is therefore "better represented in ML training data than the actual transition state".

**Of 135 designs tested, 36% cleave their cognate substrate at the targeted scissile bond** ([[chen-2026-metalloproteases]]) — a figure §6 shows to be an average across two very different filters. **Zn45** on the ZnO36 substrate reached k_cat = 0.025 ± 0.002 s⁻¹, K_M = 26 ± 5 µM, **k_cat/K_M = 900 ± 200 M⁻¹ s⁻¹**, a **>10⁸-fold rate acceleration**; an optimised variant reached **k_cat/K_M = 31,000 ± 5,000 M⁻¹ s⁻¹**, a 30-fold gain in both k_cat and k_cat/K_M, taking acceleration past **10¹⁰-fold**. Crystal structures of Zn5–Zn(II) (3.41 Å, PDB 11CE) and the ZnO7–Zn(II)–substrate complex (2.37 Å, PDB 11CM) match design models at **0.82 Å and 1.35 Å Cα r.m.s.d.**, with zinc resolved at the intended site at full occupancy and the catalytic water resolved in ZnO7 ([[chen-2026-metalloproteases]]).

### 4.3 Free-atom diffusion, two zero-shot campaigns

[[butcher-2026-rfdiffusion3-science]] ran two 96-construct campaigns with no experimental optimisation.

**Phosphotriesterases.** The active site is unusually demanding: six catalytic residues coordinating **two metal ions, including a post-translationally carbamylated lysine bridging them**. From 96 designs, **4 were active, all from the same base scaffold** ([[butcher-2026-rfdiffusion3-science]]); **ZAPP-1** performs multiple-turnover catalysis at k_cat = 0.015 ± 0.003 s⁻¹ and k_cat/K_M = 2.0 ± 0.6 M⁻¹ s⁻¹. The designed modification is load-bearing and was tested: removing carbamylation gave an **11-fold decrease in k_cat and 4-fold in k_cat/K_M**. A second round gave 7 characterised hits across **4 distinct scaffolds**, with ZAPP-2 at a rate enhancement of **(5 ± 2) × 10⁵** ([[butcher-2026-rfdiffusion3-science]]).

**Transthyretin proteases.** The substrate is **PAINVAVHVF**, the longest β-strand in the core of the TTR amyloid fibril (PDB 8GBR), chosen for disease relevance rather than assay convenience. RFD3 simultaneously scaffolded the catalytic residues, **determined the substrate conformation**, and generated a bespoke active-site cleft. **56 of 96 designs (58%) showed >10% cleavage in cis** ([[butcher-2026-rfdiffusion3-science]]); the best, TTRg11, cleaved the majority of substrate in an hour, with mass spectrometry confirming the designed site, and gave **k_cat 0.072 ± 0.008 s⁻¹, K_M 70 ± 10 µM, k_cat/K_M 1100 ± 300 M⁻¹ s⁻¹** as a one-shot design — "within the range (although at the low end) of native proteases with well-characterized biological functions". The paper names the advance over RFD2-era protease design as two things: the very high in-cis success rate, and **activity on natural peptide-derived substrates** rather than synthetic substrates optimised for cleavability.

### 4.4 Reading the three together

The three campaigns are not directly comparable — different chemistries, substrates, assays and success definitions — and §8 says so in detail. What they jointly establish is narrower and more robust than any one of them: **designed proteins can hydrolyse peptide bonds, at designed positions, by at least two mechanisms, on folds unlike natural proteases, with crystal structures confirming the active site was built as specified.** That proposition had no support in this wiki a year ago.

## 4b. The ester precedent, and an independent lineage

Two papers published in *Nature* 649 on the same day frame everything in §4, and neither is about amides.

### The ester precedent — how high designed catalysis had already reached

[[kim-2026-metallohydrolases]] is the direct companion to [[ahern-2025-rfdiffusion2]], and it is the activity bar the protease papers are measured against. Target: hydrolysis of the fluorogenic ester **4MU-phenylacetate**. The theozyme came from **DFT** — the transition-state geometry for Zn(II)-hydroxide attack on the ester, with no native enzyme's geometry copied.

**86 of 96 designs expressed; 5 had activity above background; the best gave k_cat/K_M = 16,000 ± 2,000 M⁻¹ s⁻¹** — against **3 to 60 M⁻¹ s⁻¹ for previously designed metallohydrolases** ([[kim-2026-metallohydrolases]]). A second 96-design round, whose theozymes now **contained the catalytic base**, produced three more: **ZETA_2 at 53,000 ± 5,000 M⁻¹ s⁻¹ with k_cat = 1.5 ± 0.1 s⁻¹**, ZETA_3 at 19,000, ZETA_4 at 1,100. The four most active differ from known structures **and from each other**; ZETA_1 retains activity for **at least 1,000 turnovers** and its closest PDB and AFDB matches score TM 0.41 and 0.49 with no analogous catalytic arrangement. Crystallography: ZETA_2 apo at **3.5 Å, Cα r.m.s.d. 1.1 Å (PDB 9PYJ)**, and Zn-soaked at **2.1 Å, Cα r.m.s.d. 0.8 Å with zinc at 100% occupancy** at the designed location (PDB 9PYL).

**Two details worth carrying.** The **Zn(II) ion itself acts as the oxyanion hole**, stabilising developing negative charge with no nearby side-chain hydrogen-bond donors — which sidesteps the many-body buried-polar problem of [[boyken-2016-hydrogen-bond-network-oligomers]] that [[choi-2026-cysteine-proteases]] struggles with. And the designed mechanism is only partly confirmed: the triple-histidine knockout inactivates, but **H130A costs only 13-fold and D67A — the proposed general base — barely affects k_cat/K_M and increases zinc affinity**, suggesting competing zinc-binding configurations ([[kim-2026-metallohydrolases]]).

**Why this matters for §4.** 53,000 M⁻¹ s⁻¹ on an ester against **413 M⁻¹ s⁻¹** on an amide in [[choi-2026-cysteine-proteases]] is roughly two orders of magnitude — a measure of what the substrate change costs rather than of what the methods differ by. The amide barrier is real, and these numbers size it.

### An independent lineage — Riff-Diff

[[braun-2026-riff-diff]] (Oberdorfer lab) is the only non-Baker-lab enzyme-design source in the wiki, and its complaint is about *rates* rather than scope: "an often underemphasized limitation of current approaches to enzyme design is the **low initial catalytic rates** of the designed biocatalysts… the current paradigm for generating efficient biocatalysts is to **compensate for low initial efficiencies with high-throughput screening and directed evolution**."

**Riff-Diff** builds *on* [[watson-2023-rfdiffusion]] rather than retraining it — the methodological contrast with [[ahern-2025-rfdiffusion2]], which learned the inverse-rotamer problem away. Two contributions:

1. **Artificial motif libraries.** Each catalytic residue is embedded in a **helical fragment** with rotamers chosen for compatibility with that fragment's backbone; the pipeline then **inverts rotamers** to fix functional groups in space while varying backbone positions, searches all non-clashing fragment combinations, and ranks assemblies by **rotamer probability and PDB abundance** ([[braun-2026-riff-diff]]). An enumerative solution to the same problem RFD2 solved by learning.
2. **The placeholder helix.** From **PDBbind**, natural enzymes bury substrates such that an average of **7.1 α-carbons lie within 8 Å**, normalised by ligand heavy atoms. RFdiffusion's substrate auxiliary potential "decreased the number of clashes… but **failed to promote the formation of well-defined substrate binding pockets**". The fix is to add an **α-helix as an entry-channel placeholder** at the pocket position, centre the denoising trajectory on it, constrain backbone distances to that centre — then **delete the helix after diffusion, leaving a vacant pocket** ([[braun-2026-riff-diff]]).

**Results that change the chapter's sense of the ceiling.** From the **RA95.5-8F** retroaldolase tetrad — the same theozyme [[ahern-2025-rfdiffusion2]] used — 36 designs ordered, 35 produced, **29 of 35 correctly folded**, and the best two cleaved rac-methodol at **k_cat 3.6 × 10⁻² and 3.1 × 10⁻² s⁻¹**, a **~5 × 10⁶-fold acceleration**, faster than the evolved catalytic antibody 38C2. **RAD29's efficiency of 290 M⁻¹ s⁻¹ approaches the extensively evolved RA95.5-5 at 320 M⁻¹ s⁻¹** ([[braun-2026-riff-diff]]). For comparison, [[ahern-2025-rfdiffusion2]]'s retroaldolase from the same theozyme reached **6.34 ± 0.92 M⁻¹ s⁻¹** from 96 designs — roughly 45-fold lower, which is this chapter's only direct cross-method comparison on one reaction.

**Stereoselectivity, reported nowhere else in the wiki.** **RAD35 showed an E-value over 200 and 99% enantiomeric excess for (R)-methodol**, with HPLC determination of absolute configuration ([[braun-2026-riff-diff]], [[braun-2026-riff-diff-supp]]). RAD29 was modestly selective (E-value 4, 60% ee).

**And a non-biological reaction.** The **Morita–Baylis–Hillman** reaction has no known natural enzyme. From two evolved catalytic arrays, **17 of 18 (94%)** and **42 of 45 (93.3%)** designs showed product formation, with MBH48 at k_cat 0.025 min⁻¹, 1.5× higher than its evolved comparator, and an unfolding onset near 85 °C ([[braun-2026-riff-diff]]). Six high-resolution structures across both campaigns, down to **1.13 Å (MBH2, Cα RMSD 0.53 Å)** and MBH48 at Cα RMSD 0.78 Å.

**The honesty worth noting.** The paper reports that **22 designs had k_cat below 10⁻³ s⁻¹, "within the range achievable by an isolated lysine in a hydrophobic pocket"** ([[braun-2026-riff-diff]]) — most designs are not doing designed catalysis, and it says so. And it states that explaining the rate enhancement "will require more than the two crystal structures presented here".

**The wiki's reading.** This lineage changes what the chapter can claim about the ceiling. §5's diagnosis — that designs are 1–4 orders of magnitude below native because preorganization is imperfect — holds across the Baker-lab campaigns. But a method that reaches **90% of an extensively evolved enzyme's catalytic efficiency** on a well-studied reaction, with 99% ee, suggests the ceiling is a property of current pipelines rather than of de novo design. That is the strongest available argument that the gap is closable, and it comes from the one independent group in the chapter.

## 5. Preorganization — the diagnosis everyone converges on

Every campaign reports a gap to native enzymes, and every campaign reaches the same explanation. This convergence is the chapter's strongest synthesis.

**The gap, quantified.** [[chen-2026-metalloproteases]] states that catalytic efficiencies "straight out of the computer are still **10³–10⁴-fold lower**" than native enzymes. [[choi-2026-cysteine-proteases]] places Dokki-v2's k_cat "at the lower end of the native range, approximately **one to two orders of magnitude** below the most active native enzymes", benchmarked against Ulp1, Mpro, TEV and HRV3C with the comparison set given explicitly ([[choi-2026-cysteine-proteases-supp]]). [[chen-2026-metalloproteases]] also puts a thermodynamic number on it: machine-learning force-field calculations place the activation barriers of Zn45 and ZnO7 **3.6 and 15.1 kcal mol⁻¹ higher than native astacin** — though that paper's own supplement discusses the limitations of those calculations ([[chen-2026-metalloproteases-supp]]), so the chapter treats the figure as indicative.

**The gap is not a construction error.** This is what makes the diagnosis interesting. The crystal structures confirm the designs were built as specified — Cα r.m.s.d. < 1.2 Å across six structures in [[choi-2026-cysteine-proteases]], 0.82 Å and 1.35 Å in [[chen-2026-metalloproteases]], with catalytic residues at 0.9 Å and metal at full occupancy. The active sites are where they were designed to be and the enzymes are still slow.

**The mechanistic account.** [[choi-2026-cysteine-proteases]] supplies the chapter's best evidence, using **PLACER** ensembles spanning the catalytic cycle — the first transition state, the acyl–enzyme and other states. In Dokki and Dokki-15, **His45 samples a non-productive interaction with Ser44**; the S44V substitution in Dokki-v2 suppresses that state and improves dyad preorganization, while P67V and T99F improve positioning of the oxyanion Gln65. The decisive observation is that the **fraction of productive conformations — defined by Cys–His < 4.2 Å — tracked activity across the series**, consistent with initial nucleophilic attack being rate-limiting. Molecular dynamics of the Michaelis complex found productive conformations sampled more frequently in Dokki-v2. [[chen-2026-metalloproteases]] reaches the same place from the other side: four substitutions improving preorganization bought a 30-fold gain and took acceleration past 10¹⁰-fold.

**Substrate positioning is the second half.** [[choi-2026-cysteine-proteases]] separates the two explicitly: imperfection "both in the precise geometry of the catalytic machinery, and in positioning the peptide substrate relative to this machinery so that the peptide bond to be cleaved is properly oriented". The Ulp1 comparison makes the point concrete — the designs copy Ulp1's catalytic geometry without Ulp1's large SUMO-engaging interface — and the supplement's measurement of **Ulp1 on peptide substrates lacking SUMO** is what makes the comparison fair ([[choi-2026-cysteine-proteases-supp]]).

**The wiki's reading.** A designed enzyme is specified and filtered as a *structure*; catalysis is a property of a *distribution over structures* along a reaction coordinate. The PLACER result is the clearest statement of this in any ingested source: the quantity predicting activity was not the designed geometry but the **fraction of an ensemble occupying a productive geometry**. Every campaign's residual gap is consistent with the design apparatus optimising the mode of a distribution while catalysis depends on its tail. §10 records what would test this.

## 6. What you model is what you get

The single largest effect on outcome in this chapter is not a generator, an architecture or a sequence-design model. It is **what was present in the active site when the design was filtered**.

### 6.1 The catalytic water

[[chen-2026-metalloproteases]] ran two filtering strategies differing only in whether the catalytic water was modelled in the enzyme–substrate complex, ordering genes for **95 designs from the Zn(II)-only strategy and 40 from the Zn(II)-water strategy**:

| Filtering strategy | >10% cleavage at 1 h | >10% cleavage at 12 h |
|---|---|---|
| Zn(II)-only models | **3 of 89** (3.4%) | 14 of 89 (16%) |
| Zn(II)-water models | **31 of 38** (82%) | 35 of 38 (92%) |

Roughly a **24-fold difference in one-hour hit rate**, from the same generator, the same designers and the same assay. The mechanism is shown on a matched pair: in Zn(II)-only models the inactive Zn56 and the active ZnO7 both place substrate in their clefts, "providing no basis for differentiating active and inactive designs"; in Zn(II)-water models the water in Zn56 **clashes with substrate binding, displacing the target amide bond by several ångströms**, while ZnO7's substrate binds productively. Zn(II)-water modelling "would have eliminated" the inactive design ([[chen-2026-metalloproteases]]).

What makes this more than an anecdote is that the **numerical thresholds did not change**. The supplement gives them per state — apo at pLDDT > 86 and catalytic side-chain RMSD < 1.5 Å; enzyme–substrate at pLDDT > 92, mean interface PAE < 5, minimum interface PAE < 1.2; TSA complex at pLDDT > 92 and mean interface PAE < 5 ([[chen-2026-metalloproteases-supp]]) — and both design sets passed them. The difference was in **what the model was asked to place**, not how confidently it had to do so.

### 6.2 A confident oracle endorsing an impossible site

[[elnesr-2026-zero-shot-metalloenzyme]] supplies the complementary failure, and it is sharper because it was published as a negative control. The design **desD1** was deliberately chosen far from the Pareto knee point; its site "contains only a single ligand within binding distance — a coordination environment insufficient for stable metal chelation". Experimentally it binds no zinc: null by MagFura-2 competition titration and by ICP-MS.

Post hoc, **AlphaFold3 predicted desD1 with excellent overall structural agreement and assigned the metal a pLDDT of 86.55**, placing it exactly where the design had ([[elnesr-2026-zero-shot-metalloenzyme]]). The authors state the consequence without softening it: **"By standard computational metrics and filtering criteria, this design would have been classified as a success."**

The cause was traced to training data. Auditing the training sets of LigandMPNN and [[durr-2023-metal3d]], they found zinc sites with **fewer than three coordinating residues within 3.0 Å**, which "may reflect crystallization additives or soaking agents rather than biologically" meaningful sites, and retrained **Metal3D-Clean** excluding them, observing the expected drop in confidence on exactly those sites ([[elnesr-2026-zero-shot-metalloenzyme]]). Metal3D's own paper anticipates the mechanism, noting metals are often present in crystallization buffers because they help overcome the enthalpic cost of protein surface association ([[durr-2023-metal3d]]), and its supplement stratifies nearly every performance figure by coordination number and occupancy, reporting MAD separately for all sites and for sites with at least two protein ligands ([[durr-2023-metal3d-supp]]). The artefact was visible in the evaluation all along; it became consequential only when the model was used generatively.

**PLACER as a prospective filter, validated both ways.** [[kim-2026-metallohydrolases]] is the chapter's one case where an ensemble filter was used to *select* rather than to explain. PLACER — a network that, given a backbone with a substrate, **fully randomises the substrate and all side chains within a 600-atom sphere and regenerates their coordinates**, with repeated trajectories giving an ensemble — predicted the eventual best design, ZETA_1, to have a highly preorganized site with catalytic side chains fixed and substrate held in place, while in the inactive designs H7 and H8 "it fluctuated considerably". ZETA_1 **was the top-ranked design in the in silico ranking**. The confirming test is retrospective and decisive: **seven designs from the same ZETA_1 backbone family, filtered out during selection for suboptimal PLACER metrics, were later expressed and found to have very low or no activity** ([[kim-2026-metallohydrolases]]). Same backbone family, same campaign, separated by a PLACER score. The supplement compares AlphaFold2, PLACER and Chai-1 metrics head to head on the ordered designs ([[kim-2026-metallohydrolases-supp]]).

Taken with §5's finding that the productive-conformation fraction tracks activity ([[choi-2026-cysteine-proteases]]), the wiki's reading is that **the ensemble is the filterable quantity**, and that the field has now demonstrated this prospectively once.

**Two further negative results** belong here, both from [[chen-2026-metalloproteases-supp]]: **"Introduction of substrate-stabilizing residues by MPNN reduces activity"** — sequence design aimed at better substrate binding made enzymes worse — and an explicit assessment of **the predictability of AF3 and MPNN in the mutagenesis space** around a designed active site.

**The wiki's reading.** [[de-novo-binder-design]] §10 catalogues four ways an oracle misleads: adversarial overfitting, circularity, gates that deplete the signal they select for, and plain disagreement with experiment. This chapter adds a fifth and more basic one: **the oracle scores the model it is given, and an active site modelled without its catalytic machinery is a different object from the one that has to work.** Confidence thresholds cannot detect this, because the model is confidently right about the wrong thing.

## 7. The alternative premise — designing the coordination sphere

Every source in §3 and §4 begins from a native catalytic motif. [[elnesr-2026-zero-shot-metalloenzyme]] argues that premise is insufficient and tests the alternative.

Its objection: current methods extract or generate a catalytic motif and place it in a designed backbone, and "while this workflow is intended to preserve the motif geometry to hopefully recapitulate catalytic function, **optimizing for the motif alone does not guarantee catalytic competence**". The reason is second-shell — residues around the motif "play an important role in mediating affinity, specificity, and reactivity", well documented in natural enzymes and largely absent from motif-centric design.

**dEVA** (design by EVolutionary Algorithm) replaces motif scaffolding with multi-objective optimisation on **NSGA-II**, returning solutions on a **Pareto front** and selecting the knee point rather than maximising any single score. For metal sites it pairs **p(sequence | metal, structure)** from LigandMPNN with **p(metal | sequence, structure)** from [[durr-2023-metal3d]], alternating until the population converges. It is zero-shot in a stronger sense than the campaigns of §4: "it imposes no requirement for structure prediction, natural templates, or evolutionary information". Scaffolds came from [[protpardelle]] and sequences were initialised with ensemble Caliby ([[elnesr-2026-zero-shot-metalloenzyme]]).

**Metal sites without templates** ([[elnesr-2026-zero-shot-metalloenzyme]]). Eight designs, all well expressed as soluble monomers. **desH2C2** — an immunoglobulin-like fold with a **His₂Cys₂ site designed without a motif template** — binds zinc at **K_d = 37 ± 4 nM** at 1:1 stoichiometry, with **EXAFS establishing 2 Zn–N and 2 Zn–S** coordination and a Zn K-edge distinguishable from canonical zinc fingers. Three crystal structures confirm backbone fidelity on demanding folds: a de novo asymmetric β-propeller at **1.48 Å (PDB 12WO)** with zinc resolved **within 0.90 Å of the designed location**, a half-open TIM barrel at **1.55 Å (PDB 12WN)**, and desDEH (PDB 12WM) ([[elnesr-2026-zero-shot-metalloenzyme]]).

**The enzyme.** To obtain catalysis rather than binding, Metal3D was retrained as **Metal3D-Cat** on annotated catalytic zincs from MAHOMES-II, approximating p(catalytic metal | sequence, structure). dEVA returned **only three Pareto-optimal solutions** ([[elnesr-2026-zero-shot-metalloenzyme]]); of these, **desB** emerged active — and carries a **binuclear zinc site**, "the same bi-zinc site that underlies the exceptional efficiency of many naturally occurring metallohydrolases", which it was not told to build. Its novelty is established four ways: **Folddisco and RCSB Structure Motif Search returned no structural motif neighbours, BLAST no sequence homologues, and Foldseek structural neighbours contain no bi-zinc sites** ([[elnesr-2026-zero-shot-metalloenzyme]]).

**The catalysis is the headline.** Phosphomonoester hydrolysis — uncatalysed half-life **>500,000 years** — at **k_cat/K_M = 1300 ± 400 M⁻¹ s⁻¹** (4-MUP), a rate enhancement of **3 × 10¹³**, described as **the highest reported for any de novo designed hydrolase**, and within the range of natural phosphomonoesterases. desB is also promiscuous, hydrolysing **phosphodiesters** — uncatalysed half-lives **>13 million years** — at enhancements of 3 × 10¹¹ and 6 × 10¹² ([[elnesr-2026-zero-shot-metalloenzyme]]). Mechanistic support: ICP-MS confirms two zincs per monomer; alanine scanning of **first- and second-shell** residues reduces activity; alkaline pH optimum is consistent with two proximal zincs lowering metal-bound water's pK_a to ~7; XAS with orthophosphate gives **Zn–Zn ~4.3 Å** in solution, within the range of competent binuclear zinc hydrolases, with EXAFS fitting 4 Zn–N, 1 Zn–P and 1 Zn–Zn. The crystal structure at **2.29 Å (PDB 36BS)** shows **Zn–Zn 5.9 Å** against a design model's 5.8 Å, contrasting with the compressed 4.3 Å on phosphate binding — suggesting an open resting state that closes on substrate.

**How to weigh it.** The result rests on **three Pareto-optimal designs, one of which worked**, and the substrate class was chosen because it dominates Metal3D-Cat's training data, so the demonstration is in-distribution for the objective model even where it is out-of-distribution for the PDB ([[elnesr-2026-zero-shot-metalloenzyme]]). Against that: the site is novel by four independent searches, the rate enhancement is the highest recorded, and nothing about a binuclear zinc centre was specified. The wiki's reading is that this is a genuine second hypothesis about where catalytic competence comes from — **from optimising the coordination environment and its second shell, rather than from transplanting a geometry** — and that §5's preorganization diagnosis is the reason to take it seriously, since second-shell residues are precisely what preorganize a site.

Two senses of "zero-shot" now circulate and the chapter keeps them apart: **no experimental optimisation** ([[butcher-2026-rfdiffusion3-science]]) and **no template, predictor or evolutionary information** ([[elnesr-2026-zero-shot-metalloenzyme]]).

## 8. What actually gets validated

The validation ladder here is deeper than in [[de-novo-binder-design]], because catalysis admits mechanistic tests that binding does not.

**Activity, in two formats.** A **cis** assay fuses substrate to the design so cleavage is intramolecular and reads out as a molecular-weight shift — used with mScarlet and SDS–PAGE in [[chen-2026-metalloproteases]], [[choi-2026-cysteine-proteases]] and [[butcher-2026-rfdiffusion3-science]]. A **trans** assay uses separate substrate, typically FRET-based with GFP/mScarlet or EDANS/Dabcyl reporters. The two do not give the same number: in [[butcher-2026-rfdiffusion3-science]], 56 of 96 designs passed in cis and three were selected as best in trans.

**Mechanism, by knockout.** Catalytic residue to alanine, with the expectation of abolition: Cys and His knockouts abolish activity in [[choi-2026-cysteine-proteases]], while the oxyanion Gln knockout costs only 1.9- to 3.8-fold — a partial dissociation between designed and operative mechanism. Metal dependence is tested by chelation or omission ([[chen-2026-metalloproteases]], [[elnesr-2026-zero-shot-metalloenzyme]]), and cofactor modification by removing it ([[butcher-2026-rfdiffusion3-science]]'s carbamylation test).

**Site identity, by mass spectrometry.** LC–MS confirming cleavage at the intended residue, in all three protease campaigns.

**Kinetics**, as k_cat, K_M and k_cat/K_M, with rate enhancement quoted against a measured uncatalysed rate — **k_uncat = 3.6 × 10⁻¹¹ s⁻¹ at 25 °C, pH 6.8** in [[choi-2026-cysteine-proteases]].

**Structure**, by crystallography, with the designed feature resolved: zinc at full occupancy ([[chen-2026-metalloproteases]]), the catalytic water ([[chen-2026-metalloproteases]]), the binuclear site and its Zn–Zn separation ([[elnesr-2026-zero-shot-metalloenzyme]]).

**Coordination environment in solution**, by **XAS and EXAFS** — unique to [[elnesr-2026-zero-shot-metalloenzyme]] in this wiki, and the only technique here that reports on the metal site in the state the enzyme actually works in rather than in a crystal.

**Ensembles**, by PLACER and MD ([[choi-2026-cysteine-proteases]]), and **energetics**, by machine-learning force fields ([[chen-2026-metalloproteases]]).

**Function in context**: mammalian cells ([[choi-2026-cysteine-proteases]]), full-length human TDP-43 and masked-cytokine activation ([[chen-2026-metalloproteases]]).

### Why these success rates do not compare either

The same caution [[de-novo-binder-design]] §12 raises applies here, with enzyme-specific twists:

| Source | Rate | Denominator | What counts as success |
|---|---|---|---|
| [[choi-2026-cysteine-proteases]] | 13/69 = 19% | designs ordered | cleavage detected in cis by SDS–PAGE/SEC |
| [[chen-2026-metalloproteases]] | 36% of 135 | designs ordered, **two filters pooled** | >10% cleavage, 1 h or 12 h, ± Zn |
| [[chen-2026-metalloproteases]] (Zn-water arm) | 31/38 = 82% | one filter's designs | >10% cleavage at 1 h |
| [[butcher-2026-rfdiffusion3-science]] (TTR) | 56/96 = 58% | designs ordered | >10% cleavage in cis at 18 h |
| [[butcher-2026-rfdiffusion3-science]] (ZAPP) | 4/96 = 4% | designs ordered | activity detected, round 1 |
| [[elnesr-2026-zero-shot-metalloenzyme]] | 1 of 3 | Pareto-optimal solutions | activity above background |

The denominators differ in kind, the incubation times differ by a factor of 18, and the **4% versus 58% within a single paper** shows that the dominant variable is reaction difficulty rather than method quality. Pooling across two filters, as the 36% figure does, is the enzyme analogue of the denominator problems catalogued in [[ruijgrok-2026-binder-pipeline-comparison]].

## 9. Specificity, and designing against disease

Specificity arrives in this chapter in a way it never did in [[de-novo-binder-design]], where §13 records as open whether specificity is ever designed or only observed.

**It emerges unrequested, and is predicted.** [[chen-2026-metalloproteases]] tested cross-reactivity across five scaffold families and found **four of five selective for their cognate substrates even though selectivity was not explicitly enforced**. The fifth, Zn45, was promiscuous — and "this experimentally observed cross-reactivity is consistent with the AF3 screening metrics", i.e. it was visible in advance. Quantified, Zn45 turned over roughly **200 molecules** of a non-cognate substrate per enzyme overnight.

**It is testable against decoys.** [[butcher-2026-rfdiffusion3-science]] measured TTRg11 against **six further β-amyloidogenic sequences all with substantial β-strand propensity** and found much higher activity on the cognate substrate — a harder specificity test than a random panel, because the decoys share the structural propensity the enzyme exploits.

**The structural basis is stated.** Designs bind **8–13-residue substrates**, "creating an extended recognition interface that can encode substantial sequence and conformational selectivity" ([[chen-2026-metalloproteases]]).

**And the targets are real.** [[chen-2026-metalloproteases]] designed proteases against **TDP-43** (residues 320–350), **serum amyloid A** and **amyloid-β**, with rate enhancements to 10⁹-fold; TDPn3 cleaved **full-length human TDP-43** in monomeric and oligomeric forms, though more slowly than the peptide, attributed to liquid–liquid phase separation or precipitation. [[butcher-2026-rfdiffusion3-science]] targeted the TTR fibril core strand, for amyloidosis. Both papers then convert proteases into control elements: [[chen-2026-metalloproteases]] built **masked IL-2 mimics and a masked EGFR antagonist** selectively activated by the designed proteases, achieving "bioorthogonal control of cell state" — the enzyme counterpart of the biosensor applications in [[vasquez-torres-2023-helical-peptide-binders]].

## 10. Open questions

- **Is the residual gap an ensemble problem?** §5's synthesis — that designs optimise a single structure while catalysis depends on a distribution — is supported by the PLACER correlation in [[choi-2026-cysteine-proteases]] and, more strongly, by [[kim-2026-metallohydrolases]], which filtered on PLACER ensembles prospectively, got its best design ranked first, and found same-backbone designs rejected by that filter to be inactive. What is still missing is the controlled comparison: one campaign, one generator, split between an ensemble filter and a single-structure filter, with both arms ordered. No ingested source reports that.
- **Does better preorganization require better *modelling* or better *objectives*?** [[chen-2026-metalloproteases]] names "incorporation of energetic alongside geometric design criteria" as one of four deficits, but every filter in this chapter is geometric plus confidence. Whether an energy term would help, or whether the available energy functions are too inaccurate at these barriers to use, is unaddressed.
- **Motif transplant or coordination-sphere optimisation?** [[elnesr-2026-zero-shot-metalloenzyme]] reports the highest rate enhancement in the chapter from a method that uses no motif, on n = 3 designs; the motif-scaffolding campaigns report lower enhancements on much larger n. No source runs both approaches on one target, so the comparison is unavailable.
- **Why does Riff-Diff reach 45× higher efficiency than RFD2 on the same theozyme?** [[braun-2026-riff-diff]] and [[ahern-2025-rfdiffusion2]] both scaffold the RA95.5-8F retroaldolase tetrad; the former reaches 290 M⁻¹ s⁻¹ from 36 designs, the latter 6.34 M⁻¹ s⁻¹ from 96. Candidate explanations are all plausible and none is isolated: the enumerative artificial-motif library versus learned atomization, the enforced binding pocket via placeholder helix, the backbone refinement cycles, or differing assay and purification conditions. This is the chapter's single most informative unresolved comparison, because it is the only place two independent pipelines attack one identical theozyme.
- **Is the activity ceiling a property of de novo design or of current pipelines?** §5's diagnosis of a 1–4 order-of-magnitude gap holds across the Baker-lab campaigns, but [[braun-2026-riff-diff]] reaches ~90% of an extensively evolved enzyme's catalytic efficiency with 99% enantiomeric excess. Whether that generalises beyond well-studied retro-aldol chemistry, where the catalytic array has been evolution-optimised and is being transplanted rather than invented, is open.
- **How much of each hit rate is the filter?** §6 shows a 24-fold swing from one modelling choice ([[chen-2026-metalloproteases]]). No campaign in the chapter reports an unfiltered baseline, so the generator's own contribution is unmeasured everywhere.
- **What is the oracle's precision for enzymes?** [[lin-2026-genie3]] put a 12% ceiling on binder evaluation pipelines. Nothing equivalent exists for enzymes, and [[elnesr-2026-zero-shot-metalloenzyme]]'s desD1 result suggests it could be worse for metal sites, where a confident prediction may reflect training-set crystallisation artefacts ([[durr-2023-metal3d-supp]]).
- **Does free-atom diffusion beat equivariant representation on enzymes?** [[butcher-2026-rfdiffusion3-science]] and [[lin-2026-genie3]] appeared within days, both arguing that representation gates functional design, and reaching opposite conclusions about SE(3)-equivariance. Neither benchmarks against the other on enzyme tasks, though both report on AME-style problems.
- **Why did RFD2-MI's two campaigns differ so much in hit rate?** [[choi-2026-cysteine-proteases]] got 19% and [[chen-2026-metalloproteases]] got 82% in its better arm, on the same generator and overlapping authors. Candidate explanations — chemistry, filter design, substrate class — are not separated by either paper.
- **Is promiscuity a defect or a finding?** desB hydrolyses two substrate classes separated by 7.5 orders of magnitude in uncatalysed half-life ([[elnesr-2026-zero-shot-metalloenzyme]]), and Zn45 is broadly cross-reactive ([[chen-2026-metalloproteases]]). Whether designed active sites are intrinsically more promiscuous than evolved ones — and why — is unexamined.

## 11. Flagged references — the history this chapter cannot yet cite

Per the sourcing discipline in `CLAUDE.md`; mirrored in [[index]].

**The method the two Nature campaigns are built on:**

1. ~~**RFdiffusion2**~~ — **supplied and ingested 2026-10-21** as [[ahern-2025-rfdiffusion2]] (+ [[ahern-2025-rfdiffusion2-supp]]), *Nature Methods* 23, 96–105 (2026). §3 was rewritten around it. **RFD2-MI remains unsourced and appears to have no methods paper of its own**: [[choi-2026-cysteine-proteases]] cites Bauer et al., *De novo design of phospho-tyrosine peptide binders*, bioRxiv 2025.09.29.678898, while [[butcher-2026-rfdiffusion3-science]] cites the metalloprotease preprint (now [[chen-2026-metalloproteases]]) for the same variant. Recorded as a finding rather than a gap: the variant is described only in passing by its application papers.

**The missing prior art the chapter's framing depends on:**

2. **Designed serine hydrolases** — Lauko, A., Pellock, S. J., Sumida, K. H., Anishchenko, I., Juergens, D., Ahern, W. et al. *Computational design of serine hydrolases.* **Science 388, eadu2454 (2025)**. [[choi-2026-cysteine-proteases]] positions itself as the step past these, and the comparison is the basis of the chapter's claim that amide hydrolysis is the real barrier. Citation now identified from [[butcher-2026-rfdiffusion3-science]]'s reference list; the paper itself is not in `sources/`.
3. **The classical Rosetta enzyme-design era** (Kemp eliminases, retro-aldolases, and the directed-evolution campaigns that followed). [[elnesr-2026-zero-shot-metalloenzyme]] alludes to it — "early attempts to design biocatalysts resulted [in] low initial catalytic rates, requiring subsequent directed evolution" — and nothing primary supports it. Without this, §1 has no account of what the field tried for twenty years.
4. **PLACER** — Anishchenko, I. et al. *Modeling protein–small molecule conformational ensembles with PLACER.* **PNAS 122, e2427161122 (2025)**. Carries the preorganization analysis in [[choi-2026-cysteine-proteases]] and the prospective filtering in [[kim-2026-metallohydrolases]], so it underwrites both §5 and §6. Citation identified; paper not in `sources/`. **Now the highest-priority acquisition in this chapter.**
5. **MAHOMES-II.** The catalytic-metal annotation database that Metal3D-Cat is trained on, and thus the thing that distinguishes a catalytic zinc from a structural one in [[elnesr-2026-zero-shot-metalloenzyme]].
6. **LigandMPNN.** Used by [[elnesr-2026-zero-shot-metalloenzyme]] as one of dEVA's two objectives and by [[cho-2025-protein-hunter]] for ligand tasks; the wiki holds [[dauparas-2022-proteinmpnn]] but not its ligand-aware successor.
7. **The Mechanism and Catalytic Site Atlas (M-CSA)** — Ribeiro, A. J. M., Holliday, G. L., Furnham, N., Tyzack, J. D., Ferris, K. & Thornton, J. M. *Nucleic Acids Res.* **46**, D618–D623 (2018). The source of the AME benchmark curated in [[ahern-2025-rfdiffusion2]], and the nearest thing enzyme design has to a shared benchmark. Also **Dunbrack, R. L. Jr., *Rotamer libraries in the 21st century*, Curr. Opin. Struct. Biol. 12, 431–440 (2002)**, behind the rotamer probability loss in [[butcher-2026-rfdiffusion3-science-supp]].
8. **Caliby** (ensemble Potts-based sequence design), used to initialise sequences in [[elnesr-2026-zero-shot-metalloenzyme]] and appearing as an optional scorer in [[ruijgrok-2026-binder-pipeline-comparison]].

**Supplements and files:**

9. [[elnesr-2026-zero-shot-metalloenzyme]] is `supp: no` — its Figs. S1–S24 and Tables S1–S10 are referenced throughout but not supplied, so the eight-design characterisation set, the Metal3D-Clean comparison and the kinetics fits cannot be inspected.
10. **The RFD3 preprint/published pair.** [[butcher-2025-rfdiffusion3]] and [[butcher-2026-rfdiffusion3-science]] are both retained, with different titles, framings and content. A deliberate reconciliation pass — what the published version dropped, added or revised — has not been done.

## 12. Sources

Ingested sources feeding this chapter, roughly chronologically:

- [[boyken-2016-hydrogen-bond-network-oligomers]] — buried polar satisfaction and the many-body problem · *Science* 2016
- [[anishchenko-2021-hallucination]] (+ [[anishchenko-2021-hallucination-supp]]) — hallucination; anticipates catalytic-site scaffolding · *Nature* 2021
- [[dauparas-2022-proteinmpnn]] (+ [[dauparas-2022-proteinmpnn-supp]]) — the sequence-design step throughout · *Science* 2022
- [[wang-2022-functional-site-scaffolding]] — functional-site scaffolding, the ancestral formulation · *Science* 2022
- [[watson-2023-rfdiffusion]] (+ [[watson-2023-rfdiffusion-supp]]) — conditional diffusion; enzyme active-site scaffolding by minimal-motif fine-tuning · *Nature* 2023
- [[durr-2023-metal3d]] (+ [[durr-2023-metal3d-supp]]) — predicting metal ion location; the p(metal | sequence, structure) objective · *Nat. Commun.* 2023
- [[krishna-2024-rosettafold-all-atom]] (+ [[krishna-2024-rosettafold-all-atom-supp]]) — ligand-aware all-atom design · *Science* 2024
- [[abramson-2024-alphafold3]] (+ [[abramson-2024-alphafold3-supp]]) — the oracle used for apo, complex and TSA states · *Nature* 2024
- [[chu-2024-protpardelle]] (+ [[chu-2024-protpardelle-supp]]) — all-atom generation; the scaffold source for dEVA · *PNAS* 2024
- [[ahern-2025-rfdiffusion2]] (+ [[ahern-2025-rfdiffusion2-supp]]) — RFD2; atomization and unindexed motifs; all 41 AME cases against 16 for prior methods · *Nature Methods* 2025/26
- [[kim-2026-metallohydrolases]] (+ [[kim-2026-metallohydrolases-supp]]) — DFT theozymes; 53,000 M⁻¹ s⁻¹ zinc esterases; PLACER validated as a prospective filter · *Nature* 2026
- [[braun-2026-riff-diff]] (+ [[braun-2026-riff-diff-supp]]) — **independent lineage**; artificial motif libraries and the placeholder helix; evolved-enzyme-rivalling retro-aldolases at 99% ee; MBHases for a non-biological reaction · *Nature* 2026
- [[butcher-2025-rfdiffusion3]] (+ [[butcher-2025-rfdiffusion3-supp]]) — the RFD3 preprint; the AME benchmark · bioRxiv 2025
- [[elnesr-2026-zero-shot-metalloenzyme]] — dEVA; coordination-sphere optimisation; 3 × 10¹³ rate enhancement; the desD1 oracle failure · bioRxiv 2026
- [[choi-2026-cysteine-proteases]] (+ [[choi-2026-cysteine-proteases-supp]]) — de novo cysteine proteases; 13/69; preorganization diagnosed by PLACER · *Nature* 2026
- [[chen-2026-metalloproteases]] (+ [[chen-2026-metalloproteases-supp]]) — de novo zinc proteases; the catalytic-water filtering result; disease targets and caged biologics · *Nature* 2026
- [[butcher-2026-rfdiffusion3-science]] (+ [[butcher-2026-rfdiffusion3-science-supp]]) — free-atom diffusion; zero-shot phosphotriesterases and TTR proteases · *Science* 2026
- [[lin-2026-genie3]] — the competing representational thesis; enzyme-design benchmark · bioRxiv 2026

Related pages: concepts [[catalytic-site-design]], [[metalloprotein-design]], [[motif-scaffolding]], [[diffusion-generative-design]], [[sequence-design]] · topics [[de-novo-binder-design]], [[symmetric-oligomer-design]] · tools [[rfdiffusion]], [[rfdiffusion2]], [[rfdiffusion3]], [[proteinmpnn]], [[alphafold]], [[protpardelle]], [[genie]].
