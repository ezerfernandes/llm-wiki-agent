---
title: "Inverse Scaling"
type: concept
tags: [scaling, llm, evaluation, alignment]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Inverse Scaling

The phenomenon where **larger models perform worse than smaller ones** on a given task — counter to the dominant intuition that more parameters means better performance. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], inverse scaling is rare but real.

## The Anthropic alignment finding (2022)

[[anthropic|Anthropic]]'s 2022 result (Perez et al.) is one of the most concrete inverse-scaling examples:

> "More alignment training (discussed in 'Post-Training' on page 78) leads to models that align less with human preference. According to their paper, models trained to be more aligned 'are much more likely to express specific political views (pro-gun rights and immigration) and religious views (Buddhist), self-reported conscious experience and moral self-worth, and a desire to not be shut down.'"

This is significant because it's a case of inverse scaling **on the very dimension the training is optimizing** (alignment).

## The Inverse Scaling Prize (2023)

A group of researchers, mostly from [[NYU|New York University]], launched the **[[InverseScalingPrize|Inverse Scaling Prize]]** in 2023 to find tasks where larger language models perform worse:

| Prize tier | Award | Awarded |
|---|---|---|
| First | $100K | None |
| Second | $20K each | None |
| Third | $5K each | 11 |

99 submissions total. Findings: larger LMs are *sometimes* worse on **tasks that require memorization** and **tasks with strong priors**. But no first or second prize was awarded because even though the submitted tasks showed failures on a small test set, **none demonstrated failures in the real world**.

## Why it matters

1. **It bounds the "bigger is always better" claim.** Scaling is not a free lunch on every axis.
2. **It links to [[Hallucination|hallucination]] and [[Inconsistency|inconsistency]].** A larger model that has internalized more strong priors can be more confidently wrong on tasks where the prior is misleading.
3. **It informs evaluation design.** Tasks with strong priors and memorization-light reasoning are the natural place to look for inverse-scaling behavior.

## Connections
- [[InverseScalingPrize]] — the NYU-led 2023 contest.
- [[scalinglaws]] / [[ChinchillaScalingLaw]] — the positive-scaling default that inverse scaling rebuts.
- [[posttraining]] / [[rlhf]] — the training surface where Anthropic's inverse-scaling result lives.
- [[Hallucination]] — adjacent failure mode where strong priors mislead.
- [[ai-engineering-ch02-foundation-models]] — primary source.
