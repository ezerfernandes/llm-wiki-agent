---
title: "Python for Data Analysis 3E — Ch.6: Data Loading, Storage, and File Formats"
type: source
tags: [book, pandas, io, csv, json, parquet, hdf5, pydata]
date: 2026-05-15
source_file: raw/pydata-book-web/accessing-data.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/accessing-data.html
chapter: 6
---

## Summary
How to get data into and out of pandas: text formats (CSV, TSV, fixed-width, JSON, HTML, XML), binary formats (Excel, [[HDF5]], Pickle, Feather, ORC, [[Parquet]]), web APIs (`requests` + `pd.json_normalize`), and SQL databases via [[SQLAlchemy]] / `pandas.read_sql`.

## Key Claims
- **`pandas.read_csv`** is the most-used loader; ~50 optional arguments covering indexing, type inference, NA markers, date parsing, chunked iteration (`chunksize=`), and unclean-data handling (`skiprows`, `comment=`, `thousands=`, `na_values=`).
- **Reader catalog** — `read_csv`, `read_fwf`, `read_clipboard`, `read_excel`, `read_hdf`, `read_html`, `read_json`, `read_feather`, `read_orc`, `read_parquet`, `read_pickle`, `read_sas`, `read_spss`, `read_sql`, `read_sql_table`, `read_stata`, `read_xml`. Each has a matching `DataFrame.to_*` writer.
- **Chunking** — `pd.read_csv(path, chunksize=N)` returns an iterator over `N`-row DataFrames; useful for files larger than memory.
- **Writing** — `df.to_csv(path, sep="|", na_rep="NA", index=False, columns=[...])`.
- **JSON** — `pd.read_json` / `df.to_json(orient="records"|"split"|"table"|...)`; `pd.json_normalize` flattens nested JSON into a table.
- **HTML / XML** — `pd.read_html(url)` returns a list of DataFrames (one per `<table>`); `pd.read_xml` for XML.
- **Excel** — `pd.read_excel(path, sheet_name=...)`; requires `openpyxl` (xlsx) or `xlrd` (legacy xls); writers via `pd.ExcelWriter`.
- **HDF5** — `pd.HDFStore` or `df.to_hdf(path, key="...", format="table"/"fixed")`; supports out-of-core querying for large arrays.
- **Parquet / Feather / ORC** — columnar binary formats with embedded schema; fastest read/write and smallest on disk. `pyarrow` backend.
- **Pickle** — `df.to_pickle` / `pd.read_pickle`; not a long-term archival format (Python-version dependent).
- **Web APIs** — `requests.get(url).json()` → list of dicts → `pd.DataFrame(data)`.
- **Databases** — `sqlalchemy.create_engine(url)` + `pd.read_sql_query("...", engine)` returns a DataFrame; `df.to_sql(name, engine, if_exists="...")` writes.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[pandas]] — IO subsystem.
- [[DataFrame]] — the canonical loaded object.
- [[Parquet]] / [[HDF5]] — binary formats covered.
- [[SQLAlchemy]] — DB connection abstraction.
- [[pydata-data-cleaning]] — chapter 7 next: clean loaded data.

## Contradictions
- None.
