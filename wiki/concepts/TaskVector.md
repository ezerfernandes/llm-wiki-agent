---
title: "Task Vector"
type: concept
tags: [model-merging, finetuning, task-arithmetic]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Task Vector

**The vector you get by subtracting a base model's weights from a finetuned model's weights.** Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "The idea is that once you've finetuned a model for a specific task, subtracting the base model from it should give you a vector that captures the essence of the task. Task vectors are also called **delta parameters**."

Formally: `τ_task = θ_finetuned − θ_base`. If you finetune with [[lora|LoRA]], the LoRA weights (A · B product) *are* the task vector.

## Why task vectors matter

Task vectors are the operand of **[[TaskArithmetic|task arithmetic]]** ([[Ilharco2022TaskArithmetic|Ilharco et al., 2022]]):

- **Add task vectors** → combine task capabilities. `θ_merged = θ_base + τ_A + τ_B`.
- **Subtract a task vector** → remove a capability. `θ_safer = θ_base − τ_undesirable`.

Task subtraction can be used to **remove undesirable model behaviors** — Ch 7 mentions facial recognition and pre-training biases as examples of capabilities you might want to subtract.

## Connection to model merging

Most [[LinearCombinationMerging|linear-combination model merging]] is most naturally understood as task-vector arithmetic on top of a shared base model. The constituents are *deltas from a common base*, not arbitrary model snapshots.

This is also why linear-combination merging is **most effective for models finetuned on the same base** — when the constituents share `θ_base`, the deltas live in a meaningfully comparable vector space.

## Connection to [[TIESMerging|TIES]] / [[DAREMerging|DARE]]

Most parameters in a task vector are **redundant** — finetuning made small adjustments to most parameters that don't materially affect task performance. [[Yadav2023TIES|Yadav et al. (2023)]] showed that **keeping the top 20% of task-vector parameters matches keeping 100%**. The implication: task vectors are *sparse signals diluted by noise*, and pruning the noise improves merge quality, especially as the number of constituents grows.

## Connections

- [[ModelMerging]] — the operation that uses task vectors as operands.
- [[TaskArithmetic]] — the algebra over task vectors.
- [[LinearCombinationMerging]] — the standard task-vector merge.
- [[TIESMerging]] / [[DAREMerging]] — pruning-aware merging.
- [[lora|LoRA]] — the LoRA delta is a task vector by construction.
- [[Ilharco2022TaskArithmetic]] — the foundational paper.
- [[ai-engineering-ch07-finetuning]] — primary source.
