---
title: "ParProcBook Ch4: Introduction to OpenMP"
type: source
tags: [textbook, parallel-computing, openmp, pragma, shared-memory]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
---

# ParProcBook Ch4: Introduction to OpenMP

Chapter 4 (pp. 81–118) of *Programming on Parallel Machines: GPU, Multicore, Clusters and More* by [[NormMatloff]] of [[UCDavis]]. A thirty-eight-page applied tour of [[OpenMP]] — *"the de facto standard for shared-memory programming"* — built around a worked Dijkstra shortest-path example that is revisited under successive constructs ([[ParallelPragma|parallel]], [[OpenMPSingle|single]], [[Barrier|barrier]], [[CriticalSection|critical]], [[ParallelFor|for]], [[ScheduleClause|schedule]], [[ReductionClause|reduction]], [[OpenMPTaskDirective|task]], [[AtomicClause|atomic]], [[FlushPragma|flush]], [[OpenMPLocks|locks]]) plus six secondary examples (in-place matrix transpose, [[MandelbrotSet]] timing, recursive [[Quicksort]], root finding, mutual outlinks, adjacency-matrix transformation, and maximal-burst time series). Closes with compiler/runtime mechanics (Omni / Ompi / GCC), debugging tips, a performance section that walks the same Dijkstra code through problem-size scaling + fine-tuning + Omni-emitted intermediate code, and pointers to OpenMP examples later in the book.

## Summary

Chapter 4 is the book's first prescriptive chapter — Ch1–Ch3 surveyed paradigms and hardware; here the reader actually writes [[OpenMP]] code. The pedagogical spine is the **Dijkstra shortest-path algorithm**: §4.2 presents a serial version with a global vertex distance vector `mind`, a `notdone` membership bitmap, and an inner loop that finds the closest unprocessed vertex (`findmymin`) and then updates distances through it (`updatemind`). The OpenMP rewrite parallelizes the two inner loops by **partitioning the vertex set across threads**, with each thread computing a local `mymd`/`mymv` over its chunk; an `omp critical` section then reduces those into the global `md`/`mv`.

The pragmas are introduced one at a time on this code:

