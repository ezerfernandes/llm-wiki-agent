---
title: "Aufbau Principle & Hund's Rule"
type: concept
tags: [chemistry, general-chemistry, quantum-chemistry]
sources: [chemistry-2e-ch06-electronic-structure-periodic-properties]
last_updated: 2026-06-07
---

# Aufbau Principle

The **Aufbau principle** ("building up") determines an atom's ground-state [[ElectronConfiguration|electron configuration]]: imagine adding protons to the nucleus and electrons one at a time, each electron entering the **lowest-energy available subshell**, subject to allowed [[QuantumNumbers|quantum numbers]] and the [[PauliExclusionPrinciple|Pauli exclusion principle]]. A higher subshell fills only after lower ones are full.

## Filling order
> 1s 2s 2p 3s 3p **4s 3d** 4p 5s 4d 5p **6s 4f 5d** 6p 7s 5f 6d 7p

Note **4s fills before 3d** (3d lacks radial nodes, is less penetrating, and is more shielded). Within a shell, energy ordering is s < p < d < f because higher-l electrons penetrate less and are more shielded.

## Hund's Rule
For a set of degenerate orbitals (the 3 p, 5 d, or 7 f orbitals of a subshell):

> "The lowest-energy configuration ... is that having the maximum number of unpaired electrons."

So electrons occupy separate degenerate orbitals **singly, with parallel spins**, before any orbital is doubled up. Example — carbon's 2p²: [↑ | ↑ | ] not [↑↓ | | ].

## Exceptions
Half-filled and fully-filled d subshells gain extra stability, so a 4s electron shifts into 3d:
- **Cr**: expected [Ar]4s²3d⁴ → observed **[Ar]4s¹3d⁵**
- **Cu**: expected [Ar]4s²3d⁹ → observed **[Ar]4s¹3d¹⁰**
- **Nb**: expected [Kr]5s²4d³ → observed **[Kr]5s¹4d⁴**
These occur when same-orbital electron repulsion exceeds the subshell energy gap; they are not predictable without empirical data.

## Connections
- [[HundsRule]] — the maximum-unpaired-spin rule (treated here in full)
- [[ElectronConfiguration]] — the result of applying Aufbau
- [[PauliExclusionPrinciple]] — caps each orbital at two electrons
- [[QuantumNumbers]] / [[AtomicOrbital]] — orbital energies and capacities
- [[PeriodicTable]] — the table's s/p/d/f blocks mirror the filling order
- [[chemistry-2e-ch06-electronic-structure-periodic-properties]] — source chapter
