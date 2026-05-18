---
title: "Test-and-Set (TAS)"
type: concept
tags: [parallel-computing, synchronization, hardware, shared-memory]
sources: [parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# Test-and-Set (TAS)

The canonical atomic synchronization primitive for [[SharedMemoryArchitecture|shared-memory]] hardware. Applied to memory location `L` and register `R`:

```
copy L to R
if R is 0 then write 1 to L
```

*"And most importantly, these operations are done in an **atomic** manner; no bus transactions by other processors may occur between the two steps."* ([[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.4.1).

Hardware-wise, the CPU exposes a dedicated TAS pin connected to a TAS line on the bus; bus arbitration ensures the two micro-steps run without interruption.

## Lock implementation

Using TAS to guard a critical section C with lock variable L (1 = locked, 0 = unlocked):

```
TRY: TAS R, L
     JNZ TRY
C:   ...        ; start of critical section
     ...
     ...        ; end of critical section
     MOV 0, L   ; unlock
```

The JNZ-back-to-TAS construct is a busy spin; if L was already 1, R receives 1, Z flag is clear, jump retries. When L is 0, R receives 0, Z flag is set, fall through into C, and TAS atomically writes 1 to L locking the section.

## Limitations and successors

Pure-TAS busy-spinning is **disastrous on bus-only systems** — *"as each processor contending for a lock variable spins in the loop shown above, it is adding tremendously to bus traffic."* The forcing function for adding per-CPU caches (§3.5.1) and the [[CacheCoherency|cache-coherency]] protocols that maintain them.

In crossbar or Ω-network systems, packet types must include a TAS code (e.g. 2-bit field: 00 Read, 01 Write, 10 TAS); *"the atomicity here is best done at the memory, i.e. some hardware should be added at the memory so that TAS can be done"* — otherwise the entire processor-to-memory path is locked for the duration.

Compare and exchange (`CMPXCHG` on x86, used with the Intel **`LOCK` prefix**) is the modern descendant — `lock cmpxchg` provides the same atomicity without a dedicated TAS pin/line.

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.4.1.
- [[FetchAndAdd]] — sibling synchronization primitive, optimized for `X++`-style updates.
- [[CacheCoherency]] — TAS spin-traffic motivates caches, which motivate coherency.
- [[CriticalSection]] — what TAS guards.
- [[SharedMemoryArchitecture]] — substrate.
