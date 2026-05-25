---
title: "AI Pipeline Orchestration"
type: concept
tags: [architecture, orchestration, llm-app, pipeline]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# AI Pipeline Orchestration

**The specific kind of orchestration concerned with chaining the steps of an AI application — query processing → retrieval → prompt assembly → model call → evaluation → response or escalation.** Per [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]]: *"An orchestrator helps you specify how these different components work together to create an end-to-end pipeline."*

Ch 10 draws a sharp boundary: *"An AI pipeline orchestrator is different from a general workflow orchestrator, like [[Airflow]] or [[Metaflow]]."* AI orchestrators are tuned for synchronous user-facing inference pipelines with retrieval, tool use, and conditional branching; workflow orchestrators are tuned for asynchronous DAG-shaped batch jobs.

## Two responsibilities

### Components definition

*"You need to tell the orchestrator what components your system uses, including different models, external data sources for retrieval, and tools that your system can use."* A [[ModelGateway|model gateway]] makes adding a model easier. Evaluation and monitoring tools can also register here.

### Chaining

*"Chaining is basically function composition: it combines different functions (components) together."* The canonical chain:

1. Process the raw query.
2. Retrieve relevant data.
3. Combine query + data into a prompt.
4. Generate.
5. Evaluate.
6. Return to user, or route to human operator if the response is poor.

The orchestrator passes data between components and *"should provide tooling that helps ensure that the output from the current step is in the format expected by the next step"* — and notify on data-mismatch / component failures.

## Named tools (Ch 10)

[[LangChain]], [[LlamaIndex]], [[Flowise]], [[Langflow]], [[Haystack]]. Many RAG and agent frameworks are also AI orchestrators by absorption.

## The start-simple warning

> *"While it's tempting to jump straight to an orchestration tool when starting a project, you might want to start building your application without one first. Any external tool brings additional complexity. An orchestrator can abstract away critical details of how your system works, making it hard to understand and debug your system."* — Ch 10

This is in line with Huyen's broader start-simple stance from the [[ai-engineering-chip-huyen|book's preface]].

## Three evaluation axes

1. **Integration and extensibility** — does it support your current and likely-future components? How hard is it to add an unsupported one?
2. **Support for complex pipelines** — branching, parallelism, error handling.
3. **Ease of use, performance, scalability** — intuitive APIs, docs, community, no hidden API calls or latency penalties, scales with traffic and team size.

## Parallelism for strict-latency apps

> *"When designing the pipeline for an application with strict latency requirements, try to do as much in parallel as possible. For example, if you have a routing component (deciding where to send a query) and a PII removal component, both can be done at the same time."* — Ch 10

The independent-components observation is the orchestrator-specific instance of the architecture-wide latency lever.

## Boundary with gateway and other layers

The orchestrator vs gateway boundary is fluid:

> *"Because of this, some orchestrator tools want to be gateways. In fact, so many tools seem to want to become end-to-end platforms that do everything."* — Ch 10, footnote

Strictly, the orchestrator owns the *chain*; the [[ModelGateway|gateway]] owns the *model API surface*. Many products absorb both.

## Distinction from the wiki's existing [[Orchestrator]]

The [[Orchestrator]] page in this wiki covers the **MLOps pipeline orchestrator** ([[ZenML]] / [[Airflow]] / [[Prefect]] / [[Dagster]] / [[Metaflow]] / [[Kubeflow]] / [[ArgoWorkflows]]) — the *training pipeline* class. AI pipeline orchestration is the *inference pipeline* sibling. Both schedule steps; the AI variant operates at request latency and is closer to a routing / function-composition layer than to a DAG scheduler.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[Orchestrator]] — the MLOps sibling concept.
- [[LangChain]] / [[LlamaIndex]] / [[Flowise]] / [[Langflow]] / [[Haystack]] — named tools.
- [[ModelGateway]] — adjacent layer with overlapping ambitions.
- [[ModelRouter]] / [[ContextConstruction]] / [[Agent]] — components an AI orchestrator chains.
- [[ai-engineering-chip-huyen]] — start-simple stance from the parent.
