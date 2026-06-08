---
title: "The Fuzzing Book Ch 29 — Fuzzing in the Large"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, crash-management, deduplication, triage, infrastructure, coverage]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-29-fuzzing-in-the-large.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Fuzzing in the Large

## Summary
Chapter 29 opens **Part VI (Managing Fuzzing)** by pivoting from the single-machine, single-program, few-seconds fuzzing of every prior chapter to fuzzing at **industrial scale** — dozens to thousands of machines, many programs and versions, running for hours, days, and weeks, producing a flood of failures that must be handled by many people. The central technique is an **infrastructure** for collecting failure data from individual fuzzer runs and aggregating it in a central repository, demonstrated through Mozilla's **[[FuzzManager]]** framework (authored by co-author [[ChristianHoller|Christian Holler]]). The worked examples submit crashes from trivial buggy C++ programs (`simple-crash`, `out-of-bounds`, `maze` from the `simply-buggy` repo) to a local FuzzManager server via a `Collector`, then group near-identical crashes into **[[CrashDeduplication|crash buckets]]** defined by **crash signatures** matching the program counter and stack-trace frames. It closes by collecting **per-fuzzer code coverage** (via Mozilla's `grcov`) to reveal where a fuzzer gets stuck. Builds on [[fuzzingbook-03-fuzzer|Ch 3]] (how fuzzers fork) and [[fuzzingbook-04-coverage|Ch 4]] (coverage); leads to [[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]] (when enough is enough).

## Key Concepts
- **[[FuzzingAtScale|Fuzzing in the large]]** — the management problem of running *multiple* fuzzers on *multiple* machines against *multiple* programs/versions, producing *multiple* failures handled by *multiple* people. Requires a central [[ContinuousFuzzing|crash server]] and database, ideally linked to a bug tracker.
- **Crash server + crash database** — whenever a fuzzer detects a failure it connects over the network to a crash server, which stores the crash in a database that can be queried (typically via a Web UI) and integrated with the bug database so bugs can be assigned to developers. Stored data includes the product **identifier** (name, version, platform, OS), **steps to reproduce** (the fuzzing *input*), the **stack trace**, and a **coverage** map.
- **[[FuzzManager]]** — Mozilla's modular, process-agnostic toolchain: a *server* that collects crash data plus *collector utilities* that send crash data to it. Key Python classes the chapter uses: `ProgramConfiguration` (container for product/platform/version/runtime options, read from a `.fuzzmanagerconf` file via `ProgramConfiguration.fromBinary()`), `CrashInfo` (stdout/stderr/GDB-or-ASan crash data + a `ProgramConfiguration`, built with `CrashInfo.fromRawCrashData()`), and `Collector` (client that `submit()`s crashes and downloads/matches existing signatures).
- **[[CrashDeduplication|Crash buckets & signatures]]** — because the *same* crash recurs thousands of times, FuzzManager groups *similar* failures into a **bucket** defined by a **crash signature**: a list of predicates (symptoms) over the **program counter**, **stack-trace frames** (`functionNames`), output text, and **crash address**. Buckets can be linked to an external bug tracker (e.g. Bugzilla).
- **Coarse-grained signatures & `Optimize`** — an initially fine-grained signature can be generalized to capture *variations* of one bug: lower stack frames that vary across crashes are relaxed to wildcards (`"?"`) while the function where the bug actually lives (`validateAndPerformAction`) is kept. The semi-automated `Optimize` button broadens a signature to fit untriaged crashes, then checks it does not collide with other buckets — requiring human review.
- **[[CrashTriage|Triage]]** — submission + bucketing *is* the automated front end of triage: collapsing thousands of raw crashes into a few unique signatures so developers see distinct bugs, not duplicates. A precise crash signature also auto-matches *future* occurrences.
- **Per-fuzzer [[Coverage|code coverage]] collection** — programs are rebuilt with `--coverage` (Clang/GCC); Mozilla's `grcov` captures coverage, `CovReporter` submits it, and FuzzManager's covmanager visualizes line-by-line hit counts (green = executed with a count, red = unexecuted), exposing where a fuzzer is stuck (e.g. a missed magic constant in `maze.cpp`).

