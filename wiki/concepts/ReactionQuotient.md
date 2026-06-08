---
title: "Reaction Quotient (Q)"
type: concept
tags: [chemistry, general-chemistry, equilibrium]
sources: [chemistry-2e-ch13-fundamental-equilibrium-concepts, chemistry-2e-ch15-equilibria-other-reaction-classes]
last_updated: 2026-06-07
---

# Reaction Quotient (Q)

The **reaction quotient, Q**, is the mass-action ratio of product terms to reactant terms evaluated at **any** point during a reaction (not only at equilibrium). For a general [[ReversibleReaction|reversible reaction]]

$$m\mathrm{A} + n\mathrm{B} \rightleftharpoons x\mathrm{C} + y\mathrm{D}$$

the concentration-based quotient is

$$Q_c = \frac{[\mathrm{C}]^x[\mathrm{D}]^y}{[\mathrm{A}]^m[\mathrm{B}]^n}$$

and, for gases, the pressure-based quotient is

$$Q_p = \frac{(P_\mathrm{C})^x(P_\mathrm{D})^y}{(P_\mathrm{A})^m(P_\mathrm{B})^n}$$

Each species' term is raised to its stoichiometric coefficient. (These are simplifications of more rigorous expressions that use *relative*, dimensionless activities; pure solids and pure liquids therefore drop out — see [[HeterogeneousEquilibrium]].)

## Q changes as the reaction proceeds

Q starts far from its equilibrium value and evolves as concentrations change. When the system reaches equilibrium, Q stops changing and equals the [[EquilibriumConstant|equilibrium constant]] K — this constancy is the [[LawOfMassAction|law of mass action]].

## Comparing Q to K predicts direction

| Comparison | Meaning | Net direction |
|---|---|---|
| **Q < K** | too few products | shifts **forward** (→ products) |
| **Q > K** | too many products | shifts **reverse** (→ reactants) |
| **Q = K** | mass-action ratio matches K | **at equilibrium** (no net change) |

This Q-vs-K test is also the quantitative engine behind [[LeChatelierPrinciple|Le Châtelier's principle]] and the first step of most [[EquilibriumCalculations|equilibrium calculations]].

## Solubility application: Qsp vs Ksp (Ch 15)

For a dissolution equilibrium the quotient Qsp = [ion]^p[ion]^q (the ion-product) is compared with the [[SolubilityProduct|solubility product Ksp]] to predict [[PrecipitationReaction|precipitation]]: Qsp < Ksp (unsaturated, no precipitate), Qsp = Ksp (saturated), Qsp > Ksp (supersaturated, precipitate forms until Qsp = Ksp). This is the same Q-vs-K test specialized to slightly soluble salts.

## Connections
- [[EquilibriumConstant]] — the value Q takes at equilibrium (K ≡ Q at equilibrium)
- [[SolubilityProduct]] — Qsp vs Ksp predicts precipitation (Ch 15)
- [[LawOfMassAction]] — why Q is constant at equilibrium
- [[ChemicalEquilibrium]] — the state Q diagnoses
- [[LeChatelierPrinciple]] — Q vs K explains directional shifts
- [[EquilibriumCalculations]] — Q comparison sets up ICE-table problems
- [[HeterogeneousEquilibrium]] — solids/liquids omitted from Q
- [[chemistry-2e-ch13-fundamental-equilibrium-concepts]] — source chapter (§13.2)
- [[chemistry-2e-ch15-equilibria-other-reaction-classes]] — source chapter (§15.1, Qsp vs Ksp)
