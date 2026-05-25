---
title: "Information-Based Failure"
type: concept
tags: [failure-modes, rag, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Information-Based Failure

A model failure mode where **the model lacks information** — outputs are factually wrong, outdated, or made up. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], this is one of two failure-mode categories that drive the RAG-vs-finetuning decision (the other being [[BehaviorBasedFailure]]).

## Two scenarios (Ch 7)

### The model doesn't have the information

> "Public models are unlikely to have information private to you or your organization. When a model doesn't have the information, it either tells you so or hallucinates an answer."

### The model has outdated information

> "If you ask: 'How many studio albums has Taylor Swift released?' and the correct answer is 11, but the model answers 10, it can be because the model's cut-off date was before the release of the latest album."

## The fix: [[rag|RAG]], not finetuning

Per Ch 7's core rule — **"finetuning is for form, and RAG is for facts"** — information-based failures call for [[rag|RAG]]. The model retrieves the current/private information at inference time rather than relying on what was baked into its weights.

## Empirical support: [[Ovadia2024FineTuningOrRetrieval|Ovadia et al. (2024)]]

For a current-events QA task across Mistral-7B / Llama-2-7B / Orca-2-7B:
- Base model alone: poor.
- Base model + RAG: best.
- Finetuned model alone: worse than base + RAG.
- Finetuned model + RAG: usually worse than base + RAG.

**Finetuning on current events doesn't help; RAG does.** The finetune can't substitute for fresh information.

## Connections

- [[BehaviorBasedFailure]] — the sibling failure category that *does* call for finetuning.
- [[rag|RAG]] — the fix.
- [[FineTuning]] — *not* the fix for information failures (despite practitioner intuition).
- [[Hallucination]] — the surface manifestation.
- [[Ovadia2024FineTuningOrRetrieval]] — empirical study.
- [[ai-engineering-ch07-finetuning]] — primary source.
