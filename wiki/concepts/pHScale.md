---
title: "pH and pOH Scale"
type: concept
tags: [chemistry, general-chemistry, acids-bases, equilibrium]
sources: [chemistry-2e-ch14-acid-base-equilibria]
last_updated: 2026-06-07
---

# pH and pOH Scale

The **pH scale** expresses the very small hydronium-ion concentrations of aqueous solutions on a convenient logarithmic scale. The general **p-function** is $\mathrm{p}X = -\log X$ (base-10 log). Thus:

$$\mathrm{pH} = -\log[\mathrm{H_3O^+}] \qquad\Longleftrightarrow\qquad [\mathrm{H_3O^+}] = 10^{-\mathrm{pH}}$$
$$\mathrm{pOH} = -\log[\mathrm{OH^-}] \qquad\Longleftrightarrow\qquad [\mathrm{OH^-}] = 10^{-\mathrm{pOH}}$$

## pH + pOH = pKw

Taking the negative log of the [[WaterAutoionization|ion-product]] $K_w = [\mathrm{H_3O^+}][\mathrm{OH^-}]$ gives

$$\mathrm{pK_w} = \mathrm{pH} + \mathrm{pOH}$$

At 25 °C, Kw = 1.0 × 10⁻¹⁴, so **pH + pOH = 14.00**.

## Classifying solutions (at 25 °C)

| Classification | Ion concentrations | pH at 25 °C |
|---|---|---|
| Acidic | [H₃O⁺] > [OH⁻] | pH < 7 |
| Neutral | [H₃O⁺] = [OH⁻] | pH = 7 |
| Basic | [H₃O⁺] < [OH⁻] | pH > 7 |

Pure water at 25 °C: [H₃O⁺] = 1.0 × 10⁻⁷ M → pH = pOH = 7.00.

## Temperature dependence

Because Kw varies with temperature, the numerical pH boundaries shift. At 80 °C neutral water has [H₃O⁺] = 4.9 × 10⁻⁷ M, so pH = pOH = 6.31; "acidic" then means pH < 6.31. **Neutrality is always [H₃O⁺] = [OH⁻]**, which equals pH = 7 only at 25 °C. Unless noted, reported pH values are for 25 °C.

## Measurement

pH is usually measured directly (pOH is calculated from it):
- **pH meters** — research-grade resolution 0.001 pH units, accuracy ±0.002; portable ~0.01 and ±0.2.
- **Colored indicators / pH paper** — universal indicator dyes give different colors across roughly pH 1–12; see [[AcidBaseIndicator]].

## Connections
- [[WaterAutoionization]] — Kw defines the pH/pOH relationship
- [[AcidIonizationConstant]] — pKa = −log Ka uses the same p-function
- [[HendersonHasselbalch]] — relates pH to pKa and conjugate-pair ratio
- [[AcidBaseIndicator]] — visual pH estimation
- [[chemistry-2e-ch14-acid-base-equilibria]] — source chapter (§14.2)

> Disambiguation: this is the chemistry pH/acidity scale, distinct from any logarithmic "scale" usage elsewhere in the wiki.
