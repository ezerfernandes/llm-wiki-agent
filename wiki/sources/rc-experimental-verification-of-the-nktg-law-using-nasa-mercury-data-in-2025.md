---
title: "Experimental Verification of the NKTg Law Using NASA Mercury Data in 2025 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, physics-simulation, numerical-computation, orbital-mechanics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Experimental_Verification_of_the_NKTg_Law_Using_NASA_Mercury_Data_in_2025
---

## Summary
This task asks the programmer to verify the (informal, RC-specific) "NKTg law" against NASA JPL Horizons orbital data for Mercury. Treating the conserved quantity NKTg₁ = x·m·v as a constant taken from a reference date, the program interpolates Mercury's velocity at several 2025 dates, computes linear momentum p = m·v and a secondary quantity NKTg₂ = (dm/dt)·p, then reports the relative error against the actual NASA velocities. The key insight is that x·m·v is essentially a one-dimensional proxy for the planet's conserved angular momentum, so velocity can be back-solved as v = NKTg₁ / (x·m).

## Task Requirements
- Use the reference constant NKTg₁ = x·m·v derived from the 31/12/2024 data point.
- For each 2025 date, compute interpolated velocity v = NKTg₁ / (x·m).
- Compute linear momentum p = m·v.
- Compute NKTg₂ = (dm/dt)·p, using dm/dt = -0.5 kg/s.
- Compute the relative error of the interpolated velocity versus the actual NASA velocity (in percent).
- Print a formatted table of date, v_NKTg, v_NASA, relative error, and NKTg₂.

## Language Coverage
9 languages implement this task — a small, niche set typical of recently added RC tasks. Representative implementations include Fortran, Java, Julia, Rust, Wren, Phix, FreeBASIC, Pluto, and EasyLang.

## Connections
- [[OrbitalMechanics]] — the model approximates conservation of orbital angular momentum.
- [[AngularMomentum]] — NKTg₁ = x·m·v is a one-dimensional proxy for r × p.
- [[LinearInterpolation]] — velocity is back-solved from a conserved constant.
- [[NumericalSimulation]] — comparing simulated values against observed NASA data.

## Contradictions
- None — reference task page.
