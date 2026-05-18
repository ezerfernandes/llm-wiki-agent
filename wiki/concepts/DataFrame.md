---
title: "DataFrame"
type: concept
tags: [pandas, datastructure, tabular]
sources: [pydata-pandas-basics, pydata-data-wrangling, pydata-data-aggregation, pydata-time-series]
last_updated: 2026-05-15
---

# DataFrame

The central pandas data structure: a column-oriented 2-D table with both row and column labels. Each column is a [[Series]] sharing a common row [[pandasIndex|Index]]. Modeled after R's `data.frame` but generalized — DataFrame columns can have different dtypes, and either axis can be a [[HierarchicalIndexing|MultiIndex]].

## Construction
```python
pd.DataFrame({"x0": [1,2,3], "x1": [0.1, 0.2, 0.3]})   # dict of lists
pd.DataFrame(records)                                   # list of dicts
pd.DataFrame(np.zeros((3, 4)), columns=list("abcd"))    # ndarray + column labels
```

## Access patterns
- `df[col]` / `df.col` — column access (latter is read-only attribute).
- `df.loc[row, col]` — label-based selection (both axes).
- `df.iloc[i, j]` — positional selection.
- `df[df.x > 0]` — boolean mask on rows.

## Common ops
- `head` / `tail` / `info` / `describe` / `dtypes`.
- `apply` (function over an axis) / `.map` (element-wise) / `.transform` (group-preserving).
- IO via `pd.read_*` / `df.to_*`.
- Joins (`pd.merge` / `df.join`) and concatenation (`pd.concat`).
- Reshape (`stack` / `unstack` / `pivot` / `pivot_table` / `melt`).
- Groupby ([[SplitApplyCombine]]).

## Connections
- [[pandas]] — provided by.
- [[Series]] — column type.
- [[pandasIndex]] — labels both axes.
- [[HierarchicalIndexing]] — multi-level row or column labels.
- [[Rlanguage]] — `data.frame` is the inspiration.
