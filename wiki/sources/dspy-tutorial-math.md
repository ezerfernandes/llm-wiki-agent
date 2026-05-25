---
title: "DSPy Tutorial — Math Reasoning"
type: source
tags: [dspy, tutorial, math, mipro, chain-of-thought, optimization]
date: 2026-05-24
source_file: raw/dspy-tutorial-math.md
---

## Summary

Official [[DSPy]] tutorial demonstrating end-to-end prompt optimization of a single-signature [[chainofthought|`dspy.ChainOfThought("question -> answer")`]] module on the **algebra subset of the [[MATH-benchmark|MATH benchmark]]** (Hendrycks et al. 2021). Lifts a [[GPT|GPT-4o-mini]] student program from **74.0% → 88.57%** (+14.6 pts absolute, ~20% relative) on the 350-example dev set via [[MIPROv2|`dspy.MIPROv2(auto="medium")`]] with [[GPT|GPT-4o]] as the bootstrap teacher and GPT-4o-mini as the instruction proposer. **First wiki-corpus DSPy tutorial benchmarked on a math-reasoning dataset** — fills the *symbolic / numerical reasoning* application slot in the DSPy tutorial corpus alongside RAG, ReAct agents, entity extraction, and conversation history.

## Key Claims

- **Single-signature `dspy.ChainOfThought("question -> answer")` suffices as the program** — no custom signature class, no multi-module composition, no retrieval. The full program is one line of DSPy.
- **MATH algebra subset has built-in DSPy support**: `from dspy.datasets import MATH` + `MATH(subset='algebra')` exposes `train` / `dev` (350 each) + a built-in `dataset.metric` for grading answers.
- **Teacher/student decoupling is single-line config**: `teacher_settings=dict(lm=gpt4o)` + `prompt_model=gpt4o_mini`. The student (the deployed module) runs on GPT-4o-mini; the optimizer uses GPT-4o only during bootstrap-trace generation.
- **`auto="medium"` is the workhorse preset** for medium-budget runs; the tutorial doesn't characterize cost or wall-time numerically.
- **Demo budget here is 4+4** (`max_bootstrapped_demos=4, max_labeled_demos=4`), double the typical `2+2` seen on the other tutorials. The MATH dataset includes worked-solution `answer` labels, so labeled demos are not zero.
- **`dspy.Evaluate` with 24 threads** runs in parallel over the 350-example dev set — the same harness used in every other DSPy tutorial.
- **`dspy.inspect_history()` is the post-optimization inspection surface** — exposes the optimized instruction + the bootstrapped few-shot demos in plain text.

## Key Quotes

> "MIPROv2 lifts the program from 74.0 → 88.57."

> "The optimized prompt incorporates mathematical reasoning patterns from successful bootstrapped examples, providing structured guidance for systematic algebra problem solving."

## Code Receipt

```python
import dspy

gpt4o_mini = dspy.LM('openai/gpt-4o-mini', max_tokens=2000)
gpt4o = dspy.LM('openai/gpt-4o', max_tokens=2000)
dspy.configure(lm=gpt4o_mini)

from dspy.datasets import MATH
dataset = MATH(subset='algebra')        # 350 train, 350 dev

module = dspy.ChainOfThought("question -> answer")

THREADS = 24
evaluate = dspy.Evaluate(devset=dataset.dev, metric=dataset.metric,
                         num_threads=THREADS, display_progress=True, display_table=5)

evaluate(module)                        # → 74.0

optimizer = dspy.MIPROv2(metric=dataset.metric, auto="medium",
                         num_threads=THREADS,
                         teacher_settings=dict(lm=gpt4o),
                         prompt_model=gpt4o_mini)

optimized_module = optimizer.compile(module, trainset=dataset.train,
                                     max_bootstrapped_demos=4,
                                     max_labeled_demos=4)

evaluate(optimized_module)              # → 88.57
```

## Position in the DSPy Tutorial Corpus

This is the **sixth wiki-corpus DSPy tutorial** and the **first benchmarked on a math-reasoning dataset**. Coverage map:

| Tutorial | Task shape | Dataset | Optimizer setup | Lift |
|---|---|---|---|---|
| [[dspy-conversation-history]] | Multi-turn chatbot | — | — (no opt) | — |
| [[dspy-customer-service-agent]] | 7-tool [[react\|ReAct]] agent | Custom Pydantic domain | — | — |
| [[dspy-custom-module]] | 3-stage [[rag\|RAG]] template | Wikipedia ([[ColBERTv2]]) | — | — |
| [[dspy-tutorial-rag-as-agent]] | Multi-hop ReAct agent | [[HoVer]] (3-hop) | MIPROv2 `medium` + teacher/student split | 8% → 41.67% |
| [[dspy-entity-extraction-tutorial]] | Decoder-LM NER | [[CoNLL2003]] (200-ex) | MIPROv2 `medium`, `4 demos`, `minibatch=False` | 86% → 93% |
| [[dspy-rag-tutorial]] | Single-hop RAG | [[RAGQAArenaTech]] | MIPROv2 `medium`, `2+2 demos` | 42% → 55.5% → 61.1% |
| **dspy-tutorial-math** *(this page)* | **Single-step [[chainofthought\|CoT]]** | **MATH algebra (350+350)** | **MIPROv2 `medium`, `4+4 demos`, GPT-4o teacher** | **74.0% → 88.57%** |

