---
title: "Python for Data Analysis 3E — Ch.1: Preliminaries"
type: source
tags: [book, python, data-analysis, pydata, ecosystem]
date: 2026-05-15
source_file: raw/pydata-book-web/preliminaries.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/preliminaries.html
chapter: 1
---

## Summary
Introduces the book's scope (structured-data manipulation, cleaning, processing in Python), surveys the essential Python data ecosystem — [[NumPy]], [[pandas]], [[matplotlib]], [[IPython]]/[[Jupyter]], [[SciPy]], [[scikitlearn]], [[statsmodels]] — and walks through Miniconda installation, package setup, and import conventions used throughout the book.

## Key Claims
- **Structured data** is the primary focus: tabular data, multidimensional arrays, multiple keyed tables, time series. Even unstructured data is often transformed into structured form for analysis.
- **Why Python for data analysis**: glue language for C / C++ / FORTRAN legacy code; addresses the "two-language" problem (research → production); large scientific community since ~2005.
- **Why not Python**: interpreted speed penalty; [[GlobalInterpreterLock|GIL]] hampers CPU-bound multithreading (Python C extensions sidestep the GIL).
- **Essential libraries**: NumPy (ndarray + C API); pandas (DataFrame + Series, 2010-emerged, blends NumPy + SQL semantics); matplotlib (publication plots); IPython/Jupyter (execute-explore workflow); SciPy (integrate / linalg / optimize / signal / sparse / stats / special); scikit-learn (since 2007, ML toolkit); statsmodels (classical statistics: regression, time series, ANOVA).
- **Installation**: [[Miniconda]] is the recommended distribution across Windows / macOS / Linux. Default channel: `conda-forge`. Core package set: `pandas`, `jupyter`, `matplotlib`.
- **Import conventions** used throughout the book:
  ```python
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd
  import seaborn as sns
  import statsmodels as sm
  ```

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[NumPy]] — chapter 4 dives deeper.
- [[pandas]] — chapter 5 onward.
- [[matplotlib]] — chapter 9.
- [[IPython]] — Appendix B.
- [[scikitlearn]] / [[statsmodels]] — chapter 12.
- [[WesMcKinney]] — author and pandas creator.
- [[GlobalInterpreterLock]] — concurrency caveat.

## Contradictions
- None.
