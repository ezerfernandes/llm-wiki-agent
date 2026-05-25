---
title: "DSPy Tutorial — GEPA for AIME (Math)"
type: source
tags: [dspy, tutorial, gepa, optimizer, aime, math, reasoning, chain-of-thought, reflection]
date: 2026-05-24
source_file: raw/dspy-tutorial-gepa-aime.md
---

## Summary

Official [[DSPy]] tutorial at `https://dspy.ai/tutorials/gepa_aime/` (notebook source: `docs/docs/tutorials/gepa_aime/index.ipynb`). **The wiki's first end-to-end runnable receipt of [[GEPA|`dspy.GEPA`]]** — the reflection-driven instruction optimizer introduced by [[2507.19457-gepa]]. Optimizes a single-Signature `dspy.ChainOfThought("problem -> answer")` program over [[AIME2025|AIME-2025]] math problems and reports a **clean +10-point lift (46.7% → 56.7% on 150 test items)** at the smallest budget setting (`auto="light"`, ≈560 metric calls, ≈6.22 full evals on train+val). Empirically replicates — at a lower budget — the [[2507.19457-gepa|GEPA paper's]] headline GPT-4.1 Mini × AIME-2025 result (paper: 45.33 → 59.33).

## Configuration receipt

| Slot | Value |
|---|---|
| Student LM | `openai/gpt-4.1-mini`, `temperature=1`, `max_tokens=32000` |
| Reflection LM | `openai/gpt-5`, `temperature=1.0`, `max_tokens=32000` |
| Program | `dspy.ChainOfThought(GenerateResponse)` — one Signature `problem: str -> answer: str`, instruction *"Solve the problem and provide the answer in the correct format."* |
| Train set | 45 problems (AIME 2022–2024, half of `AI-MO/aimo-validation-aime`) |
| Validation set | 45 problems (the other half) |
| Test set | 30 problems × 5 copies = **150** (AIME-2025 from `MathArena/aime_2025`, **deliberately oversampled 5×** for statistical stability) |
| Eval metric | Exact `int` match; `int(prediction.answer) == int(example.answer)`; parse failures score 0 |
| Optimizer metric | `metric_with_feedback` — returns `dspy.Prediction(score, feedback)` where `feedback` includes the **full step-by-step solution** from the training example when present (the [[FeedbackFunction|$\mu_f$ supervision channel]]) |
| Optimizer | `dspy.GEPA(metric=metric_with_feedback, auto="light", num_threads=32, track_stats=True, reflection_minibatch_size=3, reflection_lm=...)` |
| Threads | `num_threads=32` for both `dspy.Evaluate` and `GEPA` |
| Optional tracking | [[MLflow]] autologging via `mlflow.dspy.autolog(log_compiles=True, log_evals=True, log_traces=True)` |

## Key Claims

- **Headline lift: 46.7% → 56.7%** on the 150-item AIME-2025 ×5 test set (70 → 85 correct). The tutorial closes with the framing *"GEPA was able to optimize the GPT-4.1 Mini's performance on AIME 2025 from 46.6% score to 56.6%, a 10% improvement, with just a budget of `auto='light'`!"*
- **Budget disclosure (first wiki-corpus quantification of `auto="light"`)**: the GEPA runner prints *"Running GEPA for approx 560 metric calls of the program. This amounts to 6.22 full evals on the train+val set."* — i.e. **`light` ≈ 6 full evals worth of metric calls** on a 90-example train+val.
- **Validation trajectory**: base program iter 0 → 17/45 (37.8%). Iter 1 lifted to 19/45 (42.2%). Iter 5 — the **best validation candidate** — reached 24/45 (53.3%). Iters 2–4 + 6–21 each either skipped (perfect subsample) or failed to beat the iter-5 candidate. **22 iterations** total under the light budget.
- **Pareto-front coverage grew monotonically**: full valset pareto-front score 0.51 (iter 1) → 0.62 (iter 5) → **0.80 (iter 12, sustained through iter 21)**. The [[ParetoBasedCandidateSelection|per-instance Pareto front]] keeps a candidate program for each validation example it solves, even when no single program dominates aggregate.
- **Reflection LM is a strictly stronger model than the student**: GPT-5 reflects on GPT-4.1 Mini's traces. This is the **canonical asymmetric-pair GEPA setting** ([[2507.19457-gepa|paper]] §4.1) — the reflection LM is invoked rarely (`reflection_minibatch_size=3` per iteration) so the cost is dominated by the cheaper student.
- **Feedback-function content**: when a training example carries a `solution` field (AIME problems do — full multi-page contest solutions), the metric returns the entire solution as `feedback_text` along with *"Think about what takeaways you can learn from this solution to improve your future answers and approach to similar problems."* — concrete instance of the [[FeedbackFunction|domain-specific textual supervision channel]] [[2507.19457-gepa|the paper]] formalizes as $\mu_f$.

