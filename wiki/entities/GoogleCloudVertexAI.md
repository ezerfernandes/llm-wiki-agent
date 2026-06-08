---
title: "Google Cloud Vertex AI"
type: entity
tags: [product, google-cloud, mlops, cloud, llm-api]
sources: [leh-ch10-inference-pipeline-deployment, agentic-design-patterns-ch01-prompt-chaining, agentic-design-patterns-ch05-tool-use, agentic-design-patterns-ch08-memory-management, agentic-design-patterns-ch14-rag, agentic-design-patterns-ch18-guardrails]
last_updated: 2026-06-07
---

## What it is
Google Cloud Vertex AI is Google Cloud's unified MLOps and AI platform — managed training, model registry, endpoints, batch prediction, and access to Google's Gemini and PaLM model families.

## In LLM Engineer's Handbook
Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) lists Vertex AI as one of the alternative model-serving platforms one might use instead of [[AmazonSageMaker]] for the LLM Twin endpoint.

## Vertex AI prompt optimizer (Agentic Design Patterns Ch 1)
[[agentic-design-patterns-ch01-prompt-chaining|Ch 1]] of [[AgenticDesignPatterns|*Agentic Design Patterns*]] cites the **Vertex AI prompt optimizer** as a tool for automating [[ContextEngineering|context engineering]] at scale: given sample prompts, system instructions, and a template, it *"systematically evaluat[es] responses against a set of sample inputs and predefined evaluation metrics"* to programmatically refine prompts and system instructions across different models without manual rewriting — implementing the feedback loops needed for sophisticated context engineering. ([Vertex Prompt Optimizer docs](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-optimizer).)

## Tool use: Vertex AI Search & Extensions (Agentic Design Patterns Ch 5)
[[agentic-design-patterns-ch05-tool-use|Ch 5 (Tool Use)]] surfaces two Vertex tool capabilities. (1) **Vertex AI Search** — a managed datastore an agent can query for grounded answers; [[GoogleADK|ADK]]'s `VSearchAgent` (`datastore_id=...`) streams responses with source **grounding metadata** from the datastore (the enterprise-RAG tool-use pattern). (2) **[[VertexAIExtensions|Vertex AI extensions]]** — structured API wrappers (e.g., Code Interpreter, Vertex AI Search) with enterprise-grade security; their defining trait is that **Vertex AI auto-executes** them, whereas [[FunctionCalling|function calls]] require manual client execution. See [[ToolUse]] / [[VertexAIExtensions]].

## Memory Bank: managed agent memory (Agentic Design Patterns Ch 8)
[[agentic-design-patterns-ch08-memory-management|Ch 8 (Memory Management)]] presents the **Vertex AI Agent Engine's [[VertexAiMemoryBank|Memory Bank]]** — a managed [[LongTermMemory|long-term-memory]] service for agents. [[gemini|Gemini]] models asynchronously analyze conversation histories to extract key facts and user preferences, store them scoped by user ID (intelligently consolidating and resolving contradictions), and recall them on new sessions via full recall or embedding similarity. It integrates with [[GoogleADK|ADK]] out-of-the-box (`VertexAiMemoryBankService`) and with [[LangGraph]]/[[crewai|CrewAI]] via API. ADK's production long-term store, `VertexAiRagMemoryService`, is also backed by Vertex AI [[rag|RAG]]. See [[VertexAiMemoryBank]] / [[MemoryManagement]].

## RAG Engine & RAG Corpus (Agentic Design Patterns Ch 14)
[[agentic-design-patterns-ch14-rag|Ch 14 (Knowledge Retrieval / RAG)]] uses Vertex AI's **RAG Engine / RAG Corpus** as the managed semantic-retrieval backend for its second hands-on example. Via [[GoogleADK|ADK]]'s `VertexAiRagMemoryService`, an agent connects to a **Vertex AI RAG Corpus** (`RAG_CORPUS_RESOURCE_NAME = "projects/.../ragCorpora/your-corpus-id"`) with `similarity_top_k` and `vector_distance_threshold` controlling how many chunks are returned and the max semantic distance allowed — "scalable and persistent semantic knowledge retrieval from the designated RAG Corpus," integrating Google Cloud's RAG functionality into an agent for factually-[[GroundedGeneration|grounded]] responses. Gulli cites the [Vertex AI RAG Engine overview](https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview) and [RAG Corpus management](https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/manage-your-rag-corpus) docs. This is the same Vertex AI Search / RAG layer Ch 5's `VSearchAgent` taps for enterprise search. See [[rag]] / [[VectorDatabase]].

## Safety & guardrails (Agentic Design Patterns Ch 18)
[[agentic-design-patterns-ch18-guardrails|Ch 18 (Guardrails/Safety Patterns)]]'s "Hands-On Code Vertex AI Example" describes Vertex AI's multi-faceted approach to **reliable, safe agents**: establishing agent/user identity and authorization; **input and output filters**; tools with **embedded safety controls and predefined context**; **built-in [[gemini|Gemini]] safety features** (content filters + system instructions); and **validating model and tool invocations through callbacks** (the same `before_tool_callback` mechanism shown in [[GoogleADK|ADK]]). Recommended robust-safety practices: use a **less computationally intensive model (e.g. Gemini Flash Lite)** as an extra pre-screening safeguard ([[Guardrail|guardrail]]); employ **isolated code-execution environments** ([[LocalSandbox]]/[[CodeInterpreter]]); rigorously evaluate and monitor agent actions ([[EvaluationAndMonitoring]]); restrict agent activity within secure network boundaries via **VPC Service Controls** ([[PrincipleOfLeastPrivilege|least privilege]]); conduct a risk assessment before deployment; and **sanitize all model-generated content before displaying it in UIs** to prevent malicious code execution in browsers ([[InputSanitization]]). See [[Guardrail]].

## Connections
- [[Guardrail]] / [[PrincipleOfLeastPrivilege]] / [[agentic-design-patterns-ch18-guardrails]] — Ch 18: Gemini safety features, callbacks, isolated execution, VPC Service Controls, Flash-Lite pre-screen.
- [[rag]] / [[agentic-design-patterns-ch14-rag]] — Vertex AI RAG Engine / RAG Corpus as the `VertexAiRagMemoryService` retrieval backend.
- [[google]] — operator.
- [[VertexAiMemoryBank]] / [[MemoryManagement]] — managed agent long-term memory (Agent Engine).
- [[agentic-design-patterns-ch08-memory-management]] — source for the Memory Bank reference.
- [[gemini]] — Google's flagship model family hosted here.
- [[ToolUse]] / [[VertexAIExtensions]] — Vertex AI Search datastore, `VSearchAgent`, and auto-executed extensions.
- [[AmazonSageMaker]] — peer / chosen alternative.
- [[AzureML]] — peer hyperscaler MLOps platform.
- [[ModelServing]] — capability.
- [[ContextEngineering]] / [[PromptOptimization]] — the Vertex AI prompt optimizer use case.
- [[GoogleADK]] — Google's agent framework on the same AI stack.
- [[agentic-design-patterns-ch01-prompt-chaining]] — source for the prompt-optimizer reference.
