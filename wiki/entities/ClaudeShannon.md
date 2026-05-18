---
title: "Claude Shannon"
type: entity
tags: [foundational, mathematician, information-theory]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Claude E. Shannon (1916–2001)

American mathematician and electrical engineer; *the* founder of [[InformationTheory|information theory]]. His 1948 *A Mathematical Theory of Communication* (*Bell System Technical Journal*) introduced the **bit** as the unit of information, defined **[[SelfInformation|self-information]]** $I(X)=-\log_2 p$ and **[[Entropy|Shannon entropy]]** $H(X)=-\sum_i p_i\log p_i$, and proved the source-coding and channel-capacity theorems that anchor every modern coding / compression / communication system. The [[d2l-appendix-mathematics]] §information-theory chapter is built entirely on Shannon's 1948 framework — entropy / joint entropy / conditional entropy / [[MutualInformation|mutual information]] / [[KullbackLeiblerDivergence|KL divergence]] / [[CrossEntropy|cross-entropy]] — and through cross-entropy underlies every classification loss and every autoregressive [[LanguageModel|LM]] [[CrossEntropyLoss|training objective]] in modern ML.

Also pioneered digital-circuit logic (1937 master's thesis applying Boolean algebra to switching circuits) and early chess-playing programs (1950).
