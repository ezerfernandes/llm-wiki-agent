---
title: "OpenMP single Pragma"
type: concept
tags: [openmp, parallel-computing, pragma]
sources: [parproc-ch04-introduction-to-openmp]
last_updated: 2026-05-17
---

# OpenMP single Pragma

`#pragma omp single` (an [[OpenMP]] [[WorkSharing|work-sharing construct]]) marks a block to be executed by **exactly one** thread of the surrounding team. The remaining threads skip the block and wait at an **implicit barrier** at the closing `}`. The `nowait` clause removes that barrier — but use sparingly.

```c
#pragma omp parallel
{
    #pragma omp single
    {
        nth = omp_get_num_threads();
        chunk = nv / nth;
        printf("there are %d threads\n", nth);
    }
    // every thread sees nth and chunk here
    // ...
}
```

## Typical uses

- **One-shot setup**: initialize a shared variable that the team will read ([[parproc-ch04-introduction-to-openmp]] §4.2.4 — the Dijkstra example uses `single` to compute `nth` and `chunk`).
- **Recursive root**: in [[Quicksort]] with [[OpenMPTaskDirective|`omp task`]], `omp single nowait` ensures exactly one thread enters the recursive root call (§4.5.1).
- **Sequential phase inside a parallel block**: a `single` block sandwiched between two parallel phases (e.g. §4.10.2 Dijkstra fine-tuning reduces `mymins[]` in `single` after a barrier).

## Connections
- [[OpenMP]] — parent.
- [[parproc-ch04-introduction-to-openmp]] — §4.2.4 source.
- [[WorkSharing]] — `single` is one of the four work-sharing constructs.
- [[Barrier]] — implicit at the closing `}`.
- [[OpenMPTaskDirective]] — `single nowait` is the canonical entry for task-based recursion.
- [[Quicksort]] — §4.5.1 example.
