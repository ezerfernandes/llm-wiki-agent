---
title: "Xavier Initialization"
type: concept
tags: [weight-initialization, training, deep-learning]
sources: [d2l-multilayer-perceptrons, d2l-convolutional-neural-networks]
last_updated: 2026-05-16
---

# Xavier Initialization

Also called *Glorot initialization*. A [[WeightInitialization|weight-initialization]] heuristic that samples each weight from a zero-mean distribution with variance

$$\sigma^2 = \frac{2}{n_\text{in} + n_\text{out}}$$

so the variance of layer **outputs** is preserved forward *and* the variance of **gradients** is preserved backward. Introduced by [[XavierGlorot|Glorot]] & [[YoshuaBengio|Bengio]] (2010); now the standard initialization for symmetric activations like [[Tanh|tanh]] ([[d2l-multilayer-perceptrons]] §Xavier Initialization).

## Derivation in one paragraph

For a fully-connected unit $o_i = \sum_{j=1}^{n_\text{in}} w_{ij}x_j$ with IID zero-mean $w_{ij}$ (variance $\sigma^2$) and IID zero-mean $x_j$ (variance $\gamma^2$), $\mathrm{Var}[o_i] = n_\text{in}\sigma^2\gamma^2$. Keeping $\mathrm{Var}[o_i] = \gamma^2$ forward needs $n_\text{in}\sigma^2 = 1$; preserving gradient variance backward needs $n_\text{out}\sigma^2 = 1$. The two cannot hold simultaneously, so Xavier targets the *average*: $\tfrac12(n_\text{in} + n_\text{out})\sigma^2 = 1$.

## Distribution flavours

- **Gaussian:** $\mathcal{N}(0,\, 2/(n_\text{in} + n_\text{out}))$.
- **Uniform:** $\mathcal{U}\!\left(-\sqrt{6/(n_\text{in}+n_\text{out})},\;\sqrt{6/(n_\text{in}+n_\text{out})}\right)$.

## Variants and successors

- **[[HeInitialization|He / Kaiming initialization]]** ($\sigma^2 = 2/n_\text{in}$) — the [[ReLU]]-aware variant; doubles the variance because ReLU zeroes half the activations on average.
- LeCun initialization ($\sigma^2 = 1/n_\text{in}$) — for SELU / self-normalizing networks.
- Deep-network-specific variants exist that have trained 10,000-layer networks without skip connections ([[d2l-multilayer-perceptrons]] §Beyond; Xiao et al. 2018).

## Caveat

The derivation assumes *no* nonlinearity, which neural networks obviously do have. The heuristic still works well in practice; for ReLU networks the corrected variant is [[HeInitialization|He init]].

## Framework defaults

| Framework | Default for `Linear` / `Dense` |
|---|---|
| [[PyTorch]] | `kaiming_uniform_` (He, not Xavier) |
| [[TensorFlow]] / Keras | `glorot_uniform` (Xavier) |
| [[JAX]] / Flax | `lecun_normal` |
| [[MXNet]] | Xavier (`Xavier()`) |

## Connections

- [[d2l-multilayer-perceptrons]] — §Xavier Initialization (canonical derivation).
- [[WeightInitialization]] — parent concept.
- [[HeInitialization]] — ReLU-corrected counterpart.
- [[VanishingGradient]] / [[ExplodingGradient]] — pathologies it prevents.
- [[XavierGlorot]] / [[YoshuaBengio]] — authors (entities or stubs).
- [[ActivationFunction]] — interacts: He for ReLU, Xavier for tanh/sigmoid.
