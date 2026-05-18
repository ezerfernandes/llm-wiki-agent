---
title: "Kyunghyun Cho"
type: entity
tags: [person, researcher, deep-learning, nlp]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Kyunghyun Cho

South Korean computer scientist; professor at NYU (Courant + CDS) and research scientist at Genentech. Foundational figure in neural machine translation: lead author of **GRU** (Cho et al. 2014) and a co-author of the **encoder-decoder for statistical MT** paper (Cho, van Merriënboer, Gulcehre et al. 2014) that — alongside [[IlyaSutskever|Sutskever]], Vinyals & Le 2014 ([[1409.3215-seq2seq]]) — co-defined the [[SeqToSeq|seq2seq]] paradigm.

## Why he matters here

- **GRU (2014).** First author of the paper introducing the **gated recurrent unit** — the streamlined LSTM with two gates (reset + update) instead of three, no separate cell state, and comparable accuracy at lower compute ([[d2l-recurrent-modern]] §gru).
- **Encoder-decoder MT (2014).** Cho, van Merriënboer, Gulcehre et al. 2014 introduced the encoder-decoder framing where the encoder maps the source into a fixed-shape context vector $\mathbf{c}$ that is *broadcast to every decoder time step* — the design [[d2l-recurrent-modern]] §seq2seq adopts (in contrast to [[IlyaSutskever|Sutskever]] et al. who use $\mathbf{c}$ only as the decoder's initial hidden state).
- **Attention precursor.** The fixed-$\mathbf{c}$ bottleneck of the Cho-style encoder-decoder motivated Bahdanau, Cho & Bengio 2014's attention mechanism — the structural fix that later generalizes into the [[Transformer|Transformer]].

## Connections

- [[GRU]] — the architecture Cho introduced.
- [[EncoderDecoder]] / [[SeqToSeq]] — the design pattern.
- [[1409.3215-seq2seq]] — contemporaneous parallel work by Sutskever et al.
- [[IlyaSutskever]] — co-defining the seq2seq paradigm.
- [[Attention]] — Bahdanau / Cho / Bengio 2014 follow-up.
- [[d2l-recurrent-modern]] — D2L cites Cho as the GRU lead.
