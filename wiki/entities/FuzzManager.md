---
title: "FuzzManager"
type: entity
tags: [tool, fuzzing, security, crash-management, deduplication, coverage, mozilla, open-source]
sources: [fuzzingbook-29-fuzzing-in-the-large]
last_updated: 2026-06-06
---

# FuzzManager

**FuzzManager** is a modular, open-source toolchain from [[Mozilla]] for managing large-scale fuzzing processes, authored by *The Fuzzing Book* co-author [[ChristianHoller|Christian Holler]] (Mozilla Security). It is *modular* (use only the parts you need) and *versatile* (imposes no particular workflow). It consists of a **server** that collects crash data into a database and **collector utilities** that gather crash data from fuzzers and send it to the server. Its defining feature is **crash bucketing**: similar crashes are grouped by a **crash signature** so thousands of duplicate reports collapse into a few distinct, assignable bugs. It is hosted at `github.com/MozillaSecurity/FuzzManager`.

## Role in The Fuzzing Book
[[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] uses FuzzManager as its worked example of [[FuzzingAtScale|fuzzing in the large]]. The Python API the chapter exercises:
- **`ProgramConfiguration`** — container for product name, platform, version, and runtime options; `ProgramConfiguration.fromBinary()` reads them from a generated `.fuzzmanagerconf` file.
- **`CrashInfo`** — holds the crash's stdout/stderr and the GDB-or-[[AddressSanitizer|ASan]] crash data plus a `ProgramConfiguration`; built with `CrashInfo.fromRawCrashData(stdout, stderr, configuration)`.
- **`Collector`** — the client that talks to the CrashManager server; `collector.submit(crashInfo, testCase=...)` uploads a crash and can download/match existing signatures to avoid re-reporting known issues.
- **CrashManager Web UI** — lists crashes, lets you create a [[CrashDeduplication|bucket]] from a crash, and `Optimize` its signature (generalizing varying stack frames to `"?"` while keeping the buggy frame); buckets can be linked to a bug tracker (e.g. Bugzilla).
- **CovManager + `CovReporter`** — submits and visualizes per-fuzzer [[Coverage|code coverage]] (collected with Mozilla's `grcov`), showing line-by-line hit counts to reveal where a fuzzer is stuck.

The chapter notes FuzzManager is used at Mozilla for massive browser fuzzing (see "Browser Fuzzing at Mozilla").

## Connections
- [[Mozilla]] — the organization that develops FuzzManager and the `grcov` coverage tool.
- [[ChristianHoller]] — its author and a co-author of *The Fuzzing Book*.
- [[CrashDeduplication]] — its central feature: buckets defined by crash signatures.
- [[CrashTriage]] — its submit/bucket/optimize workflow is the triage front end.
- [[FuzzingAtScale]] / [[ContinuousFuzzing]] — the management problem it solves.
- [[Coverage]] — its CovManager visualizes per-fuzzer coverage.
- [[AddressSanitizer]] — the crash detector whose traces it parses into `CrashInfo`.
- [[Selenium]] — drives FuzzManager's Web UI programmatically in the chapter's notebook.
- [[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] — the chapter built on FuzzManager.

## Sources
- [[fuzzingbook-29-fuzzing-in-the-large]] — *The Fuzzing Book* Ch 29, "Fuzzing in the Large."
