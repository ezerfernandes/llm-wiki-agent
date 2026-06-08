---
title: "The Fuzzing Book Ch 22 — Mining Function Specifications"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, specification-mining, dynamic-invariants, contracts, types, oracles]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-22-dynamic-invariants.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Mining Function Specifications

## Summary
This is the closing chapter of Part IV (Semantic Fuzzing) of *The Fuzzing Book*. Where [[fuzzingbook-20-concolic-fuzzer|Ch 20]] and [[fuzzingbook-21-symbolic-fuzzer|Ch 21]] *consume* specifications (types, ranges, pre-/postconditions) to generate inputs, this chapter shows how to *mine* such specifications from observed executions — Daikon-style [[DynamicInvariant|dynamic invariant]] detection. It builds two complementary tools: a `TypeAnnotator` that mines Python [[TypeInference|type annotations]] by tracing argument and return values, and an `InvariantAnnotator` that mines value [[InvariantInference|invariants]] (candidate [[Precondition|pre-]] and [[Postcondition|postconditions]] like `x > 0`, `return_value == a + b`, `return_value == len(L)`) by checking a catalog of candidate properties against all observed calls and keeping only those that always hold. The central worked example is the Newton–Raphson `my_sqrt(x)` (carried over from [[fuzzingbook-02-intro-testing|Ch 2]]), augmented with mined `@precondition`/`@postcondition` decorators that turn it into a self-checking [[TestOracle|oracle]]. The chapter closes the Part-IV arc by arguing that mined specs are only as good as the executions they observe — so pairing [[SpecificationMining|specification mining]] with comprehensive [[TestGeneration|test generators]] makes them precise, and that system-level fuzzing is an "infinite source of executions" for mining function-level contracts. Prerequisites are tracing from [[fuzzingbook-04-coverage|Ch 4]] and AST manipulation from [[fuzzingbook-19-information-flow|Ch 19]].

## Key Concepts
- **[[SpecificationMining|Specification mining]]** — retrofitting un-specified code with formal descriptions of what it expects and delivers, *learned* from runs rather than written by hand. Quoting Ken Thompson: "Without specifications, there are no bugs – only surprises."
- **[[DynamicInvariant|Dynamic invariants]]** — pre-/postconditions over arguments and variables inferred from a *set* of executions; the general recipe is (1) check every observed variable value against a fixed set of candidate properties, and (2) keep only properties that hold across *all* runs (set intersection).
- **Call tracing** — a `Tracker` base class arms `sys.settrace()` in a `with` block (`__enter__`/`__exit__`); the `CallTracker` subclass records, per `call`/`return` event, each function's `(argument_list, return_value)` via `get_arguments(frame)` reading `frame.f_locals`. This is the same tracing facility as the [[Coverage|coverage]] chapter, repurposed to capture *values* rather than *locations*.
- **[[TypeInference|Mining types]]** — `type_string(value)` returns the runtime type name; `annotate_function_ast_with_types()` parses each function with `ast.parse`, rewrites it with a `TypeTransformer(ast.NodeTransformer)` (`visit_FunctionDef`, `annotate_arg`), and unparses it back. Conflicting types across calls collapse to `typing.Any`. `TypeAnnotator.typed_functions()` ties tracking + annotation together. Output feeds a static checker like [[MyPy]] or constrains [[SymbolicExecution|symbolic analysis]].
- **[[InvariantInference|Mining invariants]]** — a list `INVARIANT_PROPERTIES` of templated properties over metavariables `X, Y, Z` (e.g. `"X > 0"`, `"X == Y + Z"`, `"isinstance(X, int)"`, `"X == len(Y)"`, `"X.startswith(Y)"`, `"X < Y < Z"`). Helpers `metavars()`, `instantiate_prop()`, `prop_function()` (turns a property into a `lambda`), and `true_property_instantiations()` (tries all `itertools.permutations` of args). `InvariantTracker.invariants()` intersects the satisfied-property sets across all calls; `return_value` is the special variable for the result.
- **Contract decorators** — a `condition(precondition, postcondition)` decorator factory (with `precondition`/`postcondition` shorthands) wraps a function so `@precondition(lambda x: x > 0)` and `@postcondition(lambda ret, x: ret*ret - x < EPSILON)` are `assert`-checked on every call — a runtime [[DesignByContract|design-by-contract]] / [[RunTimeVerification|run-time verification]] mechanism.
- **Emitting specs** — `InvariantAnnotator` (subclass of `InvariantTracker`) produces `preconditions()`/`postconditions()` (split by whether the invariant mentions `return_value`) and `functions_with_invariants()`, decorating the source. Exercise 9's `EmbeddedInvariantAnnotator` instead inserts the invariants as inline `assert` statements (a `PreconditionTransformer`/`EmbeddedInvariantTransformer` over the AST).
- **Mining from generated tests** — a single observed call *overspecializes* (e.g. `sum2(2,2)` mines the spurious `a == b`, `return_value == a*b`); diverse runs from a grammar fuzzer (`SUM2_EBNF_GRAMMAR` + `GrammarFuzzer`) shrink the invariant set to the true ones. The chicken-and-egg caveat: you need a (system-level) spec to drive generation that mines another (function-level) spec.

