---
type: tool
tags: [binder-design, hallucination, alphafold, baseline, not-yet-primary-sourced]
sources: 4
updated: 2026-10-17
---

# BindCraft

A binder-design pipeline that works by **hallucination against AlphaFold2** — optimising a binder sequence against the predictor's confidence and alignment scores by gradient feedback, rather than sampling from a trained generative model.

**No primary source is ingested.** Everything on this page is secondary, from papers that use BindCraft as a baseline. Its primary reference is Pacesa et al. 2025, flagged as the highest-priority acquisition in §14 of [[de-novo-binder-design]]. Until it is supplied, the wiki can say what BindCraft is and that it is the pipeline others benchmark against, but cannot describe its architecture or quote a result of its own.

**What the ingested sources say about it.**

- It is the exemplar of the hallucination class: it "use[s] the confidence and alignment scores of structure predictors to assess interfaces and optimize binder sequences via gradient feedback", scaling the approach pioneered by [[anishchenko-2021-hallucination]] via gradient-based optimisation using AlphaFold2, and building on Goverde et al. 2023 ([[didi-2026-complexa-scaling]]).
- It is a **compute-normalised baseline that gets beaten.** [[didi-2026-complexa-scaling]] compares its test-time search strategies against BindCraft and BoltzDesign at matched test-time GPU-hours and reports higher success rates, noting that BindCraft "uses several stages of optimization that partially rely on ad-hoc" components. It also shows BindCraft can be *accelerated* by initialising it from a generative-model sample.
- Its weakness, as characterised by a competitor: reliance on gradient descent "leads to slow convergence" ([[cho-2025-protein-hunter]]).
- Its benchmarks are a de facto standard — [[cho-2025-protein-hunter]] describes conditional generation tasks as "relevant to binder-design tasks such as the BindCraft benchmarks".
- **It is now beaten by a plain generative model, with numbers.** [[lin-2026-genie3]] calls it "the current state-of-the-art method for binder design" and then, on ten AlphaProteo problems at a fixed 200-structure budget, finds Genie 3 best on 7 and BindCraft best on 3 — with the margin widening once success is normalised by per-sample runtime. In the blind AdaptyvBio Nipah competition, BindCraft submissions had an aggregate hit rate of **1/100** against Genie 3's 1/8, though that paper cautions the competition rates reflect diverse procedures by groups of varying expertise.
- **A named functional weakness.** For the H1 and IL-17A targets, "a sizable proportion of otherwise successful BindCraft designs fail to bind the specified interface" ([[lin-2026-genie3]]) — attributed to hotspot compliance being an ad hoc loss term in hallucination rather than a conditioning input, as it is in a generative model.

**Status in this project.** Carried as a **planned comparator, not onboarded**, in [[ruijgrok-2026-binder-pipeline-comparison]], where it sits at **27% schema coverage with 16 open questions** — no sidechain handling, scoring chain, headline metric, pass-rate denominator, GPU requirement, chain convention or failure modes established. The report lists it explicitly so the gap in coverage is visible rather than silent.

**Why it matters that this page is thin.** BindCraft is, by the account of the papers that benchmark against it, the most widely used open binder-design pipeline in practice. A chapter on binder design that cannot describe it is incomplete in a way no amount of coverage of the Baker-lab stack repairs — see §14 of [[de-novo-binder-design]].

**Connections.** Hallucination lineage: [[anishchenko-2021-hallucination]], [[wicky-2022-symmetric-assembly-design]], [[frank-2024-relaxed-sequence-optimization]]. Beaten under normalised compute by [[complexa]] ([[didi-2026-complexa-scaling]]), on ipTM by [[proteinhunter]] ([[cho-2025-protein-hunter]]), and on 7 of 10 problems plus a competition hit rate by [[genie]] ([[lin-2026-genie3]]). Concept [[binder-design]]; chapter [[de-novo-binder-design]].
