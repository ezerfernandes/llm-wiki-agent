---
title: "Working Set"
type: concept
tags: [systems, cache, memory, locality]
sources: [dis-11-3-locality]
last_updated: 2026-05-17
---

# Working Set

The **working set** of a program at a given point in time is the subset of memory the program is actively referencing — the items currently benefiting from [[TemporalLocality|temporal]] and [[SpatialLocality|spatial locality]]. The working-set framing is the underlying mechanism that makes the [[MemoryHierarchy|memory hierarchy]] effective: as long as the working set fits in a fast tier (registers / [[CacheMemory|cache]] / [[RAM]]), the program runs at the speed of that tier rather than at the speed of the slower tiers behind it.

## The DIS framing (Ch 11.3 desk/bookshelf/library analogy)

[[dis-11-3-locality|DIS Ch 11.3]] uses a desk-bookshelf-library analogy to motivate the working-set concept:

| Tier | Analogy | Reality |
|---|---|---|
| Desk (limited, fast) | Books currently in use | [[CpuRegister|Registers]] + [[CacheMemory|cache]] |
| Bookshelf | Books used occasionally | [[RAM|Main memory]] |
| Library | Books rarely needed | Disk / secondary storage |

The desk has a small, fixed capacity. Keeping frequently-used books on the desk keeps retrieval costs low. When the desk fills, the **least-recently-used** book is moved back to the bookshelf — the working-set boundary is enforced by [[LeastRecentlyUsed|LRU]]-style replacement.

## Why working set matters

- **If working set ⊂ cache size** — program runs at cache speed; cache hits dominate.
- **If working set > cache size** — program *thrashes* the cache; every access pays the full miss cost. This is the classic regime where adding more cores or more clock speed gives little benefit — the bottleneck is memory traffic, not compute.
- **If working set > RAM size** — the OS pages to disk and the program runs orders of magnitude slower.

## Connections to program design

- **[[TemporalLocality|Temporal locality]]** keeps the working set *small in count* — reusing the same items concentrates references.
- **[[SpatialLocality|Spatial locality]]** keeps the working set *small in span* — accessing nearby items means a few [[CacheLine|cache lines]] cover many references.
- **Loop tiling / cache blocking** — restructure nested loops so each tile's working set fits in cache before moving to the next tile (canonical matrix-multiplication optimization).
- **Data layout choices** — [[RowMajorOrder|row-major]] traversal of C arrays keeps the per-iteration working set to a small number of [[CacheLine|cache lines]].

## Connections

- [[LocalityOfReference]] — umbrella; working set is the property locality controls the *size* of.
- [[TemporalLocality]] / [[SpatialLocality]] — the two locality axes that determine working-set count and span.
- [[CacheMemory]] / [[CacheLine]] — the fast tier whose effectiveness depends on working set fitting inside it.
- [[MemoryHierarchy]] — the working set is the property that decides *which tier* dominates a program's effective speed.
- [[dis-11-3-locality]] — primary DIS source (desk-bookshelf-library analogy).
