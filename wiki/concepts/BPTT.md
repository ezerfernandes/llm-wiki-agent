---
title: "BPTT"
type: concept
tags: [optimization, neural-networks, rnn, training]
sources: [d2l-recurrent-neural-networks]
last_updated: 2026-05-16
---

# BPTT (Backpropagation Through Time)

The application of **[[Backpropagation|backpropagation]] to sequence models with a hidden state** (Werbos 1990). [[BPTT]] unrolls the [[RNN]]'s computational graph one time step at a time and applies the chain rule to the resulting feedforward network — with the special property that the **same parameters** appear at *every* time step, so gradients with respect to a tied parameter are *summed* across all places it occurs ([[d2l-recurrent-neural-networks]] §bptt).

## Setup

For an RNN with hidden state $\mathbf{h}_t$, output $\mathbf{o}_t$, and parameters $w_\textrm{h}$ (hidden-layer) and $w_\textrm{o}$ (output-layer):

$$\frac{\partial L}{\partial w_\textrm{h}} = \frac{1}{T}\sum_{t=1}^T \frac{\partial l(y_t, o_t)}{\partial o_t} \frac{\partial g(h_t, w_\textrm{o})}{\partial h_t} \frac{\partial h_t}{\partial w_\textrm{h}}.$$

The third factor is recursive: $h_t$ depends on $h_{t-1}$ which depends on $w_\textrm{h}$. Expanding gives a sum of $\mathcal{O}(T)$ terms.

## Why it is hard

For a $T$-step sequence the gradient computation involves $\mathcal{O}(T)$ matrix products. A 1000-token input passes through ~1000 matmuls *both* forward and backward. Worse, the closed-form gradient

$$\frac{\partial L}{\partial \mathbf{h}_t}= \sum_{i=t}^T {\left(\mathbf{W}_\textrm{hh}^\top\right)}^{T-i} \mathbf{W}_\textrm{qh}^\top \frac{\partial L}{\partial \mathbf{o}_{T+t-i}}$$

contains powers of $\mathbf{W}_\textrm{hh}^\top$. Eigenvalues $|\lambda|<1$ vanish; $|\lambda|>1$ explode → [[VanishingGradient|vanishing]] / [[ExplodingGradient|exploding]] gradients.

## Mitigations

- **[[TruncatedBPTT|Truncated BPTT]]** — terminate the recursion after $\tau$ steps (Jaeger 2002). What every framework actually does.
- **[[GradientClipping]]** — project the gradient onto a $\theta$-ball.
- **[[LSTM]] / [[GRU]] gating** — cell-state additivity preserves gradient flow.
- **Detaching gradients** at chunk boundaries during minibatch training.
- **[[Transformer]] architectures** — sidestep the problem by attending to all positions in parallel rather than sequentially.

## Storage

BPTT caches intermediate forward activations to avoid recomputation on the backward pass; storing $\partial L / \partial \mathbf{h}_t$ is reused for both $\partial L / \partial \mathbf{W}_\textrm{hx}$ and $\partial L / \partial \mathbf{W}_\textrm{hh}$.

## Connections

- [[d2l-recurrent-neural-networks]] — canonical exposition (§bptt).
- [[Backpropagation]] — the general algorithm BPTT specializes.
- [[RNN]] / [[HiddenState]] / [[RecurrentLayer]] — what BPTT trains.
- [[TruncatedBPTT]] / [[GradientClipping]] — practical companions.
- [[VanishingGradient]] / [[ExplodingGradient]] — what BPTT exposes as a structural problem.
- [[LSTM]] / [[GRU]] — gated architectures designed to keep BPTT stable.
