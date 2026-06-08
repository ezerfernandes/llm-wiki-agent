---
title: "Path Constraint"
type: concept
tags: [path-constraints, path-condition, symbolic-execution, concolic-execution, smt, z3, fuzzing, testing]
sources: [fuzzingbook-20-concolic-fuzzer, fuzzingbook-21-symbolic-fuzzer]
last_updated: 2026-06-06
---

# Path Constraint

A **path constraint** (or **path condition**) is the conjunction of all branch decisions taken along one execution path through a program, expressed as a logical formula over the program's symbolic input variables. Every `if`/`while`/`elif` test that the path passes contributes one conjunct — the test's predicate if the true branch was taken, or its negation if the false branch was taken. The path condition characterizes *exactly which inputs follow this path*: any input satisfying it reproduces the path, and an [[SMTSolver|SMT solver]] can both check the condition's satisfiability (is the path feasible?) and produce a concrete witness input. Negating one conjunct and re-solving produces an input that diverges at that branch — the basic move of [[PathExploration|systematic path exploration]] in [[SymbolicExecution|symbolic]] and [[ConcolicExecution|concolic]] execution.

## From The Fuzzing Book — Concolic Fuzzing
[[fuzzingbook-20-concolic-fuzzer|Ch 20]] materializes the path condition as the `ConcolicTracer.path` attribute — a Python list of Z3 predicates accumulated as the program runs. Each symbolic proxy's `zbool.__bool__()` appends either `self.z` or `z3.Not(self.z)` depending on the concrete branch outcome, so the list is built transparently. `smt_expr()` renders the whole list as `z3.And(path)` in [[SMTSolver|SMT-LIB]] form; `zeval()` solves it. For example, tracing `cgi_decode('a%20d')` yields a 14-element path with conjuncts like `0 < Length(s)`, `Not(str.substr(s,0,1) == "+")`, and `str.substr(s,1,1) == "%"`. Solving the unmodified condition returns an input on the *same* path (`A%20B`); calling `_.zeval({1: <negated predicate>})` replaces conjunct 1 and returns an input that takes a *different* branch there. The `SimpleConcolicFuzzer` stores path conditions as root-to-leaf walks in a `TraceTree`; `PlausibleChild.path_expression()` reconstructs the path condition of an as-yet-unexplored branch by taking the path to the root and appending the (possibly negated) frontier predicate.

## From The Fuzzing Book — Symbolic Fuzzing
[[fuzzingbook-21-symbolic-fuzzer|Ch 21]] builds path conditions *statically* from the [[ControlFlow|control-flow graph]] rather than from a concrete run. For each enumerated path, `extract_constraints()` walks the path's CFG nodes and emits a Z3 conjunct per branch — the test's predicate if the if-branch was taken, `z3.Not(...)` if the else-branch was — plus an equality (`_v_k == expr`) for every assignment. The `SymbolicFuzzer` first rewrites the path into single-static-assignment form (`to_single_assignment_predicates()`, `rename_variables()`) so that reassigned variables become distinct names (`_v_0`, `_v_1`, …) within the condition. `solve_path_constraint()` recovers the variable types (`identifiers_with_types()`), declares the Z3 symbolic variables (`define_symbolic_vars()`), solves the condition under a `checkpoint()` (push/pop), and adds `z3.Not(solution)` to avoid repeats. The chapter shows path conditions proving infeasibility (`check_triangle`'s `a==b ∧ a==c ∧ b≠c` is unsat) and being merged across paths into a single *function summary* predicate (`z3.Or(...)`) at a function's exit. Exercise 3 reuses the same conditions for concolic exploration by negating the *last* conjunct to reach a neighboring path.

## Connections
- [[ConcolicExecution]] — collects the path constraint in `ConcolicTracer.path` during concrete-plus-symbolic execution.
- [[SymbolicExecution]] — checks each path's constraint for feasibility while forking at branches.
- [[PathExploration]] — negating individual conjuncts of the path constraint is how new paths are reached.
- [[SMTSolver]] / [[Z3Prover]] — solves the path constraint (and its negated variants) for concrete inputs.
- [[ControlFlow]] / [[BranchCoverage]] — each conjunct corresponds to one branch decision; negating it flips that branch.
- [[fuzzingbook-20-concolic-fuzzer|Ch 20]] — where the path condition is built as a list of Z3 predicates.

## Sources
- [[fuzzingbook-20-concolic-fuzzer]] — *The Fuzzing Book* Ch 20, "Concolic Fuzzing."
- [[fuzzingbook-21-symbolic-fuzzer]] — *The Fuzzing Book* Ch 21, "Symbolic Fuzzing" (path conditions built statically from the CFG via `extract_constraints`/`to_single_assignment_predicates`, with SSA renaming and function summaries).
