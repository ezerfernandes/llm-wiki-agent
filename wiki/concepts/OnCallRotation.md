---
title: "On-Call Rotation (ML Systems)"
type: concept
tags: [mlops, operations, on-call, reliability]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# On-Call Rotation (ML Systems)

The practice of ensuring someone with appropriate expertise is always available to respond to production ML failures. ML on-call requires specialized practices beyond traditional software ops because ML incidents manifest as **gradual degradation** rather than hard failures: an engineer facing a 3% accuracy drop must first decide whether it is statistical noise, legitimate [[ConceptDrift|concept drift]], or a critical failure requiring rollback — demanding statistical context, not log analysis. Compounded by delayed impact visibility (Monday's worse recommendations may not move revenue until Friday) and cross-system dependencies (data issues owned by other teams).

**Tiered escalation** ([[mlsysbook-ch14-ml-operations]]): Tier 1 (ML engineer — triage, runbooks), Tier 2 (senior ML eng / data scientist — complex debugging), Tier 3 (platform lead — architecture, vendor escalation), plus a **parallel data on-call** (data engineer) because data issues cause most incidents. Effectiveness depends on runbook quality (purpose, ownership, normal operating ranges, diagnostic commands, escalation/rollback procedures), combatting [[AlertFatigue|alert fatigue]], structured shift handoffs, and burnout mitigation (limit consecutive on-call to 3–4 days, comp time after high-severity incidents).

## Connections
- [[IncidentResponse]] — what on-call engineers execute.
- [[ModelDebugging]] — the diagnostic toolkit.
- [[AlertFatigue]] — a primary operational risk.
- [[ModelMonitoring]] — the signals on-call responds to.
- [[MLOps]] — production-operations practice.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
