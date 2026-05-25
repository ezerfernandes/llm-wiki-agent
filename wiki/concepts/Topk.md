---
title: "Top-k"
type: concept
tags: [sampling, inference, llm]
sources: [ai-engineering-ch02-foundation-models, hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Top-k

A **sampling strategy that restricts softmax to the top k logits** — picking the next token from only the k most-likely candidates. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "Top-k is a sampling strategy to reduce the computation workload without sacrificing too much of the model's response diversity."

## Why it's computationally cheaper than full sampling

Softmax over a large vocabulary requires two passes over all values: one for $\sum_j e^{x_j}$, one for $e^{x_i} / \sum_j e^{x_j}$ per token. For a language model with vocab ≈100K, this is expensive. **Top-k computes the softmax only over the k highest-logit tokens** — drastically reducing this cost.

## Typical k values

- **k ranges from 50 to 500** in practice — much smaller than a model's vocabulary size.
- Smaller k → more predictable, less creative outputs.
- Larger k → approaches full distributional sampling.

## Trade-off vs [[Topp|top-p]]

- **Top-k**: fixed k regardless of the probability distribution shape.
- **Top-p**: adaptive — k effectively varies depending on the distribution's peakedness.

For a prompt like *"Do you like music? Yes or no."* the optimal k = 2. For *"What's the meaning of life?"* the optimal k is much larger. Top-k uses one fixed value across both situations; top-p adapts.

## Use in practice

Most modern LLM APIs expose both top-k and top-p (and temperature). Common production setting: temperature ≈ 0.7, top-p ≈ 0.9, top-k = 50 — though sensible defaults vary by model and task.

## Connections
- [[Topp]] — the adaptive alternative.
- [[Temperature]] — the orthogonal logit-rescaling control.
- [[Softmax]] — the operation top-k truncates.
- [[GreedyDecoding]] — top-k with k = 1 (argmax).
- [[Logprobs]] — the log-scale probabilities top-k operates on.
- [[ai-engineering-ch02-foundation-models]] — primary source (Huyen Ch 2).
- [[hands-on-llm-ch06-prompt-engineering]] — operational source (Ch 6).

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 frames top-k as the fixed-count counterpart to top-p:

> *"Similarly, the top_k parameter controls exactly how many tokens the LLM can consider. If you change its value to 100, the LLM will only consider the top 100 most probable tokens."* — Ch 6

The framing emphasizes top-k's **predictability** (fixed candidate count) versus top-p's **adaptivity** (candidate count varies by distribution shape).