## Evolved instruction shape

GEPA selected program 2 (from iter 5) as the final optimized program. Its `predict.signature.instructions` grew from the **one-sentence baseline** *"Solve the problem and provide the answer in the correct format."* into a **structured ~120-line prompt** organized as:

1. **I/O contract** — two top-level fields `reasoning` and `answer`, answer must be a bare integer.
2. **General problem-solving guidance** — type identification (base/digits, palindromes, symmetric sums, intersecting families, AP avoidance), domain constraints, prefer structural arguments over enumeration, derive bounds with constructions for extremal questions.
3. **Six domain-specific strategy modules** — each a numbered playbook with worked identities:
   - Base-conversion / digit rearrangement (`mod 9`, `mod 8` pruning patterns).
   - Palindromes across bases (3-digit / 4-digit octal forms `65A + 8B` / `513A + 72B`).
   - Symmetric sums with `a+b+c` fixed (the `(a+b+c)(ab+bc+ca) − 3abc` identity + shift to isolate `(a−A)(b−A)(c−A)`).
   - Intersecting families of subsets (size-`>n/2` pigeonhole + complement-pair structure).
   - Avoiding 4-term arithmetic progressions with fixed anchors (e.g. *"3,4,5,a forbids a=6"*, divisibility-by-3 trick).
   - Order statistics with sum + absolute-sum constraints (positive-mass / negative-mass balance bounds).
4. **Quality-check checklist** — verify digit bounds, ordered vs unordered, complement exclusions, AP integrality.

This is the **concrete shape of an evolved [[ReflectivePromptMutation|reflective mutation]] artifact** the wiki had only described in the abstract — a structured "playbook" the reflection LM authored by reading per-example failures over 21 iterations and accumulating domain heuristics. The tutorial caption is the explicit characterization: *"GEPA is precomputing some reasoning to come up with a good plan for future task instances. Due to the improved performance in unseen validation set, we expect this prompt to generalize!"*

## Notable iteration mechanics

- Iters 2, 4, 6, 7, 8, 10, 13, 14, 16, 17, 19, 20, 21 — **"new subsample score not better, skipping"** or **"all subsample scores perfect, skipping"**. GEPA accepts a proposed mutation only if it beats the current best on the iteration's 3-example sub-batch.
- Iters 3, 9, 11, 12, 15, 18 — proposed new program text but failed to beat the iter-5 best at the full-valset evaluation.
- Iter 12 produced a candidate that **maxed the pareto-front to 0.80** but **aggregate valset score stayed 0.42** — concrete receipt of the [[ParetoBasedCandidateSelection|Pareto-vs-aggregate]] divergence the paper emphasizes (specialist programs that solve a subset of problems no other program does are kept on the front).

## Key Quotes

> "GEPA is a *reflective* prompt optimizer, and it's strength lies in being able to leverage additional sources of information, like the DSPy program's execution and evaluation pipelines, which provides GEPA more visibility into why the system got the score that it did, and then GEPA can introspect to identify how to improve the score. GEPA can also leverage additional supervision provided in this manner. For example, during optimization, we can return the correct solution's to the problems the program failed to solve."

> "We note that while such explicit supervision is not available in all scenarios, GEPA can work very flexibly with different forms of feedback (for example, using LLM-as-a-judge feedback shown in the PAPILLON tutorial, or just using answer labels, as shown in the facility-support tutorial)."

> "Running GEPA for approx 560 metric calls of the program. This amounts to 6.22 full evals on the train+val set."

> "Using 45 examples for tracking Pareto scores. You can consider using a smaller sample of the valset to allow GEPA to explore more diverse solutions within the same budget."

> "It can be seen that what GEPA is doing here, is precomputing some reasoning to come up with a good plan for future task instances. Due to the improved performance in unseen validation set, we expect this prompt to generalize!"

> "GEPA was able to optimize the GPT-4.1 Mini's performance on AIME 2025 **from 46.6% score to 56.6%**, a 10% improvement, with just a budget of `auto='light'`!"

## Cross-receipt convergence with the GEPA paper

| | [[2507.19457-gepa|GEPA paper Table 1]] | This tutorial |
|---|---|---|
| Student | GPT-4.1 Mini | GPT-4.1 Mini |
| Reflection LM | GPT-5 (Pro) | GPT-5 |
| Test set | AIME-2025 (30 problems, single eval) | AIME-2025 × 5 (150 evals) |
| Baseline | 45.33% | 46.7% |
| GEPA | 59.33% | 56.7% |
| Budget | paper budget (unspecified larger) | `auto="light"` ≈ 6 full evals |

