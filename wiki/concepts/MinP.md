---
title: "Min-p"
type: concept
tags: [sampling, inference, llm]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Min-p

A sampling strategy where you set **the minimum probability a token must reach to be considered during sampling**. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "A related sampling strategy is min-p, where you set the minimum probability that a token must reach to be considered during sampling."

## How it differs from top-p and top-k

- **[[Topk|Top-k]]**: fixed *count* — always k candidates.
- **[[Topp|Top-p]]**: fixed *cumulative-probability mass* — adaptive count.
- **Min-p**: fixed *absolute probability threshold* — adaptive count, but cut by a floor rather than by accumulation.

Example: if min-p = 0.05, only tokens whose probability is ≥ 5% are considered. For a peaked distribution (one likely token at 0.9), this might admit only 1 token. For a flat distribution (50 tokens at 0.02 each), it might admit none — at which point the implementation falls back to top-k or similar.

## Position in the wiki

Ch 2 mentions min-p only briefly as a "related sampling strategy" to top-p. It's the least-deployed of the three; most production stacks default to combinations of temperature + top-k + top-p.

## Connections
- [[Topp]] — the closest relative.
- [[Topk]] — the fixed-count alternative.
- [[Temperature]] — the logit-rescaling control.
- [[Softmax]] — the operation min-p filters.
- [[ai-engineering-ch02-foundation-models]] — primary source.
