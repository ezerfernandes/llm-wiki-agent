---
title: "BootstrapFewShotWithRandomSearch"
type: concept
tags: [dspy, optimizer, bootstrap, few-shot, demonstrations, random-search, teleprompter]
sources: [dspy-optimizers, dspy-optimization-overview]
last_updated: 2026-05-17
---

# BootstrapFewShotWithRandomSearch

**`dspy.BootstrapFewShotWithRandomSearch`** is the **random-search-augmented version** of [[BootstrapFewShot]] in [[DSPy]]'s [[DSPyOptimizers|optimizer catalog]], recommended for runs with **50+ training examples**. It tunes demonstrations only (same as [[BootstrapFewShot]]) but **explores multiple bootstrap seeds** and selects the best candidate program. It is the optimizer the [[dspy-optimizers|page]] uses as its **canonical worked-example** for the general optimizer API.

The canonical source is [[dspy-optimizers|page 13 of the DSPy *Learn* corpus]].

## Mechanism

[[dspy-optimizers|The page]]'s definition:

> *"Applies `BootstrapFewShot` several times with random search over generated demonstrations, and selects the best program over the optimization."*

The candidate set evaluated:

1. The **uncompiled** original program.
2. The `LabeledFewShot`-optimized program.
3. The [[BootstrapFewShot]] compiled program **with unshuffled examples**.
4. `num_candidate_programs` additional [[BootstrapFewShot]]-compiled programs with **randomized example sets**.

The optimizer evaluates each candidate against the [[DSPyMetrics|metric]] on the training set, and returns the highest-scoring program. The randomization defense against [[BootstrapFewShot]]'s single-seed brittleness — different demo orderings can produce meaningfully different program behaviors, and random search lets the optimizer pick the seed that works best.

## Parameters

Inherits [[BootstrapFewShot]]'s parameters (`metric`, `max_labeled_demos`, `max_bootstrapped_demos`, `teacher`), and adds:

| Parameter | Type | Default | Role |
|---|---|---|---|
| `num_candidate_programs` | int | (default) | Number of [[BootstrapFewShot]]-compiled programs with **randomized example sets** to evaluate in the search. The total candidate count is `num_candidate_programs + 3` (uncompiled + LabeledFewShot + unshuffled-BootstrapFewShot + N randomized). |
| `num_threads` | int | (default) | Parallelism for evaluation (mirrors the [[DSPyEvaluate|`dspy.Evaluate`]] thread-parallel harness). |

## The canonical worked example

[[dspy-optimizers|The page]] uses `BootstrapFewShotWithRandomSearch` to demonstrate the **general optimizer API** — the same two-step lifecycle every [[DSPyOptimizers|optimizer]] in the catalog implements:

```python
import dspy

# Set up the optimizer: we want to "bootstrap" (i.e., self-generate) 8-shot examples of your program's steps.
# The optimizer will repeat this 10 times (plus some initial attempts) before selecting its best attempt on the devset.
config = dict(max_bootstrapped_demos=4, max_labeled_demos=4, num_candidate_programs=10, num_threads=4)

teleprompter = dspy.BootstrapFewShotWithRandomSearch(metric=YOUR_METRIC_HERE, **config)
optimized_program = teleprompter.compile(YOUR_PROGRAM_HERE, trainset=YOUR_TRAINSET_HERE)
```

Note the variable name `teleprompter` — a legacy holdover from the pre-rename era. The framework has officially renamed *teleprompters* → *optimizers*, but the canonical worked-example local-variable name is still `teleprompter`.

## The 50+-example default

[[dspy-optimizers|The page]]'s five-rule rubric:

> *"If you have **more data** (50 examples or more), try `BootstrapFewShotWithRandomSearch`."*

The 50-example threshold aligns with the [[DSPyOptimization|workflow page's]] 30/300 training-set regime — at 50 examples the developer is past the *"substantial value out of 30"* floor and into the regime where searching multiple bootstrap seeds is affordable.

## Connections

- [[DSPy]] — the framework.
- [[DSPyOptimizers]] — the catalog this optimizer belongs to.
- [[DSPyOptimization]] — the workflow this optimizer operationalizes.
- [[dspy-optimizers]] — the canonical source page; uses this optimizer as the canonical API worked-example.
- [[BootstrapFewShot]] — the underlying single-seed optimizer this one wraps with random search.
- [[DSPyMetrics]] — the dual-purpose `trace` argument's `trace is not None` branch is what the underlying [[BootstrapFewShot]]'s demo-validation step uses.
- [[DSPyEvaluate]] — the thread-parallel evaluation harness the `num_threads` kwarg parallels.
- [[MIPROv2]] — the next step up the data ladder (200+ examples; Bayesian search instead of random search).
- [[BootstrapFinetune]] — the weight-tuning sibling.
