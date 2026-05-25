---
title: "observability"
type: concept
tags: [mlops, operations, monitoring, ai-engineering]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# observability

**Observability** is the practice of instrumenting a system so that, when something goes wrong, *the system's external outputs (logs, metrics, traces) are sufficient to infer what went wrong internally* — without shipping new code to inspect. Distinct from **[[Monitoring|monitoring]]**, which only tracks external signals without committing to that internal-inferability property.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

[[ai-engineering-ch10-architecture-feedback|Ch 10]] adopts the industry's mid-2010s reframe from "monitoring" to "observability":

> *"Monitoring makes no assumption about the relationship between the internal state of a system and its outputs. … Observability, on the other hand, makes an assumption stronger than traditional monitoring: that a system's internal states can be inferred from knowledge of its external outputs. When something goes wrong with an observable system, we should be able to figure out what went wrong by looking at the system's logs and metrics without having to ship new code to the system."* — Ch 10

### Ch 10's terminology convention

Ch 10 uses *"monitoring"* to refer to the **act** of tracking system information, and *"observability"* to refer to the **whole process** of instrumenting, tracking, and debugging. The latter subsumes the former plus the instrumentation discipline that makes tracking diagnostic-grade.

### Three observability-quality metrics

Ch 10 imports the DevOps three:

- **[[MTTD]]** — mean time to detection.
- **[[MTTR]]** — mean time to response.
- **[[ChangeFailureRate|CFR]]** — change failure rate. *"If you don't know your CFR, it's time to redesign your platform to make it more observable."*

### AI-app-specific failure modes

Foundation-model applications introduce failure modes outside traditional observability scope:

- [[Hallucination|Hallucination]] — wrong but well-formed outputs that don't crash anything.
- [[SilentModelUpdate|Silent model updates]] — behavior change behind a stable endpoint.
- System-prompt drift, user-behavior drift ([[DriftDetection]]).
- Format failures, refusal-rate shifts, token-distribution drift.

These require AI-specific metrics design (factual-consistency scoring, refusal-rate tracking, output-length distribution monitoring), AI-specific [[RequestTrace|tracing]] (component-by-component request paths), and the *"log everything"* discipline Ch 10 advocates.

### Logs vs traces

- **Logs** — append-only event records. Answer *"what happened at time T?"*
- **[[RequestTrace|Traces]]** — reconstructed timelines linking related events. Answer *"what happened to this request?"*

Both are required; neither suffices alone.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[Monitoring]] / [[ModelMonitoring]] — sibling / sub-concepts.
- [[MTTD]] / [[MTTR]] / [[ChangeFailureRate]] — the three observability-quality metrics.
- [[RequestTrace]] / [[Logging]] / [[StructuredLogging]] — the substrate.
- [[DriftDetection]] / [[SilentModelUpdate]] — AI-specific failure modes.
- [[LangSmith]] — Ch 10's named tracing tool (Figure 10-11).
- [[DataObservability]] — the data-pipeline-side sibling.
