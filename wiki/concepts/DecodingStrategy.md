---
title: "Decoding Strategy"
type: concept
tags: [decoding, inference, generation]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Decoding Strategy

> "The method of choosing a single token from the probability distribution is called the decoding strategy." — [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

At the end of every Transformer LLM forward pass, the [[LMHead|LM head]] outputs a logit (and after softmax, a probability) for every token in the vocabulary. The **decoding strategy** is the rule for picking the actual emitted token from that distribution.

## Two regimes

1. **[[GreedyDecoding|Greedy decoding]]**. Always pick the highest-probability token. *"Choosing the highest scoring token every time is called greedy decoding. It's what happens if you set the temperature parameter to zero in an LLM."* — Ch 3.
2. **[[Sampling|Sampling]]**. Pick a token according to its probability (so a token with 40% probability has a 40% chance of being picked, etc.). Adds randomness; usually produces better outputs for open-ended generation. *"In practice, [greedy decoding] doesn't tend to lead to the best outputs for most use cases. A better approach is to add some randomness and sometimes choose the second or third highest probability token."* — Ch 3.

## Per-step, not per-sequence

The decoding strategy is applied **once per generated token**: each token is selected from its own forward-pass distribution. Ch 3 forward-references Ch 6 for the deeper coverage of [[Temperature|temperature]], [[TopK|top-k]], [[TopP|top-p (nucleus)]], and other sampling variants.

## See also

- [[GreedyDecoding]] — the degenerate case.
- [[Sampling]] — the alternative.
- [[Temperature]] / [[BeamSearch]] / [[TopK]] / [[TopP]] — variants and configurations.
- [[LMHead]] — the layer that produces the distribution decoding strategy operates on.
- [[Softmax]] — the operation that turns logits into a probability distribution.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
