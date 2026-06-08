---
title: "van 't Hoff Factor"
type: concept
tags: [chemistry, general-chemistry, solutions, colligative, electrolytes]
sources: [chemistry-2e-ch11-solutions-and-colloids]
last_updated: 2026-06-07
---

# van 't Hoff Factor

The **van 't Hoff factor (i)** is the multiplier that adapts [[ColligativeProperties|colligative-property]] equations to [[Electrolyte|electrolytes]], which dissociate or ionize into multiple particles:

$$i = \frac{\text{moles of particles in solution}}{\text{moles of formula units dissolved}}$$

Ideally i equals the number of ions per formula unit (1 for nonelectrolytes, 2 for NaCl, 3 for MgCl₂, 4 for FeCl₃). The colligative formulas become:

$$\Delta T_b = i K_b m \qquad \Delta T_f = i K_f m \qquad \Pi = i M R T$$

## Predicted vs. Measured (0.050 m)
| Solute | Type | Products | i (predicted) | i (measured) |
|--------|------|----------|---------------|--------------|
| C₁₂H₂₂O₁₁ (sucrose) | nonelectrolyte | — | 1 | 1.0 |
| NaCl | strong | Na⁺, Cl⁻ | 2 | 1.9 |
| HCl | strong | H₃O⁺, Cl⁻ | 2 | 1.9 |
| MgSO₄ | strong | Mg²⁺, SO₄²⁻ | 2 | 1.3 |
| MgCl₂ | strong | Mg²⁺, 2Cl⁻ | 3 | 2.7 |
| FeCl₃ | strong | Fe³⁺, 3Cl⁻ | 4 | 3.4 |

## Why Measured i Is Lower: Ion Pairing
Measured i values fall below the ideal because of residual interionic attraction. By the **Debye-Hückel theory (1923)**, "although interionic attraction in aqueous solution is very greatly reduced by [[Solvation|solvation]] of the ions and the insulating action of the polar solvent, it is not completely nullified." Cations and anions briefly touch to form solvated **ion pairs**, lowering the effective concentration (activity) of free ions. The effect is largest for highly charged ions (MgSO₄ drops to 1.3). In dilute solutions ions separate widely, attractions weaken, and i approaches its ideal value. This explains why measured ΔT_f for 1.0 m NaCl is 3.4 °C rather than the ideal 3.7 °C.

## Connections
- [[ColligativeProperties]] — i scales all four properties for electrolytes
- [[Electrolyte]] — dissociation/ionization sets the ion count
- [[FreezingPointDepression]] / [[BoilingPointElevation]] / [[OsmoticPressureChemistry]] — equations using i
- [[Solvation]] — reduces but does not eliminate interionic attraction
- [[chemistry-2e-ch11-solutions-and-colloids]] — source chapter
