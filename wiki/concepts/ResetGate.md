---
title: "Reset Gate"
type: concept
tags: [rnn, gru, gating]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Reset Gate

One of the two sigmoid gates in a [[GRU|GRU]] cell. Computes $\mathbf{R}_t = \sigma(\mathbf{X}_t\mathbf{W}_\textrm{xr} + \mathbf{H}_{t-1}\mathbf{W}_\textrm{hr} + \mathbf{b}_\textrm{r}) \in (0,1)^{n\times h}$ and gates the contribution of the previous hidden state to the candidate hidden state ([[d2l-recurrent-modern]] §gru):

$$\tilde{\mathbf{H}}_t = \tanh(\mathbf{X}_t\mathbf{W}_\textrm{xh} + (\mathbf{R}_t \odot \mathbf{H}_{t-1})\mathbf{W}_\textrm{hh} + \mathbf{b}_\textrm{h}).$$

When $\mathbf{R}_t \to 1$, the candidate update reduces to a vanilla [[RNN|RNN]] step. When $\mathbf{R}_t \to 0$, the previous hidden state is fully ignored and the candidate is a pure MLP on $\mathbf{X}_t$ — a learned mechanism to *reset* the latent state.

D2L mnemonic: "Reset gates help capture **short-term** dependencies in sequences."

## See also
- [[GRU]] — host architecture.
- [[UpdateGate]] — the other GRU gate.
- [[InputGate]] / [[ForgetGate]] / [[OutputGate]] — LSTM analogs.
