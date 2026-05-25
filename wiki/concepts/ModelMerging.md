---
title: "Model Merging"
type: concept
tags: [finetuning, model-composition, multi-task]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Model Merging

**Combining multiple models' weights into one model that performs better than any of its constituents alone, or that does what its constituents did using less memory.** Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], model merging is the *combination* counterpart to [[FineTuning|finetuning]]'s *adaptation* — finetuning tailors one model; merging combines multiple models. The two are complementary: you can finetune constituent models separately, then merge them.

## Why it's interesting

- **No GPUs required.** Linear-combination and [[SLERP]] merges can run on CPU. This makes merging accessible to indie model developers without compute access.
- **Multi-task alternative to sequential finetuning.** Sequential finetuning is prone to [[CatastrophicForgetting|catastrophic forgetting]]; merging finetunes-in-parallel-then-combines side-steps that.
- **Reduces memory footprint** vs deploying N task-specific models.
- **On-device deployment.** One merged model fits where multiple specialists don't.
- **[[FederatedLearning|Federated learning]]** is naturally a model-merging operation — devices train independently, then weights are merged centrally.

## The three primitives (Ch 7)

### 1. [[Summing|Summing]]

Add weight values of constituent models together. Two named variants:

- **[[LinearCombinationMerging|Linear combination]]** — weighted average. `Merge(A,B) = (w_A·A + w_B·B) / (w_A + w_B)`. Studied since [[Perrone1993|Perrone (1993)]]; the basis of [[ModelSoup|model soups]] (Wortsman et al., 2022). Most effective when constituents are finetunes of the **same base model**.
- **[[SLERP]]** — Spherical Linear Interpolation. Treats each model as a point on a sphere; the merged vector is a point along the geodesic. Defined for two vectors only; merge >2 sequentially.

Often operates on **[[TaskVector|task vectors]]** (finetuned − base) rather than raw weights — enables [[TaskArithmetic|task arithmetic]].

### 2. [[LayerStacking|Layer stacking]] ("frankenmerging" / "passthrough")

Take layers from one or more models and stack them. Can create novel architectures.

- **[[Goliath120B]]** (alpindale, 2023) — 72 of 80 layers from each of two Llama-2-70B finetunes.
- **[[SparseUpcycling|Sparse upcycling]]** ([[Komatsuzaki2022SparseUpcycling|Komatsuzaki et al., 2022]]) — replicate certain layers + add a router → turns a dense model into an [[MixtureOfExperts|MoE]].
- **[[DepthwiseScaling|Depthwise scaling]]** ([[Kim2023SOLAR|Kim et al., 2023]]) — used to build [[SOLAR107B|SOLAR 10.7B]] from a 32-layer 7B.
- **[[MixtureOfAgents]]** ([[TogetherAI]], Wang et al. 2024) — six weak open-source models combined to match [[gpt54|GPT-4o]] on some benchmarks.

Merged models from layer stacking typically need **further finetuning** to perform well.

### 3. [[ConcatenationMerging|Concatenation]]

Append parameters end-to-end. If you concat two [[lora|LoRA]] adapters of ranks r₁ and r₂, the merged adapter's rank is r₁ + r₂. Ch 7 explicitly **does not recommend** this — doesn't save memory vs serving the components separately.

## Pruning before merging: [[TIESMerging|TIES]] and [[DAREMerging|DARE]]

[[Yadav2023TIES|Yadav et al. (2023)]] showed that **resetting up to 80% of a task vector's parameters causes minimal performance degradation** — most finetuning weight updates are redundant. Two methods that prune before merging:

- **[[TIESMerging|TIES]]** (TrIm, Elect Sign, and merge) — Yadav et al. 2023.
- **[[DAREMerging|DARE]]** (Drop And REscale) — Yu et al. 2023.

The bigger insight: **the more constituent models, the more important pruning becomes** — more opportunities for one task's noise to interfere with another's signal.

## Worked use-case scenarios (Ch 7)

- **Per-customer specialization**: finetune one LoRA per customer; merge multiple customers' adapters when needed.
- **Multi-task finetuning without catastrophic forgetting**: parallel single-task finetunes, then merge.
- **Model upscaling**: build a bigger model from a smaller pre-trained one without paying for a from-scratch training run.

## What model merging is *not*

[[ModelEnsemble|Model ensembling]] combines model **outputs**, not weights. Each request runs all constituent models; final answer is combined (e.g., majority vote). Ensembling preserves each model's behavior but pays N× inference cost. Merging combines weights once, pays 1× at inference. Per Ch 7: *"Just like model ensembles used to dominate leaderboards, many models on top of the Hugging Face's Open LLM Leaderboard are merged models."*

## Connections

- [[FineTuning]] — the *adaptation* operation that merging *combines*.
- [[CatastrophicForgetting]] — the problem merging solves for multi-task setups.
- [[TaskVector]] / [[TaskArithmetic]] — the operands underlying linear-combination merging.
- [[LinearCombinationMerging]] / [[SLERP]] / [[LayerStacking]] / [[ConcatenationMerging]] — the three primitives.
- [[TIESMerging]] / [[DAREMerging]] — pruning-before-merging methods.
- [[ModelSoup]] — the canonical "average all your finetunes" technique.
- [[FederatedLearning]] — naturally a merging operation.
- [[ModelEnsemble]] — the output-combining alternative.
- [[MixtureOfExperts]] — sparse upcycling produces MoEs.
- [[Goliath120B]] / [[SOLAR107B]] / [[MixtureOfAgents]] — canonical merged models.
- [[ai-engineering-ch07-finetuning]] — primary source.
