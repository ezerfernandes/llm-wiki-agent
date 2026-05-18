---
title: "OpenMP"
type: entity
tags: [library, threading, parallel-computing, pragma, compiler]
sources: [parproc-ch01-intro-parallel-processing, parproc-ch04-introduction-to-openmp]
last_updated: 2026-05-17
---

# OpenMP

Compiler-directive-driven shared-memory parallel programming model for C/C++/Fortran. *"OpenMP has become the de facto standard for shared-memory programming"* ([[parproc-ch04-introduction-to-openmp]] §4.1). Threads are *"there, but rather hidden by higher-level abstractions"* — programmers add `#pragma omp` directives to ordinary serial code, and the compiler+runtime spin up a thread pool to execute the marked regions in parallel. Non-OpenMP compilers silently ignore `#pragma` directives, so the same source compiles serially as a fallback.

The value proposition (per [[parproc-ch01-intro-parallel-processing]] §1.3.2.2): *"the best of both worlds — the true parallelism of (nonpreemptive) threads and the pleasure of avoiding the annoyances of threads programming."* OpenMP *"alleviates you of work and alleviates your code of clutter"* relative to hand-coded [[Pthreads]].

## Pragmas

[[parproc-ch04-introduction-to-openmp]] walks each construct via a worked Dijkstra shortest-path example. Syntax: `#pragma omp ...` with the number sign as the first nonblank character of the line.

### Thread-team management
- **`#pragma omp parallel`** ([[ParallelPragma]]) — the *only* directive that creates a thread team. All threads in the team execute the following block. Variables declared *inside* the block are thread-local; variables declared *before* the block (same function scope) are shared. Globals (C/C++ sense) are *always* shared — *"the primary means by which the threads communicate with each other."*
- **`private(x,y)`** — make pre-declared variables thread-local.
- **`firstprivate(x)`** — like `private`, but initialize each thread's copy from the surrounding shared value.
- **`#pragma omp single`** ([[OpenMPSingle]]) — exactly one thread executes the block; all wait at the implicit trailing barrier (unless `nowait`).

### Synchronization
- **`#pragma omp barrier`** ([[Barrier]]) — explicit team-wide barrier.
- **Implicit barriers** at the end of `single`, `parallel`, `for`, `sections`. Override via `nowait`. *"Putting in a barrier where it is not needed would severely reduce performance"* — but `nowait` *"in most cases will not be usable."*
- **`#pragma omp critical`** ([[CriticalSection]]) — mutual-exclusion block; runtime handles lock setup.
- **`#pragma omp atomic`** ([[AtomicClause]]) — single-statement critical section; the compiler may lower to a hardware atomic instruction (e.g. Intel `LOCK` prefix; GCC emits `lock addl`). Eligible operators: `++ -- += -= *= <<= &= |=`. Far cheaper than `critical` for one-statement updates.
- **`#pragma omp flush(x)`** ([[FlushPragma]]) — force a memory flush of `x`. Used between synchronization points (which already imply flushes).

### Work sharing ([[WorkSharing]])
- **`#pragma omp for`** ([[ParallelFor]]) — distributes iterations of an immediately-following `for` loop across the team. Iterations must be independent. Loop index is private by default.
- **`#pragma omp sections`** / `#pragma omp section` — distribute named code blocks across threads.
- **`collapse(N)`** clause (OpenMP 3.0+) — flatten N levels of nested loops for thread assignment.
- **Combined forms** — `#pragma omp parallel for` and `#pragma omp parallel sections` collapse team-spawning + work-distribution into one directive.

### Schedule clause ([[ScheduleClause]])
Controls iteration→thread mapping for `#pragma omp for`:
- **`schedule(static)`** — round-robin chunks; default chunk ≈ `n/nth`.
- **`schedule(static,chunk)`** — compile-time fixed chunk size.
- **`schedule(dynamic)`** — work-queue; default chunk = 1; threads request next chunk as they finish.
- **`schedule(guided)`** — dynamic with chunk size *decreasing* over time (big chunks early to amortize overhead, small chunks late to balance the tail).
- **`schedule(runtime)`** + `omp_set_schedule()` / `OMP_SCHEDULE` env var — defer until runtime.

