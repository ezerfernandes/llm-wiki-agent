---
title: "Dive into Systems — Ch 14.3.1 Mutex"
type: source
tags: [book, textbook, dive-into-systems, pthreads, mutex, synchronization, concurrency]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C14-SharedMemory/mutex.html
---

## Summary

Chapter 14.3.1 of *[[DiveIntoSystems]]* — **first sub-leaf** of [[dis-14-3-synchronization|Ch 14.3 *Synchronizing Threads*]]. Operationalizes the [[CriticalSection|critical-section]] concept from the parent hub into the canonical [[Pthreads]] primitive: the **[[Mutex|mutex]]** (**mut**ual **ex**clusion lock). Defines a mutex as *"a synchronization primitive that ensures only one thread executes code within a critical section at any given time, preventing data races on shared variables."* Codifies the **four-function API**: declaration `pthread_mutex_t mutex;` (typically global), initialization [[PthreadMutexInit|`pthread_mutex_init(&mutex, NULL)`]] (in `main` before thread creation), acquire/release pair [[PthreadMutexLock|`pthread_mutex_lock(&mutex)`]] / [[PthreadMutexUnlock|`pthread_mutex_unlock(&mutex)`]], and teardown [[PthreadMutexDestroy|`pthread_mutex_destroy(&mutex)`]] (after `pthread_join`-ing all workers). **Blocking semantics**: *"When a thread calls `pthread_mutex_lock()`, it gains exclusive access to the protected code. Any other thread attempting to acquire the same lock will block until the holding thread calls `pthread_mutex_unlock()`."* The serialization prevents concurrent access to shared data. **Lock-placement performance lesson** — the chapter's headline empirical claim: *"Simply wrapping entire loops with locks produces correct results but serializes execution, eliminating parallelism benefits. Conversely, locking on every iteration creates expensive overhead. Optimal strategy: use local thread-private variables to accumulate intermediate results without contention, then acquire the lock only once to update shared state."* DIS's measured payoff — **1.92 s (single thread) → 0.13 s (4 threads)** on the worked accumulator example, an effective speedup of ~15× across the dual axis (parallelism + lock-coarsening). **Deadlock risk surfaced**: *"Multiple interdependent locks can cause mutual blocking"* — DIS illustrates with a banking scenario where thread A holds lock X waiting for Y, thread B holds Y waiting for X. **130th ingested DIS chapter.** Mints **4 new concept pages** ([[PthreadMutexInit]], [[PthreadMutexLock]], [[PthreadMutexUnlock]], [[PthreadMutexDestroy]]); **extends [[Mutex]] in place** with the canonical Pthreads four-function API (currently the wiki's only Mutex coverage is the Embedded Rust `cortex_m::interrupt::Mutex` variant).

## Key Claims

- **[[Mutex|Mutex]] = critical-section serializer.** *"A synchronization primitive that ensures only one thread executes code within a critical section at any given time, preventing data races on shared variables."*
- **Four-function API**: [[PthreadMutexInit|`pthread_mutex_init(&mutex, NULL)`]] / [[PthreadMutexLock|`pthread_mutex_lock(&mutex)`]] / [[PthreadMutexUnlock|`pthread_mutex_unlock(&mutex)`]] / [[PthreadMutexDestroy|`pthread_mutex_destroy(&mutex)`]]. Declared as `pthread_mutex_t mutex;` (typically global so all worker [[ThreadFunction|thread functions]] see it).
- **Lock = blocking acquire.** *"`pthread_mutex_lock(&mutex)` — Acquires the lock; blocks if already held by another thread. `pthread_mutex_unlock(&mutex)` — Releases the lock, allowing other threads to acquire it."* The initial mutex state is unlocked.
- **Lock-placement is performance-load-bearing.** Three placement strategies, only the third gives speedup:
  - **Wrap entire loop** → correct but serial; eliminates parallelism benefit.
  - **Lock every iteration** → correct but lock overhead dominates.
  - **Thread-local accumulator + one final lock** → correct **and** fast: each thread accumulates into a private variable, acquires the lock once at the end to fold into shared state.
- **Empirical speedup** on DIS's accumulator example: **1.92 s (1 thread) → 0.13 s (4 threads)** — well above the 1/c=4× ideal, indicating the single-thread baseline was lock-contended.
- **Mutex must be released by the same thread that acquired it.** (Contrast with [[Semaphore|semaphores]] where any thread can post.)
- **[[Deadlock]] risk**: nested / interdependent locks can mutually block. Banking example — thread A: lock X → request Y; thread B: lock Y → request X; both freeze.
- **Lifecycle discipline**: initialize before `pthread_create`; destroy after `pthread_join`.

## Key Quotes

> *"A mutex is a synchronization primitive that ensures only one thread executes code within a critical section at any given time, preventing data races on shared variables."*

> *"Any other thread attempting to acquire the same lock will block until the holding thread calls `pthread_mutex_unlock()`."*

> *"Simply wrapping entire loops with locks produces correct results but serializes execution, eliminating parallelism benefits."*

## Worked Pattern — thread-local accumulator + final lock

```c
pthread_mutex_t mutex;
long global_sum = 0;

void *worker(void *id) {
    long local_sum = 0;
    for (int i = start; i < end; i++) {
        local_sum += compute(i);
    }
    pthread_mutex_lock(&mutex);
    global_sum += local_sum;
    pthread_mutex_unlock(&mutex);
    return NULL;
}

int main() {
    pthread_mutex_init(&mutex, NULL);
    /* spawn + join workers */
    pthread_mutex_destroy(&mutex);
}
```

## Connections

- [[DiveIntoSystems]] — Ch 14.3.1.
- [[dis-14-3-synchronization]] — parent hub; provides the [[CriticalSection]] / [[DataRace]] vocabulary this sub-leaf operationalizes.
- [[Mutex]] — extended in place with the Pthreads four-function API; DIS supplies the canonical CPU-side framing the wiki had been missing.
- [[Pthreads]] — the API surface.
- [[PthreadMutexInit]] / [[PthreadMutexLock]] / [[PthreadMutexUnlock]] / [[PthreadMutexDestroy]] — new concept pages, one per API call.
- [[CriticalSection]] — the abstraction the mutex implements.
- [[DataRace]] — the failure mode the mutex prevents.
- [[Deadlock]] — the failure mode mutex composition introduces (interdependent locks).
- [[Synchronization]] — umbrella.
- [[parproc-ch01-intro-parallel-processing]] — Matloff's prime-sieve introduces the same `pthread_mutex_lock`/`unlock` API.
- [[dis-14-2-posix]] — Pthreads thread-creation predecessor; supplies the `pthread_t` infrastructure mutexes ride alongside.

## Contradictions

None. DIS Ch 14.3.1 supplies the CPU-side Pthreads mutex API the wiki was carrying only via The Embedded Rust Book's `cortex_m::interrupt::Mutex` variant. The two are complementary: same word, different mechanism (blocking lock vs critical-section token).
