---
title: "BootstrapFewShot"
type: concept
tags: [dspy, optimizer, bootstrap, few-shot, demonstrations, teleprompter]
sources: [dspy-optimizers, dspy-optimization-overview]
last_updated: 2026-05-17
---

# BootstrapFewShot

**`dspy.BootstrapFewShot`** is the **canonical few-shot demonstration-tuning optimizer** in [[DSPy]]'s [[DSPyOptimizers|optimizer catalog]] and the recommended starting point for any optimization run with around **10 training examples**. It belongs to the *Automatic Few-Shot Learning* family of [[DSPyOptimizers]] and tunes **only demonstrations** (the few-shot examples in each [[DSPyPredict|`dspy.Predict`]]'s prompt), leaving the natural-language instructions and the LM's weights untouched.

The canonical source is [[dspy-optimizers|page 13 of the DSPy *Learn* corpus]].

## Mechanism

[[dspy-optimizers|The page]]'s definition:

> *"Uses a `teacher` module (which defaults to your program) to generate complete demonstrations for every stage of your program, along with labeled examples in `trainset`. ... The bootstrapping process employs the metric to validate demonstrations, including only those that pass the metric in the 'compiled' prompt."*

The three-step mechanism:

1. **Sample labeled demos.** Randomly select up to `max_labeled_demos` examples from `trainset` (these come with ground-truth labels — they don't need bootstrapping).

2. **Bootstrap additional demos.** Run the `teacher` module on training inputs (without labels); each run produces a **trace** — a list of `(predictor, inputs, outputs)` tuples — of how the program decomposed and executed. Score each trace via the [[DSPyMetrics|metric]] with `trace is not None` (the metric returns a **strict bool** in this mode per [[DSPyMetrics|the dual-purpose `trace` argument]]). Keep only traces that **pass** the metric.

3. **Install demos on each [[DSPyPredict|`dspy.Predict`]].** The metric-passing traces become the new `demos` attribute on each Predict in the program; subsequent calls inject these as few-shot examples in the prompt the [[DSPyAdapters|Adapter]] formats.

## Parameters

| Parameter | Type | Default | Role |
|---|---|---|---|
| `metric` | `(example, pred, trace=None) -> bool` | required | Validates bootstrapped demos in `trace is not None` mode; only metric-passing demos enter the compiled prompt. |
| `max_labeled_demos` | int | (default) | Number of `Example`s randomly selected from `trainset` to use as ground-truth labeled demos. |
| `max_bootstrapped_demos` | int | (default) | Number of *additional* demos the `teacher` generates by running the program and validating against `metric`. |
| `teacher` | `dspy.Module` (optional) | the program itself | Advanced: use a *different* DSPy program (with compatible structure) as the demo generator. Enables **stronger-teacher / weaker-student** setups for harder tasks — e.g. a [[ChainOfThought\|`dspy.ChainOfThought`]] teacher generating demos for a [[DSPyPredict\|`dspy.Predict`]] student. |

## The 10-example default

[[dspy-optimizers|The page]]'s five-rule getting-started rubric makes `BootstrapFewShot` the **default for very small data**:

> *"If you have **very few examples** (around 10), start with `BootstrapFewShot`."*

The rationale ties to the [[DSPyOptimization|workflow-level page's]] *30-example floor*: even *below* the substantial-value-at-30 floor, `BootstrapFewShot` can produce useful improvements because (a) the bootstrap step **augments** the available labeled data with model-generated traces, and (b) the metric filter keeps only the traces that already work, so the optimizer is **conservative** — it doesn't introduce demos that confuse the program.

## Relationship to siblings in the catalog

| Sibling | Difference from `BootstrapFewShot` |
|---|---|
| `LabeledFewShot` | Skips the bootstrap step entirely; uses only labeled `trainset` examples. **Simpler but doesn't augment data.** |
| [[BootstrapFewShotWithRandomSearch]] | Wraps `BootstrapFewShot` with random search over multiple bootstrap seeds; selects the best candidate program. **More expensive but more robust.** |
| `KNNFewShot` | Uses [[KNearestNeighbors\|k-NN]] over input embeddings to pick **per-input** demos (different inputs get different demos); the k-NN-selected examples become the `trainset` for `BootstrapFewShot` underneath. |
| [[MIPROv2]] | Also tunes demos (via the bootstrapping stage) **plus** instructions; the demo-tuning portion of MIPROv2 is structurally similar to `BootstrapFewShot` but adds Bayesian search. |
| [[BootstrapFinetune]] | Uses the same bootstrap-and-filter mechanism but **distills** the resulting demos into **weight updates** rather than installing them as in-prompt few-shot examples. |

The shared structural primitive across `BootstrapFewShot`, [[BootstrapFewShotWithRandomSearch]], `KNNFewShot`, [[MIPROv2]] (bootstrapping stage), and [[BootstrapFinetune]] is **metric-validated trace collection**. This is the single mechanism that [[DSPyMetrics|the metric's dual-purpose `trace` argument]] was designed to enable — the `trace is not None` branch's strict-bool return is what these optimizers use to decide which traces survive into the next phase.

## Position in the catalog's getting-started flow

```
~10 examples       → BootstrapFewShot               (this page)
50+ examples       → BootstrapFewShotWithRandomSearch
200+ examples      → MIPROv2
post-success       → BootstrapFinetune (distill to weights)
```

`BootstrapFewShot` is the **entry point**. The rubric assumes the developer starts here and moves up the data ladder only as more examples become available.

## Connections

- [[DSPy]] — the framework.
- [[DSPyOptimizers]] — the catalog this optimizer belongs to.
- [[DSPyOptimization]] — the workflow this optimizer operationalizes.
- [[dspy-optimizers]] — the canonical source page.
- [[DSPyMetrics]] — the dual-purpose `trace` argument's `trace is not None` branch is what this optimizer's demo-validation step uses.
- [[DSPyPredict]] — the per-Module learnable parameter site; this optimizer mutates each Predict's `demos` attribute.
- [[DSPyModules]] — the program input/output type.
- [[DSPyData]] / [[DSPyExample]] — the `trainset` primitive.
- [[BootstrapFewShotWithRandomSearch]] — the random-search-augmented sibling for larger data budgets.
- [[MIPROv2]] — the joint instruction+demonstration optimizer that includes a structurally similar bootstrapping stage.
- [[BootstrapFinetune]] — the weight-tuning sibling using the same bootstrap-and-filter mechanism.
- [[ChainOfThought]] — common teacher choice for the optional `teacher=...` kwarg.
