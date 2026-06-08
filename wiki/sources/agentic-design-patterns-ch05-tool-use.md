---
title: "Chapter 5 — Tool Use / Function Calling (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, tool-use, function-calling, tool-calling, json-schema, code-execution, langchain, crewai, google-adk, vertex-ai, control-flow]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 5 of [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] presents **[[ToolUse|Tool Use]]** (commonly implemented as **[[FunctionCalling|Function Calling]]**) as the fifth pattern and the first that lets an agent reach *outside* its own reasoning loop. Where the prior four patterns ([[PromptChaining|chaining]], [[Routing|routing]], [[Parallelization|parallelization]], [[Reflection|reflection]]) only orchestrated the LLM's internal workflow, Tool Use connects the agent to external APIs, databases, services, and code execution — turning "a text generator into an agent capable of sensing, reasoning, and acting in the digital or physical world." The chapter formalizes a six-step loop (tool definition → LLM decision → function-call generation → tool execution → observation → LLM processing), broadens "function calling" to the more expansive notion of **"tool calling"** (a tool can be a function, an API, a database query, or even another agent), and walks four hands-on framework examples: [[LangChain]] (`@tool` + `create_tool_calling_agent` + `AgentExecutor` on [[gemini|Gemini]]), [[CrewAI]] (`@tool` `get_stock_price` consumed by a Senior Financial Analyst agent), and [[GoogleADK|Google ADK]] (pre-built `google_search`, sandboxed `built_in_code_execution`/`BuiltInCodeExecutor`, and `VSearchAgent` over a [[GoogleCloudVertexAI|Vertex AI Search]] datastore). It closes by contrasting [[VertexAIExtensions|Vertex AI extensions]] (auto-executed by the platform) with function calls (manually executed by the client). (Agentic Design Patterns, PDF pp 79–99.)

## Key Claims
- **Tool Use is the bridge between reasoning and the world.** Function calling "is the technical mechanism that bridges the gap between the LLM's reasoning capabilities and the vast array of external functionalities available," breaking the limitations of static training data and enabling real-time information, exact calculation, user-specific data access, and real-world actions.
- **A canonical six-step loop.** (1) **Tool Definition** — declare each external function's name, purpose, and typed parameters; (2) **LLM Decision** — given the request and the tool definitions, the LLM decides whether one or more tools are needed; (3) **Function Call Generation** — the LLM emits a structured output (usually a JSON object) naming the tool and its arguments extracted from the request; (4) **Tool Execution** — the agentic/orchestration layer intercepts the structured output and runs the actual external function; (5) **Observation/Result** — the tool's output is returned to the agent; (6) **LLM Processing (optional but common)** — the LLM consumes the result to produce a final answer or to decide the next step (another tool call, reflection, etc.).
- **"Tool calling" > "function calling."** While "function calling" describes invoking predefined code functions, the broader "tool calling" framing acknowledges that a tool can be a traditional function, a complex API endpoint, a database request, or even *an instruction directed at another specialized agent* — letting a primary agent delegate (e.g., to an "analyst agent") and act as an orchestrator across a diverse ecosystem of digital resources and other intelligent entities.
- **The LLM never executes the tool itself.** The LLM only *generates* the structured call; the framework/orchestration layer performs the actual execution and feeds the result back — the agent-vs-tool boundary.
- **Six application categories.** Information retrieval (weather agent), interacting with databases/APIs (e-commerce inventory agent), calculations/data analysis (financial agent), sending communications (personal-assistant email agent), executing code (coding-assistant code interpreter), and controlling other systems/devices (smart-home agent).
- **Frameworks provide structured tool abstractions.** [[LangChain]], [[LangGraph]], [[GoogleADK|Google ADK]], and [[CrewAI]] all offer constructs for defining tools and binding them to LLM agents, "often leveraging the native function calling capabilities of modern LLMs like those in the Gemini or OpenAI series."
- **Tools should return clean data and raise errors, not return error strings.** CrewAI best-practice: a refactored `get_stock_price` returns a raw `float` or raises a `ValueError` — "Raising a specific error is better than returning a string. The agent is equipped to handle exceptions and can decide on the next action."
- **Code execution as a deterministic escape hatch.** Google ADK's `built_in_code_execution`/`BuiltInCodeExecutor` gives an agent a sandboxed Python interpreter "critical for addressing problems that require deterministic logic and precise calculations, which are outside the scope of probabilistic language generation alone."
- **Extensions vs function calling differ on *who executes*.** A [[VertexAIExtensions|Vertex AI extension]] is "a structured API wrapper that enables a model to connect with external APIs for real-time data processing and action execution" with enterprise-grade security; the key difference is execution: "Vertex AI automatically executes extensions, whereas function calls require manual execution by the user or client."

