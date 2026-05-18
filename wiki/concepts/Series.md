---
title: "Series"
type: concept
tags: [pandas, datastructure]
sources: [pydata-pandas-basics, pydata-data-cleaning, pydata-time-series]
last_updated: 2026-05-15
---

# Series

A pandas 1-D labeled array: a values array + an associated [[pandasIndex|Index]]. The simplest pandas data structure; conceptually a one-column [[DataFrame]] (and each DataFrame column is a Series).

## Construction
```python
s = pd.Series([4, 7, -5, 3])                              # default RangeIndex(0..3)
s = pd.Series([4, 7, -5, 3], index=["a", "b", "c", "d"])  # explicit labels
s = pd.Series({"a": 4, "b": 7})                           # dict → keys become index
```

## Key behaviors
- Vectorized arithmetic with data alignment by index.
- Missing data via NaN (or `pd.NA` for extension dtypes); operations skip NaN by default.
- `.array` exposes the underlying values as a `PandasArray` (NumPy-backed by default).
- `.index` exposes the labels; mutable rename via `s.index = new` but reindex via `s.reindex(new)` for safe shape changes.
- Boolean masks, label indexing (`.loc`), positional (`.iloc`).

## Connections
- [[pandas]] — provided by.
- [[DataFrame]] — Series is the column type.
- [[pandasIndex]] — labels axis.
- [[ExtensionDataTypes]] — Series can wrap nullable Int/Bool/String/Categorical arrays.
