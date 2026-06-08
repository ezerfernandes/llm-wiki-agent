---
title: "Conjunction Fallacy"
type: concept
tags: [logic, critical-thinking, probability, cognitive-bias, fallacy]
sources: [logic-text-v2]
last_updated: 2026-06-07
---

# Conjunction Fallacy

The **conjunction fallacy** is judging a **conjunction to be more probable than one of its conjuncts** — which is impossible, since $P(A \wedge B) \le P(A)$ always. [[logic-text-v2|Van Cleave]] §3.6 introduces it with the famous **"Linda" problem** of [[AmosTversky|Tversky]] & [[DanielKahneman|Kahneman]] (1983).

## The Linda problem
> Linda is 31, single, outspoken, very bright; majored in philosophy; as a student was deeply concerned with discrimination and social justice and joined anti-nuclear demonstrations. Which is more probable?
> **(a)** Linda is a bank teller.
> **(b)** Linda is a bank teller **and** is active in the feminist movement.

Most people answer **(b)** — but (b) *contains* (a) plus more, so it cannot be more probable. Numerically, with $P(\text{teller}) = .4$ and $P(\text{feminist}) = .9$:
$$P(\text{teller} \wedge \text{feminist}) = .4 \times .9 = .36 < .4 = P(\text{teller}).$$
Even if feminism were certain ($P=1$), (b) could at best **equal** (a).

## Why it's seductive
The fallacy is obvious in some framings ("Mark has hair" vs "Mark has blonde hair") yet fools even statisticians in the Linda case. [[DanielKahneman|Kahneman]]'s explanation: the mind substitutes a question about **representativeness** (how well the description matches a feminist) for the question about **probability**. The feminist description is *representative* of Linda; "bank teller" matches nothing — so intuition wrongly ranks the richer story higher. This **attribute-substitution** account is why the book explains *why* fallacies are seductive rather than treating them as obvious.

## Connections
- [[Probability]] — the multiplication rule for conjunctions is the normative standard.
- [[BaseRateFallacy]] — sibling probabilistic fallacy from the same research program.
- [[DanielKahneman]] / [[AmosTversky]] — authors of the 1983 experiment.
- [[LogicalFallacy]] — the broader catalog (this is a probabilistic/formal fallacy).
- [[logic-text-v2]] — canonical source (§3.6).
