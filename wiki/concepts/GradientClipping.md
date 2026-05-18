---
title: "Gradient Clipping"
type: concept
tags: [optimization, neural-networks, rnn, training]
sources: [d2l-recurrent-neural-networks]
last_updated: 2026-05-16
---

# Gradient Clipping

A simple heuristic for mitigating [[ExplodingGradient|exploding gradients]] during training: **project the gradient onto a ball of radius $\theta$** before applying the optimizer step ([[d2l-recurrent-neural-networks]] §rnn-scratch). Indispensable for training [[RNN|RNNs]] and useful for [[transformer|Transformer]] training too.

## The rule

$$\mathbf{g} \leftarrow \min\!\left(1, \frac{\theta}{\|\mathbf{g}\|}\right) \mathbf{g}.$$

If $\|\mathbf{g}\|\leq\theta$, leave $\mathbf{g}$ alone. Otherwise rescale so $\|\mathbf{g}\|=\theta$. Direction is preserved, magnitude is capped.

## Why it works

Recall the SGD step $\mathbf{x} \gets \mathbf{x} - \eta \mathbf{g}$. For an $L$-Lipschitz objective, the change in $f$ is bounded by $L\eta\|\mathbf{g}\|$. When $\|\mathbf{g}\|$ explodes (which happens routinely in BPTT for long sequences — see [[BPTT]] gradient analysis), a single step can undo thousands of training iterations' worth of progress. Clipping caps $\|\mathbf{g}\|\leq\theta$ and thus caps the per-step damage.

Lowering the learning rate $\eta$ instead has the same upper-bound effect but slows down progress at *every* step — undesirable when large gradients are rare events.

## Implementation

Flatten **all** model parameters into a single concatenated gradient vector for the norm computation:

```python
params = [p for p in model.parameters() if p.requires_grad]
norm = torch.sqrt(sum((p.grad ** 2).sum() for p in params))
if norm > grad_clip_val:
    for p in params:
        p.grad[:] *= grad_clip_val / norm
```

D2L trains with `gradient_clip_val=1`.

## Honest assessment

> "To be clear, it is a hack. Gradient clipping means that we are not always following the true gradient and it is hard to reason analytically about the possible side effects. However, it is a very useful hack, and is widely adopted in RNN implementations in most deep learning frameworks." — [[d2l-recurrent-neural-networks]]

Side benefit: limits the influence any single minibatch / sample can exert on parameter updates, contributing a modicum of robustness.

## Connections

- [[d2l-recurrent-neural-networks]] — exposition + framework code (§rnn-scratch).
- [[ExplodingGradient]] — the pathology this addresses.
- [[BPTT]] / [[TruncatedBPTT]] — companion mechanisms in RNN training.
- [[RNN]] / [[LSTM]] / [[GRU]] — primary use case.
- [[StochasticGradientDescent]] / [[Adam]] — applied on top of the gradient *before* the optimizer step.
