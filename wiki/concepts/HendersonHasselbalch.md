---
title: "Henderson-Hasselbalch Equation"
type: concept
tags: [chemistry, general-chemistry, acids-bases, equilibrium]
sources: [chemistry-2e-ch14-acid-base-equilibria]
last_updated: 2026-06-07
---

# Henderson-Hasselbalch Equation

The **Henderson-Hasselbalch equation** gives the [[pHScale|pH]] of a [[BufferSolution|buffer]] (or any weak [[ConjugateAcidBasePair|conjugate acid-base pair]]) directly from the acid's pKa and the ratio of the conjugate-base to weak-acid concentrations:

$$\mathrm{pH} = \mathrm{p}K_a + \log\frac{[\mathrm{A^-}]}{[\mathrm{HA}]}$$

## Derivation

Start from the [[AcidIonizationConstant|acid ionization]] expression and solve for [H₃O⁺]:

$$K_a = \frac{[\mathrm{H_3O^+}][\mathrm{A^-}]}{[\mathrm{HA}]} \;\Longrightarrow\; [\mathrm{H_3O^+}] = K_a\frac{[\mathrm{HA}]}{[\mathrm{A^-}]}$$

Take the negative base-10 logarithm of both sides:

$$-\log[\mathrm{H_3O^+}] = -\log K_a - \log\frac{[\mathrm{HA}]}{[\mathrm{A^-}]} \;\Longrightarrow\; \mathrm{pH} = \mathrm{p}K_a + \log\frac{[\mathrm{A^-}]}{[\mathrm{HA}]}$$

## Interpretation and validity

- When [A⁻] = [HA], the log term is zero and **pH = pKa** — the buffer's center point (and the half-equivalence point of a weak-acid [[AcidBaseTitration|titration]]).
- A 10:1 ratio shifts pH by one unit from pKa; buffers work well within roughly pKa ± 1.
- The equation assumes the "x is small" approximation holds — i.e. the equilibrium concentrations of HA and A⁻ are well approximated by their formal (added) amounts. It also applies to [[AcidBaseIndicator|indicators]] (a weak acid HIn) to predict the color-determining [In⁻]/[HIn] ratio.

## Connections
- [[BufferSolution]] — the primary application
- [[ConjugateAcidBasePair]] — the [A⁻]/[HA] ratio
- [[AcidIonizationConstant]] — pKa = −log Ka, the anchor term
- [[pHScale]] — what the equation computes
- [[AcidBaseTitration]] — pH = pKa at the half-equivalence point
- [[AcidBaseIndicator]] — same form predicts indicator color
- [[chemistry-2e-ch14-acid-base-equilibria]] — source chapter (§14.6, §14.7)
