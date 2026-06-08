---
title: "Schema Validation"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, data-quality, reliability]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Schema Validation

Synchronous checking of data types, value ranges, and presence requirements as records enter the pipeline — the "type checker" of the dataset compiler (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). It rejects malformed records immediately, before they propagate downstream, evaluating individual records in microseconds.

Tools like TensorFlow Data Validation (TFDV) automatically infer schemas from training data. But schema validation alone catches only **mechanical** ([[DataQuality|container]]) problems — it cannot detect **semantic** drift, where every record is structurally valid yet the distribution has shifted (the self-driving LiDAR labels misaligned by 10–20 cm passed every schema check). That requires asynchronous statistical validation ([[KolmogorovSmirnovTest|K-S test]], [[PopulationStabilityIndex|PSI]]) on sampled traffic. Schema validation is the first line of defense against [[SchemaEvolution|schema-evolution]] failures, formalized through [[DataContract|data contracts]].

## Connections

- [[DataContract]] — the producer-consumer agreement schema validation enforces.
- [[SchemaEvolution]] — the failure mode it guards against.
- [[DataQuality]] — mechanical vs semantic checks.
- [[GreatExpectations]] — data-quality-as-code tooling.
- [[mlsysbook-ch04-data-engineering]] — source.
