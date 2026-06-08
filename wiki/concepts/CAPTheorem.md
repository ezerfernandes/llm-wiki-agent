---
title: "CAP Theorem"
type: concept
tags: [distributed-systems, ml-systems, mlsysbook, data-engineering, streaming]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# CAP Theorem

A distributed system cannot simultaneously guarantee all three of **Consistency** (all nodes see the same data), **Availability** (the system stays operational), and **Partition tolerance** (continues despite network failures) — one must be sacrificed. Conjectured by Brewer (2000), proved by Gilbert & Lynch (2002); applied to ML streaming and storage in Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]).

For streaming ingestion the theorem forces concrete choices: [[ApacheKafka|Apache Kafka]] emphasizes **CP** (consistency + partition tolerance — a partition can become unwritable for seconds during a leader re-election, sacrificing availability), Apache Pulsar emphasizes **AP**, and [[Kinesis]] exposes the trade-offs through shard configuration. For [[FeatureStore|feature stores]] the choice is equally concrete: a CP store guarantees training and serving see identical feature values but may be unavailable during partitions, while an AP store stays up but risks serving stale features that diverge from training data.

## Connections

- [[StreamIngestion]] — the regime where the theorem constrains tool choice.
- [[ApacheKafka]] / [[Kinesis]] — CP vs configurable streaming systems.
- [[FeatureStore]] — CP-vs-AP feature-store trade-off.
- [[mlsysbook-ch04-data-engineering]] — source.
