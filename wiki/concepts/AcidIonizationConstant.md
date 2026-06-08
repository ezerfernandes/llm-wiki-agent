---
title: "Acid Ionization Constant (Ka)"
type: concept
tags: [chemistry, general-chemistry, acids-bases, equilibrium]
sources: [chemistry-2e-ch14-acid-base-equilibria]
last_updated: 2026-06-07
---

# Acid Ionization Constant (Ka)

The **acid ionization constant Ka** is the [[EquilibriumConstant|equilibrium constant]] for the ionization of a [[BronstedLowryAcidsAndBases|Brønsted-Lowry acid]] in water. For

$$\mathrm{HA(aq) + H_2O(l) \rightleftharpoons H_3O^+(aq) + A^-(aq)}$$

$$K_a = \frac{[\mathrm{H_3O^+}][\mathrm{A^-}]}{[\mathrm{HA}]}$$

(Water, the solvent, does not appear.) The larger the Ka, the more H₃O⁺ and A⁻ form relative to nonionized HA, and the **stronger the acid**. Strong acids ionize essentially completely (Ka ≈ ∞); weak acids have small, experimentally measurable Ka. pKa = −log Ka, so a smaller pKa means a stronger acid.

## Computing Ka and equilibrium concentrations

Ka problems use an [[ICETable|ICE table]]:
- **From pH:** convert pH → [H₃O⁺] = 10^(−pH), fill the ICE table, solve for Ka.
- **From Ka:** solve $K_a = x^2/([\mathrm{HA}]_0 - x)$. When ionization is small, approximate $x^2/[\mathrm{HA}]_0 = K_a$. If x exceeds 5% of [HA]₀, drop the approximation and solve the quadratic.

## Relation to Kb and Kw

For a [[ConjugateAcidBasePair|conjugate acid-base pair]], the acid's Ka and its conjugate base's [[BaseIonizationConstant|Kb]] satisfy

$$K_a \times K_b = K_w \quad(= 1.0\times10^{-14}\text{ at }25\,^\circ\mathrm{C})$$

so a stronger acid necessarily has a weaker conjugate base. Molecular-structure trends: down a group acid strength rises as the H–A bond weakens (HF < HCl < HBr < HI); across a period and with higher oxidation number of the central atom of an oxyacid, acidity rises (H₂SO₃ < H₂SO₄; HNO₂ < HNO₃).

## Connections
- [[BaseIonizationConstant]] — the Kb counterpart; Ka·Kb = Kw
- [[ConjugateAcidBasePair]] — the pair linked by Ka·Kb = Kw
- [[WaterAutoionization]] — supplies Kw
- [[PercentIonization]] — an alternative, concentration-dependent strength measure
- [[ICETable]] — bookkeeping for Ka calculations
- [[EquilibriumConstant]] — Ka is a specialized K
- [[PolyproticAcid]] — stepwise Ka1 > Ka2 > Ka3
- [[chemistry-2e-ch14-acid-base-equilibria]] — source chapter (§14.3)
