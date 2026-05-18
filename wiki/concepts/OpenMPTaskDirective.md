---
title: "OpenMP task Directive"
type: concept
tags: [openmp, parallel-computing, pragma, recursion, task-queue]
sources: [parproc-ch04-introduction-to-openmp]
last_updated: 2026-05-17
---

# OpenMP task Directive

`#pragma omp task` ([[OpenMP]] §4.5) sets up a **task queue**. When any thread of the team encounters the directive, it arranges for *some* thread (not necessarily itself) to execute the associated block — *"at some time"*. The encountering thread can then continue immediately. Multiple tasks may pile up if all threads are busy.

```c
#pragma omp parallel
{
    if (firstcall == 1) {
        #pragma omp single nowait
        qs(z, 0, zend, 0);          // recursive root, one thread enters
    } else {
        if (zstart < zend) {
            part = separate(z, zstart, zend);
            #pragma omp task
            qs(z, zstart, part-1, 0);   // left subtree
            #pragma omp task
            qs(z, part+1, zend, 0);     // right subtree
        }
    }
}
```

## What `task` solves

Without `task`, parallelizing a recursive algorithm requires hand-rolling a shared work-queue plus atomic enqueue/dequeue logic plus careful thread-pool coordination. [[parproc-ch04-introduction-to-openmp]] §4.5: *"All this would amount to a lot of coding on our part, so `task` really simplifies the programming."*

The pattern complements [[ParallelFor|`#pragma omp for`]]: `for` distributes loop iterations (known statically); `task` distributes asynchronous units of work (often produced dynamically as recursion descends a tree, or as a parser tokenizes input).

## Idioms

- **Recursive root via `single nowait`** ([[Quicksort]] §4.5.1) — exactly one thread enters the topmost call; subsequent `omp task` spawns let the rest of the team grab work.
- **`#pragma omp taskwait`** — barrier-like; waits for all *direct child* tasks spawned by the current task before continuing.

## Connections
- [[OpenMP]] — parent.
- [[parproc-ch04-introduction-to-openmp]] — §4.5 source.
- [[WorkSharing]] — `task` is a non-loop work-sharing mechanism.
- [[OpenMPSingle]] — `single nowait` is the canonical entry to a `task`-based recursion.
- [[Quicksort]] — §4.5.1 example.
- [[ParallelFor]] — sibling work-sharing construct for loop iterations.
- [[WorkStealing]] — the runtime mechanism underlying most `task` implementations.
