---
title: "Rate-Determining Step"
type: concept
tags: [chemistry, general-chemistry, kinetics]
sources: [chemistry-2e-ch12-kinetics]
last_updated: 2026-06-07
---

# Rate-Determining Step

In a multistep [[ReactionMechanism|reaction mechanism]], the **rate-determining step** (rate-limiting step) is the slowest [[ElementaryReaction|elementary reaction]]. Because a reaction can proceed no faster than its slowest step, this step controls the overall [[ReactionRate|rate]] and dictates the experimentally observed [[RateLaw|rate law]]. (This is the chemistry sense of "rate-limiting"; the term is used unrelatedly for throttling in systems/networking contexts.)

## Two common cases

- **Slow first step.** The overall rate law equals the rate law of that first elementary step. Example — NO₂ + CO below 225 °C:
  - Step 1 (slow): NO₂ + NO₂ → NO₃ + NO
  - Step 2 (fast): NO₃ + CO → NO₂ + CO₂
  - Overall 2NO₂ + CO → CO₂ + NO; rate = k[NO₂]²

- **Fast initial equilibrium before the slow step.** The slow step's rate law contains an intermediate, which may not appear in the final law. Set the fast step's forward and reverse rates equal to express the intermediate via measurable reactants, then substitute. Example — 2NO + Cl₂ → 2NOCl:
  - Step 1 (fast equilibrium): NO + Cl₂ ⇌ NOCl₂, so k₁[NO][Cl₂] = k₋₁[NOCl₂] → [NOCl₂] = (k₁/k₋₁)[NO][Cl₂]
  - Step 2 (slow): NOCl₂ + NO → 2NOCl, rate = k₂[NOCl₂][NO]
  - Substituting: rate = (k₂k₁/k₋₁)[NO]²[Cl₂]

A mechanism is acceptable only if its rate-determining-step analysis reproduces the measured rate law.

## Connections
- [[ReactionMechanism]] — the multistep path it governs
- [[ElementaryReaction]] — the steps, one of which is rate-determining
- [[RateLaw]] — what the rate-determining step yields
- [[ReactionRate]] — limited by the slowest step
- [[chemistry-2e-ch12-kinetics]] — source chapter (§12.6)
