---
title: "Operational Maturity (MLOps)"
type: concept
tags: [mlops, maturity, organization, architecture]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Operational Maturity (MLOps)

The systemic integration of MLOps practices (infrastructure, automation, monitoring, governance, collaboration) into a coherent whole. The distinguishing marker is **not which tools** a team adopts but **how tightly** they integrate across the ML lifecycle. [[mlsysbook-ch14-ml-operations]] defines three stages:

| Level | Characteristics | Outcomes |
|---|---|---|
| **Ad Hoc** | Manual processing, local training, no version control, unclear ownership | Fragile, hard to reproduce/debug |
| **Repeatable** | Automated training pipelines, basic CI/CD, centralized model storage, some monitoring | Improved reproducibility, limited scalability |
| **Scalable** | Fully automated workflows, integrated observability, [[InfrastructureAsCode|IaC]], governance | High reliability, rapid iteration, production-grade |

The leap from Ad Hoc to Scalable is **architectural** (isolated scripts → cohesive system), typically 3–6 months engineering per transition. The "uptime iceberg" frames it: visible uptime sits atop hidden threats (data drift, concept drift, broken pipelines, schema changes, bias, underperforming segments) spanning data/model/service health. Single-model MLOps investment runs ~$20–65K/year + 1–2 FTE-months; the worked single-model ROI example is **4.5×**. Guidance: invest proportional to model criticality; start with monitoring + CI/CD (highest ROI). Distinct from the [[MLTestScore|ML Test Score]], which assesses individual practices rather than their integration.

## Connections
- [[MLOps]] — the discipline maturity measures.
- [[MLTestScore]] — practice-level rubric (vs. system-level maturity).
- [[InfrastructureAsCode]] / [[CICD]] / [[FeatureStore]] / [[ModelMonitoring]] — the integrating components.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
