---
title: "Assertion-Driven Example Bootstrapping"
type: concept
tags: [concept, dspy, optimizer, bootstrap, assertions]
sources: [2312.13382-dspy-assertions]
last_updated: 2026-05-22
---

# Assertion-Driven Example Bootstrapping

**Assertion-driven example bootstrapping** is the first of two compile-time optimizations enabled by [[LMAssertions|LM Assertions]] ([[2312.13382-dspy-assertions|Singhvi, Shetty, Tan et al. 2024]]). It applies [[AssertionDrivenBacktracking|assertion-driven backtracking]] to the **teacher model** inside [[BootstrapFewShot|`BootstrapFewShot`]] / [[BootstrapFewShotWithRandomSearch|`BootstrapFewShotWithRandomSearch`]] during the demonstration-bootstrapping phase.

## The problem it solves

Standard `BootstrapFewShot` runs the teacher on training examples, keeps the runs whose *final* output passes the metric, and serializes those runs' intermediate-module traces as few-shot demonstrations for the student. The hidden flaw the paper diagnoses:

> "Based on our observation, in some cases, the naïve optimizer would bootstrap an example with the correct final response while the intermediate module outputs are incorrect, which leads to wrong demos for intermediate LM modules."

A teacher whose final answer was correct but whose internal queries were malformed, repetitive, or violated the program's invariants ends up teaching the student to emit malformed queries — the final-answer metric doesn't constrain intermediate behavior.

## The fix

The teacher is wrapped with the [[AssertionDrivenBacktracking|assertion-driven backtracking]] mechanism. Every demonstration the optimizer collects must therefore pass:

1. The original final-answer metric (as before).
2. **Every [[DSPyAssert|`Assert`]] and [[DSPySuggest|`Suggest`]] in the program** — at every intermediate module.

Bootstrapped demonstrations are now guaranteed to follow the intermediate constraints, not only the final-answer metric.

> "In this way, although the prompt optimizer only has the metric for the final answer, the examples selected will have higher qualities for all intermediate modules thanks to LM Assertions."

## Position in the optimizer matrix

The paper's Table 1 names two compile-time strategies that use this:

| Strategy | Compile-time | Inference-time |
|---|---|---|
| `Compile w/ Assert` | ✓ assertion-driven bootstrap + [[CounterexampleBootstrapping\|counterexample]] | ✗ |
| `C+Infer w/ Assert` | ✓ assertion-driven bootstrap + [[CounterexampleBootstrapping\|counterexample]] | ✓ [[AssertionDrivenBacktracking\|backtracking]] |

`Compile w/ Assert` removes inference-time retry overhead while still benefiting from assertion-aware demonstrations. The paper notes this can match or exceed `Compile` baselines without backtracking cost:

> "Overall, with counterexample bootstrapping only, the overhead of backtracking and self-refinement for the student model is completely eliminated while the program still has the ability to generate more responses that adhere to programmer-defined assertions."

## Empirical effect

Compare `Compile` vs `Compile w/ Assert` (compile-time gains only, inference-time identical):

- **TweetGen Engaging (dev/test)**: 1.0 / 2.0 → 74.0 / 73.0 — adding assertion-aware bootstrapping lifts engagement-pass-rate from near-zero to ~73%.
- **QuizGen Validity**: 81.7 → 80.5 — flat (the metric was already saturating).
- **MultiHopQA Suggestions Passed**: 71.3 → 78.3 — modest but real.

The dramatic TweetGen number is the paper's headline result for the compile-only setting.

## Related

- [[BootstrapFewShot]] — host optimizer.
- [[BootstrapFewShotWithRandomSearch]] — the random-search variant used in the paper.
- [[CounterexampleBootstrapping]] — sibling compile-time optimization (negative demonstrations).
- [[AssertionDrivenBacktracking]] — the runtime mechanism repurposed at compile time.
- [[LMAssertions]] — the construct family.

## Tracked sources

- **[[2312.13382-dspy-assertions]]** (2024) — the introducing paper.
