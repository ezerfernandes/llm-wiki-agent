---
title: "Compound AI Diagnostic Framework"
type: concept
tags: [prompt-optimization, diagnostic, decision-framework, compound-ai-system]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# Compound AI Diagnostic Framework

A **two-stage practitioner decision framework** introduced by [[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] for deciding whether and how to optimize prompts in a [[CompoundAISystem|compound AI system]] — replacing the default assumption that joint optimization is needed.

## The framework (Figure 3 of the paper)

```
New compound AI pipeline
         │
         ▼
┌─────────────────────────────────────────────┐
│ Stage 1: ANOVA coupling test                │
│   Cost: ~$80, 1 day                         │
│   Grid: 10×10 prompts, n=30 samples         │
└─────────────────────────────────────────────┘
         │
         ├── Interaction significant? (rare)
         │   → Consider joint optimization
         │
         └── F < 1? (typical)
             → Optimize agents independently
                       │
                       ▼
┌─────────────────────────────────────────────┐
│ Stage 2: Headroom test                      │
│   Cost: ~$5, 10 min                         │
│   For bottleneck agent: 10–20 candidates    │
│   Score spread > 2 pts?                     │
└─────────────────────────────────────────────┘
         │
         ├── NO → Use zero-shot
         │       (landscape is flat)
         │
         └── YES → Optimize (APE first)
```

## Stage 1: Coupling test (~$80, 1 day)

Run the [[ANOVAVarianceDecomposition|ANOVA grid]] over $10 \times 10$ prompt combinations on $n = 30$ samples per model×task. Decompose variance via two-way ANOVA with question blocking.

- **If $F_{A \times B} < 1$** → agents are **decoupled**. Optimize each agent independently. Identify the bottleneck agent from main effects.
- **If $F_{A \times B} \geq 1$ and significant** → consider [[JointOptimization|joint optimization]] (the paper has not observed this in any two-agent feed-forward pipeline on mid-tier models).

## Stage 2: Headroom test (~$5, 10 min)

For the bottleneck agent identified in Stage 1, run the [[HeadroomTest|headroom test]]:

- Generate **10–20 candidate prompts**.
- Score against zero-shot on **20 held-out questions**.
- **If best gain > 2 pts** → look for the [[CanButDoesntPattern|"can but doesn't" pattern]] and optimize with [[APE]]-style generate-and-rank.
- **If best gain < 2 pts** → landscape is flat. **Use zero-shot.** Invest effort elsewhere.

## Prerequisite: Model selection

The paper insists on a prerequisite step:

> **Choose the right model first — model selection dominates all prompt-level optimization in our data. Always re-run the following stages after model updates.**

Per [[ModelSpecificityShelfLife|Section 5]] of the paper, which agent matters, which task benefits, and which method works all change with the executor model.

## Cost-benefit (Table 3 of the paper)

| Approach | Cost | What you learn | When to use |
|---|---|---|---|
| **Stage 1: ANOVA coupling test** | ~$80 | Do agents interact? | Always — rules out joint optimization if $F < 1$ |
| **Stage 2: Headroom test** | ~$5 | Is optimization worthwhile? | After Stage 1 — checks if landscape is flat |
| + APE generate-and-rank | ~$20 | Best single-agent prompt | Optional if Stage 2 finds headroom |
| [[DSPy]] compilation | $1K–$5K | Compiled pipeline | Only if coupling test shows significant interaction |
| [[TextGrad]] end-to-end | $5K–$10K | Joint-optimized prompts | Only if coupling test shows significant interaction |

The diagnostic costs ~$85 total and takes 1–2 days. In 3 of the paper's 4 tasks it would have ruled out the $1K–$10K options.

## Frequency: re-run after every model update

The paper's strongest practical recommendation. Optimization headroom is shrinking as base models absorb scaffold techniques (chain-of-thought, structured output, ReAct-style tool use) through RL training. Budget optimization as **recurring, not one-time**.

## Position in the wiki

This is the wiki's **first explicit cost-benefit decision framework for prompt optimization**. It provides a falsifiable gate that the existing wiki sources ([[MIPROv2]] / [[BetterTogether]] / [[GEPA]] / [[2025-bionlp-archehr-qa-neural|Neural at ArchEHR-QA]]) can be retrospectively read through:

- All four wiki successes are tasks that **pass Stage 2** (exploitable output structure: conditional rules, citation-format, JSON, six-metric composite).
- All four use multi-stage [[LMProgram|LM programs]] for which Stage 1 has not been directly tested — Zhang et al.'s Study 1 calls this assumption into question for two-agent pipelines but does not test the specific architectures of the four prior wins.

## Connections

- [[2604.14585-prompt-optimization-coin-flip]] — canonical source.
- [[ANOVAVarianceDecomposition]] — Stage 1 measurement.
- [[HeadroomTest]] — Stage 2 measurement.
- [[AgentCoupling]] — Stage 1 target property.
- [[CanButDoesntPattern]] — Stage 2 target property.
- [[JointOptimization]] / [[IndependentOptimization]] — Stage 1 outcomes.
- [[CoinFlipOptimization]] — the failure mode the framework prevents.
- [[ModelSpecificityShelfLife]] — re-run trigger.
- [[CompoundAISystem]] — structural object.
- [[PromptOptimization]] — parent task.
