---
title: "Clausius-Clapeyron Equation"
type: concept
tags: [chemistry, general-chemistry, phases, thermochemistry]
sources: [chemistry-2e-ch10-liquids-and-solids]
last_updated: 2026-06-07
---

# Clausius-Clapeyron Equation

The **Clausius-Clapeyron equation** gives the quantitative dependence of a liquid's [[VaporPressureChemistry|vapor pressure]] on temperature:

$$P = A\,e^{-\Delta H_{vap}/RT}$$

- *P* — vapor pressure
- ΔH_vap — [[PhaseTransitionChemistry|enthalpy of vaporization]] (J/mol)
- *R* — gas constant, 8.3145 J/mol·K
- *A* — substance-dependent constant
- *T* — temperature in **kelvin**

## Logarithmic and Two-Point Forms

$$\ln P = -\frac{\Delta H_{vap}}{RT} + \ln A$$

A plot of ln P vs 1/T is linear with slope −ΔH_vap/R. The **two-point form** (units of P consistent, T in K) is most convenient:

$$\ln\!\left(\frac{P_2}{P_1}\right) = \frac{\Delta H_{vap}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$$

## Worked Uses

- **Finding ΔH_vap:** isooctane has P = 10.0 kPa at 307.2 K and 100.0 kPa at 372.0 K → ΔH_vap = R·ln(P₂/P₁)/(1/T₁ − 1/T₂) = 33,800 J/mol = 33.8 kJ/mol. (Ethanol ≈ 41.4 kJ/mol.)
- **Finding boiling point at a new pressure:** benzene (normal bp 353.3 K, ΔH_vap 30.8 kJ/mol) at Denver's 83.4 kPa boils at T₂ = (−R·ln(P₂/P₁)/ΔH_vap + 1/T₁)⁻¹ = 346.9 K = 73.8 °C.

## Connections
- [[VaporPressureChemistry]] — the quantity it predicts
- [[PhaseTransitionChemistry]] — supplies ΔH_vap
- [[EnthalpyChemistry]] — enthalpy of vaporization is an enthalpy change
