---
title: "The Fuzzing Book Ch 20 — Concolic Fuzzing"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, concolic-execution, symbolic-execution, smt, z3, path-constraints]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-20-concolic-fuzzer.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Concolic Fuzzing

## Summary
Chapter 20 opens the path-sensitive thread of Part IV (Semantic Fuzzing) by teaching [[ConcolicExecution|concolic execution]] — CONCrete + symbOLIC execution — and turning it into a fuzzing strategy. The idea: run a Python function on a *concrete* sample input while a shadow layer of *symbolic* proxy values records the [[PathConstraint|path condition]] (the conjunction of every branch decision taken); then negate one branch's constraint and hand the result to the [[fuzzingbook-21-symbolic-fuzzer|Z3]] [[SMTSolver|SMT solver]] to synthesize a new input that drives execution down a different path. Where [[fuzzingbook-19-information-flow|Ch 19]]'s [[DynamicTaintAnalysis|dynamic taint analysis]] only tracks *which* input bytes reach a place, concolic execution captures *what must be true* of the input to reach it — a strictly richer (but costlier) signal. The chapter builds the `ConcolicTracer` context manager (with `zbool`/`zint`/`zstr`/`zfloat` symbolic proxy classes), then two fuzzers: `SimpleConcolicFuzzer`, which explores paths near a sample using a `TraceTree` binary tree of decisions, and `ConcolicGrammarFuzzer`, which *lifts* discovered string comparisons back into the input grammar. The running examples are `factorial()`, `triangle()`, `cgi_decode()`, and an `eval()`-vulnerable SQL `db_select()`. It is a prerequisite-light cousin of the heavier [[fuzzingbook-21-symbolic-fuzzer|symbolic fuzzing of Ch 21]], building on [[fuzzingbook-04-coverage|Ch 4]] (coverage) and [[fuzzingbook-19-information-flow|Ch 19]] (information flow).

## Key Concepts
- **[[ConcolicExecution|Concolic execution]]** — execute concretely while collecting symbolic constraints. The concrete value decides which branch to take at runtime; the symbolic shadow records the corresponding predicate. This sidesteps the path-explosion of pure [[SymbolicExecution|symbolic execution]] because the program always has a real value to run with.
- **`ConcolicTracer`** — the central context-manager class, used as `with ConcolicTracer() as _: _[fn](args)`. The `[fn]` item-access (`__getitem__`) inspects the function's parameters; `__call__` wraps each argument in a symbolic proxy via `concolic()`. After execution it exposes `decls` (symbolic-variable → type map), `path` (the list of collected predicates = the [[PathConstraint|path condition]]), and `context == (decls, path)`. `smt_expr()` renders the path as an [[SMTSolver|SMT-LIB]] S-expression; `zeval()` solves it (returning `('sat', {param: (value, type)})`) and accepts *negated/alternate* predicates keyed by index to obtain new inputs.
- **Symbolic proxy objects** — `zbool`, `zint`, `zstr`, `zfloat`. Each wraps a symbolic Z3 expression (`.z`) and a concrete value (`.v`). `zbool.__bool__()` is the hook that *registers a predicate*: it appends `self.z` (or `z3.Not(self.z)`) to `path` based on the concrete value, so ordinary Python `if`/`while` tests transparently record constraints. `zint`/`zstr` override comparison and arithmetic dunders (`__eq__`, `__lt__`, `__add__`, `__getitem__`, `length()`, `startswith()`, `find()`, `upper()`/`lower()`, `strip()`, `split()`) to build Z3 string/integer-theory terms. `zproxy_create()` registers a fresh symbolic variable in `decls`.
- **[[PathConstraint|Path condition]]** — the conjunction (`z3.And(path)`) of branch predicates along the executed path. Solving it reproduces the same path; solving it with one predicate negated yields an input on a *neighboring* path. `fresh_name()` mints unique variable names.
- **`SimpleConcolicFuzzer`** — implements the `Fuzzer` interface. A `TraceTree` (with `TraceNode` / `PlausibleChild`) stores observed decisions as a binary tree (`0`=else/`no_bit`, `1`=if/`yes_bit`); leaves are *unexplored* plausible children. `add_trace()` inserts a concolic trace; `fuzz()` picks a random unexplored leaf, builds its `path_expression()`, and solves it via `zeval_smt` to produce an input that forces the not-yet-taken branch.
- **`ConcolicGrammarFuzzer`** — extends [[GrammarFuzzer|`GrammarFuzzer`]]. It runs grammar-generated inputs under the tracer, then uses `span()` (mapping derivation-tree nodes to input substrings), `traverse_z3()`/`unwrap_substrings()` (extracting concrete string comparisons from predicates), and `find_alternatives()` to *lift* discovered constants (e.g. that a table must be named `inventory`) into new grammar alternatives via `update_grammar()`. This is [[PathExploration|path exploration]] guided by feedback into the [[Grammar|grammar]] itself.
- **[[SMTSolver|SMT solving with Z3]]** — `zeval_py()` uses the `z3.Solver()` Python API; `zeval_smt()` writes SMT-LIB to a temp file and shells out to the `z3` binary, parsing the model with `parse_sexp()`. Z3 understands the *theory of strings* and *theory of integers*, so it can solve constraints like `str.substr(s,0,1) == "+"`.

