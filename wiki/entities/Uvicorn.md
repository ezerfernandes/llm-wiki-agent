---
title: "Uvicorn"
type: entity
tags: [tool, web-server, asgi, python, open-source]
sources: [leh-ch10-inference-pipeline-deployment, dspy-deployment-tutorial]
last_updated: 2026-05-24
---

## What it is
Uvicorn is a lightning-fast ASGI server for Python, built on `uvloop` and `httptools`. It is the recommended production server for [[FastAPI]] and other ASGI frameworks.

## In LLM Engineer's Handbook
Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) runs the FastAPI business microservice under Uvicorn — `uvicorn tools.ml_service:app --host 0.0.0.0 --port 8000 --reload` — wired up via the `poetry poe run-inference-ml-service` task. This is the local-dev surface for the `/rag` endpoint; productionization to AWS EKS/ECS is left to Chapter 11.

## In DSPy

[[dspy-deployment-tutorial|The DSPy Deployment tutorial]] uses Uvicorn as the ASGI runner for its [[FastAPI]]-fronted DSPy program — `uvicorn fastapi_dspy:app --reload`. The pattern is identical to the LLM Twin receipt (Uvicorn → FastAPI → application code); the difference is the application code is a `dspy.asyncify`-wrapped [[chainofthought|`dspy.ChainOfThought`]] program instead of a [[rag|RAG]] microservice.

## Connections
- [[FastAPI]] — the framework Uvicorn runs.
- [[Python]] — language.
- [[AmazonEKS]] / [[AmazonECS]] — production deployment targets for the FastAPI app.
- [[PoeThePoet]] — wraps the uvicorn invocation as a task.
- [[DSPyAsync]] — `dspy.asyncify(...)` is the wrapper that makes a sync DSPy program awaitable inside the Uvicorn-served async handler.
