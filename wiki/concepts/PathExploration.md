---
title: "Path Exploration"
type: concept
tags: [path-exploration, symbolic-execution, concolic-execution, fuzzing, testing, smt, coverage, security]
sources: [fuzzingbook-20-concolic-fuzzer, fuzzingbook-21-symbolic-fuzzer]
last_updated: 2026-06-06
---

# Path Exploration

**Path exploration** is the systematic discovery of distinct execution paths through a program in order to maximize coverage and expose deep, branch-guarded bugs. Starting from a known feasible path (and its [[PathConstraint|path condition]]), an explorer repeatedly picks a branch on that path, *negates* its predicate, keeps the rest of the prefix unchanged, and asks an [[SMTSolver|SMT solver]] for an input satisfying the modified condition. Each solved condition yields an input that follows a *neighboring* path — diverging at exactly the negated branch — and the new path may reveal further branches to negate. Iterating this drives execution down branches a random or fixed sample input would never reach, which is the central value of [[SymbolicExecution|symbolic]] and [[ConcolicExecution|concolic]] execution over blackbox fuzzing.

## From The Fuzzing Book — Concolic Fuzzing
[[fuzzingbook-20-concolic-fuzzer|Ch 20]] gives two concrete path-exploration strategies built on `ConcolicTracer`:
- **`SimpleConcolicFuzzer`** records observed traces in a `TraceTree` — a binary tree where each `TraceNode` is a branch decision (`0` = else, `1` = if) and the unexplored frontier is held as `PlausibleChild` leaves. `fuzz()` selects a random unexplored leaf, builds its [[PathConstraint|path condition]] via `path_expression()`, and solves it (`zeval_smt`) to produce an input forcing the not-yet-taken branch. This explores paths *near* the seed input's path.
- **`ConcolicGrammarFuzzer`** lifts exploration up to the [[Grammar|grammar]]: it uses `span()` to map derivation-tree nodes to input substrings, `traverse_z3()` to extract concrete string comparisons from the path predicates, and `find_alternatives()`/`update_grammar()` to add discovered constants (e.g. a required table name `inventory`) as new grammar alternatives. Subsequent fuzzing then *produces* inputs that satisfy those deep equality constraints, reaching code the plain `GrammarFuzzer` never could.

The chapter also notes that [[fuzzingbook-07-search-based-fuzzer|search-based fuzzing (Ch 7)]] can offer a cheaper exploration strategy than repeatedly calling an SMT solver, and that [[fuzzingbook-21-symbolic-fuzzer|symbolic fuzzing (Ch 21)]] is a costlier but stronger explorer.

## From The Fuzzing Book — Symbolic Fuzzing
[[fuzzingbook-21-symbolic-fuzzer|Ch 21]] explores paths *exhaustively and statically* rather than by negating around a seed. The [[SymbolicFuzzer|`SymbolicFuzzer`]] enumerates the entire [[ExecutionTree|execution tree]] of the [[ControlFlow|CFG]] up to a bounded depth: `PNode.explore()` expands a node into its children one step at a time, `get_all_paths()` grows the tree breadth-first (with a `seen` counter unrolling loops only to `max_iter`), and `get_path_to_root()` recovers each complete path for solving. Every reachable path to the bound is generated, then each [[PathConstraint|path condition]] is solved once with [[Z3Prover|Z3]] — making symbolic fuzzing *path-complete* but bounded by [[PathExplosion|path explosion]] ("wide but shallow"). The chapter then unifies the two exploration styles: Exercise 3's concolic variant follows a *single seed path* through the same tree and negates its last predicate, exactly the near-seed exploration of [[fuzzingbook-20-concolic-fuzzer|Ch 20]] — so the difference between symbolic and concolic exploration is whether you enumerate the whole tree or walk one branch and perturb it.

## Connections
- [[PathConstraint]] — the formula whose conjuncts are negated, one at a time, to reach new paths.
- [[ConcolicExecution]] / [[SymbolicExecution]] — the execution models that make systematic exploration possible.
- [[ConcolicFuzzing]] — the fuzzing application (`SimpleConcolicFuzzer`, `ConcolicGrammarFuzzer`) that performs the exploration.
- [[SMTSolver]] / [[Z3Prover]] — solves each negated path condition into a path-reaching input.
- [[BranchCoverage]] / [[PathCoverage]] / [[Coverage]] — the coverage goals that drive exploration toward un-taken branches.
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — a cheaper, search-based alternative to SMT-driven exploration.
- [[fuzzingbook-20-concolic-fuzzer|Ch 20]] / [[fuzzingbook-21-symbolic-fuzzer|Ch 21]].

## Sources
- [[fuzzingbook-20-concolic-fuzzer]] — *The Fuzzing Book* Ch 20, "Concolic Fuzzing."
- [[fuzzingbook-21-symbolic-fuzzer]] — *The Fuzzing Book* Ch 21, "Symbolic Fuzzing" (exhaustive static enumeration of all CFG paths to a bounded depth via `PNode.explore()`/`get_all_paths()`).
