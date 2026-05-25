---
title: "Step (MLOps Pipeline Step)"
type: concept
tags: [mlops, orchestration, architecture]
sources: [leh-ch02-tooling-and-installation, leh-ch03-data-engineering, leh-ch04-rag-feature-pipeline]
last_updated: 2026-05-22
---

## Definition
A **step** in an MLOps pipeline is an atomic unit of computation — typically a Python function decorated with `@step` — that takes typed inputs, produces typed outputs (versioned as [[Artifact|artifacts]]), and forms a node in the pipeline's [[DirectedAcyclicGraph|DAG]]. Steps are the unit of caching, retry, and observability inside an orchestrator like [[ZenML]].

## In LLM Engineer's Handbook
[[leh-ch02-tooling-and-installation]] introduces the step primitive: `@step def get_or_create_user(user_full_name) -> Annotated[UserDocument, "user"]: ...`. The chapter explains that ZenML's typed return signatures auto-version step outputs as artifacts and allow user-attached metadata via `step_context.add_output_metadata(...)`. [[leh-ch03-data-engineering]] uses two steps (`get_or_create_user`, `crawl_links`) to compose the data collection pipeline; [[leh-ch04-rag-feature-pipeline]] uses five (`query_data_warehouse`, `clean_documents`, `chunk_and_embed`, plus two `load_to_vector_db` invocations). The book argues step granularity is a developer judgment call — too coarse loses observability and caching benefits; too fine creates artifact-tracking overhead.

## Key details
- Step input/output types are declared via Python type hints + `Annotated[...]`; ZenML uses these to generate artifact names.
- Each step run produces a versioned artifact that downstream steps reference by ID.
- Step caching skips re-execution when inputs and code are unchanged.
- Steps can attach user metadata to their outputs (e.g., dataset categories, sample counts).
- Failure in one step does not invalidate completed upstream artifacts.

## Connections
- [[Pipeline]] — the structure steps compose.
- [[Artifact]] — the versioned output produced by a step.
- [[Orchestrator]] — runs steps in DAG order.
- [[Materializer]] — the serializer extension point ZenML uses to persist step inputs/outputs.
- [[ZenML]] — concrete orchestrator using the `@step` decorator.
- [[DirectedAcyclicGraph]] — runtime structure inside which steps execute.
