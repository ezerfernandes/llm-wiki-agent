---
title: "Verifier"
type: concept
tags: [evaluation, test-time-compute, inference, llm]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Verifier

A model trained to **score candidate outputs**, typically for tasks with verifiable correctness (math, code, SQL). Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], OpenAI trained verifiers to *"help their models pick the best solutions to math problems"* (Cobbe et al. 2021).

## The 30× result

The headline finding from Ch 2:

> "The use of verifiers resulted in approximately the **same performance boost as a 30× model size increase**. This means that a 100-million-parameter model that uses a verifier can perform on par with a 3-billion-parameter model that doesn't use a verifier."

This is one of the chapter's strongest arguments that **scaling inference (via test-time compute and a verifier) can be more efficient than scaling parameters**.

## Verifier vs Reward Model

Closely related concepts:

- **[[RewardModel|Reward model]]** — trained on [[ComparisonData|comparison data]] for general human-preference alignment.
- **Verifier** — typically trained for **tasks with a single correct answer** (math, code), often with synthetic data where correctness is automatable.

Verifiers tend to be more reliable than reward models because the ground truth they're trained on is less ambiguous.

## How [[bestofn|best-of-N]] uses verifiers

The pattern:
1. Sample N candidate outputs from the foundation model.
2. Score each with the verifier.
3. Return the highest-scoring output.

[[StitchFix|Stitch Fix]] and [[Grab|Grab]] use this pattern with reward models; OpenAI used it with verifiers for math; [[Nextdoor|Nextdoor]] reported it as the key factor in their 2023 quality improvements.

## Limitation: adversarial outputs at scale

Per Ch 2's OpenAI data: **at ~400 samples, performance peaks; beyond that it declines**. The hypothesis:

> "As the number of sampled outputs increases, the chance of finding adversarial outputs that can fool the verifier also increases." — Ch 2

This is essentially **[[RewardHacking|reward hacking]]** at inference time — the more outputs you sample, the more likely one of them inadvertently exploits the verifier's weaknesses.

## Stanford "Monkey Business" counter-result

Brown et al. (2024) report log-linear scaling of problem-solving up to 10,000 samples — contradicting OpenAI's peak-at-400 finding. Ch 2 flags this as an open question.

## Connections
- [[RewardModel]] — closely related; verifier specialized for verifiable-correctness tasks.
- [[bestofn]] — the selection strategy that uses verifiers.
- [[TestTimeCompute]] — the broader pattern verifiers enable.
- [[selfconsistency]] — verifier-free alternative (majority vote).
- [[RewardHacking]] — what limits verifier-guided sampling at scale.
- [[GSM8K]] — the math-problem benchmark OpenAI's verifier was developed against.
- [[ai-engineering-ch02-foundation-models]] — primary source.
