---
type: concept
tags: [enzyme-design, catalysis, theozyme, preorganization, active-site]
sources: 14
updated: 2026-10-21
---

# Catalytic site design

Specifying and building the arrangement of atoms that performs a chemical transformation — as distinct from scaffolding it, which is [[motif-scaffolding]], and from binding a substrate, which is [[binder-design]]. The full treatment is the chapter [[enzyme-design]].

**The specification is a theozyme**: a geometric arrangement of catalytic groups around a substrate or transition state. Its provenance varies and the variation is consequential — extracted from a cocrystal with a **transition-state analogue** ([[chen-2026-metalloproteases]]), from a native enzyme structure ([[choi-2026-cysteine-proteases]], using Ulp1 PDB 1EUV), derived from **quantum chemistry** ([[butcher-2026-rfdiffusion3-science-supp]]), or dispensed with entirely in favour of optimising the coordination environment directly ([[elnesr-2026-zero-shot-metalloenzyme]]).

**What a catalytic site must do**, with the sources that establish each:

1. **Activate a nucleophile** — by a hydrogen-bonded Asp–His–Cys triad ([[choi-2026-cysteine-proteases]]) or by a metal activating water ([[chen-2026-metalloproteases]]). Designs achieve this partially: a designed cysteine pK_a shifts from ~8–8.5 to 6.0, against 2.5–4.0 in native enzymes ([[choi-2026-cysteine-proteases]]).
2. **Stabilise high-energy intermediates** via an **oxyanion hole** — the hardest part to design, because buried polar networks are many-body and badly served by pairwise energy functions ([[boyken-2016-hydrogen-bond-network-oligomers]]). Evidence it is incompletely designed: knocking out the oxyanion side chain costs only 1.9- to 3.8-fold ([[choi-2026-cysteine-proteases]]).
3. **Bind and orient the substrate** so the reacting bond is presented correctly — designed proteases use 8–13-residue substrates and an extended recognition interface ([[chen-2026-metalloproteases]]).
4. **Preorganize** all of the above across a multi-step reaction coordinate.

**Preorganization is where the field currently is.** Crystal structures confirm designed active sites are built as specified — Cα r.m.s.d. < 1.2 Å across six structures in [[choi-2026-cysteine-proteases]], 0.82–1.35 Å in [[chen-2026-metalloproteases]] — while catalytic efficiencies remain **10³–10⁴-fold below native** ([[chen-2026-metalloproteases]]). The mechanistic account comes from PLACER ensembles across the catalytic cycle: a non-productive His rotamer suppressed by a single substitution, with the **fraction of productive conformations tracking activity across a design series** ([[choi-2026-cysteine-proteases]]). The wiki's reading is that designs optimise a single structure while catalysis depends on a distribution.

**A design-time corollary with a large measured effect.** What is modelled in the active site during filtering determines the hit rate more than the generator does: including the **catalytic water** in the enzyme–substrate model moved a one-hour hit rate from 3/89 to 31/38, at unchanged numerical thresholds ([[chen-2026-metalloproteases]], [[chen-2026-metalloproteases-supp]]). The converse failure is equally sharp — AlphaFold3 assigned pLDDT 86.55 to a metal in a site with a single coordinating ligand that binds no metal experimentally ([[elnesr-2026-zero-shot-metalloenzyme]]).

**Preorganization is filterable, and has been filtered once prospectively.** [[kim-2026-metallohydrolases]] selected designs on **PLACER** ensembles — a network that randomises the substrate and all side chains within a 600-atom sphere and regenerates them, repeated to give an ensemble — ranked its eventual best design first, and then found that **seven designs from the same backbone family, rejected for suboptimal PLACER metrics, had very low or no activity**. That is the chapter's one prospective demonstration that the ensemble, not the single structure, is the quantity to filter on.

**The ceiling may be a pipeline property, not a method property.** Across the Baker-lab campaigns, efficiencies sit 1–4 orders of magnitude below native. But [[braun-2026-riff-diff]] reaches **290 M⁻¹ s⁻¹ against an extensively evolved enzyme's 320**, with **99% enantiomeric excess**, by enumerating artificial motif libraries and enforcing a binding pocket with a deletable placeholder helix. On the one reaction where two independent pipelines attack the same theozyme, the gap between them is ~45-fold ([[braun-2026-riff-diff]] vs [[ahern-2025-rfdiffusion2]]).

**Sources:** see §12 of [[enzyme-design]].
