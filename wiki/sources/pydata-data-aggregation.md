---
title: "Python for Data Analysis 3E — Ch.10: Data Aggregation and Group Operations"
type: source
tags: [book, pandas, groupby, aggregation, split-apply-combine, pydata]
date: 2026-05-15
source_file: raw/pydata-book-web/data-aggregation.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/data-aggregation.html
chapter: 10
---

## Summary
The [[SplitApplyCombine|split-apply-combine]] paradigm (term coined by [[HadleyWickham]]) implemented in pandas as `DataFrame.groupby`. Covers grouping keys, iteration, column subsetting, dictionary/Series/function-based grouping, by index level, aggregation (built-in agg names + custom + multi-function), unindexed result via `as_index=False`, the general `apply`, transformations (`transform`), `pivot_table`, `crosstab`.

## Key Claims
- **Group keys** — array of same length as axis, column name(s), dict / Series mapping labels → groups, or callable on the index. Pass via `df.groupby(keys)`.
- **GroupBy object** is lazy — no computation until an action (`mean`, `sum`, `apply`, etc.) is invoked. Iterable as `for name, group in grouped:`.
- **Aggregation** — built-ins (`mean`, `sum`, `count`, `nunique`, `std`, `var`, `min`, `max`, `first`, `last`, `quantile`, `median`); `grouped.agg("mean")` or `grouped.agg([np.mean, "std"])`; per-column dict: `grouped.agg({"col1": "mean", "col2": ["min", "max"]})`.
- **as_index** — `df.groupby(keys, as_index=False).agg(...)` keeps keys as columns instead of a MultiIndex.
- **apply** — most general operation. `grouped.apply(func)` applies a function to each group's DataFrame; results stitched together. Func can return scalar / Series / DataFrame.
- **transform** — returns an object of the same shape as input, with each row replaced by the result of the function applied to its group. Used for normalization: `df["z"] = grouped["x"].transform(lambda s: (s - s.mean()) / s.std())`.
- **Examples in chapter** — filling missing values with group means; weighted average; group-wise linear regression via `apply`; random sampling per group.
- **Quantile / bucket analysis** — `pd.qcut(...)` + `groupby` to compute stats per quantile bin.
- **Pivot table** — `df.pivot_table(values=, index=, columns=, aggfunc="mean", fill_value=, margins=True)`.
- **Crosstab** — `pd.crosstab(rows, cols, margins=True)` for frequency tables (special case of `pivot_table` with `aggfunc="count"`).
- **Time-based groupby** is covered separately as **resampling** in Ch.11.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[SplitApplyCombine]] — Wickham's organizing concept.
- [[HadleyWickham]] — R author who coined the term.
- [[pandas]] — groupby implementation.
- [[pydata-time-series]] — chapter 11 covers groupby's time-flavored cousin (`resample`).

## Contradictions
- None.
