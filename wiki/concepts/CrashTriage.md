---
title: "Crash Triage"
type: concept
tags: [fuzzing, testing, security, triage, debugging, crash-management]
sources: [fuzzingbook-29-fuzzing-in-the-large]
last_updated: 2026-06-06
---

# Crash Triage

**Crash triage** is the process of turning a raw stream of crashes from large-scale [[Fuzzing|fuzzing]] (and from production) into a small set of distinct, actionable, *assignable* bugs. It combines several steps: detecting that a run crashed (e.g. from an [[AddressSanitizer|ASan]] trace), capturing the reproduction data (input, stack trace, configuration), **de-duplicating** crashes via [[CrashDeduplication|bucketing/signatures]] so duplicates of one bug collapse to a single entry, optionally **reducing** the crashing input ([[InputReduction]] / [[DeltaDebugging]]) to ease debugging, and linking the resulting bucket to a bug tracker so a developer can be assigned. Triage is what makes [[FuzzingAtScale|fuzzing at scale]] tractable for humans: without it, the same bug appears thousands of times and developers cannot see which crashes are genuinely new.

## From The Fuzzing Book — Fuzzing in the Large
[[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] treats triage as the front end of crash management in [[FuzzManager]]. The notebook shows the automated capture half — running a binary from Python, detecting the ASan trace, building a `CrashInfo` from raw crash data, and `submit()`ting it via a `Collector` — and the human-in-the-loop half — creating buckets and refining [[CrashDeduplication|crash signatures]] (including the semi-automatic `Optimize` step) so the crash flood resolves into distinct bugs. The chapter stresses that fully automatic triage is not safe: signature optimization can over-merge different bugs, so a person must review proposed changes. It also folds in *coverage-based* triage of the fuzzer itself — central [[Coverage|coverage]] visualization reveals where a fuzzer is stuck and therefore why certain bugs are not being reached.

## Connections
- [[CrashDeduplication]] — the bucketing/signature step at the heart of triage.
- [[FuzzManager]] — the platform whose submit/bucket/optimize workflow implements triage.
- [[InputReduction]] / [[DeltaDebugging]] — minimizing a crashing input is a standard triage step.
- [[FuzzingAtScale]] — the scale that makes triage necessary.
- [[ContinuousFuzzing]] — supplies the continuous crash stream being triaged.
- [[AddressSanitizer]] — the detector that flags a crash worth triaging.
- [[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] — the chapter that mints this concept.

## Sources
- [[fuzzingbook-29-fuzzing-in-the-large]] — *The Fuzzing Book* Ch 29, "Fuzzing in the Large."
