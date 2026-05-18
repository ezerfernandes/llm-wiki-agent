---
title: "Output Gate"
type: concept
tags: [rnn, lstm, gating]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Output Gate

One of the three sigmoid gates in an [[LSTM|LSTM]] cell. Computes $\mathbf{O}_t = \sigma(\mathbf{X}_t\mathbf{W}_\textrm{xo} + \mathbf{H}_{t-1}\mathbf{W}_\textrm{ho} + \mathbf{b}_\textrm{o}) \in (0,1)^{n\times h}$ and controls how much of the cell's internal state $\tanh(\mathbf{C}_t)$ is exposed as the hidden state $\mathbf{H}_t = \mathbf{O}_t \odot \tanh(\mathbf{C}_t)$ ([[d2l-recurrent-modern]] §lstm).

Whenever $\mathbf{O}_t \to 0$, the cell can accumulate information *without* impacting other layers of the network. When the output gate then flips toward 1 at a later time step, the accumulated cell state suddenly influences downstream computation — a learned mechanism for delayed-impact memory.

## See also
- [[LSTM]] — host architecture.
- [[InputGate]] / [[ForgetGate]] — the other two LSTM gates.
- [[MemoryCell]] — the gated component.
