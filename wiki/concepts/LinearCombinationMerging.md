---
title: "Linear Combination Merging"
type: concept
tags: [model-merging, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Linear Combination Merging

The simplest [[ModelMerging|model merging]] primitive: **(weighted-)average the weights of multiple models**. For models A and B:

$$\mathrm{Merge}(A, B) = \frac{w_A A + w_B B}{w_A + w_B}$$

When `w_A = w_B = 1`, this is the unweighted mean. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], this approach **works surprisingly well given its simplicity**, and has been studied since the early 1990s ([[Perrone1993]]).

## Where it's used

- **[[ModelSoup|Model soups]]** ([[Wortsman2022ModelSoups|Wortsman et al., 2022]]) — averaging the entire weights of multiple finetuned models improves accuracy without increasing inference time.
- **[[FederatedLearning|Federated learning]]** ([[Wang2020FederatedAveraging|Wang et al., 2020]]) — the central merge step.
- **Multi-task finetuning** — finetune separately per task, then merge — Ch 7's alternative to sequential FT with [[CatastrophicForgetting|catastrophic forgetting]].
- **Adapter combining** — more common than whole-model merging; combine [[lora|LoRA]] adapters via linear combination.

## When it works best

Per Ch 7: **for models finetuned on top of the same base model**. In this case, linear combination is naturally understood through [[TaskVector|task vectors]] (`τ_i = θ_i − θ_base`) and admits [[TaskArithmetic|task arithmetic]].

For models that *don't* share a base — different architectures, sizes, or training data — linear combination still works but typically needs **alignment** first ([[Singh2020ModelFusion|"Model Fusion via Optimal Transport"]] (Singh & Jaggi, 2020); [[Ainsworth2022GitReBasin|"Git Re-Basin"]] (Ainsworth et al., 2022); [[Tam2023MergingByMatching|"Merging by Matching Models in Task Parameter Subspaces"]] (Tam et al., 2023)). Alignment ensures that *functionally related* parameters average together rather than being summed under arbitrary permutations.

## Why alignment matters

Different finetunes of the same architecture can land in **different basins** of the loss landscape — semantically related neurons may be at different indices in the weight tensor. Naive linear-combination averaging then mixes unrelated neurons together. Alignment first permutes the layers to put functionally related neurons at the same positions.

## Variants

- **[[ModelSoup|Model soup]]** — average finetunes of the same task.
- **[[SLERP]]** — spherical interpolation, an alternative to linear interpolation.
- **[[TaskArithmetic|Task-arithmetic merging]]** — average task vectors (or do other arithmetic), then add to the base.

## Connections

- [[ModelMerging]] — parent operation.
- [[SLERP]] — geodesic alternative.
- [[TaskVector]] / [[TaskArithmetic]] — the natural operand framework.
- [[ModelSoup]] — the dominant whole-model linear-combination application.
- [[FederatedLearning]] — the distributed learning application.
- [[Perrone1993]] / [[Wortsman2022ModelSoups]] / [[Wang2020FederatedAveraging]] — citations.
- [[ai-engineering-ch07-finetuning]] — primary source.
