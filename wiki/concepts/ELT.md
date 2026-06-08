---
title: "ELT"
type: concept
tags: [data-engineering, pipelines]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# ELT

Extract, Load, Transform — a modern [[DataPipeline]] pattern where raw data is loaded into a [[DataWarehouse]] or [[DataLake]] first, then transformed in-place with SQL or dbt. Inverts the [[ETL]] order, exploiting cheap warehouse compute for late-binding modeling.

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) highlights ELT's iteration-speed advantage: because transformation logic is just a query inside the warehouse, changing a feature definition takes minutes (rewrite SQL) rather than ETL's hours/days of full pipeline reprocessing — ~8× faster per schema change. The costs are higher storage (raw data is larger), repeated compute when many models transform the same source, and privacy risk from retaining raw sensitive data. ELT suits rapidly-evolving ML feature experimentation.

## Connections

- [[ETL]] — the transform-first inverse.
- [[DataIngestion]] — the stage where this decision is made.
- [[DataPipeline]] / [[DataWarehouse]] / [[DataLake]] — the substrate.
- [[mlsysbook-ch04-data-engineering]] — source.
