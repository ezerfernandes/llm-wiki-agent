---
title: "Diederik P. Kingma"
type: entity
tags: [person, researcher, deep-learning, optimization]
sources: [d2l-optimization]
last_updated: 2026-05-16
---

# Diederik P. Kingma

Dutch machine-learning researcher; co-author with [[JimmyBa|Jimmy Ba]] of the seminal **[[Adam]]** optimizer (Kingma & Ba 2014, "Adam: A Method for Stochastic Optimization", ICLR 2015) — one of the most-cited papers in ML. Also co-inventor of the **[[VariationalAutoencoder|variational autoencoder]] (VAE)** (Kingma & Welling 2013).

## Why he matters here

- **Adam (2014).** Combined [[Momentum|first-moment]] momentum with [[RMSProp]]-style second-moment scaling and bias correction $\hat{\mathbf{v}}_t = \mathbf{v}_t/(1-\beta_1^t)$ to correct zero-initialization bias. Default optimizer for the [[transformer|Transformer]] era ([[d2l-optimization]] §adam).
- **VAE (2013).** With Max Welling at the University of Amsterdam — the reparameterization trick that made variational inference work with deep nets.

## Affiliations

- [[universityofamsterdam|University of Amsterdam]] — PhD with Max Welling.
- [[openai|OpenAI]] — founding research scientist (2015).
- [[google|Google Brain]] — researcher.

## Connections

- [[d2l-optimization]] — the canonical D2L treatment of Adam.
- [[JimmyBa]] — Adam co-author.
- [[Adam]] — flagship contribution.
- [[VariationalAutoencoder]] — VAE co-author.
