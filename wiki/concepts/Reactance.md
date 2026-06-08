---
title: "Reactance (Inductive and Capacitive)"
type: concept
tags: [physics, electromagnetism, electronics, ac]
sources: [college-physics-2e-ch23]
last_updated: 2026-06-07
---
## Definition
**Reactance** is the frequency-dependent opposition that [[Inductor|inductors]] and [[Capacitor|capacitors]] present to [[AlternatingCurrent|alternating current]]. **Inductive reactance (X_L)** arises because an inductor resists changes in current; **capacitive reactance (X_C)** arises because a capacitor must charge and discharge. Unlike resistance, reactance dissipates no average power — it stores and returns energy each cycle.

## Key Points
- Inductive reactance rises with frequency (`X_L = 2πfL`): an inductor blocks high frequencies, passes low ones. The voltage **leads** the current by 90°.
- Capacitive reactance falls with frequency (`X_C = 1/(2πfC)`): a capacitor blocks low frequencies (including DC), passes high ones. The voltage **lags** the current by 90°.
- A pure resistor has no reactance: voltage and current stay in phase (0°).
- For a single reactive element, current is `I = V/X` (rms), analogous to Ohm's law.
- These opposite frequency behaviors make inductors and capacitors complementary filters and lead to resonance when combined ([[RLCCircuit]]).

## Equations
- `X_L = 2π f L`  (inductive reactance)
- `X_C = 1 / (2π f C)`  (capacitive reactance)
- `I = V / X_L`,  `I = V / X_C`  (rms current through each element)

## Related
- [[Inductor]] / [[Inductance]] — source of inductive reactance
- [[Capacitor]] — source of capacitive reactance
- [[AlternatingCurrent]] — reactance only applies to AC
- [[Impedance]] — combines reactance with resistance
- [[RLCCircuit]] — where X_L and X_C compete and can cancel
