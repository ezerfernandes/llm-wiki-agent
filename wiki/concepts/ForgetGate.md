---
title: "Forget Gate"
type: concept
tags: [rnn, lstm, gating]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Forget Gate

One of the three sigmoid gates in an [[LSTM|LSTM]] cell. Computes $\mathbf{F}_t = \sigma(\mathbf{X}_t\mathbf{W}_\textrm{xf} + \mathbf{H}_{t-1}\mathbf{W}_\textrm{hf} + \mathbf{b}_\textrm{f}) \in (0,1)^{n\times h}$ and controls how much of the previous cell state $\mathbf{C}_{t-1}$ is preserved into $\mathbf{C}_t$ ([[d2l-recurrent-modern]] §lstm).

Cell-state update: $\mathbf{C}_t = \mathbf{F}_t\odot \mathbf{C}_{t-1} + \mathbf{I}_t\odot \tilde{\mathbf{C}}_t$. When $\mathbf{F}_t \to 1$ (and [[InputGate|input gate]] $\to 0$), the cell carries state unchanged across many time steps — the structural mechanism that defeats [[VanishingGradient|vanishing gradients]] in [[LSTM|LSTMs]]. When $\mathbf{F}_t \to 0$, the cell is "flushed" and forgets its prior content.

## Historical note

The forget gate was *not* in the original Hochreiter & Schmidhuber 1997 LSTM design; it was added by Gers, Schmidhuber & Cummins 2000 ("Learning to forget"). Modern LSTM implementations universally include it.

## See also
- [[LSTM]] — host architecture.
- [[InputGate]] / [[OutputGate]] — the other two LSTM gates.
- [[MemoryCell]] — the gated component.
- [[VanishingGradient]] — the problem the forget gate (set to 1) avoids.
