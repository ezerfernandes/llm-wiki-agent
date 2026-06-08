---
title: "Acid-Base Titration"
type: concept
tags: [chemistry, general-chemistry, acids-bases, analytical-chemistry, equilibrium]
sources: [chemistry-2e-ch14-acid-base-equilibria]
last_updated: 2026-06-07
---

# Acid-Base Titration

An **acid-base titration** measures the concentration of an acid or base by reacting it (neutralization) with a standard solution of known concentration added from a buret, monitoring the [[pHScale|pH]] as titrant is added. It is the acid-base case of [[QuantitativeChemicalAnalysis|quantitative chemical analysis]]; the resulting plot of pH versus titrant volume is a [[TitrationCurve|titration curve]]. The **equivalence point** is where titrant and analyte have reacted in exact stoichiometric proportion.

## pH through the titration

**Strong acid / strong base** (e.g. 0.100 M HCl with 0.100 M NaOH):
- *Initial:* pH set by the strong acid (0.100 M HCl → pH 1.00).
- *Before equivalence:* excess unreacted strong acid sets [H₃O⁺]; pH rises gradually.
- *Equivalence point:* only a neutral salt (NaCl) and water remain — neither ion hydrolyzes — so **pH = 7.00**, in the middle of a steep, near-vertical jump.
- *After equivalence:* excess strong base sets [OH⁻] → pH > 7.

**Weak acid / strong base** (e.g. 0.100 M CH₃CO₂H with 0.100 M NaOH):
- *Initial:* higher pH than an equal-concentration strong acid (2.87 vs 1.00).
- *Half-equivalence point:* [HA] = [A⁻], so by [[HendersonHasselbalch|Henderson-Hasselbalch]] **pH = pKa** (= 4.74 for acetic acid); this region is a [[BufferSolution|buffer]].
- *Equivalence point:* the solution is the conjugate base (acetate), which hydrolyzes ([[SaltHydrolysis|salt hydrolysis]]): **pH > 7** (8.72 here), *not* neutral.
- *After equivalence:* excess strong base dominates.

The steep pH jump near equivalence is what makes endpoint detection sharp; it is smaller and centered above pH 7 for weak-acid titrations.

## Endpoint detection

An [[AcidBaseIndicator|acid-base indicator]] (or a pH meter) marks the **end point**. A well-chosen indicator's color-change interval brackets the steep pH jump so the end point ≈ equivalence point.

## Connections
- [[TitrationCurve]] — the pH-vs-volume plot analyzed here
- [[AcidBaseIndicator]] — visual endpoint detection
- [[HendersonHasselbalch]] — pH = pKa at the half-equivalence point
- [[SaltHydrolysis]] — why the weak-acid equivalence point is basic
- [[BufferSolution]] — the pre-equivalence buffer region
- [[QuantitativeChemicalAnalysis]] — the general titration methodology (Ch 4)
- [[AcidBaseReaction]] — the underlying neutralization
- [[chemistry-2e-ch14-acid-base-equilibria]] — source chapter (§14.7)

> Disambiguation: this is the equilibrium/pH treatment of titration; the Ch 4 stoichiometric mechanics live in [[QuantitativeChemicalAnalysis]].
