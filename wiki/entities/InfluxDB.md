---
title: "InfluxDB"
type: entity
tags: [tool, database, time-series, monitoring, observability]
sources: [agentic-design-patterns-ch19-evaluation]
last_updated: 2026-06-07
---

# InfluxDB

**InfluxDB** is an open-source **time-series database** purpose-built for storing and querying timestamped metrics, events, and sensor/telemetry data at high write throughput.

[[agentic-design-patterns-ch19-evaluation|*Agentic Design Patterns* Ch 19]] names InfluxDB (alongside [[Prometheus]]) as a **time-series database** option for persisting agent **latency telemetry** under the [[EvaluationAndMonitoring|Evaluation and Monitoring]] pattern — preferable to console-printing, and complementary to data warehouses ([[Snowflake]], [[GoogleBigQuery|BigQuery]]) and observability platforms ([[Datadog]], [[Splunk]], [[Grafana]]).

## Connections
- [[EvaluationAndMonitoring]] — Ch 19's recommended time-series sink for agent latency metrics.
- [[Prometheus]] — peer time-series metrics system named together in Ch 19.
- [[observability]] / [[Monitoring]] — the disciplines it serves.
