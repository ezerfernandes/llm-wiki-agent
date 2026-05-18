---
title: "Yogi"
type: concept
tags: [optimization, deep-learning]
sources: [d2l-optimization]
last_updated: 2026-05-16
---

# Yogi

Zaheer, Reddi, Sachan, Kale & Kumar 2018 (NeurIPS) — a refinement of [[Adam]] that addresses Adam's known **divergence failure mode** when the second-moment estimate has high variance or sparse updates.

## The problem with Adam

Adam's second-moment update can be rewritten as:

$$\mathbf{s}_t \leftarrow \mathbf{s}_{t-1} + (1-\beta_2)\,(\mathbf{g}_t^2 - \mathbf{s}_{t-1}).$$

When $\mathbf{g}_t^2$ has high variance, the magnitude of $(\mathbf{g}_t^2 - \mathbf{s}_{t-1})$ can be large in either direction — $\mathbf{s}_t$ "forgets" past values too quickly, causing divergence in certain convex settings (Reddi, Kale & Kumar 2019 construct explicit counterexamples) ([[d2l-optimization]] §adam-yogi).

## The Yogi fix

Replace the deviation term with one whose magnitude no longer depends on $(\mathbf{g}_t^2 - \mathbf{s}_{t-1})$:

$$\mathbf{s}_t \leftarrow \mathbf{s}_{t-1} + (1-\beta_2)\,\mathbf{g}_t^2 \odot \textrm{sgn}(\mathbf{g}_t^2 - \mathbf{s}_{t-1}).$$

Now the update step's magnitude is $\mathbf{g}_t^2$ (a stable quantity), and only its *sign* depends on whether $\mathbf{s}_t$ should grow or shrink. The first-moment update is unchanged.

## When to use

Yogi is most relevant for:

- **Sparse gradients** (NLP with rare-word embeddings).
- **Bayesian deep learning** where sample-to-sample gradient variance is intrinsically high.
- **Reinforcement learning** with high-variance return signals.

For standard supervised DL the practical difference is usually small; Adam with appropriate $\beta_2$ tuning typically suffices.

## Connections

- [[d2l-optimization]] — canonical reference (§adam-yogi).
- [[Adam]] — what Yogi refines.
- [[RMSProp]] — Adam's second-moment ancestor that Yogi's update modifies.
- [[StochasticGradientDescent]] — the family.
