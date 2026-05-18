---
title: "Positional Encoding"
type: concept
tags: [transformer, embeddings]
sources: [1706.03762-attention-is-all-you-need, d2l-attention-and-transformers]
last_updated: 2026-05-16
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
