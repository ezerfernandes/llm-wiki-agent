---
title: "Dijkstra Shortest-Path Algorithm"
type: concept
tags: [algorithm, graph, shortest-path, parallel-computing]
sources: [parproc-ch04-introduction-to-openmp]
last_updated: 2026-05-17
---

# Dijkstra Shortest-Path Algorithm

Classical single-source shortest-paths algorithm on a weighted graph with nonnegative edge weights. From source vertex 0, the algorithm maintains:
- `mind[i]` — best-known distance from 0 to vertex `i`.
- `notdone[i]` — 1 if `i` has not yet been finalized.

Each iteration picks the not-yet-finalized vertex `J` with the smallest `mind[J]`, finalizes it (`notdone[J] = 0`), then **relaxes** every other vertex `K`'s `mind[K]` through `J`:

```
for K = 1 to N-1
    if K is in NonDone
        mind[K] = min(mind[K], mind[J] + G[J][K])
```

[[parproc-ch04-introduction-to-openmp]] uses Dijkstra as **the worked example** throughout the chapter — every new pragma is demonstrated by modifying the same base implementation.

## Parallel structure

Per [[parproc-ch04-introduction-to-openmp]] §4.2.1: two loops are obvious parallelization candidates:
1. **Find `J`** — the inner search for the min-distance unfinalized vertex.
2. **For each `K`** — the relaxation pass.

The chapter's parallelization partitions vertices across threads:
- Each thread covers a contiguous chunk `[startv, endv]`.
- In step 1, each thread computes its **local** min `mymd, mymv` over its chunk via `findmymin()`, then a `#pragma omp critical` combines into the global `md, mv`.
- In step 2, each thread relaxes the distances *within its own chunk* through the just-finalized vertex.
- Two `#pragma omp barrier` synchronizations bracket the iteration.

## Variants in the chapter

§4.2.2–§4.2.7 — base parallel version with `parallel` + `single` + `for` loop + `critical` + `barrier`.

§4.3.1 — refactor with `#pragma omp for` instead of manual chunk indexing.

§4.3.3 — same code under `schedule(static)` / `schedule(guided)` to control chunking.

§4.10.1 — timing scaling table (problem size effect on speedup).

§4.10.2 — fine-tuning that **eliminates the critical section** by writing each thread's `mymd, mymv` to a shared `mymins[2*nth]` array and reducing in a post-barrier `#pragma omp single`. Yields ~15% speedup at 2 threads.

§4.10.3 — Omni `-t` output showing how `omp critical` lowers to `_ompc_enter_critical` / `_ompc_exit_critical` library calls.

## Connections
- [[parproc-ch04-introduction-to-openmp]] — primary source, used as a recurring example.
- [[OpenMP]] — every new pragma is demonstrated on this code.
- [[CriticalSection]] — the per-iteration `omp critical` that §4.10.2 eliminates.
- [[Barrier]] — two per iteration.
- [[ParallelPragma]], [[OpenMPSingle]], [[ParallelFor]], [[ScheduleClause]] — the constructs successively applied.
- [[LoadBalancing]] — `chunk = nv / nth` is the chapter's vertex-partition rule.
- [[FalseSharing]] — flagged in §4.10.2 as the next optimization target on `mymins[]`.
