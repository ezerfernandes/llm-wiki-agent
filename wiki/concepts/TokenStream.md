---
title: "Token Stream"
type: concept
tags: [transformer, architecture]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Token Stream

The **per-position computation track** through a Transformer LLM. Each input token has its own stream — *"Each token is processed through its own stream of computation (with some interaction between them in attention steps)"* ([[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]).

## Properties

- **One stream per input token.** The number of streams equals the [[ContextLength|context length]]; a 4K-context model has 4K streams.
- **Each stream begins with an input vector** — the [[Embedding|token embedding]] plus positional information ([[RoPE|RoPE]] in modern LLMs).
- **Each stream ends with an output vector** of the same [[ModelDimension|model dimension]] (3,072 for [[Phi3Mini|Phi-3-mini]]).
- **Cross-stream interaction happens only in attention sublayers.** The [[FeedForwardNetwork|feedforward]] sublayer processes each stream independently (position-wise FFN). The [[selfattention|self-attention]] sublayer is where streams talk to one another.

## Why we keep all streams when only one is used

> "For text generation, only the output result of the last stream is used to predict the next token. ... You may wonder why we go through the trouble of calculating all the token streams if we're discarding the outputs of all but the last token. The answer is that the calculations of the previous streams are required and used in calculating the final stream. Yes, we're not using their final output vector, but we use earlier outputs (in each Transformer block) in the Transformer block's attention mechanism." — Ch 3

The [[KVCache|KV cache]] is the optimization that exploits this: cache the K and V projections from the previous streams so subsequent decode steps don't recompute them.

## See also

- [[KVCache]] — the caching optimization that exploits stream reuse during decoding.
- [[ContextLength]] — the count of streams the model supports.
- [[ModelDimension]] — the size of each stream's vectors.
- [[selfattention]] — the cross-stream interaction point.
- [[FeedForwardNetwork]] — the per-stream-independent sublayer.
- [[transformer]] — the architecture.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
