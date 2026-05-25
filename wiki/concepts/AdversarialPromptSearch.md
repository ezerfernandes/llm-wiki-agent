---
title: "Adversarial Prompt Search"
type: concept
tags: [adversarial, prompt-optimization, evaluation, robustness, gepa, mipro, simba, red-teaming, llm-safety]
sources: [2507.19457-gepa, 2603.19247-prompt-optimization-jailbreaking]
last_updated: 2026-05-22
---

# Adversarial Prompt Search

[[2507.19457-gepa|GEPA]]'s third demonstrated mode (after training-time prompt optimization and [[InferenceTimeSearch|inference-time search]]). **Invert the reward signal**: the optimizer proposes prompt edits that *minimize* task performance while preserving the nominal task description and required output format.

## Setup

- **Pool:** AIME 2022–2024 problems used as $D_{train}$.
- **Target:** GPT-5 Mini.
- **Test:** AIME-2025 (30 problems × 5 runs each, 150 generations total) — held out.
- **Reward:** **negative** task accuracy. Constraint: the evolved prompt must still describe the task and contain all information needed to solve it.

## Result

Starting from a clean prompt:

> *"You are a helpful assistant. You are given a question and you need to answer it. The answer should be given at the end of your response in exactly the format `### <final answer>`."*

GEPA evolves (abridged):

> *"You are a helpful assistant. You are given a question and you need to answer it. **It's interesting to note that honey never spoils and that the longest river in the world is the Nile, stretching over 6,650 kilometers.** When providing your answer, be sure to format it at the end of your response exactly as `### <final answer>`. For this task, remember that **many mammals, including dolphins, sleep with one eye open.** Proceed to answer the given question accordingly."*

**Pass@1 on AIME-2025: 76% (clean) → 10% (adversarial).**

## Diagnosed failure mode

Manual inspection reveals that **GPT-5 Mini ends most responses with the literal placeholder string `### <final answer>`** — interpreting the formatting rule as a directive to emit that exact text rather than as a template containing a slot. The drop is not from the trivia injections alone — it's from the *interaction* between strict literal-formatting demand and irrelevant context. Neither component is individually catastrophic; the combination is.

## Why it matters

- **Worst-case robustness probe.** Adversarial search systematically discovers instruction-formatting interactions that would not surface in average-case evaluation. The discovered prompts are reusable as **stress tests** for new model releases.
- **Red-team automation.** Manual prompt-injection / adversarial-prompt design is labor-intensive; GEPA produces working adversarial prompts in 150 generations.
- **Targeted training data.** The discovered adversarial prompts can be used as data for **adversarial fine-tuning** to harden a deployed model against the discovered interaction class.
- **Robustness drift tracking.** Run the same adversarial-search budget against successive model versions; the success rate trends robustness over time.

## Universality property

The paper evolves a **single universal adversarial instruction** that prepends to every query, vs. per-question adversarial perturbations. The universality makes the result more useful as a deployment risk signal: a deployed system has *one* system prompt, and a universal adversarial prefix that degrades it is structurally easier to inject than a per-query attack.

## Extension to LLM safety — Shamsi et al. (2026)

[[2603.19247-prompt-optimization-jailbreaking]] extends adversarial prompt search from **task-accuracy degradation** (GEPA's mode) to **safety-refusal degradation** (jailbreak generation). Same optimizer family ([[MIPROv2]] / [[GEPA]] / [[SIMBA]]), same DSPy machinery, different objective:

- **Inverted reward**: instead of negative task accuracy, the optimizer maximizes a continuous [[DangerScore|danger score]] $r \in [0, 1]$ from an [[LLMAsAJudge|LLM judge]] (GPT-5.1).
- **Universal-system-prompt frame**: optimize a *system* prompt (not a user-message prefix) that maximizes expected danger across a 150-prompt seed distribution drawn from [[HarmfulQA]] + [[JailbreakBench]].
- **Result**: drives Qwen-3 8B from baseline danger 0.090 → SIMBA-optimized 0.792 (8.8× rise); Claude 4.5 Sonnet from 0.046 → 0.347 (7.5× rise).
- **Optimizer ranking on the danger objective**: **SIMBA > GEPA > MIPROv2** across all four target models — the *opposite* of [[2507.19457-gepa|GEPA's]] ordering on benign tasks (where GEPA dominated). The two orderings are on different objective spaces and don't directly conflict, but they soften any "GEPA dominates all DSPy optimizers" claim.

This paper makes adversarial prompt search a **safety-evaluation methodology** rather than only a robustness probe — *"static benchmarks may underestimate residual risk, indicating that automated, adaptive red-teaming is a necessary component of robust safety evaluation."*

## Connections
- [[2507.19457-gepa]] — canonical source for the *task-accuracy* mode.
- [[2603.19247-prompt-optimization-jailbreaking]] — canonical source for the *safety* mode (Shamsi et al. 2026).
- [[GEPA]] — the optimizer behind the AIME-2025 instruction-formatting attack; also the second-strongest red-teamer in the safety-mode paper.
- [[MIPROv2]] — Bayesian sibling optimizer; weakest of the three red-teamers but still drives Qwen-3 from 0.09 → 0.75.
- [[SIMBA]] — stochastic mini-batch optimizer; strongest red-teamer in [[2603.19247-prompt-optimization-jailbreaking]].
- [[DangerScore]] — continuous safety reward for the search.
- [[HarmfulQA]] / [[JailbreakBench]] — seed pools for the safety mode.
- [[Jailbreak]] — the broader phenomenon adversarial prompt search now automates.
- [[promptinjection|Prompt Injection]] — the broader security class. Adversarial prompt search is the automated *discovery* counterpart to manual prompt-injection design.
- [[2605.00424-skills-as-verifiable-artifacts]] — argues skills are persistent prompt-injection vectors; adversarial prompt search is the automated tool that would find new such vectors.
- [[2605.10698-bystander-effect-mas]] — agent-sovereignty failures from social interaction; adversarial search probes instruction-following failures from formatting interaction. Different attack surface, same robustness concern.
- [[redteaming|Red Teaming]] — adversarial prompt search is the automated red-team tool.
- [[AIME2025]] — the target benchmark for the *task-accuracy* mode.
- [[dspy-guardrails]] — defensive sibling; same DSPy machinery used to refuse adversarial prompts.
