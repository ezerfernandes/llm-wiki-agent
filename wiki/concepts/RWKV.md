---
title: "RWKV"
type: concept
tags: [architecture, rnn, transformer-alternative, long-context]
sources: [ai-engineering-ch02-foundation-models, hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# RWKV

An **RNN-based language-model architecture** (Peng et al., 2023) that — unusually for RNNs — **can be parallelized for training**. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], RWKV is one of the two prominent non-transformer architectures (alongside [[StateSpaceModel|SSMs]] like [[Mamba]]) gaining traction as of 2024.

## Why it's interesting

Standard [[RNN|RNNs]] (LSTM, GRU) train sequentially — gradient computation requires unrolling the recurrence through time, which is hard to parallelize across long sequences. RWKV's formulation lets training be parallel while inference can use the standard recurrent form.

## Long-context implication

> "Due to its RNN nature, in theory, it doesn't have the same context length limitation that transformer-based models have." — Ch 2

The same caveat applies as for SSMs: **no context-length limit ≠ strong long-context performance**. Architectural support is necessary but not sufficient.

## Position in the landscape

Ch 2 names two non-transformer architecture families that have gained traction:
- **[[StateSpaceModel|SSMs]]** — S4 → H3 → [[Mamba]] → [[Jamba]]; linear inference scaling.
- **RWKV** — parallel training, RNN-style inference.

Both target the long-context weakness of transformers; both have credible empirical results but neither has displaced the transformer at frontier scale.

## Connections
- [[StateSpaceModel]] / [[Mamba]] / [[Jamba]] — peer transformer alternatives.
- [[transformer|Transformer]] — the dominant architecture.
- [[RNN]] — the legacy architecture family RWKV updates.
- [[ContextLength]] — the dimension RWKV targets.
- [[ai-engineering-ch02-foundation-models]] — primary source.

## In *Hands-On LLMs* Ch 1

[[hands-on-llm-ch01-introduction-to-llms|Ch 1]] cites RWKV (Peng et al., 2023, *"RWKV: Reinventing RNNs for the transformer era"*, arXiv:2305.13048) alongside [[Mamba]] as the 2023 Transformer-alternative pairing:

> "Apart from the widely popular Transformer architecture, new promising architectures have emerged such as Mamba and RWKV. These novel architectures attempt to reach Transformer-level performance with additional advantages, like larger context windows or faster inference." — Ch 1
