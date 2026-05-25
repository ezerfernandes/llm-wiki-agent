---
title: "JSON"
type: concept
tags: [api, serialization, formats]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
**JSON** (JavaScript Object Notation) is a text-based data interchange format consisting of nested objects, arrays, strings, numbers, booleans, and nulls. It is the dominant wire format for REST APIs and the default payload format for LLM completion APIs, structured-output prompting modes, and prompt-monitoring traces.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] uses JSON throughout: the [[FastAPI]] business microservice exchanges JSON request/response bodies via [[Pydantic]] schemas; the SageMaker `invoke_endpoint` call sets `ContentType="application/json"` and serializes the LLM payload as `{"inputs": "...", "parameters": {...}}`; and TGI's `HF_MODEL_QUANTIZE`, `HF_MODEL_ID`, and similar environment variables are stringified through `json.dumps(...)` before being passed to the SageMaker SDK. The chapter contrasts JSON (text, slow, human-readable) with [[Protobuf]] (binary, fast, schema-typed) when discussing [[gRPC]] for internal-service communication.

## Key details
- Text-based — human-readable and language-agnostic.
- Slower than binary formats due to text parsing.
- The default response format for the `response_format={"type": "json_object"}` mode in OpenAI's API.
- LLM-side structured-output libraries (Outlines, Instructor) constrain decoding to valid JSON.
- The wire format for almost all LLM completion APIs.

## Connections
- [[REST]] / [[RESTAPI]] — the protocols where JSON dominates.
- [[Protobuf]] — the binary, schema-typed alternative.
- [[gRPC]] — the protocol that prefers Protobuf over JSON.
- [[FastAPI]] / [[Pydantic]] — the Python stack used to define JSON-validated schemas.
- [[Outlines]] — structured-output library that constrains decoding to JSON.
- [[LLMAsAJudge]] — uses JSON mode for structured judge outputs.