## MIPROv2 Cross-Receipt Convergence

[[MIPROv2|MIPROv2]] `auto="medium"` now has **five wiki receipts**:

| Receipt | Dataset | Baseline | Post-opt | Lift |
|---|---|---|---|---|
| [[dspy-optimizers]] (Receipt 2) | StackExchange RAG | 53% | 61% | +8 |
| [[dspy-rag-tutorial]] | [[RAGQAArenaTech]] | 55.5% | 61.1% | +5.6 |
| [[dspy-tutorial-rag-as-agent]] | [[HoVer]] (3-hop) | 8% | 41.67% | +33.67 |
| [[dspy-entity-extraction-tutorial]] | [[CoNLL2003]] | 86% | 93% | +7 |
| **This tutorial** | **MATH algebra** | **74.0%** | **88.57%** | **+14.57** |

The MATH lift (~20% relative) sits between the RAG ceiling (~10%) and the ReAct-agent lift (~5×) — consistent with the hypothesis that `auto="medium"` lift is **proportional to the headroom of the baseline**: tasks where the un-optimized CoT already does well (RAG, NER) see smaller absolute gains than tasks where the baseline barely works (HoVer at 8%). MATH's 74% baseline sits in the middle of this range and the 14.6-point lift accordingly.

## Connections

- [[DSPy]] — the framework being demonstrated.
- [[chainofthought|`dspy.ChainOfThought`]] — the only module used; **first wiki receipt where CoT is the entire program** (no retrieval, no tools, no history).
- [[MIPROv2|`dspy.MIPROv2`]] — the optimizer; the tutorial uses the **teacher/student split** + `auto="medium"` + `max_bootstrapped_demos=4, max_labeled_demos=4`.
- [[MATH-benchmark|MATH benchmark]] — Hendrycks et al. 2021 competition-math dataset; the tutorial uses the **algebra subset** (350 train, 350 dev). **First wiki receipt of `dspy.datasets.MATH` as the in-framework dataset loader.**
- [[DSPyEvaluate|`dspy.Evaluate`]] — the dev-set scoring harness; 24-thread parallel evaluation.
- [[DSPyHistory|`dspy.inspect_history`]] — the post-optimization prompt-inspection surface.
- [[GPT|GPT-4o-mini]] — student LM; runs the deployed module + the instruction-proposer role.
- [[GPT|GPT-4o]] — teacher LM; runs only during bootstrap-trace generation.
- [[openai|OpenAI]] — the LM provider for both models.
- [[MLflow]] — the tutorial recommends MLflow tracing for visualization and explainability (the same opt-in recipe as the other DSPy tutorials).
- [[2406.11695-mipro|MIPRO paper]] — the algorithmic anchor for the optimizer used here.
- [[GSM8K]] — math-reasoning benchmark sibling to MATH; not used in this tutorial but contextually adjacent.
- [[BootstrapFewShot]] / [[BootstrapFewShotWithRandomSearch]] — cheaper baseline optimizers the tutorial does not compare against.

## Contradictions

None with the existing wiki. The result reinforces:
- The [[MIPROv2|MIPROv2]] page's claim that `auto="medium"` is the workhorse cross-task preset.
- The [[dspy-modules|`dspy.ChainOfThought`]] *start simple* recommendation — a one-line program is enough infrastructure to reach 88% on competition algebra after optimization.
- The pattern from [[dspy-tutorial-rag-as-agent]] and [[dbreunig-pipelines-prompt-optimization-dspy]] that `teacher_settings=dict(lm=<bigger model>)` is the canonical small-student rehabilitation pattern, even when both models come from the same provider.

## Scope-Limit Gaps

- Tutorial uses only the **algebra** subset; no results on the other 6 MATH topical splits (counting/probability, geometry, intermediate algebra, number theory, prealgebra, precalculus) or on the harder MATH-500 / MATH-hard slices.
- No cost or wall-time numbers reported; the [[dspy-optimizers|Optimizers page]]'s *~$2 typical / minutes-to-hours* envelope applies by extrapolation but is not directly characterized.
- No comparison to cheaper optimizers ([[BootstrapFewShot]] / [[BootstrapFewShotWithRandomSearch]]) that the [[dspy-optimizers|page 13 rubric]] would recommend for a 350-example training set.
- No comparison to [[GEPA]] (reflection-based instruction-only optimization), which the [[dspy-optimization-overview|Optimization Overview]] singles out for prompt-only tuning.
- No characterization of the `auto="light"` / `"heavy"` cost-vs-quality Pareto on this task.
- No prompt inspection in the tutorial — the optimized instruction is left for the reader to view via `dspy.inspect_history()`.
