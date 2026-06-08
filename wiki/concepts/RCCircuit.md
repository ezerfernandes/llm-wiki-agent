---
title: "RC Circuit"
type: concept
tags: [physics, electricity, circuits, dc]
sources: [college-physics-2e-ch21]
last_updated: 2026-06-07
---

## Definition
An RC circuit contains a resistor (R) and a charge-storing [[Capacitor]] (C). Under a DC source it exhibits a **transient** response: when a switch closes, current charges the initially empty capacitor; the capacitor voltage rises (or, when the source is removed, decays) exponentially over a characteristic timescale set by the [[TimeConstant]] `τ = RC`.

## Key Points
- As charge accumulates, repulsion of like charges opposes further current, so current tapers off — described by Kirchhoff's loop rule ([[KirchhoffsRules]]).
- Initial charging current `I₀ = emf/R`; smaller R charges faster.
- After one time constant the charging voltage reaches 63.2% of its final value; the discharging voltage falls to 36.8% of its initial value.
- Rising battery [[InternalResistance]] with age lengthens charging time (camera-flash delay).
- Basis for timing and pulse circuits.

## Equations
- Charging: `V = emf · (1 − e^(−t/RC))`
- Discharging: `V = V₀ · e^(−t/RC)`
- Capacitor voltage: `V_C = Q / C`
- Time constant: `τ = RC`; at `t = τ`, charge ≈ 63.2% (charging) / 36.8% remaining (discharging)

## Related
- [[TimeConstant]] — `τ = RC`, the governing timescale
- [[Capacitor]] / [[Capacitance]] — the energy-storing element
- [[ElectricalResistance]] — sets the charging rate
- [[KirchhoffsRules]] — loop rule governs the transient
- [[InternalResistance]] — battery r affects charging speed
