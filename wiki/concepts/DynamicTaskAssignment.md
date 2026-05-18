---
title: "Dynamic Task Assignment"
type: concept
tags: [parallel-computing, scheduling]
sources: [parproc-ch02-recurring-performance-issues]
last_updated: 2026-05-17
---

# Dynamic Task Assignment

A task-scheduling strategy in which **processors determine their tasks as the computation proceeds**, typically by pulling work from a shared queue. Contrasted with [[StaticTaskAssignment]], where the assignment is decided at the outset.

## Implementations

[[parproc-ch02-recurring-performance-issues]] §2.4 describes three flavors:

1. **Task farm** — a shared queue of pending task IDs (e.g., the numbers 0..9999 representing matrix rows). Each thread, on finishing a task, removes the next ID from the queue and processes it.
2. **Atomic counter** (Method B) — a shared `nextchunk` variable. Each thread does an atomic fetch-and-increment to claim its next chunk. This is OpenMP's `schedule(dynamic)` policy.
3. **Guided schedule** — OpenMP's `schedule(guided)`. Large chunks early (low communication overhead while there's plenty of work) shrinking to small chunks late (fine-grained balancing as the queue empties).

A peer-to-peer variant, **[[WorkStealing|work stealing]]** (§2.4.4, [[Cilk]]'s approach), replaces the shared queue with per-thread local deques; idle threads steal from busy peers.

## The intuitive appeal

The naïve intuition: dynamic assignment is more flexible than [[StaticTaskAssignment|static]], so it should be better. If one thread happens to draw a chunk of fast tasks, it can pick up more work; meanwhile a thread with slow tasks doesn't hold the others up.

## Why the intuition fails (chapter's punchline)

[[parproc-ch02-recurring-performance-issues]] §2.4: *"It would at first seem that dynamic assignment is more efficient, as it is more flexible. However, accessing the task farm, for instance, entails communication costs, which might be very heavy. In this section, we will show that it's typically better to use the static approach, though possibly randomized."*

Two specific costs:
- **Lock contention on the shared counter / queue head.** Each task-acquisition is a serialized critical section.
- **Cache coherence traffic.** Every update to the shared counter invalidates that cache line on every other core.

Combined with the $O(1/\sqrt{m})$ chunk-time concentration argument (chunks of i.i.d. tasks have near-constant total time), the flexibility dynamic assignment offers turns out to balance nothing the static-with-large-chunks approach hasn't already balanced for free.

## When dynamic is genuinely warranted

The chapter is not absolute about it — §2.4.3 final paragraph: *"On the other hand, if we know beforehand that all of the tasks should take about the same time, we should use static scheduling, as it might yield better cache and virtual memory performance."* The implicit converse: when per-task times are highly variable and *not* well-modeled as i.i.d. (heavy-tailed, data-dependent recursion, irregular task graphs), dynamic or work-stealing schedulers can still win.

## Mandelbrot timings (from the chapter)

| Policy | Time (s) |
|---|---|
| `static` | 47.8 |
| **`dynamic`** | **21.4** |
| `guided` | 29.6 |
| `random` (static!) | 15.7 |

Dynamic does beat naïve contiguous-static on Mandelbrot. But it loses to *randomized* static by 26%.

## Connections

- [[parproc-ch02-recurring-performance-issues]] — primary source, §2.4.
- [[StaticTaskAssignment]] — the foil; the chapter's preferred default.
- [[WorkStealing]] — peer-to-peer variant ([[Cilk]]).
- [[LoadBalancing]] — what dynamic assignment is trying to optimize.
- [[CommunicationBottleneck]] — what dynamic assignment pays.
- [[OpenMP]] — exposes `dynamic` and `guided` schedules.
