---
title: "pandas"
type: concept
tags: [library, python, data-analysis, dataframe]
sources: [pydata-preface, pydata-preliminaries, pydata-pandas-basics, pydata-accessing-data, pydata-data-cleaning, pydata-data-wrangling, pydata-data-aggregation, pydata-time-series, pydata-modeling, pydata-data-analysis-examples, d2l-preliminaries, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# pandas

The dominant Python library for structured / tabular / time-series data analysis. Provides two workhorse data structures — [[Series]] (1D labeled array) and [[DataFrame]] (2D column-oriented labeled table) — plus IO, indexing, alignment, missing-data handling, groupby ([[SplitApplyCombine]]), reshape, and time-series tooling.

## Origin
- Started by [[WesMcKinney]] in early 2008 at [[AQRCapitalManagement]].
- Open-sourced in 2010.
- Community-led since 2013; 2,500+ contributors.
- Name from "*panel data*" (econometrics) and "*Python data analysis*".

## Key features
- Built atop [[NumPy]]; inherits array-oriented idioms (no Python loops).
- Labeled axes via [[pandasIndex|Index objects]] enable automatic [[DataAlignment|data alignment]] across operations.
- Built-in time-series support (the original AQR use case).
- SQL-style joins (`pd.merge`), reshape (`stack`/`unstack`/`pivot`/`melt`), groupby with split-apply-combine.
- [[ExtensionDataTypes|Extension data types]] (nullable Int / Boolean / String / [[CategoricalData|Categorical]] / [[DatetimeIndex|Datetime]]) since pandas 1.0.
- 20+ readers / writers (CSV, JSON, Parquet, HDF5, Excel, SQL, …).

## Standard import
```python
import pandas as pd
from pandas import Series, DataFrame
```

## Connections
- [[NumPy]] — array foundation; pandas semantics inherit from it.
- [[Series]] / [[DataFrame]] / [[pandasIndex]] — core data structures.
- [[SplitApplyCombine]] / [[HierarchicalIndexing]] / [[ExtensionDataTypes]] / [[CategoricalData]] / [[Resampling]] — central concepts.
- [[matplotlib]] — `.plot` accessor delegates here.
- [[scikitlearn]] / [[statsmodels]] — common downstream modeling libraries.
- [[WesMcKinney]] — original author.
- [[Rlanguage]] — `DataFrame` named after R's `data.frame`.
