---
title: "Unit Testing"
type: concept
tags: [testing, quality]
sources: [madewithml-testing, fuzzingbook-02-intro-testing, fuzzingbook-08-mutation-analysis, fuzzingbook-25-carver]
last_updated: 2026-06-06
---

# Unit Testing

Testing the smallest functional units of code in isolation. The foundation of [[Testing]] pyramids and continuous integration in [[Python]] codebases via [[Pytest]] and [[PytestCov]].

## From The Fuzzing Book — Introduction to Software Testing
[[fuzzingbook-02-intro-testing|Ch 2]] shows the example-based unit test in its most primitive form: a [[TestCase|test case]] is a single input plus an [[Assertion|assert]]-based [[TestOracle|oracle]] (`assert my_sqrt(4) == 2`, with epsilon tolerance for floats). It demonstrates why hand-written unit tests are flexible but don't scale — limited count, must be repeated after every change — motivating [[TestAutomation|automation]] and [[TestGeneration|generated]] tests, and ultimately property-style oracles ([[PropertyBasedTesting]]) and [[Fuzzing|fuzzing]].

## From The Fuzzing Book — Mutation Analysis
[[fuzzingbook-08-mutation-analysis|Ch 8]] uses Python's `unittest` framework as the unit being *graded*: its `MuProgramAnalyzer` drives `unittest.TestCase` suites (`StrongShapeTest`, `WeakShapeTest`, `TestGCD`) against each [[Mutant|mutant]] of a module via a `MutantTestRunner` (`unittest.TestSuite` + `TextTestRunner(failfast=True)`). The chapter shows that *passing* unit tests are only meaningful if the suite is *adequate* ([[TestAdequacy]]): two suites with identical [[Coverage|coverage]] earn 20% vs 100% [[MutationScore|mutation score]], so it pairs unit testing with [[MutationAnalysis|mutation analysis]] to judge suite quality.

## From The Fuzzing Book — Carving Unit Tests
[[fuzzingbook-25-carver|Ch 25]] shows that unit tests need not be written by hand at all — they can be *carved* from a system test ([[TestCarving]]). A [[Carver|`CallCarver`]] records every function call (name + arguments) during an end-to-end run, and each recording is synthesized back into a standalone unit test (replayed via `eval`, with [[Serialization|pickled]] complex objects). Because a single function call is orders of magnitude faster than the whole system, these carved unit tests run far cheaper than the [[IntegrationTesting|system test]] they came from; mining a grammar from the carved calls ([[APIGrammarMining]]) further turns them into [[APIFuzzing|API fuzzing]].
