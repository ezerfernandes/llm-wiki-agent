---
title: "Two bullet roulette (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, monte-carlo-simulation, probability]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Two_bullet_roulette
---

## Summary
A Monte Carlo simulation of a Russian-roulette variant in which two bullets are loaded into a six-chamber revolver and the trigger is pulled twice. The task explores four strategies that differ in whether the cylinder is spun (re-randomized) after loading the first bullet and/or after firing the first shot, asking which strategy maximizes the probability of firing a live round. The key insight is that loading bullets into adjacent chambers (per the stated loading procedure) changes the outcome distribution, so spinning vs. not spinning matters.

## Task Requirements
- Run a repeated simulation of each of the four scenarios (A, B, C, D), randomizing the spin, load, and fire ordering as described.
- Report the percentage of "deaths" (successful fires) for each scenario.
- Results should approximate the hand-calculated probabilities of 5/9, 7/12, 5/9, and 1/2, accurately enough to identify the highest-probability scenario.

## Language Coverage
25 languages implement this task, spanning systems, scripting, functional, and array-oriented languages. Representative implementations include C, C++, Go, Java, Python, JavaScript, Julia, Perl, Raku, Ruby, Fortran, and Wren.

## Connections
- [[MonteCarloSimulation]] — the task is solved by repeated random trials rather than closed-form math.
- [[Probability]] — comparing event probabilities across loading/spinning strategies.
- [[PseudorandomNumberGenerator]] — each spin draws a uniform random rotation of the cylinder.
- [[RussianRoulette]] — the underlying scenario being modeled.

## Contradictions
- None — reference task page.
