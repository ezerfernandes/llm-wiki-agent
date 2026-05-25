---
title: "HelpSteer2"
type: concept
tags: [benchmark, helpfulness, rating, reward-model]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# HelpSteer2

**HelpSteer2** (Wang, Dong, Delalleau, Zeng, Shen, Egert, Zhang, Sreedhar & Kuchaiev, arXiv:2406.08673, 2024) is an **open-source dataset for training top-performing reward models**, requiring **structured rubric-based evaluation with JSON-formatted output** across multiple dimensions (helpfulness, correctness, coherence, complexity, verbosity).

## The structural property that makes HelpSteer2 special

In [[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]]'s four-task Study 2, **HelpSteer2 is the sole task where prompt optimization works** — all six methods beat zero-shot on [[ClaudeHaiku45|Claude Haiku 4.5]] (best $\Delta = +6.8$ from [[EvoPrompt]]).

The reason: HelpSteer2 is the **canonical example of the [[CanButDoesntPattern|"can but doesn't" pattern]]**:

- The model **can produce** the JSON-rubric output — when prompted correctly, scores jump from **68.0 → 74.8**.
- The model's **zero-shot default is unstructured prose** — failing to produce the schema HelpSteer2 expects.
- Optimization unlocks the latent format-following capability.

All methods reaching ≥74 pts **independently discover the same JSON-rubric structure** — strong evidence that the optimization landscape has a clear feature to exploit (rather than the noisy interaction surface seen in the other three tasks).

## Results across methods (Table 2, Claude Haiku)

| Method | HelpSteer2 score |
|---|---|
| Zero-Shot | 68.0 |
| [[APE]] | 69.3 |
| [[OPRO]] | 73.8 |
| [[EvoPrompt]] | **74.8** |
| [[PromptBreeder]] | 74.6 |
| DSPy-style ([[BootstrapFewShot]]) | 69.8 |
| [[PROSEOptimizer\|PROSE]] | 74.4 |

**Best gain: +6.8 pts**. The largest in Zhang et al. Study 2.

## Model specificity: HelpSteer2 flips on Nova

On [[AmazonNovaLite|Amazon Nova Lite]] (Table 4):

- Only **1 of 6** methods beats zero-shot on HelpSteer2 (best $+2.1$ from PromptBreeder).
- The 6/6 wins on Haiku reduce to 1/6 on Nova — **a complete reversal**.

This is one of the wiki's clearest empirical examples of [[ModelSpecificityShelfLife|model-specific optimization headroom]]. The JSON-rubric format Haiku does not default to but can produce → Nova may default to closer to the expected format already (eliminating the gap) or may lack the latent capability altogether (saturating the gap at zero).

## Generation context

[[2604.14585-prompt-optimization-coin-flip|Zhang et al.]] flag HelpSteer2 as evidence for a broader claim:

> *"We hypothesize this pattern generalizes to tasks requiring specific output schemas (JSON, XML), domain-specific formatting conventions, or structured reasoning templates — any setting where the model has latent capability that a well-chosen prompt can unlock."*

The wiki's other JSON-schema unlocks ([[QuizGen]] valid-JSON 37.6 → 100% via [[2312.13382-dspy-assertions|DSPy Assertions]]; [[2025-bionlp-archehr-qa-neural|Neural at ArchEHR-QA 2025]]'s strict citation-format + ≤75-word + six-metric composite reward; [[HotPotQAConditional]]'s entity-type-conditional answer format with MIPRO) all align with this hypothesis.

## Connections

- [[2604.14585-prompt-optimization-coin-flip]] — canonical source for HelpSteer2's role as the "can but doesn't" exemplar.
- [[CanButDoesntPattern]] — the property HelpSteer2 instantiates.
- [[HeadroomTest]] — the test HelpSteer2 passes.
- [[ModelSpecificityShelfLife]] — Nova reversal evidence.
- [[FeedbackBench]] / [[WildBench]] / [[XSum]] — the three sibling tasks that fail Study 2.
- [[Prometheus2]] — open-source evaluator the rubric dimensions align with.
- [[QuizGen]] / [[HotPotQAConditional]] / [[2025-bionlp-archehr-qa-neural]] — wiki analogues with similar structural unlocks.
