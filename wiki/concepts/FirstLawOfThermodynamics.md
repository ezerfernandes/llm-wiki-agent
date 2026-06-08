---
title: "First Law of Thermodynamics"
type: concept
tags: [chemistry, physics, thermochemistry, thermodynamics]
sources: [chemistry-2e-ch05-thermochemistry, college-physics-2e-ch15]
last_updated: 2026-06-07
---

# First Law of Thermodynamics

The **first law of thermodynamics** is the conservation-of-energy principle applied to a [[ThermodynamicSystem|system]]: during a chemical or physical change, energy can be neither created nor destroyed, only changed in form. Quantitatively, the change in a system's [[InternalEnergyThermodynamics|internal energy]] equals the heat added to it plus the work done on it:

**ΔU = q + w**

## Sign Conventions
- **q** — heat: positive when absorbed by the system (flows in), negative when released (flows out).
- **w** — work: positive when done *on* the system, negative when done *by* the system.

## Expansion (Pressure-Volume) Work
When a system expands against a restraining pressure (or the surroundings compress it), it does **expansion work**:

**PΔV = −w**

The signs of ΔV and w are always opposite (expansion ⇒ system does work ⇒ w < 0).

## Link to Enthalpy
Combining the first law with the definition [[EnthalpyChemistry|H = U + PV]], at constant pressure with only expansion work the heat of reaction equals the enthalpy change: **ΔH = ΔU + PΔV = q_p**.

## Physics Convention (College Physics 2e, Ch.15)
Physics sources state the same law as
**ΔE_int = Q − W**
where Q is heat added to the system and **W is work done *by* the system** (positive when the system expands and pushes on its surroundings). This is the *opposite* work-sign convention from the chemistry form above (ΔU = q + w, w = work done *on* the system); the two are identical physics, just with W = −w. Internal energy is written E_int in physics, U in chemistry. The physics treatment emphasizes that ΔE_int is path-independent (a state function) while Q and W individually depend on the [[ThermodynamicProcess|process path]] — the basis for analyzing [[HeatEngine|heat engines]] and the [[CarnotCycle]].

## Connections
- [[InternalEnergyThermodynamics]] — the U / E_int that changes
- [[EnthalpyChemistry]] — derived for constant-pressure processes
- [[HeatThermodynamics]] — the q / Q term
- [[ThermodynamicProcess]] — isobaric/isochoric/isothermal/adiabatic specializations of the law
- [[SecondLawOfThermodynamics]] — the companion law that constrains direction and efficiency
- [[ThirdLawOfThermodynamics]] — the third member of the trio (S = 0 at 0 K)
- [[ConservationOfEnergy]] — the general principle this law specializes for thermal systems
- Sources: [[chemistry-2e-ch05-thermochemistry]], [[college-physics-2e-ch15]]
