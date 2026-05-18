---
title: "Update Gate"
type: concept
tags: [rnn, gru, gating]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Update Gate

One of the two sigmoid gates in a [[GRU|GRU]] cell. Computes $\mathbf{Z}_t = \sigma(\mathbf{X}_t\mathbf{W}_\textrm{xz} + \mathbf{H}_{t-1}\mathbf{W}_\textrm{hz} + \mathbf{b}_\textrm{z}) \in (0,1)^{n\times h}$ and parameterizes the convex combination between the old hidden state and the candidate ([[d2l-recurrent-modern]] §gru):

$$\mathbf{H}_t = \mathbf{Z}_t \odot \mathbf{H}_{t-1} + (1 - \mathbf{Z}_t) \odot \tilde{\mathbf{H}}_t.$$

When $\mathbf{Z}_t \to 1$, the unit retains the old state and *skips* time step $t$ in the dependency chain — information from $\mathbf{X}_t$ is ignored. When $\mathbf{Z}_t \to 0$, the unit fully adopts the new candidate.

D2L mnemonic: "Update gates help capture **long-term** dependencies in sequences" — because skipping time steps lets gradients flow across longer spans without attenuation.

## Equivalence

The GRU's update gate $\mathbf{Z}_t$ jointly plays the role of the [[LSTM|LSTM]]'s [[InputGate|input]] *and* [[ForgetGate|forget]] gates (with the constraint that they sum to 1): $(1-\mathbf{Z}_t)$ behaves like the input gate, $\mathbf{Z}_t$ behaves like the forget gate. This is part of the parameter savings that makes GRU smaller than LSTM.

## See also
- [[GRU]] — host architecture.
- [[ResetGate]] — the other GRU gate.
- [[InputGate]] / [[ForgetGate]] — LSTM analogs subsumed by the update gate.
