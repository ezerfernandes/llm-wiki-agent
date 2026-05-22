---
title: "Dive into Systems — Ch 14.9 Exercises"
type: source
tags: [dive-into-systems, textbook, parallel-programming, exercises]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C14-SharedMemory/exercises.html
---

## Summary

**Closing leaf of Ch 14** *Leveraging Shared Memory in the Multicore Era* of *[[DiveIntoSystems]]* — exercise-set page that **fully closes Ch 14 and the [[DiveIntoSystems]] parallel-programming arc**. Drills three thematic areas:

1. **Threading fundamentals** — implementation and performance analysis of [[Pthreads|Pthread]]-based scalar multiplication across varying thread counts and dataset sizes (operationalizing [[dis-14-1-multicore|14.1's]] 1/c [[ParallelSpeedup|speedup]] approximation against real measurements).
2. **[[Synchronization]]** — parallel implementation of the **CountSort** algorithm ([[dis-14-3-synchronization|14.3's]] motivating example) with timing analysis and multi-stage [[Pthreads]] operations using [[Mutex|mutexes]] and [[Barrier|barriers]].
3. **[[OpenMP]]** — practical considerations for thread management and function design flexibility under the implicit-threading regime from [[dis-14-7-openmp|14.7]].

## Connections

- [[DiveIntoSystems]] — parent textbook; **ninth and final leaf** of Ch 14, closing the chapter.
- [[dis-14-1-multicore]] / [[dis-14-2-posix]] / [[dis-14-3-synchronization]] / [[dis-14-7-openmp]] — the leaves the three exercise themes drill.
- [[Pthreads]] / [[Mutex]] / [[Barrier]] / [[OpenMP]] — the four APIs the exercises exercise.
- [[ParallelSpeedup]] / [[AmdahlsLaw]] — the performance theory the threading-fundamentals exercises put under measurement.
- Sibling exercise leaves: [[dis-1-8-exercises]] / [[dis-2-11-exercises]] / [[dis-4-10-exercises]] / [[dis-5-11-exercises]] / [[dis-7-11-x86-64-exercises]] / [[dis-8-11-ia32-exercises]] / [[dis-9-11-arm64-exercises]] / [[dis-11-8-exercises]] / [[dis-13-6-exercises]] — the **exercise-set closes chapter** structural pattern.

## Notes

- **140th ingested DIS chapter — closes Ch 14 *Leveraging Shared Memory in the Multicore Era* in full.** The [[DiveIntoSystems]] textbook ingest is now complete through the end of the parallel-programming arc. **No new concept pages.**
