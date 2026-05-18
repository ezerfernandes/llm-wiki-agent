---
title: "Map Batches"
type: concept
tags: [data-processing, ray, distributed]
sources: [madewithml-data, madewithml-preprocessing]
last_updated: 2026-05-15
---

# Map Batches

A Ray Data transformation that applies a function over batches of rows in parallel across workers. Enables scalable [[Preprocessing]]-style operations on [[DataFrame]]-like inputs without loading data fully into memory.
