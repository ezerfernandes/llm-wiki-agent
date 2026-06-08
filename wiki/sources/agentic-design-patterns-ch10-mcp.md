---
title: "Chapter 10 — Model Context Protocol / MCP (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, mcp, model-context-protocol, tool-use, interoperability, open-standard, adk, fastmcp]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 10 of [[AntonioGulli|Gulli's]] [[AgenticDesignPatterns|*Agentic Design Patterns*]] presents the **Model Context Protocol (MCP)** as a "universal adapter" — an open, [[anthropic|Anthropic]]-originated standard that lets any LLM ([[gemini|Gemini]], [[openai|OpenAI]]'s GPT, Mixtral, [[anthropic|Claude]]) plug into external systems via a **client-server architecture** without per-system custom integration. It distinguishes MCP from raw [[FunctionCalling|tool function calling]] (proprietary, one-to-one, statically declared vs. open, federated, dynamically discoverable), enumerates the three primitives (**Tools, Resources, Prompts**), the transport layers (JSON-RPC over STDIO for local; Streamable HTTP + SSE for remote), and a four-role component model (LLM → MCP Client → MCP Server → optional Third-Party service). It closes with hands-on [[GoogleADK|Google ADK]] code consuming a local filesystem MCP server via `MCPToolset`, and authoring an MCP server with [[FastMCP]]. (Agentic Design Patterns, PDF pp 167–182.)

