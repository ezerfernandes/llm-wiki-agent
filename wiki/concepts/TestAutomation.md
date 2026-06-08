---
title: "Test Automation"
type: concept
tags: [testing, fuzzing, quality, automation, software-engineering]
sources: [fuzzingbook-02-intro-testing]
last_updated: 2026-06-06
---

# Test Automation

**Test automation** is letting the computer both *run* a program on inputs and *check* its results, rather than doing either by hand. It is the prerequisite for testing at scale: once execution and checking are automated, a test suite can be re-run cheaply after every change, and the number of inputs checked is no longer bounded by human patience.

## From The Fuzzing Book — Introduction to Software Testing
[[fuzzingbook-02-intro-testing|Ch 2]] frames automation as the remedy for two weaknesses of manual testing: you can only check a "very limited number of executions and their results," and "after any change to the program, you have to repeat the testing process." The chapter automates the result-check with an [[Assertion|assert]] (and the `assertEquals` epsilon helper), then automates execution by sweeping inputs in a loop. Using its own `Timer` module it shows the economics: ~10,000 checks of `my_sqrt` run in well under a second (≈1 µs per call), so automated checking is essentially free and can be repeated "with every single change." Automation in this chapter spans three separable activities — **test execution**, **[[TestGeneration|test generation]]**, and **checking results** (the [[TestOracle|oracle]]) — each of which the rest of the book automates more aggressively.

## Connections
- [[TestGeneration]] / [[RandomTesting]] — automating the *production* of inputs.
- [[TestOracle]] / [[Assertion]] — automating the *checking* of results.
- [[RegressionTesting]] — re-running automated tests after every change to catch regressions.
- [[Fuzzing]] — the extreme of automated execution + generation.
- [[Pytest]] — a common framework for running automated test suites.
- [[Testing]] / [[UnitTesting]] — the practices automation operationalizes.

## Sources
- [[fuzzingbook-02-intro-testing]] — *The Fuzzing Book* Ch 2, "Introduction to Software Testing."
