---
title: "Made With ML — Versioning Code, Data and Models"
type: source
tags: [mlops, made-with-ml, versioning, reproducibility]
date: 2026-05-15
source_file: raw/madewithml/mlops-versioning.md
---

## Summary
Made With ML lesson on versioning the three artifacts of an ML system. Code is versioned with [[Git]] + a remote host (GitHub/GitLab/BitBucket). Data and models are too large for Git, so the recommended pattern is to version pointers to remote storage rather than the artifacts themselves — using GitLFS, Dolt, Pachyderm, or [[DVC]] for data, and [[MLflow]] backed by S3 + a database (e.g. PostgreSQL RDS) for models. The goal is end-to-end reproducibility: any past run can be reconstructed by checking out the code commit and resolving the data/model pointers it referenced.

## Key Claims
- Reproducibility in ML requires versioning all three of code, data, and models — versioning code alone leaves the system non-reproducible.
- Git is ideal for code but unsuited for large or frequently-changing binary artifacts; storing models or unstructured datasets in Git bloats history and breaks clone performance.
- The canonical pattern is "version pointers, not artifacts": store the artifact in remote object storage and commit only a path/URI/hash to Git.
- Data versioning tooling includes GitLFS, Dolt, Pachyderm, and [[DVC]]; choice depends on backing store and metadata needs.
- Model versioning in production should swap the local [[MLflow]] artifact + backend store for remote stores: S3 for artifacts, PostgreSQL RDS for the tracking backend.
- A consistent git workflow (`add` → `commit` → `push`) underlies the human-facing half of versioning; the data/model half is automated by tooling.
- Versioning enables both retrospective debugging (what data/model produced this incident?) and graceful regression rollback.

## Key Quotes
> "It would be ideal if we can save locations (pointers) to these large artifacts in our code as opposed to the artifacts themselves." — on the pointer-versioning pattern

## Connections
- [[MadeWithML]] — source course
- [[GokuMohandas]] — author
- [[Anyscale]] — publisher
- [[Git]] — code VCS
- [[GitHub]] — code remote
- [[GitLab]] — code remote
- [[BitBucket]] — code remote
- [[GitLFS]] — large-file extension
- [[DVC]] — data version control tool
- [[Dolt]] — data versioning database
- [[Pachyderm]] — data pipeline versioning
- [[MLflow]] — model registry / tracking
- [[AmazonS3]] — artifact store
- [[PostgreSQL]] — MLflow backend store
- [[Versioning]] — primary concept
- [[ReproducibilityInML]] — motivation
- [[ModelRegistry]] — production pattern
- [[MLOps]] — discipline
- [[DataLineage]] — adjacent concept

## Contradictions
- None identified.
