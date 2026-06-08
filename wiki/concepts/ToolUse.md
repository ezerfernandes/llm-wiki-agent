---
title: "Tool Use"
type: concept
tags: [agents, tools, llm, tool-use, function-calling]
sources: [hands-on-llm-ch07-advanced-text-generation, ai-engineering-ch06-rag-agents, agentic-design-patterns-00-frontmatter, agentic-design-patterns-ch05-tool-use, agentic-design-patterns-ch10-mcp, agentic-design-patterns-ch12-exception-handling, agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
---

# Tool Use

**Tool use** is the general technique of giving an LLM access to external functions (calculators, search engines, APIs, code interpreters, etc.) that it can call to extend its capability surface. The **action half** of [[react|ReAct]]'s Thought / Action / Observation cycle. Treated extensively in [[hands-on-llm-ch07-advanced-text-generation|*Hands-On LLMs* Ch 7]] and [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]].

## Why tool use matters

The motivating use case Ch 7 names is calculator-assisted math — *"LLMs are notoriously bad at mathematical problems and often fail at solving simple math-based tasks but they could do much more if we provide access to a calculator."* The structural generalization: any capability the LLM lacks (precise arithmetic, real-time information, code execution, persistent storage, world-mutating actions) can be exposed as a tool.

## The three tool categories (Huyen Ch 6)

Per [[ToolInventory|Huyen Ch 6]]:

| Category | Examples | Risk profile |
|---|---|---|
| **[[KnowledgeAugmentation|Knowledge augmentation]]** | Search engines, retrievers, SQL readers, email readers | Low (read-only) |
| **[[CapabilityExtension|Capability extension]]** | Calculators, code interpreters, OCR, translators | Low / medium |
| **[[WriteAction|Write actions]]** | SQL writes, email sends, bank transfers | **High — irreversible** |

Ch 7's two-tool agent (DuckDuckGo + llm-math) lives entirely in the first two categories — *low-stakes* tools.

## Tool-use frameworks

| Framework | Tool API |
|---|---|
| [[LangChain]] | `langchain.tools.Tool(name, description, func)` — wrap any callable; `load_tools([...], llm=llm)` for built-ins |
| [[DSPy]] | `dspy.Tool(func)` — wrap any callable; `dspy.ToolCalls` as a Signature output type |
| [[ModelContextProtocol|MCP]] | Protocol-level tool descriptor (standalone tool server) |
| OpenAI / Anthropic native | `tools=[...]` in chat-completion API; JSON-schema-typed |

## The ReAct pattern

[[react|ReAct]] (Yao et al. 2022) is the canonical tool-use prompting pattern: the LLM thinks, calls a tool, observes the result, then thinks again. Ch 7's LangChain `create_react_agent` is one operationalization; `dspy.ReAct` is another.

## The safety / reliability concern

Tool use is **the surface where LLM applications can take consequential real-world actions** — and where the *"no [[humanintheloop|human in the loop]]"* problem becomes most acute. Per Ch 7's parting caveat:

> *"By creating this relatively autonomous behavior, we are not involved in the intermediate steps. As such, there is no human in the loop to judge the quality of the output or reasoning process. This double-edged sword requires a careful system design to improve its reliability."*

This is the [[CompoundErrorAccumulation|compound-error-accumulation]] argument Huyen Ch 6 makes, applied to tool-using agents specifically.

## Connections

- [[ToolInventory]] — the design surface for choosing which tools to give an agent.
- [[Agent]] / [[AgenticAI]] / [[LangChainAgent]] — the systems that use tools.
- [[react|ReAct]] — the canonical tool-use prompting pattern.
- [[FunctionCalling]] — the API surface that exposes tools.
- [[DuckDuckGoSearchResults]] / [[LLMMathTool]] — the two tools Ch 7 uses.
- [[KnowledgeAugmentation]] / [[CapabilityExtension]] / [[WriteAction]] — Huyen Ch 6's tool taxonomy.
- [[humanintheloop]] / [[CompoundErrorAccumulation]] — the reliability concerns tool use surfaces.
- [[ExceptionHandlingAndRecovery]] — failed tool calls (bad input, dead dependency, 404/500, timeout) are the central failure source Ch 12's pattern detects, handles (retry/fallback/degrade), and recovers from.
- [[hands-on-llm-ch07-advanced-text-generation]] / [[ai-engineering-ch06-rag-agents]] — primary sources.
- [[agentic-design-patterns-appendix-a-prompting]] — Gulli's Appendix A "Tool Use / Function Calling" prompting section (the `get_current_weather` example; restates that the model emits a structured JSON call and the agentic system, not the model, executes the tool).

## Agentic Design Patterns (Gulli) perspective

In [[AgenticDesignPatterns|*Agentic Design Patterns*]] ([[AntonioGulli|Gulli]]), **tool use** is both one of the seven defining characteristics of an [[AgenticAI|agentic system]] — "enabling them to interact with external APIs, databases, or services, effectively reaching out beyond their immediate canvas" — and a dedicated design pattern (the book's Chapter 5). It is the capability that turns a Level-0 reasoning engine into a Level-1 **Connected Problem-Solver** on the [[AgentComplexitySpectrum|agent-complexity spectrum]] (e.g., calling a financial API for a live stock price, or a search tool for current information). Gulli pairs tool use closely with [[ContextEngineering|context engineering]]: the agent strategically packages a tool's output into a short, focused context before feeding it to the next tool.

### Chapter 5: the six-step loop and "tool calling" ([[agentic-design-patterns-ch05-tool-use]])

[[agentic-design-patterns-ch05-tool-use|Chapter 5]] is the first pattern that reaches *outside* the agent's internal workflow — the prior four ([[PromptChaining|chaining]], [[Routing|routing]], [[Parallelization|parallelization]], [[Reflection|reflection]]) only orchestrated interactions between the LLM and its own steps. It formalizes Tool Use (commonly implemented as [[FunctionCalling|function calling]]) as a **six-step loop**:

1. **Tool Definition** — declare each external function's name, purpose, and typed parameters (the schema).
2. **LLM Decision** — given the request + tool definitions, the LLM decides whether one or more tools are needed.
3. **Function Call Generation** — the LLM emits a structured output (usually JSON) naming the tool and the arguments extracted from the request.
4. **Tool Execution** — the *agentic/orchestration layer* intercepts the structured output and runs the actual external function. **The LLM never executes the tool itself** — this is the agent-vs-tool boundary.
5. **Observation/Result** — the tool's output is returned to the agent.
6. **LLM Processing** (optional but common) — the LLM consumes the result to produce a final answer or decide the next step (another tool call, reflection, etc.).

The chapter broadens "function calling" to the more expansive **"tool calling"**: a tool can be a traditional function, *but also* a complex API endpoint, a database request, or even "an instruction directed at another specialized agent" — letting a primary agent delegate to, say, an "analyst agent" and act as an orchestrator across a diverse ecosystem of digital resources and other intelligent entities. This is the conceptual link to [[ModelContextProtocol|MCP]] as a tool-access *standard*: defining a tool once (decoupled from any one framework's wrapper) is exactly what MCP formalizes, though Ch 5 does not name MCP. The book makes that link explicit in its dedicated [[ModelContextProtocol|MCP]] chapter — [[agentic-design-patterns-ch10-mcp|Chapter 10 (MCP)]] — which casts MCP as the **standardized, dynamically-discoverable** realization of tool access (a "universal adapter" / "power outlet" for tools) as opposed to per-vendor [[FunctionCalling|function calling]], and grounds it with [[GoogleADK|Google ADK]] `MCPToolset` + [[FastMCP]] receipts.

Six application categories are given: information retrieval (weather agent), database/API interaction (e-commerce inventory), calculations/data analysis (financial agent), communications (email assistant), code execution (coding assistant → [[CodeInterpreter|code interpreter]]), and controlling systems/devices (smart-home agent).

**Frameworks shown.** All four leverage modern LLMs' native function-calling ([[gemini|Gemini]], [[openai|OpenAI]]):
- [[LangChain]] — `@tool` decorator wraps a Python function; `create_tool_calling_agent(llm, tools, prompt)` binds tools to the model; `AgentExecutor` is the runtime that invokes the agent and runs the chosen tools.
- [[CrewAI]] — `@tool("...")` decorator; tools attached to an `Agent` via `tools=[...]`. Best practice: tools return clean data (a `float`) or **raise** a `ValueError` rather than returning an error string, so the agent can handle exceptions and decide the next action.
- [[GoogleADK|Google ADK]] — ships pre-built tools (`google_search`), a sandboxed code-execution tool (`built_in_code_execution` / `BuiltInCodeExecutor`), and `VSearchAgent` over a [[GoogleCloudVertexAI|Vertex AI Search]] datastore.
- [[LangGraph]] — named alongside LangChain/ADK for defining tools and integrating them into agent workflows.

**Extensions vs function calling.** A [[VertexAIExtensions|Vertex AI extension]] is a structured API wrapper with enterprise-grade security; the distinguishing axis is *who executes* — Vertex AI auto-executes extensions, whereas function calls require manual execution by the client/orchestration layer.

## From Hands-On LLMs Ch 7

Ch 7 frames tool use as the **capability multiplier** for LLMs and the structural justification for the **Agents** section: *"agents are systems that leverage a language model to determine which actions they should take and in what order."* The DuckDuckGo + llm-math two-tool demonstration is the chapter's argument that even small tool inventories can dramatically extend what an LLM can answer (real-time prices, exact arithmetic).
