---
title: "Lazy Initialization"
type: concept
tags: [deep-learning, framework, d2l, pytorch]
sources: [d2l-builders-guide]
last_updated: 2026-05-16
---

# Lazy Initialization

A framework feature that **defers parameter allocation until the first forward pass**, when the input shape becomes known. Layers declared as `nn.LazyLinear(256)` know only their *output* dimension at construction time; the input dimension and therefore the weight tensor shape are filled in when the model first sees data ([[d2l-builders-guide]] §`lazy-init.md`).

## Why defer

Before lazy init you had to declare `nn.Linear(in_features, out_features)` with **both** dimensions hard-coded. With deep architectures — especially [[CNN|convolutional]] stacks where downstream feature-map shapes depend on input resolution, kernel sizes, strides, and pooling — every modification upstream forced manual recomputation of every downstream `in_features`. Pure bookkeeping pain; a major source of bugs.

## The mechanism

1. At construction, the layer records only the output dimension (e.g. `out_features=256`).
2. No weight tensor is allocated. `print(net[0].weight)` would error before the first forward pass — there is no tensor yet.
3. On `net(X)`, the framework reads `X.shape[-1]`, allocates `weight = Tensor(X.shape[-1], 256)`, runs the default initializer, then proceeds with the computation.
4. Subsequent forward passes reuse the allocated weight; shape mismatches raise an error.

## PyTorch API

```python
net = nn.Sequential(nn.LazyLinear(256), nn.ReLU(), nn.LazyLinear(10))
# net[0].weight  -> UninitializedParameter, error if used directly
X = torch.rand(2, 20)
net(X)                 # this triggers init
net[0].weight.shape    # torch.Size([256, 20])
```

[[PyTorch]] also exposes `LazyConv2d`, `LazyBatchNorm2d`, etc. Outside `Sequential`, the D2L `Trainer.apply_init` helper feeds dummy inputs through the network as a "dry run" to force initialization before the real training loop.

## Cross-framework

| Framework | Status |
|---|---|
| [[PyTorch]] | `nn.LazyLinear`, `LazyConv2d`, … — opt-in. |
| [[MXNet]] | Lazy by default — `net.initialize()` *registers* an init scheme; allocation waits for `net(X)`. |
| [[TensorFlow]] / Keras | Default — `tf.keras.layers.Dense(units)` infers `in_features` on first call. |
| [[JAX]] / Flax | The whole framework is "lazy" — `params = net.init(rng, dummy_X)` always requires a dummy input. |

## Caveats

- **Parameter access before forward pass fails.** Code that calls `net.parameters()` for an optimizer before `net(X)` ran will see `UninitializedParameter` objects.
- **[[ParameterSharing|Tied weights]]** must be configured *after* the first forward pass — the tied tensor does not exist before then.
- **Default initialization fires when shapes are inferred.** Custom init (`net.apply(init_xavier)`) must run after the first forward pass to override defaults.

## Connections

- [[d2l-builders-guide]] — §`lazy-init.md` canonical reference.
- [[NeuralNetworkModule]] — what is being deferred.
- [[ParameterInitialization]] — interacts: lazy first, then optional custom init.
- [[ParameterSharing]] — must come *after* lazy init triggers.
- [[PyTorch]] — `LazyLinear` API.
- [[CNN]] — the architecture family lazy init most dramatically simplifies.
- [[XavierInitialization]] / [[HeInitialization]] — schemes that run automatically on lazy allocation.
