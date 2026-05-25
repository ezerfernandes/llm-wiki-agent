---
title: "Thomas Scialom"
type: entity
tags: [person, meta, llm, llama]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Thomas Scialom

Researcher at [[meta|Meta]] — **author on the Llama 2 paper**. Notable in the wiki for one specific data point in [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]] regarding the cost of [[ComparisonData|comparison data]] for [[rlhf|RLHF]].

## The data point

In a talk with [[ChipHuyen|Chip Huyen]]'s Discord community, Scialom shared:

> "Each comparison cost them $3.50. This is still much cheaper than writing responses, which cost $25 each."

So:
- **~$3.50 per (prompt, winner, loser) comparison triple.**
- **~$25 per written (prompt, response) demonstration.**

The comparison-vs-write cost ratio (~7×) is the practitioner-grade quantification of why **comparison-based [[rlhf|RLHF]] / [[DPO|DPO]] preference data is more scalable than full SFT-style demonstrations** at the preference-finetuning stage.

## Connections
- [[meta|Meta]] — employer.
- [[rlhf]] — the algorithm Scialom's data points concern.
- [[ComparisonData]] — the data format Scialom priced.
- [[Llama2_7BChat|Llama 2]] — the model family Scialom is a co-author on.
- [[ai-engineering-ch02-foundation-models]] — primary source.
