---
title: "Schema Evolution"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, reliability]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Schema Evolution

The failure mode where source systems add fields, rename columns, or change data types without coordination, breaking downstream ML processing assumptions (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). It arises from a lack of contract testing between data producers and consumers.

The chapter distinguishes two flavors. **Loud** failures (a renamed column) break explicit assumptions and crash the pipeline immediately. **Silent** failures are more dangerous: a field changing type from integer to string can pass [[SchemaValidation|validation]] but corrupt feature logic, often going undetected for weeks while degrading model accuracy by over 5% before discovery. The defense is explicit [[DataContract|data contracts]] that fail fast; the absence of them produces accumulated workarounds (defensive null checks, version-specific parsing branches) that constitute **schema debt** (a category of [[DataDebt|data debt]]).

## Connections

- [[DataContract]] / [[SchemaValidation]] — the defenses.
- [[DataDebt]] — schema debt is the unmanaged form.
- [[TrainingServingSkew]] — silent type changes are one mechanism.
- [[mlsysbook-ch04-data-engineering]] — source.
