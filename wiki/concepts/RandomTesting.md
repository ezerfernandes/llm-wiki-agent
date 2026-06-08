---
title: "Random Testing"
type: concept
tags: [testing, fuzzing, quality, automation, software-engineering]
sources: [fuzzingbook-02-intro-testing, fuzzingbook-03-fuzzer]
last_updated: 2026-06-06
---

# Random Testing

**Random testing** generates inputs at random (within some range or distribution) and checks each against a [[TestOracle|test oracle]]. It is the simplest form of [[TestGeneration|test generation]] and the conceptual ancestor of [[Fuzzing|fuzzing]]. Its appeal is that it explores far more of the input space than hand-picked examples; its weakness is that an unbiased random source is unlikely to hit narrow "special" inputs that trigger qualitatively different behavior.

## From The Fuzzing Book — Introduction to Software Testing
[[fuzzingbook-02-intro-testing|Ch 2]] runs `assertEquals(my_sqrt(x) * my_sqrt(x), x)` for 10,000 values of `x = 1 + random.random() * 1000000`, all passing within a second — illustrating how cheaply random testing reinforces confidence after each code change. It then states the central caveat precisely: a random function is "*unbiased* in producing random values" but "is unlikely to generate special values that drastically alter program behavior." Concretely, `my_sqrt(0)` divides by zero, yet even sampling 0–1,000,000 the chance of drawing exactly 0 is ~1 in a million. Exercise 3 quantifies the limit further: a corner case requiring two 32-bit values to both be zero has probability ~1/2⁶⁴ — ~584 years to hit at a billion tests/sec, the chapter's argument that "pure random choices are not sufficient as sole testing strategy" and the motivation for coverage-guided, grammar-based, and search-based generation in later parts.

## From The Fuzzing Book — Fuzzing: Breaking Things with Random Inputs
[[fuzzingbook-03-fuzzer|Ch 3]] is random testing applied to *raw strings*: the `fuzzer()` function (and its class form [[RandomFuzzer|`RandomFuzzer`]]) picks a random length and fills it with `chr(random.randrange(...))` characters. The chapter realizes Ch 2's prediction — unguided random inputs are mostly *invalid* (the `bc` run yields parse/syntax errors, almost never a crash) — which is exactly why the same `Runner` harness is later paired with mutation, coverage feedback, and grammars. It is also the historical link: [[BartonMiller|Barton Miller]]'s 1989 fuzz generator was random testing of UNIX utilities, and it still found bugs in a third of them.

## Connections
- [[TestGeneration]] — random testing is the baseline generation strategy.
- [[RandomFuzzer]] / [[Runner]] — random testing of strings, packaged as the book's reusable fuzzer/harness classes.
- [[BartonMiller]] — ran the first random-testing experiment on real programs.
- [[Fuzzing]] — extends random testing with feedback (coverage), mutation, and structure.
- [[TestOracle]] / [[Assertion]] — the property oracle that judges each random input.
- [[Coverage]] — the feedback signal greybox fuzzing adds to overcome random testing's blindness.
- [[PropertyBasedTesting]] — adds structured generation and shrinking on top of random sampling.
- [[fuzzingbook-03-fuzzer|Ch 3]] / [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — the random fuzzer and its coverage-guided successor.

## Sources
- [[fuzzingbook-02-intro-testing]] — *The Fuzzing Book* Ch 2, "Introduction to Software Testing."
- [[fuzzingbook-03-fuzzer]] — *The Fuzzing Book* Ch 3, "Fuzzing: Breaking Things with Random Inputs."
