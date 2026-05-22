---
title: "Dive into Systems — Ch 13.6 Exercises"
type: source
tags: [book-chapter, dive-into-systems, operating-systems, exercises]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C13-OS/exercises.html
---

## Summary

**Ch 13.6 *Exercises*** is the **closing leaf** of Ch 13 *The Operating System* of *[[DiveIntoSystems]]* — the standard exercise-set page that fully closes the chapter. It drills two of Ch 13's three foundational areas: **[[Process|process]] hierarchy + [[Fork|`fork()`]] semantics** (Ch 13.2) and **[[VirtualMemory|virtual memory]]** (Ch 13.3). The Ch 13.2 exercise is rendered inline — a multi-`fork` code-trace problem asking the student to (1) diagram the resulting parent-child process tree across three nested `fork()` calls and (2) enumerate the per-process output sequences. The Ch 13.3 [[VirtualMemory|virtual-memory]] exercises are externalized to the book's *Early Access Interactive Virtual Memory Questions* interactive platform — same hosting pattern as [[dis-11-8-exercises|Ch 11.8]] / [[dis-4-10-exercises|Ch 4.10]] etc. **No new concept pages** — pure problem-set redirect.

## Key Claims

- Three nested [[Fork|`fork()`]] calls produce a **non-trivial process tree** — the canonical Ch 13.2 drill, exercising the *"`fork` returns twice — `0` to child, child [[ProcessID|PID]] to parent"* rule from [[dis-13-2-processes|Ch 13.2]].
- Per-process **output interleaving** is undefined across processes — the solution traces *deterministic per-process output orderings* (e.g., parent prints `A, E, F, G`) while leaving cross-process order to the [[Scheduler|scheduler]].
- **Virtual-memory exercises are deferred to the interactive platform** — same convention as [[dis-3-1-gdb|Ch 3.1]] / [[dis-11-5-cachegrind|Ch 11.5]] for hands-on drills.

## Key Quotes

> *(exercise framing)* "Diagram the resulting process hierarchy ... trace the output sequences for each process" — the canonical [[Fork|`fork()`]] tree-trace drill from [[dis-13-2-processes|Ch 13.2]].

## Connections

- [[DiveIntoSystems]] — **closing leaf of Ch 13** — pairs with [[dis-13-5-summary-advanced|Ch 13.5 *Summary and Other OS Functionality*]] (prose recap) as the standard *summary + exercises* pair, the same pattern that closed Ch 1 ([[dis-1-7-summary]] + [[dis-1-8-exercises]]), Ch 4, Ch 5, Ch 7, Ch 8, Ch 9, Ch 11 etc.
- [[dis-13-2-processes]] — the chapter the inline [[Fork|`fork()`]]-tree exercise drills.
- [[dis-13-3-virtual-memory]] — the chapter the externalized interactive exercises drill.
- [[Fork]] / [[ProcessID]] / [[Process]] / [[Scheduler]] — the concepts the inline exercise exercises.
- [[dis-1-8-exercises]] / [[dis-2-11-exercises]] / [[dis-4-10-exercises]] / [[dis-5-11-exercises]] / [[dis-7-11-x86-64-exercises]] / [[dis-8-11-ia32-exercises]] / [[dis-9-11-arm64-exercises]] / [[dis-11-8-exercises]] — structural siblings (the **exercise-set closes chapter** pattern).

## Contradictions

None — exercise set, no new claims.