### Reduction clause ([[ReductionClause]])
- **`reduction(op:var)`** — private per-thread copies of `var` (initialized to `op`'s identity); combined into the shared `var` at end of block. C/C++ operators: `+ - * & | ^ && ||` (FORTRAN adds `min` / `max` and allows array reduction variables; C/C++ requires scalar). Initial-value table per chapter §4.3.5:

  | operator | initial |
  |---|---|
  | `+` | 0 |
  | `-` | 0 |
  | `*` | 1 |
  | `&` | all 1s |
  | `\|` | all 0s |
  | `^` | 0 |
  | `&&` | 1 |
  | `\|\|` | 0 |

  *"By maintaining separate copies of `z` until the loop is done, we are reducing the number of serializing atomic actions, and are avoiding time-costly cache coherency transactions and the like."*

### Task directive ([[OpenMPTaskDirective]])
- **`#pragma omp task`** — set up a task queue. A thread encountering `task` arranges *some* (not necessarily itself) thread to execute the block *later*. Canonical for recursive structures (e.g. [[Quicksort]] subtree calls).
- **`#pragma omp taskwait`** — barrier-like wait for spawned child tasks.

### Locks ([[OpenMPLocks]])
For the rare case the high-level constructs are insufficient:
- `omp_lock_t lock_var;`
- `omp_set_lock(&lock_var)` / `omp_unset_lock(&lock_var)`

## Memory model

OpenMP uses **[[RelaxedConsistency|relaxed consistency]]**: memory updates ("flushes") happen automatically at every synchronization point:
- `barrier`
- entry / exit of `critical`
- entry / exit of `ordered`
- entry / exit of `parallel`
- exit of `parallel for`
- exit of `parallel sections`
- exit of `single`

Between such points, `#pragma omp flush(x)` forces an explicit write-out. *"The flush operation is obviously architecture-dependent. OpenMP compilers will typically have the proper machine instructions available for some common architectures. For the rest, it can force a flush at the hardware level by doing lock/unlock operations."*

## Compilers & runtime

Three open-source OpenMP compilers per §4.9.1:
- **GCC** ≥ 4.2 — `gcc -fopenmp -g -o x x.c` (or `-lgomp`). Maintains line numbers and names well.
- **Omni** (Tsukuba) — `omcc -g -o x x.c`. Renames `main()` → `_ompc_main()`; set GDB breakpoint accordingly.
- **Ompi** (UoI Greece) — `ompicc -g -o x x.c`. From version 1.2.0 keeps `main` unchanged.

Thread count defaults to the number of processors. Override via `setenv OMP_NUM_THREADS 4` (csh) or equivalent. Set chunk-size schedule at runtime via `omp_set_schedule(omp_sched_static, chunk)` or `setenv OMP_SCHEDULE "static,20"`.

Runtime helpers: `omp_get_thread_num()`, `omp_get_num_threads()`, `omp_get_wtime()`.

Debugging caveat: under optimization, some compilers eliminate local variables from the namespace ("there is no such variable" errors in GDB). Workaround: convert locals to globals temporarily, or use `#pragma omp threadprivate`, or compile with `-gstabs+`. GCC 4.4 fixed an earlier issue, but later versions regressed due to register-residency optimizations.

## Performance notes

From [[parproc-ch04-introduction-to-openmp]] §4.10, on a quad-core machine running parallel Dijkstra:
- **Problem size matters.** Small `nv=1000`: more threads runs *slower* (5.4× slowdown at 4 threads vs 1) — synchronization overhead dominates. Large `nv=25000`: 4 threads ≈ 2× faster than 1 thread.
- **Eliminating `critical` helps modestly.** Replace the per-iteration `critical` reducer with per-thread writes to a global `mymins[2*nth]` array + a single `omp single` post-barrier scan: ~15% speedup at 2 threads on `nv=25000`, less at 4.
- Open tuning knobs: pad `mymins` against [[FalseSharing]]; switch to `#pragma omp for + schedule` for the inner loops.

## Compiler internals

Per §4.10.3, the Omni `-t` and Ompi `-k` flags emit intermediate `.c` files where pragmas have been replaced by library calls. Sample Omni output for `omp critical`:
```
_ompc_enter_critical(&__ompc_lock_critical);
if ((mymd) < (((unsigned)(md)))) {
   (md) = (((int)(mymd)));
   (mv) = (mymv);
}
_ompc_exit_critical(&__ompc_lock_critical);
```
GCC's `omp atomic` lowers to a single `lock addl` instruction. See *The GNU OpenMP Implementation* (libgomp PDF) for the full translation reference.

## Connections
- [[parproc-ch01-intro-parallel-processing]] — Ch1 introduction via [[SamplingBucketSort]].
- [[parproc-ch04-introduction-to-openmp]] — Ch4 full pragma walkthrough — primary source for the construct list above.
- [[parproc-ch03-shared-memory-parallelism]] — hardware substrate for every OpenMP construct: [[TestAndSet]]/Intel `LOCK` under `critical`/`atomic`; [[MemoryConsistency]] under `flush`; the §3.12 barrier implementations under `barrier`.
- [[Pthreads]] — the lower-level threading API OpenMP abstracts over.
- [[ParallelPragma]], [[OpenMPSingle]], [[ParallelFor]], [[ScheduleClause]], [[ReductionClause]], [[OpenMPTaskDirective]], [[AtomicClause]], [[FlushPragma]], [[WorkSharing]], [[OpenMPLocks]] — the pragma family.
- [[CriticalSection]] — `#pragma omp critical` implements it.
- [[Barrier]] — explicit (`#pragma omp barrier`) and implicit forms.
- [[RelaxedConsistency]] — OpenMP's memory model.
- [[FalseSharing]] — flagged as a tuning concern in §4.10.2.
- [[LoadBalancing]] / [[StaticTaskAssignment]] / [[DynamicTaskAssignment]] — `schedule` clause variants.
- [[MandelbrotSet]] — §4.4 timing example.
- [[Quicksort]] — §4.5.1 recursive `task` example.
- [[DijkstraAlgorithm]] — §4.2 / §4.10 worked example throughout the chapter.
- [[SamplingBucketSort]] — Ch1's introductory OpenMP example.
- [[SharedMemoryArchitecture]] — OpenMP's target.
- [[ProcessorAffinity]] — OpenMP 3.1 adds thread-to-core pinning ([[parproc-ch03-shared-memory-parallelism]] §3.10).
- [[Thread]] — OpenMP's execution unit, surfaced via `omp_get_thread_num()` / `omp_get_num_threads()`.
