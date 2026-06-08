---
title: "Gibbs Free Energy (G)"
type: concept
tags: [chemistry, thermodynamics, general-chemistry]
sources: [chemistry-2e-ch16-thermodynamics, chemistry-2e-ch17-electrochemistry]
last_updated: 2026-06-07
---

# Gibbs Free Energy (G)

> Disambiguation: this is the *chemical-thermodynamics* free energy (G = H − TS, the spontaneity criterion for reactions). It is unrelated to the ML/neuroscience "free energy principle" and to Helmholtz free energy; the chapter uses "free energy" to mean Gibbs free energy throughout.

The **Gibbs free energy (G)**, named for [[JosiahWillardGibbs]], is the state function

$$G = H - TS$$

where H is [[EnthalpyChemistry|enthalpy]], T is absolute temperature, and S is [[EntropyThermodynamics|entropy]]. At constant temperature and pressure its change is

$$\Delta G = \Delta H - T\Delta S$$

## The System-Only Spontaneity Criterion
G is derived so that spontaneity can be judged from **system properties alone**, without computing the surroundings. Substituting ΔS_surr = −ΔH/T into the [[SecondLawOfThermodynamics|second law]] (ΔS_univ = ΔS_sys − ΔH/T) and multiplying by −T:

$$\Delta G = -T\,\Delta S_{\text{univ}}$$

Since ΔS_univ > 0 marks spontaneity, the sign of ΔG (opposite, because of the −T factor) gives:

| ΔG | Process |
|---|---|
| < 0 | Spontaneous |
| = 0 | At equilibrium |
| > 0 | Nonspontaneous |

## Temperature Dependence — Four ΔH/ΔS Cases
Because ΔG = ΔH − TΔS, the signs of ΔH and ΔS determine how spontaneity changes with T:

| ΔH | ΔS | Behavior |
|---|---|---|
| − | + | Spontaneous at **all** T (ΔG < 0 always) |
| + | − | Nonspontaneous at **all** T (ΔG > 0 always) |
| − | − | Spontaneous at **low** T (T < ΔH/ΔS) |
| + | + | Spontaneous at **high** T (T > ΔH/ΔS) |

When ΔH and ΔS have the **same sign**, there is a **crossover (threshold) temperature** where ΔG = 0 and the system is at equilibrium:

$$T = \frac{\Delta H}{\Delta S}$$

A phase change's normal transition temperature (e.g. a boiling point) is exactly this T where ΔG = 0; estimates from thermodynamic data closely match experiment.

## Computing ΔG°
The standard free energy change can be found two equivalent ways:
- From enthalpy and entropy: ΔG° = ΔH° − TΔS°.
- From [[StandardFreeEnergyOfFormation|standard free energies of formation]]: ΔG° = Σν ΔGf°(products) − Σν ΔGf°(reactants).

ΔG° connects to the [[EquilibriumConstant|equilibrium constant]] through [[GibbsFreeEnergyAndEquilibrium|ΔG° = −RT ln K]].

## Electrochemical Form
For a redox reaction run in an [[ElectrochemicalCell|electrochemical cell]], the maximum work is electrical work, giving the central bridge of [[Electrochemistry|electrochemistry]]:

$$\Delta G^\circ = -nF\,E^\circ_\text{cell}$$

where n is the moles of electrons transferred, F = 96,485 C/mol is the [[FaradaysLawsOfElectrolysis|Faraday constant]], and E°cell is the [[CellPotential|standard cell potential]]. Thus ΔG° < 0 ⇔ E°cell > 0 (a spontaneous [[GalvanicCell|galvanic cell]]).

## Connections
- [[EnthalpyChemistry]] — the ΔH term
- [[EntropyThermodynamics]] — the ΔS term
- [[SecondLawOfThermodynamics]] — ΔG = −TΔS_univ derivation
- [[SpontaneousProcess]] — ΔG < 0 makes the dispersal-driven spontaneity quantitative
- [[StandardFreeEnergyOfFormation]] — ΔGf° tables for ΔG°
- [[GibbsFreeEnergyAndEquilibrium]] — ΔG° = −RT ln K and ΔG = ΔG° + RT ln Q
- [[CellPotential]] — ΔG° = −nFE°cell links free energy to electrochemistry (Ch 17)
- [[Electrochemistry]] — redox application of the spontaneity criterion
- [[JosiahWillardGibbs]] — namesake
- [[chemistry-2e-ch16-thermodynamics]] — source chapter (§16.4)
- [[chemistry-2e-ch17-electrochemistry]] — ΔG° = −nFE°cell electrochemical form (§17.4)
