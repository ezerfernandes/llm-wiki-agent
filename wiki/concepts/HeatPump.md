---
title: "Heat Pump, Refrigerator, and Coefficient of Performance"
type: concept
tags: [physics, thermodynamics, energy]
sources: [college-physics-2e-ch15]
last_updated: 2026-06-07
---

## Definition
A **heat pump** is a [[HeatEngine|heat engine]] run in reverse: using work input W, it moves heat Q_c from a cold reservoir and delivers Q_h to a hot reservoir. The same hardware is a **refrigerator** or **air conditioner** when the goal is removing heat from the cold space rather than warming the hot space. Performance is rated by a dimensionless **coefficient of performance (COP)**.

## Key Points
- Energy balance ([[FirstLawOfThermodynamics|first law]]): Q_h = Q_c + W — delivered heat equals absorbed heat plus work input.
- Work input is mandatory because the [[SecondLawOfThermodynamics|second law]] forbids heat flowing cold→hot on its own.
- **COP_hp = Q_h/W** for heating; **COP_ref = Q_c/W** for cooling; they differ by one: COP_ref = COP_hp − 1 (so a refrigerator's COP is always lower).
- COP is inversely related to engine efficiency: COP_hp = 1/Eff, so the best possible heat pump uses the reversed [[CarnotCycle|Carnot]] limit. Smaller hot–cold temperature gaps (mild climates) give higher COP.
- Refrigerant circuit: a compressor raises pressure/temperature, **evaporator coils** absorb heat where the fluid vaporizes, **condenser coils** release heat where it condenses, and an expansion valve drops pressure; reversing the flow swaps heating and cooling.
- Real performance: COP_hp ≈ 2–4, COP_ref ≈ 2–6. Heat pumps deliver more heat than the work costs but electricity can be pricier per joule than burning gas. Consumer ratings include Energy Star stars and EER (≈6–12 for room units).

## Equations
- Energy balance: $Q_h = Q_c + W$
- Heat pump: $\text{COP}_{hp} = \dfrac{Q_h}{W}$
- Refrigerator/AC: $\text{COP}_{ref} = \dfrac{Q_c}{W}$
- Relation: $\text{COP}_{ref} = \text{COP}_{hp} - 1$, and $\text{COP}_{hp} = \dfrac{1}{\text{Eff}}$
- Carnot ceiling: best $\text{Eff} = 1 - \dfrac{T_c}{T_h}$

## Related
- [[HeatEngine]]
- [[CarnotCycle]]
- [[FirstLawOfThermodynamics]]
- [[SecondLawOfThermodynamics]]
- [[EnergyEfficiency]]
- [[HeatThermodynamics]]
- [[college-physics-2e-ch15]]
