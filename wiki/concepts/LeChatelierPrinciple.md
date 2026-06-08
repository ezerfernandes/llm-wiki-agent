---
title: "Le Châtelier's Principle"
type: concept
tags: [chemistry, general-chemistry, equilibrium]
sources: [chemistry-2e-ch13-fundamental-equilibrium-concepts, chemistry-2e-ch15-equilibria-other-reaction-classes]
last_updated: 2026-06-07
---

# Le Châtelier's Principle

**Le Châtelier's principle**: *if an equilibrium system is stressed, the system will experience a shift in response to the stress that re-establishes equilibrium.* A "stress" is any change that makes the forward and reverse [[ReactionRate|rates]] temporarily unequal; the system then shifts (net forward or net reverse) until the rates re-balance.

Quantitatively, a stress moves the [[ReactionQuotient|reaction quotient]] Q away from the [[EquilibriumConstant|equilibrium constant]] K, and the reaction shifts in the direction that restores Q = K.

## Change in concentration

For $\mathrm{H_2(g) + I_2(g) \rightleftharpoons 2HI(g)}$:

- **Add reactant** or **remove product** → Q < K → shifts **right** (toward products).
- **Remove reactant** or **add product** → Q > K → shifts **left** (toward reactants).

**K is unchanged** by concentration adjustments — only the equilibrium *composition* moves.

## Change in pressure / volume (gases only)

Since $M = n/V = P/RT$, changing volume changes all partial pressures together. The net effect depends on the **moles of gas** on each side:

- **Equal moles of gas** on both sides → compressing or expanding multiplies numerator and denominator equally → Q stays equal to K → **no shift**. (E.g. H₂ + I₂ ⇌ 2HI: 2 mol ⇌ 2 mol.)
- **Unequal moles** → a **volume decrease (pressure increase)** shifts toward the side with **fewer moles of gas**; a volume increase shifts toward more moles. (E.g. 2NO₂ ⇌ 2NO + O₂: compressing shifts left, toward the 2-mole side.)

K is again unchanged.

## Change in temperature — the only stress that changes K

Treat **heat as a reactant or product** using the sign of [[EnthalpyChemistry|ΔH]]:

- **Endothermic** (ΔH > 0), e.g. heat + N₂O₄(g) ⇌ 2NO₂(g): **heating shifts right**, cooling shifts left.
- **Exothermic** (ΔH < 0), e.g. N₂(g) + 3H₂(g) ⇌ 2NH₃(g) + heat: **heating shifts left**, cooling shifts right.

Because $K_c = k_f/k_r$ and rate constants are temperature-dependent ([[ArrheniusEquation|Arrhenius]]), temperature is the one stress that actually **changes the value of K**, not just the composition.

## Catalysts do *not* shift equilibrium

A [[Catalysis|catalyst]] lowers the [[ActivationEnergy|activation energy]] of the forward **and** reverse reactions equally, so both rates rise by the same factor. Equilibrium is reached **faster**, but the position and the value of K are **unchanged**.

## Worked context: the Haber–Bosch process

Ammonia synthesis $\mathrm{N_2(g) + 3H_2(g) \rightleftharpoons 2NH_3(g)}$, ΔH = −92.2 kJ, has a small Kp and a slow rate. Industry combines several Le Châtelier levers: **high pressure (150–250 atm)** shifts toward the fewer-mole product side; **continuous removal of NH₃** keeps Q below K; a **catalyst** plus a **moderate-temperature compromise (400–500 °C)** trades a little equilibrium yield for an acceptable rate.

## Applications to solubility equilibria (Ch 15)

The same principle governs dissolution equilibria. Adding a shared ion stresses the equilibrium toward the solid — the [[CommonIonEffect|common-ion effect]] that lowers [[Solubility|solubility]]. Conversely, *removing* a dissolution product (via acid neutralizing a basic anion, or a [[Ligand|ligand]] forming a [[ComplexIon|complex ion]] with the metal) shifts dissolution forward and increases solubility — the mechanism behind [[CoupledEquilibria|coupled equilibria]].

## Connections
- [[CommonIonEffect]] — Le Châtelier applied to dissolution (lowers solubility, Ch 15)
- [[CoupledEquilibria]] — removing a product ion raises solubility (Ch 15)
- [[ReactionQuotient]] — a stress moves Q off K; the shift restores Q = K
- [[EquilibriumConstant]] — only temperature changes K's value
- [[ChemicalEquilibrium]] — the state being perturbed and restored
- [[ReactionRate]] — a stress makes forward/reverse rates temporarily unequal
- [[Catalysis]] — speeds equilibrium but does not shift it
- [[EnthalpyChemistry]] — ΔH sign sets the temperature-shift direction
- [[ArrheniusEquation]] — temperature dependence of k_f and k_r behind K(T)
- [[chemistry-2e-ch13-fundamental-equilibrium-concepts]] — source chapter (§13.3)
- [[chemistry-2e-ch15-equilibria-other-reaction-classes]] — source chapter (§15.1, 15.3, solubility shifts)
