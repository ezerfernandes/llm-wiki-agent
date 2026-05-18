---
title: "Python for Data Analysis 3E — Ch.5: Getting Started with pandas"
type: source
tags: [book, pandas, dataframe, series, pydata]
date: 2026-05-15
source_file: raw/pydata-book-web/pandas-basics.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/pandas-basics.html
chapter: 5
---

## Summary
Primer on the two workhorse [[pandas]] data structures — [[Series]] (1D labeled array) and [[DataFrame]] (2D tabular, column-oriented, labeled rows + columns) — and [[pandasIndex|Index objects]]. Covers reindexing, dropping entries, indexing / selection / filtering, arithmetic with data alignment, function application (`apply`, `map`, `applymap`), sorting and ranking, descriptive statistics, correlation/covariance, and `unique`/`value_counts`/`isin`.

## Key Claims
- **Series** — 1D array-like with an associated index (default `RangeIndex(0..N-1)`); `s.array` returns a `PandasArray` (NumPy-backed by default; can be an extension array). Constructable from list, dict (keys become index), scalar+index.
- **DataFrame** — column-oriented table; each column is a Series; shared row index. Construct from dict of equal-length lists / arrays, dict of Series, list of dicts, 2D ndarray. `df.head()`, `df.tail()`, `df.info()`, `df.describe()`, `df.values` (NumPy), `df.to_numpy()`.
- **Index objects** — immutable; can be shared between Series/DataFrame; index types include `Index`, `RangeIndex`, `DatetimeIndex`, `PeriodIndex`, `CategoricalIndex`, `MultiIndex` (hierarchical, see Ch.8).
- **Reindexing** — `reindex` conforms data to a new index, filling missing with `NaN` (override via `fill_value=` or `method="ffill"`).
- **Selection** — label-based `df.loc[row, col]`, position-based `df.iloc[i, j]`; column access `df["col"]` or `df.col` (read-only attribute access); boolean masks: `df[df["x"] > 0]`.
- **Arithmetic with data alignment** — operations on objects with different indexes produce a union index; missing pairs become `NaN`. Override via `df.add(other, fill_value=0)` etc.
- **Function application** — element-wise via Series `.map(func)` / DataFrame `.map(func)` (formerly `applymap`); axis-wise reductions via `df.apply(func, axis=...)`.
- **Sorting** — `sort_index`, `sort_values(by=...)`; `rank(method="average"/"min"/"max"/"first"/"dense")` for tie-breaking ranks.
- **Descriptive statistics** — `sum`, `mean`, `median`, `min`, `max`, `idxmin`, `idxmax`, `var`, `std`, `quantile`, `cumsum`, `cummax`, `pct_change`; default `skipna=True`.
- **Correlation / covariance** — `s.corr(s2)`, `df.corr()`, `df.cov()`; pairwise correlations via `df.corrwith(other)`.
- **Unique / counts / membership** — `s.unique()`, `s.value_counts(sort=True)`, `s.isin([...])`, `pd.value_counts`, `pd.Index.get_indexer`.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[pandas]] — the central library.
- [[Series]] / [[DataFrame]] — the two foundational data structures.
- [[pandasIndex]] — labels for axes.
- [[NumPy]] — pandas inherits much of its semantics.
- [[pydata-accessing-data]] — chapter 6 next: load DataFrames from files / DBs / APIs.

## Contradictions
- None.
