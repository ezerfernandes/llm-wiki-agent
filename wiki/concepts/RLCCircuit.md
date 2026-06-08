---
title: "RLC Series Circuit and Resonance"
type: concept
tags: [physics, electromagnetism, electronics, ac]
sources: [college-physics-2e-ch23]
last_updated: 2026-06-07
---
## Definition
An **RLC series circuit** connects a resistor (R), an [[Inductor|inductor]] (L), and a [[Capacitor|capacitor]] (C) in series across an AC source. Its total opposition is the [[Impedance|impedance]] `Z = √[R² + (X_L − X_C)²]`, combining resistance with [[Reactance|inductive and capacitive reactance]]. The circuit exhibits **resonance** — maximum current — at the frequency where the two reactances cancel.

## Key Points
- The series current is the same throughout; the resistor voltage is in phase with it, the inductor voltage leads by 90°, and the capacitor voltage lags by 90°.
- At the **resonant frequency** `f₀ = 1/(2π√(LC))`, X_L = X_C, so Z = R, the current is maximal, and the [[Resonance|resonance]] mirrors a driven mechanical oscillator at its natural frequency.
- The **power factor** `cos φ = R/Z` measures how much delivered power is real; it equals 1 at resonance (all power dissipated) and falls off-resonance.
- Below f₀ the circuit is net capacitive; above f₀ it is net inductive.
- This frequency selectivity is the basis of radio tuning and electronic filters.

## Equations
- `Z = √[R² + (X_L − X_C)²]`
- `I₀ = V₀/Z`,  `I_rms = V_rms/Z`
- `V₀ = √[V₀R² + (V₀L − V₀C)²]`  (source voltage from element voltages)
- `f₀ = 1/(2π√(LC))`  (resonant frequency)
- `cos φ = R/Z`  (power factor)
- `P_ave = I_rms V_rms cos φ`

## Related
- [[Impedance]] — total opposition Z of the circuit
- [[Reactance]] — X_L and X_C that compete and cancel at resonance
- [[Resonance]] — electrical analog of mechanical resonance
- [[Inductor]] / [[Capacitor]] — the reactive elements
- [[AlternatingCurrent]] — the driving source

## Applications
- Radio receiver tuning (variable capacitor selects f₀); LC frequency standards in digital watches; frequency-selective filters; efficient (high-power-factor) motor operation near resonance.
