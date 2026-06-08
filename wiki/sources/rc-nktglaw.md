---
title: "NKTgLaw (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, physics, numerical-computation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/NKTgLaw
---

## Summary
The task implements the "NKTg Law on Varying Inertia," a physics-inspired formula describing an object's movement tendency from its position, velocity, and mass. The core computation is two product quantities: NKTg₁ = x × p (position times momentum) and NKTg₂ = (dm/dt) × p (rate of mass change times momentum), where momentum p = m × v. The signs of these two values are interpreted to indicate whether the object tends toward or away from a stable state.

## Task Requirements
- Compute linear momentum p = m × v.
- Compute NKTg₁ = x × p (position × momentum).
- Compute NKTg₂ = (dm/dt) × p (mass-variation rate × momentum).
- Interpret the sign of NKTg₁: positive means tending away from the stable state, negative means tending toward it.
- Interpret the sign of NKTg₂: positive means mass variation supports the movement, negative means it resists.

## Language Coverage
20 languages implement this task, a modest but broad spread across compiled, scripting, and functional families. Representative implementations include Ada, C++, Java, JavaScript, Python, Julia, F#, Scheme, R, and the Solidity smart-contract language.

## Connections
- [[LinearMomentum]] — the central derived quantity p = m × v
- [[NumericalComputation]] — straightforward arithmetic evaluation of formulas
- [[Physics]] — the task models a movement-tendency rule from mechanics
- [[SignAnalysis]] — output meaning is driven by the sign of each computed value

## Contradictions
- None — reference task page.
