---
title: "Dropout"
type: concept
tags: [regularization, deep-learning, foundational]
sources: [d2l-multilayer-perceptrons, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Dropout

A regularization technique that randomly zeroes hidden-unit activations at training time with probability $p$ and rescales survivors by $1/(1-p)$ to preserve expectations. Forces the network to learn redundant, non-co-adapted representations; **disabled at inference** in standard practice. Introduced by [[NitishSrivastava|Srivastava]], [[GeoffreyHinton|Hinton]], [[AlexKrizhevsky|Krizhevsky]] et al. (2014); now a mainstay of deep learning ([[d2l-multilayer-perceptrons]] §Dropout).

## The mechanic

Per activation $h$ in a layer:

$$
h' = \begin{cases} 0 & \text{w.p. } p \\ h/(1-p) & \text{otherwise} \end{cases}
$$

By design $\mathbb{E}[h'] = h$ — *unbiased* noise injection. Connects to [[ChrisBishop|Bishop's]] (1995) result that input-noise training ≡ Tikhonov regularization, extended to *internal* layers.

## Intuitions for why it helps

- **Breaks [[Coadaptation|co-adaptation]]** — each unit cannot rely on a specific pattern of peers.
- **Implicit model averaging** — training samples one of $2^k$ subnetworks per step; inference combines them via the $1/(1-p)$ rescaling.
- **Bayesian view** — dropout at *test* time approximates Monte Carlo predictive sampling, used as a heuristic uncertainty estimator (Gal & Ghahramani 2016).

## D2L's typical recipe (FashionMNIST)

- Two hidden layers of 256 units, ReLU.
- Dropout 0.5 after each hidden layer (often lower closer to inputs).
- 10-class softmax head.

## Test-time semantics

> "Typically, we disable dropout at test time. Given a trained model and a new example, we do not drop out any nodes and thus do not need to normalize." — [[d2l-multilayer-perceptrons]]

Frameworks track `training` vs `eval` mode (PyTorch `model.eval()`, TF `training=False`, Flax `deterministic=True`).

## Composes with…

- **[[WeightDecay]]** — dropout and weight decay can both be applied; results are typically not strictly additive but compatible.
- **[[BatchNormalization]]** — historically tricky to combine; modern transformers use *LayerNorm* + dropout without much trouble.
- **[[EarlyStopping]]** — orthogonal.

## Connections

- [[d2l-multilayer-perceptrons]] — §Dropout (canonical reference).
- [[Regularization]] — parent concept.
- [[Coadaptation]] — the phenomenon dropout breaks.
- [[Overfitting]] — what dropout combats.
- [[WeightDecay]] / [[EarlyStopping]] — companion regularizers.
- [[BatchNormalization]] — orthogonal technique with subtle interactions.
- [[NitishSrivastava]] / [[GeoffreyHinton]] / [[AlexKrizhevsky]] — original authors.
- [[mlsysbook-ch05-neural-computation]] — flags dropout's systems hazard: it makes training stochastic but inference deterministic, creating divergent computational graphs; forgetting to switch from the training to the inference graph silently degrades accuracy 5–15%.
