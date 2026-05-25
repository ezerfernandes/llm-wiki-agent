---
title: "Catastrophic Forgetting"
type: concept
tags: [finetuning, training, continual-learning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Catastrophic Forgetting

A neural-network failure mode in which **a model trained on a new task forgets how to do older tasks**, leading to dramatic performance drops on previously learned capabilities. Coined in the continual-learning literature; cited by [[Kirkpatrick2016EWC|Kirkpatrick et al. (2016)]] in the modern era. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Unfortunately, neural networks are prone to catastrophic forgetting (Kirkpatrick et al., 2016). A model can forget how to do an old task when it's trained on a new task, leading to a significant performance drop on earlier tasks."

## Where this shows up in Ch 7

### Sequential multi-task finetuning

If you finetune the model on task A, then task B, then task C, the resulting model often performs worse on A than the initial post-A checkpoint. The gradient updates for B and C have shifted the parameters away from what task A needs.

### Cross-task degradation in single-task finetuning

Even single-task finetuning can cause forgetting: a model finetuned to handle "change order" requests may regress on "product recommendation" and "general feedback" requests — the case Ch 7 uses to introduce the failure mode (sometimes called "alignment tax").

## The mitigations Ch 7 names

1. **Simultaneous multi-task finetuning** — create a single dataset spanning all tasks. Works but typically requires more data and training time.
2. **[[ModelMerging|Model merging]]** — finetune separately per task (no forgetting), then merge. This is one of Ch 7's headline use cases for merging.
3. **[[PEFT]] with per-task adapters** — multi-LoRA / IA3 serving lets you swap adapters per task without forgetting.

## What's not covered in Ch 7

- **Replay buffers** / experience replay — store and re-train on old task examples.
- **Elastic weight consolidation (EWC)** — penalize updates to parameters important for old tasks.
- **Knowledge distillation from the old model** — train new model to match old model's outputs on old tasks.

These are general continual-learning techniques relevant beyond the application-engineer context.

## Connections

- [[FineTuning]] — the operation where catastrophic forgetting bites.
- [[ModelMerging]] — Ch 7's recommended workaround.
- [[AlignmentTax]] — the sibling term for cross-task degradation.
- [[PEFT]] / [[lora|LoRA]] / [[MultiLoraServing]] — adapter-based mitigations.
- [[Kirkpatrick2016EWC]] — the foundational citation.
- [[ai-engineering-ch07-finetuning]] — primary source.