## Key Claims
- MCP is an **open standard** that standardizes how LLMs communicate with external applications, data sources, and tools — "a universal connection mechanism" that reduces integration complexity.
- MCP operates on a **client-server architecture**: an MCP *server* exposes resources (data), prompts (interactive templates), and tools (actionable functions); an MCP *client* (an LLM host application or AI agent) consumes them.
- **MCP is a contract for an "agentic interface," not a substitute for good API design.** Naively wrapping legacy APIs (e.g., a ticketing API that returns tickets one-by-one) yields a poor agent experience; the underlying API should add deterministic features like filtering/sorting. "Agents do not magically replace deterministic workflows; they often require stronger deterministic support to succeed."
- An API must be **agent-friendly in its data format** — MCP does not enforce this. Wrapping a document store that returns PDFs is "mostly useless" if the agent cannot parse PDFs; better to return Markdown the agent can read.
- **MCP vs. tool function calling** differ on five axes: Standardization (open vs. proprietary/vendor-specific), Scope (broad framework vs. direct mechanism), Architecture (client-server, many servers vs. one-to-one), Discovery (dynamic query of a server's catalog vs. statically told which tools exist), and Reusability (standalone reusable servers vs. tightly-coupled integrations). Analogy: function calling = a fixed set of custom-built tools (a particular wrench); MCP = a universal power-outlet standard any compliant tool can plug into.
- The **three primitives have distinct roles**: a *Resource* is static data (a PDF, a DB record); a *Tool* is an executable function with side effects (send an email, query an API); a *Prompt* is a template guiding the LLM's interaction with a resource or tool.
- **Dynamic ("just-in-time") discovery** is a key advantage: an MCP client can query a server to learn its tools/resources at runtime, so agents adapt to new capabilities **without being redeployed**.
- **Transports**: for local interactions MCP uses **JSON-RPC over STDIO** (efficient inter-process communication); for remote connections it leverages web-friendly **Streamable HTTP and Server-Sent Events (SSE)** for persistent, efficient client-server communication.
- The **component flow** is a five-step loop: Discovery (client queries server for a manifest of tools/resources/prompts) → Request Formulation (LLM picks a tool, e.g. `send_email`, with params) → Client Communication (client sends standardized call) → Server Execution (server authenticates, validates, executes via the underlying software) → Response and Context Update (standardized response flows back, updating the LLM's context).
- Nine practical use cases: database integration (MCP Toolbox for Databases → [[GoogleBigQuery|BigQuery]]), generative media orchestration (MCP Tools for Genmedia → Imagen/Veo/Chirp 3 HD/Lyria), external API interaction, reasoning-based information extraction, custom tool development (via FastMCP), standardized LLM-to-application communication, complex workflow orchestration, IoT device control, and financial services automation.
- **Security is mandatory**: exposing tools/data via any protocol "requires robust security" — authentication and authorization to control which clients access which servers and actions.
- **Error handling** must be defined by the protocol so failures (tool execution failure, unavailable server, invalid request) are communicated back to the LLM, which can then try an alternative approach.
- Servers can be **local vs. remote** (local for speed/security with sensitive data; remote for shared, scalable org-wide access) and support **on-demand vs. batch** processing.
- **Google ADK** supports both consuming existing MCP servers (`MCPToolset` with `StdioServerParameters`/`StdioConnectionParams`/`HttpServerParameters`) and exposing ADK tools via an MCP server. `npx` runs Node.js-distributed community MCP servers (e.g. `@modelcontextprotocol/server-filesystem`); `uvx` runs Python tools in an isolated env.
- **FastMCP** is a high-level Python framework that streamlines MCP server development via decorators (`@mcp_server.tool`), with **automatic schema generation** from function signatures, type hints, and docstrings; it supports server composition and proxying.
- **Rule of thumb**: use MCP for complex, scalable, enterprise-grade agentic systems needing a diverse, evolving toolset, interoperability across LLMs/tools, and dynamic capability discovery without redeployment; for simpler apps with a fixed, limited set of predefined functions, direct tool function calling may suffice.

## Key Quotes
> "Imagine a universal adapter that allows any LLM to plug into any external system, database, or tool without a custom integration for each one. That's essentially what the Model Context Protocol (MCP) is." — MCP Pattern Overview

> "However, MCP is a contract for an 'agentic interface,' and its effectiveness depends heavily on the design of the underlying APIs it exposes. There is a risk that developers simply wrap pre-existing, legacy APIs without modification, which can be suboptimal for an agent." — the chapter's central caveat

> "This highlights that agents do not magically replace deterministic workflows; they often require stronger deterministic support to succeed." — on MCP + API design

> "Think of tool function calling as giving an AI a specific set of custom-built tools, like a particular wrench and screwdriver... MCP, on the other hand, is like creating a universal, standardized power outlet system. It doesn't provide the tools itself, but it allows any compliant tool from any manufacturer to plug in and work." — the MCP-vs-function-calling analogy

> "A resource is static data (e.g., a PDF file, a database record). A tool is an executable function that performs an action (e.g., sending an email, querying an API). A prompt is a template that guides the LLM in how to interact with a resource or tool." — the three primitives

## Connections
- [[ModelContextProtocol]] — the chapter's named pattern; this source AUGMENTS the existing concept page with Gulli's framing (universal-adapter framing, the four-role component model, the API-design caveat, the MCP-vs-function-calling table).
- [[AgenticDesignPatterns]] — the book this chapter belongs to (pattern #10 of 21).
- [[AgenticDesignPattern]] — the meta-concept; MCP is one of the 21 catalogued patterns.
- [[ToolUse]] — MCP standardizes external-tool access; it is the protocol-level realization of the Tool Use pattern (Ch 5).
- [[FunctionCalling]] — the chapter's primary contrast; MCP supersedes proprietary per-vendor function calling for cross-stack portability and dynamic discovery.
- [[anthropic|Anthropic]] — named as an SDK provider that abstracts MCP boilerplate (alongside FastMCP); the wiki records Anthropic as MCP's originator.
- [[FastMCP]] — the high-level Python MCP-server framework demonstrated in the hands-on section.
- [[GoogleADK|Google ADK]] — the framework used for the hands-on code (`MCPToolset`, consuming and exposing MCP servers).
- [[gemini|Gemini]] — the model used in the ADK examples (`gemini-2.0-flash`).
- [[GoogleBigQuery]] — database-integration use case via the MCP Toolbox for Databases.
- [[InterAgentCommunication]] / [[AgentCommunication]] — MCP is an agent-to-tool protocol; the book's separate pattern (Ch 15) covers agent-to-agent (A2A) communication — a distinct layer (see Contradictions/Notes).
- [[Routing]] / [[PromptChaining]] / [[Parallelization]] / [[Reflection]] / [[Planning]] / [[MultiAgentCollaboration]] / [[MemoryManagement]] — prior ADP patterns; MCP is the standardized tool/data-access layer those patterns build upon.

## Contradictions
- **MCP vs. A2A scope** — not a contradiction, but a boundary worth recording: this chapter treats MCP strictly as an **LLM/agent ↔ tool/data** protocol (vertical integration). The book's separate [[InterAgentCommunication|Inter-Agent Communication]] pattern (Ch 15) covers **agent ↔ agent** coordination (e.g., the A2A protocol — horizontal). MCP and A2A are complementary layers, not competitors; this chapter does not name A2A.
- **FastMCP provenance** — minor framing nuance vs. existing [[FastMCP]] page: the ADP book lists "Anthropic **or** FastMCP" as separate providers of MCP SDKs and references FastMCP at `github.com/jlowin/fastmcp` (an independently-stewarded project). The existing [[FastMCP]] page describes FastMCP as part of "the Anthropic-stewarded official Python MCP SDK." Both can be true (FastMCP's API was upstreamed into the official SDK), so I preserved the existing claim and noted Gulli's separate-provider framing. Not flagged as a hard contradiction.