The tutorial **qualitatively replicates** the paper's headline (10–14-point lift on GPT-4.1 Mini × AIME-2025) at a **smaller compute budget**. The +3-point gap between tutorial and paper is consistent with the light-vs-full budget delta and with single-eval vs 5× averaging.

## Connections

### Canonical anchors
- [[GEPA]] — the optimizer concept page. **This tutorial supplies the first wiki-corpus runnable trace** of the algorithm against a benchmark — the page previously cited the paper's aggregate results without an end-to-end runnable instance.
- [[2507.19457-gepa]] — the ICLR 2026 paper this tutorial operationalizes. AIME-2025 is one of the paper's six core benchmarks; GPT-4.1 Mini × AIME-2025 is the paper's most-cited single number.
- [[AIME2025]] — the benchmark concept page. Updated here with the **light-budget GPT-4.1 Mini receipt** (46.7 → 56.7) as a sibling to the paper's `full`-budget number (45.33 → 59.33).
- [[ReflectivePromptMutation]] — the mutation operator whose **concrete output** (~120-line structured playbook) this tutorial exhibits. Previously documented only in the abstract.
- [[FeedbackFunction]] — the $\mu_f$ supervision channel. The tutorial's `metric_with_feedback` is a textbook instance: returns `dspy.Prediction(score=int, feedback=<full step-by-step solution + framing>)`.
- [[ParetoBasedCandidateSelection]] — the selection operator. Iter-12 receipt (pareto front 0.80, aggregate 0.42) is a concrete divergence example.

### Sibling DSPy tutorials
- [[dspy-tutorial-math]] — sixth wiki-corpus DSPy tutorial; same shape (`dspy.ChainOfThought` + `MATH-algebra` + optimizer) but uses [[MIPROv2|`dspy.MIPROv2(auto="medium")`]] for **74.0 → 88.57** instead of GEPA. **First side-by-side comparable instance** of MIPROv2 vs GEPA on math-reasoning tasks in the wiki — MIPROv2 lifts more on the easier MATH-algebra subset; GEPA lifts on the much harder AIME contest set where MIPROv2's grounded-proposal stage has thinner signal.
- [[dspy-optimizer-tracking-tutorial]] — the MLflow side of the tracking surface this tutorial invokes via `mlflow.dspy.autolog(log_compiles=True, log_evals=True, log_traces=True)`.
- [[dspy-optimizers]] — the *Learn* page-13 catalog this tutorial materializes for GEPA. The page documents the **GEPA exemption from the 20/80 train/val split** ([[DSPyOptimization|page 12]]); the tutorial's 45/45 = 50/50 split is consistent with the exemption (standard ML practice).
- [[dspy-optimization-overview]] — page 12, which named GEPA as the **only carve-out** from the 20/80 inversion. This tutorial **demonstrates that the carve-out is operationally meaningful** — the 50/50 split with 45 examples per side is the actual recommended GEPA shape.

### Concept neighborhood
- [[chainofthought|`dspy.ChainOfThought`]] — the base module being optimized. **One-line baseline** (string instruction *"Solve the problem and provide the answer in the correct format."*) → **120-line structured playbook** is the cleanest receipt in the wiki of how much instruction-tuning headroom exists on a stock CoT module.
- [[DSPyOptimizers]] — the catalog. Adds the **first auto="light" budget number** (≈560 metric calls / 6.22 full evals) to the catalog's operating-envelope disclosures.
- [[DSPyOptimization]] — the three-stage workflow this tutorial walks end-to-end (Programming → Evaluation → Optimization, in that order).
- [[DSPyMetrics]] — the metric contract. This tutorial's `metric_with_feedback` is the **canonical worked example** of the textual-feedback-bearing variant.
- [[DSPyEvaluate]] / [[dspy-evaluation-overview]] — the `dspy.Evaluate(devset=..., metric=..., num_threads=32, display_table=True)` shape used for both baseline and post-optimization eval (47.6 → 56.7 against the 150-item test set).
- [[DSPyPredict]] — `optimized_program.predict.signature.instructions` is the field GEPA mutated. **First wiki receipt of inspecting an optimizer-evolved instruction directly via the `.predict.signature.instructions` attribute path.**
- [[DSPyProgrammingModel]] — the *"writing code, not strings"* discipline. The tutorial's one-line user code (`dspy.ChainOfThought("problem -> answer")`) is what GEPA evolved into a 120-line playbook — **the framework's own thesis on instruction synthesis**.

