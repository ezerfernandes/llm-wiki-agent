---
title: "Dive into Systems — Ch 14.2 POSIX Threads"
type: source
tags: [book, textbook, dive-into-systems, pthreads, threads, posix, parallel-computing, shared-memory, multithreading]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C14-SharedMemory/posix.html
---

## Summary

Chapter 14.2 of *[[DiveIntoSystems]]* — second leaf of Ch 14 *Leveraging Shared Memory in the Multicore Era*. Pivots from [[dis-14-1-multicore|Ch 14.1]]'s **motivation** for [[Thread|thread]]-level parallelism on [[MulticoreProcessor|multicore]] hardware to the **concrete API**: [[Pthreads]], the IEEE [[POSIX]] standardized C threading library "available on almost all UNIX-like operating systems." Codifies the **four-step thread lifecycle** — declare [[Thread|thread]] storage (`pthread_t`), spawn worker threads via [[PthreadCreate|`pthread_create`]], execute the [[ThreadFunction|thread function]] (one per worker), join via [[PthreadJoin|`pthread_join`]] — and the **two function signatures** that anchor the entire API: `pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(*thread_function)(void *), void *thread_args)` and `pthread_join(pthread_t thread, void **return_val)`. Introduces the canonical [[ThreadFunction|thread-function]] prototype `void *func(void *arg)` — the [[VoidStar|`void *`]] generic typing on both argument and return making the API type-agnostic. Each thread runs the thread function with its **private execution state** (own stack memory and register values) — the corpus's first explicit codification of [[Pthreads]]' [[PerThreadStack|per-thread stack]] / per-thread registers semantics. Surfaces the **[[ThreadID|TID]]** convention (a unique per-thread identifier, typically passed as the [[PthreadCreate|`pthread_create`]] argument) used to distinguish threads inside the [[ThreadFunction|thread function]] for work distribution. Names the **[[GccPthreadFlag|`-pthread`]] compile flag** required to link the Pthreads library. Worked example: a four-worker spawn — array of `pthread_t threads[4]`, loop calls [[PthreadCreate|`pthread_create`]] passing each worker its own `long ids[i]`, second loop calls [[PthreadJoin|`pthread_join`]] on each. **Cautionary principle**: *"You should never make any assumptions about the order in which threads will execute"* — correctness-by-ordering requires explicit synchronization (deferred to later sections). [[PthreadJoin|`pthread_join`]] on a still-running thread blocks; on a terminated thread frees its execution-context resources. **128th ingested DIS chapter**; promotes [[Pthreads]] to full coverage (forward-referenced from [[dis-3-6-gdb-pthreads|Ch 3.6]]); mints **5 new concept pages**: [[PthreadCreate]], [[PthreadJoin]], [[ThreadFunction]], [[ThreadID]], [[GccPthreadFlag]].

## Key Claims

- **[[Pthreads]] = IEEE [[POSIX]] threads API.** *"POSIX is an acronym for Portable Operating System Interface. It is an IEEE standard that specifies how UNIX systems look, act, and feel. The POSIX threads API is available on almost all UNIX-like operating systems."* The standardized low-level shared-memory threading layer.
- **Thread creation signature**: `pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(*thread_function)(void *), void *thread_args)`. The four parameters: (1) **`pthread_t *thread`** — out-parameter; the system writes the new thread's identification data here, enabling later [[PthreadJoin|join]] references; (2) **`const pthread_attr_t *attr`** — thread attributes, typically `NULL` for default behaviour; (3) **`void *(*thread_function)(void *)`** — the [[ThreadFunction|thread function]] the created thread executes; (4) **`void *thread_args`** — single [[VoidStar|`void *`]] argument passed through to the [[ThreadFunction|thread function]].
- **Thread join signature**: `pthread_join(pthread_t thread, void **return_val)`. Two parameters: (1) the [[Pthreads|`pthread_t`]] identifying the thread to wait on, (2) optional `void **return_val` for capturing the [[ThreadFunction|thread function]]'s return pointer (`NULL` discards it). *"The `pthread_join` function suspends the execution of its caller until the thread it references terminates."*
- **[[ThreadFunction|Thread function]] prototype**: `void *thread_function(void *arg)`. *"A thread function is analogous to a `main` function for a worker (created) thread — a thread begins execution at the start of its thread function and terminates when it reaches the end."* The [[VoidStar|`void *`]] on argument and return makes the function signature type-agnostic; callers cast.
- **Per-thread private execution state**: *"Each thread executes the thread function using its private execution state (i.e., its own stack memory and register values)."* The corpus's first explicit DIS codification of the [[PerThreadStack|per-thread stack]] / per-thread registers split — globals are shared (per [[Thread]]'s standard framing), locals are not.
- **[[ThreadID|Thread ID (TID)]] convention**: each thread receives a unique identifier, typically passed during creation as `thread_args`. *"Thread IDs enable distinguishing between threads and assigning work distribution within the thread function."* The pattern: `main` allocates `long ids[N]`, the spawn loop passes `&ids[i]` to [[PthreadCreate|`pthread_create`]], the [[ThreadFunction|thread function]] casts `(long *)id` and dereferences.
- **Compile flag**: `-pthread` links the Pthreads library: `gcc -o program program.c -pthread`. (The flag also predefines threading-related macros — distinct from `-lpthread`.)
- **Four-step thread lifecycle** for the canonical worker pattern: (1) **declare** `pthread_t threads[N]` storage in `main`, (2) **create** via a loop of [[PthreadCreate|`pthread_create`]] calls — each worker spawned with default attributes and a per-thread argument, (3) **execute** — each worker runs its [[ThreadFunction|thread function]] concurrently with its private stack and registers, (4) **join** via a loop of [[PthreadJoin|`pthread_join`]] calls so `main` waits for every worker before continuing.
- **Join semantics**: *"Joining a thread that has terminated frees the thread's execution context and resources. Attempting to join a thread that hasn't terminated blocks the caller until the thread terminates."* [[PthreadJoin|`pthread_join`]] is both a synchronization barrier and the resource-reclamation hook.
- **No ordering guarantees**: *"You should never make any assumptions about the order in which threads will execute. If the correctness of your program requires that threads run in a particular order, you must add synchronization to your program to prevent threads from running when they shouldn't."* The motivation for later [[Mutex|mutex]] / [[Barrier|barrier]] sections — this section deliberately stops at create + join.

