---
name: Prometheus
title: "Prometheus"
type: entity
tags: [tool, monitoring, observability, open-source]
sources: [mlsysbook-ch14-ml-operations, agentic-design-patterns-ch19-evaluation]
last_updated: 2026-06-07
---

# Prometheus

An open-source monitoring and time-series metrics system, used (with [[Grafana]] and Elastic) to collect, aggregate, and visualize operational metrics for ML systems. Its **pull-based model** — a central server scrapes metrics from target systems — enables the aggregated operational dashboard view used for thermal-aware scheduling and drift alerting in [[mlsysbook-ch14-ml-operations]] (mlsysbook Vol 1, Ch 14). A typical scrape interval of 15–60 seconds dictates the system's reaction time to events; finer granularity (per-accelerator thermals) costs more data but catches component-level throttling that server-level aggregates would mask. Production-grade setups maintain redundant/secondary collectors so monitoring failures do not leave teams operating blind.

[[agentic-design-patterns-ch19-evaluation|*Agentic Design Patterns* Ch 19]] names Prometheus (with [[InfluxDB]]) as a **time-series database** for persisting agent latency telemetry under the [[EvaluationAndMonitoring|Evaluation and Monitoring]] pattern.

## Connections
- [[EvaluationAndMonitoring]] — Ch 19's recommended time-series sink for agent latency metrics.
- [[Grafana]] — the dashboard layer typically paired with Prometheus.
- [[ModelMonitoring]] / [[Observability]] — the disciplines it serves.
- [[Autoscaling]] — utilization metrics feed scaling decisions.
- [[MLOps]] — production-operations tooling.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
