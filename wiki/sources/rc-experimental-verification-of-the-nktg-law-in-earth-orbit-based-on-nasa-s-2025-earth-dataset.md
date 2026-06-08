---
title: "Experimental Verification of the NKTg Law in Earth Orbit Based on NASA’s 2025 Earth Dataset (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, physics-simulation, numerical-computation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Experimental_Verification_of_the_NKTg_Law_in_Earth_Orbit_Based_on_NASA’s_2025_Earth_Dataset
---

## Summary
The task asks the programmer to compute the quantities of the (fringe) "NKTg Law" from given Earth orbital data and compare the model's simulated velocities against NASA observations. For each date, programs derive linear momentum `p = m·v`, then `NKTg₁ = x·p` (position–momentum interaction) and `NKTg₂ = (dm/dt)·p` (mass-variation–momentum interaction), using a constant atmospheric mass-loss rate `dm/dt = −1.8 kg/s`. The core work is simple arithmetic over a small fixed dataset plus a relative-error comparison; the main insight is that it is purely a data-driven numerical reporting exercise rather than a real orbital integration.

## Task Requirements
- Given 2024/2025 Earth orbital data (position x in m, velocity v in m/s, mass m in kg) and `dm/dt = −1.8 kg/s`.
- For each date compute linear momentum `p = m·v`.
- Compute `NKTg₁ = x·p`.
- Compute `NKTg₂ = (dm/dt)·p`.
- Compare the simulated velocity against NASA's observed velocity.
- Compute the relative error in percent.
- Output the calculated values and relative error for each 2025 date.

## Language Coverage
12 languages implement this task, spanning systems, scripting, BASIC-family, and esoteric languages. Representative implementations include Java, Python, Rust, Phix, Wren, FreeBASIC, EasyLang, Oberon-07, ALGOL 68, Pluto, Zen C, and LOLCODE.

## Connections
- [[NewtonianMechanics]] — momentum `p = m·v` and orbital position/velocity are the underlying quantities.
- [[FloatingPointArithmetic]] — values span ~10⁴ to ~10⁴⁰, exercising large-magnitude float handling.
- [[RelativeError]] — the comparison step computes percent deviation from NASA observations.
- [[TabularDataProcessing]] — the task is iteration and formatted reporting over a fixed dataset.

## Contradictions
- None — reference task page.
