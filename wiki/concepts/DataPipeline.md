---
title: "Data Pipeline"
type: concept
tags: [data-engineering, mlops]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Data Pipeline

An orchestrated sequence of transformations (extract, clean, join, aggregate, load) that moves data from sources to consumable form for analytics or ML. Implemented via Airflow, Dagster, Prefect, or Ray; integrates with [[DataLake]], [[DataWarehouse]], [[FeatureStore]], and is monitored by [[DataObservability]].

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) treats the ML data pipeline as a **compiler**: sources → [[DataIngestion|ingestion]] (lexer) → storage → processing (optimization pass) → [[DataLabeling|labeling]] → training, with a [[DataGovernance|governance]] band spanning all layers. Each layer scales independently. The pipeline is constrained by storage hierarchies and I/O bandwidth (the [[DataLoaderChokePoint|feeding tax]]) rather than CPU, and is governed throughout by the [[FourPillarsOfDataEngineering|four pillars]].

## Connections

- [[DataIngestion]] / [[DataLabeling]] / [[StorageArchitecture]] — the pipeline layers.
- [[ETL]] / [[ELT]] — the transformation-placement patterns.
- [[FourPillarsOfDataEngineering]] — the design lens applied at every layer.
- [[DataLoaderChokePoint]] — the I/O constraint that dominates pipeline design.
- [[DataLake]] / [[DataWarehouse]] / [[FeatureStore]] — integration points.
- [[mlsysbook-ch04-data-engineering]] — source.
