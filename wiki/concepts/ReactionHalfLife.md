---
title: "Reaction Half-Life"
type: concept
tags: [chemistry, general-chemistry, kinetics]
sources: [chemistry-2e-ch12-kinetics]
last_updated: 2026-06-07
---

# Reaction Half-Life

The **half-life** of a reaction, $t_{1/2}$, is the time required for a reactant's [[Molarity|concentration]] to fall to half its value. Its dependence on initial concentration differs by [[ReactionOrder|reaction order]], so half-life behavior is itself a diagnostic of order. (This is the chemical-kinetics half-life — the decay of a reactant concentration — distinct from the radioactive-decay half-life in physics and from the ML model-accuracy half-life used elsewhere in the wiki.)

Derived from the [[IntegratedRateLaw|integrated rate laws]]:

| Order | Half-life | Behavior |
|---|---|---|
| First | $t_{1/2} = \dfrac{0.693}{k}$ | **Constant** — independent of [A]₀; the hallmark of first-order kinetics |
| Second | $t_{1/2} = \dfrac{1}{k[A]_0}$ | Inversely proportional to [A]₀; lengthens as the reaction proceeds |
| Zero | $t_{1/2} = \dfrac{[A]_0}{2k}$ | Proportional to [A]₀; shortens as the reaction proceeds |

Because a first-order half-life is constant, successive half-lives take equal time — a convenient signature for identifying first-order processes.

## Connections
- [[IntegratedRateLaw]] — source of each half-life formula
- [[ReactionOrder]] — half-life behavior diagnoses the order
- [[RateConstant]] — appears in every half-life expression
- [[ReactionRate]] — the time evolution being measured
- [[RadioactiveHalfLife]] — the nuclear-decay half-life (Ch 21), a first-order process obeying the same $t_{1/2} = 0.693/k$ law
- [[chemistry-2e-ch12-kinetics]] — source chapter (§12.4)
