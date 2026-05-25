---
title: "DSPy Tutorial — Output Refinement (BestOfN and Refine)"
type: source
tags: [dspy, tutorial, output-refinement, inference-time, reliability]
date: 2026-05-24
source_file: raw/dspy-output-refinement-tutorial.md
---

## Summary

Short single-page [[DSPy]] tutorial at `https://dspy.ai/tutorials/output_refinement/best-of-n-and-refine/` that **canonicalizes the framework's inference-time output-refinement surface** — two sibling modules ([[DSPyBestOfN|`dspy.BestOfN`]] and [[DSPyRefine|`dspy.Refine`]]) that wrap any [[DSPyModules|Module]] with a **reward-driven retry loop**. **Migration receipt**: *"As of DSPy 2.6, these modules replace `dspy.Suggest` and `dspy.Assert`"* — the first wiki-corpus statement that [[DSPyAssert|`dspy.Assert`]] / [[DSPySuggest|`dspy.Suggest`]] from [[2312.13382-dspy-assertions]] are deprecated in favor of a reward-function-based API. Both modules take the same four-kwarg surface: `module`, `N`, `reward_fn(args, pred) -> float`, `threshold`, plus optional `fail_count` for error tolerance.

## Key Claims

- **`dspy.BestOfN(module, N, reward_fn, threshold)`** — executes `module` up to **N times with different rollout IDs** (rollout ID variation bypasses [[DSPyCache|cache]] so each call is genuinely different), returns the first prediction whose `reward_fn` score exceeds `threshold` OR the highest-scoring result if no run clears the bar. Pure selection — no feedback loop.
- **`dspy.Refine(module, N, reward_fn, threshold)`** — same surface as `BestOfN` but adds an **automatic feedback loop**: unsuccessful attempts generate detailed performance feedback that is injected as hints for subsequent runs. The LM analyzes its own failures and self-corrects across the N rollouts.
- **`reward_fn(args, pred) -> float`** signature is **two-argument**: `args` (the input kwargs passed to the wrapped module) and `pred` (the [[DSPyPrediction|`dspy.Prediction`]] from the module). Returns a scalar — `threshold` is the cutoff for "good enough."
- **`fail_count` parameter** — controls **error tolerance**: raises the underlying exception after that many failed rollouts (e.g. `fail_count=1` raises on the first failure). Lets users distinguish *low-reward-but-valid* outputs (selection task) from *exception-throwing* outputs (error-handling task).
- **Reward functions can themselves be LM calls** — the `factuality_reward` example wires a [[ChainOfThought|`dspy.ChainOfThought`]] `FactualityJudge` (with `is_factual: bool` OutputField) *inside* the reward function, so refinement is judge-driven. The tutorial's first wiki receipt of **LM-as-judge composed with output refinement** as a single inference-time pipeline.
- **Migration story**: DSPy 2.6 replaces [[DSPyAssert]] / [[DSPySuggest]] with `BestOfN` / `Refine`. The retry-with-feedback semantics from the [[2312.13382-dspy-assertions|LM Assertions paper]] survive — what changes is the **constraint API**: from `(constraint: bool, msg: Optional[str])` to `(reward_fn: Callable -> float, threshold: float)`. Boolean-constraint becomes scalar-reward with a threshold; the binary halt-vs-warn distinction (`Assert` vs `Suggest`) becomes the binary selection-vs-feedback distinction (`BestOfN` vs `Refine`).

## Key Quotes

> "Both `BestOfN` and `Refine` are DSPy modules that improve the reliability and quality of predictions by making multiple LM calls with different rollout IDs to bypass caching."

> "Refine extends BestOfN by adding an automatic feedback loop where unsuccessful attempts generate detailed performance feedback used as hints for subsequent runs."

> "As of DSPy 2.6, these modules replace `dspy.Suggest` and `dspy.Assert`."

## Worked Examples

1. **One-word-answer constraint** — `reward_fn = 1.0 if len(pred.answer.split()) == 1 else 0.0`, `threshold=1.0`, `N=3` over `dspy.ChainOfThought("question -> answer")`. Canonical deterministic-reward example; shared verbatim between `BestOfN` and `Refine` to highlight the API symmetry.
2. **Factuality validation** — `FactualityJudge` Signature with `is_factual: bool` OutputField under `dspy.ChainOfThought` produces the reward; `Refine(N=3, threshold=1.0)` over `dspy.ChainOfThought("question -> answer")`. **LM-judge-driven refinement** is the canonical use case.
3. **Length-controlled summarization** — soft-margin reward (`1.0 - distance/125` where `distance = abs(word_count - 75)`) with `BestOfN(N=50, threshold=0.9)`. Largest `N` in the tutorial — demonstrates that `BestOfN` scales to substantial parallel sampling for tasks where reward is continuous and the optimum is a soft target (75-word ideal length with tapering).

## Connections