## Key Claims
- Concolic execution collects the constraints an execution path encounters and can answer questions about program behavior at any point along that path; negating those constraints and re-solving systematically explores other paths.
- A symbolic variable is "a sort of placeholder for the real variable, like the `x` in solving for `x` in algebra"; constraints over symbolic variables are solved by an [[SMTSolver|SMT solver]], which extends a SAT solver with background theories (integers, reals, bit-vectors, **strings**).
- Solving the unmodified [[PathConstraint|path condition]] yields an input that takes the *exact same path*; passing `_.zeval({i: negated_predicate})` replaces predicate `i` and yields an input on a different path (demonstrated turning an `equilateral` `triangle()` trace into an `isosceles` one).
- Concolic proxies propagate *across function calls* (shown with `abs_max()` calling `abs_value()`), because the proxy objects flow as ordinary arguments.
- `ConcolicGrammarFuzzer` reaches strictly deeper than a plain `GrammarFuzzer`: by lifting the constraint "table == inventory/vehicles/months" into the grammar, it gets past table-name validation that the plain grammar fuzzer never satisfies.
- Concolic execution generally provides more information than [[DynamicTaintAnalysis|taint analysis]] but at much larger runtime cost, so real-time analysis is usually infeasible.
- Both techniques share the same blind spots: *implicit/indirect control flow* and calls into internal C functions discard symbolic information (e.g. the tracer cannot track string-length changes, so strings sharing a prefix are treated alike).

## Key Quotes
> "We start with a sample input for the function, and execute the function under trace. At each point the execution passes through a conditional, we save the conditional encountered in the form of relations between symbolic variables." — the definition of concolic execution.

> "Concolic execution can often provide more information than taint analysis with respect to the program behavior. However, this comes at a much larger runtime cost. Hence, unlike taint analysis, real-time analysis is often not possible." — Lessons Learned.

> "The technique of concolic execution was originally used to inform and expand the scope of symbolic execution, a static analysis technique for program analysis." — Background, on the historical relation to [[SymbolicExecution|symbolic execution]] (King 1976).

## Connections
- [[ConcolicExecution]] — the core technique the chapter teaches and implements as `ConcolicTracer`.
- [[ConcolicFuzzing]] — the application of concolic execution to fuzzing (`SimpleConcolicFuzzer`, `ConcolicGrammarFuzzer`).
- [[SymbolicExecution]] — the foundational technique concolic execution combines with concrete execution; pure symbolic execution is the costlier sibling expanded in [[fuzzingbook-21-symbolic-fuzzer|Ch 21]].
- [[PathConstraint]] — the path condition collected in `ConcolicTracer.path` and solved/negated to explore paths.
- [[PathExploration]] — the systematic branch-negation strategy realized by the `TraceTree` and the grammar-lifting fuzzer.
- [[SMTSolver]] — the engine (Z3) that solves the path conditions; reused from [[fuzzingbook-17-fuzzing-with-constraints|Ch 17]].
- [[Z3Prover]] — Microsoft Research's Z3 SMT solver/theorem prover used throughout the chapter.
- [[DynamicTaintAnalysis]] / [[InformationFlow]] — Ch 19's technique that this chapter strengthens; the `db_select`/`INVENTORY_GRAMMAR` examples and `ConcolicDB` come directly from Ch 19.
- [[ControlFlow]] — the chapter visualizes coverage as control-flow-graph arcs and targets un-taken branches; implicit control flow is its main limitation.
- [[Coverage]] / [[BranchCoverage]] / [[PathCoverage]] — the `ArcCoverage(Coverage)` subclass and arcs motivate the technique (cover the red, un-taken branches).
- [[AndreasZeller]] / [[CISPA]] — lead author and publisher.
- [[fuzzingbook-19-information-flow|Ch 19]] — direct prerequisite (taint analysis, `DB`/`INVENTORY_GRAMMAR`).
- [[fuzzingbook-21-symbolic-fuzzer|Ch 21]] — the next, stronger-but-costlier symbolic-fuzzing step.
- [[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] — earlier SMT-solver-based (declarative) input generation.
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — search-based fuzzing offered as a cheaper alternative to SMT-driven path exploration.

## Contradictions
- None identified. The chapter is consistent with [[DynamicTaintAnalysis]] and [[SMTSolver]] as already described in the wiki; it positions concolic execution as the more complete (costlier) alternative to taint tracking, which those pages already anticipate.
