---
title: "Memory Allocation"
type: concept
tags: [systems, performance, memory]
sources: [parproc-ch02-recurring-performance-issues, parproc-appA-systems-issues]
last_updated: 2026-05-17
---

# Memory Allocation

The act of obtaining storage for data. In a typical C/C++ program this means **static allocation** (compile-time-sized arrays in `.bss` / `.data`), **stack allocation** (function-local variables), or **dynamic allocation** via `malloc()` / C++'s `new` (which itself usually calls `malloc` underneath).

## In the chapter

[[parproc-ch02-recurring-performance-issues]] §2.7 flags memory allocation as one of the recurring performance issues — short section, three pragmatic points:

1. **Dynamic allocation is expensive in time.** `malloc()` / `new` traverse free-list / arena bookkeeping data structures; large allocations on first-touch trigger page-table updates and cache misses. *"Very expensive in time."*
2. **Large allocations are expensive in space-effects.** Even after the allocation returns, working sets that exceed cache capacity generate cache misses, and working sets that exceed physical memory generate page faults.
3. **Use static arrays where possible** to dodge `malloc()` entirely. When you can't, *"tweak one's code accordingly, say by adjusting calls to `malloc()` so that one achieves a balance between allocating too much memory and making too many calls."*

This is the smallest of [[parproc-ch02-recurring-performance-issues|Ch2's]] recurring issues — Matloff explicitly says *"there are no magic solutions here. One must simply be aware of the problem"* — but he places it in the chapter alongside [[CommunicationBottleneck|communication]] and [[LoadBalancing|load balancing]] to signal that systems-level concerns (not just algorithmic ones) drive parallel performance.

## Appendix A addendum (§A.3.3)

[[parproc-appA-systems-issues]] reinforces Ch2's advice with two practical tips:

- With an array whose size is known at compile time but declared local to a function, it will be stack-allocated; on large arrays this may exhaust stack space. The easiest fix is to make the array global (fixed size), avoiding both `malloc()` overhead and stack overflow.
- On a 64-bit system using `gcc`, use the **`-mcmodel=medium`** compiler flag to accommodate large global arrays that exceed the default small-model 2 GB limit.

## Connections

- [[parproc-ch02-recurring-performance-issues]] — primary source, §2.7.
- [[parproc-appA-systems-issues]] — §A.3.3; reinforces Ch2 advice with `gcc -mcmodel=medium` tip.
- [[CommunicationBottleneck]] — companion recurring issue.
- [[LoadBalancing]] — companion recurring issue.
- [[CoherentCaches]] — cache misses from large allocations show up here.
- [[VirtualMemory]] — first-touch of newly allocated pages triggers page-table updates and potential page faults.
