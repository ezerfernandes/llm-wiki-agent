---
title: "Positional Encoding"
type: concept
tags: [transformer, embeddings]
sources: [1706.03762-attention-is-all-you-need, d2l-attention-and-transformers, hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Positional Encoding

Because the [[Transformer]] contains no recurrence and no convolution, it has no built-in notion of token order. [[1706.03762-attention-is-all-you-need]] introduces *positional encodings* — vectors of dimension d_model that are **added** to the input embeddings at the bottom of both the encoder and decoder stacks.

## Sinusoidal definition

The original paper uses sine and cosine functions of geometrically progressing wavelengths:

```
PE(pos, 2i)   = sin(pos / 10000^(2i / d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i / d_model))
```

where `pos` is the absolute position in the sequence and `i` indexes the encoding dimension. Wavelengths form a geometric progression from 2π up to 10000·2π.

The chosen form is motivated by an algebraic identity: for any fixed offset k, `PE(pos+k)` can be expressed as a linear function of `PE(pos)`. The hypothesis is that this makes it easy for the model to learn to attend by *relative* position.

## Sinusoidal vs. learned

[[1706.03762-attention-is-all-you-need]] also tested learned positional embeddings (Table 3, row E) and found "nearly identical" results. Sinusoidal encoding is preferred for one extrapolation reason: it may allow the model to handle sequence lengths longer than those seen during training, since the encoding generalizes to any position.

This finding has aged: many later models use learned positional embeddings or rotary position embeddings (RoPE), but the additive injection of position into token representations remains the dominant pattern.

## See also
- [[Transformer]]
- [[SelfAttention]]
- [[RoPE]] — the modern relative-aware rotary scheme.
- [[SequencePacking]] — the training-time pressure that motivated RoPE.

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3 frames the move from **absolute** to **relative-aware** positional encodings as a response to two scaling pressures:

1. **[[SequencePacking|Sequence packing]]** during training. Packing multiple short documents into one fixed-length context makes absolute position labels misleading at document boundaries: *"if Document 50 ... starts at position 50, then we'd be misinforming the model if we tell it that that first token is number 50 ... it would assume there's previous context while in reality the earlier tokens belong to a different and unrelated document."*
2. **Model-scale efficiency**. *"Some challenges arise from such methods when we scale up models, which requires us to find ways to improve their efficiency."*

The chapter's named alternative is **[[RoPE|rotary positional embeddings (RoPE)]]** — *"a method to encode positional information in a way that captures absolute and relative token position information. It is based on the idea of rotating vectors in their embeddings space."* RoPE is **applied at the attention step** (mixed into [[QueryProjection|queries]] and [[KeyProjection|keys]] just before relevance scoring) rather than added once at the input — a structural change from this page's "additive at the bottom of the stack" framing. The wiki's dedicated [[RoPE]] page covers the mechanism in depth.
