---
title: "ETL"
type: concept
tags: [data-engineering, pipelines]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# ETL

Extract, Transform, Load — the traditional [[DataPipeline]] order where data is reshaped before landing in the [[DataWarehouse]]. Contrast with the modern [[ELT]] pattern; both serve as substrate for [[FeatureEngineering]] and ML training data assembly.

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) frames the ETL-vs-[[ELT]] choice as **where transformation authority lives**. ETL validates schema *and* distributional properties before loading, so only clean, schema-conformant data reaches the warehouse (enforcing quality + privacy at ingestion). Its cost is rigidity: a feature-definition change requires reprocessing all source data — hours/days, and ~8× more engineering time per schema change than ELT. In a 10 TB/day reference example, ETL is slightly cheaper on cloud cost but far slower to iterate; stable schemas favor ETL, rapidly-evolving features favor ELT.

## Connections

- [[ELT]] — the load-first inverse; the cost-of-transformation-placement trade-off.
- [[DataIngestion]] — the stage where this decision is made.
- [[DataPipeline]] / [[DataWarehouse]] / [[FeatureEngineering]] — the substrate.
- [[mlsysbook-ch04-data-engineering]] — source.
