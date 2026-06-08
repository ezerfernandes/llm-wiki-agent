---
title: "Bohr Model"
type: concept
tags: [chemistry, general-chemistry, quantum-chemistry, physics]
sources: [chemistry-2e-ch06-electronic-structure-periodic-properties, college-physics-2e-ch30]
last_updated: 2026-06-07
---

# Bohr Model

The **Bohr model** (Niels Bohr, 1913) describes the hydrogen atom as an [[Electron|electron]] occupying one of a set of quantized, stationary circular orbits around the [[AtomicNucleus|nucleus]]. It was the first model to explain the hydrogen [[AtomicSpectra|line spectrum]].

## The Problem It Solved
The [[RutherfordScattering|Rutherford]] planetary atom was classically unstable: an orbiting (accelerating) electron should continuously radiate energy and spiral into the nucleus. Bohr postulated instead that electrons occupy **stationary states** and emit or absorb energy *only* when jumping between orbits.

## Physics Framing (College Physics 2e, Ch.30)
The physics text states the rule as **angular-momentum quantization**, L = mₑvrₙ = nh/2π (n = 1,2,3,…), and obtains hydrogen energy levels Eₙ = −13.6 eV/n² (generalized Eₙ = −Z²·E₀/n² with E₀ = 13.6 eV). It groups the resulting hydrogen lines into the Lyman (n_f=1), Balmer (n_f=2), and Paschen (n_f=3) series. Crucially, [[DeBroglieWavelength|de Broglie]] standing waves justify the quantization: nλ = 2πrₙ — only orbits holding a whole number of electron wavelengths survive (see [[WaveParticleDuality]]).

## Key Equations
Quantized orbital energy:

> **E_n = −k/n²** (hydrogen), generalized to one-electron ions: **E_n = −kZ²/n²**

with **k = R∞ = 2.179 × 10⁻¹⁸ J**, Z = nuclear charge (+1 H, +2 He⁺, …), and n = 1, 2, 3, …

Energy of a transition (emitted/absorbed as a photon):

> **|ΔE| = |E_f − E_i| = hν = hc/λ**

Combining these reproduces the [[AtomicSpectra|Rydberg formula]] 1/λ = (k/hc)(1/n₁² − 1/n₂²). Orbit radius: **r = n²a₀/Z** with Bohr radius a₀ = 5.292 × 10⁻¹¹ m.

## Concepts
- **Ground state** (lowest energy, n = 1 for H) vs **excited state** (higher n).
- **Absorption** raises n (positive ΔE, photon absorbed); **emission** lowers n (photon emitted).
- **Ionization limit**: as n → ∞, E → 0; the electron is fully removed. For ground-state H, ionization energy = k.

## Worked example
H, n = 4 → n = 6: ΔE = 2.179 × 10⁻¹⁸(1/16 − 1/36) = 7.566 × 10⁻²⁰ J (absorption); λ = hc/E = 2.626 × 10⁻⁶ m (infrared).

## Limitations
The model works only for hydrogen-like (single-electron) species; it fails for helium and beyond, and its notion of precise classical orbits was overturned by the quantum-mechanical model (see [[WaveParticleDuality]], [[QuantumNumbers]], [[HeisenbergUncertaintyPrinciple]]). Three of its features survived: energies are quantized, energy rises with distance from the nucleus, and discrete spectra reflect quantized levels.

## Connections
- [[NielsBohr]] — proposed the model
- [[AtomicSpectra]] — the line spectrum it explained
- [[EnergyQuantization]] — quantized orbital energies
- [[WaveParticleDuality]] — de Broglie's 2πr = nλ justifies the quantization
- [[QuantumNumbers]] / [[AtomicOrbital]] — the model that superseded it
- [[Electron]] / [[AtomicNucleus]] — the orbiting particle and its center
- [[RutherfordScattering]] — revealed the nucleus this model orbits
- [[DeBroglieWavelength]] — standing-wave origin of the quantization
- [[chemistry-2e-ch06-electronic-structure-periodic-properties]] / [[college-physics-2e-ch30]] — source chapters
