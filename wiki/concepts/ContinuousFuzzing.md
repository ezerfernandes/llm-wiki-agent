---
title: "Continuous Fuzzing"
type: concept
tags: [fuzzing, testing, security, infrastructure, ci-cd, crash-management]
sources: [fuzzingbook-29-fuzzing-in-the-large]
last_updated: 2026-06-06
---

# Continuous Fuzzing

**Continuous fuzzing** is the practice of running [[Fuzzing|fuzzers]] perpetually — across a fleet of machines, against many programs and every new revision — rather than as a one-off campaign. It is the infrastructure dimension of [[FuzzingAtScale|fuzzing at scale]]: fuzzers run as background workers that, on detecting a failure, report it over the network to a central **crash server** and **crash database**, which deduplicates, stores, and (ideally) files the result into a bug tracker. Because the fleet runs indefinitely, the same bug is rediscovered constantly, making [[CrashDeduplication|crash deduplication]] and [[CrashTriage|triage]] indispensable. Industrial continuous-fuzzing systems include Google's OSS-Fuzz/ClusterFuzz (fuzzing open-source projects continuously) and Microsoft's Project Springfield/OneFuzz; the management layer demonstrated in the book is Mozilla's [[FuzzManager]].

## From The Fuzzing Book — Fuzzing in the Large
[[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] frames continuous, distributed fuzzing as the real-world default: "in the real world ... fuzzers are run on dozens or even thousands of machines; for hours, days and weeks." It demonstrates the client/server split that makes this work — fuzzers anywhere (remote machines, beta testers, even production) use a [[FuzzManager]] `Collector` to push `CrashInfo` to a shared server — and shows the server-side dashboards for crashes, buckets, and coverage. Centrally aggregating *per-fuzzer* [[Coverage|coverage]] over the continuous run is what lets operators see where fuzzers stall and improve them, closing the loop. The chapter is the management bookend before [[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]], which asks how long such a continuous campaign should run.

## Connections
- [[FuzzingAtScale]] — continuous fuzzing is the always-on form of fuzzing in the large.
- [[FuzzManager]] — the crash server/collector infrastructure for continuous campaigns.
- [[CrashDeduplication]] / [[CrashTriage]] — required to manage the steady stream of recurring crashes.
- [[Coverage]] — continuously aggregated coverage reveals where fuzzers are stuck.
- [[Fuzzing]] / [[AFL]] — the fuzzers run continuously in the fleet.
- [[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] — the chapter that mints this concept.
- [[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]] — when to stop a continuous fuzzing campaign.

## Sources
- [[fuzzingbook-29-fuzzing-in-the-large]] — *The Fuzzing Book* Ch 29, "Fuzzing in the Large."
