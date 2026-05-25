---
title: "Grab"
type: entity
tags: [company, super-app, southeast-asia, ai-application]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Grab

Southeast Asian super-app — ride-hailing, food delivery, fintech. Notable in the wiki because of [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]'s framing of Grab as **one of two canonical "skip the RL step" production examples** in [[rlhf|RLHF]] / preference finetuning.

## What they do with LLMs (per Ch 2)

> "Some companies find it okay to skip reinforcement learning altogether. For example, Stitch Fix and Grab find that having the reward model alone is good enough for their applications. They get their models to generate multiple outputs and pick the ones given high scores by their reward models."

The pattern: train a [[RewardModel|reward model]] on [[ComparisonData|comparison data]], generate multiple candidates per query, pick the highest-RM-scoring one (the **[[bestofn|best-of-N]] + RM** pattern). Skip the PPO/DPO step.

## Why this matters to the wiki

Grab and [[StitchFix|Stitch Fix]] together provide Huyen's transition from the preference-finetuning section to the [[TestTimeCompute|test-time compute]] section. Their production use illustrates that **a reward model alone — without RL — is a usable production artifact**.

## Connections
- [[StitchFix]] — peer "skip-the-RL" example in Ch 2.
- [[Nextdoor]] — peer reward-model production user.
- [[bestofn]] — the inference-time pattern.
- [[RewardModel]] — the kept artifact.
- [[rlhf]] — the full pipeline shortcut.
- [[ai-engineering-ch02-foundation-models]] — primary source.
