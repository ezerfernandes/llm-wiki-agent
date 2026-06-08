---
title: "Fuzzing at Scale (Fuzzing in the Large)"
type: concept
tags: [fuzzing, testing, security, infrastructure, scalability, software-engineering]
sources: [fuzzingbook-29-fuzzing-in-the-large]
last_updated: 2026-06-06
---

# Fuzzing at Scale (Fuzzing in the Large)

**Fuzzing at scale** — "fuzzing in the large" — is the management discipline of running [[Fuzzing|fuzzing]] not as one fuzzer on one machine for a few seconds, but as *multiple* fuzzers on *multiple* machines testing *multiple* programs (and versions), continuously, for hours to weeks, with the resulting failures handled by *multiple* people. At this scale the bottleneck shifts from *generating* inputs to *coordinating* runs and *routing* the flood of resulting failures to the right developers. The standard solution is a central **crash server** with a **crash database** that every fuzzer reports to over the network, which can be queried (usually via a Web UI) and integrated with the project's bug tracker so crashes can be assigned to engineers.

## From The Fuzzing Book — Fuzzing in the Large
[[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] mints this concept as the opening of **Part VI (Managing Fuzzing)**. It enumerates the data a crash database must store — the product **identifier** (name, version, platform, OS), **steps to reproduce** (the input), the **stack trace**, and a **coverage** map — and notes that in industry such databases routinely collect *thousands* of crashes, including from production (minus user inputs, for privacy). Two scale problems follow directly: thousands of duplicate crashes from one bug (solved by [[CrashDeduplication|crash bucketing]]) and the question of where each fuzzer gets stuck (solved by central per-fuzzer [[Coverage|coverage]] collection). The chapter demonstrates the whole pipeline with Mozilla's [[FuzzManager]] toolchain authored by co-author [[ChristianHoller|Christian Holler]]. It is the management counterpart to the *statistical* scale question of [[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]] (when to stop). Industrial realizations of the same pattern include Google's OSS-Fuzz/ClusterFuzz and Microsoft's Project Springfield/OneFuzz, though the chapter itself focuses on FuzzManager.

## Connections
- [[Fuzzing]] — the activity being scaled out across machines and programs.
- [[CrashDeduplication]] — the bucketing/signature technique that keeps the crash flood manageable.
- [[CrashTriage]] — routing distinct bugs to developers once duplicates are collapsed.
- [[ContinuousFuzzing]] — the always-on infrastructure dimension of fuzzing at scale.
- [[FuzzManager]] — the chapter's demonstrated crash-management platform.
- [[Coverage]] — per-fuzzer coverage collection to find where fuzzers stall.
- [[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] — the chapter that mints this concept.
- [[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]] — the companion management chapter (when enough fuzzing is enough).

## Sources
- [[fuzzingbook-29-fuzzing-in-the-large]] — *The Fuzzing Book* Ch 29, "Fuzzing in the Large."
