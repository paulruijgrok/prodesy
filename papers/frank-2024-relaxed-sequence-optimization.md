---
type: source
title: Scalable protein design using optimization in a relaxed sequence space
authors: Frank, Khoshouei, Fub et al. (Ovchinnikov & Dietz labs)
venue: Science 2024
pdf: "../sources/ProteinDesign/FrankDietz_Science_2024_Scalable protein design using optimization in a relaxed sequence space.pdf"
supp: yes
tags: [hallucination, gradient-descent, alphafold, scalability, oligomers, interfaces, frontier]
ingested: 2026-08-24
---

# RSO — relaxed sequence optimization

Hallucination done with **gradients instead of random search**, by letting the sequence be continuous during optimization. The result scales to single chains of **1000 amino acids**, where diffusion models struggle past ~600.

**Problem.** Hallucination — iterative sequence evolution against a structure-prediction network — was an established alternative to diffusion, but two things had held it back: **slowly converging random-search algorithms** ([[anishchenko-2021-hallucination]], [[wang-2022-functional-site-scaffolding]], [[wicky-2022-symmetric-assembly-design]] are all cited here as the prior art), and the difficulty of implementing robust **gradient descent in a discrete sequence space**. Meanwhile diffusion and flow-matching models ([[watson-2023-rfdiffusion]], [[ingraham-2023-chroma]]) had come to dominate design pipelines. This is precisely the improvement [[anishchenko-2021-hallucination]] anticipated in its closing paragraphs — that the Monte Carlo approach could be made more efficient by tracing gradients back to the inputs.

**Approach.** Backpropagate through AlphaFold2: input a sequence, compute a loss on the predicted structure, backpropagate to the **input sequence**, and use the gradient to update it. The update generally does not produce a one-hot sequence but a **logit-like or position-specific scoring matrix** — a "relaxed" representation in which every position is a weighted superposition of all 20 amino acids. Where earlier methods forced this back to discrete sequence at each step, RSO deliberately **stays in the relaxed space** during optimization, on the hypothesis that operating outside physically realistic sequence space allows smoother, more direct optimization transitions. Only afterwards is the converged **backbone** handed to [[proteinmpnn]] for real sequences, which are then filtered with ESMFold and AF2. Implemented in ColabDesign with normalized gradient descent from a Gumbel-noise initialization; the standard loss combines pLDDT, pAE, a contact term, a radius-of-gyration term and a negative helix weight to counter helical bias ([[frank-2024-relaxed-sequence-optimization-supp]]).

**Key results.**

- **Scale.** RSO produced viable designs up to **1000 amino acids** with **median TM score 0.89** at that length, and lower RMSD than RFdiffusion particularly for large proteins. [[watson-2023-rfdiffusion]] "faced challenges with producing viable backbones beyond 600 amino acids" in the same comparison. GPU efficiency per successful design was similar between the two.
- **Experimental validation.** More than **100 proteins** produced and characterized; **three high-resolution crystal structures** and **two cryo-EM density maps** of designed single chains of up to 1000 residues, one at **1.91 Å Cα-RMSD** to the repredicted design.
- **Novelty scales with size.** Foldseek comparison against the PDB found significant similarity for small designs but progressively fewer homologs for larger ones, which the authors read as RSO leveraging AF2 generalization beyond known protein space.
- **Generality without retraining.** The same framework handles unconditional generation, discontinuous functional-site scaffolding (solving all tasks in the [[watson-2023-rfdiffusion]] benchmark set under a whole-backbone RMSD < 2.0 Å / motif RMSD < 1.0 Å / pLDDT > 85 criterion), binder design, and multi-chain complexes — no retraining for any of it.
- **Interfaces.** Multi-chain designs use AF2's **residue-index gap** trick (an index offset of 50 between chains). Heterodimers designed with two partial radius-of-gyration losses plus a homodimer filter gave monomers that stayed monomeric alone but formed dimers on mixing, with **K_d of 560 nM (MST) and 480 nM (fluorescence polarization)**; a second set ranged from **<4.0 to 790 nM**.

**The adversarial-sequence result, stated mechanistically.** Directly relevant to [[symmetric-oligomer-design]]: the authors tested whether the relaxed sequences could be used *directly* rather than passing backbones to ProteinMPNN. Argmax discretization gave repredicted structures deviating strongly from the target. Simulated annealing from the relaxed sequences improved *in silico* success — but **experimental testing of those annealed sequences still showed poor success rates**, consistent with earlier AF2-only design work. The stated cause is that **AF2 predictions are highly tolerant of mutations, which limits their ability to distinguish valid from adversarial sequences**. Including ProteinMPNN, built specifically to produce valid sequences for a given backbone, is what improves experimental success.

**The oligomerization result.** Also relevant: a second set of heterodimers was designed **omitting the in silico homo-oligomer filter**, and those proteins **independently formed homo-oligomers** at elution concentrations — though at low concentration three of four were monomeric, and all four converted to the intended heterodimer on mixing. Homo-oligomers proper were designed with ColabDesign's `copies` option, which **copies the input logits** and adds interface PAE and contact losses ([[frank-2024-relaxed-sequence-optimization-supp]]).

**Significance.** Two things. First, it reopens the hallucination-versus-diffusion question that [[watson-2023-rfdiffusion]] appeared to settle: on large single chains, the predictor-inversion route now wins. Second, it is the third independent observation in this wiki that **predictor-derived generators produce homo-oligomers unless actively prevented** — after [[anishchenko-2021-hallucination]] and [[wicky-2022-symmetric-assembly-design]] — and the first to state the underlying oracle problem as *mutation tolerance* rather than as overfitting per se. Both threads are developed in [[symmetric-oligomer-design]].

**Connections.**

- Direct successor to [[anishchenko-2021-hallucination]] (shared author: Ovchinnikov), realizing the gradient-based optimization that paper proposed.
- Benchmarked against [[watson-2023-rfdiffusion]]; cites [[ingraham-2023-chroma]] as the other diffusion lineage.
- Depends on [[jumper-2021-alphafold2]] as the differentiable oracle and [[dauparas-2022-proteinmpnn]] for final sequences.
- **Supplement:** [[frank-2024-relaxed-sequence-optimization-supp]] — loss weights, ColabDesign usage, multimer/oligomer protocols, filtering thresholds.
- Concepts: [[diffusion-generative-design]] (as the competing non-diffusion route), [[symmetric-assembly-design]], [[binder-design]], [[motif-scaffolding]]; chapter [[symmetric-oligomer-design]].
