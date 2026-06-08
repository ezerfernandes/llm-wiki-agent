---
title: "Data Warehouse"
type: concept
tags: [data, infrastructure, analytics]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Data Warehouse

A schema-on-write analytical store ([[Snowflake]], BigQuery, [[AmazonRedshift|Redshift]]) optimized for SQL aggregations over curated, modeled data. Sits downstream of raw [[DataLake]] zones in modern [[DataPipeline]] architectures; primary serving layer for BI and ML feature derivation.

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) positions warehouses as the **high-throughput / [[ColumnarStorage|columnar]]** option in the [[StorageArchitecture|storage decision]] (OLAP): ideal for batch training and feature engineering, delivering 5–10× I/O reduction by reading only needed columns from wide tables. They assume relatively stable schemas and struggle with unstructured data or rapidly-evolving formats (an `ALTER TABLE` can take hours on large datasets).

## Connections

- [[DataLake]] / [[Lakehouse]] — the schema-on-read and hybrid alternatives.
- [[StorageArchitecture]] — the IOPS-vs-throughput decision.
- [[ColumnarStorage]] / [[Parquet]] — the layout that gives warehouses their I/O advantage.
- [[mlsysbook-ch04-data-engineering]] — source.
