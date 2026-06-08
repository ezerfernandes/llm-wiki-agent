---
title: "Crash Deduplication (Bucketing & Crash Signatures)"
type: concept
tags: [fuzzing, testing, security, deduplication, triage, crash-management]
sources: [fuzzingbook-29-fuzzing-in-the-large]
last_updated: 2026-06-06
---

# Crash Deduplication (Bucketing & Crash Signatures)

**Crash deduplication** is the practice of recognizing that many distinct crash reports are caused by the *same* underlying bug and collapsing them into one group. When a product runs on many machines (or in the hands of millions of users), a single bug produces thousands of near-identical crashes; without deduplication the crash database is unusable. Deduplication groups *similar* failures into a **crash bucket**, defined by a **crash signature** — a set of predicates ("symptoms") that match a crash. The most discriminating features are the **program counter** (the instruction executing at the crash) and the **stack-trace frames** (which functions were active), often supplemented by output text and the **crash address**. A good signature both de-duplicates past crashes and *auto-matches future* occurrences of the same bug.

## From The Fuzzing Book — Fuzzing in the Large
[[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] mints this concept as the central abstraction of [[FuzzManager]]. A FuzzManager **bucket** is defined by a crash signature expressed as a JSON list of `symptoms` (e.g. an `output` regex over stderr, a `stackFrames` predicate with `functionNames`, and a `crashAddress` predicate). The chapter's `out-of-bounds.cpp` example shows why one bug yields *several* signatures: the missing bounds check lives in `validateAndPerformAction()`, but the illegal access happens deeper in either `printFirst()` or `printLast()`, producing slightly different stacks. The fix is **coarse-grained signatures**: keep the common frame (`validateAndPerformAction`, where the bug lives) and generalize the varying lower frames to wildcards (`"?"`). FuzzManager's semi-automatic `Optimize` function broadens a signature to absorb untriaged crashes and checks for collisions with other buckets — but because it can over-merge distinct bugs when data is sparse, the process requires human review. Buckets can be linked to an external bug tracker (e.g. Bugzilla). This is the de-duplication step that turns the raw crash flood into a few assignable bugs, and the [[CrashTriage|triage]] front end of [[FuzzingAtScale|fuzzing at scale]].

## Connections
- [[FuzzManager]] — implements buckets and crash signatures (JSON `symptoms`, `Optimize`).
- [[CrashTriage]] — deduplication is the first step of triaging the crash flood.
- [[FuzzingAtScale]] — the scale problem (thousands of duplicate crashes) that makes deduplication necessary.
- [[ContinuousFuzzing]] — the always-on pipeline whose output must be deduplicated.
- [[InputReduction]] / [[DeltaDebugging]] — reduced crashing inputs make signatures cleaner and help confirm two crashes share a cause.
- [[AddressSanitizer]] — ASan output (e.g. `heap-buffer-overflow`) is a common signature symptom.
- [[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] — the chapter that mints this concept.

## Sources
- [[fuzzingbook-29-fuzzing-in-the-large]] — *The Fuzzing Book* Ch 29, "Fuzzing in the Large."
