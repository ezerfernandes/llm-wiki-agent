---
title: "Dive into Systems — Ch 11.4 Caching"
type: source
tags: [textbook, systems, cache, memory-hierarchy, dis]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C11-MemHierarchy/caching.html
---

## Summary

**Fourth leaf of Ch 11 *The Memory Hierarchy*** of *[[DiveIntoSystems]]* — operationalizes [[dis-11-3-locality|Ch 11.3]]'s [[LocalityOfReference|locality]] property into a concrete hardware design: the **CPU [[CacheMemory|cache]]**. Answers the three structural questions every cache architect must resolve — *which* subset of main memory to hold, *when* to transfer data between cache and memory, and *how* to determine whether a requested datum is present. Introduces the **[[CacheLine|cache line]]** as the unit of storage, the **tag/index/offset** address decomposition, three placement architectures ([[DirectMappedCache|direct-mapped]] / [[SetAssociativeCache|set associative]] / [[FullyAssociativeCache|fully associative]]), the **[[LeastRecentlyUsed|LRU]]** replacement policy, the **[[WriteThroughCache|write-through]] vs [[WriteBackCache|write-back]]** write-policy split, and the **3C miss taxonomy** (compulsory / capacity / conflict). **109th ingested DIS chapter — fourth leaf of Ch 11.**

## Key Claims

- **Caches exploit [[LocalityOfReference|locality]] to hide [[RAM|main-memory]] latency.** Hardware sends each memory address simultaneously to the [[CacheMemory|cache]] and to [[RAM|main memory]]; the cache responds faster, so when data is present (a **[[CacheHit|cache hit]]**) the CPU never waits for RAM. On a **[[CacheMiss|cache miss]]**, the CPU stalls for the RAM access, then loads the retrieved block into the cache so that *"subsequent requests for the same address... can be serviced quickly"* — the mechanism that converts [[TemporalLocality|temporal locality]] into a hit-rate.
- **Cache storage is organized into [[CacheLine|cache lines]].** Each cache line holds (a) a **cache data block** — a multibyte chunk of consecutive program data, typically **16–64 bytes** — and (b) **metadata**: a **valid bit**, a **tag** identifying which memory region the block represents, and (for [[WriteBackCache|write-back]] caches) a **dirty bit**. The block size is the granularity at which the hardware exploits [[SpatialLocality|spatial locality]]: *"cache designers balance a trade-off in choosing a cache's block size"* between block-count diversity and spatial-locality payoff.
- **Memory addresses decompose into tag + index + offset.** The **offset** (low bits) selects a byte within the block; the **index** (middle bits) selects the cache line (or set); the **tag** (high bits) identifies which memory region currently occupies that line. Using **middle bits** for the index — not high bits — is deliberate: *"caches spread data more evenly among the available cache lines"*, otherwise nearby variables would cluster into the same line.
- **Three placement architectures, increasing flexibility.**
  - **[[DirectMappedCache|Direct-mapped]]** — each memory address maps to **exactly one** cache line. Simplest lookup (index → line, check valid, check tag, extract offset bytes) but suffers most from **conflict misses** when multiple hot addresses map to the same line.
  - **[[SetAssociativeCache|Set associative]]** — each address maps to a **set** containing **N lines** (typically N = 2–8); the lookup checks all N tags in parallel. *"Offers a good compromise between complexity and conflicts."* The dominant design in modern CPU caches.
  - **[[FullyAssociativeCache|Fully associative]]** — any address can occupy any line; maximum flexibility but lookup must check every tag in parallel. *"Generally unfit for a general-purpose CPU cache"* — reserved for tiny structures like [[TLB|TLBs]].
- **[[LeastRecentlyUsed|LRU]] is the standard replacement policy.** When a set is full and a new line must be installed, the **least-recently-used** line is evicted — leveraging [[TemporalLocality|temporal locality]]: *"recently used data is likely to be used again."* Tracking LRU requires extra metadata bits per set (roughly `log2(N)` bits for an N-way set).
- **Two write policies, opposite trade-offs.**
  - **[[WriteThroughCache|Write-through]]** — every write updates both cache and memory simultaneously. Simple, no dirty bit needed, but pays main-memory latency on every store.
  - **[[WriteBackCache|Write-back]]** — writes update only the cache; the line is marked dirty; the dirty data is written to memory only on **eviction**. *"Amortizing the cost of a memory access across many writes significantly improves performance"* — the dominant policy in modern caches.
- **Three causes of cache misses (the 3C model).**
  - **Compulsory (cold) miss** — first access to a block never previously seen; unavoidable.
  - **Capacity miss** — the program's [[WorkingSet|working set]] exceeds total cache capacity; the line was evicted because the cache is too small.
  - **Conflict miss** — the line was evicted because **placement restrictions** forced contention even though cache space was available elsewhere — the miss class [[SetAssociativeCache|set associative]] designs are built to attack.
- **Set-associative design eliminates conflict misses on patterns that defeat direct-mapped.** The chapter's worked example walks the **same access trace** through a [[DirectMappedCache|direct-mapped]] cache (2 conflict misses) and a **two-way [[SetAssociativeCache|set-associative]]** cache of the same total size (**zero conflict misses**) — demonstrating that associativity converts conflict misses into hits at the cost of parallel tag comparison.

