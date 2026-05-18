---
title: "Split-Apply-Combine"
type: concept
tags: [pandas, groupby, paradigm, statistics]
sources: [pydata-data-aggregation]
last_updated: 2026-05-15
---

# Split-Apply-Combine

Organizing pattern for group operations on tabular data — coined by [[HadleyWickham]] in his 2011 *Journal of Statistical Software* paper. Three phases:

1. **Split** — partition the data along one or more keys (column values, dict mapping, function on index, or array of group labels).
2. **Apply** — run a function on each group's data. Three flavors:
   - *Aggregate*: group → scalar (`mean`, `sum`, `count`, custom).
   - *Transform*: group → same-shape replacement (normalization, lag, rank).
   - *Filter*: group → boolean (keep / drop the whole group).
3. **Combine** — stitch the per-group results back into a single output indexed by group keys (and original row labels for transforms).

## pandas implementation
- `df.groupby(keys).agg(...)` — aggregate.
- `df.groupby(keys).transform(...)` — transform.
- `df.groupby(keys).filter(...)` — filter.
- `df.groupby(keys).apply(func)` — fully general; func may return scalar / Series / DataFrame.

## Connections
- [[HadleyWickham]] — coined the term.
- [[pandas]] / [[DataFrame]] — implements via `groupby`.
- [[Resampling]] — time-flavored special case (`df.resample("M").mean()`).
- [[Rlanguage]] — `plyr` / `dplyr` are the R-side implementations.
