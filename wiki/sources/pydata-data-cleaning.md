---
title: "Python for Data Analysis 3E — Ch.7: Data Cleaning and Preparation"
type: source
tags: [book, pandas, missing-data, strings, regex, categorical, pydata]
date: 2026-05-15
source_file: raw/pydata-book-web/data-cleaning.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/data-cleaning.html
chapter: 7
---

## Summary
The "80%-of-an-analyst's-time" chapter. Missing data handling, deduplication, value mapping and replacement, axis renaming, discretization / binning, outlier filtering, sampling / shuffling, dummy variable construction, [[ExtensionDataTypes|pandas extension types]] (nullable Int, Boolean, String — fixing NaN-coerces-int-to-float pain), string methods (Python + regex + vectorized pandas `.str` accessor), and [[CategoricalData|categorical extension type]].

## Key Claims
- **Missing data sentinel** — `NaN` (float64), `pd.NA` (extension types). `s.isna()` / `s.notna()`; Python `None` treated as NA.
- **Drop** — `df.dropna(how="any"/"all", thresh=N, axis=0/1)`; **Fill** — `df.fillna(value)` (scalar, dict, or method=`"ffill"`/`"bfill"`); `s.fillna(s.mean())` for imputation.
- **Deduplication** — `df.duplicated()`, `df.drop_duplicates(subset=[...], keep="first"/"last"/False)`.
- **Map / Replace** — `s.map(dict)` or `s.map(func)`; `s.replace(old, new)` / `s.replace([a, b], [x, y])`; `df.rename(index=..., columns=..., mapper=str.lower)`.
- **Discretization** — `pd.cut(x, bins=[0,18,35,60], labels=[...])` → `Categorical`; `pd.qcut(x, q=4)` for quantile-based bins.
- **Outlier filtering** — boolean masks: `df[(df.abs() < 3).all(axis=1)]`.
- **Sampling** — `df.sample(n=, frac=, replace=, random_state=)`; `np.random.permutation` to shuffle row order.
- **Dummies** — `pd.get_dummies(df["category"], prefix=...)` one-hot encodes categorical columns.
- **Extension types** — `Int64`, `Int32`, `Float64`, `boolean`, `string` (uppercase = nullable / pd.NA-aware); declared via `pd.array([...], dtype="Int64")` or `df.astype("Int64")`.
- **String methods** — Python built-ins (`split`, `strip`, `replace`, `find`, `count`, `lower`, `upper`, `startswith`, `join`); `re` regex module (`re.compile`, `re.findall`, `re.sub`, named groups via `(?P<name>...)`); **vectorized via `Series.str.*`** — `s.str.contains`, `s.str.findall`, `s.str.extract`, `s.str.split`, `s.str.lower`. Handles NA gracefully.
- **Categorical** — `s.astype("category")`; stores integer codes + categories array; memory-efficient and faster `groupby`. Methods on `s.cat.*`: `categories`, `codes`, `set_categories`, `rename_categories`, `remove_unused_categories`, `as_ordered`.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[pandas]] — cleaning toolset.
- [[ExtensionDataTypes]] — nullable Int / Boolean / String extension arrays.
- [[CategoricalData]] — categorical extension type.
- [[RegularExpressions]] — Python `re` module.
- [[pydata-data-wrangling]] — chapter 8 next: combine / reshape cleaned data.

## Contradictions
- None.
