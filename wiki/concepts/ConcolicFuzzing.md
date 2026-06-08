---
title: "Concolic Fuzzing"
type: concept
tags: [concolic-execution, fuzzing, testing, smt, z3, grammar-fuzzing, path-constraints, semantic-fuzzing, security]
sources: [fuzzingbook-20-concolic-fuzzer]
last_updated: 2026-06-06
---

# Concolic Fuzzing

**Concolic fuzzing** is test-input generation driven by [[ConcolicExecution|concolic execution]]: rather than mutating inputs blindly, the fuzzer traces a program on a sample input, collects the [[PathConstraint|path condition]], negates one or more branch predicates, and solves the result with an [[SMTSolver|SMT solver]] to synthesize a new input *guaranteed* to take a different path. Iterating this turns the fuzzer into a [[PathExploration|systematic path explorer]] that reaches branches a random or fixed seed would miss. It sits between cheap blackbox/greybox fuzzing and full [[SymbolicExecution|symbolic fuzzing]]: more directed than the former, cheaper than the latter, because it always has a concrete execution to anchor on.

## From The Fuzzing Book — Concolic Fuzzing
[[fuzzingbook-20-concolic-fuzzer|Ch 20]] builds two concolic fuzzers on top of the `ConcolicTracer`:
- **`SimpleConcolicFuzzer`** (implements the `Fuzzer` interface) stores observed concolic traces in a `TraceTree` of branch decisions and keeps the unexplored frontier as `PlausibleChild` leaves. `add_trace()` inserts a trace; `fuzz()` picks a random unexplored leaf, builds its path condition, and solves it to produce an input forcing a not-yet-taken branch. It explores paths *close to* a seed but is "not very intelligent" about which to pursue.
- **`ConcolicGrammarFuzzer`** (extends [[GrammarFuzzer|`GrammarFuzzer`]]) is smarter: it knows the input [[Grammar|grammar]] and collects feedback from the program under test. Using `span()`, `traverse_z3()`, and `find_alternatives()`, it *lifts* concrete string comparisons discovered during tracing (e.g. that a query's table must equal `inventory`) into new grammar alternatives via `update_grammar()`, so later inputs satisfy those deep equality constraints and reach code (the `eval()`-vulnerable `my_eval()`) the plain grammar fuzzer never reaches.

The chapter demonstrates both on `cgi_decode()` and an SQL `db_select()` from [[fuzzingbook-19-information-flow|Ch 19]]. Its Lessons Learned: concolic-derived predicates make a stronger bug-indicator than [[DynamicTaintAnalysis|taints]] and can build grammars that produce *valid* deep inputs — but at much higher runtime cost, and with the same implicit-control-flow / internal-C-function blind spots as taint analysis.

## Connections
- [[ConcolicExecution]] — the underlying execution model (`ConcolicTracer`) the fuzzers run on.
- [[PathExploration]] — what concolic fuzzing does: negate branch predicates to discover new paths.
- [[PathConstraint]] — the conditions collected and negated to drive generation.
- [[SMTSolver]] / [[Z3Prover]] — solves the (negated) path conditions into concrete fuzzing inputs.
- [[GrammarFuzzer]] / [[Grammar]] — `ConcolicGrammarFuzzer` extends grammar fuzzing by lifting discovered constants into the grammar.
- [[DynamicTaintAnalysis]] / [[TaintDirectedFuzzing]] — the Ch 19 technique concolic fuzzing strengthens (richer signal, higher cost).
- [[Fuzzing]] / [[CoverageGuidedFuzzing]] — the broader fuzzing family this directed strategy belongs to.
- [[fuzzingbook-20-concolic-fuzzer|Ch 20]] / [[fuzzingbook-21-symbolic-fuzzer|Ch 21]] / [[fuzzingbook-19-information-flow|Ch 19]] / [[fuzzingbook-07-search-based-fuzzer|Ch 7]].

## Sources
- [[fuzzingbook-20-concolic-fuzzer]] — *The Fuzzing Book* Ch 20, "Concolic Fuzzing."
