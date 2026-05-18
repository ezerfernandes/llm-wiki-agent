---
title: "Fully Associative Cache"
type: concept
tags: [cache, memory-hierarchy, systems, hardware, architecture]
sources: [dis-11-4-caching]
last_updated: 2026-05-17
---

# Fully Associative Cache

A **fully associative cache** is the maximum-flexibility [[CacheMemory|cache]] placement architecture: **any memory address can occupy any [[CacheLine|cache line]]**. Lookup must compare the requested tag against **every line in the cache in parallel**. Maximum hit-rate potential but impractical hardware cost for general-purpose caches — *"generally unfit for a general-purpose CPU cache"* ([[dis-11-4-caching|DIS Ch 11.4]]).

## Lookup mechanism ([[dis-11-4-caching|DIS Ch 11.4]])

There is **no index field** in the address decomposition — only tag + offset. Lookup is:

1. The **tag** is broadcast to **every** cache line.
2. **All lines compare their tag in parallel** (one comparator per line).
3. **At most one** line can match (caches enforce one-copy invariants); that line's offset bytes are returned on a [[CacheHit|hit]].
4. No match → [[CacheMiss|miss]]: fetch, install in any line per the [[CacheReplacementPolicy|replacement policy]].

## Trade-offs

**Advantages**:
- **Zero conflict misses** by construction — placement is unconstrained, so any cache space can absorb any incoming block.
- Approaches the theoretical hit-rate ceiling for a given total capacity.

**Fatal weakness — lookup cost scales with cache size**:
- A cache with K lines needs K parallel tag comparators.
- K ≈ thousands for L1, hundreds of thousands for L3 — wholly impractical.
- Comparator network depth gates cycle time; full associativity blows the L1 budget by orders of magnitude.

## Where fully associative survives

Despite being impractical for the main data caches, fully associative designs persist where the structure is **small enough** that K parallel comparators is affordable:

- **[[TLB|Translation Lookaside Buffers]]** — typically 32–64 entries; full associativity is feasible and conflict misses are catastrophic ([[VirtualMemory|VM]] page-walk fallback is hugely expensive).
- **Branch target buffers** (some designs) — small, hot, conflict-sensitive.
- **Victim caches** — small overflow caches that catch direct-mapped evictions.
- **L1 micro-op caches** — short, highly conflict-sensitive.

## Connections

- [[CacheMemory]] — the parent storage tier.
- [[CacheLine]] — the unit; any line can hold any address.
- [[DirectMappedCache]] / [[SetAssociativeCache]] — the lower-flexibility placement architectures.
- [[CacheReplacementPolicy]] / [[LeastRecentlyUsed]] — required (any line is a candidate eviction target).
- [[TLB]] — the canonical use case for full associativity in a real CPU.
- [[CacheMiss]] — fully associative eliminates conflict misses; compulsory and capacity misses remain.
