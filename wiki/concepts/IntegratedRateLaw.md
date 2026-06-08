---
title: "Integrated Rate Law"
type: concept
tags: [chemistry, general-chemistry, kinetics]
sources: [chemistry-2e-ch12-kinetics]
last_updated: 2026-06-07
---

# Integrated Rate Law

An **integrated rate law** relates reactant [[Molarity|concentration]] to **time** (whereas the differential [[RateLaw|rate law]] relates rate to concentration). Integrating each rate law yields a form whose linear plot both confirms the [[ReactionOrder|order]] and gives the [[RateConstant|rate constant]].

## First order — rate = k[A]
$$[A]_t = [A]_0\,e^{-kt} \qquad \ln[A]_t = -kt + \ln[A]_0$$
- Linear plot: **ln[A]ₜ vs t** → slope = −k, intercept = ln[A]₀
- [[ReactionHalfLife|Half-life]]: t½ = 0.693/k (independent of initial concentration)

## Second order — rate = k[A]²
$$\frac{1}{[A]_t} = kt + \frac{1}{[A]_0}$$
- Linear plot: **1/[A]ₜ vs t** → slope = k, intercept = 1/[A]₀
- [[ReactionHalfLife|Half-life]]: t½ = 1/(k[A]₀) (inversely proportional to [A]₀; lengthens as the reaction proceeds)

## Zero order — rate = k
$$[A]_t = -kt + [A]_0$$
- Linear plot: **[A]ₜ vs t** → slope = −k, intercept = [A]₀
- [[ReactionHalfLife|Half-life]]: t½ = [A]₀/(2k) (proportional to [A]₀)

**Identifying order graphically:** whichever of [A], ln[A], or 1/[A] gives a straight line against t reveals zero, first, or second order. Worked examples include first-order cyclobutane decomposition at 500 °C (k = 9.2×10⁻³ s⁻¹), first-order H₂O₂ (k = 0.116 h⁻¹ from a linear ln[H₂O₂] plot), and second-order butadiene dimerization (k = 5.76×10⁻² L mol⁻¹ min⁻¹).

## Connections
- [[RateLaw]] — the differential form that is integrated
- [[ReactionHalfLife]] — derived from each integrated form
- [[ReactionOrder]] — identified by which plot is linear
- [[RateConstant]] — read from the slope
- [[ReactionRate]] — the underlying quantity over time
- [[chemistry-2e-ch12-kinetics]] — source chapter (§12.4)
