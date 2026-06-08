---
title: "Experimental Verification of the NKTg Law Using NASA Neptune Data (2023–2024) (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-simulation, physics, scientific-computing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Experimental_Verification_of_the_NKTg_Law_Using_NASA_Neptune_Data_(2023–2024)
---

## Summary
The task asks the programmer to implement the "NKTg Law," a function NKTg = f(x, v, m) defined over an object's position x, velocity v, and mass m. From momentum p = m·v it computes two interaction quantities — NKTg₁ = x·p (position–momentum) and NKTg₂ = (dm/dt)·p (mass-variation–momentum) — and combines them as NKTg = √(NKTg₁² + NKTg₂²). The program applies this to NASA's 2023 Neptune position/velocity/mass data and simulates the planet's 2024 motion parameters under an assumed micro gas-loss rate of –0.00002000 kg/s, then compares the simulated trend against NASA's published 2024 observations.

## Task Requirements
- For each dated data point, compute momentum p = m·v.
- Compute NKTg₁ = x·p and NKTg₂ = (dm/dt)·p, then the magnitude NKTg = √(NKTg₁² + NKTg₂²).
- Apply a constant mass-loss rate dm/dt = –0.00002000 kg/s to propagate mass forward from 2023 into 2024.
- Tabulate the simulated 2024 values and compare them to NASA's actual published 2024 data to assess the law's predictive stability.

## Language Coverage
17 languages implement this task, a modest spread skewed toward numerically oriented and niche languages rather than mainstream scripting ones. Representative implementations include Python, Java, Julia, Fortran, FreeBASIC, F#, Phix, Wren, Q#, and Pluto.

## Connections
- [[NumericalSimulation]] — propagating physical state forward in time from initial data.
- [[Momentum]] — the core quantity p = m·v underlying both NKTg terms.
- [[OrbitalMechanics]] — modeling Neptune's position, velocity, and mass over a year.
- [[EuclideanNorm]] — the √(a² + b²) combination of the two interaction terms.
- [[FloatingPointArithmetic]] — handling the very large/small magnitudes (10²⁶ kg, 10³⁶ scale) involved.

## Contradictions
- None — reference task page.
