---
title: "APE"
type: concept
tags: [prompt-optimization, llm, baseline]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# APE

**Automatic Prompt Engineer** (Zhou et al. 2023, arXiv:2211.01910). Single-prompt single-stage [[PromptOptimization|prompt optimization]] via reranking brute-force search: an LM generates many candidate instructions for a task, each is evaluated against examples, the highest-scoring one is kept.

The [[2406.11695-mipro|MIPRO paper]] cites APE as one of the **single-prompt antecedents** that Algorithm 1 generalizes. APE is structurally a **proposal-then-filter** algorithm — the natural extension to multi-stage LM programs runs into the [[CreditAssignment|credit-assignment challenge]] that MIPRO addresses.

## Connections

- [[PromptOptimization]] — parent task.
- [[OPRO]] — successor LM-as-optimizer method.
- [[2406.11695-mipro|MIPRO]] — the multi-stage generalization.
- [[EvoPrompt]] — contemporaneous evolutionary alternative.