### Reasoning / math context
- [[ChainOfThought]] — the technique GEPA tuned. **First wiki-corpus instance** of a contest-math task running on chain-of-thought without external tools / search / verifier — GEPA's lift comes entirely from instruction structure.
- [[MATH-benchmark]] / [[GSM8K]] — sibling reasoning benchmarks. AIME problems are **harder** (AIME-2025 baseline ≈47%; MATH-algebra baseline ≈74% on the same `gpt-4o-mini` family) — explains why GEPA's relative gain on AIME (+10pt) is smaller than MIPROv2's on MATH (+14.6pt) despite GEPA being the stronger optimizer.
- [[AdversarialPromptSearch]] — GEPA's third application mode. Both this tutorial and [[2603.19247-prompt-optimization-jailbreaking]] use the same benign-vs-adversarial GEPA loop; the difference is the sign of the reward.

### LMs invoked
- [[GPT|GPT-4.1 Mini]] — the student. First wiki receipt of this model paired with GEPA.
- [[GPT|GPT-5]] — the reflection LM. First wiki receipt of GPT-5 in a DSPy tutorial.
- [[OpenAI]] — provider for both.

### External datasets
- `AI-MO/aimo-validation-aime` — HuggingFace dataset of AIME 2022–2024 problems (90 total), used here as 45/45 train/val split.
- [[MathArena]] / `MathArena/aime_2025` — the 30-problem AIME-2025 evaluation set, oversampled 5× to 150 for statistical stability.

## Contradictions

None with the prior corpus. The tutorial **extends and concretizes** every prior GEPA-related receipt:

- [[GEPA]] page previously cited paper's 45.33 → 59.33 result; this tutorial adds the light-budget 46.7 → 56.7 sibling receipt and the **first runnable trace**.
- [[AIME2025]] page previously cited paper Table 1 numbers only; this tutorial adds the light-budget GPT-4.1 Mini receipt.
- [[ReflectivePromptMutation]] page previously described the mutation operator abstractly; this tutorial supplies the **first concrete evolved-instruction artifact** (the 120-line playbook).
- [[ParetoBasedCandidateSelection]] page previously described the per-instance Pareto front abstractly; this tutorial supplies a **concrete divergence receipt** (iter 12: pareto 0.80 vs aggregate 0.42).
- [[DSPyOptimization]] / [[dspy-optimization-overview]] specified the **GEPA exemption from the 20/80 split**; this tutorial uses the carve-out's recommended 50/50 split and **shows it works** at the light budget.

The minor numeric gap with the paper (56.7 vs 59.33 final score) is **expected** given the lower compute budget and the 5× test-set oversampling; the qualitative claim (10%+ lift on GPT-4.1 Mini × AIME-2025) is preserved.

## Scope-limit gaps

1. **No cost disclosure** — neither the GPT-4.1 Mini student calls nor the (much more expensive) GPT-5 reflection calls have a dollar number attached. Prior MIPROv2 tutorials ([[dspy-rag-tutorial]], [[dspy-entity-extraction-tutorial]]) reported `~$1.50` and `~$0.26` respectively; this GEPA tutorial breaks that disclosure convention.
2. **No `auto="medium"` or `auto="heavy"` comparison** — the tutorial only runs `light`. The paper used a larger budget; how much of the 56.7 → 59.33 gap closes at heavier budgets is left as the user's exercise.
3. **No reflection-LM ablation** — GPT-5 reflection on GPT-4.1 Mini student is the only configuration shown. The paper ablates with same-model reflection (GPT-4.1 Mini reflecting on itself) and shows a ~5pt gap; the tutorial doesn't re-run.
4. **No save/load receipt** — `optimized_program.save(...)` is not invoked; the evolved 120-line playbook exists only in-memory for the tutorial's lifetime. Composing with [[DSPySaving]] / [[dspy-saving-tutorial]] is left implicit.
5. **No streaming / async / observability composition** — the four production-shape sibling tutorials ([[dspy-streaming-tutorial]] / [[dspy-async-tutorial]] / [[dspy-cache-tutorial]] / [[dspy-observability-tutorial]]) are not invoked over the evolved program.
6. **No prompt-evolution visualization** — the tutorial prints the *final* evolved instructions but does not show the **diff trajectory** across iterations. Reading the raw log (preserved in `raw/dspy-tutorial-gepa-aime.md`) is the only way to see the per-iteration mutation deltas.
7. **No comparison against [[MIPROv2]] on the same task** — the paper's headline claim is *"GEPA beats MIPROv2 by +12 on AIME-2025"*; the tutorial doesn't re-run that comparison.
8. **No discussion of why iter 5 was best** — the structured playbook from iter 5 stayed on the linear pareto front for the rest of the run; iters 7–21 proposed alternative playbooks (some richer, some with different domain coverage) that didn't aggregate-beat it. The tutorial doesn't speculate on whether this reflects budget exhaustion, local-optimum stickiness, or genuine convergence.
