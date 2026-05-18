---
title: "ELT"
type: concept
tags: [data-engineering, pipelines]
sources: []
last_updated: 2026-05-15
---

# ELT

Extract, Load, Transform — a modern [[DataPipeline]] pattern where raw data is loaded into a [[DataWarehouse]] or [[DataLake]] first, then transformed in-place with SQL or dbt. Inverts the [[ETL]] order, exploiting cheap warehouse compute for late-binding modeling.