- [[DSPyBestOfN]] — new concept page (this tutorial mints it).
- [[DSPyRefine]] — new concept page (this tutorial mints it).
- [[DSPyAssert]] / [[DSPySuggest]] — the deprecated predecessors. Migration note added to both concept pages.
- [[2312.13382-dspy-assertions|Singhvi, Shetty, Tan et al. (2024)]] — the LM Assertions paper introducing `Assert` / `Suggest`. Underwrites the historical lineage; the retry-with-feedback semantics from [[AssertionDrivenBacktracking|backtracking]] survive in `Refine`.
- [[LMAssertions]] — umbrella concept that subsumes both the deprecated `Assert` / `Suggest` API and the new `BestOfN` / `Refine` API.
- [[bestofn|Best-of-N]] — the generic [[testtimescaling|test-time scaling]] pattern. `dspy.BestOfN` is the DSPy-module instantiation of this strategy, but distinct in that it ships with a programmable `reward_fn` and a `threshold`-based early-exit (vs majority-vote or fixed-budget BoN).
- [[testtimescaling]] / [[InferenceTimeSearch]] — parent strategies. `BestOfN` / `Refine` are framework-level inference-time-scaling surfaces orthogonal to the [[DSPyProgrammingModel|four-concerns decomposition]] (Signature / Adapter / Module / Optimizer).
- [[RewardFunction]] — the RL-formalism `r(s,a) → ℝ`. `BestOfN` / `Refine` use a degenerate reward shape: $r(\text{pred}) \in [0, 1]$ (no state-action dependence), with the LM-rollout standing in for the policy.
- [[chainofthought|`dspy.ChainOfThought`]] — the wrapped Module in every example.
- [[DSPyPrediction]] — the type the `reward_fn`'s `pred` argument is bound to.
- [[DSPyCache]] — rollout-ID variation is the cache-bypass mechanism (in [[dspy-cache-tutorial|the Caching tutorial's]] vocabulary, this is the canonical *intentional* cache miss).
- [[DSPyModules]] — both new modules are themselves Modules; they compose with every other Module.

## Contradictions

- **Migration / deprecation**: this tutorial states `BestOfN` / `Refine` *replace* [[DSPyAssert|`dspy.Assert`]] / [[DSPySuggest|`dspy.Suggest`]] as of DSPy 2.6. The existing [[DSPyAssert]] / [[DSPySuggest]] concept pages (sourced from [[2312.13382-dspy-assertions]]) document them as the active API. **Resolution**: both pages updated in place with a "Deprecation" section noting the DSPy 2.6 replacement, with the underlying retry-with-feedback semantics preserved. The [[2312.13382-dspy-assertions]] paper remains historically authoritative for the *mechanism* (the [[AssertionDrivenBacktracking|backtracking]] machinery, the [[AssertionDrivenExampleBootstrapping|example-bootstrapping]] optimization); only the user-facing API shape changed.
- **`reward_fn` arity mismatch with [[DSPyMetrics|`dspy.Metric`]]**: DSPy metrics elsewhere in the corpus take `(example, prediction, trace=None)` — a three-arg signature with the gold example. The output-refinement `reward_fn(args, pred)` takes the *input* args (not a gold example) because there is no ground truth at refinement time — the reward is intrinsic / judge-based. **Not a contradiction**; the two are different surfaces serving different stages (metrics for evaluation/optimization, reward functions for inference-time selection).

## Scope-Limit Gaps

1. **No quantitative results** — zero benchmark numbers, zero before/after lift. The tutorial is API documentation; reliability claims are qualitative ("improve").
2. **No explanation of the rollout-ID mechanism** — *what* a rollout ID is, how it propagates through [[DSPyLM|`dspy.LM`]] to the [[LiteLLM]] provider call, and how it bypasses [[DSPyCache|caching]] at the [[DSPyCache|three-layer caching architecture]] level is not specified.
3. **No `Refine` feedback-prompt example** — the *form* of the auto-generated feedback ("detailed performance feedback used as hints") is not shown, only described. The corpus has no receipt of what the LM actually sees as the hint in iteration 2.
4. **No interaction with `dspy.streamify`** — does the [[DSPyStreaming|streaming]] surface emit per-rollout chunks or only the final selected prediction? Not specified.
5. **No interaction with [[DSPyOptimizers|Optimizers]]** — can `BestOfN` / `Refine` be the **inner** module compiled by [[MIPROv2]] / [[GEPA]]? Not specified.
6. **No cost / latency disclosure** — `N=50` summarization × LM call cost is not measured; whether providers offer batching is not discussed.
7. **No `BestOfN` selection-mode disclosure** — does it return the **first** prediction exceeding `threshold` (early-exit) or the **highest-scoring** in $[1, N]$ rollouts? The tutorial prose says "either the first prediction exceeding a threshold or the highest-scoring result" — the trigger that picks between the two modes (full-N exhaustion vs threshold-clearance) is not explicit.
8. **No assertion-paper-style stacking** — the [[2312.13382-dspy-assertions]] paper's headline contribution was [[AssertionDrivenExampleBootstrapping|compile-time example bootstrapping]] from constraint violations and [[CounterexampleBootstrapping|counterexample bootstrapping]] from corrected outputs. Whether `Refine` exposes either compile-time optimization is not addressed.
9. **No `Refine` formal pseudocode** — the *order* of (reward eval → feedback generation → next rollout) is implied but not specified; whether the feedback-generating LM is the *same* as the wrapped Module's LM (and counts toward `N`) is not stated.
10. **No fail-mode taxonomy** — `fail_count` is documented but the distinction between *reward-score-below-threshold* (an honest low-quality output) and *underlying-exception* (a tool error / parse error / API error) is implicit; whether a single failing rollout consumes one of the `N` budget slots is not stated.
