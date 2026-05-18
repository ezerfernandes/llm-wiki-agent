---
title: "Extension Data Types"
type: concept
tags: [pandas, dtype, missing-data]
sources: [pydata-data-cleaning]
last_updated: 2026-05-15
---

# Extension Data Types

pandas extension arrays / dtypes (since 1.0) that go beyond what NumPy can express natively. Most important capability: **integer + boolean + string columns with proper missing-data support** (no need to coerce to float64 just to host a NaN). Marked by capitalized dtype names — `Int64`, `Int32`, `UInt8`, `Float64`, `boolean`, `string`, plus `category` ([[CategoricalData]]) and `datetime64[ns, tz]`.

## Why
NumPy `int64` has no NaN slot — a missing value forces the whole column to float64 (which has NaN). Extension dtypes carry a separate validity mask, so an `Int64` Series can contain integers *and* `pd.NA`.

## Usage
```python
s = pd.array([1, 2, None, 4], dtype="Int64")
df["col"] = df["col"].astype("string")
df["nullable_bool"] = df["bool_col"].astype("boolean")
```

## Connections
- [[pandas]] — provider.
- [[CategoricalData]] — most prominent extension type, with its own chapter section.
- [[pydata-data-cleaning]] — chapter 7 introduces them.
