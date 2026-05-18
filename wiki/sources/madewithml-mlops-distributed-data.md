---
title: "Made With ML — Distributed Data Processing"
type: source
tags: [mlops, made-with-ml, distributed-data, ray]
date: 2026-05-15
source_file: raw/madewithml/mlops-distributed-data.md
---

## Summary
This lesson scales the previous single-machine preprocessing pipeline to a distributed setting using [[Ray]] Data. The pandas-based `preprocess` function from the prior lesson is reused unchanged — Ray's `map_batches` (with `batch_format="pandas"`) distributes it across the cluster. Ingestion uses `ray.data.read_csv`, deterministic ordering is enabled via `DatasetContext.execution_options.preserve_order = True`, and splitting uses a custom `stratify_split` to maintain tag distribution across the train/val sets.

## Key Claims
- As datasets and models grow (especially LLMs), single-machine processing becomes infeasible; distribution is unavoidable.
- Many distributed frameworks exist (Ray, Dask, Modin, Spark) but Ray is chosen because it scales Python with *minimal* code changes and integrates with all the others.
- Setting `ray.data.DatasetContext.get_current().execution_options.preserve_order = True` is required for deterministic, reproducible results.
- The same pandas preprocessing function written for a single machine works under Ray's `map_batches` with no rewriting.
- Ray Data has built-in I/O for every major format and source; ingestion is a one-liner: `ray.data.read_csv(DATASET_LOC)`.
- Stratified splitting on the distributed dataset preserves class balance just as `sklearn.train_test_split(stratify=...)` does on a single machine.
- Adding more compute resources scales preprocessing throughput automatically with no code changes.

## Key Quotes
> "We want to choose a framework that is will allow us to scale our data processing operations with minimal changes to our existing code and all in Python."

> "If we add more compute resources, we can scale our data processing operations to be even faster with no changes to our code."

## Connections
- [[MadeWithML]] — parent course.
- [[GokuMohandas]] — author.
- [[Anyscale]] — publisher (commercial host of Ray).
- [[Ray]] — distributed runtime.
- [[RayData]] — Ray's distributed data library used here.
- [[pandas]] — DataFrame format inside `map_batches`.
- [[Dask]] — alternative framework discussed.
- [[Modin]] — alternative framework discussed.
- [[ApacheSpark]] — alternative framework discussed.
- [[DistributedComputing]] — broader paradigm.
- [[MapBatches]] — Ray Data primitive for distributed apply.
- [[StratifiedSampling]] — used in the custom `stratify_split`.
- [[Determinism]] — `preserve_order` flag for reproducibility.
- [[MLOps]] — surrounding discipline.
- [[CSVFormat]] — input source format.
- [[DataPipeline]] — broader pattern this lesson exemplifies.

## Contradictions
- None identified.
