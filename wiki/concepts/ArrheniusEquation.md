---
title: "Arrhenius Equation"
type: concept
tags: [chemistry, general-chemistry, kinetics]
sources: [chemistry-2e-ch12-kinetics]
last_updated: 2026-06-07
---

# Arrhenius Equation

The **Arrhenius equation** is the quantitative form of [[CollisionTheory|collision theory]], relating the [[RateConstant|rate constant]] to temperature and the [[ActivationEnergy|activation energy]]:

$$k = A\,e^{-E_a/RT}$$

- $k$ — rate constant
- $A$ — **frequency factor** (pre-exponential factor): reflects the frequency of collisions *and* the fraction with correct orientation; a larger A means conditions more favorable to productive collisions
- $E_a$ — activation energy (J/mol)
- $R$ — gas constant, 8.314 J mol⁻¹ K⁻¹
- $T$ — temperature (K)

The exponential term $e^{-E_a/RT}$ is the fraction of molecules with enough energy to clear the activation barrier; raising T increases this fraction and thus k.

## Linear form (finding Eₐ)

$$\ln k = \left(-\frac{E_a}{R}\right)\frac{1}{T} + \ln A$$

A plot of **ln k vs 1/T** is a straight line: slope = −Eₐ/R (so Eₐ = −slope × R) and intercept = ln A.

## Two-temperature form

From rate constants at two temperatures:

$$\ln\frac{k_1}{k_2} = \frac{E_a}{R}\left(\frac{1}{T_2}-\frac{1}{T_1}\right)$$

which rearranges to give Eₐ from just two (k, T) measurements.

## Connections
- [[RateConstant]] — the k this equation predicts
- [[ActivationEnergy]] — the Eₐ extracted from the slope
- [[CollisionTheory]] — A encodes frequency + orientation; the exponential encodes the energy postulate
- [[Temperature]] — the T dependence of rate
- [[chemistry-2e-ch12-kinetics]] — source chapter (§12.5)
