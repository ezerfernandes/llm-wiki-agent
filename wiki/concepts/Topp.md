---
title: "Top-p (Nucleus Sampling)"
type: concept
tags: [sampling, inference, llm]
sources: [ai-engineering-ch02-foundation-models, hands-on-llm-ch06-prompt-engineering, agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
---

# Top-p (Nucleus Sampling)

A **sampling strategy that adapts the number of candidate tokens to the shape of the distribution** by summing probabilities in descending order and stopping when the cumulative sum reaches p. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "In top-p sampling, the model sums the probabilities of the most likely next values in descending order and stops when the sum reaches p. Only the values within this cumulative probability are considered."

Also called **nucleus sampling** (Holtzman et al. 2019).

## Why "adaptive" matters

[[Topk|Top-k]] uses a fixed k regardless of the distribution shape. But the optimal number of candidate tokens varies by context:

- *"Do you like music? Yes or no."* → 2 candidates is enough.
- *"What's the meaning of life?"* → many candidates should be considered.

Top-p naturally varies the number of candidates depending on how peaked the distribution is. Common p values: **0.9 to 0.95**.

## Worked example (Ch 2 Fig 2-18)

Token probabilities: yes 0.7, maybe 0.25, no 0.04, other 0.01.

- **p = 0.9** → "yes" + "maybe" considered (cumulative 0.95 > 0.9).
- **p = 0.99** → "yes" + "maybe" + "no" considered (cumulative 0.99 = 0.99).

## Top-p vs Top-k: cost

Unlike top-k, **top-p doesn't necessarily reduce softmax compute** — you still need full softmax to compute the probability ranks. Its benefit is **contextually appropriate output diversity**, not computational savings.

> "In theory, there don't seem to be a lot of benefits to top-p sampling. However, in practice, top-p sampling has proven to work well, causing its popularity to rise."

## Related: min-p

> "A related sampling strategy is min-p, where you set the minimum probability that a token must reach to be considered during sampling."

## Connections
- [[Topk]] — the fixed-k alternative.
- [[Temperature]] — the orthogonal logit-rescaling control.
- [[Softmax]] — the operation top-p filters.
- [[MinP]] — the related minimum-probability-threshold strategy.
- [[Logprobs]] — the log-scale probabilities top-p sums.
- [[ai-engineering-ch02-foundation-models]] — primary source (Huyen Ch 2).
- [[hands-on-llm-ch06-prompt-engineering]] — operational source (Ch 6).
- [[agentic-design-patterns-appendix-a-prompting]] — Gulli's Appendix A lists top-p among the sampling controls (with [[Temperature|temperature]] / [[Topk|top-k]]) in its experimentation/best-practices guidance.

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 frames top-p operationally:

> *"top_p, also known as nucleus sampling, is a sampling technique that controls which subset of tokens (the nucleus) the LLM can consider. It will consider tokens until it reaches their cumulative probability. If we set top_p to 0.1, it will consider tokens until it reaches that value. If we set top_p to 1, it will consider all tokens."* — Ch 6

The Ch 6 use-case-quadrant table (mapping temperature × top_p to brainstorming / email / creative-writing / translation) lives on the [[Temperature]] page; top_p is one of the two axes.
