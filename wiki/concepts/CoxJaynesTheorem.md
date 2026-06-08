---
title: "Cox-Jaynes Theorem"
type: concept
tags: [probability, foundational, philosophy]
sources: [mml-book, mml-ch06-probability-and-distributions]
last_updated: 2026-06-04
---

# Cox-Jaynes Theorem

Any consistent quantification of plausibility must obey the axioms of probability ([[mml-book]] §6.1.1, citing Jaynes 2003). Probability is a generalization of Boolean logic.

## From [[mml-ch06-probability-and-distributions|MML Ch 6]]

[[mml-book]] §6.1.1 (book pp. 172–174) motivates the theorem with the failure of classical Boolean logic to express *plausible* reasoning: observing "$A$ is false" can make $B$ "less plausible" though no logical conclusion follows; observing "$B$ is true" can make $A$ "more plausible." The everyday "waiting for a late friend" example (H1 on time / H2 stuck in traffic / H3 abducted by aliens) shows us ruling out H1 and ranking H2 over H3 without being logically compelled.

> "For plausible reasoning it is necessary to extend the discrete true and false values of truth to continuous plausibilities." — Jaynes (2003), [[mml-book]] marginal, p. 173

E. T. Jaynes (1922–1998) laid out **three desiderata** any plausibility assignment must satisfy (§6.1.1, p. 173–174):

1. Degrees of plausibility are represented by **real numbers**.
2. These numbers are based on the **rules of common sense**.
3. The reasoning is **consistent**, in three senses: *non-contradiction* (the same plausibility is reached via different routes), *honesty* (all available data is used), and *reproducibility* (equal states of knowledge ⇒ equal plausibilities).

The **Cox–Jaynes theorem** proves these desiderata are *sufficient* to determine the universal mathematical rules of plausibility **up to an arbitrary monotonic transformation** — and crucially, *those rules are the rules of probability* (the [[SumRule]] and [[ProductRule]], hence [[BayesTheorem]]). This grounds the **Bayesian** reading of probability as degree of belief while remaining compatible with the **frequentist** reading; [[mml-book]] is deliberately agnostic between them (§6.1 Remark). Further arguments that probability is the foundation of reasoning systems: Pearl (1988), Hacking (2001).

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.1.1 deep dive.
- [[mml-book]] — §6.1.1 canonical reference.
- [[probability]] — the theory whose axioms this justifies.
- [[ProbabilitySpace]] — the formal structure obeying the axioms.
- [[SumRule]] / [[ProductRule]] / [[BayesTheorem]] — "the rules of probability" the theorem yields.
