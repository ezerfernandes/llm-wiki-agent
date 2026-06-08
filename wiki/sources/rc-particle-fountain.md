---
title: "Particle fountain (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, simulation, physics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Particle_fountain
---

## Summary
The task asks the programmer to implement an animated particle fountain that emulates water droplets sprayed upward and falling back down under gravity. The system should look generally ordered yet individually chaotic — particles travel in broadly the same direction but carry slightly randomized velocity vectors. The key insight is combining a shared upward emission impulse with per-particle randomized perturbations and constant gravitational acceleration to produce a convincing fountain effect.

## Task Requirements
- Emulate a fountain of water droplets in a gravitational field, sprayed up and then falling back down.
- Make the motion generally ordered but individually chaotic: particles head mostly the same direction but with slightly different vectors.
- Keep at least several hundred particles in motion at any time, ideally several thousand.
- Inter-particle interaction is optional.
- Optionally link to a short video clip of the fountain in action.

## Language Coverage
15 languages implement this task, spanning systems and graphics-capable languages alongside scripting and array languages; representative entries include C++, Java, Python, Lua, Julia, Perl, Raku, Nim, FreeBASIC, and Uiua.

## Connections
- [[ParticleSystem]] — the fountain is a canonical particle-system animation
- [[NumericalIntegration]] — positions/velocities are stepped via simple Euler integration each frame
- [[GravitationalField]] — constant downward acceleration drives the falling arc
- [[PseudorandomNumbers]] — per-particle velocity jitter creates the chaotic spread
- [[RealTimeRendering]] — frame-by-frame drawing of hundreds to thousands of points

## Contradictions
- None — reference task page.
