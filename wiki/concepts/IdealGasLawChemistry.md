---
title: "Ideal Gas Law (Chemistry)"
type: concept
tags: [chemistry, general-chemistry, gases]
sources: [chemistry-2e-ch09-gases]
last_updated: 2026-06-07
---

# Ideal Gas Law (Chemistry)

The **ideal gas law** is the equation of state that unifies the four simple [[GasLaws|gas laws]] into a single relationship among pressure, volume, amount, and absolute temperature:

$$PV = nRT$$

where P = pressure, V = volume, n = moles, T = absolute temperature (kelvin), and R = the **ideal (universal) gas constant**. This is the OpenStax *Chemistry 2e* (Ch 9) treatment; the College Physics 2e physics-domain version is the separate [[IdealGasLaw]] page (which uses both the molar form PV = nRT and the molecular form PV = NkT).

## The Gas Constant R

The numerical value of R depends on the units chosen for P, V, T (handled by [[DimensionalAnalysis]]):

- R = **0.08206 L·atm/(mol·K)**
- R = **8.314 kPa·L/(mol·K)** = **8.314 J/(mol·K)**

The equation has five quantities (R plus P, V, n, T); fixing any four determines the fifth. Gases follow it most accurately at **relatively low pressure and high temperature** (see [[RealGases]] for deviations).

**Example:** 655 g CH₄ (40.8 mol) at 298 K and 745 torr (0.980 atm) occupies V = nRT/P = (40.8)(0.08206)(298)/0.980 = 1.02 × 10³ L.

## How It Combines the Simple Laws

| Law | Form |
|---|---|
| [[BoylesLaw|Boyle's]] | PV = const (T, n fixed) |
| Amontons's | P/T = const (V, n fixed) |
| [[CharlesLaw|Charles's]] | V/T = const (P, n fixed) |
| [[AvogadrosLaw|Avogadro's]] | V/n = const (P, T fixed) |

Combining the first three gives the combined gas law P₁V₁/T₁ = P₂V₂/T₂; adding the fourth yields PV = nRT.

## STP and Standard Molar Volume

**Standard conditions of temperature and pressure (STP)** are 273.15 K (0 °C) and 1 atm (101.325 kPa). IUPAC changed the standard pressure to 1 bar in 1982, but 1 atm remains widely used. One mole of an ideal gas at STP occupies the standard [[MolarVolume|molar volume]] ≈ 22.4 L (≈ 22.71 L at the 1-bar standard), independent of identity.

## Extensions

- **Gas density:** d = ℳP/RT (see [[MolarMass]]).
- **Molar mass from measurements:** ℳ = mRT/PV.
- **Mixtures:** [[DaltonsLawOfPartialPressures|Dalton's law]] of partial pressures.
- **Reactions:** [[GasStoichiometry|gas stoichiometry]].

## Connections
- [[GasLaws]] — the four laws it unifies
- [[MolarVolume]] — ≈ 22.4 L at STP
- [[IdealGasLaw]] — the physics-domain treatment (distinct, College Physics 2e)
- [[KineticMolecularTheory]] — the microscopic model justifying ideal behavior
- [[RealGases]] / [[VanDerWaalsEquation]] — when PV = nRT breaks down
- [[GasStoichiometry]] / [[DaltonsLawOfPartialPressures]] / [[MolarMass]] — applications
- [[DimensionalAnalysis]] — selecting the right value of R
- [[chemistry-2e-ch09-gases]] — source chapter (§9.2)
