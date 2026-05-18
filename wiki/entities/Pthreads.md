---
title: "Pthreads"
type: entity
tags: [library, threading, posix, c, parallel-computing]
sources: [parproc-ch01-intro-parallel-processing, dis-3-6-gdb-pthreads]
last_updated: 2026-05-17
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

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces Pthreads with the prime-sieve example.
- [[dis-3-6-gdb-pthreads]] — *Dive into Systems* Ch 3.6: Pthreads' first sighting in DIS, in the context of [[GDB]] thread-aware debugging. Full Pthreads coverage deferred to DIS Ch 14.
- [[OpenMP]] — higher-level pragma-based alternative built on the same threading substrate.
- [[CriticalSection]] — the lock pattern Pthreads makes explicit via `pthread_mutex_*`.
- [[Mutex]] — `pthread_mutex_t` is the canonical mutex implementation.
- [[Barrier]] — `pthread_barrier_wait` is Pthreads' barrier primitive.
- [[Thread]] — the abstraction Pthreads instantiates.
- [[SharedMemoryArchitecture]] — Pthreads' execution model.
- [[GDB]] / [[GdbInfoThreads]] / [[GdbThreadSwitch]] / [[GdbThreadApply]] — the [[GDB]] thread-debugging command surface that reflects over Pthreads state.