- **[[ParallelPragma|`#pragma omp parallel`]]** (§4.2.2): the only directive that *creates* a thread team. Variables declared **before** the directive within a function become shared across the team; variables declared **inside** the parallel block are thread-local. `private(x,y)` overrides; `firstprivate` initializes thread-locals from the surrounding shared value. Globals in the C/C++ sense are *always* shared — *"the primary means by which threads communicate with each other."*
- **[[OpenMPSingle|`#pragma omp single`]]** (§4.2.4): one thread runs the block; all wait at the implicit trailing barrier (unless `nowait`).
- **[[Barrier|`#pragma omp barrier`]]** (§4.2.5): explicit team-wide barrier.
- **Implicit barriers** (§4.2.6): live at the end of `single`, `parallel`, `for`, `sections`. Override with `nowait`. *"Putting in a barrier where it is not needed would severely reduce performance."*
- **[[CriticalSection|`#pragma omp critical`]]** (§4.2.7): mutual-exclusion block — the runtime handles lock setup.
- **[[ParallelFor|`#pragma omp for`]]** (§4.3): distributes the iterations of an immediately-following `for` loop across the team. Iterations must be independent. The loop index `i` is forced private *"even if by context it would be shared."*
- **Nested loops & `collapse(2)`** (§4.3.2): by default `for` parallelizes only the outer loop; nested `for` directives or — since OpenMP 3.0 — `collapse(N)` flattens N levels of nesting.
- **[[ScheduleClause|`schedule(static|dynamic|guided|runtime)`]]** (§4.3.3): controls iteration→thread mapping. **static** = round-robin chunks (default chunk = `n/nth`); **dynamic** = work-queue (default chunk = 1); **guided** = dynamic with chunk size *decreasing* over time (big chunks early to amortize overhead, small chunks late to balance the tail). **`schedule(static,chunk)`** takes a compile-time chunk; **`schedule(runtime)`** + **`omp_set_schedule()`** or **`OMP_SCHEDULE`** env var allows runtime selection.
- **In-place matrix transpose** (§4.3.4): triangular nested loop walks above-diagonal elements and swaps each with its below-diagonal counterpart; serves as a worked `#pragma omp for` example with poor cache behavior (Matloff suggests *"horizontal slabs above the diagonal, trade them with vertical ones below"* as a refinement).
- **[[ReductionClause|`reduction(op:var)`]]** (§4.3.5): private per-thread copies of `var` (initialized to `op`'s identity — 0 for `+`/`-`/`|`/`^`/`||`, 1 for `*`/`&&`, all-1s for `&`, all-0s for `|`); summed atomically into the shared `var` at end of block. *"Reducing the number of serializing atomic actions, and avoiding time-costly cache coherency transactions."* C/C++ eligible ops: `+ - * & | ^ && ||`. Variable must be scalar in C/C++ (array in FORTRAN), shared (typically global), and the FORTRAN version additionally has `min`/`max`. *"If we had old serial code that we wanted to parallelize, we would have to make no change to it!"*
- **[[MandelbrotSet|Mandelbrot]] example** (§4.4): instantiates the Ch2 [[LoadBalancing|load-balance]] case under OpenMP, with `#ifdef STATIC|DYNAMIC|GUIDED|RC` compile-time switches between `schedule()` clauses (and an `RC` random-chunk variant using a `rpermute()` shuffle).
- **[[OpenMPTaskDirective|`#pragma omp task`]]** (§4.5): explicit task queue — a thread encountering `task` arranges *some* (not necessarily itself) thread to execute the block *later*. Tasks may have to wait if all threads are busy. *"Task really simplifies the programming"* over hand-rolling a shared work-queue plus atomic enqueue/dequeue.
- **[[Quicksort]] with tasks** (§4.5.1): the canonical recursive case — `omp parallel` outside; `omp single nowait` to make exactly one thread call `qs(z, 0, zend, 0)` (the root of the recursion tree); then within each `qs` call, after `separate(z, …)`, two `omp task` directives spawn the left- and right-subtree recursive calls so any free team thread can pick them up. Refinements include the barrier-like `taskwait` clause.
- **[[AtomicClause|`#pragma omp atomic`]]** (§4.6.1): single-statement critical section that the compiler can lower to an atomic hardware instruction (e.g. Intel `LOCK` prefix). Eligible ops: `++ -- += -= *= <<= &= |=`. Far less overhead than `critical`. The chapter shows the GCC-emitted assembly: `lock addl %eax, tot(%rip)` for `#pragma omp atomic / tot += mysum;`.
- **[[FlushPragma|`#pragma omp flush(x)`]]** (§4.6.2): OpenMP takes a **[[RelaxedConsistency|relaxed consistency]]** approach — memory updates ("flushes") happen automatically at every synchronization point (barrier; entry/exit of critical/ordered/parallel; exit of parallel-for/sections/single). Between such points, `flush` forces a write-out. Architecture-dependent; if no hardware flush instruction exists the compiler falls back to a lock/unlock cycle.
- **Combining work-sharing constructs** (§4.7): `#pragma omp parallel for` and `#pragma omp parallel sections` collapse the team-spawning and work-distribution directives into one line.
- **Compiling, running, debugging** (§4.9): three open-source OpenMP compilers — **Omni** (Tsukuba; `omcc -g -o x x.c`; renames `main` to `_ompc_main`), **Ompi** (UoI Greece; `ompicc -g -o x x.c`; current 1.2.0 keeps `main`), and **GCC** ≥ 4.2 (`gcc -fopenmp -g -o x x.c`, or `-lgomp`). Thread count defaults to processor count; override via `OMP_NUM_THREADS` env var. Debugging uses the underlying threads facilities; GCC keeps line numbers and names well (with regressions noted past 4.4 due to register-residency optimizations).
- **Performance** (§4.10): three sub-sections walk the same Dijkstra code on a quad-core machine. **§4.10.1 problem size**: on `nv=1000`, more threads *slow* the program (`nth=1` 0.0055s, `nth=2` 0.0111s, `nth=4` 0.0296s) — synchronization overhead dominates. On `nv=25000`, threads *help* (`nth=1` 2.86s, `nth=2` 1.71s, `nth=4` 1.45s). **§4.10.2 fine-tuning**: eliminate the `critical` section by having each thread write `mymd`/`mymv` into a `mymins` global array, then one thread reduces post-barrier — yields ~15% speedup at 2 threads, less at 4. Open question: pad `mymins` to defeat [[FalseSharing]]; or switch to the §4.3.1 `#pragma omp for` variant with `schedule`. **§4.10.3 internals**: shows Omni's `-t` and Ompi's `-k` flags that emit intermediate `.c` files where pragmas have been replaced by `_ompc_enter_critical(&__ompc_lock_critical)` / `_ompc_exit_critical(...)` library calls. Cites *The GNU OpenMP Implementation* PDF for the libgomp translation reference.
- **Root finding** (§4.11): bracketing root finder where each iteration splits the current interval `[curra, currb]` into `nth` equal parts, one thread per part checks `f(myleft) * f(myright) < 0`, and the unique winner overwrites the shared `curra`/`currb`. *"The variables `curra` and `currb` are shared by all the threads, but due to the nature of the application, no critical sections are needed"* — the barrier, however, is essential.
- **Mutual outlinks** (§4.12): for a 0/1 adjacency matrix `m[n][n]`, compute the mean over $i<j$ of `sum_k m[i][k] * m[j][k]`. The example uses the Ch2 §2.4.3 randomized [[StaticTaskAssignment|static assignment]] pattern (`for (i = me; i < n; i += nth)`) for load balance; `#pragma omp atomic` aggregates each thread's `mysum` into `tot`; `#pragma omp barrier` separates the accumulation from the divide-and-return.
- **Adjacency-matrix transformation** (§4.13): converts an `n×n` 0/1 adjacency matrix into a lex-sorted 2-column edge list. Two `#pragma omp single`-guarded malloc/cumulative-sum phases bracket two parallel row-scan phases; the `cumul1s` prefix sum gives each row its starting offset in the output, so threads can fill their portion in parallel without contention.
- **Maximal burst in a time series** (§4.14): for a nonnegative series of length `n` and minimum window `k`, find the contiguous block of length ≥ `k` with maximal mean. $O(n^2)$ work — good parallelization candidate. The OpenMP code uses `#pragma omp for` over `perstart`, an inner serial loop over `perlen`, per-thread bests, and a `#pragma omp critical` final reduction. The `mean()` is updated incrementally as `(pl1 * xbar + x[perend]) / perlen` for `perlen > k`.
- **[[OpenMPLocks|Locks with OpenMP]]** (§4.15): in the rare case the high-level constructs are insufficient, OpenMP exposes locks: declare `omp_lock_t`, call `omp_set_lock()` / `omp_unset_lock()`.

## Key Claims

- **OpenMP is the de facto standard for shared-memory programming.** *"OpenMP has become the de facto standard for shared-memory programming."* (§4.1). The value proposition is "the best of both worlds — the true parallelism of (nonpreemptive) threads and the pleasure of avoiding the annoyances of threads programming."
- **All OpenMP constructs are pragmas.** *"#pragma omp ......"* — the number sign must be the first nonblank character. The compiler sees `#pragma` directives as hints it may translate to library calls; non-OpenMP compilers silently ignore them, so the same source compiles serially.
- **Only `parallel` creates threads.** Other constructs (`for`, `single`, `sections`, `critical`, `barrier`, `atomic`, `task`, `flush`) operate within an *existing* team — they are useless outside an enclosing `#pragma omp parallel` (or a combined `parallel for`/`parallel sections`).
- **Scope rule.** Variables declared **before** `#pragma omp parallel` (within the function) become shared across the team; variables declared **inside** the block are thread-local. `private(x,y)` makes pre-declared variables thread-local; `firstprivate` does the same but initializes from the outer value. Global (C/C++) variables are *always* shared.
- **Implicit barriers everywhere.** End of `single`, `parallel`, `for`, `sections` blocks all have implicit barriers. `nowait` removes them but is dangerous: *"in most cases will not be usable."* Conversely, *"putting in a barrier where it is not needed would severely reduce performance."*
- **The OpenMP `for` constraint: iterations must be independent.** *"one iteration cannot depend on the result of another."*
- **Loop index is private by default.** *"By the way, for obvious reasons OpenMP treats the loop index, `i` here, as private even if by context it would be shared."*
- **Schedule taxonomy.** **static** — round-robin chunks (default chunk ≈ `n/nth`). **dynamic** — work-queue (default chunk = 1). **guided** — dynamic with monotonically-decreasing chunk size. **runtime** — defer until `omp_set_schedule()` or `OMP_SCHEDULE` env var resolves the choice.
- **Big chunks vs small chunks tradeoff.** *"Large chunks are good, due to there being less overhead — every time a thread finishes a chunk, it must go through the critical section."* But *"if chunk sizes are large, then toward the end of the work, some threads may be working on their last chunks while others have finished and are now idle."* The `guided` clause is the structural answer.
- **`collapse(N)`** flattens N levels of loop nesting for thread assignment (since OpenMP 3.0).
- **Reduction identity table** (§4.3.5):

  | operator | initial value |
  |---|---|
  | `+` | 0 |
  | `-` | 0 |
  | `*` | 1 |
  | `&` | bit string of 1s |
  | `\|` | bit string of 0s |
  | `^` | 0 |
  | `&&` | 1 |
  | `\|\|` | 0 |

- **Reduction is efficient because it avoids per-iteration atomics.** *"By maintaining separate copies of `z` until the loop is done, we are reducing the number of serializing atomic actions, and are avoiding time-costly cache coherency transactions and the like."*
- **C/C++ reduction is scalar-only; FORTRAN allows arrays + has `min`/`max`.** *"The lack of other operations typically found in other parallel programming languages, such as min and max, is due to the lack of these operators in C/C++."* The footnote flags that for the Dijkstra example, min/max would not help anyway — Matloff needs both the minimum value and the vertex attaining it.
- **The `task` directive sets up a queue.** *"When a thread encounters a `task` directive, it arranges for some thread to execute the associated block — at some time. The first thread can continue. Note that the task might not execute right away."* This generalizes work-sharing to non-loop, non-section structures — recursion is the canonical use.
- **Quicksort root needs `single nowait`.** *"We want only one thread to execute the root of the recursion tree, hence the need for the `single` clause."* From there, each `qs` call's two recursive subcalls are wrapped in `omp task` so they propagate through the team.
- **`atomic` is a cheap one-statement `critical`.** *"The `critical` construct not only serializes your program, but also it adds a lot of overhead. If your critical section involves just a one-statement update to a shared variable… the OpenMP compiler can take advantage of an atomic hardware instruction, e.g. the LOCK prefix on Intel."* Eligible: `++ -- += -= *= <<= &= |=`.
- **GCC emits a `lock addl` for `omp atomic`** (§4.6.1) — confirmed by the worked assembly:
  ```
  lock addl  %eax, tot(%rip)
  call       GOMP_barrier
  ```
- **OpenMP uses [[RelaxedConsistency|relaxed consistency]].** Memory updates are flushed at every synchronization point: barrier; entry/exit of `critical`; entry/exit of `ordered`; entry/exit of `parallel`; exit of `parallel for`; exit of `parallel sections`; exit of `single`. Between such points, `#pragma omp flush(x)` forces an explicit write-out.
- **`flush` is architecture-dependent.** *"OpenMP compilers will typically have the proper machine instructions available for some common architectures. For the rest, it can force a flush at the hardware level by doing lock/unlock operations, though this may be costly in terms of time."*
- **Combining directives.** `#pragma omp parallel for` ≡ `#pragma omp parallel` + immediately-nested `#pragma omp for`. Also `parallel sections`.
- **Three open-source OpenMP compilers.** **Omni** (Tsukuba) `omcc -g -o x x.c`; renames `main` → `_ompc_main`. **Ompi** (UoI Greece) `ompicc -g -o x x.c`; from 1.2.0 keeps `main`. **GCC** ≥ 4.2 `gcc -fopenmp -g -o x x.c` (or `-lgomp`).
- **Thread count.** Default = number of processors. Override: `setenv OMP_NUM_THREADS 4` (csh) or `export OMP_NUM_THREADS=4`.
- **Debugging.** Underlying threads facilities work as usual. *"GCC maintains line numbers and names well. In earlier versions, it had a problem in that it did not retain names of local variables within blocks controlled by `omp parallel`. That problem was fixed in version 4.4 of the GCC suite, but seems to have slipped back in with some later versions! This may be due to compiler optimizations that place variables in registers."*
- **Problem-size effect** (§4.10.1, Dijkstra on quad-core):

  | nv | nth | time (s) |
  |---|---|---|
  | 1000 | 1 | 0.005472 |
  | 1000 | 2 | 0.011143 |
  | 1000 | 4 | 0.029574 |
  | 25000 | 1 | 2.861814 |
  | 25000 | 2 | 1.710665 |
  | 25000 | 4 | 1.453052 |

  *"The more parallelism we had, the slower the program ran!"* — at small `nv`, synchronization overhead dominates the parallel computation. At large `nv`, parallelization helps.
- **Fine-tuning Dijkstra by eliminating `critical`** (§4.10.2). Have each thread write `mymd`/`mymv` into a shared `mymins[2*nth]` array; after a barrier, one thread (in a `#pragma omp single`) scans `mymins` and updates global `md`/`mv`. Yields ~15% speedup at 2 threads:

  | nv | nth | time (s) |
  |---|---|---|
  | 25000 | 1 | 2.546335 |
  | 25000 | 2 | 1.449387 |
  | 25000 | 4 | 1.411387 |

  Further ideas Matloff flags but does not implement: pad `mymins` against [[FalseSharing]]; switch to §4.3.1's `#pragma omp for + schedule`.
- **OpenMP locks API** (§4.15). `omp_lock_t` variable type; `omp_set_lock()` / `omp_unset_lock()`. *"Though one of OpenMP's best virtues is that you can avoid working with those pesky lock variables… there are still some instances in which lock variables may be useful."*
- **Cross-references to later OpenMP examples** (§4.16): sampling bucket sort (§1.6.1.1), parallel prefix sum / run-length decoding (§10.3), matrix multiplication (§11.3.2.1), Jacobi linear-system solver with `reduction` (§11.5.4), another Quicksort implementation (§12.1.2).

## Key Quotes

> *"OpenMP has become the de facto standard for shared-memory programming."* — §4.1, p. 81.

> *"Most OpenMP constructs are expressed via **pragmas**, i.e. directives. The syntax is `#pragma omp ......`. The number sign must be the first nonblank character in the line."* — §4.1, p. 81.

> *"That directive sets up a team of threads (which includes the master), all of which execute the block following the directive in parallel. Note that, unlike the **for** directive… the **parallel** directive leaves it up to the programmer as to how to partition the work."* — §4.2.2, p. 85.

> *"It is crucial to keep in mind that variables which are global to the program (in the C/C++ sense) are automatically global to all threads. This is the primary means by which the threads communicate with each other."* — §4.2.3, p. 86.

> *"Needless to say, the latter [`nowait`] should be used with care, and in most cases will not be usable. On the other hand, putting in a barrier where it is not needed would severely reduce performance."* — §4.2.6, p. 87.

> *"By the way, for obvious reasons OpenMP treats the loop index, `i` here, as private even if by context it would be shared."* — §4.3.1, p. 90.

> *"In this default version of the `for` construct, iterations are executed by threads in unpredictable order; the OpenMP standard does not specify which threads will execute which iterations in which order."* — §4.3.3, p. 90.

> *"By maintaining separate copies of `z` until the loop is done, we are reducing the number of serializing atomic actions, and are avoiding time-costly cache coherency transactions and the like."* — §4.3.5, p. 93. The reduction-clause performance thesis in one line.

> *"Indeed, if we had old serial code that we wanted to parallelize, we would have to make no change to it!"* — §4.3.5, p. 93. On the reduction clause's drop-in property.

> *"The basic idea is to set up a task queue: When a thread encounters a `task` directive, it arranges for some thread to execute the associated block — at some time."* — §4.5, p. 97.

> *"task really simplifies the programming."* — §4.5, p. 98.

> *"The `critical` construct not only serializes your program, but also it adds a lot of overhead. If your critical section involves just a one-statement update to a shared variable… the OpenMP compiler can take advantage of an atomic hardware instruction, e.g. the LOCK prefix on Intel, to set up an extremely efficient critical section."* — §4.6.1, p. 99.

> *"OpenMP takes a **relaxed consistency** approach, meaning that it forces updates to memory ('flushes') at all synchronization points."* — §4.6.2, p. 101.

> *"As is usually the case with parallel programming, merely parallelizing a program won't necessarily make it faster, even on shared-memory hardware. Operations such as critical sections, barriers and so on serialize an otherwise-parallel program, sapping much of its speed."* — §4.10, p. 104.

> *"The more parallelism we had, the slower the program ran! The synchronization overhead was just too much to be compensated by the parallel computation."* — §4.10.1, p. 104. The problem-size effect headline.

> *"The variables `curra` and `currb` are shared by all the threads, but due to the nature of the application, no critical sections are needed."* — §4.11, p. 109. The root-finding correctness argument.

> *"Though one of OpenMP's best virtues is that you can avoid working with those pesky lock variables needed for straight threads programming, there are still some instances in which lock variables may be useful."* — §4.15, p. 117.

## Connections

- [[NormMatloff]] — author.
- [[UCDavis]] — author's institution.
- [[parproc-ch01-intro-parallel-processing]] — Ch1 surveyed [[OpenMP]] alongside [[Pthreads]]/[[MPI]]/[[Snow]]/[[Rdsm]] via the [[SamplingBucketSort]] example; this chapter follows up with the full pragma walkthrough.
- [[parproc-ch02-recurring-performance-issues]] — Ch2's [[StaticTaskAssignment]] / [[DynamicTaskAssignment]] / [[Mandelbrot]] timing thesis is operationalized here under `schedule(static|dynamic|guided)` (§4.4 Mandelbrot) and replicated on Dijkstra (§4.10 problem-size scaling).
- [[parproc-ch03-shared-memory-parallelism]] — Ch3 supplies the hardware substrate underneath every Ch4 pragma: [[CriticalSection]] on top of [[TestAndSet]]/`LOCK`; `omp atomic` on top of `lock addl`; `omp flush` on top of [[MemoryConsistency|relaxed consistency models]]; `omp barrier` on top of the §3.12 tree/butterfly implementations; [[FalseSharing]] revisited as the §4.10.2 padding ideas.
- [[OpenMP]] — primary entity; substantially fleshed out by this ingest.
- [[ParallelPragma]] — `#pragma omp parallel`; only directive that creates a thread team.
- [[OpenMPSingle]] — `#pragma omp single`; one-thread-only block.
- [[Barrier]] — `#pragma omp barrier` and the implicit barriers at the end of `single`/`parallel`/`for`/`sections`; `nowait` override.
- [[CriticalSection]] — `#pragma omp critical`; mutual-exclusion block.
- [[ParallelFor]] — `#pragma omp for`; loop-iteration distribution.
- [[ScheduleClause]] — `schedule(static|dynamic|guided|runtime)` + chunk sizing.
- [[ReductionClause]] — `reduction(op:var)` with private per-thread copies and atomic final combine.
- [[OpenMPTaskDirective]] — `#pragma omp task` for non-loop work distribution; `taskwait` refinement.
- [[AtomicClause]] — `#pragma omp atomic` for one-statement updates; lowers to hardware atomic instructions.
- [[FlushPragma]] — `#pragma omp flush(x)` + the relaxed-consistency synchronization-point list.
- [[WorkSharing]] — umbrella term covering `for`/`sections`/`single`; the combined `parallel for` / `parallel sections` form.
- [[RelaxedConsistency]] — OpenMP's memory model.
- [[FalseSharing]] — flagged as a tuning concern in §4.10.2.
- [[LoadBalancing]] — the `schedule` clause's reason for being; revisits Ch2's Mandelbrot story.
- [[StaticTaskAssignment]] / [[DynamicTaskAssignment]] — schedule(static) vs schedule(dynamic); §4.12 mutual-outlinks reuses Ch2's randomized static pattern.
- [[Pthreads]] — implicit baseline OpenMP abstracts over.
- [[MandelbrotSet]] — §4.4 timing example.
- [[Quicksort]] — §4.5.1 recursive task example.
- [[DijkstraAlgorithm]] — §4.2 / §4.10 worked example.
- [[OpenMPLocks]] — `omp_lock_t` + `omp_set_lock` / `omp_unset_lock` API for when high-level constructs are insufficient.
- [[Mandelbrot]] — Ch2 page; this chapter's §4.4 supplies the OpenMP code that produces Ch2's timing table.

## Contradictions

- **No contradictions with prior wiki content.** This chapter is the prescriptive follow-up to Ch1's OpenMP survey and Ch3's hardware substrate. Ch1 introduced `#pragma omp parallel/single/for/barrier/critical`; Ch4 adds `for`'s `schedule` clause + `reduction` + `task` + `atomic` + `flush` + `sections` + lock API + the `parallel for` combined form — all additive.
- **Internal tension between §4.10.1 and §4.10.2.** §4.10.1 shows raw parallelization *hurts* small problems (1000-vertex Dijkstra: 4 threads 5.4× slower than 1 thread). §4.10.2 then shows that for 25000 vertices, eliminating the critical section recovers ~15% — but only at 2 threads. At 4 threads the gain is "less". Not a contradiction with the wiki, but worth flagging: the chapter's optimism about OpenMP's ease-of-use is empirically uneven and depends on problem size, contention, and (per §4.10.2's open questions) [[FalseSharing]] mitigations the chapter does not implement.
- **§4.6.1 atomic-instruction claim refines Ch3.** Ch3 §3.4.1.1 already mentioned Intel `LOCK` as the substrate; Ch4 §4.6.1 confirms by showing GCC's actual `lock addl %eax, tot(%rip)` output for `#pragma omp atomic`. The MIT-licensed *libgomp* PDF is cited as the translation reference.
