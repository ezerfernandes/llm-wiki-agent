---
title: "Concolic Execution"
type: concept
tags: [concolic-execution, symbolic-execution, smt, z3, fuzzing, testing, dynamic-analysis, path-constraints, security]
sources: [fuzzingbook-20-concolic-fuzzer, fuzzingbook-21-symbolic-fuzzer]
last_updated: 2026-06-06
---

# Concolic Execution

**Concolic execution** (a portmanteau of **CONC**rete + symb**OLIC**) runs a program on a *concrete* input while simultaneously maintaining a *symbolic* shadow of every value derived from the input. As execution flows through conditionals, the concrete values decide which branch to take at runtime, and the symbolic shadow records the corresponding predicate. The accumulated conjunction of these branch predicates is the [[PathConstraint|path condition]]. Because the program always has real values to run with, concolic execution avoids the *path explosion* and *unmodeled-call* problems that hobble pure [[SymbolicExecution|symbolic execution]] — at the cost of only exploring one path per run. To explore *other* paths, one negates a branch's predicate and asks an [[SMTSolver|SMT solver]] for a new input satisfying the modified path condition.

## From The Fuzzing Book — Concolic Fuzzing
[[fuzzingbook-20-concolic-fuzzer|Ch 20]] implements concolic execution for Python with the `ConcolicTracer` context manager, used as `with ConcolicTracer() as _: _[fn](args)`. Each argument is wrapped in a *symbolic proxy* — `zbool`, `zint`, `zstr`, or `zfloat` — that carries both a Z3 symbolic expression (`.z`) and the concrete value (`.v`). The key trick is overriding Python's `__bool__()` on `zbool`: whenever a wrapped value is tested in an `if`/`while`, the proxy appends the symbolic predicate (or its negation, per the concrete outcome) to `ConcolicTracer.path`. Comparison and arithmetic dunders (`__eq__`, `__lt__`, `__add__`, `__getitem__`, `length()`, `startswith()`, `upper()`, `split()`, …) build the matching Z3 string-/integer-theory terms, so an ordinary Python function runs unmodified yet leaves behind its full path condition. The chapter shows the technique on `factorial()`, `triangle()`, `cgi_decode()`, and an SQL `db_select()`, and notes that proxies flow across function calls (`abs_max` → `abs_value`). Its stated limitations mirror [[DynamicTaintAnalysis|taint analysis]]: implicit/indirect control flow and calls into internal C functions discard symbolic information, and the tracer does not track string-length changes.

## From The Fuzzing Book — Symbolic Fuzzing
[[fuzzingbook-21-symbolic-fuzzer|Ch 21]] frames concolic execution as the pragmatic counterpart to *pure* [[SymbolicExecution|symbolic execution]]: "one of the ways in which the concolic execution simplifies symbolic execution is in the treatment of loops" — concolic runs avoid having to enumerate or bound every loop unrolling because the concrete run picks one path. The chapter also notes concolic execution's two advantages over static symbolic analysis are mirror images: symbolic execution needs *no sample input* and is unaffected by indirect (control-flow) information flow, whereas concolic execution requires a seed but can "go deeper than pure symbolic execution." Exercise 3 makes the relationship concrete by re-implementing concolic tracing **on top of** the chapter's [[SymbolicFuzzer|`SymbolicFuzzer`]]: a `ConcolicTracer(SymbolicFuzzer)` runs a seed under `TrackingArcCoverage`, follows only the seed's path during `explore()` to collect a representative [[PathConstraint|path condition]], then negates its last predicate to explore neighboring paths — demonstrating symbolic and concolic execution as two driving strategies over the same [[ExecutionTree|path tree]] and [[Z3Prover|Z3]] machinery.

## Concolic vs. symbolic vs. taint
- Versus [[DynamicTaintAnalysis|dynamic taint analysis]] ([[fuzzingbook-19-information-flow|Ch 19]]): taint tracking records *which* input bytes reach a location; concolic execution records *what must be true* of the input to reach it — a richer signal, but far more expensive at runtime.
- Versus [[SymbolicExecution|symbolic execution]] ([[fuzzingbook-21-symbolic-fuzzer|Ch 21]]): symbolic execution carries *no* concrete values and reasons about all paths abstractly; concolic execution keeps a concrete anchor, trading completeness for tractability.

## Connections
- [[SymbolicExecution]] — the symbolic half of "concolic"; concolic = concrete + symbolic.
- [[PathConstraint]] — the conjunction of branch predicates that concolic execution collects.
- [[PathExploration]] — negating path-condition predicates to reach new paths.
- [[SMTSolver]] / [[Z3Prover]] — the constraint engine that solves the collected (and negated) path conditions.
- [[ConcolicFuzzing]] — applying concolic execution to fuzzing (`SimpleConcolicFuzzer`, `ConcolicGrammarFuzzer`).
- [[DynamicTaintAnalysis]] / [[InformationFlow]] — the lighter Ch 19 technique that concolic execution strengthens.
- [[ControlFlow]] / [[BranchCoverage]] / [[Coverage]] — concolic execution targets un-taken branches to raise coverage.
- [[fuzzingbook-20-concolic-fuzzer|Ch 20]] / [[fuzzingbook-21-symbolic-fuzzer|Ch 21]] / [[fuzzingbook-19-information-flow|Ch 19]].

## Sources
- [[fuzzingbook-20-concolic-fuzzer]] — *The Fuzzing Book* Ch 20, "Concolic Fuzzing."
- [[fuzzingbook-21-symbolic-fuzzer]] — *The Fuzzing Book* Ch 21, "Symbolic Fuzzing" (concolic as the pragmatic counterpart to pure symbolic execution; Exercise 3 rebuilds a `ConcolicTracer` on the `SymbolicFuzzer`).
