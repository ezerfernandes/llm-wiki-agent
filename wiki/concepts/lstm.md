---
title: "Long Short-Term Memory (LSTM)"
type: concept
tags: [rnn, architecture, foundational]
sources: [1409.3215-seq2seq]
last_updated: 2026-05-10
---

# Long Short-Term Memory (LSTM)

A recurrent neural network architecture introduced by Hochreiter & Schmidhuber (1997) designed to learn long-range temporal dependencies that standard RNNs cannot, by replacing the simple sigmoid update with a gated memory cell.

A plain RNN computes `h_t = sigm(W_hx · x_t + W_hh · h_{t-1})`, which suffers from vanishing gradients across long sequences. The LSTM adds an internal cell state regulated by input, forget, and output gates, letting gradients flow over many timesteps.

## Role in this wiki

[[1409.3215-seq2seq]] uses two stacked 4-layer LSTMs (encoder + decoder), 1000 cells per layer, 384M total parameters, to map English sentences to French. Key empirical findings:

- **Depth helps.** Each added LSTM layer reduced perplexity by ~10%.
- **Exploding gradients are the real risk.** LSTMs do not suffer from *vanishing* gradients but can still explode; the paper clips gradient norm to 5.
- **Source reversal** (mapping `c,b,a → α,β,γ` instead of `a,b,c → α,β,γ`) drops perplexity 5.8 → 4.7 and lifts BLEU 25.9 → 30.6 — interpreted as reducing the "minimal time lag" between aligned tokens.
- **Long sentences are not a structural problem** for an LSTM trained on reversed inputs — contrary to other groups' contemporaneous findings with similar architectures.

## Successor

LSTMs were the default sequence-modeling backbone until [[1706.03762-attention-is-all-you-need]] showed that pure attention is faster to train (O(1) sequential ops per layer vs. O(n) for RNNs) and reaches higher BLEU. Modern LLMs do not use LSTMs.

[[2001.08361-scaling-laws]] (Kaplan et al., 2020) supplies the empirical scaling argument for the displacement: with matched non-embedding parameter counts, LSTMs and Transformers tie on the first ~100 tokens of a 1024-token context, but **LSTMs plateau** while Transformers keep improving across the full context. The per-token loss obeys a power law in context position with a larger exponent for larger Transformers — bigger Transformers exploit long context more effectively, an advantage LSTMs structurally cannot match.

## See also
- [[SeqToSeq]]
- [[EncoderDecoder]]
- [[Transformer]]
