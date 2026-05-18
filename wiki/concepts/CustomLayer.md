---
title: "Custom Layer"
type: concept
tags: [deep-learning, framework, d2l]
sources: [d2l-builders-guide]
last_updated: 2026-05-16
---

# Custom Layer

A user-defined [[NeuralNetworkModule|module]] implementing a new operation that the framework does not ship — e.g. centering, custom normalization, Fourier-coefficient extraction, dynamic-programming layers, an unusual activation. Built by subclassing the framework's base module class ([[d2l-builders-guide]] §`custom-layer.md`).

## Layers without parameters

The minimum viable layer overrides only `forward`:

```python
class CenteredLayer(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, X):
        return X - X.mean()
```

Drop it into any `Sequential` — `nn.Sequential(nn.LazyLinear(128), CenteredLayer())`. No init, no `state_dict` entries, behaves exactly like `nn.ReLU` or `nn.Flatten`.

## Layers with parameters

Wrap learnable tensors in `nn.Parameter` so the framework discovers, initializes, saves, and moves them:

```python
class MyLinear(nn.Module):
    def __init__(self, in_units, units):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(in_units, units))
        self.bias = nn.Parameter(torch.randn(units,))
    def forward(self, X):
        linear = torch.matmul(X, self.weight.data) + self.bias.data
        return F.relu(linear)
```

`nn.Parameter` is the registration mechanism — assigning a bare `torch.randn(...)` as `self.weight` would *not* register it for `.parameters()`, `.to(device)`, or `state_dict`.

## Cross-framework

| Framework | Parameter wrapper |
|---|---|
| [[PyTorch]] | `nn.Parameter(torch.randn(...))` |
| [[MXNet]] | `self.params.get('weight', shape=(in_units, units))` |
| [[TensorFlow]] | `self.add_weight(name, shape, initializer)` in `build()` |
| [[JAX]] / Flax | `self.param('weight', init_fn, shape)` |

[[TensorFlow]]'s `build()` method is the framework-native lazy-init equivalent — it is called the first time the layer sees data with a known shape.

## Once defined, indistinguishable from built-ins

Custom layers can be composed in `Sequential`, nested inside other modules, used in `apply(init_fn)`, saved by `state_dict`, moved by `.to(device)`. The whole point of the [[NeuralNetworkModule|module abstraction]] is that user code is a first-class citizen.

## Connections

- [[d2l-builders-guide]] — §`custom-layer.md` canonical reference.
- [[NeuralNetworkModule]] — parent abstraction.
- [[Parameter]] — the wrapper that turns a tensor into a tracked weight.
- [[ParameterInitialization]] — how custom-layer weights get initialized.
- [[LazyInitialization]] — Keras `build()` is structurally similar.
- `CenteredLayer` — D2L's canonical no-parameter example (`X - X.mean()`), defined inline in [[d2l-builders-guide]] §`custom-layer.md`.
- [[BatchNormalization]] — real-world custom-layer-with-state archetype.
