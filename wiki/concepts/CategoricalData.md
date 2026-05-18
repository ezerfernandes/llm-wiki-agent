---
title: "Categorical Data"
type: concept
tags: [pandas, dtype, memory, performance]
sources: [pydata-data-cleaning]
last_updated: 2026-05-15
---

# Categorical Data

A pandas [[ExtensionDataTypes|extension type]] for low-cardinality string-or-label columns. Internally stores integer codes (the *positions* of each value into a separate `categories` array) plus the categories themselves. Two wins:

1. **Memory** — replacing repeated string values by `int8`/`int16` codes can shrink a column by 5–50×.
2. **Speed** — `groupby` / `value_counts` / sorting on a categorical column is faster (operates on integer codes).

## API
- `s = s.astype("category")` — convert.
- `s.cat.categories` — sorted unique category array.
- `s.cat.codes` — integer codes.
- `s.cat.set_categories([...])` — change category set (NaN for unmatched).
- `s.cat.as_ordered()` / `s.cat.as_unordered()` — ordinal vs nominal.
- `s.cat.rename_categories({...})` — rename in place.
- `s.cat.remove_unused_categories()` — clean up.

## Construction
```python
pd.Categorical(["a","b","a"], categories=["a","b","c"], ordered=True)
pd.cut(x, bins=...)         # returns a Categorical
pd.qcut(x, q=4)             # returns a Categorical
```

## Connections
- [[pandas]] — extension dtype.
- [[ExtensionDataTypes]] — broader family.
- [[Rlanguage]] — analogous to R's `factor`.
- [[pydata-data-cleaning]] — chapter 7 introduces.
