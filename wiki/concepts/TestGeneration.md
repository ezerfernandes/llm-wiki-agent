---
title: "Test Generation"
type: concept
tags: [testing, fuzzing, quality, automation, software-engineering]
sources: [fuzzingbook-02-intro-testing]
last_updated: 2026-06-06
---

# Test Generation

**Test generation** is the automatic production of inputs (and, where possible, expected outcomes) for a program under test, rather than hand-writing each [[TestCase|test case]]. It is the central subject of *The Fuzzing Book*: every fuzzing technique in the book — random, mutation-based, grammar-based, search-based, constraint-based, symbolic — is ultimately a test-generation strategy, differing in how cleverly it explores the input space.

## From The Fuzzing Book — Introduction to Software Testing
[[fuzzingbook-02-intro-testing|Ch 2]] introduces test generation in its simplest form: instead of asserting one value, it generates inputs in a loop (`for n in range(1, 1000)`) and checks each against the property oracle √x·√x = x, then escalates to [[RandomTesting|random]] inputs via `random.random()`. The key requirement it surfaces is the [[TestOracle|oracle]] problem — generating inputs is easy, but checking arbitrary generated inputs needs a property oracle, not a known-answer one. It also surfaces the requirement that, to *call a function* with generated values, "we have to *know* its precise [[Precondition|preconditions]]" — otherwise generated inputs trip latent crashes (`my_sqrt(0)` divides by zero; a negative argument loops forever). Finally it gives the quantitative case (Exercise 3) for why naive generation is insufficient: a rare two-zero corner case has probability ~1/2⁶⁴, i.e. ~584 years at a billion tests/sec — motivating the *guided* and *structured* generation techniques that follow.

## Connections
- [[RandomTesting]] — the simplest test-generation strategy; unbiased but blind to rare special values.
- [[Fuzzing]] — automated, often coverage-guided test generation at scale.
- [[TestOracle]] — needed to judge the results of generated inputs.
- [[Precondition]] — generated calls must respect the target's preconditions.
- [[PropertyBasedTesting]] — strategy-driven generation of structured valid inputs.
- [[TestAutomation]] — generation is one of the three automatable testing activities.
- [[fuzzingbook-03-fuzzer|Ch 3]] — the first concrete generator (the random `Fuzzer`).

## Sources
- [[fuzzingbook-02-intro-testing]] — *The Fuzzing Book* Ch 2, "Introduction to Software Testing."
