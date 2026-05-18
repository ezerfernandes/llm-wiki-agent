---
title: "Parameter (nn.Parameter)"
type: concept
tags: [deep-learning, framework, d2l, pytorch]
sources: [d2l-builders-guide]
last_updated: 2026-05-16
---

# Parameter (`nn.Parameter`)

A *tracked* learnable tensor — a thin wrapper around `torch.Tensor` that signals to the framework "this is a model weight, please discover it, initialize it, save it, move it with the model, and optimize it" ([[d2l-builders-guide]] §`custom-layer.md`).

## Why a wrapper

A bare `self.weight = torch.randn(d, k)` inside an `nn.Module.__init__` would silently fail to appear in `named_parameters()`, would not be moved by `net.to(device)`, would not be serialized by `state_dict()`, and would not receive gradients. Wrapping with `nn.Parameter(...)` is the registration mechanism:

```python
class MyLinear(nn.Module):
    def __init__(self, in_units, units):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(in_units, units))  # tracked
        self.bias   = nn.Parameter(torch.randn(units))             # tracked
        self.const  = torch.rand(units)                            # NOT tracked
```

The `const` tensor exists, computes, but is invisible to the optimizer — useful for the "constant parameters" pattern ([[d2l-builders-guide]] `FixedHiddenMLP`).

## What it carries

| Attribute | Meaning |
|---|---|
| `param.data` | the underlying tensor value |
| `param.grad` | the gradient accumulator (`None` until backward) |
| `param.requires_grad` | flag; flip to `False` to freeze the parameter |

## Cross-framework analogues

| Framework | Wrapper |
|---|---|
| [[PyTorch]] | `nn.Parameter(tensor)` |
| [[MXNet]] | `self.params.get(name, shape=...)` |
| [[TensorFlow]] | `self.add_weight(name, shape, initializer)` |
| [[JAX]] / Flax | `self.param(name, init_fn, shape)` |

## Connections

- [[d2l-builders-guide]] — §`custom-layer.md` canonical reference.
- [[NeuralNetworkModule]] — the container.
- [[ParameterAccess]] — how to walk them.
- [[ParameterSharing]] — what happens when the same `Parameter` is referenced twice.
- [[ParameterInitialization]] — how their values get assigned.
- [[StateDict]] — what they show up in.
- [[Autograd]] — how `.grad` is populated.
- [[CustomLayer]] — where you typically allocate them.
