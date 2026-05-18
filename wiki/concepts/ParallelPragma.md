---
title: "OpenMP parallel Pragma"
type: concept
tags: [openmp, parallel-computing, pragma, threading]
sources: [parproc-ch04-introduction-to-openmp]
last_updated: 2026-05-17
---

# OpenMP parallel Pragma

`#pragma omp parallel` is the **only** [[OpenMP]] directive that creates a thread team. Every other OpenMP construct (`for`, `single`, `sections`, `critical`, `barrier`, `atomic`, `task`, `flush`) operates within an *existing* team — it has no effect outside an enclosing `parallel` block (or the combined `parallel for` / `parallel sections` form).

```c
#pragma omp parallel
{
    int startv, endv, me = omp_get_thread_num();
    // every thread in the team runs this block
}
```

## Scope rule

[[parproc-ch04-introduction-to-openmp]] §4.2.3 codifies the variable-sharing convention:
- Variables declared **before** `#pragma omp parallel` (within the same function): **shared** across the team.
- Variables declared **inside** the block: **thread-local**.
- Global (C/C++ sense) variables: **always shared** — *"the primary means by which the threads communicate with each other."*

Overrides via clauses:
- `private(x, y)` — make pre-declared variables thread-local.
- `firstprivate(x)` — like `private`, but initialize each thread's copy from the surrounding shared value.

## Implicit barrier

Like `single` / `for` / `sections`, `parallel` has an **implicit barrier at the exit** — all threads in the team wait at `}` before the master continues.

## Thread startup cost

Per [[parproc-ch04-introduction-to-openmp]] §4.2.2 footnote 1: with the OMPi compiler, threads are created once at program startup; the `parallel` directive **awakens** them and the closing `}` **suspends** them. So each `parallel` boundary is light, not a `pthread_create` cost.

## Combined forms

- `#pragma omp parallel for` ≡ `parallel` + `for`.
- `#pragma omp parallel sections` ≡ `parallel` + `sections`.

## Connections
- [[OpenMP]] — parent.
- [[parproc-ch04-introduction-to-openmp]] — §4.2.2 / §4.2.3 source.
- [[WorkSharing]] — work-distribution constructs operate within `parallel`.
- [[Barrier]] — implicit at block exit.
- [[OpenMPSingle]] — limit a `parallel`-internal section to one thread.
- [[ParallelFor]] — typical inner directive.
