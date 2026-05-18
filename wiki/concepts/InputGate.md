---
title: "Input Gate"
type: concept
tags: [rnn, lstm, gating]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Input Gate

One of the three sigmoid gates in an [[LSTM|LSTM]] cell. Computes $\mathbf{I}_t = \sigma(\mathbf{X}_t\mathbf{W}_\textrm{xi} + \mathbf{H}_{t-1}\mathbf{W}_\textrm{hi} + \mathbf{b}_\textrm{i}) \in (0,1)^{n\times h}$ and controls how much of the candidate cell update $\tilde{\mathbf{C}}_t$ enters the [[MemoryCell|memory cell]]'s internal state ([[d2l-recurrent-modern]] §lstm).

Together with the [[ForgetGate|forget gate]], the input gate parameterizes the cell-state update $\mathbf{C}_t = \mathbf{F}_t\odot \mathbf{C}_{t-1} + \mathbf{I}_t\odot \tilde{\mathbf{C}}_t$. When $\mathbf{I}_t\!\to\!0$, no new information is admitted to the cell; when $\mathbf{I}_t\!\to\!1$, the candidate is fully integrated.

## See also
- [[LSTM]] — host architecture.
- [[ForgetGate]] / [[OutputGate]] — the other two LSTM gates.
- [[MemoryCell]] — the gated component.
