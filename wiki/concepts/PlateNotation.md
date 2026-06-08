---
title: "Plate Notation"
type: concept
tags: [probabilistic-modeling, graphical-models, notation]
sources: [mml-ch08-when-models-meet-data, mml-book]
last_updated: 2026-06-04
---

# Plate Notation

A compact convention for [[DirectedGraphicalModel|directed graphical models]] in which a **plate** (a box) "repeats everything inside … $N$ times" ([[mml-book]] §8.5.1, p. 281). It is the standard way to draw **i.i.d. / repeated** structure without redrawing every node.

## The canonical example

A repeated Bernoulli experiment factorizes (because the trials are independent) as $p(x_1,\dots,x_N\,|\,\mu)=\prod_{n=1}^N p(x_n\,|\,\mu)$ (Eqs. 8.32–8.33). Two equivalent graphical models (Fig. 8.10):

- **(a)** $x_1,\dots,x_N$ drawn explicitly, all sharing the single parameter $\mu$.
- **(b)** a single $x_n$ inside a **plate** labeled $n=1,\dots,N$ — equivalent but more compact.

## Companion conventions

- **Shaded nodes are observed variables**; unshaded nodes are latent/unobserved ([[LatentVariable|latent variables]] or uncertain parameters).
- **Hyperprior** (Fig. 8.10c): plates make it trivial to add a second layer of priors — e.g. a $\text{Beta}(\alpha,\beta)$ prior on $\mu$. *"A hyperprior is a second layer of prior distributions on the parameters of the first layer of priors."* If $\alpha,\beta$ are deterministic (not random variables), their circle is omitted.

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.5.1 canonical reference (Fig. 8.10, Eqs. 8.32–8.33).
- [[mml-book]] — §8.5.1.
- [[DirectedGraphicalModel]] — the notation it compresses.
- [[LatentVariable]] — drawn unshaded; the hyperprior layers a prior on parameters.
- [[ConjugatePrior]] — the Beta–Bernoulli conjugacy behind the Fig. 8.10c hyperprior.
- [[IID]] — what the plate's repetition expresses.
