---
title: "Animate a pendulum (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, physics-simulation, animation, numerical-integration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Animate_a_pendulum
---

## Summary
This task asks the programmer to build a simple physical model of a gravity pendulum and render it as a live animation. The key insight is coupling a numerical simulation of a physical system to a dynamically updating graphical display, where the changing state variables (angle and angular velocity) drive what is drawn each frame.

## Task Requirements
- Create a simple physical model of a simple gravity pendulum.
- Animate it, illustrating the system's changing variables on a dynamic graphical display.
- Requires graphics support.

## Language Coverage
72 languages implement this task, spanning systems languages, scripting languages, math/array environments, and many BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, JavaScript, Python, Haskell, Julia, MATLAB, and Mathematica/Wolfram Language.

## Connections
- [[NumericalIntegration]] — stepping the pendulum's equation of motion over time
- [[OrdinaryDifferentialEquation]] — the pendulum motion is governed by a second-order ODE
- [[Animation]] — frame-by-frame rendering of the changing physical state
- [[SimpleHarmonicMotion]] — the small-angle approximation of pendulum dynamics
- [[GameLoop]] — the update-and-render cycle driving real-time display

## Contradictions
- None — reference task page.
