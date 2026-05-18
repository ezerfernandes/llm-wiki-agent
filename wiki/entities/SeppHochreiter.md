---
title: "Sepp Hochreiter"
type: entity
tags: [person, researcher, deep-learning, rnn]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Sepp Hochreiter

Austrian computer scientist; co-inventor of the **[[LSTM|Long Short-Term Memory]]** architecture with [[JurgenSchmidhuber|Jürgen Schmidhuber]] (Hochreiter & Schmidhuber 1997). His 1991 Master's thesis (in German, supervised by Schmidhuber) first articulated the **vanishing-gradient problem** in RNNs — the analysis that motivated the LSTM design ([[d2l-recurrent-modern]] §lstm; Bengio et al. 1994 independently formalized the problem in English). Currently head of the Institute for Machine Learning at JKU Linz.

## Why he matters here

- **Vanishing-gradient analysis (1991).** Hochreiter's Master's thesis is the canonical early articulation of why deep / recurrent networks fail to train via backpropagation: $(\mathbf{W}_\textrm{hh}^\top)^k$ eigenvalue powers shrink toward zero. The result was not widely known outside the German-speaking community for years because the thesis was in German.
- **LSTM (1997).** Co-author with Schmidhuber of the paper that defined sequence learning for two decades. The LSTM's [[MemoryCell|memory cell]] with self-connected weight-1 recurrent edge is the structural fix for vanishing gradients ([[d2l-recurrent-modern]] §lstm).

## Connections

- [[JurgenSchmidhuber]] — LSTM co-author and PhD advisor.
- [[LSTM]] — the architecture.
- [[VanishingGradient]] — the problem he diagnosed.
- [[d2l-recurrent-modern]] — D2L's exposition of LSTM cites him as first author.
