---
name: MLPlatform
title: "ML Platform"
type: concept
tags: [mlops, infrastructure, platform]
sources: [dmls-ch10-infrastructure-mlops]
last_updated: 2026-05-23
---

# ML Platform

Shared infrastructure layer that hosts the **model deployment service** + **[[ModelStore|model store]]** + **[[FeatureStore|feature store]]** + **[[Monitoring|monitoring]]** components common to all of an organization's ML applications. Per [[ChipHuyen|Huyen]]'s [[dmls-ch10-infrastructure-mlops|DMLS Ch 10]], the ML platform sits **above** raw [[ComputeLayer|compute/storage]] and resource-management primitives ([[Kubernetes]] / [[Slurm]] / [[Borg]]) and **below** application-specific dev environments and pipelines.

## How it emerges
ML platforms are typically born inside the recommender-system team — the first team to need shared inference infrastructure at scale — and then absorbed across teams as other ML applications mature. Uber's [[MichelangeloPlatform]] (2017) and [[StitchFix|Stitch Fix]]'s internal platform are canonical examples; [[AmazonSageMaker]], [[GoogleCloudVertexAI]], and [[AzureML]] are the managed-cloud counterparts.

## Maturity of components (per Huyen)
- **[[ModelDeployment]]** — most mature; every cloud has it.
- **[[ModelStore]]** — least mature; reduces to "throw the file on [[AmazonS3]]" at most companies.
- **[[FeatureStore]]** — emerging; [[Feast]] / [[Tecton]] / [[Amundsen]] / [[DataHub]] in active development.
- **[[Monitoring]]** — third-party-tool layer ([[Datadog]] / [[AmazonCloudWatch]]).

## Build vs buy
Huyen names three deciding factors: company stage, focus (is ML the product or not?), and component maturity. Cf. [[ModelBuildVsBuy]].

## Connections
- [[MLOps]] — the platform is the operational substrate of MLOps.
- [[FeatureStore]], [[ModelStore]], [[ModelDeployment]], [[Monitoring]] — the four canonical components.
- [[MichelangeloPlatform]] — Uber's reference implementation.
- [[Kubernetes]], [[Docker]] — typical compute substrate.