## Key Quotes
> "Tool Use is what transforms a language model from a text generator into an agent capable of sensing, reasoning, and acting in the digital or physical world." — the chapter's thesis (Fig. 1)

> "A 'tool' can be a traditional function, but it can also be a complex API endpoint, a request to a database, or even an instruction directed at another specialized agent... Thinking in terms of 'tool calling' better captures the full potential of agents to act as orchestrators across a diverse ecosystem of digital resources and other intelligent entities." — broadening function calling to tool calling

> "The key difference between extensions and function calling lies in their execution: Vertex AI automatically executes extensions, whereas function calls require manual execution by the user or client." — At a Glance

> "Use the Tool Use pattern whenever an agent needs to break out of the LLM's internal knowledge and interact with the outside world." — Rule of thumb

## Connections
- [[ToolUse]] — the chapter's named pattern (this source augments that concept page with the Ch 5 six-step loop and framework survey).
- [[FunctionCalling]] — the concrete API mechanism that implements Tool Use; the chapter treats the two as near-synonyms while preferring the broader "tool calling."
- [[AgenticDesignPatterns]] — the book hub; this is its Chapter 5.
- [[AgenticDesignPattern]] — the meta-concept; Tool Use is the 5th of 21 patterns and the first to reach outside the agent's workflow.
- [[PromptChaining]] / [[Routing]] / [[Parallelization]] / [[Reflection]] — the four prior patterns that orchestrate only internal flow; Tool Use is explicitly framed against them as the pattern that adds external reach.
- [[ModelContextProtocol]] — the framework-agnostic tool-access *standard*; the chapter's "tool definition decoupled from a framework-native wrapper" idea is the conceptual seed MCP standardizes (the chapter does not name MCP, but its tool-definition/tool-consumption split is exactly what MCP formalizes).
- [[react|ReAct]] — Tool Use is the Action half of the Thought/Action/Observation loop; the chapter's six-step loop is a ReAct-shaped cycle.
- [[CodeInterpreter]] — the code-execution tool category; realized here as ADK's `built_in_code_execution`/`BuiltInCodeExecutor`.
- [[LangChain]] / [[LangGraph]] / [[CrewAI]] / [[GoogleADK]] — the four frameworks shown defining and binding tools.
- [[gemini|Gemini]] / [[openai|OpenAI]] — the LLM series whose native function-calling capabilities the frameworks leverage.
- [[GoogleCloudVertexAI|Vertex AI]] / [[VertexAIExtensions]] — the enterprise tool/extension layer; `VSearchAgent` over a Vertex AI Search datastore; extensions vs function calling.
- [[ToolInventory]] / [[KnowledgeAugmentation]] / [[CapabilityExtension]] / [[WriteAction]] — the tool taxonomy from Huyen Ch 6 that the chapter's six application categories map onto.

## Contradictions
- None found. The chapter is consistent with the wiki's existing [[ToolUse]] / [[FunctionCalling]] treatment (Huyen, Hands-On LLMs) and with [[ModelContextProtocol]]; it adds a framework-centric, hands-on perspective and the auto-execute-vs-manual-execute extensions distinction not previously recorded.
