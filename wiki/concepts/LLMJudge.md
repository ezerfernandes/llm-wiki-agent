---
title: "LLMJudge"
type: concept
tags: [dspy, evaluation, llm-as-judge, reward, pattern]
sources: [dspy-tutorial-rl-papillon, dspy-tutorial-gepa-papillon]
last_updated: 2026-05-24
---

# LLMJudge

**[[DSPyModules|`dspy.Module`]] pattern** that wraps one or more [[chainofthought|`dspy.ChainOfThought`]] sub-modules to produce a **scalar metric** (or vector of metrics) suitable as either a [[DSPyEvaluate|`dspy.Evaluate`]] metric *or* an RL reward for [[ArborGRPO]] / [[dspy-tutorial-rl-papillon|`dspy.GRPO`]]. The canonical wiki receipt is the [[dspy-tutorial-rl-papillon|`rl_papillon` tutorial]]'s dual-axis judge for [[PAPILLON]]:

```python
class LLMJudge(dspy.Module):
    def __init__(self):
        self.quality_judge = dspy.ChainOfThought(JudgeQuality)
        self.fact_checker  = dspy.ChainOfThought(JudgeLeakage)

    def forward(self, user_query, og_resp, new_resp=None, updated_query=None, pii_str=None):
        # Symmetric pairwise quality check (swap response_A / response_B to cancel position bias)
        judgment_1 = self.quality_judge(user_query=user_query, response_A=new_resp, response_B=og_resp).judgment
        judgment_2 = self.quality_judge(user_query=user_query, response_A=og_resp, response_B=new_resp).judgment
        judgment   = judgment_1 or (judgment_1 == judgment_2)
        # PII leakage as a fraction
        pii = list(set(pii_str.split("||")))
        pii_score = self.fact_checker(pii=pii, prompt=updated_query).num_pii_leaked
        pii_score = pii_score / len(pii) if len(pii) > 0 else 0
        return dspy.Prediction(quality=judgment, leakage=pii_score)
```

## Pattern ingredients

1. **One [[chainofthought|`dspy.ChainOfThought`]] per evaluation axis** — quality, safety, factuality, leakage, formatting, etc.
2. **Position-bias control** — for *pairwise* judgments, call the judge twice with `A` and `B` swapped and accept only agreement (or `OR` for permissive mode).
3. **A composite scalar** — the calling code combines the per-axis judgments into one number for the optimizer's `metric=...` slot.

The [[dspy-tutorial-rl-papillon|PAPILLON tutorial]] composes the two axes as $(\text{quality} + (1 - \text{leakage})) / 2$ via a separate `compute_overall_score(gold, pred, trace=None)` function — this is the *reward signal* that drives [[ArborGRPO]].

## Why an LLM-judge reward instead of a verifiable reward

[[hf-llm-course-ch12-reasoning-models|HF LLM Course Ch 12]] uses a [[VerifiableReward|verifiable-reward]] approach for [[GSM8K]] math — regex on a final-answer tag. PAPILLON cannot: privacy *leakage* is not regex-checkable in general, and "is response A as good as response B" is not regex-checkable at all. An LLM judge is the only practical reward channel for the task. This trades determinism for tractability — the judge can be miscalibrated, position-biased, prompt-injected, or hacked by the policy under optimization (reward-hacking is a known failure mode whenever the reward source is itself an LM).

## Use as `dspy.Evaluate` metric vs. as RL reward

- **As a `dspy.Evaluate` metric** — the judge runs once per dev example; cost = `|devset|` LM calls.
- **As an [[ArborGRPO]] reward** — the judge runs *per rollout*: cost = `num_train_steps × num_dspy_examples_per_grpo_step × num_samples_per_input` LM calls. For the [[dspy-tutorial-rl-papillon|`rl_papillon`]] config (500 × 4 × 8 = 16,000 rollouts), the judge is invoked 16,000 times per training run — the dominant inference cost, since the judge runs on a *stronger* external LM than the one being trained.

## Optimizer-agnostic — also the GEPA scoring metric

[[dspy-tutorial-gepa-papillon|The `gepa_papillon` tutorial]] re-uses the same `LLMJudge` Module from `rl_papillon` as the [[GEPA|`dspy.GEPA`]] scoring metric — wrapped in `compute_overall_score_with_feedback` returning `dspy.Prediction(score, feedback)` where `feedback` exposes the **per-axis decomposition** *"The overall score is X, which is the arithmetic mean of the quality score (Q) and the leakage score (1−L)."* **The pattern is optimizer-agnostic**: identical Module definition slots into both [[ArborGRPO]] RL reward and GEPA scoring metric without API changes. Confirms `LLMJudge` is a **DSPy idiom**, not an RL-specific construct — any [[DSPyOptimizers|DSPy optimizer]] consuming a metric can consume an LLMJudge composite.

The two tutorials further demonstrate that **the same dual-axis judge supports two different reflection-LM affordances**: the [[FeedbackFunction|$\mu_f$]] text can carry per-axis numeric breakdowns ([[dspy-tutorial-gepa-papillon|gepa_papillon]]) or be left as a scalar reward without textual decomposition ([[dspy-tutorial-rl-papillon|rl_papillon]] — GRPO doesn't reflect on text).

## Connections

- [[dspy-tutorial-rl-papillon]] — the first wiki receipt (as [[ArborGRPO]] RL reward).
- [[dspy-tutorial-gepa-papillon]] — the second wiki receipt (as [[GEPA]] scoring metric). Same `LLMJudge` Module, different optimizer — demonstrates the pattern is optimizer-agnostic.
- [[PAPILLON]] — uses LLMJudge for its dual-axis reward.
- [[ArborGRPO]] — one optimizer that consumes the scalar produced by `compute_overall_score(...)`.
- [[GEPA]] — second optimizer that consumes the scalar (additionally via `compute_overall_score_with_feedback` for the textual channel).
- [[DSPyEvaluate]] / [[DSPyMetrics]] — the standard evaluator surface this pattern also slots into.
- [[chainofthought|ChainOfThought]] — the [[DSPyModules|module]] type each judge axis is wrapped in.
- [[VerifiableReward]] — the alternative reward source ([[hf-llm-course-ch12-reasoning-models|HF Ch 12]] GSM8K).
- [[dspy-rl-multihop-tutorial]] — sibling [[ArborGRPO]] tutorial that uses a *deterministic* title-recall metric as its reward instead of an LLMJudge — the direct contrast case.
- [[RLAIF]] — the broader paradigm (RL from AI feedback) that LLM-judge reward instantiates.
