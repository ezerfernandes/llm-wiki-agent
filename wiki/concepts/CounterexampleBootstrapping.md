---
title: "Counterexample Bootstrapping"
type: concept
tags: [concept, dspy, optimizer, bootstrap, assertions]
sources: [2312.13382-dspy-assertions]
last_updated: 2026-05-22
---

# Counterexample Bootstrapping

**Counterexample bootstrapping** is the second of two compile-time optimizations enabled by [[LMAssertions|LM Assertions]] ([[2312.13382-dspy-assertions|Singhvi, Shetty, Tan et al. 2024]]). It collects the traces where the teacher LM **failed** an assertion before fixing it, and uses those failure-then-fix pairs as few-shot demonstrations.

## Mechanism

While running [[AssertionDrivenBacktracking|assertion-driven backtracking]] on the teacher during demonstration bootstrapping, the framework retains:

1. The **failing output** that violated the assertion.
2. The **error message** the assertion raised.
3. The **corrected output** produced on retry.

These triples are mixed into the bootstrapped few-shot demonstrations alongside the regular passing traces.

> "The optimizer in DSPy is able to incorporate feedback from the erroneous examples during backtracking as demonstrations. The usage of counterexample is twofold. First, counterexamples serve as negative demonstrations in the few-shot learning prompt, guiding models to avoid making similar mistakes. Second, with assertion-driven backtracking, counterexample traces often come with the demonstrations of fixing particular LM Assertion failures."

## Why it works without inference-time retry

The student model trained on counterexample-augmented demonstrations sees:

- *What violation looks like* (the failing output).
- *Why it failed* (the error message).
- *How to fix it* (the corrected output).

This teaches the student to **avoid the failure mode on first try** rather than relying on inference-time backtracking. The paper notes:

> "These demonstrations are helpful for the student model to achieve a much higher rate of passing the underlying constraints even without LM Assertions and assertion-drive backtracking."

## Operating regime

Counterexample bootstrapping is active in both `Compile w/ Assert` (compile-time only — no inference-time backtracking) and `C+Infer w/ Assert` (compile-time + inference-time). The former is the **cost-saving** mode: backtracking overhead is paid once at compile time, the student model runs with no per-call retry overhead, yet still respects assertions more often than a naive student.

## Position vs related ideas

- **vs negative-example prompting.** Counterexample bootstrapping is automated negative-example mining — the framework discovers which negative examples are *relevant* by collecting actual constraint violations during teacher rollout, rather than relying on a hand-picked list.
- **vs RLHF / DPO with rejected outputs.** Both teach a model what *not* to produce, but counterexample bootstrapping operates at the demonstration-prompt level (no weight update); the signal lives in the few-shot prompt the optimizer assembles.
- **vs [[2507.19457-gepa|GEPA]]'s [[FeedbackFunction|feedback function $\mu_f$]].** GEPA extends *scalar* reward with natural-language evaluation-trace text; counterexample bootstrapping is the demonstration-prompt-level analogue — capture textual failure + correction and use it as a demonstration. Both are mechanisms for delivering *richer-than-scalar* supervision to a prompt-optimization process.

## Related

- [[AssertionDrivenExampleBootstrapping]] — sibling compile-time optimization (positive demonstrations).
- [[AssertionDrivenBacktracking]] — the runtime mechanism whose traces this optimization captures.
- [[BootstrapFewShotWithRandomSearch]] — host optimizer.
- [[LMAssertions]] — the construct family.

## Tracked sources

- **[[2312.13382-dspy-assertions]]** (2024) — the introducing paper.
