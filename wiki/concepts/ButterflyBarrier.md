---
title: "Butterfly Barrier"
type: concept
tags: [parallel-computing, synchronization, concurrency, shared-memory]
sources: [parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# Butterfly Barrier

A parallelized [[Barrier]] implementation in which each node *"shakes hands"* with every other node in $\log_2 n$ phases, using a **bit-flipping partner schedule**. ([[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.12.4.2.2).

## Partner schedule

For `n = 2^k` nodes (numbered 0 to `n − 1` in binary), and for each phase `k = 0, 1, …, log₂n − 1`:

Node `i` shakes hands with node `i ⊕ 2^k` — i.e. with the node whose binary representation differs from `i`'s in bit `k`.

Worked example for `n = 8`:
- **Phase 0**: node 5 = 101₂ shakes with node 4 = 100₂ (flip bit 0).
- **Phase 1**: node 5 = 101₂ shakes with node 7 = 111₂ (flip bit 1).
- **Phase 2**: node 5 = 101₂ shakes with node 1 = 001₂ (flip bit 2).

After `log₂n` phases, every node has indirectly communicated with every other.

## Implementation (shared-memory)

A global array `ReachedBarrier[n]`:

```c
// Phase k between nodes i and j = i XOR (1 << k):
ReachedBarrier[i] = 1;
while (ReachedBarrier[j] == 0) ;   // or pthread_cond_wait
// then continue to phase k+1
```

The wait is a busy loop or — better — `pthread_cond_wait`.

## Why it works

*"Actually, a butterfly exchange amounts to a number of simultaneously tree operations."* The partner pairings in phase `k` partition the nodes into `n/2` disjoint pairs; these pairs synchronize *simultaneously and independently*. Across `log₂n` phases, every information bit reaches every node.

## Comparison to tree barrier

- **[[TreeBarrier|Tree barrier]]**: $\log_2 n$ levels of nested sub-barriers, asymmetric (designated representatives propagate up then back down).
- **Butterfly barrier**: $\log_2 n$ phases of fully-symmetric pairwise handshakes, every node participates in every phase.

Both achieve $O(\log n)$ critical-path latency; butterfly has the symmetry advantage but slightly more total handshake work.

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.12.4.2.2.
- [[Barrier]] — the parent synchronization primitive.
- [[TreeBarrier]] — sibling parallelization scheme.
- [[Pthreads]] — substrate.
- [[CriticalSection]] — what butterflies fan out.
- [[SharedMemoryArchitecture]] — context.
