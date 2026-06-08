---
title: "Great Expectations"
type: entity
tags: [tool, data-validation, testing]
sources: [madewithml-mlops-testing, madewithml-mlops-monitoring, mlsysbook-ch04-data-engineering, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Great Expectations

Python data-validation library for declaring and testing expectations on tabular data. Used in [[madewithml-mlops-testing]] for data tests and in [[madewithml-mlops-monitoring]] for production data quality.

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) presents Great Expectations (with Pandera/Pydantic) as the canonical **data-quality-as-code** tool: executable expectation suites (range, null, uniqueness, categorical-set checks) run in CI/CD, fail deployments before bad data reaches training, and version alongside training code — catching ~60% of production data issues pre-training. It is also the recommended remediation for [[DataContract|data contracts]] / [[SchemaEvolution|schema debt]].

## Connections

- [[DataQuality]] — mechanical vs semantic validation.
- [[SchemaValidation]] / [[DataContract]] — what expectation suites enforce.
- [[DataDebt]] — schema-debt remediation via contract enforcement.
- [[madewithml-mlops-testing]] / [[madewithml-mlops-monitoring]] / [[mlsysbook-ch04-data-engineering]] — sources.
- [[mlsysbook-ch14-ml-operations]] — Ch 14 uses Great Expectations for input-data validation (column existence, types, nulls, statistical bounds) before inference.

