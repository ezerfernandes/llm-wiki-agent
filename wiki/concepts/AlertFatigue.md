---
title: "Alert Fatigue"
type: concept
tags: [mlops, monitoring, on-call, operations]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Alert Fatigue

The tendency to ignore or dismiss alerts after experiencing too many false positives — a significant operational risk that erodes [[OnCallRotation|on-call]] effectiveness even when monitoring is technically sound. Teams combat it through:

- **Consolidation** — grouping related alerts (e.g., multiple features drifting at once → one notification, not dozens).
- **Adaptive thresholds** — accounting for weekly/seasonal patterns so predictable variation does not page anyone.
- **Actionability measurement** — alerts acted upon < 10% of the time should be retired or recalibrated.
- **Accountability for silencing** — requiring a follow-up ticket before snoozing prevents permanent suppression.

Described in [[mlsysbook-ch14-ml-operations]] (mlsysbook Vol 1, Ch 14).

## Connections
- [[OnCallRotation]] — the practice alert fatigue degrades.
- [[IncidentResponse]] / [[ModelMonitoring]] — alerting context.
- [[Observability]] — monitoring-cost trade-offs feed alert design.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
