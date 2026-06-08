---
title: "Vertex AI Extensions"
type: concept
tags: [agents, tools, google, vertex-ai, function-calling, code-execution, enterprise, agentic-design-patterns]
sources: [agentic-design-patterns-ch05-tool-use]
last_updated: 2026-06-07
---

# Vertex AI Extensions

A **Vertex AI extension** is a structured API wrapper that enables a model to connect with external APIs for real-time data processing and action execution. Introduced in [[agentic-design-patterns-ch05-tool-use|Chapter 5 (Tool Use)]] of [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]], extensions are [[google|Google]]'s enterprise-oriented realization of the [[ToolUse|tool-use]] capability on the [[GoogleCloudVertexAI|Vertex AI]] platform.

## What they offer
- **Enterprise-grade security, data privacy, and performance guarantees** — the value proposition over raw [[FunctionCalling|function calling]].
- **Prebuilt extensions** for common use cases, including **Code Interpreter** (see [[CodeInterpreter]]) and **Vertex AI Search** (querying private datastores) — plus the option to create custom ones.
- Use across tasks like generating and running code, querying websites, and analyzing information from private datastores.
- Strong enterprise controls and seamless integration with other Google products.

## Extensions vs function calling — the execution axis
The chapter's load-bearing distinction is **who executes the tool**:

| | [[VertexAIExtensions|Vertex AI extension]] | [[FunctionCalling|Function calling]] |
|---|---|---|
| **Execution** | **Vertex AI automatically executes** the extension | The **client/orchestration layer manually executes** the function call |
| **Security/governance** | Enterprise-grade, platform-managed | Application's responsibility |
| **Setup** | Platform-integrated wrapper | Per-framework tool wrapper ([[LangChain]] `@tool`, etc.) |

> *"The key difference between extensions and function calling lies in their execution: Vertex AI automatically executes extensions, whereas function calls require manual execution by the user or client."*

## Related: VSearchAgent (Enterprise search)
Chapter 5's enterprise-search example uses [[GoogleADK|Google ADK]]'s **`VSearchAgent`** — an agent that answers questions by searching a specified **[[GoogleCloudVertexAI|Vertex AI Search]] datastore** (`datastore_id`), streaming the response token-by-token and surfacing source **grounding metadata** (source attributions) from the datastore. This is the RAG-flavored tool-use pattern wired through Vertex's managed search rather than a hand-built retriever.

## Connections
- [[ToolUse]] — extensions are an enterprise realization of the tool-use pattern.
- [[FunctionCalling]] — the manual-execution counterpart; extensions differ on who executes.
- [[GoogleCloudVertexAI]] — the platform; hosts extensions, Vertex AI Search datastores, and `VSearchAgent`.
- [[GoogleADK]] — provides `VSearchAgent` and `built_in_code_execution`; ADK tools map onto Vertex prebuilt extensions.
- [[CodeInterpreter]] — a prebuilt Vertex extension (Code Interpreter).
- [[google|Google]] — the vendor.
- [[agentic-design-patterns-ch05-tool-use]] — source.
