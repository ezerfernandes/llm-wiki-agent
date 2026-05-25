---
title: "dspy.Assert"
type: concept
tags: [concept, dspy, assertions, hard-constraint, deprecated]
sources: [2312.13382-dspy-assertions, dspy-output-refinement-tutorial]
last_updated: 2026-05-24
---

# `dspy.Assert`

> **Deprecated as of [[DSPy]] 2.6** — replaced by [[DSPyBestOfN|`dspy.BestOfN`]] / [[DSPyRefine|`dspy.Refine`]] per [[dspy-output-refinement-tutorial]]. The boolean-constraint API (`constraint: bool`, `msg: str`) becomes the scalar-reward API (`reward_fn: Callable -> float`, `threshold: float`); `Assert`'s halt-on-fail semantics map to `dspy.BestOfN(..., fail_count=1)`; the retry-with-feedback mechanism survives in [[DSPyRefine|`Refine`]]. This page documents the original API for historical reference and for the [[AssertionDrivenBacktracking|backtracking]] / [[AssertionDrivenExampleBootstrapping|example-bootstrapping]] / [[CounterexampleBootstrapping|counterexample-bootstrapping]] compile-time optimizations the [[2312.13382-dspy-assertions]] paper formalizes.

The **hard** variant of [[LMAssertions|LM Assertions]] in [[DSPy]], introduced in [[2312.13382-dspy-assertions|Singhvi, Shetty, Tan et al. (2024)]]. Expresses a non-negotiable constraint on a DSPy module's output: after a maximum number of retries $R$, persistent failure halts the pipeline with `AssertionError`.

## Signature

```python
dspy.Assert(constraint: bool, msg: Optional[str], backtrack: Optional[module])
```

## Behavior

- `constraint == True` → pipeline transitions to next state, execution continues.
- `constraint == False` and retry count $r < R$ → pipeline transitions to retry state $\sigma_{r+1}$; the failing module is re-invoked with its prior erring output + `msg` injected into the prompt.
- `constraint == False` and $r \geq R$ → pipeline transitions to error state $\sigma^\perp$; raises `AssertionError(msg)`.

## Use cases

Hard constraints — invariants the program *must* satisfy or the result is unusable:

- Output must be valid JSON.
- Output must include a required field.
- Output must respect a strict structural format.
- Output must pass a deterministic algorithmic check.

Soft constraints (engagement, conciseness, plausibility) should use [[DSPySuggest|`dspy.Suggest`]] instead.

## Delineation from Python `assert`

Conventional Python `assert` is binary halt-on-fail with no retry. `dspy.Assert` offers a retry-with-feedback loop:

> "On an `Assert` failing, the pipeline transitions to a special retry state, allowing it to reattempt a failing LM call while being aware of its previous attempts and the error message raised. If, after a maximum of self-refinement attempts, the assertion still fails, the pipeline transitions to an error state and raises an `AssertionError`."

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-output-refinement-tutorial]] — the canonical deprecation receipt: shows the DSPy 2.6 migration of `dspy.Assert(constraint, msg)`'s halt-on-fail semantics to `dspy.BestOfN(..., reward_fn=..., threshold=1.0, fail_count=1)`, with the retry-with-feedback half surviving in [[DSPyRefine|`dspy.Refine`]].
- [[dspy-customer-service-agent]] — gap-shaped receipt: names `dspy.Assert` as the natural extension surface for hard-constraint invariants on tool returns (e.g. `dspy.Assert(flight.date_time > now())` inside `book_flight`); the agent itself ships **without** assertion gates, which the source page flags as the production-readiness gap.
- [[dspy-yahoo-finance-react-tutorial]] — gap-shaped receipt: explicitly cites the absence of `dspy.Assert` / [[DSPyGuardrails]] as a production-readiness gap for a financial-advice agent (no hard buy/sell recommendation guards, no price-prediction blockers).

## Related

- [[DSPySuggest]] — soft variant.
- [[LMAssertions]] — umbrella concept.
- [[AssertionDrivenBacktracking]] — the retry mechanism.

## Tracked sources

- **[[2312.13382-dspy-assertions]]** (2024) — the introducing paper.
