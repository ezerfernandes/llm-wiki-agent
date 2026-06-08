---
title: "gcov"
type: entity
tags: [tool, coverage, c-language, gcc, testing]
sources: [fuzzingbook-04-coverage]
last_updated: 2026-06-06
---

# gcov

**gcov** is the GNU coverage utility (part of the GCC toolchain) that reports which lines of a C/C++ program were executed, and how many times, during a run. It is the C-world counterpart to Python's [[TraceFunction|`sys.settrace`]]-based [[Coverage|coverage]] tooling.

## Role in The Fuzzing Book — Code Coverage
[[fuzzingbook-04-coverage|Ch 4]] uses `gcov` to demonstrate that coverage measurement generalizes beyond Python. A C port of `cgi_decode` is compiled with `cc --coverage` (which instruments the binary to collect coverage at runtime); after the program runs, `gcov` produces a `.gcov` file in which each source line is prefixed by its execution count — `-` marks non-executable lines and `#####` marks zero-execution lines. The chapter's `read_gcov_coverage()` parses this file into the same `(file, line)` coverage set used by the Python `Coverage` class, so the rest of the book's coverage computations apply unchanged. In the example, the only uncovered line is the `return -1` for illegal input.

## Connections
- [[Coverage]] / [[LineCoverage]] — gcov measures statement coverage for compiled C/C++.
- [[TraceFunction]] — the Python analogue used elsewhere in the chapter.
- [[fuzzingbook-04-coverage|Ch 4]] — where gcov is demonstrated.

## Sources
- [[fuzzingbook-04-coverage]] — *The Fuzzing Book* Ch 4, "Code Coverage."