## Key Claims
- Type and value specifications can be *mined* automatically by observing a function and its invocations, requiring no hand-written annotations.
- A property becomes an invariant of a function iff it holds for *every* observed call; the inferred invariant set is the intersection of per-call satisfied-property sets, so it can only shrink as more (diverse) runs are seen.
- Mined types collapse to `Any` on type conflict (e.g. `my_sqrt` called with both `int` and `float`); mined value invariants similarly vanish when calls are sufficiently heterogeneous (e.g. `sum3` with mixed strings, numbers, and zeros leaves *no* invariants — "the price of flexibility").
- Mined pre-/postconditions and types serve as [[TestOracle|oracles]]: a regression that flips `my_sqrt` to return `-approx` is caught by the mined `return_value >= 0` / `return_value < x` postconditions on the first call.
- Mined invariants overspecialize to the observed values; the cure is more diverse executions, ideally from an automated [[TestGeneration|test generator]]. System-level fuzzing gives an "infinite source of executions" in which every function is called within its (implicit) precondition.
- The chapter's miner is deliberately incomplete versus [[Daikon]], which additionally supports data/object invariants, eliminates invariants implied by others, and applies statistical confidence to discard unlikely ones.

## Key Quotes
> "These so-called *dynamic invariants* produce pre- and post-conditions over function arguments and variables from a set of executions." — opening framing of the chapter.

> "Without specifications, there are no bugs – only surprises." — Ken Thompson, quoted to motivate retrofitting specs onto unspecified code.

> "The [DAIKON dynamic invariant detector](https://plse.cs.washington.edu/daikon/) can be considered the mother of function specification miners." — Background, on the seminal tool by Michael Ernst et al.

## Connections
- [[SpecificationMining]] — the umbrella technique this chapter mints; learning formal descriptions of behavior from executions.
- [[DynamicInvariant]] — the artifact produced: likely pre-/postconditions over args and return value.
- [[TypeInference]] — the `TypeAnnotator` mining of Python type annotations from observed values.
- [[InvariantInference]] — the `InvariantAnnotator` mining of value properties as candidate pre-/postconditions.
- [[Precondition]] / [[Postcondition]] / [[DesignByContract]] — the contract clauses the chapter both *checks* (via `@precondition`/`@postcondition` decorators) and *mines*.
- [[Assertion]] — the underlying check mechanism; Exercise 9 emits invariants as inline `assert`s.
- [[TestOracle]] / [[RunTimeVerification]] — mined specs become always-on oracles catching regressions on every call.
- [[DynamicAnalysis]] — the chapter is a dynamic analysis: it observes values at runtime via `sys.settrace`.
- [[Coverage]] — supplies the `sys.settrace` tracing facility reused here for value capture.
- [[Daikon]] — the seminal dynamic invariant detector this chapter reconstructs in miniature.
- [[AndreasZeller]] — lead author; this chapter continues his dynamic specification-mining research line.
- [[MyPy]] — the static type checker that consumes mined type annotations.
- [[CISPA]] — publisher of the book.
- [[fuzzingbook-02-intro-testing|Ch 2]] — source of the `my_sqrt` example and the pre-/postcondition framing this chapter mines.
- [[fuzzingbook-04-coverage|Ch 4]] — the `sys.settrace` tracing prerequisite.
- [[fuzzingbook-19-information-flow|Ch 19]] — the AST-manipulation prerequisite (parsing/transforming functions).
- [[fuzzingbook-20-concolic-fuzzer|Ch 20]] / [[fuzzingbook-21-symbolic-fuzzer|Ch 21]] — symbolic/concolic fuzzers that *consume* the types and ranges this chapter *produces*.
- [[fuzzingbook-18-grammar-miner|Ch 18]] — grammar mining, framed in the Background as another specification-mining approach (learning input formats).
- [[TestGeneration]] / [[Fuzzing]] — diverse generated runs are what make mined invariants precise.

## Contradictions
- None identified.
