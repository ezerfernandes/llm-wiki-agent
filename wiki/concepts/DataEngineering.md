---
title: "Data Engineering"
type: concept
tags: [data, infrastructure]
sources: [mlsysbook-ch03-ml-workflow, mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Data Engineering

The discipline of designing and operating systems that ingest, transform, store, and serve data reliably at scale — [[ETL]], [[ELT]], [[DataPipeline]], [[DataWarehouse]], [[DataLake]]. Upstream of ML modeling; quality here determines everything downstream including [[FeatureEngineering]] and [[DataQuality]].

Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]) puts data engineering at the center of the [[MLWorkflow|ML workflow]]: data work consumes **60–80% of ML effort**, most iteration cycles originate in data, and most failures begin there — which is why Part I of the book *ends* with the dedicated data-engineering chapter (Ch 4). It introduces [[TieredStorage|tiered storage]], [[DataVersioning|data versioning]], and the [[DataCascade|data cascade]] failure mode.

The dedicated **[[mlsysbook-ch04-data-engineering|Ch 4]]** (Part I capstone) reframes data engineering not as "data cleaning" but as **Dataset Compilation** — a compiler-style pipeline where filtering = dead-code elimination, augmentation = loop unrolling, [[DataDeduplication|dedup]] = common-subexpression elimination, and [[SchemaValidation|schema validation]] = type checker. It organizes the whole discipline around the [[FourPillarsOfDataEngineering|four pillars]] (Quality, Reliability, Scalability, Governance), grounds it in the physics of [[DataGravity|data gravity]] and [[InformationEntropy|information entropy]], and runs a single [[KeywordSpotting|KWS]] lighthouse through acquisition → [[DataIngestion|ingestion]] → processing → [[DataLabeling|labeling]] → [[StorageArchitecture|storage]] → [[DataDebt|operational health]].
