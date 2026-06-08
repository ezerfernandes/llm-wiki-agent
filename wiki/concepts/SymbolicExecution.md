---
title: "Symbolic Execution"
type: concept
tags: [symbolic-execution, concolic-execution, smt, z3, fuzzing, testing, static-analysis, program-analysis, path-constraints, security]
sources: [fuzzingbook-20-concolic-fuzzer, fuzzingbook-21-symbolic-fuzzer]
last_updated: 2026-06-06
---

# Symbolic Execution

**Symbolic execution** is a program-analysis technique that runs a program on *symbolic* inputs — placeholders standing for "any value" — instead of concrete data. Each variable holds a symbolic *expression* over the inputs rather than a number, and every conditional **forks** the analysis into two sub-executions: one assuming the branch condition is true, one assuming it is false. Along each path the analyzer accumulates a [[PathConstraint|path condition]] (the conjunction of branch assumptions); a path is *feasible* iff its path condition is satisfiable, which an [[SMTSolver|SMT solver]] decides, also yielding a concrete input that exercises that exact path. Originating with King's 1976 work, symbolic execution is the foundation on which [[ConcolicExecution|concolic execution]] (concrete + symbolic) is built — concolic execution was introduced precisely "to inform and expand the scope of symbolic execution."

The defining cost of symbolic execution is **path explosion**: the number of paths grows combinatorially with branches and loops, and parts of a program that call out to unmodeled native code or perform complex pointer arithmetic produce constraints the solver cannot handle. [[ConcolicExecution|Concolic execution]] mitigates both by always keeping a concrete value to fall back on; pure symbolic execution instead reasons about whole regions of the input space at once, which makes it more *complete* but more expensive.

## From The Fuzzing Book — Concolic Fuzzing
[[fuzzingbook-20-concolic-fuzzer|Ch 20]] introduces symbolic execution as the conceptual basis of its concrete-plus-symbolic approach: a *symbolic variable* is "a placeholder for the real variable, like the `x` in solving for `x` in algebra," used to *encode* constraints without solving them until an [[SMTSolver|SMT solver]] (Z3) is invoked. The chapter's `ConcolicTracer` realizes a *concolic* variant, but the symbolic machinery — symbolic shadow variables, path conditions, branch negation, SMT solving — is exactly the symbolic-execution apparatus, applied alongside concrete execution. *The Fuzzing Book* expands pure symbolic execution proper in [[fuzzingbook-21-symbolic-fuzzer|Ch 21, "Symbolic Fuzzing"]], presented there as "a costlier but stronger alternative to concolic fuzzing."

## From The Fuzzing Book — Symbolic Fuzzing
[[fuzzingbook-21-symbolic-fuzzer|Ch 21]] is the wiki's full treatment of *pure* symbolic execution — a **static** analysis that never runs the target. It treats inputs as [[SymbolicVariable|symbolic variables]] (minted from the function's type annotations via `SYM_VARS`/`get_symbolicparams`: `int → z3.Int`, `float → z3.Real`, `str → z3.String`), statically walks the function's [[ControlFlow|control-flow graph]] (`PyCFG`/`gen_cfg` from the `ControlFlow` module) to enumerate every path, builds each path's [[PathConstraint|path condition]], and solves it with [[Z3Prover|Z3]]. Inverting a branch (`z3.Not(...)`) selects a sibling path and can *prove paths infeasible* (e.g. `check_triangle`'s `a==b ∧ a==c ∧ b≠c` is unsatisfiable). The chapter shows a whole function reduced to one Z3 *function summary* at its exit node, and builds two fuzzers — the loop-free `SimpleSymbolicFuzzer` and the full [[SymbolicFuzzer|`SymbolicFuzzer`]] (a.k.a. `AdvancedSymbolicFuzzer`), which handles **variable reassignment** by single-static-assignment renaming (`v` → `_v_0`, `_v_1`, …) and bounds **loops/recursion** by *unrolling* them to `max_iter`/`max_depth` instead of inferring loop invariants. The trade-off it makes explicit: symbolic execution is "wide but shallow" — path-complete across branches but only to a fixed depth, dominated by [[PathExplosion|path explosion]], and unable to reason about opaque/external code. Production tools in this lineage — [[KLEE]], [[angr]], Driller, [[SAGE]], and the Python interpreter-modifying CHEF — are cited in its Background, with the technique tracing to King (1976). Exercise 3 rebuilds [[ConcolicExecution|concolic execution]] *on top of* this symbolic machinery, confirming the two are driving strategies over a shared substrate.

## Connections
- [[ConcolicExecution]] — concrete + symbolic execution; the symbolic half is this technique.
- [[SymbolicFuzzer]] / [[SymbolicVariable]] / [[ExecutionTree]] / [[PathExplosion]] — the Ch 21 apparatus (the fuzzer, its input placeholders, the path tree it walks, and its defining scalability limit).
- [[PathConstraint]] — the path condition that symbolic execution accumulates and an SMT solver checks for feasibility.
- [[PathExploration]] — forking at each branch (and solving the resulting path conditions) is how symbolic execution explores the program.
- [[SMTSolver]] / [[Z3Prover]] — decides path-condition satisfiability and produces path-reaching inputs.
- [[SymbolicAI]] / [[SymbolicProgramming]] — the broader symbolic-reasoning lineage (distinct topic, but related "operate over symbols, not values" idea).
- [[ControlFlow]] — branches are exactly the fork points of symbolic execution.
- [[fuzzingbook-21-symbolic-fuzzer|Ch 21]] — the dedicated symbolic-fuzzing chapter that expands this concept.
- [[fuzzingbook-20-concolic-fuzzer|Ch 20]] — introduces it as the basis for concolic execution.

## Sources
- [[fuzzingbook-20-concolic-fuzzer]] — *The Fuzzing Book* Ch 20, "Concolic Fuzzing" (introduces symbolic variables/execution as the basis of concolic execution).
- [[fuzzingbook-21-symbolic-fuzzer]] — *The Fuzzing Book* Ch 21, "Symbolic Fuzzing" (the full pure-symbolic treatment: `SimpleSymbolicFuzzer`/`SymbolicFuzzer`, CFG path enumeration, function summaries, loop unrolling).
