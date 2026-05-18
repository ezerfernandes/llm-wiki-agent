---
title: "DSPy Learn — Metrics"
type: source
tags: [dspy, llm-programming, evaluation, metrics, llm-as-judge, ai-feedback]
date: 2026-05-17
source_file: raw/dspy-metrics.md
---

# DSPy Learn — Metrics

## Summary

**Page 11 of 13** of the [[DSPy]] *Learn* documentation; **third page of the [[DSPyEvaluation|Evaluation stage]]** (after [[dspy-evaluation-overview|the Evaluation Overview]] page 9 and [[dspy-data|Data Handling]] page 10). Expands **Step 2** of [[DSPyEvaluation|the four-step iterative-evaluation loop]] — *"define a DSPy metric"* — into the concrete **`(example, pred, trace=None) -> score`** function-signature contract every other DSPy artifact composes against. The page is structurally analogous to [[dspy-data]] in the same stage: short, deliberately small API surface, every claim in it load-bearing for the rest of DSPy. The canonical claim is that **a DSPy metric is a Python function** — *"A DSPy metric is just a function in Python that takes `example` (e.g., from your training or dev set) and the output `pred` from your DSPy program, and outputs a `float` (or `int` or `bool`) score."* — and that the **optional third argument `trace`** is the **dual-purpose-metric mechanism** that lets the same callable serve both **evaluation/optimization** (`trace is None`) and **bootstrapping** (`trace is not None`). The page also defines **two regimes** the Evaluation Overview only named — **simple boolean / numeric metrics** for short-form tasks (`answer_exact_match`, `answer_passage_match`, hand-written `validate_*`) and **AI-feedback metrics** for long-form tasks (a [[dspy.Signature]] `Assess` plus N `dspy.Predict(Assess)` invocations summed and thresholded, DSPy's structural operationalization of the [[llmasjudge|LLM-as-judge]] pattern). Closes with a **trace-aware bootstrapping recipe** (`validate_hops` — inspect intermediate predictor outputs during optimization) and the **`dspy.Evaluate`** utility (a parallel-evaluation harness over a dev set with progress display and tabular result rendering). Mints the [[DSPyMetrics]] concept page as the canonical anchor for the metric contract and the [[DSPyEvaluate]] concept page for the dev-set-evaluation utility — **resolves the long-standing forward reference [[DSPyMetrics]]** carried by [[DSPyEvaluation]] / [[dspy-evaluation-overview]] / [[dspy-data]] / [[DSPyExample]] / [[DSPyPrediction]] / every prior DSPy ingest since the corpus opened.

## Key Claims

- **A metric is a Python function with signature `(example, pred, trace=None) -> score`.** *"A DSPy metric is just a function in Python that takes `example` (e.g., from your training or dev set) and the output `pred` from your DSPy program, and outputs a `float` (or `int` or `bool`) score."* This is the canonical metric contract. The metric is **executable Python** — not a string, not a static threshold, not a configuration value. The return type is **scalar** — `float` / `int` / `bool` — and the three are interconvertible at evaluation time (`True`/`False` summed by [[DSPyEvaluate|`dspy.Evaluate`]] is `1.0`/`0.0`). This sharpens [[dspy-evaluation-overview|the Evaluation Overview's]] *"a function that takes examples from your data and takes the output of your system, and returns a score"* into a typed Python function signature.

- **The `trace` argument is the dual-purpose mechanism.** *"Your metric should also accept an optional third argument called `trace`. You can ignore this for a moment, but it will enable some powerful tricks if you want to use your metric for both evaluation and optimization."* The same callable serves **two distinct DSPy phases** depending on whether `trace` is `None`:
  - **`trace is None`** — *"if we're doing evaluation or optimization"*. The metric is being called from [[DSPyEvaluate|`dspy.Evaluate`]] or from an [[DSPyOptimizers|Optimizer's]] dev-set evaluation pass. The metric returns a **continuous score** ($\in [0, 1]$ typically) the optimizer can climb.
  - **`trace is not None`** — *"if we're doing bootstrapping, i.e. self-generating good demonstrations of each step"*. The metric is being called from an Optimizer's bootstrap phase, deciding **whether to retain a candidate trajectory as a few-shot demonstration**. The metric returns a **strict boolean** (e.g. `score >= 2`) — an example only becomes a demo if it scores at the top of the scale. This is the structural reason DSPy's metric is a function, not a number — the **same code** computes both signals and decides which to emit based on the argument.

- **Two metric regimes: simple (scalar) and AI-feedback (LLM-as-judge).** The page operationalizes [[dspy-evaluation-overview|the Evaluation Overview's]] *"scalar `accuracy` for simple tasks; a smaller DSPy program for long-form tasks"* claim into two worked subsections:
  - **Simple metrics** — *"`example.answer.lower() == pred.answer.lower()`"* — a one-line exact-match. The page also names two built-in utilities: `dspy.evaluate.metrics.answer_exact_match` and `dspy.evaluate.metrics.answer_passage_match`. These are reference-based metrics (per [[dspy-evaluation-overview|the Overview's]] *"inputs and final outputs"* labeling regime) and require ground-truth labels in the [[DSPyExample]].
  - **AI-feedback / LLM-as-judge metrics** — a [[DSPySignatures|`dspy.Signature`]] (`class Assess(dspy.Signature)` with `assessed_text` / `assessment_question` inputs and a `bool` `assessment_answer` output) plus N `dspy.Predict(Assess)` invocations over different rubric questions. The page's worked tweet example checks **two properties** (`correct` — does the tweet contain the answer; `engaging` — is the tweet engaging) via two `Predict` calls plus **one hard constraint** (`len(tweet) <= 280`). This is **DSPy's structural operationalization of the [[llmasjudge|LLM-as-judge]] pattern**: the judge is itself a typed [[DSPySignatures|Signature]] called through [[DSPyPredict|`dspy.Predict`]], adapted by an [[DSPyAdapters|Adapter]], routed through [[DSPyLM|`dspy.LM`]] — i.e. a fully-DSPy-native artifact, not a hand-written prompt.

- **A composite metric combines AI feedback, hard constraints, and the `trace`-based regime switch.** The tweet metric:
  ```python
  score = (correct + engaging) if correct and (len(tweet) <= 280) else 0
  if trace is not None: return score >= 2
  return score / 2.0
  ```
  combines three patterns: (1) **multi-property AI judgment** (`correct` + `engaging`), (2) **a deterministic hard gate** (`correct and len <= 280` — both required for any positive score), and (3) the **regime-dependent return type** (`>= 2` boolean for bootstrapping, `/2.0` continuous for evaluation). This is the page's most consequential code receipt — it shows the metric is a **first-class DSPy program** that combines deterministic code with [[DSPyPredict|`dspy.Predict`]] calls and switches behavior on the calling context.

- **A `dspy.Signature` rubric is the canonical AI-feedback primitive.** The `Assess` signature is a generic **rubric template**: `assessed_text` (the candidate output) + `assessment_question` (the rubric in natural language) → `assessment_answer: bool`. The same signature is reused across all rubric dimensions — the variation is in the `assessment_question` string passed at call time. This is a **reusable judge primitive**: define the signature once, instantiate `dspy.Predict(Assess)` once per dimension, sum the booleans. The author of a long-form metric writes **one signature, many questions**, not many signatures.

- **The `trace`-aware bootstrapping recipe inspects intermediate predictor outputs.** *"But during compiling (optimization), DSPy will trace your LM calls. The trace will contain inputs/outputs to each DSPy predictor and you can leverage that to validate intermediate steps for optimization."* The page's `validate_hops` example reads `[outputs.query for *_, outputs in trace if 'query' in outputs]` — pulling the **`query` field from every predictor output that produced one** — then validates two intermediate-step properties (`len(query) <= 100` and *"no two consecutive queries are 80%+ identical"*). This is the **only place in the *Learn* corpus so far** the developer is asked to look at intermediate steps, and it is **bootstrap-only** — *"DSPy will not try to track the steps of your program"* during plain evaluation. The trace is unpacked with `*_, outputs` (discard everything but the last per-tuple element) — i.e. the trace is a sequence of `(predictor, inputs, outputs)` tuples per LM call.

- **`dspy.Evaluate` is the parallel-evaluation harness.** *"If you need some utilities, you can also use the built-in `Evaluate` utility. It can help with things like parallel evaluation (multiple threads) or showing you a sample of inputs/outputs and the metric scores."* The page's worked usage:
  ```python
  from dspy.evaluate import Evaluate
  evaluator = Evaluate(devset=YOUR_DEVSET, num_threads=1, display_progress=True, display_table=5)
  evaluator(YOUR_PROGRAM, metric=YOUR_METRIC)
  ```
  documents four configuration kwargs: `devset` (a `list[dspy.Example]`), `num_threads` (parallelism), `display_progress` (TQDM-style bar), and `display_table=N` (sample first N rows in a tabular display). The evaluator is **reusable** — *"can be re-used in your code"* — instantiate once, call multiple times with different programs against the same dev set. The two-line baseline equivalent the page shows first (`for x in devset: pred = program(**x.inputs()); score = metric(x, pred)`) makes explicit what `Evaluate` is doing: it's a **thread-parallel wrapper** around that loop with display ergonomics. **Note `program(**x.inputs())`** — uses [[DSPyExample|`Example.inputs()`]] from [[dspy-data|page 10]] to extract only the input fields before passing to the program. This is the structural reason `Example.inputs()` exists: it's the canonical bridge from a `list[dspy.Example]` to a program-callable input dict.

- **Defining a good metric is iterative.** *"Defining a good metric is an iterative process, so doing some initial evaluations and looking at your data and your outputs is key."* This restates [[dspy-evaluation-overview|the Evaluation Overview's]] *"Invest in defining metrics and improving them incrementally over time"* and *"Getting this right on the first try is unlikely, but you should start with something simple and iterate"* — i.e. the page **commits** the framework to the *metric-is-a-moving-target* discipline at the API level. The simple `answer_exact_match` metric is the *"start simple"* anchor; the AI-feedback metric is the *"grow"* destination.

- **Recursive metric optimization is operationalized at this page.** *"If your metric is itself a DSPy program, one of the most powerful ways to iterate is to compile (optimize) your metric itself. That's usually easy because the output of the metric is usually a simple value (e.g., a score out of 5) so the metric's metric is easy to define and optimize by collecting a few examples."* This is the same claim [[dspy-evaluation-overview|the Evaluation Overview]] made (Step 4 of the four-step loop), now anchored to the concrete `dspy.Predict(Assess)`-based AI-feedback pattern. The metric is **a DSPy program** because it calls `dspy.Predict(Assess)` — therefore it has learnable parameters (the `Assess` signature's instructions, its few-shot demonstrations, the underlying LM's prompts) — therefore it is **optimizable by a [[DSPyOptimizers|DSPy Optimizer]]** the same way the system program is. The "metric of the metric" is a `(metric_example, metric_pred) -> bool` function over a small set of labeled outputs (e.g. *"this rubric output was the right judgment, this one was wrong"*) — easier to define and label than the original metric because the metric's output is **bounded and scalar**.

- **Metrics span the evaluation/optimization boundary.** The page opens with: *"automatic metrics for evaluation (to track your progress) and optimization (so DSPy can make your programs more effective)"*. This is the page's compact statement of **what a metric is *for***: it's not just a measurement instrument — it is **the only signal the [[DSPyOptimizers|Optimizer]] climbs**. The metric is therefore the **interface contract between the Evaluation and Optimization stages**: get the metric wrong and the optimizer climbs the wrong hill. This restates [[DSPyEvaluation|the Evaluation concept's]] *"the metric is the function the Optimizer maximizes"* commitment, now from the metric-page side.

## Key Quotes

> "DSPy is a machine learning framework, so you must think about your **automatic metrics** for evaluation (to track your progress) and optimization (so DSPy can make your programs more effective)." — opens the page; the metric's role spans both Evaluation and Optimization stages.

> "A DSPy metric is just a function in Python that takes `example` (e.g., from your training or dev set) and the output `pred` from your DSPy program, and outputs a `float` (or `int` or `bool`) score." — the canonical metric contract.

> "Your metric should also accept an optional third argument called `trace`. You can ignore this for a moment, but it will enable some powerful tricks if you want to use your metric for both evaluation and optimization." — names the dual-purpose `trace` argument.

> "For simple tasks, this could be just 'accuracy' or 'exact match' or 'F1 score'. This may be the case for simple classification or short-form QA tasks. However, for most applications, your system will output long-form outputs. There, your metric should probably be a smaller DSPy program that checks multiple properties of the output (quite possibly using AI feedback from LMs)." — the two-regime metric story, sharpened from the Evaluation Overview.

> "Getting this right on the first try is unlikely, but you should start with something simple and iterate." — the *start-simple-then-grow* discipline at the metric layer.

> "If your metric is itself a DSPy program, one of the most powerful ways to iterate is to compile (optimize) your metric itself. That's usually easy because the output of the metric is usually a simple value (e.g., a score out of 5) so the metric's metric is easy to define and optimize by collecting a few examples." — the recursive-metric-optimization claim, anchored to the page-11 `Assess`-signature pattern.

> "When your metric is used during evaluation runs, DSPy will not try to track the steps of your program. But during compiling (optimization), DSPy will trace your LM calls. The trace will contain inputs/outputs to each DSPy predictor and you can leverage that to validate intermediate steps for optimization." — the trace's bootstrap-only availability rule.

## Worked Code Receipts

### Receipt 1 — The simple boolean metric

```python
def validate_answer(example, pred, trace=None):
    return example.answer.lower() == pred.answer.lower()
```

The minimal viable metric. Demonstrates the three-argument signature, the dot-notation `.answer` access on both [[DSPyExample|`Example`]] and [[DSPyPrediction|`Prediction`]] (the type-symmetry [[dspy-data|page 10]] established), and the `bool` return type. **No `trace` use** — the function is correct for both regimes because the same boolean is the right answer in both.

### Receipt 2 — The `trace`-aware composite metric

```python
def validate_context_and_answer(example, pred, trace=None):
    answer_match = example.answer.lower() == pred.answer.lower()
    context_match = any((pred.answer.lower() in c) for c in pred.context)

    if trace is None:        # evaluation or optimization
        return (answer_match + context_match) / 2.0
    else:                    # bootstrapping
        return answer_match and context_match
```

The first time the page uses `trace` to switch return semantics. `(answer_match + context_match) / 2.0` returns one of `{0.0, 0.5, 1.0}` for evaluation; `answer_match and context_match` returns `True` only when **both** properties hold for bootstrapping — a strictly stronger gate. This is the canonical pattern: **continuous score for evaluation, AND-gate for bootstrapping**.

### Receipt 3 — The AI-feedback rubric signature

```python
class Assess(dspy.Signature):
    """Assess the quality of a tweet along the specified dimension."""

    assessed_text = dspy.InputField()
    assessment_question = dspy.InputField()
    assessment_answer: bool = dspy.OutputField()
```

A **generic rubric primitive**: same signature for every dimension, the dimension is supplied per-call as `assessment_question`. The `bool` output type ([[DSPySignatures|page 4]]'s five-tier type system, basic-Python tier) is the most-constrained available — the LM must answer Yes/No, not free-form. This is **the canonical LLM-as-judge sub-program** in DSPy.

### Receipt 4 — The composite AI-feedback metric

```python
def metric(gold, pred, trace=None):
    question, answer, tweet = gold.question, gold.answer, pred.output

    engaging = "Does the assessed text make for a self-contained, engaging tweet?"
    correct = f"The text should answer `{question}` with `{answer}`. Does the assessed text contain this answer?"

    correct =  dspy.Predict(Assess)(assessed_text=tweet, assessment_question=correct)
    engaging = dspy.Predict(Assess)(assessed_text=tweet, assessment_question=engaging)

    correct, engaging = [m.assessment_answer for m in [correct, engaging]]
    score = (correct + engaging) if correct and (len(tweet) <= 280) else 0

    if trace is not None: return score >= 2
    return score / 2.0
```

The page's most consequential receipt — combines **multi-property AI judgment**, a **deterministic hard gate** (`len(tweet) <= 280`), and the **regime switch**. Note the **AND-gated short circuit**: if `correct` is False or the tweet is too long, the score is `0` regardless of `engaging` — i.e. the metric encodes a *correctness-first, engagement-modulates* priority that pure averaging would lose. The bootstrapping branch returns `True` only when the score reaches `2` — the maximum — i.e. **only top-scoring examples become demos**. The evaluation branch returns `score / 2.0` ∈ {0.0, 0.5, 1.0}.

### Receipt 5 — The `dspy.Evaluate` harness

```python
from dspy.evaluate import Evaluate

evaluator = Evaluate(devset=YOUR_DEVSET, num_threads=1, display_progress=True, display_table=5)
evaluator(YOUR_PROGRAM, metric=YOUR_METRIC)
```

A **reusable evaluation object**: the dev set and ergonomic kwargs are bound at construction; the program and metric are supplied per-invocation. The same `evaluator` can compare multiple candidate programs against the same dev set with the same metric — i.e. it is **the dev-set-comparison primitive** the [[DSPyOptimizers|Optimizer]] uses internally and the developer uses externally during the [[DSPyEvaluation|four-step loop]]'s Step 3. The two-line raw equivalent (`for x in devset: pred = program(**x.inputs()); score = metric(x, pred)`) makes the abstraction visible — `Evaluate` is a thread-parallel wrapper around it.

### Receipt 6 — The trace-aware bootstrap validator

```python
def validate_hops(example, pred, trace=None):
    hops = [example.question] + [outputs.query for *_, outputs in trace if 'query' in outputs]

    if max([len(h) for h in hops]) > 100: return False
    if any(dspy.evaluate.answer_exact_match_str(hops[idx], hops[:idx], frac=0.8) for idx in range(2, len(hops))): return False

    return True
```

The only intermediate-step validator in the *Learn* corpus so far. Pulls every predictor's `query` output field from the trace and validates two **structural** properties of the multi-hop search trajectory: (1) no hop is too long; (2) no hop is too similar to a previous one (80% fuzzy match). Returns a strict boolean — usable only in `trace is not None` bootstrap mode. This is the **anti-degenerate-trajectory filter** for [[DSPyModules|multi-hop modules]] like the `Hop` example from [[dspy-modules]]. Demonstrates that **intermediate-step quality is the Optimizer's job to discover** ([[dspy-evaluation-overview|Evaluation Overview's]] commitment) but can be **structurally constrained** at bootstrap time via the trace.

## The `(example, pred, trace) -> score` contract

The page's most important contribution is the formal contract for what every DSPy metric must be:

| Argument | Type | What it is | Source |
|---|---|---|---|
| `example` | [[DSPyExample\|`dspy.Example`]] | One datapoint from the dev set | [[dspy-data\|Data Handling]] (page 10) |
| `pred` | [[DSPyPrediction\|`dspy.Prediction`]] | The program's output for `example.inputs()` | [[dspy-modules\|Modules]] (page 5) |
| `trace` | `None` (evaluation/optimization) or `list[(predictor, inputs, outputs)]` (bootstrapping) | The per-predictor I/O trace; `None` outside compilation | This page |
| **return** | `float` / `int` / `bool` | The score | This page |

The contract is **type-symmetric** on the data side ([[DSPyPrediction|`Prediction`]] is a subclass of [[DSPyExample|`Example`]] per [[dspy-data|page 10]] — both have dot-access / `inputs()` / `labels()`) and **regime-asymmetric** on the calling side (the same metric is called with `trace=None` from [[DSPyEvaluate|`dspy.Evaluate`]] and with `trace=[...]` from an [[DSPyOptimizers|Optimizer's]] bootstrap phase).

## The dual-purpose-`trace` pattern

The `trace` argument is the **single most important DSPy-specific feature** of the metric contract — it is what makes a metric **dual-purpose** across DSPy's two compilation phases:

```
evaluation / optimization      ←  trace is None    →  returns float/int   (a score the Optimizer climbs)
bootstrapping (demo selection) ←  trace is not None →  returns bool        (keep this trajectory as a demo? Y/N)
```

The pattern lets a single function express both *"how good is this prediction"* and *"is this prediction good enough to be a demonstration"*. The bootstrapping bar is **always strictly tighter** (a strict boolean threshold on the top of the score scale) — only top-scoring trajectories become few-shot demonstrations. This is what makes [[DSPyOptimizers|optimizers like `BootstrapFewShotWithRandomSearch`]] possible: they need a function that **both ranks candidates and gates demonstrations**, and a single `trace`-aware metric provides both.

## Connections

- [[DSPy]] — the framework whose Evaluation stage this page is the third page of.
- [[dspy-learn-index]] — the three-stage Programming → Evaluation → Optimization model; this page is **page 11 of 13** and **Step 2** of the Evaluation stage's four-step loop.
- [[DSPyMetrics]] — the canonical concept page minted by this ingest; the *"`(example, pred, trace) -> score`"* contract, the two regimes (simple vs AI-feedback), the dual-purpose `trace` argument, the built-in utilities (`answer_exact_match` / `answer_passage_match`), and the recursive-metric-optimization claim. **Resolves the long-standing forward reference** carried by [[DSPyEvaluation]] / [[dspy-evaluation-overview]] / [[dspy-data]] / [[DSPyExample]] / [[DSPyPrediction]] / every prior DSPy ingest.
- [[DSPyEvaluate]] — the canonical concept page minted by this ingest for the [[dspy.evaluate.Evaluate]] dev-set-evaluation utility; a reusable parallel-evaluation harness over a dev set with progress display and tabular result rendering.
- [[DSPyEvaluation]] — the parent concept (the Evaluation stage); this page operationalizes its Step 2 (*"define a DSPy metric"*) into the function-signature contract.
- [[dspy-evaluation-overview]] — page 9 of 13; opens the Evaluation stage and forward-references this page for the metric contract.
- [[dspy-data]] — page 10 of 13; the **prerequisite** page — the metric's first argument is a [[DSPyExample|`dspy.Example`]] from a `list[dspy.Example]` dev set, and `program(**x.inputs())` uses the [[DSPyExample|`Example.inputs()`]] partition accessor.
- [[DSPyExample]] — the metric's first argument type; the [[dspy-data]]-minted data primitive.
- [[DSPyPrediction]] — the metric's second argument type; a subclass of [[DSPyExample|`Example`]], makes the contract type-symmetric.
- [[DSPyModules]] — the metric is called on the output of a `dspy.Module`'s `forward()`; the AI-feedback metric *is itself a [[DSPyModules|Module]]-like artifact* built from [[DSPyPredict|`dspy.Predict`]] over an `Assess` Signature.
- [[DSPyPredict]] — the substrate every metric-as-DSPy-program is built on; the tweet metric calls `dspy.Predict(Assess)(...)` twice.
- [[DSPySignatures]] — the rubric template (`class Assess(dspy.Signature)`) is a Signature; the `bool` output type uses [[DSPySignatures|page 4]]'s five-tier type system.
- [[DSPyAdapters]] — the Adapter is what turns the `Assess` Signature into the LM's wire format; the metric is **adapter-portable** the same way the system program is.
- [[DSPyLM]] — the AI-feedback metric routes through `dspy.LM` like any other DSPy program.
- [[DSPyOptimizers]] — forward reference to page 13 of 13; the consumer of this metric. The dual-purpose `trace` argument is what makes a metric usable by bootstrap-based optimizers like `BootstrapFewShotWithRandomSearch`. The recursive-metric-optimization claim — *"compile (optimize) your metric itself"* — is realized here.
- [[ChainOfThought]] — the AI-feedback metric could use `dspy.ChainOfThought(Assess)` instead of `dspy.Predict(Assess)` for reasoning-enabled judges; this page only demonstrates the `Predict` form but the substitution is the same as anywhere else in DSPy.
- [[llmasjudge|LLM-as-judge]] — the AI-feedback metric pattern is DSPy's structural operationalization of the [[llmasjudge|LLM-as-judge]] pattern; the judge is a typed [[DSPySignatures|Signature]] not a hand-written prompt.
- [[DSPyProgrammingModel]] — the *"start simple, then grow"* discipline from page 2 is restated at the metric layer; the metric is a [[DSPyModules|Module]]-like artifact under the four-concerns decomposition.
- [[ModelEvaluation]] — the general wiki concept this DSPy-specific metric layer specializes.
- [[OfflineEvaluation]] — the regime [[DSPyEvaluate|`dspy.Evaluate`]] operates in; the dev set is held-out, not live traffic.
- [[2604.25850-agentic-harness-engineering]] — AHE's *"the metric must measure tool-use quality"* prescription maps directly onto the `validate_hops` recipe — both are about validating intermediate steps of the trajectory.
- [[LLMModuloFramework]] — DSPy's [[DSPyMetrics|metric]] is the *critic* in Kambhampati et al.'s Generate-Test-Critique loop; the AI-feedback metric is the *soft critic* (LLM-graded), the deterministic hard gate (`len <= 280`) is the *sound critic*.

## Contradictions

- **None new.** This page **extends** every prior DSPy ingest:
  - It **fulfills** [[dspy-evaluation-overview|the Evaluation Overview's]] forward reference (*"page 11 will expand the metric into the full `(example, prediction) -> score` contract"*) — the contract now includes a third argument `trace` the Overview didn't name, but this is an **expansion**, not a contradiction.
  - It **vindicates** [[dspy-data|the Data Handling page's]] *"`Prediction` is a subclass of `Example`"* — the metric reads `example.answer.lower() == pred.answer.lower()` with no class-aware branching, exactly as the type-symmetry predicted.
  - It **operationalizes** [[dspy-evaluation-overview|the Overview's]] *"smaller DSPy program that checks multiple properties of the output"* as the concrete `Assess` Signature + N `dspy.Predict(Assess)` pattern.
  - It **operationalizes** the recursive-self-improvement claim (Step 4 of the four-step loop) as the *"compile your metric itself"* observation grounded in the AI-feedback metric's `dspy.Predict(Assess)` calls (which are themselves optimizable parameters).
- **One framing nuance to track.** The page does not formally state that the AI-feedback metric *is itself a [[DSPyModules|`dspy.Module`]]*; it says *"your metric should probably be a smaller DSPy program"*. The tweet `metric` function is a plain Python function that *calls* `dspy.Predict(Assess)` — it is not a `dspy.Module` subclass. The framework treats both shapes as valid metrics. The [[DSPyOptimizers|Optimizers page]] (page 13) may sharpen this; the wiki should not over-commit on whether *the metric must be a `Module`* from this page alone — it must only be a **callable with the right signature**.
- **Receipt 1's `len <= 280` is a hard constraint, not an AI judgment.** A subtle but important commitment: not every component of a metric is LLM-graded. The page **mixes** AI-judgment with deterministic Python — *"`score = (correct + engaging) if correct and (len(tweet) <= 280) else 0`"* combines two LM-judged booleans with one deterministic boolean inside the same `score` computation. This is **the wiki's first explicit demonstration** that a DSPy metric is **not all-or-nothing AI-feedback**; it can — and the page implies *should* — combine LLM-as-judge with deterministic gates. The [[LLMModuloFramework|LLM-Modulo]] mapping is clean: the deterministic gate is a *sound critic*; the LM-judged dimensions are *soft critics*.
