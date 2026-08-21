# Glossary {#glossary}

Concise definitions of the recurring terms in this book. Where a term has its own chapter or concept entry, follow its cross-references for the full treatment.

AF2 / AF3
:   AlphaFold 2 and AlphaFold 3, DeepMind's structure predictors. AF2 predicts protein monomers and complexes from an MSA; AF3 replaces the structure module with a diffusion decoder and generalises to nucleic acids, ligands and modified residues.

All-atom design
:   Generative design that places side-chain (and often ligand) atoms jointly with the backbone, rather than generating a backbone first and assigning sequence afterwards. Contrast *two-stage design*.

Backbone
:   The repeating N–Cα–C(=O) chain of a protein, ignoring side chains. Most first-generation generative models produce backbones only.

Binder
:   A designed protein that binds a specified target with useful affinity and specificity. See the binder-design chapter.

Chroma
:   Generate Biomedicines' programmable generative model, which diffuses under a polymer-statistics prior and steers sampling with modular conditioners.

Codesign
:   Generating structure and sequence simultaneously in one model, as opposed to designing sequence onto a fixed backbone.

Conditioner
:   A module that biases a diffusion model's sampling toward a constraint (symmetry, shape, substructure, a natural-language or property target) without retraining the base model.

CASP
:   Critical Assessment of Structure Prediction — the biennial blind community benchmark on which AlphaFold2's accuracy was first established.

Denoising / reverse diffusion
:   The generative process in a diffusion model: start from noise and iteratively remove it, each step conditioned on the model's current estimate of the clean structure.

De novo design
:   Designing a protein from scratch rather than modifying a natural one.

Diffusion model
:   A generative model trained to reverse a gradual noising process; the dominant architecture for structure generation (RFdiffusion, Chroma, Protpardelle, RFdiffusion3).

Evoformer
:   AlphaFold2's trunk: paired sequence and residue-pair representations updated by attention with triangle operations that enforce geometric consistency.

FAPE (frame-aligned point error)
:   AlphaFold2's training loss, comparing predicted and true atom positions in every residue's local frame — rotation- and translation-invariant, and sensitive to local as well as global error.

Foldseek
:   A fast structural-alignment search tool; used in design pipelines to test whether a generated backbone resembles anything in the PDB (i.e. how novel it is).

Fold switching
:   The ability of one sequence to adopt more than one distinct fold — a known failure mode for single-conformation structure prediction.

Hallucination
:   Design by optimising a sequence so that a structure predictor confidently folds it into something — the input is an objective, not a target backbone. The route used for early motif scaffolding and symmetric assemblies.

Hotspot residues
:   Target-surface residues specified as the intended contact patch when designing a binder.

Inpainting
:   Filling in missing structure or sequence around a fixed region, the complement of hallucination for motif scaffolding.

Inverse folding
:   Predicting a sequence that will fold into a given backbone — the problem ProteinMPNN solves. Synonym in practice for *fixed-backbone sequence design*.

IPA (invariant point attention)
:   The attention mechanism in AlphaFold2's structure module that operates on 3D points in residue frames and is invariant to global rotation and translation.

lDDT / pLDDT
:   The local distance difference test, a superposition-free measure of local structural accuracy; **pLDDT** is a model's per-residue self-estimate of it, widely reused as a design filter.

MaSIF
:   Molecular surface interaction fingerprints — geometric deep learning on protein surfaces, used to find and design interaction patches.

Motif scaffolding
:   Building a new protein around a fixed functional site (a binding motif, an active site) so the motif's geometry is preserved.

MPNN
:   Message-passing neural network; in this field usually shorthand for ProteinMPNN.

MSA (multiple sequence alignment)
:   A stack of evolutionarily related sequences whose covariation encodes contact information; the input signal that made AlphaFold2 accurate, and a dependency later models try to reduce.

Oracle
:   A predictor used to score designs *in silico* before synthesis — typically AlphaFold2, which both filters designs and (via hallucination) can be optimised against.

pAE / PAE (predicted aligned error)
:   A predicted pairwise error matrix; `pAE_interaction` across a designed interface is a standard in silico discriminator of binders that will work experimentally.

Partial diffusion
:   Noising an existing design only part-way and re-denoising it, to sample local variants around a promising solution rather than starting from scratch.

PDB
:   The Protein Data Bank — the archive of experimentally determined structures that trains and benchmarks essentially every model in this book.

ProteinMPNN
:   The Baker-lab graph neural network for fixed-backbone sequence design; fast, high sequence-recovery, and the default sequence step in most design pipelines.

Protpardelle
:   The Huang-lab all-atom generative model, which handles side chains via a superposition over side-chain states.

RFAA (RoseTTAFold All-Atom)
:   The Baker-lab generalised predictor covering proteins with small molecules, nucleic acids and covalent modifications; the basis for RFdiffusionAA.

RFdiffusion
:   The Baker-lab diffusion model that generates protein backbones, fine-tuned from RoseTTAFold; the workhorse for de novo backbones, motif scaffolding, symmetric oligomers and binders.

RFdiffusion3
:   The all-atom successor generating tokens and atoms directly, substantially cheaper to sample and extended to nucleic-acid and small-molecule interactions.

RMSD (root-mean-square deviation)
:   The standard measure of structural agreement between two aligned structures; design success is usually defined by an RMSD threshold between the design model and the predictor's refolded prediction.

Rosetta
:   The physics- and knowledge-based macromolecular modelling suite that defined computational protein design before deep learning, and still supplies energy functions and relax/repack protocols.

Scaffold
:   (1) The designed protein framework that presents a functional motif; (2) a reusable natural framework (nanobody, monobody, fibronectin III domain) engineered for new binding.

Self-conditioning
:   Feeding a diffusion model its own previous-step structure prediction as extra input; a large empirical accuracy gain in RFdiffusion.

Sequence recovery
:   The fraction of native residues a sequence-design model reproduces when given a native backbone — the standard in silico metric for inverse folding.

Structure module
:   AlphaFold2's final block, which converts the Evoformer representations into explicit 3D coordinates via residue frames and IPA.

Symmetric assembly
:   A designed homo-oligomer with cyclic (C*n*), dihedral (D*n*) or point-group symmetry; symmetry is imposed during generation rather than discovered.

Test-time compute
:   Spending more sampling or search effort per design at inference (more seeds, more denoising steps, re-ranking) to buy success rate without retraining.

Tokenization
:   How a model discretises a biomolecular system into units — residues, atoms, or a mixture — which determines what kinds of molecules it can represent.

Two-stage design
:   The dominant pipeline: generate a backbone (RFdiffusion), then design a sequence onto it (ProteinMPNN), then verify by refolding (AlphaFold2). Contrast *codesign* and *all-atom design*.

Yeast display
:   A high-throughput experimental screen presenting designed proteins on the yeast surface, used to measure binding across large design libraries.
