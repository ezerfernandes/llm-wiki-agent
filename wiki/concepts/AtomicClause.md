---
title: "OpenMP atomic Clause"
type: concept
tags: [openmp, parallel-computing, pragma, atomic, hardware]
sources: [parproc-ch04-introduction-to-openmp, parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# OpenMP atomic Clause

`#pragma omp atomic` ([[OpenMP]] §4.6.1) declares a **single-statement** critical section that the compiler may lower to an atomic hardware instruction (e.g. Intel `LOCK` prefix; ARM LL/SC). Cheaper than `#pragma omp critical` for one-statement updates because it skips the runtime mutex setup.

```c
#pragma omp atomic
x += y;
```

No braces — the directive applies to the single statement that follows.

## Eligible operators

`++`, `--`, `+=`, `-=`, `*=`, `<<=`, `&=`, `|=` (plus their right-hand variants where applicable).

## Cost argument

[[parproc-ch04-introduction-to-openmp]]: *"The `critical` construct not only serializes your program, but also it adds a lot of overhead. If your critical section involves just a one-statement update to a shared variable… the OpenMP compiler can take advantage of an atomic hardware instruction."*

## Lowering example

The book demonstrates GCC's actual output for `#pragma omp atomic tot += mysum`:

```
movl    n(%rip), %eax
cmpl    %eax, -8(%rbp)
jl      .L22
movl    -12(%rbp), %eax
lock addl  %eax, tot(%rip)
call    GOMP_barrier
jmp     .L24
```

The `lock addl` is the entire atomic — one CPU instruction with the `LOCK` prefix asserted, replacing what `critical` would have lowered to (a mutex lock + add + mutex unlock).

## Relationship to hardware atomics

[[parproc-ch03-shared-memory-parallelism]] §3.4.1 already named Intel's `LOCK` prefix and [[TestAndSet]] as the indivisible primitives. `omp atomic` is the high-level surface to those — Matloff explicitly shows the bridge in the §4.6.1 assembly listing.

## Connections
- [[OpenMP]] — parent.
- [[parproc-ch04-introduction-to-openmp]] — §4.6.1 source.
- [[parproc-ch03-shared-memory-parallelism]] — §3.4 hardware-atomics substrate.
- [[CriticalSection]] — the heavier-weight alternative.
- [[ReductionClause]] — uses an atomic-style combine for the final per-thread merge.
- [[TestAndSet]] / [[FetchAndAdd]] — sibling hardware-atomic primitives.
- [[FalseSharing]] — an atomic still triggers cache-line ping-pong if the variable shares a line with hot data.
