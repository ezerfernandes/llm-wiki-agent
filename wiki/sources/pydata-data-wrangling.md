---
title: "Python for Data Analysis 3E — Ch.8: Data Wrangling: Join, Combine, and Reshape"
type: source
tags: [book, pandas, join, merge, reshape, multiindex, pydata]
date: 2026-05-15
source_file: raw/pydata-book-web/data-wrangling.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/data-wrangling.html
chapter: 8
---

## Summary
[[HierarchicalIndexing]] (MultiIndex) for representing higher-dimensional data in 2D form; database-style joins (`pd.merge`); concatenation (`pd.concat`); patching with `combine_first`; pivot and reshape between long and wide formats (`stack` / `unstack` / `pivot` / `pivot_table` / `melt`).

## Key Claims
- **MultiIndex** — `pd.MultiIndex.from_arrays`/`from_tuples`/`from_product`; multi-level index on rows or columns lets a 2D DataFrame represent N-dimensional data. Partial indexing via `s["a"]`, `s["a":"c"]`, `df.loc[(outer, inner)]`.
- **Stack / Unstack** — `df.stack()` pivots columns into a row-level index (wide → long); `df.unstack(level=...)` pivots a row level into columns. Missing combinations become NaN unless `fill_value=` given.
- **set_index / reset_index** — `df.set_index([col1, col2])` promotes columns to row index; `df.reset_index()` does the inverse.
- **merge** — `pd.merge(left, right, on=, how="inner"/"left"/"right"/"outer"/"cross", left_on=, right_on=, suffixes=)`; SQL-style joins on shared key columns. `validate="one_to_one"` etc to assert cardinality.
- **merge on index** — `pd.merge(left, right, left_on="key", right_index=True)`; or `df.join(other, on=, how=)`.
- **concat** — `pd.concat([a, b], axis=0/1, keys=[...], ignore_index=True/False, join="inner"/"outer")`. Vertical or horizontal stacking, optional outer-product index.
- **combine_first** — `a.combine_first(b)`: take values from `a`, fill missing from `b`. Equivalent of SQL COALESCE.
- **pivot** — `df.pivot(index=, columns=, values=)`: long-to-wide reshape; one row per `index`, one column per `columns` value.
- **pivot_table** — like `pivot` but supports duplicate keys via aggregation (`aggfunc="mean"` default; pass list for multi-stats); `margins=True` adds row/column totals.
- **melt** — `pd.melt(df, id_vars=, value_vars=, var_name=, value_name=)`: wide-to-long inverse of `pivot`. Each non-id column becomes a row.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[pandas]] — join / reshape API.
- [[HierarchicalIndexing]] — MultiIndex backbone.
- [[DataFrame]] — operations on the central object.
- [[pydata-plotting-and-visualization]] — chapter 9 next.

## Contradictions
- None.
