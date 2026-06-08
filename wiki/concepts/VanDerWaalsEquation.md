---
title: "Van der Waals Equation"
type: concept
tags: [chemistry, general-chemistry, gases]
sources: [chemistry-2e-ch09-gases]
last_updated: 2026-06-07
---

# Van der Waals Equation

The **van der Waals equation** (Johannes van der Waals, 1879) is a modified equation of state that approximates [[RealGases|real-gas]] behavior by adding two correction terms to the [[IdealGasLawChemistry|ideal gas law]]:

$$\left(P + \frac{a n^2}{V^2}\right)(V - nb) = nRT$$

## The Two Correction Terms

- **Pressure correction $a n^2/V^2$** — accounts for **intermolecular attractions**, which reduce the observed pressure below the ideal prediction. The constant *a* reflects the strength of attraction between a particular gas's molecules. More important at **low pressures**.
- **Volume correction $nb$** — accounts for the **finite, incompressible volume of the molecules** themselves, subtracted from the container volume. The constant *b* reflects molecular size. More important at **high pressures and small volumes**.

When V is large and n small, both corrections become negligible and the equation reduces to PV = nRT. At low pressure the *a* correction dominates; at high pressure/small volume the *b* correction dominates; at an intermediate pressure the two offset and the gas appears nearly ideal over a small range.

## Selected Constants

| Gas | a (L²·atm/mol²) | b (L/mol) |
|---|---|---|
| N₂ | 1.39 | 0.0391 |
| O₂ | 1.36 | 0.0318 |
| CO₂ | 3.59 | 0.0427 |
| H₂O | 5.46 | 0.0305 |
| He | 0.0342 | 0.0237 |
| CCl₄ | 20.4 | 0.1383 |

## Worked Example

For 3.46 mol CO₂ at 502 K in 4.25 L: the ideal gas law gives P = nRT/V = **33.5 atm**, while the van der Waals equation P = nRT/(V − nb) − n²a/V² gives **32.4 atm** — a 3.3% difference, small at moderate pressure and elevated temperature.

## Connections
- [[RealGases]] — the deviations this equation corrects for
- [[IdealGasLawChemistry]] — the equation it modifies (and reduces to in the dilute limit)
- [[KineticMolecularTheory]] — the *a* and *b* terms restore the size and forces KMT ignores
- [[chemistry-2e-ch09-gases]] — source chapter (§9.6)
