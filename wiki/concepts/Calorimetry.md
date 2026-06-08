---
title: "Calorimetry"
type: concept
tags: [chemistry, physics, thermochemistry, measurement]
sources: [chemistry-2e-ch05-thermochemistry, college-physics-2e-ch14]
last_updated: 2026-06-07
---

# Calorimetry

**Calorimetry** is a technique for measuring the amount of [[HeatThermodynamics|heat]] transferred to or from a substance during a chemical or physical process. A **calorimeter** is the device used; the measurement requires defining the [[ThermodynamicSystem|system]] (the substance/reaction of interest) and its surroundings.

## Governing Principle
In an idealized, isolated calorimeter no heat escapes to the wider environment, so heat lost by one body equals heat gained by another:

**q₁ + q₂ = 0**  →  **q₁ = −q₂**

For a reaction carried out in solution:

**q_reaction + q_solution = 0**  →  **q_reaction = −q_solution**

Each substance's heat is found from q = c·m·ΔT (see [[SpecificHeatCapacity]]). An [[ExothermicEndothermic|exothermic]] reaction (q_reaction < 0) warms the solution; an endothermic one (q_reaction > 0) cools it.

## Calorimeter Types
- **Coffee-cup calorimeter** — two nested polystyrene cups with an insulated lid, thermometer, and stirrer. Operates at **constant pressure**, so the measured heat equals the [[EnthalpyChemistry|enthalpy change]] (q_p = ΔH). Simple but allows some heat exchange with the environment, reducing accuracy.
- **Bomb calorimeter** — a robust sealed steel "bomb" submerged in water, charged with sample and high-pressure oxygen and ignited by a spark. Operates at **constant volume**; used for combustion reactions that release large amounts of heat and produce gases. Calibrated with a known reaction (e.g., benzoic acid) to determine the calorimeter's heat capacity (in J/°C) before measurements.

## Physics View (College Physics 2e, Ch.14)
In mechanics/thermal-physics problems the same isolated-system balance is written **Q_cold + Q_hot = 0**: heat lost by hot bodies equals heat gained by cold ones until they reach a common equilibrium temperature. Each term is evaluated with **Q = m·c·ΔT** (see [[SpecificHeatCapacity]]), and any [[PhaseChange]] occurring in range adds a [[LatentHeat]] term (Q = m·L) at constant temperature. This is the standard method for finding final equilibrium temperatures and for identifying unknown materials by their specific heat.

## Connections
- [[ThermodynamicSystem]] — system/surroundings framework
- [[SpecificHeatCapacity]] — q = cmΔT used in every calculation
- [[LatentHeat]] — phase-change energy term in calorimetric balances
- [[ExothermicEndothermic]] — interpreting the sign of the measured heat
- [[EnthalpyChemistry]] — constant-pressure calorimetry yields ΔH directly
- Source: [[chemistry-2e-ch05-thermochemistry]], [[college-physics-2e-ch14]]
