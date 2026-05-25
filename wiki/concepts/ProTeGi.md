---
title: "ProTeGi"
type: concept
tags: [prompt-optimization, gradient-descent, beam-search]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# ProTeGi

**ProTeGi** (Pryzant, Iter, Li, Lee, Zhu & Zeng, arXiv:2305.03495, 2023) is a single-prompt optimizer that performs **automatic prompt optimization with "gradient descent" and beam search**: an LM acts as a critic generating natural-language "gradients" (i.e. error signals) over the current prompt's failures, and a beam search expands the most promising edits.

The "textual gradient" framing in ProTeGi is the direct antecedent of [[TextGrad]]'s multi-component generalization (2025).

## Position

ProTeGi sits in the LM-as-critic branch of single-prompt [[PromptOptimization|prompt optimization]], alongside [[APE]] / [[OPRO]] / [[EvoPrompt]] / [[PromptBreeder]] in the single-prompt prior-art family. [[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] cite ProTeGi as one of the single-prompt prior works — it is **not** included in the six-optimizer benchmark, but is referenced as part of the family of single-call prompt optimizers that *"does not address inter-agent dependencies."*

## Connections

- [[TextGrad]] — multi-component descendant of ProTeGi's textual-gradient framing.
- [[2604.14585-prompt-optimization-coin-flip]] — cites ProTeGi in related work.
- [[APE]] / [[OPRO]] / [[EvoPrompt]] / [[PromptBreeder]] — sibling single-prompt optimizers.
- [[PromptOptimization]] — parent task.
