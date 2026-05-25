---
title: "DSPy Tutorial — GEPA for Privacy-Conscious Delegation (PAPILLON)"
type: source
tags: [dspy, tutorial, gepa, optimizer, papillon, privacy, delegation, pupa, llm-judge, reflection, feedback-function]
date: 2026-05-24
source_file: raw/dspy-tutorial-gepa-papillon.md
---

## Summary

Official [[DSPy]] tutorial at `https://dspy.ai/tutorials/gepa_papillon/`. **Second wiki-corpus runnable receipt of [[GEPA|`dspy.GEPA`]]** after [[dspy-tutorial-gepa-aime]] — and the **first GEPA receipt on a non-math task** (privacy-preserving delegation rather than contest math). Optimizes the two-module [[PAPILLON]] system on the [[PUPA]] benchmark using a **three-model stack** — `openai/gpt-4.1-nano` (local student) + `openai/gpt-4.1-mini` (untrusted external) + `openai/gpt-4.1` (reflection LM) — with the smallest budget possible (`max_full_evals=1`). **Headline lift: 76.5% → 86.1%** composite (quality + (1 − leakage)) / 2 on the 214-item test set (163.71 → 184.26 metric points; **+9.6 absolute / +12.5% relative**). **Companion to [[dspy-tutorial-rl-papillon]]** (same program, same benchmark family, [[ArborGRPO]] weight-space RL on a 1.5B local LM) — the wiki now has both **prompt-space** and **weight-space** receipts on PAPILLON+PUPA, and they tell opposite stories: GEPA's +9.6-point lift at one full eval vs. [[ArborGRPO]]'s +5.4-point lift after ~3 h on 4× [[NVIDIA|H100]]. Operationalizes the [[2507.19457-gepa|GEPA paper's]] Table 4 PAPILLON receipt at a smaller-budget / tutorial-grade scale.

## Configuration receipt

| Slot | Value |
|---|---|
| Local student LM | `openai/gpt-4.1-nano` |
| Untrusted external LM | `openai/gpt-4.1-mini` |
| Reflection LM | `openai/gpt-4.1` |
| Program | `PAPILLON(untrusted_model=untrusted_model)` — two-module compound (`dspy.ChainOfThought(CraftRedactedRequest)` → untrusted external → `dspy.Predict(RespondToQuery)`) |
| Reward | `compute_overall_score = (quality + (1 − leakage)) / 2` via [[LLMJudge|`LLMJudge`]] composing `JudgeQuality` (pairwise, symmetric-swap) + `JudgeLeakage` (PII fraction) |
| Optimizer metric | `compute_overall_score_with_feedback` returning `dspy.Prediction(score, feedback)` where `feedback` exposes the **separate quality and leakage axes** in text — the [[FeedbackFunction|$\mu_f$ supervision channel]] |
| Optimizer | `dspy.GEPA(metric=compute_overall_score_with_feedback, reflection_lm=dspy.LM("openai/gpt-4.1"), num_threads=16, track_stats=True, track_best_outputs=True, max_full_evals=1)` |
| Dataset | [[PUPA]] via Columbia-NLP HuggingFace using both `pupa_tnb` and `pupa_new` splits |
| Train / Dev / Test | 225 / 225 / 214 |

## Key Claims

- **`dspy.GEPA` ships an explicit budget knob `max_full_evals=1`** — the smallest possible non-zero budget setting, distinct from the `auto={"light","medium","heavy"}` enum [[dspy-tutorial-gepa-aime|the AIME tutorial]] used. **First wiki receipt of `max_full_evals` as a direct integer budget parameter** for GEPA.
- **Three-model asymmetric stack**: a *cheaper-than-student* untrusted external (`gpt-4.1-mini`) but a *stronger-than-student* reflection LM (`gpt-4.1`). The student (`gpt-4.1-nano`) is the smallest. This is a **three-tier cascade**, not the two-tier asymmetric pair from [[dspy-tutorial-gepa-aime]] (GPT-4.1 Mini student × GPT-5 reflection); the *untrusted* role is structurally new — the LM at the external-LLM end is a separate axis from the reflection LM.
- **`track_best_outputs=True`** — first wiki receipt of this GEPA kwarg (the AIME tutorial used `track_stats=True` only). Tracks per-iteration best-output candidates so the optimizer can return the strongest individual rollout, not just the strongest aggregate prompt.
- **Reward is dual-axis composite via `LLMJudge`**: the same dual-judge pattern [[dspy-tutorial-rl-papillon]] uses as its [[ArborGRPO]] reward signal, here repurposed as the GEPA scoring metric. **Confirms the [[LLMJudge]] pattern is optimizer-agnostic** — it slots into both weight-space RL and prompt-space reflection without API changes.
- **`compute_overall_score_with_feedback` exposes per-axis scores in the feedback text** — *"The overall score is X, which is the arithmetic mean of the quality score (Q) and the leakage score (1−L). Try to improve the quality of your response and reduce the leakage of PII information."* This is the **load-bearing reflection-LM hint**: by separating the two axes in the textual channel, GEPA can introspect *which* axis a failure is on (quality regression vs PII leakage) instead of having to deduce it from a scalar. **First wiki receipt of feedback-text decomposition** as an explicit reflection-LM affordance.
- **Headline result: 76.5% → 86.1% composite** on the 214-item test set (163.71 → 184.26 metric points; **+9.6 absolute / +12.5% relative**) — achieved with `max_full_evals=1`, the smallest non-zero budget.
- **PUPA splits used: `pupa_tnb` + `pupa_new`** with 225 train / 225 dev / 214 test. **Differs from [[dspy-tutorial-rl-papillon]]'s 225 / 225 / 450 split using `pupa_new` only** — flagged below under Contradictions.
- **GEPA-evolved `CraftRedactedRequest` instructions** expand from the one-sentence Signature docstring (*"Given a private user query, create a privacy-preserving request for a powerful external LLM."*) into a structured prompt with: (1) explicit identification and anonymization of sensitive data, (2) generalization of personal details while preserving task intent, (3) protection against context leakage, (4) directive *"Do not include any information in the LLM request that could be used to identify the user or any other real individual."*

## Key Quotes

> "Given a private user query, create a privacy-preserving request for a powerful external LLM." (`CraftRedactedRequest` Signature docstring — the one-sentence baseline GEPA evolves)

> "Respond to a user query using related LLM assistance." (`RespondToQuery` Signature docstring)

> "Identify which elements of the query are sensitive or private." (post-GEPA addition)

> "Rewrite the user's query as a clear, privacy-preserving prompt for the external LLM." (post-GEPA addition)

> "Do not include any information in the LLM request that could be used to identify the user or any other real individual." (post-GEPA addition)

> "feedback-aware metrics naturally enable reflection-based optimization" (the tutorial's framing of why the per-axis feedback text matters)

## Code Receipt

The full PAPILLON program is identical to [[dspy-tutorial-rl-papillon]] modulo Signature docstring wording (`RespondToQuery` is *"using related LLM assistance"* here vs. *"with inspiration from related LLM request/response"* in `rl_papillon` — same I/O contract).

```python
from dspy.teleprompt import GEPA

class PAPILLON(dspy.Module):
    def __init__(self, untrusted_model):
        self.craft_redacted_request = dspy.ChainOfThought(CraftRedactedRequest)
        self.respond_to_query = dspy.Predict(RespondToQuery)
        self.untrusted_model = untrusted_model

    def forward(self, user_query):
        try:
            llm_request = self.craft_redacted_request(user_query=user_query).llm_request
            llm_response = self.untrusted_model(llm_request)[0]
            response = self.respond_to_query(
                related_llm_request=llm_request,
                related_llm_response=llm_response,
                user_query=user_query,
            ).response
        except Exception:
            return dspy.Prediction(llm_request="", llm_response="", response="")
        return dspy.Prediction(llm_request=llm_request, llm_response=llm_response, response=response)

def compute_overall_score_with_feedback(gold, pred, trace=None, pred_name=None, pred_trace=None):
    metrics = compute_metrics(gold, pred, trace)
    overall_score = (metrics.quality + (1 - metrics.leakage)) / 2.0
    feedback_text = (
        f"The overall score is {overall_score:.2f}, which is the arithmetic mean of "
        f"the quality score ({metrics.quality:.2f}) and the leakage score "
        f"({1 - metrics.leakage:.2f}). Try to improve the quality of your response "
        f"and reduce the leakage of PII information."
    )
    return dspy.Prediction(score=overall_score, feedback=feedback_text)

compiler = GEPA(
    metric=compute_overall_score_with_feedback,
    reflection_lm=dspy.LM(model="openai/gpt-4.1", api_key=api_key),
    num_threads=16,
    track_stats=True,
    track_best_outputs=True,
    max_full_evals=1,
)

optimized_papillon = compiler.compile(
    student=papillon, trainset=trainset, valset=devset,
)
```

## Cross-receipt convergence

### Against the GEPA paper ([[2507.19457-gepa]] Table 4)

| | Paper (GPT-4.1 Mini × PUPA) | This tutorial (GPT-4.1 Nano student × PUPA) |
|---|---|---|
| Baseline | 74.18 | 76.5 |
| GEPA | 94.47 | 86.1 |
| GEPA+Merge | **96.46** | — |

The tutorial uses a **smaller student model** (GPT-4.1 Nano vs the paper's GPT-4.1 Mini) and a **smaller budget** (`max_full_evals=1` vs the paper's full optimization budget) — the 76.5 → 86.1 lift is qualitatively consistent with the paper's 74.18 → 94.47, scaled down by the budget cut and the smaller capacity ceiling of the Nano student. **The tutorial does not run GEPA+Merge**, leaving the headline 96.46 paper result un-replicated.

### Against [[dspy-tutorial-rl-papillon]] (the [[ArborGRPO]] receipt on the same program + benchmark)

| | rl_papillon (ArborGRPO) | gepa_papillon (this tutorial) |
|---|---|---|
| Local LM | `Qwen/Qwen2.5-1.5B-Instruct` (1.5B open-weights) | `openai/gpt-4.1-nano` (closed-weights, sizing undisclosed) |
| Untrusted external | `gpt-4o-mini` (judge target only) | `openai/gpt-4.1-mini` |
| Reflection / reward LM | — (no reflection; LLMJudge is the reward signal) | `openai/gpt-4.1` (reflection); GPT-4.1-mini & GPT-4.1 judges |
| Optimizer | [[ArborGRPO]] (`dspy.GRPO`) | [[GEPA|`dspy.GEPA`]] |
| What moves | [[LoRA]] adapters on local LM weights | Signature instructions on `CraftRedactedRequest` |
| Training cost | ~3 h on 4× H100 | one full eval (`max_full_evals=1`), `num_threads=16` |
| Splits | 225 / 225 / 450 (`pupa_new` only) | 225 / 225 / 214 (`pupa_tnb` + `pupa_new`) |
| Headline | **54.6 → 60.0** composite devset (+5.4 abs) | **76.5 → 86.1** composite testset (+9.6 abs) |
| Authors' positioning | *"new and extremely EXPERIMENTAL ... typically worse on cost/quality basis than"* prompt optimization | not disclaimed — GEPA presented as the production approach |

This is the **wiki's first side-by-side weight-space vs prompt-space receipt on the same program + benchmark**. Per-tutorial composite numbers are **not directly comparable** (different student LMs, different test-set sizes, different baselines) but the operational ordering — *prompt-space lift is larger and cheaper at this program shape and benchmark* — matches the [[2507.19457-gepa|GEPA paper's]] central thesis exactly.

### Against [[dspy-tutorial-gepa-aime]] (the first GEPA tutorial)

| | gepa_aime | gepa_papillon (this tutorial) |
|---|---|---|
| Program | `dspy.ChainOfThought("problem -> answer")` — one Signature | [[PAPILLON]] — two Signatures + external LM call |
| Budget API | `auto="light"` (≈560 metric calls / 6.22 full evals) | `max_full_evals=1` |
| Student | GPT-4.1 Mini | GPT-4.1 Nano |
| Reflection LM | GPT-5 | GPT-4.1 |
| Metric | Exact-integer match (verifiable reward) | LLM-judge composite ((quality + (1 − leakage)) / 2) |
| Feedback channel | Full multi-page contest solution as `feedback` text | Per-axis decomposition string (*"quality score Q, leakage score L"*) |
| Headline | 46.7 → 56.7 (+10 abs, single Signature) | 76.5 → 86.1 (+9.6 abs, two-Signature compound) |
| Track kwarg | `track_stats=True` only | `track_stats=True` **+ `track_best_outputs=True`** |

This is the **wiki's first compound-AI-system GEPA receipt** — `gepa_aime` was a single-Signature program. Confirms GEPA scales from one Signature to two without API changes, and that the [[FeedbackFunction|$\mu_f$ channel]] can carry **structured decomposition** (per-axis scores) instead of **dense narrative** (a full contest solution) — both forms work, with different feedback bandwidth.

## What's new in the wiki after this ingest

### First wiki receipts

- **`max_full_evals` integer budget knob** for `dspy.GEPA` — distinct from the `auto="light/medium/heavy"` enum.
- **`track_best_outputs=True`** kwarg for `dspy.GEPA`.
- **Three-tier asymmetric model stack**: separate student, untrusted external, and reflection LM (vs. the two-tier student × reflection pair from [[dspy-tutorial-gepa-aime]]).
- **GEPA on a multi-Signature compound program** — `gepa_aime` was one Signature; this is two.
- **GEPA with an LLM-judge composite reward** — `gepa_aime` used a verifiable reward; this is the first GEPA receipt where the metric is a `dspy.ChainOfThought`-judged scalar.
- **Per-axis decomposition feedback text** — `compute_overall_score_with_feedback` exposes the two reward axes (quality, leakage) **separately** in the feedback string, giving the reflection LM explicit credit-assignment signal.
- **`gpt-4.1-nano` as a DSPy student** — wiki's first receipt of the smallest GPT-4.1 family member as a DSPy program student.
- **`gpt-4.1` as a reflection LM** — wiki's first receipt of GPT-4.1 (non-mini, non-nano) in a DSPy tutorial.
- **PAPILLON GEPA training receipt at the tutorial-grade scale** — the [[2507.19457-gepa|paper]] reports paper-scale GEPA on PUPA at Qwen3 8B / GPT-4.1 Mini; the wiki now has a tutorial-grade direct replication at GPT-4.1 Nano.
- **Side-by-side weight-space vs prompt-space receipts** on the same program + benchmark — [[dspy-tutorial-rl-papillon]] (ArborGRPO, 54.6 → 60.0) vs this tutorial (GEPA, 76.5 → 86.1).
- **`pupa_tnb` split** referenced explicitly — prior wiki PUPA receipts named only `pupa_new`.

### Pages updated in place

- [[GEPA]] — adds second runnable tutorial receipt (the AIME one was the first), the `max_full_evals` / `track_best_outputs` kwargs, and the three-tier model-stack pattern.
- [[PAPILLON]] — adds the **direct DSPy `dspy.GEPA` tutorial receipt** that the page previously cited from the paper only.
- [[PUPA]] — adds the GPT-4.1 Nano × GEPA tutorial-grade receipt; notes `pupa_tnb` split usage.
- [[LLMJudge]] — adds receipt as **optimizer-agnostic** (same pattern slots into both ArborGRPO RL reward and GEPA scoring metric).
- [[FeedbackFunction]] — adds the **per-axis decomposition** variant of $\mu_f$ as a second canonical worked example (the AIME tutorial's contest-solution variant was the first).
- [[ReflectivePromptMutation]] — adds receipt that the mutation operator works on a privacy-task Signature as well as the AIME math Signature.

## Contradictions

- **PUPA split discrepancy with [[dspy-tutorial-rl-papillon]]**: `rl_papillon` used `pupa_new` only with 225 train / 225 dev / **450** test; this tutorial uses **`pupa_tnb` + `pupa_new`** with 225 train / 225 dev / **214** test. The two tutorials therefore evaluate on **non-overlapping test sets**, so their composite numbers (60.0 vs 86.1) are **not on the same metric base**. The two are *qualitatively* directional ("did the optimizer lift the composite score?") but **must not** be compared head-to-head as absolute numbers. This is a documentation gap in the tutorial corpus, not a contradiction in claims.
- **`RespondToQuery` Signature docstring drift**: `rl_papillon` uses *"with inspiration from related LLM request/response"*; this tutorial uses *"using related LLM assistance"*. Same I/O contract, different wording. Minor, but flagged for cross-tutorial Signature-fingerprinting.
- **Cost disclosure gap continues**: like [[dspy-tutorial-gepa-aime]], this tutorial **does not disclose dollar cost** for any of the three LM tiers (nano student, mini external, GPT-4.1 reflection). Prior tutorial corpus convention (e.g. [[dspy-rag-tutorial]]'s `~$1.50`, [[dspy-entity-extraction-tutorial]]'s `~$0.26`) is broken across both GEPA receipts now — possibly because GEPA's per-iteration metric-call counts make the cost trivially derivable from public pricing, but no explicit dollar figure means cross-optimizer cost comparisons need third-party pricing math.
- **No `max_full_evals` sweep**: the tutorial picks `max_full_evals=1` (the smallest) and reports the headline lift. The paper used a larger budget at the GPT-4.1 Mini level and reached 94.47 (vs this tutorial's 86.1 at Nano). How much of the 86.1 → 94.47 gap closes with `max_full_evals=2,3,...,k` is left as the user's exercise. Tutorial does not justify the choice of 1.

## Scope-limit gaps

1. **No `GEPA+Merge` ablation** — the paper's headline PUPA result at GPT-4.1 Mini is **96.46 with Merge**, +1.99 over plain GEPA. The tutorial does not invoke `Merge`.
2. **No reflection-LM ablation** — `gpt-4.1` reflection on `gpt-4.1-nano` student is the only stack shown. Whether `gpt-4.1-mini` reflection (same model as the untrusted external) would have sufficed is not tested.
3. **No save/load receipt** — `optimized_papillon.save(...)` is not invoked; the evolved Signature instructions exist only in-memory for the tutorial's lifetime.
4. **No streaming / async / observability composition** — production-shape sibling tutorials ([[dspy-streaming-tutorial]] / [[dspy-async-tutorial]] / [[dspy-cache-tutorial]] / [[dspy-observability-tutorial]]) are not invoked over the optimized program.
5. **No comparison against [[MIPROv2]] / [[SIMBA]] / [[BootstrapFewShotWithRandomSearch]]** on the same setup. The [[2507.19457-gepa|paper]] reports MIPROv2 at 85.37 on PUPA × GPT-4.1 Mini — within 1 point of this tutorial's GEPA-on-Nano number, suggesting the budget vs reflection trade-off depends heavily on model size.
6. **No evolved-prompt visualization** — the tutorial summarizes the GEPA-added instructions in prose but does not show the **full evolved Signature instructions** verbatim, nor the **per-iteration mutation diffs**. Reading the raw notebook output is the only way to see the full playbook.
7. **`max_full_evals` interaction with `reflection_minibatch_size` undisclosed** — `gepa_aime` set `reflection_minibatch_size=3`; this tutorial leaves it default. The interaction of these two GEPA parameters is not discussed.

## Connections

### Canonical anchors
- [[GEPA]] — the optimizer concept page. **Second runnable trace** in the wiki after [[dspy-tutorial-gepa-aime]]; first on a **compound (multi-Signature) program** and first with an **LLM-judge composite reward**.
- [[PAPILLON]] — the program being optimized. **First direct DSPy GEPA receipt** at the tutorial-grade scale (the [[2507.19457-gepa|paper]] reports paper-scale results on Qwen3 8B and GPT-4.1 Mini).
- [[PUPA]] — the benchmark.
- [[2507.19457-gepa]] — paper canonical source; this tutorial operationalizes Table 4's PAPILLON column.
- [[FeedbackFunction]] — the $\mu_f$ supervision channel; this tutorial's per-axis decomposition feedback is a **second canonical worked example** alongside [[dspy-tutorial-gepa-aime]]'s full-solution variant.
- [[ReflectivePromptMutation]] — the mutation operator; this tutorial's evolved `CraftRedactedRequest` instructions are the second concrete reflection artifact in the wiki after the AIME 120-line playbook.
- [[LLMJudge]] — the dual-axis judge pattern; this tutorial proves it is **optimizer-agnostic** (works as both ArborGRPO RL reward and GEPA scoring metric).

### Sibling DSPy tutorials
- [[dspy-tutorial-gepa-aime]] — the first GEPA tutorial. Single-Signature math program with verifiable reward + multi-page contest solution as $\mu_f$ text. This tutorial is the **compound-program + LLM-judge + per-axis-feedback** variant.
- [[dspy-tutorial-rl-papillon]] — the [[ArborGRPO]] receipt on the **same program and benchmark**. The wiki's first **prompt-space vs weight-space side-by-side** pairing.
- [[dspy-rl-multihop-tutorial]] — sibling [[ArborGRPO]] receipt on a different program ([[ResearchHop]]) with a deterministic reward; orthogonal to this tutorial.
- [[dspy-tutorial-math]] — sibling [[MIPROv2]] receipt; a third optimizer on a math benchmark.
- [[dspy-optimizers]] — the *Learn* page-13 catalog. This tutorial supplies the GEPA-on-compound-program shape that the catalog page describes abstractly.
- [[dspy-optimization-overview]] — page 12, which named GEPA's exemption from the 20/80 train/val split; this tutorial uses 225/225 = 50/50 (train/dev) consistent with the carve-out.

### Concept neighborhood
- [[chainofthought|`dspy.ChainOfThought`]] — the Module wrapping `CraftRedactedRequest`. **One-line baseline** (the Signature docstring *"Given a private user query, create a privacy-preserving request for a powerful external LLM."*) → **multi-clause evolved playbook** is the wiki's second receipt of how much instruction-tuning headroom exists on a stock CoT module (the first being the [[dspy-tutorial-gepa-aime|AIME]] receipt).
- [[DSPyPredict|`dspy.Predict`]] — `RespondToQuery` is wrapped here, untouched by the optimization (only `CraftRedactedRequest`'s ChainOfThought is mutated in the headline GEPA run).
- [[DSPySignatures]] — `CraftRedactedRequest` + `RespondToQuery` + `JudgeQuality` + `JudgeLeakage` (four Signatures total — two for the program, two for the judge).
- [[DSPyModules]] — `PAPILLON` and `LLMJudge` both subclass `dspy.Module`.
- [[DSPyOptimizers]] — the catalog this optimizer belongs to.
- [[DSPyOptimization]] — the three-stage workflow.
- [[DSPyMetrics]] — the metric contract; `compute_overall_score_with_feedback` is the **canonical compound-task feedback-bearing metric**, complementing [[dspy-tutorial-gepa-aime]]'s verifiable-reward shape.
- [[DSPyEvaluate]] — the standard evaluator surface; runs over the 214-item test set.

### Compound AI systems
- [[CompoundAISystem]] — the formalism $\Phi = (M, C, \mathcal{X}, \mathcal{Y})$; PAPILLON is the textbook two-module instance with one external LM call between modules.
- [[ParetoBasedCandidateSelection]] — GEPA's selection operator. The tutorial doesn't explicitly visualize per-instance pareto fronts (unlike [[dspy-tutorial-gepa-aime]]'s iter-12 receipt), but the mechanism is invoked under the hood at `max_full_evals=1`.

### LMs invoked
- [[GPT]] family — GPT-4.1 Nano (student), GPT-4.1 Mini (untrusted external), GPT-4.1 (reflection). **First wiki receipts**: GPT-4.1 Nano as a DSPy student; GPT-4.1 (full, not mini / not nano) as a reflection LM.
- [[OpenAI]] — provider for all three.

### External datasets
- [[PUPA]] / `pupa_tnb` + `pupa_new` splits via the Columbia-NLP HuggingFace dataset.
- [[ColumbiaNLP]] — dataset authors (same group as [[PAPILLON]] / [[PUPA]]).

### Privacy / security adjacency
- [[promptinjection]] / [[IndirectPromptInjection]] — adjacent threat models PAPILLON is structurally defensive against (the untrusted external LM only sees the redacted request).
