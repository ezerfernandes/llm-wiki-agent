---
title: "XSum"
type: concept
tags: [benchmark, summarization, nlp]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# XSum

**XSum** (Narayan, Cohen & Lapata, EMNLP 2018) — *"Don't give me the details, just the summary!"* — is an **extreme summarization** benchmark of BBC news articles paired with single-sentence summaries. Topic-aware convolutional models established the original baseline; LLM era treats it as a free-form generation task with LM-judge scoring.

## In Zhang et al. 2026 (the rare cross-study benchmark)

[[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] use XSum in **both** their studies — the only task to appear in both:

**Study 1 (agent coupling, two-agent pipeline).** XSum was the *a priori* "loose coupling" prediction — summarization seems to be a single-step task. Result: confirms loose coupling — interaction explains 0.49% of total variance on Haiku, 0.87% on Nova; all $F < 1.0$ and $p > 0.52$. Question difficulty dominates (80.3% Haiku, 58.4% Nova).

**Study 2 (single-agent optimization).** XSum is one of the three **free-form** tasks (alongside [[FeedbackBench]], [[WildBench]]) where optimization fails to beat zero-shot reliably. Best gain across six methods: **+0.6 pts** (within the noise floor of 20-question evaluation). Average gain across all methods: **−0.17 pts** on Haiku.

XSum is the canonical **negative example** for the [[HeadroomTest|headroom test]]: the model's zero-shot summarization is already near-optimal for the free-form format, leaving no [[CanButDoesntPattern|"can but doesn't" gap]] for optimization to exploit.

## Cross-study bridge

XSum's appearance in both studies provides a direct bridge: even on a task where Study 1 measures no agent coupling (so Stage 1 of the [[CompoundAIDiagnostic|diagnostic]] passes), Study 2 measures no single-agent headroom either (so Stage 2 fails). The framework's two-gate structure is needed because the gates measure orthogonal properties.

## Connections

- [[2604.14585-prompt-optimization-coin-flip]] — the only canonical wiki source.
- [[FeedbackBench]] / [[WildBench]] — sibling free-form tasks that fail the [[HeadroomTest]].
- [[HelpSteer2]] — the optimizable counterexample (structured-rubric output).
- [[CanButDoesntPattern]] — the property XSum lacks.
- [[HeadroomTest]] — the diagnostic that flags XSum as not worth optimizing.
- [[AgentCoupling]] — the structural property Study 1 measures on XSum.
- [[hotpotqa]] / [[MBPP]] — sibling Study 1 tasks.
