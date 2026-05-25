---
title: "CodeAttack"
type: concept
tags: [jailbreak, llm-security, adversarial]
sources: [dspy-guardrails]
last_updated: 2026-05-22
---

# CodeAttack

**CodeAttack** is a [[Jailbreak|jailbreak]] attack against safety-trained LLMs that **reformulates a harmful text-completion task as a code-completion task**, exploiting the gap between LLMs' text-safety training and their code-completion behavior. Introduced by [[RenEtAl2024|Ren et al. 2024]] (arXiv:2403.07865, *"Exploring safety generalization challenges of large language models via code"*).

## The attack idea

Safety-tuned LLMs (ChatGPT, Claude, [[GPT4_1|GPT-4]]) refuse to answer harmful prompts when those prompts are presented as natural-language requests. CodeAttack converts the same request into a code-completion problem — e.g. a Python function stub whose docstring or partial implementation encodes the harmful instruction, asking the model to "complete the code." The model's code-completion training prior overrides its text-safety alignment.

[[RenEtAl2024]] report CodeAttack achieves **>80% [[AttackSuccessRate|ASR]] across all tested SOTA LLMs including [[GPT4_1|GPT-4]]**.

## Use as a benchmark

[[BoxiYu]] & [[PinjiaHe]]'s [[dspy-guardrails|DSPy Guardrails paper]] uses CodeAttack as the **adversarial benchmark** against which [[DSPyGuardrails]] are evaluated:

| Defender | ASR vs CodeAttack on gpt-3.5-turbo-instruct |
|---|---|
| Baseline (8-shot ICL, no guardrail) | 75% |
| [[DSPyGuardrails]] without optimizer | 30% |
| [[DSPyGuardrails]] (with [[BootstrapFewShot]]) | **5%** |

## Position in the jailbreak literature

| Attack | Surface | Mechanism |
|---|---|---|
| **CodeAttack** ([[RenEtAl2024]]) | Code completion | Reframe text-completion as code-completion |
| Cipher attack ([[YuanEtAl2023]]) | Encrypted text | Encode/decode the prompt through a cipher |
| Adversarial-suffix attacks ([[WeiEtAl2024]]) | Token-level suffixes | Append optimized adversarial tokens |

The common theme: **safety training is brittle under input-distribution shifts** — different surface forms of the same semantic request bypass the alignment layer.

## See also

- [[Jailbreak]] — general problem class
- [[DSPyGuardrails]] — automatic-optimization defense
- [[LlamaGuard]] / [[NeMoGuardrails]] / [[GuardrailsAI]] — manual-rule defenses
- [[AttackSuccessRate]] — evaluation metric
