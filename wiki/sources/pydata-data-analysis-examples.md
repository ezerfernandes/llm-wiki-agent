---
title: "Python for Data Analysis 3E — Ch.13: Data Analysis Examples"
type: source
tags: [book, pandas, examples, eda, pydata]
date: 2026-05-15
source_file: raw/pydata-book-web/data-analysis-examples.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/data-analysis-examples.html
chapter: 13
---

## Summary
Capstone of the book — five worked exploratory analyses on real datasets, exercising the full pipeline (load → clean → wrangle → group → plot). Datasets: 1.USA.gov Bitly click feed, MovieLens 1M ratings, US Baby Names 1880–2010, USDA Food Database, 2012 FEC presidential campaign donations.

## Key Claims
- **Bitly / 1.USA.gov** — line-delimited JSON; `json.loads` per line → list of dicts → `pd.DataFrame(records)`. Count time zones via `value_counts` (pandas) vs `collections.Counter` (pure Python). Plot top time zones via `seaborn.barplot`.
- **MovieLens 1M** — three CSV-like `dat` files joined on user/movie IDs (`pd.merge`). Compute mean rating per movie per gender via `pivot_table`. Measure rating disagreement via standard deviation of rating across users per movie.
- **US Baby Names 1880–2010** — yearly per-state CSVs concatenated via `pd.concat`. Demonstrate name popularity over time (`groupby` + `pivot_table`), proportion of births (`groupby.transform`), and **diversity trends** (number of names accounting for 50% of births per year — narrative arc of the analysis).
- **USDA Food Database** — nested JSON of nutrients per food; flatten with `pd.json_normalize` then merge tables; explore by food group via `groupby` aggregations.
- **2012 FEC** — donation records with donor occupation + employer + amount + recipient. Clean occupation strings (map abbreviations), bucket donation amounts via `pd.cut`, and aggregate by candidate × state via `pivot_table`. Demonstrates real-world value of categorical cleaning and `pivot_table` margins.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- Capstone for all preceding chapters — exercises ingestion, cleaning, joining, reshaping, groupby, plotting.
- [[pydata-data-aggregation]] / [[pydata-data-wrangling]] / [[pydata-plotting-and-visualization]] / [[pydata-data-cleaning]] — building blocks demonstrated together here.
- [[pydata-advanced-numpy]] — Appendix A.
- [[pydata-ipython]] — Appendix B.

## Contradictions
- None.
