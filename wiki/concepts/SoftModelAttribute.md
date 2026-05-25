---
title: "Soft Model Attribute"
type: concept
tags: [model-selection, methodology, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Soft Model Attribute

A model attribute **you can improve** through prompting, finetuning, or other adaptation. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Soft attributes are attributes that can be improved upon, such as accuracy, toxicity, or factual consistency."

## Examples

- Accuracy on your specific task.
- [[FactualConsistency|Factual consistency]] / hallucination rate.
- Toxicity rate.
- [[InstructionFollowingCapability|Instruction-following]] reliability.
- Latency (only if you self-host).

## The optimism trap

Huyen's heuristic on estimating soft-attribute improvability:

> "I've had situations where a model's accuracy hovered around 20% for the first few prompts. However, the accuracy jumped to 70% after I decomposed the task into two steps. At the same time, I've had situations where a model remained unusable for my task even after weeks of tweaking, and I had to give up on that model."

The honest framing: *"it can be tricky to balance being optimistic and being realistic."*

## Position in model selection

Soft attributes are what you target in [[ModelSelectionWorkflow|step 3]] (private experiments) of the four-step workflow. Hard attributes filter the pool; soft attributes determine the winner within the filtered pool.

## Context-dependence

A latency that's a [[HardModelAttribute|hard attribute]] when you use a model API becomes a soft attribute when you self-host, because you can [[Quantization|quantize]], batch, or otherwise optimize.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[HardModelAttribute]] — the complement.
- [[ModelSelectionWorkflow]] — where soft attributes drive decisions.
- [[PromptEngineering]] / [[FineTuning]] — the techniques that move soft attributes.
- [[EvaluationPipeline]] — what measures soft-attribute changes.
