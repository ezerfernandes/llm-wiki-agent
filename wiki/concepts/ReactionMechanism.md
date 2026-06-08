---
title: "Reaction Mechanism"
type: concept
tags: [chemistry, general-chemistry, kinetics]
sources: [chemistry-2e-ch12-kinetics]
last_updated: 2026-06-07
---

# Reaction Mechanism

A **reaction mechanism** (reaction path) is the precise, step-by-step sequence of [[ElementaryReaction|elementary reactions]] by which an overall reaction actually occurs. A balanced [[ChemicalEquation|overall equation]] shows only what reacts and what is produced; it says nothing about the intervening molecular events. The elementary steps of a mechanism must **sum to the overall balanced equation**.

Example — ozone decomposition (2O₃ → 3O₂):
- Step 1: O₃ → O₂ + O
- Step 2: O + O₃ → 2O₂

The oxygen atom O is a **[[ReactionMechanism|reaction intermediate]]**: produced in one step and consumed in a later one, so it does not appear in the overall equation. (An intermediate differs from the [[TransitionState|transition state]], which is a fleeting energy maximum within a single step, not a discrete species.)

## Rate law from a mechanism

Unlike overall reactions, each [[ElementaryReaction|elementary step]]'s rate law follows directly from its equation (order = molecularity). The overall [[RateLaw|rate law]] is governed by the [[RateDeterminingStep|rate-determining (slowest) step]]:
- **Slow first step** → overall rate law = that step's rate law (e.g., 2NO₂ + CO → CO₂ + NO has rate = k[NO₂]² from the slow NO₂ + NO₂ step).
- **Fast pre-equilibrium then slow step** → set forward = reverse rates of the fast step to express the intermediate's concentration in terms of measurable reactants, then substitute it into the slow step (intermediates may not appear in the final rate law). E.g., 2NO + Cl₂ → 2NOCl yields rate = (k₂k₁/k₋₁)[NO]²[Cl₂].

A proposed mechanism is plausible only if its steps sum correctly *and* its derived rate law matches the experimental one.

## Connections
- [[ElementaryReaction]] — the building-block steps and their molecularity
- [[RateDeterminingStep]] — sets the overall rate
- [[RateLaw]] — what a valid mechanism must reproduce
- [[TransitionState]] — energy maximum within each step (vs an intermediate)
- [[ChemicalEquation]] — steps must sum to it
- [[Catalysis]] — catalysts change the mechanism to lower its barrier
- [[chemistry-2e-ch12-kinetics]] — source chapter (§12.6)
