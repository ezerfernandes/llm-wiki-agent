---
title: "Encoder-Decoder"
type: concept
tags: [architecture, sequence-transduction]
sources: [1409.3215-seq2seq, 1706.03762-attention-is-all-you-need, 1910.10683-t5, d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Encoder-Decoder

A high-level pattern for sequence transduction in which one network component (the encoder) maps an input sequence (x_1, …, x_n) to a continuous representation z = (z_1, …, z_n), and a second component (the decoder) generates an output sequence (y_1, …, y_m) one element at a time, conditioning on z and on previously generated outputs.

The pattern was established for end-to-end neural machine translation by [[KyunghyunCho|Cho]] et al. 2014 and [[1409.3215-seq2seq]] (Sutskever, Vinyals & Le, 2014), where both the encoder and the decoder are deep [[LSTM]]s ([[1409.3215-seq2seq]]) or [[GRU|GRUs]] ([[d2l-recurrent-modern]] §encoder-decoder, §seq2seq), and `z` collapses to a single fixed-dimensional vector (the encoder's final hidden state). [[1706.03762-attention-is-all-you-need]] retains the same encoder-decoder framing but removes recurrence entirely: the encoder is a stack of self-attention + FFN blocks, and the decoder is the same with an extra encoder-decoder attention sub-layer per block. The fixed-vector bottleneck of [[1409.3215-seq2seq]] (mitigated there by source-sentence reversal) is structurally resolved by encoder-decoder attention.

## Auto-regressive decoding

> "At each step the model is auto-regressive, consuming the previously generated symbols as additional input when generating the next."

Auto-regression is enforced in two ways inside the Transformer decoder:
1. The output embeddings are offset by one position (each step predicts the next token).
2. Self-attention in the decoder is *masked* — positions cannot attend to subsequent positions. See [[SelfAttention]].

## Three flavors of attention

In an encoder-decoder Transformer, [[MultiHeadAttention]] appears in three different roles:
- **Encoder self-attention.** Queries, keys, values from the previous encoder layer.
- **Decoder self-attention (masked).** Queries, keys, values from the previous decoder layer; future positions masked.
- **Encoder-decoder attention.** Queries from the previous decoder layer; keys and values from the encoder output. Lets every decoder position attend over every encoder position — the long-range cross-modal channel.

## Decoder-only and encoder-only descendants

Modern LLMs split into three families that reuse pieces of this pattern:
- **Decoder-only** (GPT-style): only the masked self-attention stack, used auto-regressively.
- **Encoder-only** ([[bert]]-style): only the encoder stack, used for representation learning.
- **Encoder-decoder** ([[t5]], original Transformer): full structure, used for translation, summarization, and — per [[1910.10683-t5]] — every task once cast in the [[texttotextframework]].

## T5's evidence that encoder-decoder wins

[[1910.10683-t5]] §3.2 compares encoder-decoder, decoder-only LM, [[prefixlm]], and a shared-parameter encoder-decoder under matched compute on text-to-text tasks. **Encoder-decoder with a denoising objective wins on every task**, even though it uses 2P parameters vs P for the single-stack variants — at the *same* computational cost (M FLOPs), because each stack only processes one of the two sequences. Sharing parameters across encoder and decoder preserved most of the performance at half the parameters. The lesson: explicit encoder-decoder cross-attention is a meaningful inductive bias for conditional generation.

## See also
- [[SeqToSeq]]
- [[LSTM]] / [[GRU]]
- [[Transformer]]
- [[SelfAttention]]
- [[MultiHeadAttention]]
- [[d2l-recurrent-modern]] — D2L's textbook abstraction (`EncoderDecoder` base class with `init_state`).
