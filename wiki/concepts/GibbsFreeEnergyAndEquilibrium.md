---
title: "Free Energy and the Equilibrium Constant (ΔG° = −RT ln K)"
type: concept
tags: [chemistry, thermodynamics, equilibrium, general-chemistry]
sources: [chemistry-2e-ch16-thermodynamics, chemistry-2e-ch17-electrochemistry]
last_updated: 2026-06-07
---

# Free Energy and the Equilibrium Constant

The standard [[GibbsFreeEnergy|Gibbs free energy]] change of a reaction is tied directly to its [[EquilibriumConstant|equilibrium constant K]]:

$$\Delta G^\circ = -RT \ln K \qquad\Longleftrightarrow\qquad K = e^{-\Delta G^\circ / RT}$$

with **R = 8.314 J mol⁻¹ K⁻¹** and T in kelvin.

| K | ΔG° | Position |
|---|---|---|
| K > 1 | ΔG° < 0 | products favored |
| K < 1 | ΔG° > 0 | reactants favored |
| K = 1 | ΔG° = 0 | comparable amounts |

## Nonstandard Conditions
Away from standard state, the free energy change depends on the [[ReactionQuotient|reaction quotient Q]]:

$$\Delta G = \Delta G^\circ + RT \ln Q$$

This predicts the direction of spontaneous change under *any* conditions:
- Q < K ⇒ ΔG < 0 ⇒ reaction proceeds **forward**.
- Q > K ⇒ ΔG > 0 ⇒ reaction proceeds in **reverse**.
- Q = K ⇒ ΔG = 0 ⇒ system at [[ChemicalEquilibrium|equilibrium]] (recovering ΔG° = −RT ln K).

## Electrochemical Form
Combining ΔG° = −RT ln K with the electrochemical ΔG° = −nF·E°cell yields the link between a cell's [[CellPotential|standard potential]] and the equilibrium constant:

$$E^\circ_\text{cell} = \frac{RT}{nF}\ln K = \frac{0.0592\text{ V}}{n}\log K \quad (298\text{ K})$$

Away from standard state, the same ΔG = ΔG° + RT ln Q relation becomes the [[NernstEquation|Nernst equation]] E_cell = E°cell − (RT/nF)ln Q; at equilibrium Q = K and E_cell = 0.

## Applications
- Equilibrium constants — including the solubility product Ksp — can be computed from thermodynamic data via K = e^(−ΔG°/RT).
- This bridges the thermodynamics of Chapter 16 with the equilibrium treatment of Chapters 13–15, and with electrochemistry in Chapter 17.

## Connections
- [[GibbsFreeEnergy]] — ΔG° = ΔH° − TΔS° supplies the ΔG° used here
- [[EquilibriumConstant]] — the K this relates to ΔG°
- [[ChemicalEquilibrium]] — the state reached when Q = K (ΔG = 0)
- [[ReactionQuotient]] — Q in ΔG = ΔG° + RT ln Q
- [[StandardFreeEnergyOfFormation]] — a source of ΔG° values
- [[CellPotential]] — E°cell = (RT/nF)ln K, the electrochemical form (Ch 17)
- [[NernstEquation]] — the ΔG = ΔG° + RT ln Q relation cast in potentials
- [[chemistry-2e-ch16-thermodynamics]] — source chapter (§16.4)
- [[chemistry-2e-ch17-electrochemistry]] — E°cell ↔ K and the Nernst equation (§17.4)
