---
title: "Barton Miller"
type: entity
tags: [person, researcher, fuzzing, software-engineering, security, computer-science]
sources: [fuzzingbook-03-fuzzer]
last_updated: 2026-06-06
---

# Barton Miller

**Barton ("Bart") Miller** is a computer scientist at the **University of Wisconsin–Madison**, widely credited as the **originator of fuzzing**. He coined the term *"fuzz"* for random, unstructured input data and ran the first systematic fuzzing study of UNIX utilities.

## Role in The Fuzzing Book
[[fuzzingbook-03-fuzzer|Ch 3]] of *The Fuzzing Book* opens with Miller's origin story: on a "dark and stormy night in the Fall of 1988," line noise on a 1200-baud modem corrupted the input to UNIX commands and crashed them. Surprised that programs were so fragile, Miller turned the observation into a graduate programming assignment (CS736) that had students *build a fuzz generator and use it to attack as many UNIX utilities as possible.* The resulting 1989/1990 experiment found that **about a third** of the tested utilities crashed or hung on random input — the seminal result reported in "An Empirical Study of the Reliability of UNIX Utilities" (Miller et al., 1990), cited in the chapter as a must-read foundation of the field whose observations "are as valid today as they were 30 years ago."

## Connections
- [[Fuzzing]] — Miller originated the technique and the term "fuzz."
- [[fuzzingbook-03-fuzzer|Ch 3]] — frames the entire chapter around his experiment.
- [[RandomTesting]] — his fuzz generator was random string generation applied to real programs.
- [[BufferOverflow]] — among the bug classes his experiment exposed (along with missing error checks and rogue numbers).
- [[AndreasZeller]] — *The Fuzzing Book* author who recounts and builds on Miller's work.

## Sources
- [[fuzzingbook-03-fuzzer]] — *The Fuzzing Book* Ch 3, "Fuzzing: Breaking Things with Random Inputs."
