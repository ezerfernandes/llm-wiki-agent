---
title: "Made With ML — Pandas"
type: source
tags: [foundations, made-with-ml, pandas, dataframe, eda, course]
date: 2026-05-15
source_file: raw/madewithml/foundations-pandas.md
---

## Summary
Hands-on lesson on [[pandas]] for tabular data. Loads a Titanic-style dataset, performs initial exploratory data analysis (`head`, `describe`, `info`, `value_counts`, `hist`, scatter), then walks through filtering (boolean masks), sorting (`sort_values`), grouping/aggregation (`groupby` + `mean` / `sum` / `agg`), indexing (`loc` vs `iloc`), preprocessing (handling NaN via `dropna` and `fillna`, dropping columns, replacing values, one-hot encoding via `pd.get_dummies`), feature engineering (deriving new columns from existing ones, applying functions row-wise via `apply`/`lambda`), saving to CSV, and scaling discussion (when single-machine pandas hits memory limits and the path to [[Dask]] / [[ModinPandas]] / [[Ray]]). The lesson is the canonical "from raw CSV to ML-ready features" pipeline expressed in pandas idioms.

## Key Claims
- pandas excels at single-machine tabular workflows up to a few GB; beyond that, the same API surface is preserved by [[Dask]], [[ModinPandas]], or distributed [[Ray]] backends.
- `.loc` is label-based, `.iloc` is positional — mixing them is a frequent bug source; the lesson treats them as distinct primitives.
- `groupby` is the workhorse of pandas EDA: split-apply-combine across one or more grouping keys returns aggregated views without materializing intermediate frames.
- One-hot encoding via `pd.get_dummies` is the canonical way to convert categorical features to numeric inputs for ML models that consume continuous vectors.
- Apply with a lambda (`df.col.apply(lambda x: ...)`) is the escape hatch for arbitrary row-level logic, but vectorized column operations should be preferred when possible for performance.
- The trio of `info` / `describe` / `value_counts` is the standard first pass on any new dataset before any modeling work.

## Key Quotes
> "Pandas is a popular library for data manipulation and analysis."

> "We're going to use the Titanic dataset to demonstrate ... loading, exploration, manipulation, and saving of tabular data."

## Connections
- [[GokuMohandas]] — author.
- [[MadeWithML]] — parent course.
- [[pandas]] — the library itself.
- [[DataFrame]] — pandas' 2D labeled tabular structure.
- [[NumPy]] — the underlying array engine for pandas Series/DataFrame.
- [[Python]] — prerequisite lesson.
- [[PyTorch]] — successor lesson; pandas DataFrames frequently feed `torch.utils.data.Dataset`.
- [[ExploratoryDataAnalysis]] — workflow this lesson formalizes.
- [[OneHotEncoding]] — `pd.get_dummies` operation.
- [[FeatureEngineering]] — pattern of deriving new columns from raw data.
- [[WesMcKinney]] — pandas creator.
- [[Dask]] / [[ModinPandas]] — pandas-API-compatible scale-out options.

## Contradictions
None — applied data-handling primer.
