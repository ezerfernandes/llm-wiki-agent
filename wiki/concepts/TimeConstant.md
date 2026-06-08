---
title: "Time Constant (RC)"
type: concept
tags: [physics, electricity, circuits, dc]
sources: [college-physics-2e-ch21]
last_updated: 2026-06-07
---

## Definition
The time constant τ characterizes how quickly an [[RCCircuit]] charges or discharges. For a resistor–capacitor circuit it equals the product of resistance and capacitance, `τ = RC`, and has units of seconds (ohm × farad = second).

## Key Points
- After one time constant, a charging capacitor reaches 63.2% of its final voltage.
- After one time constant, a discharging capacitor falls to 36.8% of its initial voltage.
- Larger R or larger C lengthens τ, slowing the transient; smaller values speed it up.
- A circuit is essentially fully charged/discharged after roughly 5τ.
- Sets timing in strobe flashes, intermittent wipers, pacemakers, and other RC timing circuits.

## Equations
- `τ = RC`
- Charging: `V = emf · (1 − e^(−t/τ))`; at `t = τ`, `V = 0.632 · emf`
- Discharging: `V = V₀ · e^(−t/τ)`; at `t = τ`, `V = 0.368 · V₀`

## Related
- [[RCCircuit]] — the circuit whose transient τ describes
- [[Capacitance]] / [[Capacitor]] — the C in `τ = RC`
- [[ElectricalResistance]] — the R in `τ = RC`
- [[InternalResistance]] — adds to R, lengthening τ in real sources
