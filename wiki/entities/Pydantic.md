---
title: "Pydantic"
type: entity
tags: [tool, library, python, validation, typing, open-source]
sources: [leh-ch03-data-engineering, leh-ch04-rag-feature-pipeline, leh-ch10-inference-pipeline-deployment, dspy-customer-service-agent, dspy-email-extraction-tutorial, dspy-mcp-tutorial]
last_updated: 2026-05-24
---

## What it is
Pydantic is a Python library for data validation and settings management using Python type hints. Its `BaseModel` class provides typed fields with automatic validation, JSON (de)serialization, and integration with FastAPI for request/response schemas.

## In LLM Engineer's Handbook
Pydantic is the typed-schema backbone of the LLM Twin codebase. Ch. 3 ([[leh-ch03-data-engineering]]) builds `NoSQLBaseDocument(BaseModel, Generic[T], ABC)` on top of Pydantic so that every domain document (`ArticleDocument`, `PostDocument`, `RepositoryDocument`, `UserDocument`) has typed fields with validation — "By leveraging Python packages such as Pydantic, we have out-of-the-box type validation, which ensures consistency in our datasets." Ch. 4 ([[leh-ch04-rag-feature-pipeline]]) extends the pattern with `VectorBaseDocument(BaseModel, Generic[T], ABC)` for the Object-Vector Mapping layer, plus a `Settings` class for `.env`-driven configuration. Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) uses Pydantic for the FastAPI `QueryRequest` / `QueryResponse` schemas exposed by the `/rag` endpoint.

## In DSPy

Pydantic is the **tier-three type** in [[DSPySignatures|DSPy's five-tier type system]] ([[dspy-signatures|page 4]]) — arbitrary `BaseModel` subclasses can be used as `InputField` or `OutputField` types, and the [[DSPyAdapters|Adapter]] serializes them in/out of the LM. Two wiki-corpus DSPy tutorials exercise this surface:

- [[dspy-customer-service-agent]] — five-class Pydantic domain (`Date`, `UserProfile`, `Flight`, `Itinerary`, `Ticket`) wired as tool argument and return types in a [[react|`dspy.ReAct`]] agent. Demonstrates **nested composition** — `Itinerary ⊃ Flight + UserProfile`, `Flight ⊃ Date`.
- [[dspy-email-extraction-tutorial]] — `class ExtractedEntity(BaseModel): entity_type: str; value: str; confidence: float` used as `list[ExtractedEntity]` in OutputField and InputField across four Signatures. **First wiki-corpus DSPy receipt embedding LM-self-reported confidence scores in a structured output**.
- [[dspy-mcp-tutorial]] — same five-class airline domain as [[dspy-customer-service-agent]] (`Date` / `UserProfile` / `Flight` / `Itinerary` / `Ticket`), but now serialized through the [[ModelContextProtocol|MCP]] wire protocol via [[FastMCP]]'s automatic JSON Schema generation. **First wiki-corpus receipt of a Pydantic model crossing a JSON serialization boundary inside a DSPy tool** — the tutorial's `pick_flight` body uses a `x.get(...) if isinstance(x, dict) else x.attr` double-dispatch to accommodate the round-trip downgrade from `BaseModel` to `dict`.

## Connections
- [[FastAPI]] — built on Pydantic for schema validation.
- [[MongoDB]] — `NoSQLBaseDocument` wraps `pymongo` with Pydantic types.
- [[Qdrant]] — `VectorBaseDocument` wraps Qdrant points with Pydantic types.
- [[SQLAlchemy]] / [[SQLModel]] — ORM analogues (SQLModel is built on Pydantic).
- [[Python]] — language.
- [[DSPySignatures]] / [[DSPyAdapters]] — Pydantic models compose as tier-three types in DSPy.
