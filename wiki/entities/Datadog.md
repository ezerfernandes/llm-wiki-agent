---
title: "Datadog"
type: entity
tags: [tool, observability, monitoring]
sources: [madewithml-mlops-monitoring, agentic-design-patterns-ch19-evaluation]
last_updated: 2026-06-07
---

# Datadog

Observability and monitoring SaaS. Mentioned as a system-monitoring option alongside [[Grafana]] in [[madewithml-mlops-monitoring]].

[[agentic-design-patterns-ch19-evaluation|*Agentic Design Patterns* Ch 19]] names Datadog (with [[Splunk]] and [[Grafana|Grafana Cloud]]) as an observability platform for **persisting agent latency telemetry**, rather than printing it to the console — one of the recommended sinks for the [[EvaluationAndMonitoring|Evaluation and Monitoring]] pattern (alongside time-series DBs [[Prometheus]]/[[InfluxDB]] and data warehouses [[Snowflake]]/[[GoogleBigQuery|BigQuery]]).
