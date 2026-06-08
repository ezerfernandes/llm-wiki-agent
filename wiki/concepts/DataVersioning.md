---
title: "Data Versioning"
type: concept
tags: [mlops, data, reproducibility, mlsysbook]
sources: [mlsysbook-ch03-ml-workflow, mlsysbook-ch04-data-engineering, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Data Versioning

Tracking versions of datasets so a training run can be reproduced and accuracy regressions diagnosed. Unlike code — which changes through discrete, auditable commits — **data can drift gradually** (distribution shift), **suddenly** (schema migration), or **subtly** (label-quality degradation) (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]).

Plain Git cannot version multi-terabyte datasets, forcing specialized tooling like **DVC** and **[[GitLFS|Git LFS]]**. The systems consequence: without data versioning, teams cannot reproduce a prior training run or determine whether an accuracy regression stems from a code change or a data change — making root-cause analysis intractable.

## Connections

- [[Reproducibility]] / [[ReproducibleSystemArtifact]] — data version is part of the reproducible bundle.
- [[DataLineage]] — links data versions to the models they produced.
- [[GitLFS]] / [[DVC]] / [[MLflow]] — large-file/metadata tooling for versioning datasets ([[mlsysbook-ch04-data-engineering|Ch 4]] adds Delta Lake time-travel: `SELECT ... VERSION AS OF 47`).
- [[TieredStorage]] — the storage substrate datasets migrate across.
- [[DataDebt]] — [[mlsysbook-ch04-data-engineering|Ch 4]]: deferring versioning until debugging needs it causes 2–4× longer investigations.
- [[mlsysbook-ch03-ml-workflow]] / [[mlsysbook-ch04-data-engineering]] — sources.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 makes data versioning part of the reproducibility/lineage layer (DVC), snapshotting datasets and associating them with model runs.

