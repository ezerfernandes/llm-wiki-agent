---
title: "DSPy Tutorial — GEPA for Facility Support Analyzer (Structured Information Extraction)"
type: source
tags: [dspy, tutorial, gepa, optimizer, classification, multi-module, structured-extraction, enterprise, chain-of-thought, reflection, feedback-function]
date: 2026-05-24
source_file: raw/dspy-tutorial-gepa-facility-support-analyzer.md
---

## Summary

Official [[DSPy]] tutorial at `https://dspy.ai/tutorials/gepa_facilitysupportanalyzer/` titled *"Tutorial: GEPA for Structured Information Extraction for Enterprise Tasks"*. **Second wiki-corpus end-to-end runnable receipt of [[GEPA|`dspy.GEPA`]]** after [[dspy-tutorial-gepa-aime]] — and the first that exercises GEPA on a **three-module compound system** with **per-predictor textual feedback** (vs the AIME tutorial's single-Signature `ChainOfThought`). Optimizes a three-`ChainOfThought` classifier (`FacilitySupportAnalyzerMM`) over the Meta-released [[FacilitySupportAnalyzer|Facility Support Analyzer]] dataset for three tasks simultaneously: urgency (`low`/`medium`/`high`), sentiment (`positive`/`neutral`/`negative`), and multi-label categories (10-way). **Headline lift: 75.4% → 87.0%** on the 68-item test set (51.30 → 59.17) — a clean **+11.6-point absolute** improvement at `auto="light"`. Uses **GPT-4.1 nano** as student (cheapest model in the GPT-4.1 family) reflected on by **GPT-5** — the canonical asymmetric-pair setting (strong reflector, cheap executor) from [[2507.19457-gepa|the GEPA paper]].

## Configuration receipt

| Slot | Value |
|---|---|
| Student LM | `openai/gpt-4.1-nano`, `temperature=1` |
| Reflection LM | `openai/gpt-5`, `temperature=1.0`, `max_tokens=32000` |
| Program | `FacilitySupportAnalyzerMM` — three sibling `dspy.ChainOfThought` predictors (`urgency_module`, `sentiment_module`, `categories_module`) called sequentially in `forward(message)` and fanned back into a single `dspy.Prediction(urgency=, sentiment=, categories=)` |
| Signatures | `FacilitySupportAnalyzerUrgency` (message → `Literal['low','medium','high']`), `FacilitySupportAnalyzerSentiment` (message → `Literal['positive','neutral','negative']`), `FacilitySupportAnalyzerCategories` (message → `List[Literal[...10 categories...]]`) |
| Dataset | `meta-llama/llama-prompt-ops/use-cases/facility-support-analyzer/dataset.json` — 200 ProCare facility-support emails with gold labels |
| Train / Val / Test | 66 / 66 / 68 (33%/33%/34% shuffled with `random.Random(0)`) |
| Eval metric | `metric(example, pred)` — average of three sub-scores (urgency exact match, sentiment exact match, per-category match/mismatch accuracy) |
| Optimizer metric | `metric_with_feedback` — same scalar score plus per-predictor textual feedback (`pred_name in {'urgency_module.predict', 'sentiment_module.predict', 'categories_module.predict'}`); returns `dspy.Prediction(score, feedback)` |
| Optimizer | `dspy.GEPA(metric=metric_with_feedback, auto="light", num_threads=32, track_stats=True, use_merge=False, reflection_lm=...)` |
| Eval shape | `dspy.Evaluate(devset=test_set, metric=metric, num_threads=32, display_table=True, display_progress=True)` |
| Optional tracking | [[MLflow]] autologging recommended (callout in tutorial intro) |

## Key Claims

- **Headline lift: 75.4% → 87.0%** on the 68-item test set (`EvaluationResult(score=87.01, results=<list of 68 results>)`). Tutorial closing line: *"GEPA was able to optimize GPT-4.1 nano's performance **from 75% score to 87%** in the auto='light' setting."*
- **First wiki-corpus GEPA receipt on a small/cheap student model** — [[GPT|GPT-4.1 nano]] (the cheapest tier of the GPT-4.1 family) vs the GPT-4.1 Mini in [[dspy-tutorial-gepa-aime]]. The tutorial frames this as the design point: *"We use GPT-4.1 nano to demonstrate how a small model can be tuned with GEPA."*
- **Asymmetric reflector → student gap is wider here than in the AIME tutorial**: GPT-5 reflecting on GPT-4.1 nano (vs GPT-5 reflecting on GPT-4.1 Mini). Same `reflection_lm=dspy.LM(model="gpt-5", temperature=1.0, max_tokens=32000)` config across both GEPA tutorials.
- **Multi-predictor textual feedback channel** is the load-bearing surface. `metric_with_feedback` branches on `pred_name` to return predictor-specific feedback strings (urgency: classification right/wrong + correct label; sentiment: same; categories: which labels were `correctly_included` / `incorrectly_included` / `incorrectly_excluded` / `correctly_excluded`). **First wiki receipt of [[FeedbackFunction|`pred_name`-routed feedback]]** — the AIME tutorial returned the same feedback string to all predictors (only one predictor existed).
- **Best validation candidate**: program 17, iteration 35, **valset aggregate score 0.8626** (≈86.3%). The tutorial ran **22 candidate programs** logged in the parent-DAG visualization (programs 0–21), with **program 17** marked as best (cyan in the printed Graphviz DAG) and **9 other programs on the per-instance Pareto front** (orange in the DAG: programs 4, 8, 9, 12, 13, 15, 19, 20, 21).
- **Pareto front coverage**: per-instance dominators include several programs with sub-best aggregate scores (e.g. program 19 at 0.74, program 21 at 0.77) — concrete receipt of GEPA's [[ParetoBasedCandidateSelection|specialist-retention behavior]] (programs kept because they uniquely solve some validation examples, even with lower aggregate).
- **Validation trajectory** (from `dspy.teleprompt.gepa.gepa` log): iter 1 → 0.72 (program 0), iter 3 → 0.72 (program 0 still best), iter 4 → **0.79** (program 2 new best), iter 5 → **0.86** (program 3 new best), iter 6 → **0.86 (program 4)** — **the 86% plateau is reached by iteration 6** out of ≈39 total iterations. Iter 35 → **0.8626 (program 17)** — the eventual best. Iterations 7–34 propose 13 new candidates but only program 17 beats the iter-6 plateau.
- **Three-way independent module mutation**: GEPA proposes new prompt text **one predictor at a time per iteration**, cycling through `urgency_module.predict` (iters 1, 4, 7, ...), `sentiment_module.predict` (iters 2, 5, 8, ...), `categories_module.predict` (iters 3, 6, 9, ...). **First wiki receipt of GEPA's per-predictor mutation discipline** on a multi-module program — the AIME tutorial only had one predictor so this rotation was invisible.
- **`use_merge=False` is set explicitly** — disables the optional [[SystemAwareMerge|System Aware Merge]] crossover (GEPA+Merge variant). **First wiki receipt of `use_merge` as a `dspy.GEPA(...)` kwarg.**

## Evolved instruction shape

The optimized predictors (best candidate, program 17) carry GEPA-evolved instructions in `optimized_program.{urgency_module,sentiment_module,categories_module}.predict.signature.instructions`. The tutorial prints all three via `for name, pred in optimized_program.named_predictors():`. Shape of each:

**Urgency module (urgency_module.predict)** — evolved from the one-line `"""Read the provided message and determine the urgency."""` baseline into a structured **decision framework** organized around:
1. **Safety / risk signals** — immediate physical hazards (gas leaks, water flooding, electrical shorts) → `high`; minor concerns → `low`/`medium`.
2. **Operational impact** — full outage of critical service → `high`; partial degradation → `medium`; cosmetic/routine → `low`.
3. **Time sensitivity** — explicit "ASAP" / "immediately" / hard deadline → `high`; "this week" / "soon" → `medium`; "when convenient" → `low`.
4. **Tone vs intent** — politeness markers ("please", "thank you") do **not** raise urgency; explicit urgency cues do.

**Sentiment module (sentiment_module.predict)** — evolved into a framework that:
- Distinguishes **explicit emotional language** ("disappointing", "exceptional service") from **polite formalities** ("hope you're well", "kind regards").
- Notes that **reporting a problem alone** does not entail negative sentiment — a calm, factual maintenance request is `neutral`.
- Establishes **tone dominance** when signals conflict: if a message thanks the team but escalates a complaint, weight the dominant tone.

**Categories module (categories_module.predict)** — evolved into a multi-label decision framework with:
- **Strict evidence requirement** — only assign a category when the message explicitly references it.
- **Scheduling vs complaint disambiguation** — a request to schedule cleaning is `cleaning_services_scheduling`; a complaint about prior cleaning is `customer_feedback_and_complaints` + the relevant cleaning category.
- **Specialized vs routine cleaning** — deep cleaning, carpet care, window washing → `specialized_cleaning_services`; standard recurring → `cleaning_services_scheduling` / `routine_maintenance_requests`.
- **Multi-label assignment** — assign **all** applicable categories from the fixed 10-label set, not just the most prominent one.

This is the **first wiki-corpus instance** of GEPA evolving **three sibling instructions in parallel** under a per-predictor feedback channel. The AIME tutorial's [[dspy-tutorial-gepa-aime|~120-line evolved playbook]] was for a single predictor; this tutorial's evolved instructions are shorter per-module but the **architectural receipt is the parallel decomposition** — GEPA does not try to write one mega-prompt; it writes three orthogonal decision frameworks, each conditioned on its own predictor's failure modes via the `pred_name`-routed `metric_with_feedback`.

## The feedback function — three sibling shapes

The tutorial's `metric_with_feedback` is the **canonical worked example** of [[FeedbackFunction|multi-predictor textual supervision]]. Three sub-functions:

```python
def feedback_urgency(gold_urgency, pred_urgency):
    score = 1.0 if gold_urgency == pred_urgency else 0.0
    if gold_urgency == pred_urgency:
        feedback = f"You correctly classified the urgency of the message as `{gold_urgency}`. ..."
    else:
        feedback = f"You incorrectly classified the urgency of the message as `{pred_urgency}`. The correct urgency is `{gold_urgency}`. Think about how you could have reasoned to get the correct urgency label."
    return feedback, score
```

`feedback_sentiment` mirrors this shape. `feedback_categories` is more elaborate — it computes the four label-set partitions (`correctly_included`, `incorrectly_included`, `incorrectly_excluded`, `correctly_excluded`) and constructs a multi-paragraph feedback string naming each set explicitly.

The tutorial's framing of why this works:

> *"Notice that the evaluation metric already contained all the information needed to generate the text feedback—we simply modified it to explicitly state what was being compared. In general, the metric functions for most tasks provide the essential components for creating such feedback; it often just requires identifying which elements to expose to the GEPA optimizer, enabling it to reflect on and enhance the program's performance."*

This is the **canonical pattern**: most existing scalar metrics already contain the structural information needed for feedback — GEPA's textual channel is a **re-projection** of the scalar comparison into prose, not new supervision.

## Key Quotes

> "In this tutorial, we'll explore a three-part task for structured information extraction and classification using the Facility Support Analyzer dataset released by Meta. Given an email or message sent in an enterprise setting related to facility maintenance or support requests, the goal is to extract its urgency, assess the sentiment, and identify all relevant service request categories."

> "We use GPT-4.1 nano to demonstrate how a small model can be tuned with GEPA."

> "GEPA is a *reflective* prompt optimizer. Its strength lies in its ability to examine textual feedback from the DSPy program's execution and evaluation pipelines. This gives GEPA greater insight into why the system achieved a particular score, enabling it to introspect and determine ways to enhance performance."

> "GEPA supports providing feedback at the individual predictor level (though this isn't required—see the GEPA PAPILLON tutorial for an example without it). Let's make a quick adjustment to our evaluation metric, to make it an optimization metric, that also provides text feedback!"

> "We will use a light budget for this tutorial. However, we typically recommend using `auto='heavy'` for optimized performance!"

> "Notice that the evaluation metric already contained all the information needed to generate the text feedback—we simply modified it to explicitly state what was being compared."

> "GEPA was able to optimize GPT-4.1 nano's performance **from 75% score to 87%** in the auto='light' setting."

## Cross-receipt convergence with the AIME tutorial

| | [[dspy-tutorial-gepa-aime|AIME tutorial]] | This tutorial |
|---|---|---|
| Task | Single-Signature math reasoning | Three-Signature classification |
| Student | GPT-4.1 Mini (temp=1, max_tokens=32000) | GPT-4.1 nano (temp=1) |
| Reflection LM | GPT-5 (temp=1.0, max_tokens=32000) | GPT-5 (temp=1.0, max_tokens=32000) |
| Predictors | 1 | 3 (parallel) |
| Train / Val / Test | 45 / 45 / 150 | 66 / 66 / 68 |
| `use_merge` | not set (default False) | explicitly `False` |
| `reflection_minibatch_size` | 3 | (default 3) |
| `auto` | `"light"` | `"light"` |
| Baseline | 46.7% | 75.4% |
| Optimized | 56.7% | 87.0% |
| Lift | +10 pts | +11.6 pts |
| Feedback channel | full step-by-step solution returned as `feedback_text` (single predictor) | per-predictor structured feedback routed by `pred_name` |
| Evolved artifact | one ~120-line structured playbook | three orthogonal decision frameworks |

**The two GEPA tutorials together establish the wiki's GEPA shape envelope** — same reflection LM, same optimizer settings, same `auto="light"` budget; varying student LM tier, program decomposition, feedback-function topology, and benchmark difficulty.

## Connections

### Canonical anchors
- [[GEPA]] — the optimizer concept page. **This tutorial supplies the wiki's first GEPA-on-classification receipt** to sibling [[dspy-tutorial-gepa-aime|GEPA-on-math]]. Updates the page with the **multi-predictor `pred_name`-routed feedback pattern** and the **`use_merge` kwarg disclosure**.
- [[2507.19457-gepa]] — the ICLR 2026 paper. The Facility Support Analyzer task is **not** one of the paper's six core benchmarks (HotpotQA / IFBench / HoVer / PUPA / AIME-2025 / LiveBench-Math); this tutorial extends GEPA's documented operating envelope to **enterprise structured-extraction classification** outside the paper's evaluation grid.
- [[FeedbackFunction]] — the $\mu_f$ supervision channel. **First wiki receipt of `pred_name`-routed multi-predictor feedback** — branching on `'urgency_module.predict'` vs `'sentiment_module.predict'` vs `'categories_module.predict'` to deliver predictor-specific failure analyses.
- [[ReflectivePromptMutation]] — the mutation operator. **First wiki receipt of the mutation rotating through three sibling predictors per iteration** (urgency on iter 1, sentiment on iter 2, categories on iter 3, repeat).
- [[ParetoBasedCandidateSelection]] — concrete Pareto-front receipt with 9 specialist programs (programs 4, 8, 9, 12, 13, 15, 19, 20, 21) retained alongside the aggregate-best program 17 in the printed DAG.

### Sibling DSPy tutorials
- [[dspy-tutorial-gepa-aime]] — the prior GEPA tutorial. Same optimizer settings; different benchmark, program decomposition, and feedback topology. Side-by-side comparison table above.
- [[dspy-tutorial-math]] — uses [[MIPROv2|`dspy.MIPROv2(auto="medium")`]] on a math-reasoning task with `ChainOfThought`. **First side-by-side comparable trio** in the wiki: MIPROv2-on-math (74→88.57), GEPA-on-math (46.7→56.7), GEPA-on-classification (75.4→87.0).
- [[dspy-email-extraction-tutorial]] — also a multi-Signature classification/extraction pipeline (4 Signatures), but **Programming-stage only** (no optimizer, no eval). This tutorial is the **Optimization-stage upgrade** of that pattern — same multi-Signature shape, plus GEPA tuning.
- [[dspy-optimizers]] — the *Learn* page-13 catalog. Adds the **first multi-module GEPA receipt** to the catalog's GEPA section and confirms `use_merge=False` as the default-equivalent disabling of [[SystemAwareMerge|GEPA+Merge]].
- [[dspy-optimization-overview]] — page 12, [[DSPyOptimization|the workflow page]]. Confirms the **GEPA exemption from the 20/80 train/val split**: the tutorial uses **33/33/34** = a roughly equal split, consistent with the carve-out (standard ML practice rather than the 20/80 inversion).

### Concept neighborhood
- [[chainofthought|`dspy.ChainOfThought`]] — the base module composed three times. **First wiki receipt of three sibling `ChainOfThought` predictors inside one `dspy.Module` being co-optimized by a single optimizer call.** Sibling to [[dspy-email-extraction-tutorial]] (4 `ChainOfThought` predictors, no optimizer) and [[dspy-llms-txt-generation-tutorial]] (4 `ChainOfThought` predictors, no optimizer).
- [[DSPyOptimizers]] — adds the `use_merge` kwarg disclosure and the multi-module GEPA pattern.
- [[DSPyMetrics]] — the metric contract. The `metric_with_feedback` function shows the canonical way to **upgrade a scalar evaluation metric into a textual-feedback optimization metric** by branching on the `pred_name` parameter.
- [[DSPyEvaluate]] — the `dspy.Evaluate(devset=test_set, metric=metric, num_threads=32, display_table=True, display_progress=True)` shape. **First wiki receipt of `display_table=True` showing a per-example results table after `evaluate(...)` returns**.
- [[DSPyPredict]] — `optimized_program.named_predictors()` and `pred.signature.instructions` are the inspection surfaces. **First wiki receipt of iterating `named_predictors()` to inspect post-optimization instructions across multiple sub-modules.**
- [[DSPyModules]] / [[DSPyProgrammingModel]] — the discipline of putting logic in a custom `dspy.Module` subclass with a `forward(message)` method that calls three sibling `dspy.ChainOfThought` predictors.
- [[DSPySignatures]] — three custom class-form Signatures with `Literal[...]` `OutputField` types (urgency: 3-way; sentiment: 3-way; categories: 10-way multi-label via `List[Literal[...]]`). **First wiki receipt of a `List[Literal[...]]` multi-label categorical OutputField being optimized by GEPA.**

### Application / domain
- [[FacilitySupportAnalyzer]] — the Meta-released dataset. **First wiki concept page.** 200 enterprise facility-support emails with gold urgency/sentiment/categories labels.
- [[meta|Meta]] — dataset publisher via the `llama-prompt-ops` repository.
- [[Classification]] — multi-task classification (3 independent classifiers). Updates the page with **first GEPA-on-classification receipt**.
- [[StructuredOutput]] — `Literal[...]` and `List[Literal[...]]` typed outputs are the framework's structured-output discipline.

### LMs invoked
- [[GPT|GPT-4.1 nano]] — the student. **First wiki receipt of the `openai/gpt-4.1-nano` model identifier** and the first time the **nano tier of the GPT-4.1 family** appears in a DSPy tutorial. Cheapest GPT-4.1 model.
- [[GPT|GPT-5]] — the reflection LM. Same configuration as [[dspy-tutorial-gepa-aime]] (`temperature=1.0`, `max_tokens=32000`).
- [[OpenAI]] — provider for both.

### External datasets and tooling
- `meta-llama/llama-prompt-ops/use-cases/facility-support-analyzer/dataset.json` — the dataset URL hardcoded in the tutorial.
- [[MLflow]] — recommended optional tracking layer (autologging callout in tutorial intro).
- [[Graphviz]] — tutorial's optional visualization tool for the candidate-DAG output (printed as DOT format, `online tool: https://is.gd/meuHtO`).

### Methodological receipts
- **The `detailed_results` attribute** (when `track_stats=True`): exposes `candidates`, `parents`, `val_aggregate_scores`, `val_subscores`, `per_val_instance_best_candidates`, `discovery_eval_counts`, `best_outputs_valset`, `best_idx`, `best_candidate`. **First wiki documentation of the `detailed_results` surface** — the AIME tutorial used it implicitly; this tutorial enumerates all eight fields and shows the parent-DAG construction via `from gepa.gepa_utils import find_dominator_programs`.
- **The `dag_to_dot(...)` visualization recipe** — manually-written DOT-format generator that color-codes the **best** candidate (cyan), **Pareto-front dominators** (orange), and **non-dominator** programs (default). **First wiki receipt of a GEPA optimization-trajectory visualization** beyond the per-iteration log lines.

## Contradictions

None with the prior corpus. The tutorial **extends** every prior GEPA receipt along orthogonal axes:

- [[GEPA]] page previously cited one tutorial ([[dspy-tutorial-gepa-aime]]); this is the **second runnable receipt** on a different task family (classification vs reasoning).
- [[FeedbackFunction]] page previously documented one feedback shape (full solution as feedback for one predictor); this introduces **predictor-routed feedback** (different feedback per `pred_name`).
- [[ReflectivePromptMutation]] page previously showed one evolved artifact (one ~120-line playbook); this shows **three sibling evolved artifacts** evolved in parallel.
- [[ParetoBasedCandidateSelection]] page previously had one Pareto-vs-aggregate receipt (iter 12 of AIME); this adds **nine specialist programs on a 22-candidate front**.
- [[DSPyOptimizers]] catalog previously did not document `use_merge`; this disclosure adds the first kwarg receipt.

## Scope-limit gaps

1. **No cost disclosure** — neither GPT-4.1 nano student tokens nor GPT-5 reflection tokens have a dollar number attached. Same convention break as [[dspy-tutorial-gepa-aime]].
2. **No `auto="medium"` or `auto="heavy"` comparison** — the tutorial only runs `light` despite explicitly recommending `heavy` for "optimized performance" in the inline callout.
3. **No reflection-LM ablation** — GPT-5 reflection on GPT-4.1 nano student is the only configuration shown. Whether a same-model reflector (GPT-4.1 nano reflecting on itself) would converge is not investigated.
4. **No save/load receipt** — `optimized_program.save(...)` is not invoked; the evolved three-predictor instructions exist only in-memory.
5. **No comparison against [[MIPROv2]] on the same task** — the dataset would be a natural MIPROv2 vs GEPA benchmark, but the tutorial does not run MIPROv2.
6. **No streaming / async / observability composition** — the four production-shape sibling tutorials are not invoked over the evolved program.
7. **No baseline-prompt printout** — the tutorial does not print the un-optimized `signature.instructions` (only the one-line docstrings on each Signature class) before showing the optimized version, so the *delta* must be inferred.
8. **`use_merge=True` ablation not run** — the [[SystemAwareMerge|GEPA+Merge]] variant is explicitly disabled, but no run shows whether merging would help on a three-predictor program.
9. **No discussion of why iter 6's 86% plateau persisted until iter 35** — programs 5–16 (twelve candidates spread across all three predictor mutation slots) failed to beat the iter-6 best until program 17 finally cleared by **0.0015 points** (0.8611 → 0.8626). The tutorial does not speculate on whether this reflects local-optimum stickiness or budget exhaustion.
