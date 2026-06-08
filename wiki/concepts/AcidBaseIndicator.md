---
title: "Acid-Base Indicator"
type: concept
tags: [chemistry, general-chemistry, acids-bases, analytical-chemistry, equilibrium]
sources: [chemistry-2e-ch14-acid-base-equilibria]
last_updated: 2026-06-07
---

# Acid-Base Indicator

An **acid-base indicator** is a weak organic acid (or base) whose acid form and conjugate-base form have **different colors**, used to signal the [[pHScale|pH]] / end point of an [[AcidBaseTitration|acid-base titration]]. For an indicator HIn:

$$\mathrm{HIn(aq) + H_2O(l) \rightleftharpoons H_3O^+(aq) + In^-(aq)}$$

Example — methyl orange: HIn is red, In⁻ is yellow, with Ka = 4.0 × 10⁻⁴.

## Color depends on the ratio

The observed color is set by the ratio [In⁻]/[HIn], given (like a [[BufferSolution|buffer]]) by [[HendersonHasselbalch|Henderson-Hasselbalch]]:

$$\mathrm{pH} = \mathrm{p}K_a + \log\frac{[\mathrm{In^-}]}{[\mathrm{HIn}]}$$

- pH < pKa → mostly HIn (acid color, e.g. red);
- pH > pKa → mostly In⁻ (base color, e.g. yellow);
- pH ≈ pKa → mixture (intermediate color, e.g. orange).

## Color-change interval and selection

The **color-change interval** (pH interval) is the pH range over which the visible change occurs, approximately **pKa ± 1** for most indicators. To choose an indicator for a titration, its interval must lie within the steep part of the [[TitrationCurve|titration curve]] so the **end point ≈ equivalence point**:
- *Strong acid / strong base:* methyl orange, litmus, or phenolphthalein all work (large vertical jump spans many indicators).
- *Weak acid / strong base:* only phenolphthalein is suitable — its interval brackets the (basic) equivalence point, whereas methyl orange changes color well before equivalence and litmus just before it.

## Connections
- [[AcidBaseTitration]] — endpoint detection
- [[TitrationCurve]] — interval must match the steep region
- [[HendersonHasselbalch]] — predicts the [In⁻]/[HIn] color ratio
- [[pHScale]] — universal-indicator/pH-paper estimation
- [[AcidIonizationConstant]] — the indicator's own Ka/pKa
- [[chemistry-2e-ch14-acid-base-equilibria]] — source chapter (§14.7)

> Disambiguation: chemistry acid-base *indicator* dye — not a metric/finance/KPI "indicator".
