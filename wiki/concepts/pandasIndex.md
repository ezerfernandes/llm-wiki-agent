---
title: "pandas Index"
type: concept
tags: [pandas, datastructure]
sources: [pydata-pandas-basics, pydata-data-wrangling, pydata-time-series]
last_updated: 2026-05-15
---

# pandas Index

Immutable labeled axis attached to every [[Series]] and to each axis of a [[DataFrame]]. Enables label-based selection (`.loc`), automatic alignment in arithmetic, and join semantics. Mutating an Index requires creating a new one (`s.index = new` works because the new object replaces the old, not because Index is mutable).

## Index types
- `Index` — generic, object dtype.
- `RangeIndex` — memory-efficient default for `0..N-1`.
- `Int64Index`, `Float64Index`, `UInt64Index` — typed numeric (largely subsumed by generic `Index` in modern pandas).
- `DatetimeIndex` — timestamps with optional time zone.
- `PeriodIndex` — fixed periods (month, quarter, year, …).
- `TimedeltaIndex` — durations.
- `CategoricalIndex` — finite-set labels.
- `MultiIndex` — hierarchical, multiple levels per axis (see [[HierarchicalIndexing]]).

## Connections
- [[Series]] / [[DataFrame]] — host data structures.
- [[HierarchicalIndexing]] — MultiIndex.
- [[Resampling]] — uses `DatetimeIndex` / `PeriodIndex`.
- [[pydata-pandas-basics]] — chapter 5 introduces.
