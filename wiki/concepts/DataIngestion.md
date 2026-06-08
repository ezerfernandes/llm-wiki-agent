---
title: "Data Ingestion"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, data-pipeline]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Data Ingestion

The pipeline boundary where heterogeneous external data (databases, APIs, file systems, IoT/audio streams) enters the controlled ML pipeline. In the compiler metaphor of Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]), ingestion is the **lexer**: it reads raw source streams and tokenizes them into well-formed records, standardizing formats and validating schemas at the boundary so source diversity is decoupled from feature-engineering complexity.

A critical, often-overlooked constraint is the **IO bottleneck**: training speed is $T_{\text{step}} = \max(T_{\text{compute}}, T_{\text{io}})$, so if data does not arrive fast enough the accelerator starves (see [[DataLoaderChokePoint]]). The two governing decisions are **timing** ([[BatchIngestion|batch]] vs [[StreamIngestion|streaming]]) and **transformation authority** ([[ETL]] vs [[ELT]]) — together they fix the cost, latency, and reliability profile of every downstream stage.

JSON's schema flexibility makes it common for APIs but creates a validation bottleneck — per-record parsing can be 10× slower than binary formats like Protobuf or [[Parquet]].

## Connections

- [[BatchIngestion]] / [[StreamIngestion]] — the timing decision.
- [[ETL]] / [[ELT]] — the transformation-authority decision.
- [[DataLoaderChokePoint]] — the IO bottleneck this stage must avoid.
- [[DataPipeline]] — the layered architecture ingestion feeds.
- [[DataContract]] / [[SchemaValidation]] — boundary standardization.
- [[mlsysbook-ch04-data-engineering]] — source.
