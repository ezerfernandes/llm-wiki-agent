---
title: "Pthreads"
type: entity
tags: [library, threading, posix, c, parallel-computing]
sources: [parproc-ch01-intro-parallel-processing, dis-3-6-gdb-pthreads, dis-14-2-posix]
last_updated: 2026-05-18
---

# Pthreads

POSIX threads — the standardized C threads library originating on Unix and since ported to other platforms. The low-level shared-memory threading API: applications create threads with `pthread_create`, wait on them with `pthread_join`, lock shared state with `pthread_mutex_lock`/`unlock`, and synchronize with `pthread_barrier_wait` ([[Barrier]]).

[[parproc-ch01-intro-parallel-processing]] introduces Pthreads via a Sieve-of-Eratosthenes prime finder: a fixed pool of worker threads grabs the "next sieve multiplier" from a shared `nextbase` counter (protected by a mutex — the chapter's canonical [[CriticalSection]] example), each thread crosses out multiples in a shared `prime[]` array, and `main` joins all workers before counting results.

The chapter's framing: "shared-memory programming is generally done with *threads*. All major OSs offer threads systems, and independent ones have been developed too. One issue, though, is whether one uses threads directly, as with the Pthreads system, or from a higher-level interface such as [[OpenMP]]." Pthreads sits at the low-level end of that spectrum; modern alternatives include C++11's `std::thread`.

## Debugging Pthreads with GDB ([[dis-3-6-gdb-pthreads|DIS Ch 3.6]])

[[GDB]] tracks each Pthreads thread by **three identifiers**: the [[Pthreads|`pthread_t`]] library ID, the kernel-side **LWP ID** ([[LightweightProcess|lightweight-process]] scheduling ID), and [[GDB]]'s own **GDB thread number** (the one used in commands). Most platforms maintain a 1:1 correspondence.

Thread-aware [[GDB]] commands layered on Pthreads:

- [[GdbInfoThreads|`info threads`]] — enumerate all active threads (`*` marks the current one)
- [[GdbThreadSwitch|`thread <N>`]] — switch the inspection context to a specific thread's [[StackFrame|stack]] / [[LocalVariable|locals]] / [[CpuRegister|registers]]
- `break <loc> thread <N>` — thread-qualified [[Breakpoint|breakpoint]] firing only for the named thread
- [[GdbThreadApply|`thread apply all <cmd>`]] — broadcast a [[GDB]] command across every thread; canonical use is `thread apply all bt` for a multi-thread call-stack snapshot (the standard **deadlock diagnostic**)
- [[GdbSet|`set print thread-events on`]] — notify on thread create / terminate
- [[GdbSet|`set scheduler-locking`]] — override the default stop-the-world breakpoint behaviour (any thread hitting a breakpoint pauses all threads) so only the triggering thread halts

Practical debugging recommendations from Ch 3.6: **minimize active thread count** during development, **include the thread ID in debug output**, and **scope verbose logging to one thread** to suppress interleaved noise.

Full Pthreads coverage in *Dive into Systems* is deferred to Ch 14; Ch 3.6 introduces the library only insofar as needed for [[GDB]]'s thread-debugging commands.

## Core API ([[dis-14-2-posix|DIS Ch 14.2]])

DIS Ch 14.2 delivers the full API codification (the forward reference from Ch 3.6 closes here). Pthreads is *"available on almost all UNIX-like operating systems"* — the IEEE [[POSIX]] standardized threading layer.

### [[PthreadCreate|`pthread_create`]] — spawn a worker

```c
pthread_create(pthread_t *thread,
               const pthread_attr_t *attr,
               void *(*thread_function)(void *),
               void *thread_args)
```

Writes the new thread's `pthread_t` to `*thread`; the worker immediately starts running `thread_function(thread_args)` concurrently with the caller. `attr` is typically `NULL` for defaults.

### [[PthreadJoin|`pthread_join`]] — wait + reclaim

```c
pthread_join(pthread_t thread, void **return_val)
```

> *"The `pthread_join` function suspends the execution of its caller until the thread it references terminates."*

Blocks if the target is still running; reclaims its execution-context resources once it terminates. `return_val` (or `NULL`) captures the thread function's return pointer.

### [[ThreadFunction|Thread function]] prototype

```c
void *thread_function(void *arg) { ... return NULL; }
```

> *"A thread function is analogous to a `main` function for a worker (created) thread — a thread begins execution at the start of its thread function and terminates when it reaches the end."*

Both argument and return are [[VoidStar|`void *`]] — the generic typing that lets one API surface handle any data shape.

### Per-thread execution state

> *"Each thread executes the thread function using its private execution state (i.e., its own stack memory and register values)."*

Locals inside the [[ThreadFunction|thread function]] are per-thread (separate stack frames); globals and heap are shared.

### [[ThreadID|Thread ID (TID)]] convention

User-supplied per-thread identifier, typically a `long` passed via `thread_args`, used to distinguish workers for work distribution / debug output. Distinct from the library-level `pthread_t`, the kernel **LWP ID**, and [[GDB]]'s thread number (the [[dis-3-6-gdb-pthreads|Ch 3.6]] triple).

### Four-step lifecycle

1. Declare `pthread_t threads[N]` storage.
2. Spawn workers in a [[PthreadCreate|`pthread_create`]] loop.
3. Each worker runs its [[ThreadFunction|thread function]] with private state.
4. [[PthreadJoin|`pthread_join`]] each worker before `main` exits.

### Compile flag

```bash
gcc -o program program.c -pthread
```

The [[GccPthreadFlag|`-pthread`]] flag links the Pthreads library and predefines threading macros.

### No ordering guarantees

> *"You should never make any assumptions about the order in which threads will execute."*

Correctness-by-ordering requires explicit synchronization ([[Mutex|mutex]] / [[Barrier|barrier]]) introduced in later Ch 14 sections.

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces Pthreads with the prime-sieve example.
- [[dis-3-6-gdb-pthreads]] — *Dive into Systems* Ch 3.6: Pthreads' first sighting in DIS, in the context of [[GDB]] thread-aware debugging. Full Pthreads coverage deferred to DIS Ch 14.
- [[dis-14-2-posix]] — *Dive into Systems* Ch 14.2: full API codification ([[PthreadCreate|`pthread_create`]] / [[PthreadJoin|`pthread_join`]] / [[ThreadFunction|thread function]] / [[ThreadID|TID]] / [[GccPthreadFlag|`-pthread`]]).
- [[PthreadCreate]] / [[PthreadJoin]] / [[ThreadFunction]] / [[ThreadID]] / [[GccPthreadFlag]] — the per-primitive concept pages.
- [[POSIX]] — the IEEE standard family.
- [[VoidStar]] — the generic-pointer convention Pthreads' API rests on.
- [[OpenMP]] — higher-level pragma-based alternative built on the same threading substrate.
- [[CriticalSection]] — the lock pattern Pthreads makes explicit via `pthread_mutex_*`.
- [[Mutex]] — `pthread_mutex_t` is the canonical mutex implementation.
- [[Barrier]] — `pthread_barrier_wait` is Pthreads' barrier primitive.
- [[Thread]] — the abstraction Pthreads instantiates.
- [[SharedMemoryArchitecture]] — Pthreads' execution model.
- [[GDB]] / [[GdbInfoThreads]] / [[GdbThreadSwitch]] / [[GdbThreadApply]] — the [[GDB]] thread-debugging command surface that reflects over Pthreads state.
