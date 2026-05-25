---
title: "DSPy Metrics"
type: concept
tags: [dspy, llm-programming, evaluation, metrics, llm-as-judge, ai-feedback, bootstrap]
sources: [dspy-metrics, dspy-evaluation-overview, dspy-data, dspy-learn-index]
last_updated: 2026-05-24
---

# DSPy Metrics

**DSPy Metrics** are **Python functions** with the canonical signature `(example, pred, trace=None) -> score` that quantify how good a [[DSPyModules|DSPy program's]] output is. Introduced by [[dspy-metrics|the Metrics page]] (page 11 of 13 of the *Learn* section); the **third page of the [[DSPyEvaluation|Evaluation stage]]** (after [[dspy-evaluation-overview|the Evaluation Overview]] and [[dspy-data|Data Handling]]). The metric is the **interface contract between the Evaluation and Optimization stages** — *"automatic metrics for evaluation (to track your progress) and optimization (so DSPy can make your programs more effective)"* ([[dspy-metrics]]) — and the **only signal a [[DSPyOptimizers|DSPy Optimizer]] climbs**.

This concept page **resolves the long-standing forward reference [[DSPyMetrics]]** carried by [[DSPyEvaluation]] / [[dspy-evaluation-overview]] / [[dspy-data]] / [[DSPyExample]] / [[DSPyPrediction]] / [[DSPyModules]] / [[DSPyProgrammingModel]] / every prior DSPy ingest since the corpus opened on 2026-05-17.

## The canonical contract

```python
def metric(example, pred, trace=None) -> float | int | bool: ...
```

| Argument | Type | What it is |
|---|---|---|
| `example` | [[DSPyExample\|`dspy.Example`]] | One datapoint from the dev/train set (input fields + optional reference labels) |
| `pred` | [[DSPyPrediction\|`dspy.Prediction`]] | The [[DSPyModules\|Module's]] output — `program(**example.inputs())` |
| `trace` | `None` or a list of `(predictor, inputs, outputs)` tuples | `None` during evaluation/optimization; populated during bootstrapping |
| **return** | `float` / `int` / `bool` | The score — interpreted by [[DSPyEvaluate\|`dspy.Evaluate`]] and [[DSPyOptimizers\|Optimizers]] as a numeric quantity to climb |

Three properties make this contract structurally important:

- **Type-symmetric on the data side.** Because [[DSPyPrediction|`dspy.Prediction`]] is a subclass of [[DSPyExample|`dspy.Example`]] (a fact [[dspy-data|Data Handling]] established), the metric author writes `example.answer == pred.answer` with **no class-aware branching** — both arguments expose the same dot-access / `inputs()` / `labels()` surface.
- **Regime-asymmetric on the calling side.** The same metric is called with `trace=None` from [[DSPyEvaluate|`dspy.Evaluate`]] and with `trace=[...]` from a [[DSPyOptimizers|Optimizer's]] bootstrap phase. The metric author switches behavior on `if trace is None:` vs `if trace is not None:`.
- **Scalar return.** `float` / `int` / `bool` are the only valid return types — the metric must yield a quantity an optimizer can monotonically climb. `True`/`False` are summed by [[DSPyEvaluate|`dspy.Evaluate`]] as `1.0`/`0.0`.

## The two regimes

[[dspy-metrics|The Metrics page]] sharpens [[dspy-evaluation-overview|the Evaluation Overview's]] two-regime story into concrete code patterns:

### Regime 1 — Simple metrics (short-form tasks)

A one-line scalar function over reference labels:

```python
def validate_answer(example, pred, trace=None):
    return example.answer.lower() == pred.answer.lower()
```

Two **built-in utilities** the page names:

- `dspy.evaluate.metrics.answer_exact_match` — exact-match comparison of `example.answer` and `pred.answer` (case-insensitive).
- `dspy.evaluate.metrics.answer_passage_match` — checks `pred.answer` appears in one of the retrieved passages (the RAG-task built-in).

These are **reference-based metrics** in [[dspy-evaluation-overview|the Evaluation Overview's]] taxonomy — they require ground-truth final-output labels in the [[DSPyExample]]. Use for: classification, short-form QA, exact-match-graded tasks.

### Regime 2 — AI-feedback metrics (long-form tasks)

A DSPy program — typically a [[DSPySignatures|Signature]] (`Assess`) plus N [[DSPyPredict|`dspy.Predict`]] calls over different rubric dimensions — checks **multiple properties** of the output:

```python
class Assess(dspy.Signature):
    """Assess the quality of a tweet along the specified dimension."""
    assessed_text = dspy.InputField()
    assessment_question = dspy.InputField()
    assessment_answer: bool = dspy.OutputField()

def metric(gold, pred, trace=None):
    correct  = dspy.Predict(Assess)(assessed_text=pred.output,
                                    assessment_question=f"Does the text answer `{gold.question}` with `{gold.answer}`?")
    engaging = dspy.Predict(Assess)(assessed_text=pred.output,
                                    assessment_question="Does the text make for a self-contained, engaging tweet?")
    correct, engaging = correct.assessment_answer, engaging.assessment_answer
    score = (correct + engaging) if correct and (len(pred.output) <= 280) else 0
    if trace is not None: return score >= 2
    return score / 2.0
```

This is **DSPy's structural operationalization of [[llmasjudge|LLM-as-judge]]**: the judge is itself a typed [[DSPySignatures|Signature]] called through [[DSPyPredict|`dspy.Predict`]], adapted by an [[DSPyAdapters|Adapter]], routed through [[DSPyLM|`dspy.LM`]] — a **fully DSPy-native artifact**, not a hand-written prompt. The `Assess` signature is a **reusable rubric primitive**: one signature, many `assessment_question` strings, one [[DSPyPredict|`Predict`]] call per dimension.

Three structural patterns the worked metric demonstrates:

1. **Multi-property AI judgment.** Two `dspy.Predict(Assess)` calls produce two booleans, summed into a 0/1/2 score.
2. **Deterministic hard gates mixed with AI judgment.** `len(tweet) <= 280` is **not** an LM judgment; it's a plain Python expression in the same `score` computation. A DSPy metric is **not all-or-nothing AI-feedback** — it can and should combine LLM-as-judge with deterministic gates. In [[LLMModuloFramework|LLM-Modulo]] terms: the deterministic gate is a *sound critic*; the LM-judged dimensions are *soft critics*.
3. **AND-gated short-circuit.** `if correct and (len <= 280) else 0` encodes a *correctness-first, engagement-modulates* priority that pure averaging would lose — if the answer is wrong, the score is 0 regardless of engagement.

## The `trace` argument — the dual-purpose mechanism

The optional third argument `trace` is **what makes the same callable serve two distinct DSPy phases**:

| `trace` value | Calling phase | Return type | Purpose |
|---|---|---|---|
| `None` | **Evaluation / optimization** (via [[DSPyEvaluate\|`dspy.Evaluate`]] or an [[DSPyOptimizers\|Optimizer's]] dev-set pass) | **Continuous** `float` / `int` (e.g. `score / 2.0`) | The optimizer climbs this number |
| `list[(predictor, inputs, outputs)]` | **Bootstrapping** (an Optimizer's demo-collection phase) | **Strict** `bool` (e.g. `score >= 2`) | Decide whether to retain this trajectory as a few-shot demonstration |

The bootstrapping bar is **always strictly tighter** than the evaluation bar — only top-scoring trajectories become demos. This is **what makes [[DSPyOptimizers|optimizers like `BootstrapFewShotWithRandomSearch`]] possible**: they need a function that *both ranks candidates and gates demonstrations*, and a single `trace`-aware metric provides both.

The canonical idiom:

```python
def metric(example, pred, trace=None):
    score = ...                              # compute the continuous score
    if trace is not None:
        return score >= THRESHOLD            # strict gate for bootstrapping
    return score                             # continuous for evaluation/optimization
```

### The `trace` itself

When `trace is not None`, it is a list of `(predictor, inputs, outputs)` tuples — one per [[DSPyPredict|`dspy.Predict`]] call inside the program's `forward()`. The metric author can pull **any intermediate predictor's output** out of the trace:

```python
def validate_hops(example, pred, trace=None):
    hops = [example.question] + [outputs.query for *_, outputs in trace if 'query' in outputs]
    if max([len(h) for h in hops]) > 100: return False
    if any(dspy.evaluate.answer_exact_match_str(hops[idx], hops[:idx], frac=0.8) for idx in range(2, len(hops))): return False
    return True
```

This is **the only place in the [[dspy-learn-index|*Learn* corpus]] the developer is asked to inspect intermediate steps**, and it is **bootstrap-only** — *"DSPy will not try to track the steps of your program"* during plain evaluation ([[dspy-metrics]]). The trace is the **anti-degenerate-trajectory filter** for [[DSPyModules|multi-hop modules]] like the `Hop` example from [[dspy-modules]] — structurally constrain *what counts as a good demonstration* without labeling intermediate steps.

## Metric definition is iterative

[[dspy-metrics|The Metrics page]] restates [[dspy-evaluation-overview|the Evaluation Overview's]] *start-simple-then-grow* discipline at the API level: *"Getting this right on the first try is unlikely, but you should start with something simple and iterate"*. The simple `answer_exact_match` metric is the *"start simple"* anchor; the AI-feedback metric is the *"grow"* destination. The metric has **versions** over the project's lifetime; a change in metric definition may invalidate prior baselines.

## Recursive metric optimization

[[dspy-metrics|The Metrics page]] anchors [[DSPyEvaluation|the Evaluation stage's]] **recursive-self-improvement** claim (Step 4 of the four-step loop): *"If your metric is itself a DSPy program, one of the most powerful ways to iterate is to compile (optimize) your metric itself. That's usually easy because the output of the metric is usually a simple value (e.g., a score out of 5) so the metric's metric is easy to define and optimize by collecting a few examples."* When the metric is a Regime-2 program (calls `dspy.Predict(Assess)`), it has **learnable parameters** — the `Assess` signature's instructions, its few-shot demonstrations, the underlying LM's prompts — therefore it is **optimizable by a [[DSPyOptimizers|DSPy Optimizer]]** the same way the system program is. The "metric of the metric" is a `(metric_example, metric_pred) -> bool` function over a small set of labeled outputs (e.g. *"this rubric judgment was right, this one was wrong"*) — **easier to define and label** than the original metric because the metric's output is **bounded and scalar**.

This makes the Evaluation stage **recursively self-improving** — a claim no other LLM-evaluation framework the wiki has recorded makes explicit.

## Metrics span the evaluation/optimization boundary

The metric is **not just a measurement instrument** — it is **the only signal the [[DSPyOptimizers|Optimizer]] climbs**. Three consequences:

- **The Optimizer's objective function is the metric.** [[DSPyOptimizers|Optimizers]] like `BootstrapFewShotWithRandomSearch`, `MIPROv2`, `BootstrapFinetune` (forward references to page 13) search over instructions / demonstrations / weights to **maximize the metric**. If the metric is wrong, the optimizer climbs the wrong hill.
- **The Optimizer's demonstrations come from the metric's bootstrap branch.** When `trace is not None`, the metric's strict-boolean return selects which trajectories become few-shot demos for the next optimization iteration.
- **The baseline an Optimizer must beat is the metric on the dev set under the unoptimized program.** Without a metric, there is no baseline, and *"optimization"* is just running the program more.

This is why [[dspy-learn-index|the Learn index]] is explicit: *"it's unproductive to launch optimization runs using a poorly designed program or a bad metric."*

## Position in the wiki's evaluation landscape

DSPy Metrics is the wiki's first **framework-level operationalization of the LLM-as-judge contract** as executable typed Python:

- **vs. ad-hoc [[llmasjudge|LLM-as-judge]] prompts in the broader literature.** Most LLM-as-judge implementations are hand-written prompts with brittle output-parsing. DSPy's version is **structurally different**: the judge is a typed [[DSPySignatures|Signature]] with a `bool` output type, called via [[DSPyPredict|`dspy.Predict`]], adapted by an [[DSPyAdapters|Adapter]], routed through [[DSPyLM|`dspy.LM`]] — i.e. the judge **composes with the rest of DSPy** the same way every other Module does. The judge is **swappable** across LMs ([[DSPyLM]]) and adapters ([[DSPyAdapters]]), and **optimizable** by [[DSPyOptimizers|Optimizers]].
- **vs. [[ModelEvaluation]] (the general concept).** [[ModelEvaluation]] is *"measuring model quality on a held-out set"* in general. DSPy Metrics is the **DSPy-specific operationalization**: the `(example, pred, trace) -> score` contract, the two regimes, the dual-purpose `trace` argument. Narrower (specific to programs over LMs), richer (commits to the contract + the bootstrap mechanism).
- **vs. [[OfflineEvaluation]] / [[OnlineEvaluation]].** DSPy Metrics is unambiguously **offline** — the metric is applied to held-out dev-set examples, not live traffic. [[OnlineEvaluation]] is out of scope.
- **vs. [[LLMModuloFramework|LLM-Modulo]].** DSPy Metrics are precisely the *critic* layer in Kambhampati et al.'s generate-test-critique loop. The Regime-1 reference-based metric is a *deterministic critic*; the Regime-2 AI-feedback metric is a *soft critic* (LM-graded). The *"composite metric mixing hard gates and AI judgments"* the tweet receipt demonstrates is the canonical hybrid-critic shape [[LLMModuloFramework|LLM-Modulo]] argues for.
- **vs. [[2604.25850-agentic-harness-engineering|AHE]].** AHE's *"the metric must measure tool-use quality, not just final-output quality"* maps onto the `validate_hops` recipe — both are about validating **intermediate steps** of the trajectory. DSPy's contribution is that this validation is **bootstrap-only** (via the `trace` argument) and that the metric **need not change** when moving from final-output scoring to trajectory scoring — same function, different branch.

## Built-in metric utilities

[[dspy-metrics|The Metrics page]] names two scalar metric utilities pre-built in DSPy:

| Utility | Path | Returns | Use case |
|---|---|---|---|
| `answer_exact_match` | `dspy.evaluate.metrics.answer_exact_match` | `bool` | Compare `example.answer` to `pred.answer` (case-insensitive) |
| `answer_passage_match` | `dspy.evaluate.metrics.answer_passage_match` | `bool` | Check `pred.answer` appears in one of the retrieved passages (RAG) |

A third utility named only in the bootstrap-trace example: `dspy.evaluate.answer_exact_match_str(s, [s_list], frac=0.8)` — fuzzy-string match used as the anti-degenerate-trajectory test in `validate_hops`.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-tutorial-math]] — Regime-1 scalar metric: `dataset.metric` is the built-in [[MATH-benchmark|MATH]] exact-match `int(prediction.answer) == int(example.answer)` over the algebra subset.
- [[dspy-tutorial-classification-finetuning]] — Regime-1 accuracy: `metric` is plain label-equality `x.label == y.label` over Banking77; the same callable drives [[DSPyEvaluate|`dspy.Evaluate`]] and [[BootstrapFinetune|`dspy.BootstrapFinetune`]].
- [[dspy-entity-extraction-tutorial]] — Regime-1 **custom** metric: `extraction_correctness_metric(example, pred, trace=None)` compares `set(pred.entities)` against `set(example.entities)` for exact-list match over CoNLL-2003 PER spans.
- [[dspy-tool-use-tutorial]] — task-aware normalization metric (`rstrip(".0").replace(",", "").lower()`) for the [[ToolHop]] benchmark; first wiki receipt where the metric's normalization rules become the optimizer's primary lift target.
- [[dspy-rag-tutorial]] — Regime-2 LLM-as-judge: [[SemanticF1]] is a `dspy.Module` (multi-property judgment over claim coverage) — the canonical *"metric is itself a DSPy program"* receipt the page commits to.
- [[dspy-multihop-search-tutorial]] — dual-mode `top5_recall(example, pred, trace=None)` — returns continuous recall during evaluation, strict `recall >= 1.0` boolean during bootstrapping; the canonical worked example of the `trace`-aware idiom.
- [[dspy-tutorial-gepa-aime]] — first wiki receipt of the **`Prediction(score, feedback)` metric shape**: `metric_with_feedback` returns a [[DSPyPrediction|`dspy.Prediction`]] carrying both the scalar score and textual feedback for [[GEPA|`dspy.GEPA`]]'s reflective proposer.
- [[dspy-tutorial-gepa-facility-support-analyzer]] — extends the GEPA metric shape to **multi-property weighted-average** (urgency / sentiment / categories sub-scores) with **per-predictor feedback strings**; the most structurally complex DSPy metric in the corpus.

## Connections

- [[DSPy]] — the framework whose Evaluation stage this concept anchors.
- [[dspy-metrics]] — the canonical source for this concept (page 11 of 13 of the *Learn* section); mints this page.
- [[DSPyEvaluation]] — the parent concept (the Evaluation stage); this concept operationalizes its Step 2 (*"define a DSPy metric"*).
- [[DSPyEvaluate]] — the sibling concept minted by the same ingest; the dev-set-evaluation utility that **calls** metrics conforming to this contract.
- [[dspy-evaluation-overview]] — page 9 of 13; forward-references this concept for the full metric contract.
- [[dspy-data]] — page 10 of 13; establishes the type-symmetry ([[DSPyPrediction|`Prediction`]] is a subclass of [[DSPyExample|`Example`]]) that makes the metric's `(example, pred)` contract compose without class-aware branching.
- [[DSPyExample]] — the metric's first argument type; provides `.inputs()` (used as `program(**x.inputs())`), `.labels()`, dot-notation field access.
- [[DSPyPrediction]] — the metric's second argument type; subclass of `Example`.
- [[DSPyModules]] — the metric is applied to the output of a `dspy.Module`'s `forward()`; the AI-feedback metric is itself a [[DSPyModules|Module]]-like artifact.
- [[DSPyPredict]] — the substrate every AI-feedback metric is built on; the metric calls `dspy.Predict(Assess)(...)` once per rubric dimension.
- [[DSPySignatures]] — the rubric template (`class Assess(dspy.Signature)`) is a Signature; uses the `bool`-output tier of [[DSPySignatures|page 4]]'s five-tier type system.
- [[DSPyAdapters]] — the AI-feedback metric is **adapter-portable**; the `Assess` Signature works under any [[DSPyAdapters|Adapter]].
- [[DSPyLM]] — the AI-feedback metric routes through `dspy.LM` like any other DSPy program; the judge can be a different model than the system.
- [[DSPyOptimizers]] — **forward reference to page 13 of 13**; the consumer of metrics conforming to this contract. The dual-purpose `trace` argument is what makes the contract usable by bootstrap-based optimizers (`BootstrapFewShotWithRandomSearch`, `MIPROv2`, `BootstrapFinetune`).
- [[DSPyProgrammingModel]] — the *"start simple, then grow"* discipline from page 2 is restated at the metric layer.
- [[ChainOfThought]] — AI-feedback metrics can use `dspy.ChainOfThought(Assess)` instead of `dspy.Predict(Assess)` for reasoning-enabled judges; the substitution is structurally identical.
- [[llmasjudge|LLM-as-judge]] — DSPy Metrics is **DSPy's structural operationalization** of this general pattern; the judge is a typed [[DSPySignatures|Signature]], not a hand-written prompt.
- [[ModelEvaluation]] — the general wiki concept this DSPy-specific concept specializes.
- [[OfflineEvaluation]] — the regime DSPy Metrics operates in; held-out dev-set evaluation, not live traffic.
- [[LLMModuloFramework]] — DSPy Metrics are precisely the *critic* layer in Kambhampati et al.'s Generate-Test-Critique loop; hybrid hard-gate-plus-soft-judge is the canonical shape.
- [[2604.25850-agentic-harness-engineering]] — AHE's *"measure tool-use quality"* prescription maps onto the `validate_hops` trace-aware recipe.
- [[PromptEngineering]] — the manual baseline DSPy displaces; the AI-feedback metric is what an automated, optimizable judge looks like in the DSPy world.
