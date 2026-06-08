---
title: "Experimental Verification of the NKT Law: Interpolating the Masses of 8 Planets Using NASA Data as of 30–31/12/2024 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, physics, interpolation, numerical-computing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Experimental_Verification_of_the_NKT_Law:_Interpolating_the_Masses_of_8_Planets_Using_NASA_Data_as_of_30–31/12/2024
---

## Summary
The task implements the "NKTg Law of Variable Inertia," a speculative framework in which an object's motion tendency is described by interaction quantities NKTg₁ = x·p and NKTg₂ = (dm/dt)·p, where p = m·v is linear momentum. Given each planet's orbital position x, velocity v, and a precomputed NKTg₁ value from NASA reference data (30/12/2024), a program recovers the planet's mass via the rearranged relation m = NKTg₁ / (x·v). The exercise is essentially a sanity check: since NKTg₁ was itself derived from x·m·v, the "interpolated" mass should reproduce the original NASA mass with Δm ≈ 0 to within floating-point precision.

## Task Requirements
- For each of the 8 planets, given x (km), v (km/s), and NKTg₁ (NKTm) from the 30/12/2024 dataset, compute the interpolated mass m = NKTg₁ / (x·v).
- Compute linear momentum p = m·v.
- Compute the absolute difference Δm = |m_NASA − m| against the published NASA mass.
- Demonstrate that Δm is approximately zero within floating-point precision for all eight planets.

## Language Coverage
11 languages implement this task, a relatively narrow Rosetta Code task built around a numeric verification loop. Representative implementations include C, C++, Fortran, Java, Julia, Python, Phix, FreeBASIC, Wren, Pluto, and X86 Assembly.

## Connections
- [[Interpolation]] — the task frames mass recovery as an interpolation between reference and target dates.
- [[LinearMomentum]] — momentum p = m·v underpins the NKTg₁ = x·p definition.
- [[FloatingPointPrecision]] — correctness is judged by Δm being negligibly small under floating-point arithmetic.
- [[OrbitalMechanics]] — the dataset is drawn from NASA JPL Horizons planetary position/velocity/mass data.

## Contradictions
- None — reference task page.
