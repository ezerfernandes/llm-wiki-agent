---
title: "Stitch Fix"
type: entity
tags: [company, retail, ai-application]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Stitch Fix

US-based online personal-styling and apparel-retail company. Notable in the wiki because of [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]'s framing of Stitch Fix as **one of the canonical "skip the RL step" production examples** in [[rlhf|RLHF]] / preference finetuning.

## What they do with LLMs (per Ch 2)

> "Some companies find it okay to skip reinforcement learning altogether. For example, Stitch Fix and Grab find that having the reward model alone is good enough for their applications. They get their models to generate multiple outputs and pick the ones given high scores by their reward models."

This is the **[[bestofn|best-of-N]] + reward-model pattern**: train an RM on [[ComparisonData|comparison data]], then at inference time generate multiple candidate outputs and return the highest-RM-scored one — without the PPO/DPO step that traditional RLHF does.

## Why the pattern works for Stitch Fix

The pattern works best when:
- The task has **verifiable or scoreable correctness** — a fashion/styling recommendation can be scored against existing customer preferences.
- The cost of inference is acceptable compared to the cost/complexity of full RLHF.
- The application benefits from output diversity more than from a single tightly-tuned policy.

## Connections
- [[Grab]] — peer "skip-the-RL" example in Ch 2.
- [[Nextdoor]] — peer reward-model production user.
- [[bestofn]] — the inference-time pattern Stitch Fix uses.
- [[RewardModel]] — the artifact they keep from the RLHF pipeline.
- [[rlhf]] — the full pipeline they shortcut.
- [[ai-engineering-ch02-foundation-models]] — primary source.
