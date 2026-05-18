---
title: "Massif"
type: concept
tags: [valgrind, profiling, tooling, memory, heap]
sources: [dis-12-3-memory-considerations]
last_updated: 2026-05-17
---

# Massif

A **[[Valgrind]] sub-tool** that **profiles heap memory usage over the lifetime of a program** — peak allocation, per-function allocation breakdown, allocation timeline. [[DiveIntoSystems]] Ch 12.3 introduces Massif as the **memory-side counterpart** to [[Callgrind]] (instruction profiling) and [[Cachegrind]] (cache profiling), completing the [[DiveIntoSystems]] [[Valgrind]] optimization triad.

## Usage

```bash
$ valgrind --tool=massif ./prog
$ ms_print massif.out.<pid>
```

Massif samples heap allocations at strategic points (function entry, allocation calls) and produces a textual time-series report decoded by `ms_print` — peak usage, per-snapshot allocation tree, top allocator functions.

## What it measures

- **Total heap allocation over time** — `malloc`, `calloc`, `realloc`, custom allocators.
- **Peak heap usage** — and at which point in execution it occurred.
- **Per-function allocation breakdown** — which call site is responsible for which fraction of heap pressure.
- **Optional stack profiling** — `--stacks=yes` adds stack-frame measurement.

## Worked example

In [[dis-12-3-memory-considerations|Ch 12.3]]'s matrix-vector benchmark, Massif revealed **800 MB total heap allocation** with **99.96% occurring in a single allocation function** — diagnostically perfect: the program's memory profile is essentially one fat allocation, and any size-reduction effort should target it.

## Use cases

- **Memory leak diagnosis** — unmatched `malloc`/`free` shows up as a continuously rising allocation curve.
- **Peak-usage tuning** — bring down peak heap size to fit constrained environments.
- **Allocation-hot-spot finding** — `malloc` itself is expensive; reducing the number of allocations (via pooling, slab allocators, stack allocation) is a [[HotSpot|hot-spot]] optimization.

## Place in the Valgrind family

| Tool | Dimension profiled | Chapter |
|---|---|---|
| [[Memcheck]] | Memory errors / leaks | [[dis-3-3-valgrind]] |
| [[Callgrind]] | Instruction count per function | [[dis-12-1-first-steps]] |
| [[Cachegrind]] | Cache hits / misses | [[dis-11-5-cachegrind]] |
| **Massif** | **Heap allocation over time** | **[[dis-12-3-memory-considerations]]** |

## Connections

- [[Valgrind]] — parent suite.
- [[Profiling]] — the methodology Massif serves.
- [[Callgrind]] / [[Cachegrind]] / [[Memcheck]] — sibling Valgrind tools.
- [[HotSpot]] — what Massif output identifies (allocation hot spots).
- [[dis-12-3-memory-considerations]] — canonical [[DiveIntoSystems]] source.
