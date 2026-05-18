---
title: "Parameter Initialization (Framework Mechanics)"
type: concept
tags: [deep-learning, framework, d2l, weight-initialization]
sources: [d2l-builders-guide]
last_updated: 2026-05-16
---

# Parameter Initialization (Framework Mechanics)

The *mechanical* side of [[WeightInitialization|weight initialization]] — **how** a framework actually sets the values of every `nn.Parameter` once a module's shape is known ([[d2l-builders-guide]] §`init-param.md`). The mathematical side (Xavier / He / LeCun variance formulas, symmetry breaking, vanishing/exploding gradients) lives at [[WeightInitialization]].

## Three layers of init in PyTorch

1. **Default init at allocation.** Every `nn.Linear` / `nn.LazyLinear` / `nn.Conv2d` ships with a built-in default (PyTorch: `kaiming_uniform_` with $\sqrt{5}$ gain — historical). Triggered automatically when shapes are known, before any user code.
2. **Bulk override via `apply`.** A user-supplied function is walked across every submodule:

   ```python
   def init_normal(m):
       if type(m) == nn.Linear:
           nn.init.normal_(m.weight, mean=0, std=0.01)
           nn.init.zeros_(m.bias)
   net.apply(init_normal)
   ```

3. **Targeted per-layer override.** Apply different inits to different submodules — Xavier on layer 0, constant-42 on layer 2:

   ```python
   net[0].apply(init_xavier)
   net[2].apply(init_42)
   ```

## Built-in initializers

| Family | PyTorch (`torch.nn.init`) | Use |
|---|---|---|
| Normal | `normal_(t, mean, std)` | small-σ Gaussian; classic 0.01-std baseline |
| Constant | `constant_(t, val)` / `zeros_` / `ones_` | bias = 0; debugging |
| Uniform | `uniform_(t, a, b)` | range-bounded |
| [[XavierInitialization\|Xavier]] | `xavier_uniform_` / `xavier_normal_` | tanh / sigmoid nets |
| [[HeInitialization\|Kaiming / He]] | `kaiming_uniform_` / `kaiming_normal_` | ReLU nets |
| Orthogonal | `orthogonal_` | RNN recurrent matrices |

## Custom initializers

A custom initializer is just a Python function that mutates `module.weight.data` in place — there is nothing framework-blessed about it. [[d2l-builders-guide]] demonstrates a three-way mixture (uniform `(5,10)` w.p. ¼ / 0 w.p. ½ / uniform `(-10,-5)` w.p. ¼):

```python
def my_init(m):
    if type(m) == nn.Linear:
        nn.init.uniform_(m.weight, -10, 10)
        m.weight.data *= m.weight.data.abs() >= 5
```

Direct assignment also works: `net[0].weight.data[0, 0] = 42`. Frameworks treat the data tensor as mutable through `.data`.

## Framework defaults

| Framework | Default for `Linear` / `Dense` |
|---|---|
| [[PyTorch]] | `kaiming_uniform_` (He uniform, $\sqrt 5$ gain) |
| [[TensorFlow]] / Keras | `glorot_uniform` ([[XavierInitialization\|Xavier]] uniform) |
| [[JAX]] / Flax | `lecun_normal` |
| [[MXNet]] | $U(-0.07, 0.07)$; switch with `init.Xavier()`, `init.Constant(1)`, etc. |

## Interaction with [[LazyInitialization|lazy init]]

Lazy modules allocate weights only on the first forward pass — at which point the default initializer fires. Custom `apply(init_fn)` must run *after* the first forward pass to override. In [[MXNet]], `net.initialize()` before a forward pass merely *registers* the chosen scheme; the actual draw happens once shapes are inferred.

## JAX / Flax exception

JAX decouples parameters from the network. Initialization happens explicitly:

```python
params = net.init(rng_key, dummy_input)
```

Initializers are functions `(key, shape, dtype) -> array`. The returned `FrozenDict` is immutable — to mutate, call `params.unfreeze()`.

## Connections

- [[d2l-builders-guide]] — §`init-param.md` canonical reference.
- [[WeightInitialization]] — *why* certain variances; the mathematical companion.
- [[XavierInitialization]] / [[HeInitialization]] — the canonical heuristic schemes.
- [[NeuralNetworkModule]] — what `apply()` walks.
- [[Parameter]] — the wrapper init writes through `.data`.
- [[LazyInitialization]] — interaction: default init fires on shape inference.
- [[ParameterAccess]] — `named_parameters()` is how `apply` discovers submodules.
- [[VanishingGradient]] / [[ExplodingGradient]] — the pathologies init prevents.
