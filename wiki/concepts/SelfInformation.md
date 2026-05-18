---
title: "Self-Information"
type: concept
tags: [information-theory, foundational]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Self-Information

The amount of "surprise" associated with observing an event of probability $p$, measured in **bits** ([[ClaudeShannon|Shannon]] 1948 / [[d2l-appendix-mathematics]] §information-theory):

$$I(X) = -\log_2 p(X).$$

Rare events carry high information; certain events carry zero. The base-2 logarithm gives bits; using $\ln$ instead gives **nats**.

## Why $-\log p$ and not some other function

The functional form is uniquely determined by three desiderata:

1. Information is non-negative and zero for certain events ($p=1$).
2. Independent events accumulate additively: $I(X\cap Y) = I(X)+I(Y)$ when $X\perp Y$.
3. Information is a continuous function of the probability.

The only continuous $f:[0,1]\to[0,\infty]$ satisfying $f(pq)=f(p)+f(q)$ is $f(p)=-c\log p$, and choosing $c=1$ with base $2$ makes a fair-coin flip carry exactly $1$ bit. *"A series of binary digits of length $n$ contains $n$ bits of information."*

## Examples ([[d2l-appendix-mathematics]] thought experiment)

| Statement on a shuffled deck | Probability | Self-information |
|---|---:|---:|
| "I see a card." | 1 | 0 bits |
| "I see a heart." | 1/4 | 2 bits |
| "This is the 3 of spades." | 1/52 | ~5.7 bits |
| Full 52-card sequence revealed | 1/52! | ~225.6 bits |

## Connections

- [[d2l-appendix-mathematics]] — §information-theory canonical reference.
- [[Entropy]] — the expected self-information $H(X)=\mathbb{E}[I(X)]$.
- [[InformationTheory]] — parent field.
- [[ClaudeShannon]] — originator (1948).
