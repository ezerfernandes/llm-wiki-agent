---
title: "Nernst Equation"
type: concept
tags: [chemistry, general-chemistry, electrochemistry, redox, equilibrium]
sources: [chemistry-2e-ch17-electrochemistry]
last_updated: 2026-06-07
---

# Nernst Equation

The **Nernst equation** gives the [[CellPotential|cell potential]] of a redox system under **nonstandard conditions** — arbitrary concentrations, pressures, and temperature — in terms of the standard cell potential and the [[ReactionQuotient|reaction quotient Q]].

## Derivation and Forms
Starting from the free-energy dependence on composition, ΔG = ΔG° + RT ln Q, and substituting ΔG = −nFE_cell and ΔG° = −nFE°cell:
$$-nFE_\text{cell} = -nFE^\circ_\text{cell} + RT \ln Q$$
$$\boxed{E_\text{cell} = E^\circ_\text{cell} - \frac{RT}{nF}\ln Q}$$
At **298 K (25 °C)**, folding in R = 8.314 J mol⁻¹ K⁻¹ and F = 96,485 C/mol and converting to base-10 log:
$$E_\text{cell} = E^\circ_\text{cell} - \frac{0.0592\text{ V}}{n}\log Q$$
where n = moles of electrons transferred.

## What It Shows
Cell potential is a function of **n, temperature, and composition (Q)**. As a reaction proceeds, Q changes and E_cell drifts toward 0; at equilibrium Q = K, E_cell = 0, and the relation collapses to E°cell = (RT/nF)ln K (see [[GibbsFreeEnergyAndEquilibrium]]).

## Example
Co(s) + Fe²⁺(aq, 1.94 M) → Co²⁺(aq, 0.15 M) + Fe(s): E°cell = −0.17 V, Q = 0.15/1.94 = 0.077, n = 2:
E_cell = −0.17 − (0.0592/2)log(0.077) = −0.17 + 0.033 = **−0.14 V** (still nonspontaneous).

## Special Case: Concentration Cells
A [[ConcentrationCell|concentration cell]] has E°cell = 0, so its entire potential comes from the Nernst term — driven purely by the concentration difference of one species.

## Connections
- [[CellPotential]] — what this computes off standard
- [[StandardReductionPotential]] — supplies E°cell
- [[ReactionQuotient]] — Q in the equation
- [[ConcentrationCell]] — the E°cell = 0 application
- [[GibbsFreeEnergyAndEquilibrium]] — the ΔG = ΔG° + RT ln Q this derives from; equilibrium limit E°cell = (RT/nF)ln K
- [[Electrochemistry]] — the broader field
- [[chemistry-2e-ch17-electrochemistry]] — source chapter (§17.4)
