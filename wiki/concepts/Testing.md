---
title: "Testing"
type: concept
tags: [testing, quality]
sources: [madewithml-testing, fuzzingbook-02-intro-testing, fuzzingbook-03-fuzzer, fuzzingbook-08-mutation-analysis, fuzzingbook-16-reducer]
last_updated: 2026-06-06
---

# Testing

The discipline of validating code, data, and models against expected behavior. Spans [[UnitTesting]], [[RegressionTesting]], [[CheckList]] suites for NLP, and behavioral tests, often via [[Pytest]].

## From The Fuzzing Book — Introduction to Software Testing
[[fuzzingbook-02-intro-testing|Ch 2]] of *The Fuzzing Book* gives the wiki's foundational definition: **testing is executing a program on a chosen input and checking whether the result is correct.** It decomposes testing into a [[TestCase|test case]] (input + check), a [[TestOracle|test oracle]] (the pass/fail decision, e.g. an [[Assertion|assert]]), [[TestGeneration|test generation]] / [[RandomTesting|random testing]], and [[TestAutomation|test automation]] of all three. It stresses the central limit echoed throughout the book — testing is **incomplete**, covering only a finite input subset and never proving the absence of bugs — and contrasts it with [[RunTimeVerification|run-time verification]] and proofs. This motivates the systematic [[Fuzzing|fuzzing]] techniques the rest of the book develops.

## From The Fuzzing Book — Fuzzing: Breaking Things with Random Inputs
[[fuzzingbook-03-fuzzer|Ch 3]] turns testing into *generated* testing and packages it as reusable infrastructure: a [[Runner|`Runner`]] executes the program under test and returns a `(result, outcome)` with `PASS`/`FAIL`/`UNRESOLVED`, while a [[RandomFuzzer|`Fuzzer`]] supplies the inputs. It broadens the [[TestOracle|oracle]] beyond known-answer checks to **generic runtime checkers** ([[AddressSanitizer]]) and **program-specific** ones ([[RepresentationInvariant|`repOK()`]] invariants, [[Assertion|assertions]], [[StaticAnalysis|static typing]]), with the doctrine to enable as many automatic checkers as possible since "CPU cycles are cheap, errors are expensive."

## From The Fuzzing Book — Mutation Analysis
[[fuzzingbook-08-mutation-analysis|Ch 8]] turns the lens back on the tests themselves: rather than asking whether a *program* is correct, it asks whether a *test suite* is good enough — the question of [[TestAdequacy|test adequacy]]. It argues that [[Coverage|coverage]] is a weak adequacy criterion (it ignores [[Assertion|assertion]] quality) and introduces [[MutationAnalysis|mutation analysis]]: seed artificial faults ([[Mutant|mutants]]) into the program and measure how many the suite kills ([[MutationScore|mutation score]]). It also reframes a test suite as "a program whose input is the program under test," uniting [[Fuzzing|fuzzing]] and testing under one lens.

## From The Fuzzing Book — Reducing Failure-Inducing Inputs
[[fuzzingbook-16-reducer|Ch 16]] addresses what happens *after* a test fails: the failing [[TestCase|test case]] is often a huge, noisy input that is hard to debug. [[InputReduction|Reduction]] automatically shrinks it — via [[DeltaDebugging|delta debugging]] ([[DDMin|`ddmin`]]) or [[GrammarReducer|grammar-based reduction]] — to a [[OneMinimality|1-minimal]] core, driven by a [[Runner|`Runner`]] whose [[TestOracle|oracle]] returns `FAIL` only for the *precise* failure of interest. A reduced test case lowers cognitive load, is far easier to communicate, and helps de-duplicate bug reports, making reduction the natural companion to fuzzing on the testing-and-debugging pipeline.
