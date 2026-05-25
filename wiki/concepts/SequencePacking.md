---
title: "Sequence Packing"
type: concept
tags: [training, efficiency, transformer]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Sequence Packing

A **training-time efficiency technique** that combines multiple short training documents into one fixed-length context window, minimizing wasted padding at the end of the context.

> "Packing is the process of efficiently organizing short training documents into the context. It includes grouping multiple documents in a single context while minimizing the padding at the end of the context." — [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

## Why it exists

> "One challenge in efficiently training models with large context is that a lot of documents in the training set are much shorter than that context. It would be inefficient to allocate the entire, say, 4K context to a short 10-word sentence." — Ch 3

Without packing, a 4K-context training batch processing a 10-word document wastes ~4,090 tokens of compute on padding. Packing fills the context with multiple short documents back-to-back, so most token positions correspond to real training signal.

## Citations from Ch 3

- *"Efficient sequence packing without cross-contamination: Accelerating large language models without impacting performance."*
- Graphcore — *"Introducing packed BERT for 2X training speed-up in natural language processing."*

## Why it motivates relative-aware positional encodings

> "If Document 50, for example, starts at position 50, then we'd be misinforming the model if we tell it that that first token is number 50 and that would affect its performance (because it would assume there's previous context while in reality the earlier tokens belong to a different and unrelated document the model should ignore)." — Ch 3

This is the primary practical pressure that pushed modern LLMs toward **relative-aware positional schemes** like [[RoPE|rotary positional embeddings (RoPE)]] — packed sequences make absolute positions meaningless across document boundaries.

## See also

- [[RoPE]] — the relative-aware positional encoding sequence packing motivates.
- [[positionalencoding]] — the umbrella concept.
- [[ContextLength]] — the resource sequence packing makes efficient use of.
- [[transformer]] — the architecture.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
