---
title: "Made With ML — Data Engineering for Machine Learning"
type: source
tags: [mlops, made-with-ml, data-engineering, elt, modern-data-stack, course]
date: 2026-05-15
source_file: raw/madewithml/mlops-data-engineering.md
---

## Summary
Walkthrough of building a modern data stack to feed ML applications. Distinguishes three data system archetypes — [[DataLake]] (flat object store, raw multi-format data), [[Database]] (OLTP, row-oriented, single-app CRUD), [[DataWarehouse]] (OLAP, column-oriented, multi-source analytics) — then implements ELT end-to-end: extract CSV sources via [[Airbyte]] connectors, load into [[GoogleBigQuery]], and transform with [[dbt]] Cloud (SQL joins + `schema.yml` tests + dbt jobs/environments). Covers batch vs streaming ingestion, micro-batch as a middle ground, and the "raw to lake, processed to warehouse" best practice. Closes with observability dimensions (data quality, lineage, discoverability, privacy/security) and tooling-selection criteria (cost, connectors, team aptitude, support).

## Key Claims
- The ML use case is one of many downstream consumers; transformation and testing should be moved upstream so other apps (analytics, BI) benefit too.
- Three storage archetypes with sharply different access patterns: data lakes (object-store, all formats, cheap), databases (OLTP, row access), data warehouses (OLAP, column aggregation).
- ELT > ETL for the modern stack: load raw to the warehouse first, then transform in-warehouse with [[dbt]] — leverages the warehouse's compute and keeps raw lineage.
- Ingestion tooling ([[Airbyte]], [[Fivetran]], [[Stitch]]) is now a commodity layer of connectors + scheduling — custom scripts are an anti-pattern at any non-trivial scale.
- "Start simple": begin with batch ingestion and a single source → DB → report pipeline; add micro-batch / streaming complexity only when downstream value is proven.
- dbt Cloud delivers production hygiene around SQL (version control, tests, docs, lineage, environments, jobs) that raw warehouse views don't.
- Analytics use cases should ship before ML use cases — a robust dashboard stack establishes data trust before model-driven infra adds [[FeatureStore]] / orchestration complexity.
- Data observability has four dimensions: quality (schemas, completeness, recency), lineage (where it came from), discoverability (catalog), and privacy/security.
- Streaming ingestion uses [[ApacheKafka]] / [[Kinesis]]; micro-batch sits at <15-minute intervals; "interval → 0" never collapses into streaming because the trigger model is fundamentally different (continuous vs scheduled).

## Key Quotes
> "Start with the simplest infrastructure (source → database → report) and add complexity (in infrastructure, performance and team) as needed."

> "It's a good idea for the first several applications to be analytics and reporting based in order to establish a robust data stack."

> "Batch processing is deliberately deciding to extract data from a source at a given interval. As that interval becomes <15 minutes, it's referred to as a micro-batch ... However, with stream ingestion, the extraction process is continuously on and events will keep being ingested."

## Connections
- [[GokuMohandas]] — author.
- [[MadeWithML]] — parent course.
- [[DataEngineering]] — umbrella concept.
- [[ModernDataStack]] — the assembled architecture.
- [[ELT]] / [[ETL]] — pipeline ordering pattern.
- [[DataLake]] — raw object storage layer.
- [[DataWarehouse]] — OLAP analytics storage.
- [[OLTP]] / [[OLAP]] — transactional vs analytical access patterns.
- [[Airbyte]] — open-source ingestion tool used in the lesson.
- [[Fivetran]] / [[Stitch]] — alternative ingestion tools.
- [[GoogleBigQuery]] — chosen data warehouse.
- [[Snowflake]] / [[AmazonRedshift]] / [[ApacheHive]] — alternative warehouses.
- [[dbt]] — in-warehouse SQL transformation tool with tests/lineage.
- [[GreatExpectations]] — referenced as the deeper data-quality testing layer.
- [[ApacheKafka]] / [[Kinesis]] — streaming ingestion substrates.
- [[ApacheSpark]] / [[ApacheFlink]] — large-scale analytics engines for heavy transforms.
- [[FeatureStore]] — downstream ML consumer of the warehouse.
- [[DataObservability]] — quality + lineage + discoverability + privacy/security.
- [[MonteCarloData]] / [[Bigeye]] — observability tooling.
- [[Tableau]] / [[Looker]] / [[Metabase]] / [[Superset]] — analytics consumers.

## Contradictions
None. Sits upstream of the rest of the MLOps track — the data this stack produces is what the training and monitoring chapters consume.
