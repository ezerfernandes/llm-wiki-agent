---
title: "K-d tree (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, nearest-neighbor, spatial-search]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/K-d_tree
---

## Summary
The task asks the programmer to build a k-d tree (a k-dimensional space-partitioning binary tree) and use it to perform a nearest-neighbor search. The key insight is that by alternating the splitting axis at each tree depth, the search can prune entire subtrees and visit far fewer nodes than a brute-force scan, though this advantage collapses in high dimensions (it requires N ≫ 2^k).

## Task Requirements
- Construct a k-d tree, e.g. using a simple median-of-points splitting strategy.
- Run a nearest-neighbor search on two datasets: the Wikipedia 2-D example [(2,3),(5,4),(9,6),(4,7),(8,1),(7,2)] querying (9,2), and 1000 uniformly random 3-D points in a cube querying a random location.
- Instrument the search to count nodes visited (any field access counts as a visit).
- Output the query point, the found point, the distance, and the node-visit count.
- Only the single nearest neighbor is required; insertion, deletion, balancing, N-nearest, approximate, and range searches are explicitly not required.

## Language Coverage
35 languages implement this task, spanning low-level assembly, systems, functional, and scripting families. Representative implementations include C, C++, Rust, Go, Java, Haskell, Common Lisp, Python, Perl, Julia, and Swift.

## Connections
- [[KDimensionalTree]] — the core space-partitioning data structure being built.
- [[BinarySpacePartitioning]] — k-d trees are a special case of BSP trees.
- [[NearestNeighborSearch]] — the query algorithm the task exercises.
- [[BinaryTree]] — the underlying tree structure with axis-alternating splits.
- [[EuclideanDistance]] — the metric used to measure proximity between points.

## Contradictions
- None — reference task page.
