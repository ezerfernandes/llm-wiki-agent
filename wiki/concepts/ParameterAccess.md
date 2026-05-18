---
title: "Parameter Access"
type: concept
tags: [deep-learning, framework, d2l]
sources: [d2l-builders-guide]
last_updated: 2026-05-16
---

# Parameter Access

The set of API patterns by which a [[NeuralNetworkModule|module]] exposes its learnable [[Parameter|Parameters]] — for diagnostics, custom initialization, weight visualization, gradient inspection, or serialization ([[d2l-builders-guide]] §`parameters.md`).

## The three modes

| Mode | PyTorch | When |
|---|---|---|
| **Indexed** | `net[2].state_dict()` | one layer of a `Sequential` |
| **Named tree** | `[(n, p.shape) for n,p in net.named_parameters()]` | walk *all* parameters with hierarchical names |
| **Flat list** | `list(net.parameters())` | bulk handover to an optimizer |

## Each parameter is a *complex object*

Not a bare tensor — it carries `data` (the value) **and** `grad` (the gradient; `None` until backward is called).

```python
net[2].bias.data      # the bias tensor
net[2].weight.grad    # None before .backward()
```

This is why custom init writes to `module.weight.data` (not `module.weight`) and why `nn.Parameter(torch.randn(...))` wraps a tensor — the wrapper is what makes it tracked.

## Cross-framework analogues

| Framework | "All parameters" |
|---|---|
| [[PyTorch]] | `net.named_parameters()` |
| [[MXNet]] | `net.collect_params()` |
| [[TensorFlow]] | `net.get_weights()` |
| [[JAX]] / Flax | `jax.tree_util.tree_map(lambda x: x.shape, params)` |

Flax / JAX is the outlier: the model and the parameters are **decoupled** — `params` is a plain `FrozenDict` returned by `net.init(rng, X)`, not stored inside the module.

## Why this matters

- **Custom init** — `net.apply(init_xavier)` walks `named_parameters()` to find what to initialize.
- **Optimizer hookup** — `torch.optim.SGD(net.parameters(), lr=0.01)` passes the flat list.
- **Diagnostics** — shape audits ("did my layer get the dim I expected?") and gradient sanity checks during debugging.
- **Selective freezing** — set `param.requires_grad = False` on a subset for [[TransferLearning|transfer learning]] / [[adapterlayers|adapter]] fine-tuning.

## Connections

- [[d2l-builders-guide]] — §`parameters.md` canonical reference.
- [[NeuralNetworkModule]] — the abstraction parameters live inside.
- [[Parameter]] — the wrapped-tensor class.
- [[ParameterSharing]] — tying parameters across modules.
- [[ParameterInitialization]] — what `apply()` operates on.
- [[StateDict]] — the serialized form of all named parameters.
- [[Autograd]] — provider of `.grad`.
