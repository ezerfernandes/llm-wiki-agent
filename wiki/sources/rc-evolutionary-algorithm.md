---
title: "Evolutionary algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, evolutionary-algorithm, optimization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Evolutionary_algorithm
---

## Summary
This task implements Dawkins' "Weasel program," a toy evolutionary algorithm that evolves a random starting string toward the fixed target `"METHINKS IT IS LIKE A WEASEL"`. The key insight is cumulative selection: rather than searching the full space at random, each generation breeds many mutated copies of the current best (the parent) and keeps only the fittest, so progress accumulates and convergence is rapid. A subtle correctness point the task stresses is that the new parent must be chosen from the pool of mutants *and* the prior parent, so fitness never regresses.

## Task Requirements
- Begin with a `target` string and a random `parent` of equal length drawn from uppercase letters plus space.
- Define a `fitness` function measuring how close a candidate is to the target.
- Define a `mutate` function that copies a string and randomly alters characters at a given mutation rate.
- Loop while `parent != target`: produce C mutated copies of the parent, score all of them (plus the parent) with `fitness`, and promote the fittest to be the new parent.
- Repeat until the parent converges to the target; mutation must not deliberately preserve already-correct characters.

## Language Coverage
116 languages implement this task, spanning systems, scripting, functional, and assembly tiers — including C, C++, Rust, Go, Python, Haskell, Common Lisp, Java, Perl, and even 8080/8086 Assembly.

## Connections
- [[EvolutionaryAlgorithm]] — the algorithm family this task names directly
- [[GeneticAlgorithm]] — closely related mutation-and-selection optimization
- [[FitnessFunction]] — scoring mechanism that drives selection pressure
- [[CumulativeSelection]] — the principle making the search converge quickly
- [[RandomNumberGeneration]] — underlies both mutation and initial parent generation

## Contradictions
- None — reference task page.
