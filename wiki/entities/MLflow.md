---
title: "MLflow"
type: entity
tags: [tool, experiment-tracking, model-registry]
sources: [madewithml-mlops-experiment-tracking, madewithml-mlops-jobs-and-services, madewithml-mlops-versioning]
last_updated: 2026-05-15
---

# MLflow

Open-source platform for [[ExperimentTracking]] and [[ModelRegistry]]. Integrated via `MLflowLoggerCallback` in [[madewithml-mlops-experiment-tracking]]; uses [[PostgreSQL]] for the tracking store and [[AmazonS3]] for artifacts. Underlies [[Databricks]]'s managed offering.
