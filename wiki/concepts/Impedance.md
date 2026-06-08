---
title: "Impedance"
type: concept
tags: [physics, electromagnetism, electronics, ac]
sources: [college-physics-2e-ch23]
last_updated: 2026-06-07
---
## Definition
**Impedance (Z)** is the total opposition an AC circuit presents to current, combining resistance R with [[Reactance|inductive and capacitive reactance]] (X_L and X_C). It is the AC generalization of resistance and relates rms voltage and current by an Ohm's-law form `I = V/Z`. Because R and the reactances act 90° out of phase, they add in quadrature rather than linearly.

## Key Points
- For a series [[RLCCircuit|RLC circuit]], `Z = √[R² + (X_L − X_C)²]`.
- Z is frequency-dependent through X_L and X_C: capacitive reactance dominates at low frequency, inductive at high frequency.
- Impedance is minimized (Z = R) at the resonant frequency, where X_L and X_C cancel, giving maximum current.
- The **phase angle** between voltage and current satisfies `cos φ = R/Z` (the power factor).

## Equations
- `Z = √[R² + (X_L − X_C)²]`
- `I = V/Z`  (rms, AC Ohm's law)
- `cos φ = R/Z`  (power factor)

## Related
- [[Reactance]] — X_L and X_C combine with R to form Z
- [[RLCCircuit]] — the circuit whose impedance this describes
- [[Resonance]] — Z is minimal at the resonant frequency
- [[AlternatingCurrent]] — impedance applies to AC circuits
- [[OhmsLaw]] — Z plays the role of R in AC form
