---
title: "Boris T. Polyak"
type: entity
tags: [person, researcher, optimization, mathematics]
sources: [d2l-optimization]
last_updated: 2026-05-16
---

# Boris T. Polyak

Soviet / Russian mathematician (1935–2023); foundational figure in convex and stochastic optimization. Introduced **heavy-ball momentum** (Polyak 1964, "Some methods of speeding up the convergence of iteration methods") — the accelerated gradient method that survived essentially unchanged into the [[Momentum|momentum]] term of every modern DL optimizer.

## Why he matters here

- **Heavy-ball momentum (1964).** The original $\mathbf{v}_t = \beta\mathbf{v}_{t-1}+\mathbf{g}_t$, $\mathbf{x}_t = \mathbf{x}_{t-1}-\eta\mathbf{v}_t$ formulation — used identically in [[Momentum]], [[Adam]] (as $\mathbf{v}_t$), and every accelerated gradient method ([[d2l-optimization]] §momentum).
- **Polyak averaging (1990).** Tail-averaging of SGD iterates as a variance-reduction technique that recovers optimal asymptotic rates.

## Affiliations

- Institute of Control Sciences (Moscow), Russian Academy of Sciences.

## Connections

- [[d2l-optimization]] — cites Polyak 1964 as momentum's origin.
- [[Momentum]] / [[NesterovMomentum]] — the algorithmic family.
- [[YuriiNesterov]] — extended Polyak's work with accelerated gradient methods.
