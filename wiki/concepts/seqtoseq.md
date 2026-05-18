---
title: "Sequence-to-Sequence Learning"
type: concept
tags: [architecture, foundational, machine-translation]
sources: [1409.3215-seq2seq, d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Sequence-to-Sequence Learning (seq2seq)

A framework for mapping variable-length input sequences to variable-length output sequences using a pair of neural networks: an **encoder** that reads the input and produces a fixed-dimensional vector representation `v`, and a **decoder** that emits the output sequence one token at a time, conditioned on `v` and all previously emitted tokens.

Introduced in [[1409.3215-seq2seq]] (Sutskever, Vinyals & Le, 2014) with LSTM encoders and decoders. The framing factors the conditional probability as

```
p(y₁,…,y_{T'} | x₁,…,x_T) = ∏_{t=1..T'} p(y_t | v, y₁,…,y_{t-1})
```

The end-of-sequence token `<EOS>` lets the model define a distribution over outputs of any length.

## Why it matters

- **Generality.** No assumption about alignment, monotonicity, or length ratio between input and output — applies to translation, summarization, question answering, dialog, code generation.
- **First neural win on MT.** [[1409.3215-seq2seq]] was the first pure neural system to beat a phrase-based SMT baseline on a large MT task (WMT'14 EN→FR, BLEU 34.81 vs. 33.30).
- **Architectural template.** The encoder-decoder pattern survives unchanged in [[1706.03762-attention-is-all-you-need]]; only the recurrent backbone is replaced by [[SelfAttention]].

## Limitation: the fixed-vector bottleneck

Compressing the entire input into a single fixed-dimensional vector becomes harder as sentences grow. [[1409.3215-seq2seq]] mitigates this with the **source-reversal trick** (reverse input word order to introduce short-term dependencies). Bahdanau et al. 2014 introduced attention as a structural fix: instead of one summary vector, the decoder learns to attend over the full sequence of encoder hidden states. The Transformer ([[1706.03762-attention-is-all-you-need]]) generalizes this to pure attention with no recurrence.

## Two flavors of context plumbing

D2L's [[d2l-recurrent-modern]] §seq2seq distinguishes two designs for how the encoder's final hidden state $\mathbf{c}$ reaches the decoder:

- **[[KyunghyunCho|Cho]]-style (Cho et al. 2014; D2L's implementation):** broadcast $\mathbf{c}$ as additional input at *every* decoder time step (concatenate with each input embedding).
- **[[IlyaSutskever|Sutskever]]-style ([[1409.3215-seq2seq]]):** use $\mathbf{c}$ only to initialize the decoder's hidden state at step 1; subsequent steps see only the previous token + decoder state.

Both work; the Cho-style design tends to be more robust to long sequences but doubles the decoder's input dimensionality. Both are structurally bottlenecked by $\mathbf{c}$'s fixed shape — the bottleneck attention was invented to remove.

## See also
- [[EncoderDecoder]]
- [[LSTM]] / [[GRU]]
- [[BeamSearch]] / [[GreedyDecoding]]
- [[TeacherForcing]] — the training-time recipe.
- [[Transformer]]
- [[d2l-recurrent-modern]] — textbook GRU-based implementation.
