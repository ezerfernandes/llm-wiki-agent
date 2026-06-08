---
title: "Standard Free Energy of Formation (ΔGf°)"
type: concept
tags: [chemistry, thermodynamics, general-chemistry]
sources: [chemistry-2e-ch16-thermodynamics, chemistry-2e-ch17-electrochemistry]
last_updated: 2026-06-07
---

# Standard Free Energy of Formation (ΔGf°) and ΔG°

The **standard free energy of formation (ΔGf°)** is the [[GibbsFreeEnergy|Gibbs free energy]] change accompanying the formation of **one mole** of a substance from its constituent elements in their standard states (1 bar, conventionally 298.15 K). By definition:

> ΔGf° = 0 for an element in its standard state.

This mirrors the convention for the [[StandardEnthalpyOfFormation|standard enthalpy of formation ΔHf°]].

## ΔG° of Reaction from Formation Values
For mA + nB → xC + yD:

$$\Delta G^\circ = \sum \nu\,\Delta G_f^\circ(\text{products}) - \sum \nu\,\Delta G_f^\circ(\text{reactants})$$
$$\Delta G^\circ = [x\,\Delta G_f^\circ(C) + y\,\Delta G_f^\circ(D)] - [m\,\Delta G_f^\circ(A) + n\,\Delta G_f^\circ(B)]$$

This is the same products-minus-reactants pattern as [[HessLaw|Hess's law]] / [[StandardEnthalpyOfFormation|ΔH°_rxn]].

## Two Equivalent Routes to ΔG°
ΔG° computed from ΔGf° tables equals ΔG° computed from ΔH° and S° via **ΔG° = ΔH° − TΔS°** (using [[StandardEnthalpyOfFormation|ΔHf°]] and [[StandardMolarEntropy|S°]] data). Both methods give identical results; the formation-value route is faster when ΔGf° tables are available, while the ΔH° − TΔS° route is needed to study temperature dependence.

## Connections
- [[GibbsFreeEnergy]] — the G whose formation change this is
- [[StandardEnthalpyOfFormation]] — parallel ΔHf° convention and summation
- [[StandardMolarEntropy]] — S° used in the ΔG° = ΔH° − TΔS° route
- [[HessLaw]] — the products-minus-reactants additivity
- [[GibbsFreeEnergyAndEquilibrium]] — ΔG° → K via ΔG° = −RT ln K
- [[CellPotential]] — ΔG° also equals −nFE°cell for redox cells (Ch 17)
- [[chemistry-2e-ch16-thermodynamics]] — source chapter (§16.4)
- [[chemistry-2e-ch17-electrochemistry]] — ΔG° linked to cell potential (§17.4)
