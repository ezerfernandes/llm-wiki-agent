---
title: "Pydantic"
type: entity
tags: [tool, library, python, validation, typing, open-source]
sources: [leh-ch03-data-engineering, leh-ch04-rag-feature-pipeline, leh-ch10-inference-pipeline-deployment, dspy-customer-service-agent, dspy-email-extraction-tutorial, dspy-mcp-tutorial, agentic-design-patterns-ch18-guardrails, agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
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

## As a guardrail (Agentic Design Patterns Ch 18)
[[AntonioGulli|Gulli's]] [[AgenticDesignPatterns|*Agentic Design Patterns*]] [[agentic-design-patterns-ch18-guardrails|Ch 18 (Guardrails/Safety Patterns)]] uses a Pydantic `BaseModel` as a **technical [[Guardrail|guardrail]]** in its [[crewai|CrewAI]] content-policy-enforcer example: `class PolicyEvaluation(BaseModel)` declares `compliance_status: str`, `evaluation_summary: str`, and `triggered_policies: List[str]` (each a `Field(description=...)`), and the task's `output_pydantic=PolicyEvaluation` instructs CrewAI to structure and validate the LLM policy-enforcer's JSON verdict against it. A `validate_policy_evaluation` function then `PolicyEvaluation.model_validate(data)`-checks the parsed output (catching `ValidationError`/`JSONDecodeError`) before the agent acts — *"this function acts as a technical guardrail, ensuring the LLM's output is correctly formatted."* See [[SchemaValidation]] / [[Guardrail]] — the constrain-and-validate use of Pydantic for LLM safety/[[ContentModeration|moderation]].

## As an object-oriented facade for LLM output (Agentic Design Patterns Appendix A)
[[agentic-design-patterns-appendix-a-prompting|Appendix A]] presents Pydantic as the recommended way to enforce [[StructuredOutputs|structured output]] from an LLM: define a `BaseModel` (typed fields + `Field(description=...)`) as an *"object-oriented facade to the prompt's output,"* then parse the model's JSON string directly into a validated instance in a **single step** with `User.model_validate_json(llm_output_json)` — combining JSON parsing and validation, raising `ValidationError` on malformed or type-mismatched data. For XML, `xmltodict` converts XML → dict for the same Pydantic path (using `Field` aliases). This *"parse, don't validate at component boundaries"* discipline makes LLM components reliably interoperable with the rest of a system.

## Connections
- [[StructuredOutputs]] / [[agentic-design-patterns-appendix-a-prompting]] — Appendix A's `model_validate_json` object-oriented-facade pattern for LLM output.
- [[Guardrail]] / [[SchemaValidation]] / [[crewai|CrewAI]] — Ch 18 `PolicyEvaluation(BaseModel)` as a structured-output guardrail (`output_pydantic=` + `model_validate`).
- [[FastAPI]] — built on Pydantic for schema validation.
- [[MongoDB]] — `NoSQLBaseDocument` wraps `pymongo` with Pydantic types.
- [[Qdrant]] — `VectorBaseDocument` wraps Qdrant points with Pydantic types.
- [[SQLAlchemy]] / [[SQLModel]] — ORM analogues (SQLModel is built on Pydantic).
- [[Python]] — language.
- [[DSPySignatures]] / [[DSPyAdapters]] — Pydantic models compose as tier-three types in DSPy.
