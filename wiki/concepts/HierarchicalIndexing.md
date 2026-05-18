---
title: "Hierarchical Indexing (MultiIndex)"
type: concept
tags: [pandas, datastructure]
sources: [pydata-data-wrangling, pydata-data-aggregation]
last_updated: 2026-05-15
---

# Hierarchical Indexing (MultiIndex)

A pandas index with multiple levels per axis — lets a 2-D DataFrame represent higher-dimensional data without resorting to N-D arrays. Either rows or columns can carry a `MultiIndex` (or both).

## Construction
```python
pd.MultiIndex.from_arrays([["a","a","b"], [1,2,1]], names=["k1", "k2"])
pd.MultiIndex.from_tuples([("a",1),("a",2),("b",1)])
pd.MultiIndex.from_product([["a","b"], [1,2]])
df.set_index(["k1", "k2"])     # promote columns to MultiIndex
```

## Operations
- **Partial indexing** — `s["a"]`, `s["a":"c"]`; `df.loc[("a", 1)]`.
- **Level access** — `df.xs("a", level="k1")`, `df.groupby(level=0)`.
- **Stack / unstack** pivots a level between rows and columns.
- **swaplevel** / **sort_index(level=)** — reorder levels.

## Connections
- [[pandas]] / [[DataFrame]] / [[Series]] — host data structures.
- [[pandasIndex]] — base index type.
- [[SplitApplyCombine]] — groupby on levels uses MultiIndex.
- [[pydata-data-wrangling]] — chapter 8 covers depth.
