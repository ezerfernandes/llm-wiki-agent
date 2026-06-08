---
title: "Splunk"
type: entity
tags: [tool, observability, monitoring, logging]
sources: [agentic-design-patterns-ch19-evaluation]
last_updated: 2026-06-07
---

# Splunk

**Splunk** is an observability, log-management, and operational-intelligence platform for searching, monitoring, and analyzing machine-generated data (logs, metrics, traces) at scale.

[[agentic-design-patterns-ch19-evaluation|*Agentic Design Patterns* Ch 19]] names Splunk (alongside [[Datadog]] and [[Grafana|Grafana Cloud]]) as an **observability platform** for persisting agent **latency telemetry** rather than printing it to the console — one of the recommended sinks for the [[EvaluationAndMonitoring|Evaluation and Monitoring]] pattern, alongside time-series DBs ([[Prometheus]], [[InfluxDB]]) and data warehouses ([[Snowflake]], [[GoogleBigQuery|BigQuery]]).

## Connections
- [[EvaluationAndMonitoring]] — Ch 19's recommended observability sink for agent latency metrics.
- [[Datadog]] / [[Grafana]] — peer observability platforms named together in Ch 19.
- [[observability]] / [[Monitoring]] — the disciplines it serves.
