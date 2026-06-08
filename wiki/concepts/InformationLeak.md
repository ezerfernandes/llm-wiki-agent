---
title: "Information Leak"
type: concept
tags: [security, fuzzing, memory-safety, information-flow, vulnerability]
sources: [fuzzingbook-03-fuzzer]
last_updated: 2026-06-06
---

# Information Leak

An **information leak** is the disclosure of data that should remain confidential — secret keys, credentials, or uninitialized memory contents — through a program's output. Crucially, leaks can occur **within valid memory bounds**: no out-of-bounds access is required, so a memory-safety tool like [[AddressSanitizer]] will not flag them. This makes information leaks a distinct, harder-to-detect bug class for [[Fuzzing|fuzzing]].

## From The Fuzzing Book — Fuzzing: Breaking Things with Random Inputs
[[fuzzingbook-03-fuzzer|Ch 3]] illustrates the leak class with a Python simulation of the [[Heartbleed]]-style heartbeat service. `secrets` is a memory buffer holding a reply slot, `<secret-certificate>`/`<secret-key>` markers, and `"deadbeef"` filler standing in for uninitialized memory. The `heartbeat(reply, length, memory)` function stores `reply` at the front of `memory` and returns the first `length` bytes. When the requested `length` exceeds the reply, the surplus bytes spill secret and uninitialized memory into the response — *while staying inside the array*, so ASan stays silent. The chapter's detection idea is a check that asserts the response contains neither the `uninitialized_memory_marker` nor any `"secret"` string, and it forwards the reader to [[fuzzingbook-19-information-flow|Ch 19]] for automatic detection via **taint tracking** ("tainting" sensitive values and ensuring tainted data never reaches output).

## Connections
- [[Heartbleed]] — the real-world OpenSSL over-read this simulation models.
- [[AddressSanitizer]] — catches out-of-bounds accesses but **not** in-bounds information leaks.
- [[BufferOverflow]] — the related, out-of-bounds memory-safety class (over-reads vs over-writes).
- [[Fuzzing]] / [[Runner]] — a checker-equipped runner turns a leak into an observable failure.
- [[fuzzingbook-19-information-flow|Ch 19]] — tracks information flow / taint to detect leaks automatically.
- [[fuzzingbook-03-fuzzer|Ch 3]] — introduces information leaks as a checker target.

## Sources
- [[fuzzingbook-03-fuzzer]] — *The Fuzzing Book* Ch 3, "Fuzzing: Breaking Things with Random Inputs."
