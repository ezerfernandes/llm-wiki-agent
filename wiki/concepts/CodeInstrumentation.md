---
title: "Code Instrumentation"
type: concept
tags: [testing, instrumentation, ast, dynamic-analysis, search-based-testing, coverage]
sources: [fuzzingbook-07-search-based-fuzzer]
last_updated: 2026-06-06
---

# CodeInstrumentation

**Instrumentation** is the insertion (or transformation) of code into a program so that its execution can be *observed* — recording which lines/branches run, capturing the operand values at a condition, or computing a [[BranchDistance|branch distance]]. It is the mechanism that turns a program's runtime behavior into a measurable signal for [[Coverage|coverage]] tracking, [[SearchBasedTesting|search-based testing]] fitness, and greybox-fuzzing feedback.

## From The Fuzzing Book — Search-Based Fuzzing
[[fuzzingbook-07-search-based-fuzzer|Ch 7]] needs instrumentation because the values compared in a branch may be derived deep inside the function, so a [[FitnessFunction|fitness function]] must observe them *at the conditional statement* during a real execution. The chapter escalates through three designs:
- **Global variable** — `test_me_instrumented` writes `calculate_distance(...)` into a global `distance` that the fitness function reads. Simple, but clumsy and unsafe.
- **Condition transformation** — to avoid double-evaluating operands (which would re-trigger side effects and break short-circuiting), the comparison `x == 2*foo(y)` is *replaced* by a call `evaluate_condition(num, op, lhs, rhs)` that evaluates each operand once, computes true/false distances, stores them in the `distances_true`/`distances_false` maps via `update_maps`, and returns the boolean.
- **Automatic AST rewriting** — `BranchTransformer(ast.NodeTransformer)` overrides `visit_Compare` to rewrite every comparison into an `evaluate_condition(...)` call and `visit_FunctionDef` to append `_instrumented` to the name; `create_instrumented_function(f)` parses the source (`ast.parse`/`inspect.getsource`), transforms it, then `compile`s and `exec`s the result into the current module so e.g. `cgi_decode_instrumented` becomes directly callable.

This is the same observation idea as Ch 4's `sys.settrace`-based [[Coverage|`Coverage`]] class, but tailored to extract *distance* rather than just executed-line sets.

## Connections
- [[BranchDistance]] — the quantity instrumentation computes and records.
- [[FitnessFunction]] — instrumentation supplies the fitness value from a concrete run.
- [[SearchBasedTesting]] — relies on instrumentation to score candidate inputs.
- [[Coverage]] / [[BranchCoverage]] — coverage tracking is the other major use of instrumentation.
- [[fuzzingbook-04-coverage|Ch 4]] — the `sys.settrace` `Coverage` class this chapter parallels.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — greybox fuzzing uses (compile-time/binary) instrumentation for coverage feedback.
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — where AST-based branch instrumentation is built.

## Sources
- [[fuzzingbook-07-search-based-fuzzer]] — *The Fuzzing Book* Ch 7, "Search-Based Fuzzing."