## Key Quotes

> "When the request to main memory completes, the CPU loads the retrieved data into the cache so that subsequent requests for the same address... can be serviced quickly." — the locality-to-hit-rate conversion mechanism.

> "Cache designers balance a trade-off in choosing a cache's block size." — the spatial-locality / block-diversity trade.

> "Using bits from the middle of the address, caches spread data more evenly among the available cache lines." — design rationale for middle-bit indexing.

> "[Set associative] offers a good compromise between complexity and conflicts." — the dominant modern design point.

> "Recently used data is likely to be used again." — the [[TemporalLocality|temporal-locality]] axiom that justifies [[LeastRecentlyUsed|LRU]] eviction.

> "Amortizing the cost of a memory access across many writes significantly improves performance." — why [[WriteBackCache|write-back]] dominates modern caches.

## Connections

- [[DiveIntoSystems]] — Ch 11.4 is the **fourth leaf of Ch 11 *The Memory Hierarchy*** — **109th ingested DIS chapter**, following [[dis-11-3-locality|Ch 11.3 *Locality*]] (108th). Operationalizes the [[LocalityOfReference|locality]] property of 11.3 into the concrete cache-design mechanism.
- [[dis-11-3-locality]] — prior leaf; 11.3 supplied the [[TemporalLocality|temporal]] / [[SpatialLocality|spatial]] property; 11.4 supplies the **hardware that exploits it**. [[LeastRecentlyUsed|LRU]] eviction is the [[TemporalLocality|temporal-locality]] payoff; [[CacheLine|block-granularity fetch]] is the [[SpatialLocality|spatial-locality]] payoff.
- [[dis-11-2-storage-devices]] — supplied the [[SRAM]] / [[DRAM]] latency gap (~5 ns vs ~100 ns) that motivates the cache layer. 11.4 specifies *how* that gap is hidden.
- [[dis-11-1-memory-hierarchy]] — opening leaf of Ch 11; explicitly deferred *Caching* to 11.4, now delivered.
- [[LocalityOfReference]] — the umbrella property; **[[CacheLine|cache lines]] + [[LeastRecentlyUsed|LRU]] + tag-indexed storage** are the three mechanisms by which hardware extracts performance from this property.
- [[CacheMemory]] — expanded in place: 11.4 adds the **internal organization** (lines / sets / tag / index / offset / valid / dirty) on top of the existing *small fast on-chip storage* framing.
- [[CacheLine]] — **new concept page** — the unit of cache storage (data block + metadata).
- [[CacheHit]] — **new concept page** — request satisfied from cache; fast path.
- [[CacheMiss]] — **new concept page** — request not in cache; stalls for main-memory access; 3C taxonomy.
- [[CacheReplacementPolicy]] — **new concept page** — eviction-target selection on a full set; [[LeastRecentlyUsed|LRU]] is the canonical policy.
- [[LeastRecentlyUsed]] — **new concept page** — the [[TemporalLocality|temporal-locality]]-driven replacement policy that dominates modern caches.
- [[DirectMappedCache]] — **new concept page** — one-line-per-address; simplest; highest conflict-miss rate.
- [[SetAssociativeCache]] — **new concept page** — N lines per set; the modern compromise; the dominant CPU-cache design.
- [[FullyAssociativeCache]] — **new concept page** — any-line-any-address; max flexibility; impractical at general-CPU scale; lives in [[TLB|TLBs]].
- [[WriteThroughCache]] — **new concept page** — simple write policy; updates cache + memory atomically; no dirty bit.
- [[WriteBackCache]] — **new concept page** — modern dominant write policy; updates cache only; writes back on eviction; dirty-bit metadata.
- [[CacheLevel]] — the L1 / L2 / L3 stratification from [[dis-11-1-memory-hierarchy|Ch 11.1]]; each level uses these placement / replacement / write architectures independently.
- [[CacheCoherency]] — coherence between caches across cores is the [[dis-11-6-caching-on-multicore]] follow-on topic (not in 11.4); [[WriteBackCache|write-back]] caches make coherence harder than [[WriteThroughCache|write-through]].
- [[TemporalLocality]] / [[SpatialLocality]] — the two locality axes from [[dis-11-3-locality|Ch 11.3]] that motivate [[LeastRecentlyUsed|LRU]] (temporal) and [[CacheLine|block-granularity fetch]] (spatial).
- [[WorkingSet]] — when working set fits in cache → capacity misses absent; when it overflows → capacity misses dominate. The cache-sizing target.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.

## Contradictions

None. Ch 11.4's three-architecture taxonomy ([[DirectMappedCache|direct-mapped]] / [[SetAssociativeCache|set-associative]] / [[FullyAssociativeCache|fully associative]]) matches the [[CacheMemory]] / [[CacheCoherency]] treatment from [[parproc-appA-systems-issues|ParProc App A]] and [[parproc-ch03-shared-memory-parallelism|ParProc Ch 3]]; [[DiveIntoSystems|DIS]] adds the **tag/index/offset decomposition** and the **3C miss taxonomy** not previously surfaced in the wiki.