## Key Quotes

> *"POSIX is an acronym for Portable Operating System Interface. It is an IEEE standard that specifies how UNIX systems look, act, and feel. The POSIX threads API is available on almost all UNIX-like operating systems."*

> *"A thread function is analogous to a `main` function for a worker (created) thread — a thread begins execution at the start of its thread function and terminates when it reaches the end."*

> *"Each thread executes the thread function using its private execution state (i.e., its own stack memory and register values)."*

> *"The `pthread_join` function suspends the execution of its caller until the thread it references terminates."*

> *"You should never make any assumptions about the order in which threads will execute."*

## Worked Example — four-worker spawn

```c
#include <pthread.h>

void *thread_function(void *id) {
    long *myid = (long *) id;
    printf("Thread %ld\n", *myid);
    return NULL;
}

int main() {
    pthread_t threads[4];
    long ids[4];
    for (int i = 0; i < 4; i++) {
        ids[i] = i;
        pthread_create(&threads[i], NULL, thread_function, &ids[i]);
    }
    for (int i = 0; i < 4; i++) {
        pthread_join(threads[i], NULL);
    }
    return 0;
}
```

Compile: `gcc -o program program.c -pthread`. Each of the four workers runs `thread_function` with its own [[ThreadID|TID]] (`0`/`1`/`2`/`3`); `main` waits via [[PthreadJoin|`pthread_join`]] before exiting. Print order is **not** guaranteed.

## Connections

- [[DiveIntoSystems]] — Ch 14.2 of the book; second leaf of Ch 14 *Leveraging Shared Memory in the Multicore Era*.
- [[dis-14-1-multicore]] — immediate predecessor; motivates [[Thread|thread]]-level parallelism on [[MulticoreProcessor|multicore]] hardware. Ch 14.2 supplies the API that realizes the motivation: [[Pthreads]].
- [[Pthreads]] — promoted from [[dis-3-6-gdb-pthreads|Ch 3.6]]'s forward-referenced [[GDB]]-debugging stub to **full coverage** here. Ch 14.2 is the corpus's canonical DIS-side codification of [[PthreadCreate|`pthread_create`]] / [[PthreadJoin|`pthread_join`]] / [[ThreadFunction|thread function]] / [[ThreadID|TID]] semantics.
- [[dis-3-6-gdb-pthreads]] — Ch 3.6 forward-referenced Pthreads only for [[GDB]] thread-aware debugging; Ch 14.2 delivers the API the debugger reflects over.
- [[Thread]] — the abstraction Pthreads instantiates; Ch 14.2 supplies the C-level *create / join / function-pointer* mechanics.
- [[PthreadCreate]] — new concept; `pthread_create` signature + parameters.
- [[PthreadJoin]] — new concept; `pthread_join` signature + blocking semantics.
- [[ThreadFunction]] — new concept; the `void *func(void *)` prototype every Pthreads worker takes.
- [[ThreadID]] — new concept; per-thread unique identifier, the work-distribution discriminator.
- [[GccPthreadFlag]] — new concept; the `-pthread` link flag.
- [[POSIX]] — the IEEE standard family Pthreads belongs to.
- [[VoidStar]] — the generic-pointer convention Pthreads' API design rests on (argument + return both [[VoidStar|`void *`]]).
- [[parproc-ch01-intro-parallel-processing]] — Pacheco's *Parallel Processing* introduces the same `pthread_create` / `pthread_join` API via a Sieve-of-Eratosthenes example; Ch 14.2 is DIS's parallel introduction.
- [[SharedMemoryArchitecture]] — Pthreads' execution model (single address space, multiple threads).
- [[ConcurrencyVsParallelism]] — Ch 14.1 distinction Ch 14.2's API operationalizes.
- [[Mutex]] / [[Barrier]] / [[RaceCondition]] — synchronization primitives deferred to later Ch 14 sections; Ch 14.2 ends with the explicit warning that without them ordering cannot be assumed.

## Contradictions

None. Ch 14.2 strictly extends [[Pthreads]] coverage from the [[dis-3-6-gdb-pthreads|Ch 3.6]] stub. No existing claim in the wiki conflicts with the `pthread_create` / `pthread_join` signatures or the `void *func(void *)` thread-function prototype.
