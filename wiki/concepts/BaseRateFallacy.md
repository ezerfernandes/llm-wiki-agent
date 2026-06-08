---
title: "Base Rate Fallacy"
type: concept
tags: [logic, critical-thinking, probability, cognitive-bias, fallacy, bayesian-inference]
sources: [logic-text-v2]
last_updated: 2026-06-07
---

# Base Rate Fallacy

The **base-rate fallacy** is ignoring the **prior prevalence (base rate)** of a condition when interpreting evidence such as a test result — concluding from a 95%-accurate positive test that there is a 95% chance you have the disease. [[logic-text-v2|Van Cleave]] §3.7.

## The colon-cancer example
Suppose colon cancer has a base rate of **0.5%** in the population, and a test is **95% accurate** (95% true-positive rate, and a 5% false-positive rate on the healthy). A positive result feels like "95% chance of cancer," but that ignores how many **healthy** people also test positive:

- Of 10,000 people, ~50 have cancer → ~**47.5 true positives** (95% of 50).
- The other 9,950 are healthy → ~**497.5 false positives** (5% of 9,950).
- So $P(\text{cancer} \mid \text{positive}) \approx \dfrac{47.5}{47.5 + 497.5} \approx 8.7\%$ — **not 95%.**

The low base rate dominates: most positives are false positives because the healthy group is so much larger.

## It is Bayes' theorem, informally
The correct computation is exactly **[[BayesTheorem|Bayes' theorem]]**: the posterior depends on the **prior** (base rate), not the likelihood alone. Neglecting the base rate is neglecting the prior. As with the [[ConjunctionFallacy|conjunction fallacy]], [[DanielKahneman|Kahneman]]'s diagnosis is that intuition substitutes the vivid test accuracy (representativeness/availability) for the proper probabilistic integration.

## Connections
- [[BayesTheorem]] — the normatively correct calculation the fallacy violates.
- [[Probability]] / [[ConditionalProbability]] — the underlying machinery.
- [[ConjunctionFallacy]] — sibling probabilistic fallacy.
- [[DanielKahneman]] / [[AmosTversky]] — the heuristics-and-biases program.
- [[logic-text-v2]] — canonical source (§3.7).
