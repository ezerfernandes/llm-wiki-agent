---
title: "Equilibrium Constant (K)"
type: concept
tags: [chemistry, general-chemistry, equilibrium]
sources: [chemistry-2e-ch13-fundamental-equilibrium-concepts, chemistry-2e-ch15-equilibria-other-reaction-classes, chemistry-2e-ch16-thermodynamics]
last_updated: 2026-06-07
---

# Equilibrium Constant (K)

The **equilibrium constant, K**, is the constant value the [[ReactionQuotient|reaction quotient]] Q takes once a system reaches [[ChemicalEquilibrium|equilibrium]]:

$$K \equiv Q \ \text{at equilibrium}$$

For $m\mathrm{A} + n\mathrm{B} \rightleftharpoons x\mathrm{C} + y\mathrm{D}$ the concentration form is

$$K_c = \frac{[\mathrm{C}]^x[\mathrm{D}]^y}{[\mathrm{A}]^m[\mathrm{B}]^n}$$

By the [[LawOfMassAction|law of mass action]], at a fixed temperature every starting mixture of a given reaction converges to the **same** K, regardless of initial amounts.

## Magnitude of K

- **Large K** → equilibrium lies toward **products**; most reactant is converted before equilibrium is reached.
- **Small K** → equilibrium lies toward **reactants**; very little reactant is converted.

K's magnitude says **nothing** about *how fast* equilibrium is reached — that is a kinetics question ([[ReactionRate]]), not a thermodynamic one.

## Kc versus Kp

For gas-phase reactions K can be written with molar concentrations (**Kc**) or partial pressures (**Kp**). They are related through the [[IdealGasLawChemistry|ideal gas law]] (M = n/V = P/RT):

$$K_p = K_c (RT)^{\Delta n}$$

- $R$ = 0.0821 L·atm·mol⁻¹·K⁻¹
- $T$ = absolute temperature (K)
- $\Delta n$ = (moles of gaseous products) − (moles of gaseous reactants)

When $\Delta n = 0$, $K_p = K_c$.

## Thermodynamic origin of K

K is fixed by the standard [[GibbsFreeEnergy|Gibbs free energy]] change of the reaction ([[GibbsFreeEnergyAndEquilibrium|Ch 16]]):

$$\Delta G^\circ = -RT \ln K \qquad\Longleftrightarrow\qquad K = e^{-\Delta G^\circ/RT}$$

so K > 1 corresponds to ΔG° < 0 (products favored) and K < 1 to ΔG° > 0 (reactants favored). Because ΔG° = ΔH° − TΔS° depends on temperature, this is the thermodynamic reason K changes with temperature.

## K depends on temperature

K is constant at a *given* temperature but **changes when temperature changes** (because the underlying [[RateConstant|rate constants]] do): $K_c = k_f/k_r$. This temperature dependence is the basis for the temperature part of [[LeChatelierPrinciple|Le Châtelier's principle]].

## Combining (coupled) equilibria

When equilibrium equations are manipulated, K transforms predictably:

1. **Reverse an equation** → $K' = 1/K$
2. **Multiply all coefficients by a factor $x$** → $K' = K^{x}$
3. **Add two equations** → $K_\text{overall} = K_1 \times K_2$

These rules are exactly what makes [[CoupledEquilibria|coupled equilibria]] (Ch 15) tractable: e.g. adding a dissolution to a complex-formation reaction gives K = Ksp × Kf, and adding it to the reverse of an acid ionization gives K = Ksp/Ka. Specialized equilibrium constants in this chapter include the [[SolubilityProduct|solubility product Ksp]] and the [[FormationConstant|formation constant Kf]].

## Connections
- [[ReactionQuotient]] — K is the equilibrium value of Q
- [[LawOfMassAction]] — guarantees a single K per reaction per temperature
- [[ChemicalEquilibrium]] — the state K describes
- [[IdealGasLawChemistry]] — supplies the (RT)^Δn link between Kp and Kc
- [[LeChatelierPrinciple]] — only temperature changes K's value
- [[EquilibriumCalculations]] — K plugged into ICE tables to solve for concentrations
- [[ReactionRate]] — K = k_f/k_r, but K does not set the speed
- [[SolubilityProduct]] / [[FormationConstant]] — Ksp and Kf, specialized equilibrium constants (Ch 15)
- [[CoupledEquilibria]] — multiplying/inverting K applied to combined equilibria (Ch 15)
- [[GibbsFreeEnergyAndEquilibrium]] — ΔG° = −RT ln K, the thermodynamic source of K (Ch 16)
- [[chemistry-2e-ch13-fundamental-equilibrium-concepts]] — source chapter (§13.2)
- [[chemistry-2e-ch15-equilibria-other-reaction-classes]] — source chapter (§15.1–15.3, Ksp/Kf and coupled K)
- [[chemistry-2e-ch16-thermodynamics]] — ΔG° = −RT ln K (Ch 16, §16.4)
