---
title: "Artifact (MLOps Artifact)"
type: concept
tags: [mlops, versioning, lineage, architecture]
sources: [leh-ch02-tooling-and-installation, leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## Definition
An **artifact** in MLOps is any file or data object produced during the ML lifecycle that needs to be tracked, versioned, and reused — datasets, trained models, checkpoints, configurations, logs, evaluation reports. Artifacts are the unit of lineage: every pipeline run produces them, and downstream runs consume them by reference.

## In LLM Engineer's Handbook
[[leh-ch02-tooling-and-installation]] gives the canonical working definition: "In MLOps, an artifact is any file(s) produced during the machine learning lifecycle, such as datasets, trained models, checkpoints, or logs." The chapter shows ZenML auto-versioning every step output as an artifact and supporting user-attached metadata (e.g., `step_context.add_output_metadata(...)` with dataset categories, train/test split size, and per-category sample counts on an `instruct_datasets` artifact). Loading a specific artifact version becomes `Client().get_artifact_version('8bba35c4-...').load()`. [[leh-ch03-data-engineering]] uses artifacts as the `user` and `crawled_links` outputs of the ETL pipeline, each inspectable in the ZenML dashboard.

## Key details
- Artifacts are content-addressable: versions identified by UUID or hash.
- Each artifact carries metadata (tags, lineage, schema, custom key/value pairs).
- Artifacts are the natural interface between pipelines — a downstream pipeline reads artifacts by ID, not by direct upstream call.
- ZenML's `ArtifactConfig(name=..., tags=[...])` annotates the return value of a step.
- The artifact store (S3, GCS, local FS) is one of the four core MLOps components.

## Connections
- [[Step]] — the unit that produces artifacts.
- [[Pipeline]] / [[Orchestrator]] — wire artifacts between steps.
- [[ZenML]] — the orchestrator whose artifact model this concept describes most directly.
- [[Materializer]] — serializer extension point for custom artifact types.
- [[ModelRegistry]] — a specialized artifact store for trained models.
- [[FeatureStore]] / [[LogicalFeatureStore]] — feature-specific artifact stores.
- [[ExperimentTracking]] — tracks artifacts alongside metrics and hyperparameters.
- [[Versioning]] — the underlying discipline artifacts implement.
