---
title: "Parameter Sharing (Tied Weights)"
type: concept
tags: [deep-learning, framework, d2l, weight-sharing]
sources: [d2l-builders-guide]
last_updated: 2026-05-16
---

# Parameter Sharing / Tied Weights

Multiple layers (or multiple positions in a forward pass) sharing the **same** parameter tensor — not merely equal values, but *the same object* in memory. Created by reusing the same module instance in multiple positions ([[d2l-builders-guide]] §`parameters.md` → Tied Parameters).

## Mechanism

```python
shared = nn.LazyLinear(8)
net = nn.Sequential(
    nn.LazyLinear(8), nn.ReLU(),
    shared, nn.ReLU(),
    shared, nn.ReLU(),
    nn.LazyLinear(1))
```

The same `shared` instance occupies positions 2 and 4. Mutating `net[2].weight.data[0,0] = 100` also mutates `net[4].weight.data[0,0]` — `print(net[2].weight.data[0] == net[4].weight.data[0])` returns all-True.

## Gradients add

When parameters are tied, **gradients from every location where the parameter appears are summed** during the single backward pass — a direct consequence of how [[Autograd|autograd]] traverses the computational graph. No special bookkeeping needed.

## Where it shows up in practice

| Use | Tying pattern |
|---|---|
| [[CNN|Convolutional layers]] | the kernel is shared across all spatial positions — translation equivariance is parameter tying. |
| [[RNN|RNNs]] | the recurrent matrix is shared across all timesteps. |
| Transformer **input ↔ output embedding** | weight matrix tied between token embedding and final softmax projection ([[1706.03762-attention-is-all-you-need|Vaswani et al.]]). |
| Siamese / contrastive networks | the encoder is shared across both branches. |
| Autoencoders (sometimes) | decoder weights = encoder weights transposed. |

## Why tie weights

- **Sample efficiency** — fewer effective parameters mean less data to learn them.
- **Inductive bias** — translation / temporal invariance baked into the architecture.
- **Memory footprint** — one tensor, not many.
- **Faster training** — gradient signal accumulates from all use sites.

## Lazy-init gotcha

[[d2l-builders-guide]] notes: with [[LazyInitialization|lazy modules]], you must run a forward pass `net(X)` **before** accessing tied parameters, because lazy modules have not allocated their tensors yet.

## Framework note

- [[TensorFlow]] / Keras *removes the duplicate*: a `Sequential` containing the same layer twice ends up with `len(net.layers) == 3` (not 4) — Keras deduplicates instead of preserving the multi-reference.
- [[PyTorch]] / [[MXNet]] / [[JAX]] preserve the multi-reference semantics described above.

## Connections

- [[d2l-builders-guide]] — §Tied Parameters canonical reference.
- [[NeuralNetworkModule]] — the substrate.
- [[ParameterAccess]] — how to verify tying.
- [[Parameter]] — what is being shared.
- [[CNN]] — translation-equivariance as parameter sharing.
- [[RNN]] — temporal parameter sharing.
- [[transformer|Transformer]] — embedding↔softmax tying.
- [[Autograd]] — explains why gradients add naturally.
