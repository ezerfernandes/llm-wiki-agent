---
title: "Alignment Tax"
type: concept
tags: [finetuning, alignment, training]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Alignment Tax

The performance loss on tasks A, B, ..., that a model suffers as a side effect of being finetuned (or aligned) on task C. Coined by Bai et al. (2020) in the context of [[rlhf|RLHF]]. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Finetuning a model for a specific task can improve its performance for that task, [but] it can degrade its performance for other tasks. Some people call this phenomenon an alignment tax (Bai et al., 2020), but this term can be confused with penalties against human preference alignment."

## Mechanism

Same as [[CatastrophicForgetting|catastrophic forgetting]] — the gradient updates needed to do task C well move the model's parameters away from the basin that supports tasks A and B.

## Why Ch 7 hedges on the term

The term "alignment tax" was originally used in the [[rlhf|RLHF]] / preference-finetuning context. Some practitioners now use it for any finetuning-induced cross-task degradation. The ambiguity makes Ch 7 cautious about it — preferring to describe the phenomenon than name it.

## When you'll feel the alignment tax

- You finetune for one query type, then notice the model regresses on other query types in production.
- A new aligned base model release is worse on some benchmarks than its un-aligned predecessor.
- Your single-purpose finetune underperforms the original general model on tasks outside its training distribution.

## How to mitigate

Per Ch 7's recommendations (also applicable to catastrophic forgetting):
1. **Finetune on all query types you care about**, not just the failing one.
2. **Use [[ModelMerging|model merging]]** — finetune separately, merge after.
3. **Use [[PEFT|per-task PEFT adapters]]** — swap [[lora|LoRA]] adapters per query type.
4. **Consider separate models** for fundamentally distinct tasks if merging hurts.

## Connections

- [[CatastrophicForgetting]] — the structurally identical failure mode in continual-learning terminology.
- [[FineTuning]] — the operation where alignment tax appears.
- [[PreferenceFinetuning]] / [[rlhf|RLHF]] — the original alignment-tax context.
- [[ModelMerging]] — Ch 7's recommended workaround.
- [[ai-engineering-ch07-finetuning]] — primary source.
