---
title: "Execution Tree"
type: concept
tags: [symbolic-execution, concolic-execution, control-flow, fuzzing, testing, path-constraints, static-analysis]
sources: [fuzzingbook-21-symbolic-fuzzer]
last_updated: 2026-06-06
---

# Execution Tree

An **execution tree** (or *path-condition tree* / *symbolic execution tree*) is the tree of all execution paths a program can take, rooted at the function entry. Each interior node is a branch point in the [[ControlFlow|control-flow graph]]; each edge records the decision taken (true/if vs. false/else); and each root-to-leaf path corresponds to one feasible (or candidate) execution path with its own [[PathConstraint|path condition]]. [[SymbolicExecution|Symbolic execution]] explores this tree statically — forking at every branch — and [[PathExplosion|path explosion]] is precisely the combinatorial growth of this tree with branches, loops, and recursion. It is the structural backbone over which a [[SymbolicFuzzer|symbolic fuzzer]] enumerates and solves paths.

## From The Fuzzing Book — Symbolic Fuzzing
[[fuzzingbook-21-symbolic-fuzzer|Ch 21]] materializes the execution tree through the `PNode` class. Each `PNode` wraps one CFG node together with a `parent` pointer, an `order` (which branch the child took: `0` = if, `1` = else), and a shared `seen` dictionary capping loop unrolling at `max_iter`. `PNode.explore()` expands a node into its children — one step of growing the tree — and the full `SymbolicFuzzer.get_all_paths()` grows the tree breadth-first to a bounded depth, returning the leaf nodes. `get_path_to_root()` walks the `parent` chain back up to recover a complete root-to-leaf path, which `to_single_assignment_predicates()` then turns into a solvable [[PathConstraint|path condition]]. The earlier `SimpleSymbolicFuzzer.get_all_paths()` builds the same tree recursively (depth-first, no bounding). The chapter contrasts this static, exhaustive tree-walk with [[fuzzingbook-20-concolic-fuzzer|Ch 20]]'s concolic `TraceTree`, which only records the branches a concrete seed actually took; Exercise 3's `ConcolicTracer(SymbolicFuzzer)` follows a single seed path through the same `PNode` tree before negating its last predicate to explore neighbors.

## Connections
- [[SymbolicExecution]] — explores the execution tree by forking at every branch.
- [[SymbolicFuzzer]] — builds the tree with `PNode`/`explore()`/`get_all_paths()` and solves its leaves.
- [[PathConstraint]] — each root-to-leaf path yields one path condition.
- [[PathExploration]] — walking and expanding the tree (with branch inversion) is path exploration.
- [[PathExplosion]] — the tree's combinatorial growth is the explosion problem.
- [[ControlFlow]] — the CFG whose branches become the tree's fork points.
- [[ConcolicExecution]] — Ch 20's `TraceTree` is the concrete-seed-pruned analogue of the full execution tree.
- [[fuzzingbook-21-symbolic-fuzzer|Ch 21]] / [[fuzzingbook-20-concolic-fuzzer|Ch 20]].

## Sources
- [[fuzzingbook-21-symbolic-fuzzer]] — *The Fuzzing Book* Ch 21, "Symbolic Fuzzing" (`PNode` tree, `explore()`, `get_all_paths()`, `get_path_to_root()`).
