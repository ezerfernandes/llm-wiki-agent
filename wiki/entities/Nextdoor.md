---
title: "Nextdoor"
type: entity
tags: [company, social-network, ai-application]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Nextdoor

US-based neighborhood-focused social-networking platform. Notable in the wiki because of a [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]] data point: in 2023, Nextdoor reported that **using a [[RewardModel|reward model]] was the key factor in improving their application's performance**.

## The 2023 reward-model result

Per Ch 2:

> "Nextdoor found that using a reward model was the key factor in improving their application's performance (2023)."

Sparse on details in the chapter, but the implication is the same pattern [[StitchFix|Stitch Fix]] and [[Grab|Grab]] use: train an RM on [[ComparisonData|comparison data]], use it to score candidate outputs at inference time, return the highest-scoring one. The "skip-the-RL" pattern.

## Connections
- [[StitchFix]] / [[Grab]] — peer reward-model production users.
- [[bestofn]] — the inference-time pattern Nextdoor likely uses.
- [[RewardModel]] — the named lever for the 2023 quality improvement.
- [[rlhf]] — the full pipeline that Nextdoor (probably) shortcut.
- [[ai-engineering-ch02-foundation-models]] — primary source.
