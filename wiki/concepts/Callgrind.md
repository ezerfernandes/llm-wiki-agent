---
title: "Callgrind"
type: concept
tags: [valgrind, profiling, tooling, performance]
sources: [dis-12-1-first-steps]
last_updated: 2026-05-17
---

# Callgrind

A **[[Valgrind]] sub-tool** that profiles a program by **counting instruction executions per function** and recording the **call graph** — which function called which, how many times. [[DiveIntoSystems]] Ch 12.1 introduces Callgrind as the canonical [[HotSpot|hot-spot]]-finding instrument: *"Callgrind enables analysis of instruction-count breakdowns per function"*.

## Usage

```bash
$ valgrind --tool=callgrind ./prog
$ callgrind_annotate callgrind.out.<pid>
```

The first command runs the program under Callgrind's instrumented simulator; the second decodes the binary `callgrind.out.<pid>` trace into a human-readable per-function and per-source-line annotation.

## What it measures

- **Total instructions per function** — the headline metric.
- **Call frequency** — how many times each function was invoked.
- **Caller-callee relationships** — the dynamic call graph.
- **Per-source-line costs** — via `callgrind_annotate --auto=yes`.

Unlike sampling profilers (`perf`, `gprof`) which estimate via periodic interrupts, Callgrind **simulates every instruction** — slow but deterministic, with no statistical noise.

## Worked example

In [[dis-12-1-first-steps|Ch 12.1]]'s `isPrime` benchmark (5,000,000 primes), Callgrind revealed `sqrt` executing **2,700,000 times = 20.5% of total instructions**. After lifting `sqrt(x)+1` out of the loop (loop-invariant code motion), Callgrind confirmed only **100,001 calls** (96% reduction) and runtime dropped 47%.

## Trade-offs

- **Slow** — Callgrind-instrumented runs are typically 20–100× slower than native execution.
- **Deterministic** — same input produces same counts; ideal for A/B optimization comparisons.
- **No wall-clock data** — Callgrind counts instructions, not seconds; runtime improvements must be confirmed with [[Benchmarking|wall-clock benchmarks]].

## Place in the Valgrind family

| Tool | Dimension profiled | Chapter |
|---|---|---|
| [[Memcheck]] | Memory errors / leaks | [[dis-3-3-valgrind]] |
| **Callgrind** | **Instruction count per function** | **[[dis-12-1-first-steps]]** |
| [[Cachegrind]] | Cache hits / misses | [[dis-11-5-cachegrind]] |
| [[Massif]] | Heap allocation over time | [[dis-12-3-memory-considerations]] |

## Connections

- [[Valgrind]] — parent suite.
- [[Profiling]] — the methodology Callgrind serves.
- [[HotSpot]] — what Callgrind output identifies.
- [[Cachegrind]] / [[Massif]] / [[Memcheck]] — sibling Valgrind tools.
- [[Benchmarking]] — the wall-clock companion that validates Callgrind-guided changes.
- [[dis-12-1-first-steps]] — canonical [[DiveIntoSystems]] source.
