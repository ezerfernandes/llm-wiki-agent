---
title: "Test Case"
type: concept
tags: [testing, fuzzing, quality, software-engineering]
sources: [fuzzingbook-02-intro-testing]
last_updated: 2026-06-06
---

# Test Case

A **test case** is a single, concrete pairing of an *input* fed to the program under test and a *check* applied to the resulting behavior. In the framing of *The Fuzzing Book*, testing is precisely the act of *executing* a program on a given input and *checking* whether its result is correct — so a test case is one instance of that execute-and-check loop. The check itself is the [[TestOracle|test oracle]]; the input may be hand-written (manual testing) or produced by [[TestGeneration|test generation]] / [[Fuzzing|fuzzing]].

## From The Fuzzing Book — Introduction to Software Testing
[[fuzzingbook-02-intro-testing|Ch 2]] introduces the test case through the running `my_sqrt(x)` example: a manual test is just `my_sqrt(2)` followed by a sanity check that `my_sqrt(2) * my_sqrt(2) ≈ 2`, described as "the bare minimum of quality assurance before a program goes into production." The chapter notes that manual test cases are flexible but inefficient — you can only check a handful by hand, and you must repeat them after every change — which motivates compacting each case with an [[Assertion|assert]], then automating execution ([[TestAutomation]]) and generating cases at scale ([[TestGeneration]], [[RandomTesting]]). Exercises generalize the idea to lists (Shellsort, checked with `is_sorted`/`is_permutation` oracles) and to corner-case selection ("extreme cases" such as empty lists, duplicates, and boundary values).

## Connections
- [[TestOracle]] — the pass/fail check half of a test case.
- [[Assertion]] — the usual compact encoding of a test case's check.
- [[TestAutomation]] — running many test cases without manual effort.
- [[TestGeneration]] / [[RandomTesting]] — producing test-case inputs automatically.
- [[Testing]] / [[UnitTesting]] — test cases are the atoms of these practices.
- [[Fuzzing]] — generates vast numbers of (often invalid) test-case inputs.

## Sources
- [[fuzzingbook-02-intro-testing]] — *The Fuzzing Book* Ch 2, "Introduction to Software Testing."
