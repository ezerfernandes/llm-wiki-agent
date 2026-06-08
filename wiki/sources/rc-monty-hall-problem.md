---
title: "Monty Hall problem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Monty_Hall_problem
---

## Summary
The task models the classic Monty Hall game-show puzzle: a contestant picks one of three doors (one hides a car, two hide goats), the host then opens a different door revealing a goat and offers the chance to switch. The programmer must run a Monte Carlo simulation to empirically demonstrate the counterintuitive result that switching wins about 2/3 of the time while staying wins only about 1/3.

## Task Requirements
- Simulate the game with three doors, randomizing car placement and the contestant's initial pick.
- Have the host open a remaining door that hides a goat (choosing randomly if two goat doors remain).
- Run at least 1000 games for the "always stay" strategy and 1000 for the "always switch" strategy.
- Report the win rates of both strategies side by side so the difference is easy to compare.

## Language Coverage
104 languages implement this task, spanning systems languages, scripting languages, functional languages, and even SQL. Representative examples include C, C++, Rust, Go, Python, Ruby, Haskell, Java, JavaScript, Perl, and Transact SQL.

## Connections
- [[ProbabilityTheory]] — the underlying mathematics of conditional probability.
- [[MonteCarloSimulation]] — the empirical method used to verify the result.
- [[ConditionalProbability]] — Bayes' reasoning explains why switching wins 2/3 of the time.
- [[RandomNumberGeneration]] — required to randomize door placement and choices.

## Contradictions
- None — reference task page.
