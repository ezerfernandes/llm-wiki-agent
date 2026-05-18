---
title: "Thread"
type: concept
tags: [parallel-computing, concurrency, os, shared-memory]
sources: [parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# Thread

The standard shared-memory unit of execution. [[parproc-ch01-intro-parallel-processing]] defines it operationally: "a *thread* is similar to a *process* in an operating system (OS), but with much less overhead." Crucially, "in the typical implementation, a thread is a special case of an OS process. But the key difference is that the various threads of a program share memory. (One can arrange for processes to share memory too in some OSs, but they don't do so by default.)"

Properties surveyed by the chapter:
- **On a uniprocessor**, "the threads of a program take turns executing, so that there is only an *illusion* of parallelism." On a multiprocessor, threads can genuinely run in parallel; "whenever a processor becomes available, the OS will assign some ready thread to it. So, among other things, this says that a thread might actually run on different processors during different turns."
- **Global vs local variables**: "although the global variables are shared, the locals are not. Recall that local variables are stored on a stack. Each thread (just like each process in general) has its own stack."
- **Communication via globals is the norm**: "in most threaded programs, all communication between threads is done via global variables." Matloff offers his own (linked) essay defending this against the "globals are evil" convention.
- **Cross-language ubiquity**: "Unix, Windows, Python, Java, Perl and now C++11 and R (via my [[Rdsm]] package) all support threaded programming."

Concrete APIs introduced in the chapter:
- [[Pthreads]] — POSIX threads, the low-level Unix-standardized API.
- C++11 `std::thread` — the language-standard interface.
- [[OpenMP]] — higher-level pragma layer that hides explicit thread management.
- [[Rdsm]] — quasi-threads for R via operator overloading.

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces the thread abstraction across multiple APIs.
- [[Process]] — the OS abstraction threads are a "special case" of.
- [[Pthreads]] / [[OpenMP]] / [[Rdsm]] — programming layers.
- [[CriticalSection]] — synchronization between threads.
- [[Barrier]] — coordination across threads.
- [[SharedMemoryArchitecture]] — the hardware substrate that makes threads efficient.
