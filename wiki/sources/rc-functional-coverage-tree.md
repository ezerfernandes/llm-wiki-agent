---
title: "Functional coverage tree (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, tree-traversal, weighted-average]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Functional_coverage_tree
---

## Summary
The task models functional coverage tracking (borrowed from System-on-Chip verification) over a hierarchy of cleaning sub-tasks. Each leaf node reports a fractional completion (coverage 0.0–1.0) and each node may carry a weight (defaulting to 1.0). The goal is to compute every internal node's coverage as the weighted average of its children's coverage, evaluated bottom-up, then display the whole tree with its weights and computed coverages. The key insight is that this is a single post-order traversal aggregating weighted means up to the root.

## Task Requirements
- Parse the given indented hierarchy of (sub)tasks into a tree, with missing weights defaulting to 1.0 and missing coverage to 0.0.
- Compute each non-leaf node's coverage as the weighted arithmetic mean of its direct children's coverage, processed bottom-upwards.
- Display the coverage at all levels in a way that visually preserves the hierarchy, weights, and coverage.
- Extra credit: compute each node's `delta` — the additional top-level coverage gained if that node were fully covered — via `(1 - coverage) * power`, where a child's power is the parent's power times the child's weight over the sum of sibling weights, seeded with `top.delta_calculation(power=1)`.

## Language Coverage
19 languages implement this task, a moderate spread across functional, imperative, and array paradigms. Representative entries include C++, Go, Haskell, Java, JavaScript, Julia, Python, Perl, Raku, Rust, and the array language J.

## Connections
- [[TreeTraversal]] — bottom-up (post-order) aggregation over the task hierarchy
- [[WeightedArithmeticMean]] — each node's coverage is the weighted average of its children
- [[RecursiveDescent]] — natural recursive structure for both coverage and delta computation
- [[FunctionalVerification]] — the SoC coverage-tracking scenario the task is modeled on

## Contradictions
- None — reference task page.
