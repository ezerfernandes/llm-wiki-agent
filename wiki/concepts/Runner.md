---
title: "Runner"
type: concept
tags: [fuzzing, testing, harness, python, class-hierarchy, software-engineering]
sources: [fuzzingbook-03-fuzzer, fuzzingbook-05-mutation-fuzzer, fuzzingbook-28-gui-fuzzer]
last_updated: 2026-06-06
---

# Runner

**`Runner`** is *The Fuzzing Book*'s **fuzzing-harness abstraction**: the object whose job is to execute the program (or function) under test on a given input and classify the result. It is the counterpart to the [[RandomFuzzer|`Fuzzer`]] base class — a [[Fuzzing|fuzzer]] *generates* inputs, a `Runner` *consumes* them and decides whether the run passed, failed, or could not be judged. The pairing `fuzzer.run(runner)` is the core feedback unit the whole book builds on.

## The interface
A `Runner` exposes `run(inp) -> (result, outcome)`:

- `result` — a runner-specific value with the run's details (e.g. a `subprocess.CompletedProcess`).
- `outcome` — one of three constants: `Runner.PASS` (correct), `Runner.FAIL` (incorrect / crashed), `Runner.UNRESOLVED` (the run could not take place or be judged, e.g. an invalid input).

The three-valued outcome is significant: a random input usually produces `UNRESOLVED`, not `FAIL`, which is precisely why blackbox random fuzzing struggles to reach meaningful failures and why later chapters add coverage feedback and structure.

## From The Fuzzing Book — Fuzzing: Breaking Things with Random Inputs
[[fuzzingbook-03-fuzzer|Ch 3]] defines `Runner` and three subclasses:

- **`PrintRunner`** — echoes the input and returns `UNRESOLVED`; the default runner for demonstrations.
- **`ProgramRunner`** — runs an external program via `subprocess.run(self.program, input=inp, ...)` and maps the OS return code to an outcome: `0 → PASS`, negative (terminated by signal) `→ FAIL`, positive `→ UNRESOLVED`. Demonstrated with `cat` and `bc`.
- **`BinaryProgramRunner`** — a `ProgramRunner` variant that encodes input as bytes for binary stdin (used to fuzz the real `troff` in the exercises).

This interface is deliberately minimal so later chapters can subclass it: e.g. coverage-collecting runners in [[fuzzingbook-04-coverage|Ch 4]] and [[fuzzingbook-06-greybox-fuzzer|Ch 6]], or `FunctionRunner`/specialized runners that wrap Python callables. The custom `TroffRunner` in the chapter's exercises shows the pattern — subclass `Runner`, override `run()` to apply program-specific [[Assertion|assertion]] checkers, and tally failures.

## From The Fuzzing Book — Mutation-Based Fuzzing
[[fuzzingbook-05-mutation-fuzzer|Ch 5]] adds two `Runner` subclasses that wrap a Python *callable* (rather than an external program): `FunctionRunner(function)` calls `function(inp)` in `run()`, returning `(result, PASS)` or `(None, FAIL)` on exception; `FunctionCoverageRunner` extends it to execute the call inside a `with Coverage() as cov` block and expose the executed [[Coverage|`Location`]] set via `coverage()` after each run (even on exceptions). This coverage-capturing runner is what [[MutationCoverageFuzzer|`MutationCoverageFuzzer`]] consumes to decide which mutated inputs to keep — the `Runner` becoming the source of the [[CoverageGuidedFuzzing|coverage feedback signal]].

## From The Fuzzing Book — Testing Graphical User Interfaces
[[fuzzingbook-28-gui-fuzzer|Ch 28]] subclasses `Runner` as `GUIRunner` for [[GUIFuzzing|GUI fuzzing]]: rather than feeding an input to a program, its `run(inp)` *executes an action string* (e.g. `fill('name', 'Walter White')\nsubmit('submit')`) against a live [[Selenium]] browser. It does so with `exec()` over the four action functions (`fill`/`check`/`submit`/`click`), with `__builtins__` set to `{}` and `html.escape()`d element names to limit code injection through UI element names (a residual risk flagged in [[fuzzingbook-19-information-flow|Ch 19]]). The `do_*` methods defer to Selenium with explicit `WebDriverWait` delays. It pairs with [[GUIFuzzer|`GUIFuzzer`]] exactly as the base `Runner` pairs with a `Fuzzer` — `gui_fuzzer.run(gui_runner)`.

## Connections
- [[GUIFuzzer]] — the Ch 28 `GUIRunner` subclass executes UI action strings via Selenium.
- [[Selenium]] — the framework `GUIRunner` drives.
- [[RandomFuzzer]] — the `Fuzzer` side of the pair; `fuzzer.run(runner)` and `fuzzer.runs(runner, trials)` drive a `Runner`.
- [[MutationCoverageFuzzer]] — driven by the Ch 5 `FunctionCoverageRunner` to get per-input coverage.
- [[Fuzzing]] — the harness through which generated inputs reach the program under test.
- [[Assertion]] / [[RepresentationInvariant]] — program-specific checkers a custom `Runner` can apply to detect subtle failures.
- [[Testing]] — the `(result, outcome)` model is a test-execution + [[TestOracle|oracle]] step.
- [[fuzzingbook-03-fuzzer|Ch 3]] — where `Runner`/`PrintRunner`/`ProgramRunner`/`BinaryProgramRunner` are defined.
- [[fuzzingbook-04-coverage|Ch 4]] / [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — chapters that subclass `Runner` to collect coverage.

## Sources
- [[fuzzingbook-03-fuzzer]] — *The Fuzzing Book* Ch 3, "Fuzzing: Breaking Things with Random Inputs."
- [[fuzzingbook-05-mutation-fuzzer]] — *The Fuzzing Book* Ch 5, "Mutation-Based Fuzzing" (the `FunctionRunner`/`FunctionCoverageRunner` callable-wrapping runners).
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces" (the `GUIRunner` executing UI action strings via Selenium).
