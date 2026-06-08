---
title: "Stable marriage problem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-theory, matching-algorithm, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Stable_marriage_problem
---

## Summary
The task asks the programmer to solve the classic stable marriage problem using the Gale-Shapley algorithm. Given an equal number of men and women, each ranking every member of the opposite group by preference, the goal is to produce a set of pairings with no "blocking pair" — no man and woman who would both rather be with each other than with their assigned partners. Gale and Shapley proved a stable matching always exists, and their deferred-acceptance algorithm constructs one by having unengaged men propose down their preference lists while women provisionally accept and trade up.

## Task Requirements
- Use the Gale-Shapley algorithm to compute a stable set of engagements from the given preference data.
- Use the supplied fixed input: 10 named men, 10 named women, and each person's complete ranked preference list (most-preferred first).
- After computing the stable matching, perturb it (swap partners to create an intentionally unstable set) and run a stability check that detects the resulting blocking pair.

## Language Coverage
57 languages implement this task, reflecting broad coverage across paradigms — functional, imperative, scripting, and shell. Representative implementations include C, C++, Java, Python, Haskell, Go, Rust, Ruby, Perl, OCaml, Prolog, and JavaScript.

## Connections
- [[GaleShapleyAlgorithm]] — the deferred-acceptance procedure the task requires
- [[StableMatching]] — the equilibrium concept the algorithm guarantees
- [[GraphTheory]] — bipartite matching underlies the problem structure
- [[Combinatorics]] — preferences define a search over possible pairings
- [[GreedyAlgorithm]] — proposals are made greedily down each man's preference list

## Contradictions
- None — reference task page.
