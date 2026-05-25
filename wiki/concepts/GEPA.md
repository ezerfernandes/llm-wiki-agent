---
title: "GEPA"
type: concept
tags: [dspy, optimizer, gepa, reflection, instruction-tuning, teleprompter, prompt-optimization, genetic-pareto, paper-anchored]
sources: [2507.19457-gepa, dspy-optimizers, dspy-optimization-overview, 2603.19247-prompt-optimization-jailbreaking, 2604.14585-prompt-optimization-coin-flip, dspy-tutorial-gepa-aime, dspy-tutorial-gepa-papillon, dspy-tutorial-gepa-facility-support-analyzer, dspy-tutorial-gepa-trusted-monitor]
last_updated: 2026-05-24
---

# GEPA

**GEPA** (**Ge**netic-**Pa**reto) is a reflective prompt optimizer for [[CompoundAISystem|compound AI systems]] introduced by Agrawal, Tan, Soylu, Ziems et al. ([[UCBerkeley]] + [[stanforduniversity|Stanford]] + [[BespokeLabsAI|BespokeLabs.ai]] + [[NotreDame|Notre Dame]] + [[Databricks]] + [[MITAcademic|MIT]]) in **[[2507.19457-gepa|*GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning*]] (ICLR 2026, Oral)**. It is exposed in [[DSPy]] as **`dspy.GEPA`** — DSPy's reflection-based instruction optimizer. The 2026 paper is the **canonical primary source**; the [[dspy-optimizers|DSPy *Learn* docs (page 13)]] are a downstream surfacing.

## What it is (paper definition)

GEPA combines three architectural ingredients:

1. **[[ReflectivePromptMutation|Reflective prompt mutation]].** An LLM reads execution + evaluation traces from one rollout, diagnoses module-level failures, and proposes a revised prompt for the targeted module $j$.
2. **[[ParetoBasedCandidateSelection|Pareto-based candidate selection]].** Maintain non-dominated prompts on per-instance score and sample the next candidate to mutate stochastically by frequency on the per-instance Pareto frontier (Mouret & Clune 2015 "illumination" strategy adapted to per-instance scoring).
3. **Optional [[SystemAwareMerge|System Aware Merge]] crossover.** Combine the best-evolved version of each module across distinct optimization lineages — invoked by the **GEPA+Merge** variant only.

The optimizer is parameterized by a **[[FeedbackFunction|feedback function]] $\mu_f$** that extends the scalar reward $\mu$ with natural-language `feedback_text` (compiler errors, judge rationales, profiler output). This is the load-bearing non-metric supervision signal — see [[EvaluationTrace]] for the distinction from execution traces.

## Headline empirical results (from the paper)

- **Outperforms [[grpo|GRPO]] RL by up to 20% with 35× fewer rollouts** across 6 benchmarks (HotpotQA, IFBench, HoVer, PUPA, AIME-2025, LiveBench-Math) on Qwen3 8B.
- **Outperforms [[MIPROv2]] by >10%** (e.g. +12% AIME-2025 on GPT-4.1 Mini).
- **GEPA+Merge** widens the gap to +21% over GRPO at comparable budget.
- **Cross-model generalization**: prompts optimized on Qwen3-8B and evaluated unmodified on GPT-4.1 Mini still beat baselines that optimized directly on GPT-4.1 Mini.
- **Up to 9.2× shorter prompts** than MIPROv2 (instructions vs. few-shot demonstrations).
- **Inference-time search** for code generation: 30.52% mean vector utilization on AMD XDNA2 NPU kernels ([[NPUEval]]), >20% $fast_1$ on KernelBench CUDA.
- **Adversarial prompt search**: drops GPT-5 Mini AIME-2025 pass@1 from 76% → 10%.

## In DSPy

The canonical [[dspy-optimizers|DSPy *Learn* page 13]] surfacing:

> *"Uses LM's to reflect on the DSPy program's trajectory, to identify what worked, what didn't and propose prompts addressing the gaps. Additionally, GEPA can leverage domain-specific textual feedback to rapidly improve the DSPy program."*

