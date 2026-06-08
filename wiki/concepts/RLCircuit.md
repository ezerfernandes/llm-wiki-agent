---
title: "RL Circuit"
type: concept
tags: [physics, electromagnetism, electronics, circuits]
sources: [college-physics-2e-ch23]
last_updated: 2026-06-07
---
## Definition
An **RL circuit** contains a resistor (R) and an [[Inductor|inductor]] (L) in series. Because the inductor opposes changes in current ([[LenzsLaw|Lenz's law]]), the current cannot jump instantaneously; instead it rises or decays exponentially toward its steady value, governed by the **time constant** `τ = L/R`. It is the inductive analog of the [[RCCircuit|RC circuit]].

## Key Points
- On turn-on, current climbs as `I = I₀(1 − e^(−t/τ))`, reaching ~63.2% of its final value after one τ.
- On turn-off, current decays as `I = I₀ e^(−t/τ)`, dropping to ~36.8% of its value after each τ.
- A larger L (more stored magnetic energy) or smaller R lengthens τ, slowing the transient.
- The steady-state current is simply `I₀ = V/R` — the inductor behaves like a plain wire once the current stops changing.

## Equations
- `τ = L/R`  (1 H = 1 Ω·s)
- `I = I₀ (1 − e^(−t/τ))`  (turn-on)
- `I = I₀ e^(−t/τ)`  (turn-off)
- `I₀ = V/R`  (steady state)

## Related
- [[Inductor]] / [[Inductance]] — the L that resists current change
- [[RCCircuit]] — the capacitive analog (time constant RC)
- [[LenzsLaw]] — why current cannot change instantaneously
- [[Reactance]] — AC counterpart of the inductor's opposition
