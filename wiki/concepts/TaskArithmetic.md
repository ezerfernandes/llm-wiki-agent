---
title: "Task Arithmetic"
type: concept
tags: [model-merging, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Task Arithmetic

**Algebraic operations on [[TaskVector|task vectors]]** to compose, remove, or interpolate model capabilities. Coined by [[Ilharco2022TaskArithmetic|Ilharco et al. (2022)]] — "Editing models with task arithmetic." Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Task vectors allow us to do task arithmetic (Ilharco et al., 2022), such as adding two task vectors to combine task capabilities or subtracting a task vector to reduce specific capabilities. Task subtraction can be useful for removing undesirable model behaviors, such as invasive capabilities like facial recognition or biases obtained during pre-training."

## The operations

| Operation | Formula | Effect |
|---|---|---|
| **Add** | `θ_base + τ_A + τ_B` | Combine capability A and capability B in one model. |
| **Subtract** | `θ_base − τ_unwanted` | Remove an unwanted behavior. |
| **Scale** | `θ_base + α · τ_A` | Adjust the strength of behavior A. |
| **Interpolate** | `θ_base + (1−α) · τ_A + α · τ_B` | Move between two finetunes. |

## What it enables

- **Custom model composition** without retraining.
- **Safety editing** — remove a capability post-hoc via subtraction.
- **Multi-task models** without [[CatastrophicForgetting|catastrophic forgetting]].

## Limitations

Task vectors interfere with one another more as more are added — which is why [[TIESMerging|TIES]] and [[DAREMerging|DARE]] prune redundant task-vector parameters before combining. The simple "add all the task vectors" approach degrades with more constituents.

## Connections

- [[TaskVector]] — the operand.
- [[ModelMerging]] — the operation category task arithmetic lives inside.
- [[LinearCombinationMerging]] — the underlying merge primitive.
- [[TIESMerging]] / [[DAREMerging]] — interference-mitigating variants.
- [[Ilharco2022TaskArithmetic]] — the foundational paper.
- [[ai-engineering-ch07-finetuning]] — primary source.
