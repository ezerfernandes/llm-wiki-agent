---
title: "dspy.Refine"
type: concept
tags: [concept, dspy, output-refinement, inference-time, reliability, self-refinement]
sources: [dspy-output-refinement-tutorial]
last_updated: 2026-05-24
---

# `dspy.Refine`

A [[DSPy]] module that extends [[DSPyBestOfN|`dspy.BestOfN`]] with an **automatic feedback loop**: unsuccessful attempts generate detailed performance feedback that is injected as hints for subsequent rollouts. Introduced in DSPy 2.6 as one of the two replacements for [[DSPyAssert|`dspy.Assert`]] / [[DSPySuggest|`dspy.Suggest`]] (the other is [[DSPyBestOfN|`dspy.BestOfN`]]).

## Signature

```python
dspy.Refine(
    module: dspy.Module,
    N: int,
    reward_fn: Callable[[dict, dspy.Prediction], float],
    threshold: float,
    fail_count: Optional[int] = None,
)
```

API surface identical to [[DSPyBestOfN|`dspy.BestOfN`]] — same four required kwargs plus optional `fail_count`. The behavior differs in the **between-rollout** step.

## Behavior

- Same rollout-ID-variation cache-bypass mechanism as [[DSPyBestOfN|`BestOfN`]].
- **Auto-feedback step** — between rollouts, the framework generates detailed performance feedback (an LM analyzes the previous rollout's `reward_fn` score and the prediction itself) and **injects it as a hint** for the next rollout's prompt. The wrapped Module sees a progressively informed prompt rather than independent re-rolls.
- Same selection rule as `BestOfN`: return the first prediction clearing `threshold`, or the highest-scoring overall.
- Same `fail_count` error-tolerance semantics.

## Use cases

- **Self-correcting factuality** — the canonical tutorial example wires a [[ChainOfThought|`dspy.ChainOfThought`]] `FactualityJudge` (with `is_factual: bool` OutputField) as the reward function; `Refine` self-corrects across N rollouts using the judge's verdict as the feedback signal.
- **Iterative format-fixing** — when the reward function captures a structural constraint, `Refine`'s feedback loop teaches the LM why the prior attempt failed (e.g. *"output was 3 words, must be 1 word"*) so subsequent rollouts are guided, not blind.
- **LM-judge composition** — `reward_fn` may itself invoke an LM (see the factuality example). Combined with `Refine`'s feedback loop, this yields a **two-LM iterative pipeline**: judge-scores-then-feedback-guides-author.

## Relation to [[DSPyBestOfN]]

| Property | [[DSPyBestOfN|`BestOfN`]] | `Refine` |
|---|---|---|
| Between-rollout state | independent re-rolls | feedback-injected re-rolls |
| Cost per rollout | 1 LM call | 1 LM call + 1 feedback-generation call |
| Sampling distribution | unchanged across rollouts | shifts toward higher-reward region |
| When to prefer | reward is cheap and well-formed candidates are common | reward is high-stakes / candidates are rare / feedback is informative |

`Refine` ⊇ `BestOfN` in capability — every `BestOfN` reward function works with `Refine`. The trade-off is the extra LM call per failed rollout for feedback generation.

## Lineage from [[2312.13382-dspy-assertions|LM Assertions]]

The retry-with-feedback semantics from [[AssertionDrivenBacktracking|assertion-driven backtracking]] survive in `Refine` — the mechanism the original paper called *"re-invoking the failing module with its prior erring output + `msg` injected as `Past Query` / `Instruction` prompt fields"* is now generalized to feedback generated from a scalar `reward_fn` rather than a binary `constraint`. The DSPy 2.6 migration replaces the (`constraint: bool`, `msg: Optional[str]`) surface with (`reward_fn: Callable -> float`, `threshold: float`) — the feedback `msg` is no longer user-authored but framework-synthesized from the reward signal.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-output-refinement-tutorial]] — minting tutorial; the canonical receipt is the **factuality-validation** worked example wrapping `dspy.ChainOfThought("question -> answer")` with `dspy.Refine(N=3, threshold=1.0)` over a `FactualityJudge` (Signature with `is_factual: bool` OutputField under `dspy.ChainOfThought`) as the `reward_fn` — first wiki receipt of **LM-judge-driven inference-time refinement** as a single pipeline, with the framework-synthesized feedback closing the loop the deprecated `dspy.Assert(constraint, msg)` opened.

## Related

- [[DSPyBestOfN]] — sibling without the feedback loop.
- [[DSPyAssert]] / [[DSPySuggest]] — deprecated predecessors; `Refine` inherits their retry-with-feedback semantics.
- [[LMAssertions]] — umbrella concept spanning both API generations.
- [[AssertionDrivenBacktracking]] — the underlying retry mechanism formalized by [[2312.13382-dspy-assertions]].
- [[chainofthought|`dspy.ChainOfThought`]] — the wrapped Module in every tutorial example.
- [[DSPyCache]] — rollout-ID variation is the canonical *intentional* cache miss.
- [[RewardFunction]] — RL-formalism cousin; `reward_fn` is the inference-time degenerate case.
- [[InferenceTimeSearch]] — framework-level parent strategy.

## Tracked sources

- **[[dspy-output-refinement-tutorial]]** — minting tutorial.
