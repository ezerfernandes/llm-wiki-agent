---
title: "Heat Engine"
type: concept
tags: [physics, thermodynamics, energy]
sources: [college-physics-2e-ch15]
last_updated: 2026-06-07
---

## Definition
A **heat engine** converts heat transfer into mechanical work by running a [[ThermodynamicProcess|cyclical process]] between a hot reservoir (T_h) and a cold reservoir (T_c). It absorbs heat Q_h from the hot reservoir, does net work W, and rejects waste heat Q_c to the cold reservoir. Examples: automobile (Otto-cycle) engines, steam turbines, and thermal power plants.

## Key Points
- Over a complete cycle ΔE_int = 0, so the [[FirstLawOfThermodynamics|first law]] gives W = Q_h − Q_c — net work is the net heat absorbed.
- **Thermal efficiency** is the fraction of input heat turned into work, Eff = W/Q_h = 1 − Q_c/Q_h (a thermodynamic-specific case of [[EnergyEfficiency]]).
- The [[SecondLawOfThermodynamics|second law]] (Kelvin statement) requires Q_c > 0 always, so efficiency is strictly below 100%.
- The [[CarnotCycle|Carnot cycle]] sets the upper bound Eff_C = 1 − T_c/T_h; real engines fall below it because of irreversibility.
- **Otto cycle** (four-stroke model): adiabatic compression → constant-volume ignition → adiabatic power stroke → constant-volume heat rejection; net work is the enclosed PV-loop area, and rejecting heat is mandatory.
- Practical figures: coal plants ~42%, nuclear ~35%; raising T_h and lowering T_c improves efficiency. Waste heat warms the environment and coal emits the most CO₂ per unit energy.

## Equations
- Net work: $W = Q_h - Q_c$
- Efficiency: $\text{Eff} = \dfrac{W}{Q_h} = 1 - \dfrac{Q_c}{Q_h}$
- Carnot limit: $\text{Eff}_C = 1 - \dfrac{T_c}{T_h}$

## Related
- [[FirstLawOfThermodynamics]]
- [[SecondLawOfThermodynamics]]
- [[CarnotCycle]]
- [[ThermodynamicProcess]]
- [[HeatPump]] — a heat engine run in reverse
- [[EnergyEfficiency]]
- [[HeatThermodynamics]]
- [[college-physics-2e-ch15]]
