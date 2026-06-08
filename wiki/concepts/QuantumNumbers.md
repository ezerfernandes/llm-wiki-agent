---
title: "Quantum Numbers"
type: concept
tags: [chemistry, general-chemistry, quantum-chemistry]
sources: [chemistry-2e-ch06-electronic-structure-periodic-properties, college-physics-2e-ch30]
last_updated: 2026-06-07
---

# Quantum Numbers

In the quantum-mechanical model, each [[Electron|electron]] in an atom is completely specified by **four quantum numbers**. They arise from solving the Schrödinger equation (**Ĥψ = Eψ**), in which the electron is a three-dimensional stationary wave (**wavefunction ψ**) and **|ψ|²** gives the probability of finding the electron at a point (Born interpretation).

| Name | Symbol | Allowed values | Meaning |
|---|---|---|---|
| Principal | n | 1, 2, 3, 4, … | Shell — energy level and general orbital size |
| Angular momentum (azimuthal) | l | 0 ≤ l ≤ n − 1 | Subshell — orbital **shape** |
| Magnetic | m_l | −l, …, 0, …, +l | **Orientation** of the orbital in space |
| Spin | m_s | +½ (α), −½ (β) | Direction of the electron's intrinsic spin |

## Subshells and orbital counts
- Subshell letters by l: **l=0 → s, l=1 → p, l=2 → d, l=3 → f** (then g, h).
- Orbitals per subshell = **2l + 1**: s = 1, p = 3, d = 5, f = 7.
- A shell n holds a maximum of **2n²** electrons (n=2 → 8, n=3 → 18, n=4 → 32).

## Spin
Electron spin is an intrinsic quantum property (each electron acts as a tiny magnet) with no classical analogue; it cannot be derived from the Schrödinger equation. The two spin states differ in energy in a magnetic field, causing fine-structure splitting in spectra. See [[ElectronSpin]].

## Quantized Magnitudes and Directions (Physics, Ch.30)
College Physics 2e gives the explicit quantized values:
- Orbital angular-momentum magnitude: **L = √[l(l+1)]·(h/2π)**, with l = 0…n−1
- Its z-component: **L_z = m_l·(h/2π)**, m_l = −l…+l, and the allowed orientation angle cos θ = L_z/L
- Intrinsic spin magnitude: **S = √[s(s+1)]·(h/2π)** with s = 1/2; z-component **S_z = m_s·(h/2π)**, m_s = ±1/2

Because L_z can take only discrete values, the angular-momentum vector points only along certain cones around the field axis — **space quantization** — which underlies the Zeeman effect and [[AtomicSpectra|fine structure]].

## Orbitals and nodes
The wavefunction defines an [[AtomicOrbital|atomic orbital]] (s spherical, p dumbbell, d/f more complex). **Radial nodes** (where ψ = 0) number **n − l − 1** (e.g., 2s has 1, 3s has 2, 4f has 0).

## Degeneracy
In hydrogen / one-electron ions, all orbitals of the same n have equal energy (degenerate). Electron-electron repulsion in multi-electron atoms removes this, splitting subshells by l, though orbitals within a subshell stay degenerate.

## Connections
- [[AtomicOrbital]] — the spatial region the quantum numbers describe
- [[PauliExclusionPrinciple]] — no two electrons share all four quantum numbers
- [[ElectronConfiguration]] — built from filling orbitals by quantum number
- [[ErwinSchrodinger]] — derived the wave equation; [[WolfgangPauli]] — the exclusion rule
- [[BohrModel]] — n generalizes Bohr's quantized orbits
- [[WaveParticleDuality]] / [[HeisenbergUncertaintyPrinciple]] — basis of the wave description
- [[ElectronSpin]] — the intrinsic-spin quantum number in detail
- [[AtomicSpectra]] — space quantization shows up as Zeeman/fine-structure splitting
- [[chemistry-2e-ch06-electronic-structure-periodic-properties]] / [[college-physics-2e-ch30]] — source chapters
