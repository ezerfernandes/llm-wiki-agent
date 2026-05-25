---
title: "dspy.BestOfN"
type: concept
tags: [concept, dspy, output-refinement, inference-time, reliability]
sources: [dspy-output-refinement-tutorial]
last_updated: 2026-05-24
---

# `dspy.BestOfN`

A [[DSPy]] module that wraps any other [[DSPyModules|Module]] in a **reward-driven retry loop**: executes the wrapped module up to **N times with different rollout IDs**, returning either the first prediction whose `reward_fn` score exceeds `threshold`, or the highest-scoring result if no rollout clears the bar. Introduced in DSPy 2.6 as one of the two replacements for [[DSPyAssert|`dspy.Assert`]] / [[DSPySuggest|`dspy.Suggest`]] (the other is [[DSPyRefine|`dspy.Refine`]]).

## Signature

```python
dspy.BestOfN(
    module: dspy.Module,
    N: int,
    reward_fn: Callable[[dict, dspy.Prediction], float],
    threshold: float,
    fail_count: Optional[int] = None,
)
```

## Behavior

- **Rollout-ID variation** is the cache-bypass mechanism — each of the N calls receives a distinct rollout ID, so [[DSPyCache|`dspy.Cache`]] does not collapse them to a single response.
- **Reward function** is two-argument: `reward_fn(args, pred) -> float` where `args` is the input kwargs and `pred` is the [[DSPyPrediction|`dspy.Prediction`]] from the wrapped module.
- **Selection rule** — return the first rollout whose reward exceeds `threshold` (early-exit), or the highest-scoring rollout if none clears the threshold across all N attempts.
- **`fail_count`** controls error tolerance — raises the underlying exception after that many failed rollouts (e.g. `fail_count=1` raises on the first failure). Distinguishes *low-reward-but-valid* outputs (selection task) from *exception-throwing* outputs (error-handling task).

## Use cases

- **Constraint enforcement via deterministic scoring** — one-word-answer, valid-JSON-output, length-window. The reward is a Python predicate cast to float.
- **Soft-target optimization** — the canonical length-controlled summarization example uses `1.0 - distance / 125` (tapering reward away from a 75-word ideal) with `N=50, threshold=0.9`. Scales to substantial parallel sampling when reward is continuous.
- **LM-judge-driven sampling** — `reward_fn` may itself invoke an LM (see [[DSPyRefine]] for the canonical `FactualityJudge` example, applicable equally to `BestOfN`).

## Relation to generic [[bestofn|Best-of-N]]

`dspy.BestOfN` is the [[DSPy]]-module instantiation of the generic [[bestofn|Best-of-N]] [[testtimescaling|test-time-scaling]] strategy (width = N, depth = fixed-to-completion, ANSWER = `reward_fn` argmax). Differences from the textbook formulation:

- **Programmable scoring function** rather than majority-vote or [[Logprobs|logprob]] aggregation — supports arbitrary Python including [[RewardModel|reward-model]]-style or LM-judge-style scorers.
- **Threshold-based early-exit** — short-circuits at the first rollout clearing `threshold`, so empirical N often < specified N. The textbook generic [[bestofn|BoN]] formulation samples all N then aggregates.
- **`fail_count` semantics** — bakes error tolerance into the selection loop. The textbook formulation typically aborts on any error.

## Migration from [[DSPyAssert|`dspy.Assert`]] / [[DSPySuggest|`dspy.Suggest`]]

DSPy 2.6 replaces the boolean-constraint API of [[2312.13382-dspy-assertions|LM Assertions]] with the scalar-reward API of `BestOfN` / `Refine`. The translation:

| Old API | New API |
|---|---|
| `dspy.Assert(constraint, msg)` halt-on-fail | `dspy.BestOfN(..., reward_fn=lambda a, p: 1.0 if constraint(p) else 0.0, threshold=1.0, fail_count=1)` |
| `dspy.Suggest(constraint, msg)` warn-on-fail | `dspy.BestOfN(..., reward_fn=..., threshold=1.0)` (no fail_count → return best-effort) |
| `dspy.Assert` with retry-and-feedback | [[DSPyRefine|`dspy.Refine`]] — the auto-feedback-loop sibling |

The retry-with-feedback semantics from [[AssertionDrivenBacktracking|assertion-driven backtracking]] survive in [[DSPyRefine|`Refine`]]; selection-without-feedback is `BestOfN`.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-output-refinement-tutorial]] — minting tutorial; three escalating receipts share the `dspy.BestOfN(module, N, reward_fn, threshold)` surface: (1) **one-word-answer constraint** with deterministic Python-predicate reward (`N=3, threshold=1.0`) — pure selection, no feedback; (2) **length-controlled summarization** with continuous soft-margin reward (`1.0 - distance/125` toward a 75-word ideal, `N=50, threshold=0.9`) — largest-`N` receipt in the corpus, demonstrates `BestOfN` scales to substantial parallel sampling when reward is continuous; (3) the migration table mapping deprecated `dspy.Assert(constraint, msg)` halt-on-fail to `BestOfN(..., reward_fn=..., threshold=1.0, fail_count=1)`.

## Related

- [[DSPyRefine]] — feedback-augmented sibling.
- [[bestofn|Best-of-N (generic)]] — the textbook test-time-scaling pattern.
- [[DSPyAssert]] / [[DSPySuggest]] — deprecated predecessors.
- [[LMAssertions]] — umbrella concept spanning both API generations.
- [[DSPyCache]] — rollout-ID variation is the canonical *intentional* cache miss.
- [[RewardFunction]] — RL-formalism cousin; `reward_fn` is the inference-time degenerate case.
- [[2312.13382-dspy-assertions]] — historical paper for the retry-with-feedback mechanism that `Refine` inherits.

## Tracked sources

- **[[dspy-output-refinement-tutorial]]** — minting tutorial.
