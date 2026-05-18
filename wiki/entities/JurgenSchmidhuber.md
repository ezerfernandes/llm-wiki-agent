---
title: "Jürgen Schmidhuber"
type: entity
tags: [person, researcher, deep-learning, rnn]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Jürgen Schmidhuber

German-Swiss computer scientist; co-inventor of the **[[LSTM|Long Short-Term Memory]]** architecture with [[SeppHochreiter|Sepp Hochreiter]] (Hochreiter & Schmidhuber 1997). Long-time director of IDSIA (Lugano) and currently at KAUST. Schmidhuber's group also produced influential follow-up RNN work including connectionist temporal classification (Graves et al.) and LSTM-based phoneme classification ([[d2l-recurrent-modern]] introduction cites Graves & Schmidhuber 2005).

## Why he matters here

- **LSTM (1997).** Senior author of the LSTM paper. The architecture's gated memory cell is the basis for sequence modeling from 2011 until the [[Transformer|Transformer]] era (2017+) ([[d2l-recurrent-modern]] §lstm).
- **Subsequent RNN ecosystem.** Schmidhuber's lab trained Sepp Hochreiter, Felix Gers (LSTM forget gate, 2000), and Alex Graves (CTC, deep bidirectional LSTM for speech/handwriting). Graves & Schmidhuber 2005 demonstrated that bidirectional + LSTM compose well — phoneme classification (Graves & Schmidhuber 2005) and handwriting recognition (Graves 2008).
- **Priority debates.** Schmidhuber has been outspoken about attribution of deep-learning ideas (residual connections, GANs, attention) to earlier RNN work from his group, sometimes contentiously.

## Connections

- [[SeppHochreiter]] — LSTM co-author and Schmidhuber's Master's student.
- [[LSTM]] — the architecture.
- [[BidirectionalRNN]] — Graves & Schmidhuber 2005 combined LSTM + bi-RNN.
- [[d2l-recurrent-modern]] — D2L cites Schmidhuber as senior LSTM author.