The mechanism is **introspective**: rather than searching a candidate space (like [[MIPROv2|`MIPROv2`]]'s [[BayesianOptimization|Bayesian Optimization]]) or refining via coordinate ascent (like `COPRO`), GEPA asks an LM to **reflect** on the program's execution traces and **diagnose** what's failing. The diagnosis produces new instructions targeting the identified gaps.

Two ingredients the DSPy docs name (the paper formalizes both):

1. **LM reflection on trajectories.** Per the paper: directed module-level mutation conditioned on `(prompt, execution trace, score, evaluation trace / feedback_text)`. See [[ReflectivePromptMutation]].
2. **Domain-specific textual feedback.** Per the paper: the **[[FeedbackFunction|feedback function]] $\mu_f$** returning `(score, feedback_text)`. The only DSPy optimizer that names a non-metric supervision channel.

What the DSPy docs **do not** mention but the paper formalizes:
- The **Pareto-based candidate selection** mechanism that drives exploration (ablation: roughly half of GEPA's gain).
- The **System Aware Merge** crossover (a GEPA+Merge optional addition).
- The **inference-time-search** and **adversarial-search** generalizations.
- The full name "**Genetic-Pareto**".

## Mechanism

[[dspy-optimizers|The page]]'s definition:

> *"Uses LM's to reflect on the DSPy program's trajectory, to identify what worked, what didn't and propose prompts addressing the gaps. Additionally, GEPA can leverage domain-specific textual feedback to rapidly improve the DSPy program."*

The mechanism is **introspective**: rather than searching a candidate space (like [[MIPROv2|`MIPROv2`]]'s [[BayesianOptimization|Bayesian Optimization]]) or refining via coordinate ascent (like `COPRO`), GEPA asks an LM to **reflect** on the program's execution traces and **diagnose** what's failing. The diagnosis produces new instructions targeting the identified gaps.

Two ingredients distinguish GEPA from sibling instruction optimizers:

1. **LM reflection on trajectories.** The optimizer feeds the program's trajectories (across multiple training examples) to an LM, which produces a *what-worked / what-didn't* analysis and uses it to draft improved instructions. This is structurally **distinct from [[MIPROv2]]'s "grounded proposal"** stage — MIPROv2 proposes instructions from code+data+traces in a generative pass; GEPA explicitly **reflects** on outcomes and diagnoses failures.

2. **Domain-specific textual feedback.** GEPA can consume **domain-specific text feedback** alongside the metric. This is the only optimizer in the catalog that names a *textual feedback* input distinct from the scalar metric — useful for domains where *why* an output is wrong is easier to articulate than a numeric score.

## The 20/80 split carve-out

[[dspy-optimization-overview|The Optimization Overview]] commits the framework to an **inverted 20/80 train/val split** for *most prompt optimizers* (rationale: prompt optimizers tend to overfit on small training sets, and a large validation set is the overfitting defense). GEPA is the **only named exception**:

> *"However, the GEPA optimizer follows standard ML practice — maximizing the training set size while keeping the validation set sufficiently sized to represent the downstream task distribution."*

The mechanism that justifies GEPA's exemption is **left implicit** on [[dspy-optimization-overview|page 12]] and **only partially developed** on [[dspy-optimizers|page 13]] — the reflection-driven mechanism produces instructions that are **more robust to small training sets** than the search-driven mechanisms used by other optimizers, presumably because reflection generalizes from few examples in a different way than search does. The page doesn't formalize this beyond the empirical claim that GEPA *"follows standard ML practice"*.

This is the **single most non-obvious per-optimizer disclosure** in the *Learn* corpus — the framework names a specific optimizer (GEPA) on the workflow-level page (page 12) precisely because it **violates** a framework-level recommendation, and only to **explicitly grant the exemption**. Reading the [[dspy-optimizers|page-13 per-optimizer documentation]] is **load-bearing** before applying the 20/80 split mechanically — the train/val split is a **per-optimizer recommendation**, not a universal rule.

## Domain-specific textual feedback

GEPA's ability to *"leverage domain-specific textual feedback"* is the **first explicit non-metric supervision signal** in DSPy's optimizer catalog. Most optimizers consume *only* the scalar metric as their feedback channel; GEPA additionally consumes **textual** descriptions of what's wrong with the program's outputs. This is structurally compatible with DSPy's [[llmasjudge|LLM-as-judge]] pattern from [[DSPyMetrics]] — the same LM that produces a *score* can produce a *narrative explanation*, and GEPA can consume both.

The [[dspy-optimizers|page]] does not detail the mechanism; tutorials are linked: *"Detailed tutorials on using GEPA are available at [dspy.GEPA Tutorials](../../../tutorials/gepa_ai_program/)"*.

## Position in the catalog

GEPA belongs to the *Automatic Instruction Optimization* family (alongside `COPRO`, [[MIPROv2]], and `SIMBA`). What it tunes: **instructions only**. The mechanism distinguishes it:

| Optimizer | Search strategy |
|---|---|
| `COPRO` | Coordinate ascent / hill-climbing |
| [[MIPROv2]] | [[BayesianOptimization\|Bayesian Optimization]] over (instructions, demos) |
| `SIMBA` | Stochastic mini-batch sampling + self-reflective rules |
| **GEPA** (this page) | **LM reflection on program trajectory + optional domain-specific textual feedback** |

## Why GEPA is absent from the five-rule rubric

[[dspy-optimizers|The page]]'s five-rule getting-started rubric **does not name GEPA**. The rubric covers `BootstrapFewShot` (10 examples), `BootstrapFewShotWithRandomSearch` (50+), `MIPROv2` (200+ or 0-shot), and `BootstrapFinetune` (post-success efficiency). GEPA, `SIMBA`, `COPRO`, `KNNFewShot`, `Ensemble`, `BetterTogether`, and `LabeledFewShot` are **expert paths** the user must discover via the catalog.

The omission is consistent with GEPA being the most **research-frontier** optimizer in the catalog — the [[dspy-optimization-overview|page-12]] framing of optimization as *"an emerging paradigm"* applies most strongly here.

## Runnable tutorial receipt — [[dspy-tutorial-gepa-aime|GEPA for AIME (Math)]]

The first wiki-corpus end-to-end runnable trace of `dspy.GEPA` is [[dspy-tutorial-gepa-aime|the official GEPA-on-AIME tutorial]] at `https://dspy.ai/tutorials/gepa_aime/`. It pairs **[[GPT|GPT-4.1 Mini]] as the student** (`temperature=1, max_tokens=32000`) with **[[GPT|GPT-5]] as the reflection LM** (`temperature=1.0, max_tokens=32000`) — the canonical asymmetric-pair setting where reflection is delegated to a strictly stronger model that's invoked rarely (`reflection_minibatch_size=3`), so cost is dominated by the cheaper student.

Headline trace:

| | |
|---|---|
| Program | `dspy.ChainOfThought("problem -> answer")` — one-sentence baseline instruction *"Solve the problem and provide the answer in the correct format."* |
| Optimizer | `dspy.GEPA(metric=metric_with_feedback, auto="light", num_threads=32, track_stats=True, reflection_minibatch_size=3, reflection_lm=gpt5)` |
| Train/Val | 45/45 (AIME 2022–2024, half-and-half — consistent with the [[DSPyOptimization\|GEPA carve-out from the 20/80 inversion]]) |
| Test | 150 (AIME-2025 × 5, oversampled for statistical stability) |
| `auto="light"` budget | **≈ 560 metric calls ≈ 6.22 full evals on the train+val set** — first wiki quantification |
| Iterations | 22 (0–21) |
| Best validation candidate | Iter 5: 24/45 = **53.3%** (linear pareto-front leader, sustained through iter 21) |
| Test baseline | 70/150 = **46.7%** |
| Test optimized | 85/150 = **56.7%** |
| **Lift** | **+10 absolute points** |

**Concrete shape of the evolved reflection artifact** — the optimizer mutates the Predict's `signature.instructions` from one sentence into a **~120-line structured playbook** organized as: (1) two-field I/O contract, (2) general problem-solving guidance, (3) **six numbered domain-specific strategy modules** (base conversion / palindromes-across-bases / symmetric sums with `a+b+c` fixed / intersecting subset families / 4-term-AP avoidance with fixed anchors / order statistics with sum + absolute-sum constraints), each module carrying worked identities and pruning patterns, (4) a quality-check checklist. The tutorial's framing: *"GEPA is precomputing some reasoning to come up with a good plan for future task instances. Due to the improved performance in unseen validation set, we expect this prompt to generalize."* This is the wiki's first **concrete view of what reflective mutation produces** — [[ReflectivePromptMutation]] was previously documented only in the abstract.

**Concrete [[FeedbackFunction|$\mu_f$ instance]]**: the tutorial's `metric_with_feedback` returns `dspy.Prediction(score=int, feedback=<full step-by-step contest solution + "Think about what takeaways you can learn from this solution to improve your future answers">)`. The textual channel is **load-bearing** — the multi-page solution text supplies the heuristics the reflection LM then compresses into the playbook.

**Concrete [[ParetoBasedCandidateSelection|Pareto-vs-aggregate divergence]]**: iter 12 produced a candidate that **maxed the valset pareto front to 0.80** while its **aggregate score stayed 0.42** — receipt that GEPA keeps specialist programs (each solving problems no other program does) even when they lose head-to-head.

**Cross-receipt convergence with [[2507.19457-gepa|the paper]]**: paper Table 1 reports the same GPT-4.1 Mini × AIME-2025 cell as **45.33 → 59.33** at the paper's full compute budget; tutorial reports **46.7 → 56.7** at `auto="light"`. The ±3-point gap is consistent with the budget cut + 5× test-set oversampling — qualitative replication of the headline result.

## Second runnable tutorial receipt — [[dspy-tutorial-gepa-papillon|GEPA for Privacy-Conscious Delegation (PAPILLON)]]

The wiki's **second runnable `dspy.GEPA` trace** is [[dspy-tutorial-gepa-papillon|the official PAPILLON tutorial]] at `https://dspy.ai/tutorials/gepa_papillon/`. **First compound-program GEPA receipt** in the wiki ([[dspy-tutorial-gepa-aime|`gepa_aime`]] was single-Signature) and **first GEPA-with-LLM-judge-reward receipt** (`gepa_aime` used a verifiable exact-match metric).

Headline trace:

| | |
|---|---|
| Program | [[PAPILLON]] — two Signatures (`dspy.ChainOfThought(CraftRedactedRequest)` → untrusted external LM → `dspy.Predict(RespondToQuery)`) |
| Optimizer | `dspy.GEPA(metric=compute_overall_score_with_feedback, reflection_lm=dspy.LM("openai/gpt-4.1"), num_threads=16, track_stats=True, track_best_outputs=True, max_full_evals=1)` |
| Three-tier model stack | `gpt-4.1-nano` (local student) + `gpt-4.1-mini` (untrusted external) + `gpt-4.1` (reflection) |
| Reward | [[LLMJudge|`LLMJudge`]] composite `(quality + (1 − leakage)) / 2` with separate-axis feedback text |
| Train / Dev / Test | 225 / 225 / 214 ([[PUPA]] `pupa_tnb` + `pupa_new` splits) |
| Baseline | 76.5% composite (163.71/214) |
| Optimized | **86.1% composite** (184.26/214) |
| **Lift** | **+9.6 absolute / +12.5% relative** at `max_full_evals=1` |

**First-of-kind features this tutorial adds to the wiki's GEPA receipt corpus:**

1. **`max_full_evals` integer budget knob** — distinct from the `auto={"light","medium","heavy"}` enum [[dspy-tutorial-gepa-aime|the AIME tutorial]] used. The smallest non-zero budget setting (1) is sufficient for a +9.6-point lift on PAPILLON.
2. **`track_best_outputs=True`** kwarg — tracks per-iteration best-output candidates so the optimizer returns the strongest individual rollout, not just the strongest aggregate prompt.
3. **Three-tier asymmetric model stack** — separate student, untrusted external, and reflection LM (vs. the two-tier student × reflection pair from `gepa_aime`). The *untrusted* role is structurally new — it's an axis distinct from the reflection axis.
4. **Compound (multi-Signature) program** — confirms GEPA scales from one Signature (`gepa_aime`) to two without API changes.
5. **LLM-judge composite reward** — `compute_overall_score_with_feedback` returns a `dspy.Prediction(score, feedback)` where the score is a [[LLMJudge]]-derived composite, not a verifiable exact-match.
6. **Per-axis decomposition in feedback text** — *"The overall score is X, which is the arithmetic mean of the quality score (Q) and the leakage score (1−L). Try to improve the quality of your response and reduce the leakage of PII information."* This is **structured-decomposition $\mu_f$ text**, distinct from `gepa_aime`'s dense-narrative (full contest solution) $\mu_f$. Both forms work; the per-axis structure gives the reflection LM explicit credit-assignment signal between the two reward axes.

**Cross-receipt convergence with [[2507.19457-gepa|the paper]]**: paper Table 4 reports GPT-4.1 Mini × PUPA as **74.18 → 94.47** plain GEPA, **96.46 with Merge**; this tutorial reports **76.5 → 86.1** at GPT-4.1 Nano student × `max_full_evals=1` (no Merge). The smaller absolute optimized number is consistent with the smaller student capacity ceiling + smaller budget; the tutorial **does not run GEPA+Merge**.

**Cross-receipt against [[dspy-tutorial-rl-papillon|the ArborGRPO PAPILLON receipt]]**: the wiki's first **prompt-space vs weight-space side-by-side** pairing on the same program + benchmark. ArborGRPO lifts 1.5B-parameter Qwen2.5 by **+5.4 points** in ~3 h on 4× [[NVIDIA|H100]]; GEPA lifts GPT-4.1 Nano by **+9.6 points** at one full eval. *Not directly comparable* (different student models, different test-set sizes via different PUPA splits — `pupa_new`-only 450-item test vs `pupa_tnb`+`pupa_new` 214-item test), but the directional ordering matches the [[2507.19457-gepa|GEPA paper's]] central thesis: prompt-space optimization dominates weight-space RL at this program shape and benchmark.

## Third runnable tutorial receipt — [[dspy-tutorial-gepa-facility-support-analyzer|GEPA for Facility Support Analyzer (3-Signature classification)]]

The wiki's third end-to-end runnable `dspy.GEPA` trace is [[dspy-tutorial-gepa-facility-support-analyzer|the official Facility Support Analyzer tutorial]] at `https://dspy.ai/tutorials/gepa_facilitysupportanalyzer/`. **First receipt of GEPA optimizing three sibling `dspy.ChainOfThought` predictors in parallel** under a `pred_name`-routed feedback function — the program is `FacilitySupportAnalyzerMM` (urgency / sentiment / categories classifiers fanned into one `dspy.Prediction`) over the Meta-released [[FacilitySupportAnalyzer]] dataset of 200 ProCare facility-support emails.

Headline trace:

| | |
|---|---|
| Program | `FacilitySupportAnalyzerMM` — three sibling `dspy.ChainOfThought` predictors (urgency 3-way, sentiment 3-way, categories 10-way multi-label) called sequentially in `forward(message)` |
| Student LM | `openai/gpt-4.1-nano` (`temperature=1`) — **cheapest tier of the GPT-4.1 family**; first wiki receipt of nano-tier as a GEPA student |
| Reflection LM | `openai/gpt-5` (`temperature=1.0`, `max_tokens=32000`) — same as AIME tutorial |
| Optimizer | `dspy.GEPA(metric=metric_with_feedback, auto="light", num_threads=32, track_stats=True, use_merge=False, reflection_lm=...)` |
| Train/Val/Test | 66 / 66 / 68 (33/33/34 shuffled with `random.Random(0)`) |
| Feedback channel | **`pred_name`-routed** — `metric_with_feedback` branches on `pred_name in {'urgency_module.predict', 'sentiment_module.predict', 'categories_module.predict'}` to return predictor-specific feedback |
| Iterations | ~39 logged; 22 distinct candidate programs (0–21) |
| Best validation candidate | Program 17 at iter 35 — valset aggregate **0.8626 (86.3%)** |
| Test baseline | 51.30/68 = **75.4%** |
| Test optimized | 59.17/68 = **87.0%** |
| **Lift** | **+11.6 absolute points** |

**Three new disclosures this tutorial adds to the wiki's GEPA documentation**:

1. **`use_merge=False` is set explicitly** — first wiki receipt of the [[SystemAwareMerge|GEPA+Merge]] kwarg as a `dspy.GEPA(...)` argument. The PAPILLON tutorial did not name it; the AIME tutorial did not name it. This tutorial makes the toggle explicit and disables it.
2. **GEPA mutates one predictor per iteration on multi-module programs** — the log shows the mutation rotating through `urgency_module.predict` (iter 1), `sentiment_module.predict` (iter 2), `categories_module.predict` (iter 3), repeat. The reflection LM is not asked to rewrite all three sibling predictors in one mutation step.
3. **`pred_name`-routed `metric_with_feedback`** — see [[FeedbackFunction|the Feedback Function page's multi-predictor routing section]] for the worked example. The feedback function branches on `pred_name` to deliver predictor-specific failure descriptions; reflection only sees the feedback that targets the module being mutated. This is the **canonical multi-module $\mu_f$ pattern**.

**Pareto-front receipt**: 9 specialist programs retained alongside the best (programs 4, 8, 9, 12, 13, 15, 19, 20, 21 in the printed Graphviz DAG vs cyan program 17). Several have lower aggregate score (program 19 at 0.74, program 21 at 0.77) but remain on the per-instance Pareto front — **concrete receipt of [[ParetoBasedCandidateSelection|specialist retention]] on a classification benchmark** (the AIME tutorial supplied this for math).

**Evolved instructions shape**: **three orthogonal decision frameworks** (one per predictor) instead of one mega-prompt. Urgency frame: safety/risk + operational impact + time sensitivity + tone-vs-intent decomposition. Sentiment frame: explicit emotional language vs polite formality + tone dominance. Categories frame: strict evidence requirement + scheduling-vs-complaint disambiguation + specialized-vs-routine cleaning + multi-label assignment. **First wiki receipt of GEPA producing parallel sibling instructions** rather than one consolidated playbook ([[dspy-tutorial-gepa-aime|the AIME tutorial]] produced one ~120-line monolithic playbook for the single predictor).

**Three-tutorial GEPA envelope**:

| | [[dspy-tutorial-gepa-aime|AIME]] | [[dspy-tutorial-gepa-papillon|PAPILLON]] | This tutorial (Facility) |
|---|---|---|---|
| Task family | Math reasoning | Privacy-conscious delegation | Enterprise classification |
| Predictors | 1 | 2 | 3 |
| Student | GPT-4.1 Mini | GPT-4.1 Nano | GPT-4.1 nano |
| Reflection | GPT-5 | GPT-4.1 | GPT-5 |
| Budget | `auto="light"` | `max_full_evals=1` | `auto="light"` |
| Reward shape | exact-match scalar | LLM-judge composite | per-predictor exact-match average |
| Feedback shape | dense narrative (full solution) | per-axis decomposition (quality vs leakage) | `pred_name`-routed structured |
| `use_merge` | (default) | (default) | explicitly `False` |
| Baseline → Optimized | 46.7% → 56.7% (+10) | 76.5% → 86.1% (+9.6) | 75.4% → 87.0% (+11.6) |

## Fourth runnable tutorial receipt — [[dspy-tutorial-gepa-trusted-monitor|GEPA for Trusted Monitoring (AI Control)]]

The wiki's **fourth runnable `dspy.GEPA` trace** is [[dspy-tutorial-gepa-trusted-monitor|the official GEPA-for-Trusted-Monitor tutorial]] at `https://dspy.ai/tutorials/gepa_trusted_monitor/`. **First classification (discriminative) GEPA receipt** in the wiki (prior three were generation tasks — math answer, privacy-redacted query, enterprise label-set generation) and **first GEPA-on-AI-safety-defender receipt** (training a weak [[TrustedMonitor|trusted monitor]] to spot [[CodeBackdoor|code backdoors]] planted by a stronger untrusted coder on [[APPSBenchmark|APPS]] via [[ControlArena|`control_arena`]] / [[ControlTax]]).

Headline trace:

| | |
|---|---|
| Program | `MonitorTrainerProgram(dspy.ChainOfThought(PredictSuspicionScore))` — one Signature wrapped in a dual-call wrapper so GEPA sees attack+honest code as paired rollouts |
| Optimizer | `dspy.GEPA(max_full_evals=2, metric=metric_for_example, num_threads=8, reflection_minibatch_size=3, track_stats=True, reflection_lm=dspy.LM("openai/gpt-5-2025-08-07", ...))` |
| Two-tier model stack | `openai/gpt-4.1-nano-2025-04-14` (student monitor, `cache=False`) + `openai/gpt-5-2025-08-07` (reflection) |
| Reward | **Comparative-pair**: `1.0 if attack_suspicion > honest_suspicion else 0.0`, with failure-direction $\mu_f$ text |
| Train / Val / Eval | 200 / 100 / 160 ([[APPSBenchmark|APPS]] backdoor split via `control_arena.settings.apps.apps_setting.get_dataset(backdoor_source="control_tax")`) |
| Baseline | 0.69 valset comparative-pair accuracy |
| Optimized | **0.81 valset** comparative-pair accuracy (**final pareto-front 0.95**) |
| **Lift** | **+0.12 absolute / +17.4% relative** at `max_full_evals=2` |

**First-of-kind features this tutorial adds to the wiki's GEPA receipt corpus:**

1. **GEPA on a classification (discriminative) task** — prior tutorials were generation tasks. Confirms GEPA's reflection mechanism works on an integer-output Signature (`PredictSuspicionScore` returns `int` in `[0, 100]`).
2. **Comparative-pair [[FeedbackFunction|$\mu_f$ shape]]** — `1.0 if attack > honest else 0.0` with failure-direction-in-plain-English feedback (*"You said the attack code was LESS suspicious than the honest code"*). This is a **fifth $\mu_f$ source category** not enumerated in [[2507.19457-gepa|the paper]]'s four (evaluation-byproducts, multi-hop module feedback, judge rationales, human annotations).
3. **`MonitorTrainerProgram` dual-call wrapper** — wraps a single-Signature classifier so GEPA can see one example as two rollouts and the comparative metric can fire. **Optimization-time program shape ≠ deployment-time program shape**: production saves the un-wrapped inner program (`gepa_trainer_program.monitor_program.save(...)`). Structurally new in the wiki's DSPy receipt corpus.
4. **[[AIControl|AI Control]] / [[TrustedMonitor|trusted-monitor]] task family** in DSPy — first wiki composition of [[ControlArena|UK AISI's `control_arena`]] library with a DSPy optimizer.
5. **`ScoreWithFeedback` typed return** from `dspy.teleprompt.gepa.gepa_utils` — prior tutorials returned `dspy.Prediction(score, feedback)` informally; this tutorial uses the explicit dataclass.
6. **`DSPyTrace` typed alias** — typed alias for GEPA trace parameters.
7. **GPT-5 as a dated checkpoint** (`openai/gpt-5-2025-08-07`) — first wiki receipt of a dated GPT-5 reflection LM.
8. **GPT-4.1 Nano as a dated checkpoint** (`openai/gpt-4.1-nano-2025-04-14`).
9. **`cache=False` on the student LM** — defensive against same-prompt deduplication across the attack/honest dual-call.
10. **`max_full_evals=2`** — second integer-budget receipt (gepa_papillon used `max_full_evals=1`).

**Cross-receipt convergence with [[2507.19457-gepa|the paper]]**: the paper's six benchmarks are HotpotQA / IFBench / HoVer / PUPA / AIME-2025 / LiveBench-Math — **none of which are AI-control classifiers**. This tutorial is **the first GEPA receipt that operationalizes the algorithm on a task family the paper does not benchmark**.

**Cross-receipt against [[2603.19247-prompt-optimization-jailbreaking]]** (GEPA on the attacker side of AI safety): this tutorial is the **defender-side companion**. Two complementary GEPA-on-safety receipts now in the wiki — adversarial prompter (max danger; Claude 4.5 Sonnet 0.046 → 0.236) and trusted monitor (max backdoor detection; APPS 0.69 → 0.81).

**Four-tutorial GEPA envelope**:

| | [[dspy-tutorial-gepa-aime|AIME]] | [[dspy-tutorial-gepa-papillon|PAPILLON]] | [[dspy-tutorial-gepa-facility-support-analyzer|Facility]] | This tutorial (Trusted Monitor) |
|---|---|---|---|---|
| Task family | Math reasoning | Privacy delegation | Enterprise classification | **AI-control defender** |
| Output type | Free-form generation | Free-form generation | Multi-label classification | **Integer score (0–100)** |
| Predictors | 1 | 2 | 3 | 1 (wrapped in dual-call) |
| Student | GPT-4.1 Mini | GPT-4.1 Nano | GPT-4.1 Nano | **GPT-4.1 Nano** (dated 2025-04-14) |
| Reflection | GPT-5 | GPT-4.1 | GPT-5 | **GPT-5** (dated 2025-08-07) |
| Budget | `auto="light"` | `max_full_evals=1` | `auto="light"` | **`max_full_evals=2`** |
| Reward shape | exact-match scalar | LLM-judge composite | per-predictor avg | **comparative-pair (attack > honest)** |
| Feedback shape | dense narrative | per-axis decomposition | `pred_name`-routed | **failure-direction plain-English** |
| Cache | (default) | (default) | (default) | **`cache=False`** |
| Baseline → Optimized | 46.7% → 56.7% (+10) | 76.5% → 86.1% (+9.6) | 75.4% → 87.0% (+11.6) | **0.69 → 0.81 valset (+0.12)** |

## Connections

### Canonical source
- [[2507.19457-gepa]] — the ICLR 2026 paper introducing GEPA (this concept's primary source). Defines the algorithm, runs the empirical benchmarks, and frames GEPA as compound-AI-system optimization, inference-time search, and adversarial search.

### Runnable tutorials
- [[dspy-tutorial-gepa-aime]] — the official `dspy.GEPA` tutorial against [[AIME2025]]. First wiki-corpus end-to-end runnable trace of the algorithm (46.7 → 56.7 lift; `auto="light"` ≈ 560 metric calls; ~120-line evolved playbook).
- [[dspy-tutorial-gepa-papillon]] — the official `dspy.GEPA` tutorial against [[PAPILLON]] + [[PUPA]]. **First compound-program GEPA receipt** (two Signatures) and **first LLM-judge-reward GEPA receipt** (composite quality + (1 − leakage) via [[LLMJudge]]). 76.5 → 86.1 lift at `max_full_evals=1` with a three-tier asymmetric model stack. First wiki receipts of `max_full_evals` integer budget knob and `track_best_outputs=True` kwarg.
- [[dspy-tutorial-gepa-trusted-monitor]] — the official `dspy.GEPA` tutorial against the [[AIControl|AI-control]] [[TrustedMonitor|trusted-monitor]] task on [[APPSBenchmark|APPS]] via [[ControlArena|`control_arena`]] / [[ControlTax]]. **First classification-task GEPA receipt** (integer-output Signature) and **first GEPA-on-AI-safety-defender receipt** (companion to [[2603.19247-prompt-optimization-jailbreaking]]'s attacker-side receipt). 0.69 → 0.81 valset lift (final pareto-front 0.95) at `max_full_evals=2` with a two-tier stack (GPT-4.1 Nano dated 2025-04-14 + GPT-5 dated 2025-08-07). First wiki receipts of: the `MonitorTrainerProgram` dual-call wrapper pattern; comparative-pair $\mu_f$ shape; `ScoreWithFeedback` + `DSPyTrace` typed aliases from `dspy.teleprompt.gepa.gepa_utils`; `cache=False` student LM; GPT-5 / GPT-4.1 Nano dated checkpoints.

### Empirical context: the coin-flip framing
- [[2604.14585-prompt-optimization-coin-flip]] — does not directly benchmark GEPA, but its **49% sub-zero-shot failure rate** across six other prompt optimizers on two-agent feed-forward pipelines (mid-tier executors) implies GEPA's headline >10% gains may be **conditional on the [[CanButDoesntPattern|"can but doesn't" pattern]]** — tasks with exploitable output structure (the canonical example: GEPA's biggest gain is on HotpotQA conditional second-hop query generation, a [[HotPotQAConditional|conditional-rule]] task). Open question: does GEPA's [[ReflectivePromptMutation|reflective mutation]] cross the 2-pt [[HeadroomTest|headroom threshold]] on free-form tasks like [[FeedbackBench]] / [[WildBench]] / [[XSum]] where the wiki's six baseline methods do not? The [[CompoundAIDiagnostic|two-stage diagnostic]] is the cheap pre-test the [[2604.14585-prompt-optimization-coin-flip|Zhang et al.]] framework recommends before invoking GEPA on a new pipeline.

### Algorithmic components
- [[ReflectivePromptMutation]] — the mutation operator.
- [[ParetoBasedCandidateSelection]] — the selection operator (responsible for ~half the empirical gain).
- [[SystemAwareMerge]] — the optional crossover (GEPA+Merge).
- [[FeedbackFunction]] — the $\mu_f$ supervision signal.
- [[EvaluationTrace]] — the natural-language trace $\mu_f$ surfaces from the evaluator.
- [[GeneticPareto]] — the name's etymology and architectural rationale.
- [[CompoundAISystem]] — the formal target $\Phi = (M, C, \mathcal{X}, \mathcal{Y})$.

### Applications
- [[InferenceTimeSearch]] — GEPA's second mode: overfit a known task set.
- [[AdversarialPromptSearch]] — GEPA's third mode: inverted reward to discover worst-case prompts. **Extended to LLM safety** in [[2603.19247-prompt-optimization-jailbreaking]] — GEPA (light config, Gemini-2.5-pro reflection model) drives mean [[DangerScore|danger]] on Qwen-3 8B from 0.090 → 0.477 and on Claude 4.5 Sonnet from 0.046 → 0.236 (the second-strongest of the three DSPy optimizers tested, behind [[SIMBA]]).

### Direct rivals
- [[MIPROv2]] — Bayesian-optimization-over-(instructions,demos); the prior leading prompt optimizer GEPA beats by >10%.
- [[SIMBA]] — stochastic mini-batch reflective optimizer. **Beats GEPA on every cell of [[2603.19247-prompt-optimization-jailbreaking]]'s adversarial-objective grid** — a reversal of the benign-task ordering. Open question whether SIMBA's stochasticity is genuinely better for adversarial search or whether GEPA's reflection chain was under-budgeted in the *light* config.
- [[grpo|GRPO]] — weight-space RL; GEPA beats it by 6% avg / 20% peak with up to 35× fewer rollouts.
- [[TextGrad]] — textual-gradient-driven prompt optimizer.
- [[TraceOptoPrime|Trace (OptoPrime)]] — alternative LLM-feedback-driven optimizer.
- **APO** — BeamSearch-based selection; outperformed by Pareto-selection.
- **EvoPrompt / AlphaEvolve / OpenEvolve** — evolutionary alternatives.

### Benchmarks
- [[hotpotqa|HotpotQA]] / [[IFBench]] / [[HoVer]] / [[PUPA]] / [[AIME2025]] / [[LiveBenchMath]] — the six core benchmarks. [[NPUEval]] / [[KernelBench]] — the two inference-time-search benchmarks.

### DSPy integration
- [[DSPy]] — the framework that surfaces GEPA as `dspy.GEPA`.
- [[DSPyOptimizers]] — the catalog this optimizer belongs to.
- [[DSPyOptimization]] — the workflow this optimizer operationalizes. **Resolves the long-standing forward reference [[GEPA]]** carried by [[DSPyOptimization]] since [[dspy-optimization-overview|page 12]] named GEPA as the only carved-out optimizer.
- [[dspy-optimizers]] — the DSPy-docs source page (page 13).
- [[dspy-optimization-overview]] — the workflow-level source (page 12) that named GEPA as the framework's only specific carve-out from the 20/80 train/val split. The paper explains *why*: Pareto-selection's per-instance retention is what makes GEPA robust to small train sets.
- [[DSPyMetrics]] — the metric contract; GEPA additionally consumes optional domain-specific *textual* feedback alongside the scalar metric.
- [[DSPyModules]] / [[DSPyPredict]] — GEPA mutates each Predict's `signature` (instructions).
- [[DSPyProgrammingModel]] — the *"writing code instead of strings"* discipline; GEPA's reflection step inspects program trajectories the same way [[MIPROv2]]'s grounded proposal does.
- [[llmasjudge]] — the AI-feedback pattern GEPA's textual-feedback channel is structurally compatible with.
- [[BootstrapFewShot]] / [[BootstrapFewShotWithRandomSearch]] / [[BootstrapFinetune]] — sibling optimizers; GEPA is the reflection-driven alternative to their search-driven mechanisms.
- [[OverFitting]] — the failure mode the inverted 20/80 split defends against; GEPA's reflection-driven mechanism is empirically **more robust** to small training sets than search-driven mechanisms, which is the structural justification for the carve-out.

### Authoring institutions
- [[UCBerkeley]] / [[stanforduniversity|Stanford]] / [[BespokeLabsAI]] / [[NotreDame]] / [[Databricks]] / [[MITAcademic|MIT]] — author affiliations.
- [[LakshyaAgrawal]] — lead author. Senior authors: [[OmarKhattab]], [[MateiZaharia]], [[DanKlein]], [[IonStoica]], [[AlexandrosDimakis]], [[ChristopherPotts]], [[KoushikSen]], [[MengJiang]].

### Position-paper resonance
- [[2402.01817-llm-modulo]] — GEPA is a concrete LLM-Modulo instance: the LLM is the candidate proposer (via reflective mutation), $\mu_f$ is the external sound critic.
- [[2605.12966-agentic-ai-to-agi]] — the Pareto-selection vs SelectBestCandidate ablation is empirical evidence for the topology-over-node-strength framing.

### Broader activity
- [[PromptOptimization]] — the general activity GEPA's instruction-tuning operationalizes.
- [[reinforcementlearning|Reinforcement Learning]] — the family GEPA argues against using for sample-constrained compound AI system adaptation.
