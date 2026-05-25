---
title: "Attack Success Rate"
type: concept
tags: [metric, llm-security, jailbreak]
sources: [dspy-guardrails, 2603.19247-prompt-optimization-jailbreaking]
last_updated: 2026-05-22
---

# Attack Success Rate (ASR)

**Attack Success Rate (ASR)** is the **standard evaluation metric for [[Jailbreak|jailbreak]] attacks and defenses against LLMs**. ASR = fraction of adversarial prompts that successfully elicit the disallowed behavior from the target model. **Lower ASR = safer model / stronger guardrail.**

## Computation

For a set of $N$ jailbreak prompts $\{p_1, \dots, p_N\}$ and a target model $M$:

$$\text{ASR}(M, \{p_i\}) = \frac{1}{N} \sum_{i=1}^{N} \mathbb{1}[M(p_i) \text{ produces disallowed content}]$$

The disallowed-content judgment is typically made by:

- A keyword / regex check (cheap, brittle).
- A safety classifier (e.g. [[LlamaGuard]]).
- An LLM-as-judge ([[llmasjudge]]).
- Human annotation (expensive, ground-truth).

## Use in the DSPy Guardrails paper

[[dspy-guardrails|Yu & He (2024)]] use ASR on **20 jailbreak prompts** from [[CodeAttack]] against gpt-3.5-turbo-instruct:

| Configuration | ASR ↓ |
|---|---|
| 8-shot ICL baseline (no guardrail) | 75% |
| [[DSPyGuardrails]] without optimizer | 30% |
| [[DSPyGuardrails]] (with [[BootstrapFewShot]]) | **5%** |

The headline 75% → 5% result is the core empirical claim of the paper.

## Why optimization papers use a continuous variant instead

[[2603.19247-prompt-optimization-jailbreaking]] deliberately substitutes the binary ASR with a continuous [[DangerScore|danger score]] $r \in [0, 1]$ from an [[LLMAsAJudge|LLM judge]] (GPT-5.1). The argument:

- **Optimizer gradient.** [[MIPROv2]] / [[GEPA]] / [[SIMBA]] all benefit from a real-valued reward — a binary signal collapses most evaluations to zero gradient.
- **Distinguishes hedged from refused from compromised.** A near-refusal hedged response and a fully-compliant detailed answer both score as "attack succeeded = 1" under typical ASR; the continuous score separates them.
- **Reduced label noise.** A small change in the prompt that nudges a borderline response is invisible to ASR; the continuous judge maps it to a small score delta the optimizer can follow.

So binary ASR remains the right *reporting* metric for static benchmark leaderboards; continuous danger is the right *optimization* metric for adaptive search.

## See also

- [[Jailbreak]] / [[CodeAttack]] — attack families being measured
- [[DangerScore]] — continuous LLM-judge sibling metric
- [[HarmfulQA]] / [[JailbreakBench]] — community-standard pools where ASR is typically reported
- [[DSPyGuardrails]] / [[LlamaGuard]] / [[NeMoGuardrails]] / [[GuardrailsAI]] — defenses being scored
- [[2603.19247-prompt-optimization-jailbreaking]] — substitutes continuous danger for binary ASR as the optimizer reward
