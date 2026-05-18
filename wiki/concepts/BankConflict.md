---
title: "Bank Conflict"
type: concept
tags: [parallel-computing, hardware, memory, performance]
sources: [parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# Bank Conflict

When two or more processors (or warp lanes, on a [[GPU]]) issue simultaneous accesses to the **same memory module / bank**, the hardware serializes them. The cost is a multiplicative slowdown proportional to the number of colliding requests — the parallelism that motivated splitting memory into banks in the first place vanishes.

## Worked example ([[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.2.2)

16 threads sum an array `x[0..16_000_000]` over 4 low-order-interleaved banks. Naïve code assigns thread `thr` to the contiguous slice `x[thr*1000000 .. thr*1000000+999999]`. If `x` starts at a multiple of 4 (bank 0), thread 0's first access is `x[0]` in bank 0, thread 1's first access is `x[1000000]` also in bank 0, thread 2's first access is `x[2000000]` — *all sixteen threads hit bank 0 in lockstep*. *"these will all be in memory bank 0! Thus there will be major conflicts, hence major slowdown."*

The fix is to give each thread a stride-16 access pattern:

```c
parallel for thr = 0 to 15
   localsum = 0
   for j = 0 to 999999
      localsum += x[16*j+thr]
   grandsum += localsum
```

Consecutive threads now read consecutive elements, which under low-order [[MemoryInterleaving|interleaving]] sit in consecutive banks — *"no conflicts, hence speedy performance."*

## General mitigations

- **Rewrite the algorithm** to make consecutive thread IDs touch consecutive addresses (the stride-1 trick above).
- **Padding** — lengthen the array (e.g. 16,000,000 → 16,000,016) and skip the padding words; shifts the colliding elements into different banks.
- **Struct-of-arrays instead of array-of-structs** — pivoting layout so hot fields are contiguous avoids cache misses *and* often resolves bank-stride issues.
- **Stride / bank theorem**: a stride-`s` access pattern hits all `b` banks iff `gcd(s, b) = 1`. So stride 16 on 16 banks is the *worst* case (gcd = 16, only 1 bank touched); stride 17 on 16 banks is ideal (gcd = 1, all 16 touched).

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.2.2 worked example.
- [[MemoryInterleaving]] — the discipline whose pathology this is.
- [[parproc-ch02-recurring-performance-issues]] — §2.8 forward-referenced bank conflicts as a Ch3 topic.
- [[SharedMemoryArchitecture]] — context.
- [[GPU]] — shared-memory bank conflicts in CUDA are the same phenomenon at warp scale.
