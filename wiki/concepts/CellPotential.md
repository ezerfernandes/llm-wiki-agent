---
title: "Cell Potential (E_cell)"
type: concept
tags: [chemistry, general-chemistry, electrochemistry, redox]
sources: [chemistry-2e-ch17-electrochemistry]
last_updated: 2026-06-07
---

# Cell Potential (E_cell)

The **cell potential (E_cell)** is the difference in [[StandardReductionPotential|electrode potential]] between the two half-cells of an [[ElectrochemicalCell|electrochemical cell]] — the net driving force for electron transfer, measured in **volts (1 V = 1 J/C)**.

> Disambiguation: this is the *chemistry* potential of a redox cell (a.k.a. cell voltage / electromotive force of the cell), defined relative to the [[StandardHydrogenElectrode|standard hydrogen electrode]]. It is related to, but narrower than, the physics notions of [[Voltage]] and [[ElectricPotential]].

## Definition
A single half-cell's potential cannot be measured alone; only the difference between two half-cells is observable:
$$E_\text{cell} = E_\text{cathode} - E_\text{anode}$$
Under standard-state conditions (1 M solutes, 1 bar gases, 298 K) this is the **standard cell potential**:
$$E^\circ_\text{cell} = E^\circ_\text{cathode} - E^\circ_\text{anode}$$

## Sign and Spontaneity
- **E°cell > 0** ⇒ spontaneous reaction ⇒ a [[GalvanicCell|galvanic cell]] (and ΔG° < 0).
- **E°cell < 0** ⇒ nonspontaneous ⇒ requires [[ElectrolysisChemistry|electrolysis]] to drive.
- Reversing the reaction reverses the cathode/anode assignment and **flips the sign** of E°cell.

Standard electrode potentials are **intensive**: they are *not* multiplied by stoichiometric coefficients. E.g., for Cu + 2Ag⁺ → Cu²⁺ + 2Ag, E°cell = E°Ag − E°Cu = 0.7996 − 0.34 = **+0.46 V**, using E°Ag as listed despite the factor of 2.

## Beyond Standard State
At nonstandard concentrations/pressures, use the [[NernstEquation|Nernst equation]]: E_cell = E°cell − (0.0592 V/n)log Q at 298 K.

## Connections
- [[StandardReductionPotential]] — the per-half-cell E° values combined here
- [[StandardHydrogenElectrode]] — the 0 V reference for all electrode potentials
- [[NernstEquation]] — E_cell away from standard conditions
- [[GibbsFreeEnergy]] / [[GibbsFreeEnergyAndEquilibrium]] — ΔG° = −nFE°cell, E°cell = (RT/nF)ln K
- [[GalvanicCell]] / [[ElectrolysisChemistry]] — positive vs negative E°cell
- [[Electrochemistry]] — the broader field
- [[chemistry-2e-ch17-electrochemistry]] — source chapter (§17.3)
