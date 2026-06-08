---
title: "Runge-Kutta method (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-methods, differential-equations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Runge-Kutta_method
---

## Summary
The task asks the programmer to implement the classic explicit fourth-order Runge-Kutta (RK4) method to numerically integrate a given ordinary differential equation, y'(t) = t·√y(t), from an initial condition. The key insight is that RK4 estimates each step by combining four weighted slope evaluations (the increments δy₁..δy₄), achieving much higher accuracy than a simple Euler step for the same step size. Because the equation has a known exact solution y(t) = (t²+4)²/16, the implementation can report the numerical error directly.

## Task Requirements
- Solve the ODE over t = 0 … 10 using a fixed step size δt = 0.1 (101 total points, including the given initial point).
- For each step, compute the four RK4 increments δy₁, δy₂, δy₃, δy₄, then advance y by (δy₁ + 2δy₂ + 2δy₃ + δy₄)/6.
- Print the computed y values at whole-numbered t values (0.0, 1.0, … 10.0) alongside the error versus the exact solution y(t) = (t²+4)²/16.

## Language Coverage
74 languages implement this task, spanning low-level systems languages, functional languages, scientific/array languages, and BASIC dialects — representative examples include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Fortran, Julia, MATLAB, and R.

## Connections
- [[RungeKuttaMethods]] — the family of methods this task's RK4 belongs to
- [[OrdinaryDifferentialEquation]] — the initial-value problem being solved
- [[NumericalIntegration]] — the broader class of step-wise approximation techniques
- [[EulerMethod]] — the simpler first-order method RK4 improves upon
- [[NumericalErrorAnalysis]] — comparing computed values against the exact solution

## Contradictions
- None — reference task page.
