---
title: "Carnot Cycle and Carnot Efficiency"
type: concept
tags: [physics, thermodynamics, energy]
sources: [college-physics-2e-ch15]
last_updated: 2026-06-07
---

## Definition
The **Carnot cycle** is an idealized, fully reversible thermodynamic cycle made of two isothermal and two adiabatic steps. A **Carnot engine** running this cycle achieves the maximum efficiency physically possible for a [[HeatEngine|heat engine]] operating between a hot reservoir at T_h and a cold reservoir at T_c. Devised by [[SadiCarnot]] in 1824.

## Key Points
- Four reversible steps: (1) isothermal expansion at T_h absorbing Q_h; (2) adiabatic expansion cooling to T_c; (3) isothermal compression at T_c rejecting Q_c; (4) adiabatic compression reheating to T_h.
- **Carnot's principle** (a restatement of the [[SecondLawOfThermodynamics|second law]]): no engine between two given temperatures can beat a Carnot engine, and all fully reversible engines between those temperatures share the same maximum efficiency.
- Because it is reversible, Q_c/Q_h = T_c/T_h, which yields the efficiency formula and makes the cycle's total [[ThermodynamicEntropy|entropy]] change zero.
- **100% efficiency is impossible**: Eff_C = 1 only if T_c = 0 K (absolute zero), which is unattainable.
- Maximize efficiency by raising T_h and lowering T_c (widening the temperature ratio).
- Real engines never reach Eff_C because all real processes involve irreversibilities (friction, turbulence, peripheral losses).

## Equations
- Carnot efficiency: $\text{Eff}_C = 1 - \dfrac{T_c}{T_h}$ (absolute temperature, kelvin)
- Reversible heat ratio: $\dfrac{Q_c}{Q_h} = \dfrac{T_c}{T_h}$
- General engine efficiency: $\text{Eff} = 1 - \dfrac{Q_c}{Q_h}$

## Related
- [[HeatEngine]]
- [[SecondLawOfThermodynamics]]
- [[ThermodynamicProcess]] — isothermal + adiabatic building blocks
- [[ThermodynamicEntropy]]
- [[HeatPump]] — best COP uses the reversed Carnot cycle
- [[ThermodynamicTemperature]]
- [[SadiCarnot]]
- [[college-physics-2e-ch15]]
