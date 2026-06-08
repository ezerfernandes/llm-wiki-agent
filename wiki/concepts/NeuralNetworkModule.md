---
title: "Neural Network Module (Block)"
type: concept
tags: [deep-learning, framework, d2l, abstraction]
sources: [d2l-builders-guide, mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Neural Network Module / Block

The universal abstraction for **any callable piece of a neural network** in modern frameworks. A *module* (PyTorch / Flax terminology) — also called a *Block* ([[MXNet]] Gluon) or a *Model* (Keras) — can represent a single layer, a multi-layer sub-network, or the entire model. [[d2l-builders-guide]] §`model-construction` is the canonical reference.

## The contract

A subclass must provide:

1. A `forward` method (PyTorch / MXNet) or `__call__` / `call` (JAX/Flax / Keras) that maps inputs to outputs.
2. Storage for any learnable [[Parameter|Parameters]] — typically as attributes assigned in `__init__` / `setup`.

In return the framework supplies:

- **Automatic backpropagation** via [[Autograd|automatic differentiation]].
- **Recursive parameter discovery** — submodules assigned to `self.x` are walked by `named_parameters()` / `state_dict()`.
- **`__call__` shorthand** — `net(X)` invokes `net.forward(X)` (plus hooks).
- **Bulk device movement** via `.to(device)`.
- **Initialization apply** via `net.apply(fn)`.
- **Serialization** via `state_dict()`.

## Framework parity table

| Framework | Base class | Forward method |
|---|---|---|
| [[PyTorch]] | `torch.nn.Module` | `forward(self, X)` |
| [[MXNet]] / Gluon | `mxnet.gluon.nn.Block` | `forward(self, X)` |
| [[TensorFlow]] / Keras | `tf.keras.Model` | `call(self, X)` |
| [[JAX]] / Flax | `flax.linen.Module` | `__call__(self, X)` |

## Composition

Modules compose recursively — that is the entire programming model:

```python
class NestMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(nn.LazyLinear(64), nn.ReLU(),
                                 nn.LazyLinear(32), nn.ReLU())
        self.linear = nn.LazyLinear(16)
    def forward(self, X):
        return self.linear(self.net(X))

chimera = nn.Sequential(NestMLP(), nn.LazyLinear(20), FixedHiddenMLP())
```

[[d2l-builders-guide]]: "Individual layers can be modules. Many layers can comprise a module. Many modules can comprise a module."

## Three universal principles ([[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]])

Ch 7 distills the module abstraction (see [[nnModule]]) to three problems every framework solves: (1) **automatic parameter discovery** (metaclass-intercepted assignment + recursive DFS, so `optimizer.step()` updates millions of params in one vectorized call); (2) **mode-dependent behavior** (a single `.eval()` flag propagates `training=False` to switch dropout/batchnorm); (3) **hierarchical composition + serialization** (`state_dict()` flattens to dotted keys for sequential-byte-stream checkpointing). It also stresses the **parameter vs buffer** split: buffers (`register_buffer`) move with the model but get no gradients.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] / [[nnModule]] — the three-principle framing of the module abstraction.
- [[d2l-builders-guide]] — canonical reference for the abstraction.
- [[Module]] — D2L's *training-loop* base class (orthogonal layer above `nn.Module`).
- [[PyTorch]] / [[MXNet]] / [[TensorFlow]] / [[JAX]] — the four frameworks compared.
- [[Parameter]] — what modules store.
- [[ParameterAccess]] — how to walk a module's parameters.
- [[StateDict]] — the serialization output.
- [[Autograd]] — what makes the `forward`-only contract sufficient.
- [[CustomLayer]] — concrete subclassing examples.
- `nn.Sequential` / `tf.keras.Sequential` / `flax.linen.Sequential` — the trivial daisy-chain subclass; re-implemented from scratch in [[d2l-builders-guide]] §`model-construction.md`.
