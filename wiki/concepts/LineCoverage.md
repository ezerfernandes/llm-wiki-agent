---
title: "Line (Statement) Coverage"
type: concept
tags: [testing, coverage, fuzzing, dynamic-analysis, white-box-testing]
sources: [fuzzingbook-04-coverage]
last_updated: 2026-06-06
---

# LineCoverage

**Line coverage** (a.k.a. **statement coverage**) is the white-box [[Coverage|coverage]] criterion that requires *each statement in the program to be executed by at least one test input*. It is the simplest and most widely used coverage metric: the rationale is that a statement never executed during testing can never have its faults triggered.

## From The Fuzzing Book — Code Coverage
[[fuzzingbook-04-coverage|Ch 4]] operationalizes statement coverage as the *set* of executed `(function_name, line_number)` [[TraceFunction|`Location`]] pairs returned by the `Coverage` class's `coverage()` method. Lines not in the set are annotated with `#` when the coverage object is printed, directing the developer's attention to untested code. The chapter shows that on the running `cgi_decode()` example the manually written black-box assertions happen to also achieve full statement coverage (a common coincidence, since distinct behaviors live in distinct code locations), and that the random `fuzzer()` from [[fuzzingbook-03-fuzzer|Ch 3]] reaches full statement coverage after about **40–60 inputs** on average. Statement coverage is contrasted with the stricter [[BranchCoverage|branch coverage]]: the two coincide on a simple `if/else`, but diverge when an `if` has no `else` body — statement coverage is satisfied by a single true-case test, whereas branch coverage also demands the false case.

## Connections
- [[Coverage]] — the umbrella concept; line coverage is its most basic criterion.
- [[BranchCoverage]] — the stricter sibling criterion (decisions, not just statements).
- [[TraceFunction]] — `sys.settrace` is the mechanism by which executed lines are recorded.
- [[CoverageGuidedFuzzing]] — line coverage is one feedback signal a coverage-guided fuzzer can chase.
- [[RandomFuzzer]] — the Ch 3 fuzzer whose statement-coverage growth is measured.
- [[fuzzingbook-04-coverage|Ch 4]] — where this criterion is operationalized.

## Sources
- [[fuzzingbook-04-coverage]] — *The Fuzzing Book* Ch 4, "Code Coverage."
