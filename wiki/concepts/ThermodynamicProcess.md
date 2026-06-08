---
title: "Thermodynamic Process (Isobaric, Isochoric, Isothermal, Adiabatic)"
type: concept
tags: [physics, thermodynamics]
sources: [college-physics-2e-ch15]
last_updated: 2026-06-07
---

## Definition
A **thermodynamic process** is a path by which a system moves between states while exchanging heat and work. Four idealized processes specialize the [[FirstLawOfThermodynamics|first law]] (ΔE_int = Q − W) by fixing one variable. **PV work** is the energy exchanged when a system changes volume against pressure; on a PV diagram, work equals the **area under the curve** and is path-dependent.

## Key Points
- **Isobaric** (constant pressure): work is straightforward, W = PΔV.
- **Isochoric / isovolumetric** (constant volume): a vertical line on a PV diagram; W = 0, so all heat goes into internal energy.
- **Isothermal** (constant temperature): for an ideal gas ΔE_int = 0, so Q = W; PV = constant. The isothermal curve sits above the adiabatic one from the same start (heat input sustains pressure), yielding more work.
- **Adiabatic** (no heat, Q = 0): ΔE_int = −W; expansion work comes entirely at the expense of internal energy, so temperature and pressure drop.
- **Reversible process**: an idealization with no dissipation, returnable to its initial state; real processes have friction/turbulence and are **irreversible**.
- **Cyclical process**: returns to the start (ΔE_int = 0); net work equals the enclosed PV-loop area, positive for clockwise traversal. This is how [[HeatEngine|heat engines]] produce net work.

## Equations
- General work: $W = \int P\,dV$ (area under the PV curve)
- Isobaric: $W = P\,\Delta V$
- Isochoric: $W = 0$
- Isothermal (ideal gas): $PV = \text{const}$, $\Delta E_{\text{int}} = 0$, $Q = W$
- Adiabatic: $Q = 0$, $\Delta E_{\text{int}} = -W$
- Monatomic ideal-gas internal energy: $E_{\text{int}} = \tfrac{3}{2}NkT$
- Cyclical: $W_{\text{net}} = $ enclosed loop area

## Related
- [[FirstLawOfThermodynamics]]
- [[HeatEngine]]
- [[CarnotCycle]] — built from reversible isothermal + adiabatic steps
- [[IdealGasLaw]] — PV = NkT underlies the isothermal/adiabatic relations
- [[HeatThermodynamics]]
- [[InternalEnergyThermodynamics]]
- [[college-physics-2e-ch15]]
