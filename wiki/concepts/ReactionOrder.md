---
title: "Reaction Order"
type: concept
tags: [chemistry, general-chemistry, kinetics]
sources: [chemistry-2e-ch12-kinetics]
last_updated: 2026-06-07
---

# Reaction Order

The **reaction order** is the exponent on a reactant's concentration in the [[RateLaw|rate law]] rate = k[A]^m[B]^n…. The reaction is "order m with respect to A," and the **overall reaction order** is the sum m + n + …. Orders are usually small positive integers but may be fractional, negative, or zero, and they **must be determined experimentally** — they are not the coefficients of the [[ChemicalEquation|balanced equation]] (except for an [[ElementaryReaction|elementary reaction]], where order equals molecularity).

The overall order also fixes the units of the [[RateConstant|rate constant]].

## Method of initial rates

The standard experimental procedure for finding orders:
1. Measure the **initial** [[ReactionRate|rate]] for several trials with different initial concentrations.
2. Take pairs of trials in which **only one** reactant's concentration changes (others held constant) and form the rate ratio:

$$\frac{\text{rate}_x}{\text{rate}_y} = \frac{k[A]_x^m[B]_x^n}{k[A]_y^m[B]_y^n}$$

k and the unchanged terms cancel, leaving an equation in that reactant's order (solved with logarithms if it is not obvious). Repeat for each reactant.
3. Substitute back to compute k.

The order can also be read off the [[IntegratedRateLaw|integrated rate laws]]: whichever plot — [A], ln[A], or 1/[A] versus time — is linear identifies zero, first, or second order respectively.

## Connections
- [[RateLaw]] — where the orders live
- [[RateConstant]] — its units depend on the overall order
- [[IntegratedRateLaw]] — graphical determination of order
- [[ReactionRate]] — initial rates are the measured input
- [[ElementaryReaction]] — order = molecularity only for elementary steps
- [[chemistry-2e-ch12-kinetics]] — source chapter (§12.3)
