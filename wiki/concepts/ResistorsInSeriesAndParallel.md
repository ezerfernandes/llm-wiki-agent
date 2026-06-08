---
title: "Resistors in Series and Parallel"
type: concept
tags: [physics, electricity, circuits, dc]
sources: [college-physics-2e-ch21]
last_updated: 2026-06-07
---

## Definition
Two ways of combining resistors in a circuit. In a **series** connection the same current flows through each resistor in turn; in a **parallel** connection each resistor is wired directly across the source and sees the same voltage. Each combination can be replaced by a single **equivalent resistance** that preserves the circuit's overall behavior.

## Key Points
- Series: current is identical in all resistors; voltage drops add up.
- Parallel: voltage is identical across all resistors; branch currents add up.
- Parallel equivalent resistance is always less than the smallest branch resistor (adding paths makes it easier for charge to flow).
- Mixed (combination) circuits are solved by stepwise reduction of series and parallel sub-blocks.
- Energy and charge conservation guarantee the source power equals the sum of resistor powers.
- A long wire's own resistance acts in series with a load, causing voltage drop (dimming headlights, lossy extension cords).

## Equations
- Series total: `Rs = R₁ + R₂ + R₃ + ...`
- Series voltage division: `V = V₁ + V₂ + V₃`, `Vₙ = I Rₙ`
- Parallel total: `1/Rp = 1/R₁ + 1/R₂ + 1/R₃ + ...`
- Parallel current division: `I = I₁ + I₂ + I₃`, `Iₙ = V / Rₙ`
- Power: `P = IV = I²R = V²/R`; `P_source = Σ Pₙ`

## Related
- [[OhmsLaw]] — `V = IR`, applied to each resistor
- [[ElectricalResistance]] — the quantity being combined
- [[ElectricCurrent]], [[Voltage]], [[ElectricPower]] — distributed across the combination
- [[KirchhoffsRules]] — generalizes to circuits that won't reduce by series/parallel alone
- [[Capacitor]] — combines by the reverse rules (series/parallel swapped)
