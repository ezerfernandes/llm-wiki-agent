---
title: "Decision Making Under Uncertainty"
type: concept
tags: [decision-theory, foundational]
sources: [pml1-murphy]
last_updated: 2026-05-15
---

# Decision Making Under Uncertainty

Choosing an action whose value depends on unknown future outcomes. [[pml1-murphy]] §5 (Decision Theory) develops the canonical Bayesian treatment: each action $a$ has an expected utility $\mathbb{E}_{p(s)}[U(s,a)]$ under a belief distribution $p(s)$ over states, and the optimal action is $a^* = \arg\max_a \mathbb{E}[U(s,a)]$.

## Why it justifies the [[ProbabilisticPerspective]]

The Dutch-book / Cox / Savage axiomatizations all show: any agent making decisions under uncertainty whose belief representation is *not* probabilistic can be exploited (Dutch-booked) or is inconsistent (Cox / Savage). Hence "we should represent uncertainty probabilistically" follows from "we should make rational decisions" — not vice versa.

This is the deeper of Murphy's two arguments for the probabilistic framing (§1.1).

## Practical instantiations in this wiki

- **Loss matrices** (Murphy §1.2.1.5, Table 1.2): asymmetric costs of misclassification (e.g., eating a poisonous flower is much worse than declining a safe one) make the optimal Bayes classifier *not* the argmax of $p(y|\mathbf{x})$.
- **Reward hacking** (Murphy §1.6.3): when the utility function is *misspecified*, the rational-under-uncertainty agent optimizes the wrong thing. This is the alignment problem in decision-theoretic clothing.
- **Inverse reinforcement learning / assistance games** (Russell, cited Murphy §1.6.3): infer the utility function from observed human behavior, then act under uncertainty about it.
- **[[BystanderEffect|Bystander effect]] under social load** ([[2605.10698-bystander-effect-mas]]): a decision agent's optimal action under uncertainty about peer competence + status differs systematically from optimal under no-social-load — this is decision theory with a [[CompositeSocialLoad]] term in the utility.

## Connections

- [[pml1-murphy]] — Ch 5 (Decision Theory) is the textbook reference.
- [[ProbabilisticPerspective]] — the framing this concept justifies.
- [[AlignmentHallucination]] — decision-theoretic pathology when utility includes social-conformity terms.
