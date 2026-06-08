---
title: "Symbolic Variable"
type: concept
tags: [symbolic-execution, concolic-execution, smt, z3, fuzzing, testing, path-constraints]
sources: [fuzzingbook-21-symbolic-fuzzer]
last_updated: 2026-06-06
---

# Symbolic Variable

A **symbolic variable** is a placeholder standing for "any value" of a given type, used in [[SymbolicExecution|symbolic]] and [[ConcolicExecution|concolic]] execution instead of a concrete datum. It behaves "like the `x` in solving for `x` in algebra": operations on it build up a symbolic *expression* rather than computing a number, and conditions on it accumulate into a [[PathConstraint|path condition]] that an [[SMTSolver|SMT solver]] later solves for a concrete witness. Each input parameter (and, in symbolic execution, each local) becomes a typed symbolic variable in the solver's logic — an `Int`, `Real`, or `String` term in Z3.

## From The Fuzzing Book — Symbolic Fuzzing
[[fuzzingbook-21-symbolic-fuzzer|Ch 21]] derives symbolic variables directly from a function's **type annotations**: `get_annotations()` reads the signature, and `get_symbolicparams()` maps each parameter through the `SYM_VARS` table — `int → z3.Int`, `float → z3.Real`, `str → z3.String` (with matching value constructors `z3.IntVal`/`z3.RealVal`/`z3.StringVal`) — to mint Z3 symbolic constants. Correct annotations on *all* parameters **and local variables** are a hard requirement of the [[SymbolicFuzzer|`SymbolicFuzzer`]]. Because the full `SymbolicFuzzer` allows variable reassignment, each assignment spawns a *new* symbolic variable in single-static-assignment style (`v` → `_v_0`, `_v_1`, …) via `rename_variables()` / `to_single_assignment_predicates()`, so a reused name never collides. Helpers `z3_names_and_types()`, `used_identifiers()`, `declarations()`/`used_vars()`, and `define_symbolic_vars()` recover the names/types of the symbolic variables used in a constraint and regenerate their Z3 declarations for `exec()`. The same idea underlies function summaries, where `prefix_vars()` namespaces a callee's symbolic variables per call site (the SMT-LIB `define-fun` macro facility is not exposed by z3py).

## Connections
- [[SymbolicExecution]] — operates entirely over symbolic variables (no concrete run).
- [[ConcolicExecution]] — pairs each symbolic variable with a concrete value (the [[fuzzingbook-20-concolic-fuzzer|Ch 20]] proxies `zint`/`zstr`/`zfloat`).
- [[PathConstraint]] — the formula built from operations and conditions on symbolic variables.
- [[SMTSolver]] / [[Z3Prover]] — solve the constraints over typed symbolic variables (`z3.Int`/`z3.Real`/`z3.String`).
- [[SymbolicFuzzer]] — derives symbolic variables from type annotations and renames them per assignment.
- [[ControlFlow]] — branches on symbolic variables are the fork points of symbolic execution.
- [[fuzzingbook-21-symbolic-fuzzer|Ch 21]] / [[fuzzingbook-20-concolic-fuzzer|Ch 20]].

## Sources
- [[fuzzingbook-21-symbolic-fuzzer]] — *The Fuzzing Book* Ch 21, "Symbolic Fuzzing" (symbolic variables from type annotations via `SYM_VARS`/`get_symbolicparams`, SSA renaming).
