---
title: "Latin Squares in reduced form/Randomizing using Jacobson and Matthews' technique (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, random-sampling, markov-chain]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Latin_Squares_in_reduced_form/Randomizing_using_Jacobson_and_Matthews'_technique
---

## Summary
The task asks the programmer to implement the Jacobson and Matthews algorithm for transforming one valid Latin square of order n into another, producing a near-uniform random walk over the space of Latin squares. Starting from a seed square X0, each step applies a local "move" (a proper move or an improper-move correction involving a 3-dimensional incidence structure) to generate the next square, so that repeated application samples Latin squares essentially uniformly at random. The key insight is that this Markov-chain method can sample huge spaces (e.g. order 256) that are intractable to enumerate exhaustively.

## Task Requirements
- Implement a function that, given a valid Latin square, returns another via the Jacobson and Matthews technique (per section 3.3 of Drizen's "Generalised 2-designs with Block Size 3").
- Part 1: Seed with a reduced-form order-4 square, generate 10000 squares iteratively (X(n-1) -> X(n)), reduce each to reduced form, display them, and count occurrences of each.
- Part 2: Same for order 5 without displaying squares; generate all 56 reduced-form order-5 squares, confirm all 56 are produced, and display the count of each.
- Part 3: Generate 750 order-42 squares and display the 750th.
- Part 4: Generate 1000 order-256 squares, display nothing but report the approximate time taken and any observations.

## Language Coverage
15 languages implement this task, spanning systems and functional styles. Representative implementations include C#, C++, F#, Go, Java, JavaScript, Julia, Python, Rust, and Wren.

## Connections
- [[LatinSquare]] — the combinatorial object being randomized
- [[MarkovChainMonteCarlo]] — the random-walk sampling framework this method embodies
- [[UniformRandomSampling]] — the goal of producing near-uniform Latin squares
- [[Combinatorics]] — the broader field of counting and generating such structures

## Contradictions
- None — reference task page.
