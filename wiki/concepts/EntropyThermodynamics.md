---
title: "Entropy (Chemical Thermodynamics)"
type: concept
tags: [chemistry, thermodynamics, general-chemistry]
sources: [chemistry-2e-ch16-thermodynamics]
last_updated: 2026-06-07
---

# Entropy (S) in Chemical Thermodynamics

> Disambiguation: this page is the *chemistry / general-chemistry* treatment of entropy (state function, microstates, standard molar entropy). For the **information-theory** measure (Shannon entropy used in ML) see [[Entropy]]; for the **physics / heat-engine** treatment (ΔS = Q/T, Carnot, heat death) see [[ThermodynamicEntropy]]. All three share the form S = −Σ p log p / S = k ln W up to constants.

**Entropy (S)** is a thermodynamic **state function**, introduced by [[RudolfClausius]] (building on [[SadiCarnot]]), that relates the spontaneous heat flow of a process to the temperature at which it occurs:

$$\Delta S = \frac{q_{\text{rev}}}{T}$$

where q_rev is the reversible heat and T is absolute temperature (K). Because S is a state function, the entropy change of any *real* (irreversible) process equals that of the reversible path between the same initial and final states.

## Statistical Meaning
Microscopically, entropy measures the **dispersal of matter and energy**: more uniformly dispersed configurations correspond to many more accessible microstates and thus higher entropy. The most probable (most dispersed) macrostate is the one of greatest entropy. This is made exact by the [[BoltzmannEntropyEquation|Boltzmann equation]] S = k ln W.

## Factors That Increase Entropy
- **Phase**: S_gas > S_liquid > S_solid. Melting, vaporization, sublimation give ΔS > 0; freezing, condensation, deposition give ΔS < 0.
- **Temperature**: higher T broadens the kinetic-energy distribution and increases vibration ⇒ S increases with T.
- **Particle count / molecular complexity**: more particles or more atoms per molecule ⇒ more vibrational modes ⇒ more microstates ⇒ higher S; heavier atoms have higher S than lighter ones at a given T.
- **Mixing**: a mixture has greater entropy than the corresponding pure substances.
- **Dissolution**: dissolving a solid in a liquid generally gives ΔS > 0.

## Predicting the Sign of ΔS (Example 16.3)
- Liquid water warmed 25 °C → 50 °C: ΔS > 0 (temperature).
- Ag⁺(aq) + Cl⁻(aq) → AgCl(s): ΔS < 0 (fewer dissolved particles).
- Combustion producing fewer moles of gas: ΔS < 0.
- NH₃(s) → NH₃(l): ΔS > 0 (solid → liquid).

The absolute, tabulated values are [[StandardMolarEntropy|standard molar entropies S°]], anchored by the [[ThirdLawOfThermodynamics|third law]].

## Connections
- [[BoltzmannEntropyEquation]] — S = k ln W, the microstate definition
- [[StandardMolarEntropy]] — tabulated S° and ΔS° of reaction
- [[SecondLawOfThermodynamics]] — ΔS_univ ≥ 0 governs spontaneity
- [[ThirdLawOfThermodynamics]] — sets S = 0 at 0 K (absolute reference)
- [[GibbsFreeEnergy]] — combines ΔS with ΔH as ΔG = ΔH − TΔS
- [[SpontaneousProcess]] — dispersal of matter/energy that entropy quantifies
- [[ThermodynamicEntropy]] — physics/heat-engine counterpart (disambiguation)
- [[Entropy]] — information-theory counterpart (disambiguation)
- [[RudolfClausius]] / [[SadiCarnot]] — origins of the concept
- [[chemistry-2e-ch16-thermodynamics]] — source chapter (§16.2)