## Key Claims
- Real-world fuzzing is *multiple fuzzers × multiple machines × multiple programs × multiple people*; the binding problem is coordinating them and routing failures, not generating inputs.
- A central crash repository is the standard coordination mechanism; in industry, crash databases routinely collect *thousands* of crashes, including from production runs (though user inputs are not collected from production for privacy reasons).
- The most useful bug-report data for developers are, in order: the product identifier, the steps to reproduce (the input), and the stack trace; coverage maps additionally help.
- Crash **deduplication via bucketing** is essential: a single bug in a product used by millions yields thousands of identical crashes that must collapse to one entry.
- A crash signature in FuzzManager is a set of symptom predicates over program counter, stack frames, output, and crash address; the bug typically lives in the stack frame common to *all* crashes in the bucket, while varying frames are generalized to `"?"`.
- Fully automatic deduplication cannot be guaranteed correct — `Optimize` can over-merge distinct bugs when bucket data is sparse — so the workflow is *semi-automated* with mandatory human review.
- Centrally collected per-fuzzer coverage reveals where fuzzers get stuck (uncovered branches, rarely-taken paths), guiding fuzzer improvement; sudden coverage drops at a branch quantify how rarely a fuzzer satisfies a condition.

## Key Quotes
> "In the real world, however, fuzzers are run on dozens or even thousands of machines; for hours, days and weeks; for one program or dozens of programs." — the scale that motivates the chapter's infrastructure.

> "If a product is in the hands of millions of users, chances are that thousands of them will encounter the same bug, and thus the same crash ... it is necessary to identify those failures that are _similar_ and to group them together in a set called a _crash bucket_." — the case for crash deduplication.

> "Buckets and their signatures are a central concept in FuzzManager. If you receive a lot of crash reports from various sources, bucketing allows you to easily group crashes and filter duplicates." — the core abstraction.

## Connections
- [[FuzzingAtScale]] — the chapter mints this management-layer concept (fuzzing in the large).
- [[CrashDeduplication]] — bucketing crashes by signature (stack-trace/program-counter predicates) to filter duplicates; the chapter's central technique.
- [[CrashTriage]] — automated/semi-automated routing of the crash flood to distinct, assignable bugs.
- [[ContinuousFuzzing]] — the always-on, distributed crash-server infrastructure this chapter is the management layer for.
- [[FuzzManager]] — Mozilla's crash-management toolchain demonstrated throughout (`ProgramConfiguration`, `CrashInfo`, `Collector`, covmanager).
- [[Mozilla]] — author org of FuzzManager and the `grcov`/`CovReporter` coverage tooling.
- [[ChristianHoller]] — co-author of *The Fuzzing Book* and the author of FuzzManager.
- [[Coverage]] — per-fuzzer code-coverage collection/visualization reuses the Ch 4 coverage idea to debug *fuzzers*.
- [[AddressSanitizer]] — crashes are detected and parsed from ASan traces before submission.
- [[InputReduction]] / [[DeltaDebugging]] — triage typically reduces a crashing input before filing; the reduced input is the "steps to reproduce" a crash entry stores.
- [[Selenium]] — used to drive the FuzzManager Web UI programmatically in the notebook.
- [[AFL]] — the kind of coverage-guided fuzzer whose mass output a FuzzManager-style server collects.
- [[MarcelBohme]] / [[AndreasZeller]] — co-authors of the book.
- [[fuzzingbook-03-fuzzer|Ch 3]] — prerequisite (how fuzzers fork/run).
- [[fuzzingbook-04-coverage|Ch 4]] — prerequisite for the coverage-collection section.
- [[fuzzingbook-16-reducer|Ch 16]] — input reduction, the natural triage companion to crash collection.
- [[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]] — the next management chapter: estimating remaining bugs and when to stop.

## Contradictions
- None identified.
