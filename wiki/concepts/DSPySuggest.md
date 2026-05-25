---
title: "dspy.Suggest"
type: concept
tags: [concept, dspy, assertions, soft-constraint, deprecated]
sources: [2312.13382-dspy-assertions, dspy-output-refinement-tutorial]
last_updated: 2026-05-24
---

# `dspy.Suggest`

> **Deprecated as of [[DSPy]] 2.6** — replaced by [[DSPyBestOfN|`dspy.BestOfN`]] / [[DSPyRefine|`dspy.Refine`]] per [[dspy-output-refinement-tutorial]]. The boolean-constraint API (`constraint: bool`, `msg: str`) becomes the scalar-reward API (`reward_fn: Callable -> float`, `threshold: float`); `Suggest`'s warn-and-continue semantics map to `dspy.BestOfN(...)` (no `fail_count` → returns best-effort prediction without raising); the retry-with-feedback mechanism — and the *conflicting-suggestions* failure mode this page diagnoses — survive in [[DSPyRefine|`Refine`]] but with framework-synthesized feedback in place of user-authored `msg` strings. This page documents the original API for historical reference.

The **soft** variant of [[LMAssertions|LM Assertions]] in [[DSPy]], introduced in [[2312.13382-dspy-assertions|Singhvi, Shetty, Tan et al. (2024)]]. Expresses a heuristic guideline on a DSPy module's output: after a maximum number of retries $R$, persistent failure is logged as a `SuggestionError` warning and pipeline execution **continues to the next module**.

## Signature

```python
dspy.Suggest(constraint: bool, msg: Optional[str], backtrack: Optional[module])
```

## Behavior

- `constraint == True` → next state, continue.
- `constraint == False` and $r < R$ → retry state $\sigma_{r+1}$; failing module re-invoked with prior output + `msg` injected.
- `constraint == False` and $r \geq R$ → transitions to $\sigma''_0$: log `SuggestionError(msg)`, reset retry count, continue execution.

## Use cases

Soft constraints — desirable but non-essential properties:

- "Query should be less than 100 characters" (efficiency hint, not invariant).
- "Tweet should be engaging" (LM-judged subjective property).
- "Distractors should be plausible" (LM-judged quality bar).
- "Each query should be distinct from previous queries" (diversity hint).

If a hard halt is required on persistent failure, use [[DSPyAssert|`dspy.Assert`]] instead.

## Sequential-suggestion failure mode

The paper identifies a subtle pitfall: when multiple suggestions are defined sequentially on the same output, satisfying one can break another. The paper names this **"conflicting suggestions"**:

> "where sequentially defined suggestions can override each other's impact if they are hard to disentangle during self-refinement."

In TweetGen with all five suggestions enabled (`No "#"`, `Has Answer`, `Concise`, `Engaging`, `Faithful`), the *Engaging* rate actually drops below the inference-only baseline — designing the suggestion set is itself a skill.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-output-refinement-tutorial]] — the canonical deprecation receipt: the migration table maps `dspy.Suggest(constraint, msg)`'s warn-and-continue semantics to `dspy.BestOfN(..., reward_fn=..., threshold=1.0)` (no `fail_count` → returns best-effort prediction without raising), while the retry-with-feedback half — and the *conflicting-suggestions* failure mode this page diagnoses — survive in [[DSPyRefine|`dspy.Refine`]] with framework-synthesized feedback in place of user-authored `msg` strings.

## Related

- [[DSPyAssert]] — hard variant.
- [[LMAssertions]] — umbrella concept.
- [[AssertionDrivenBacktracking]] — the retry mechanism.

## Tracked sources

- **[[2312.13382-dspy-assertions]]** (2024) — the introducing paper.
