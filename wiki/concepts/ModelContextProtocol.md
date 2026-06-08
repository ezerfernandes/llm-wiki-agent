---
title: "Model Context Protocol (MCP)"
type: concept
tags: [mcp, model-context-protocol, protocol, anthropic, tools, function-calling, agents, interoperability, open-standard]
sources: [dspy-mcp, dspy-mcp-tutorial, dspy-tools, dspy-learn-index, agentic-design-patterns-ch06-planning, agentic-design-patterns-ch10-mcp, agentic-design-patterns-ch15-a2a]
last_updated: 2026-06-07
---

# Model Context Protocol (MCP)

**The Model Context Protocol (MCP) is an [[anthropic|Anthropic]]-originated, framework-agnostic open standard for connecting [[LanguageModel|language models]] to external tools, data sources, and contextual resources via standalone servers.** A program that supports MCP becomes a *client* to any conforming MCP *server* — the server exposes a typed catalog of tools (functions the LM can invoke), resources (read-only data the LM can fetch), and prompts (parameterized prompt templates) over a small JSON-RPC-style wire protocol, and the client routes the LM's requests through that catalog. MCP's load-bearing design choice is **decoupling tool definition from tool consumption**: the same server can serve every MCP-aware framework — [[DSPy]], [[ClaudeCode|Claude Code]], a hand-written agent — without per-framework rewrapping, and conversely a single framework gains access to the entire MCP server ecosystem through one integration. This concept page records the protocol itself, framework-agnostically; [[DSPyMCP]] is the DSPy-specific binding.

## Why a protocol

Before MCP, every tool-using LM stack reinvented the same plumbing:

- **Per-framework tool wrappers.** A weather API would be wrapped as a [[LangChain]] `Tool`, a [[DSPyTools|`dspy.Tool`]], an [[openai|OpenAI Assistants]] function-spec, and an Anthropic `tool_use` schema — four near-identical adapters for the same underlying capability.
- **Per-agent tool registries.** Every agent harness shipped its own discovery API; sharing tools across teams meant copying code, not pointing at a server.
- **No common authorization or transport story.** Authentication, rate limiting, error formats, streaming protocols — every integration negotiated them ad-hoc.

MCP's answer is to **standardize the wire protocol** so the tool implementation lives in one place (the server) and every client speaks the same language to it. The protocol is **published openly** — *"an open protocol that standardizes how applications provide context to language models"* ([[dspy-mcp]]) — and the reference SDKs (Python, TypeScript, others) are public.

## What an MCP server exposes

An MCP server is a process that exposes three categories of items to clients:

| Category | What it is | Client-side use |
|---|---|---|
| **Tools** | Named callable endpoints with typed parameter schemas — the LM-invocable units | Wrapped as the client framework's tool primitive ([[DSPyTools|`dspy.Tool`]], `LangChain.Tool`, etc.) and used by tool-calling agents |
| **Resources** | Read-only data items (files, database rows, API responses) identified by URI | Fetched on demand to assemble context |
| **Prompts** | Parameterized prompt templates with named arguments | Substituted at runtime to produce LM-ready prompts |

The page-8 DSPy treatment focuses on **tools** because that's the entry-point most agent frameworks need. Resources and prompts are part of the protocol surface but are not covered on [[dspy-mcp|the DSPy MCP page]].

## The client–server lifecycle

Every MCP integration follows the same four-step lifecycle, regardless of client framework:

1. **Open a transport.** The client connects to the server over one of the supported transports:
   - **stdio** — the client spawns the server as a subprocess and communicates over its stdin/stdout (used for local MCP servers, no network exposure).
   - **streamable HTTP** — the client opens an HTTP connection to a remote MCP endpoint, with bidirectional streaming for long-running tool calls.
   - (The protocol supports further transports; the two above are the ones the DSPy page documents.)
2. **Initialize a session.** `ClientSession(read, write)` wraps the transport's read/write streams; `await session.initialize()` performs the handshake (protocol version negotiation, capability exchange).
3. **List the catalog.** `await session.list_tools()` (and the analogous `list_resources()` / `list_prompts()`) returns the server's typed catalog. Each entry carries name + description + parameter schema.
4. **Invoke.** When the LM produces a tool call, the client routes it back through the session as a JSON-RPC `tools/call` request; the server runs the implementation and returns the result; the client surfaces it as a normal tool-call result inside the framework.

The **session is stateful** — keeping it open avoids per-call connection overhead and lets the server retain context (caches, prepared statements, authenticated connections to downstream services).

## Transports

### stdio (local processes)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="python",
    args=["path/to/your/mcp_server.py"],
    env=None,
)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        response = await session.list_tools()
```

Use cases: tools that need filesystem access, locally-installed CLIs, no-network development environments, security-sensitive deployments where remote network access is unacceptable.

### Streamable HTTP (remote servers)

```python
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async with streamablehttp_client("http://localhost:8000/mcp") as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        response = await session.list_tools()
```

Use cases: tools that wrap remote APIs (weather, search, third-party SaaS), shared organizational tool registries served from a central host, multi-client deployments where one server backs many agents.

**API symmetry.** Once the session is open, the client code is identical across transports — the same `session.list_tools()` / `session.call_tool(...)` calls work regardless of whether the underlying transport is stdio or HTTP. This is deliberate; it lets a client framework support both with one code path.

## Asynchrony

Every MCP operation is **asynchronous**. The reference SDKs are built on Python's `asyncio` and TypeScript's `async`/`await`; clients must use `await session.initialize()`, `await session.list_tools()`, `await session.call_tool(...)`, and so on. This shapes how MCP-consuming frameworks expose tools to users — DSPy, for example, requires `react_agent.acall(...)` rather than the sync `react_agent(...)` when MCP-routed tools are in the toolset (see [[dspy-mcp]]).

## The framework-agnosticism payoff

MCP's distinguishing property is that **the same server serves every conforming client**. A "fetch weather" MCP server can be consumed by:

- A [[DSPy]] program via `dspy.Tool.from_mcp_tool(session, tool)` ([[DSPyMCP]] / [[dspy-mcp]]).
- [[ClaudeCode|Claude Code]] — [[anthropic|Anthropic]]'s coding agent — via its built-in MCP client.
- A custom Python agent built on the `mcp` SDK directly.
- A TypeScript / Node.js agent on the JavaScript SDK.

This decoupling has three concrete consequences:

1. **Tool authors write once.** A team maintaining a corporate-data MCP server doesn't need to know which agent frameworks will consume it; one implementation serves all clients.
2. **Agent authors get a tool ecosystem.** Connecting to an MCP server is a one-time integration (`mcp.client.stdio` / `mcp.client.streamable_http`); after that, every existing MCP server is reachable.
3. **Tooling can be operated as a service.** Tools that need privileged credentials (databases, internal APIs) can live behind an authenticated MCP HTTP endpoint; agents call them without holding the credentials themselves.

## MCP and the DSPy four-concerns decomposition

[[DSPyProgrammingModel|DSPy's Programming Model]] factors a conventional prompt into four orthogonal artifacts — Signature / Module / Adapter / Optimizer. MCP composes through **two** of them:

| DSPy artifact | MCP role |
|---|---|
| **[[DSPySignatures\|Signature]]** | Unchanged. MCP-converted tools fit the same `tools: list[dspy.Tool]` input field already documented. |
| **[[DSPyModules\|Module]]** | Unchanged. [[react\|`dspy.ReAct`]] consumes MCP-converted tools the same way it consumes locally-defined ones. |
| **[[DSPyAdapters\|Adapter]]** | Unchanged. The Adapter sees a typed `dspy.Tool` and is unaware of its origin (local function vs MCP server). |
| **[[DSPyOptimizers\|Optimizer]]** | Unchanged. Optimizers tune prompts and demos regardless of tool source. |

The MCP page does **not** modify any of these abstractions — it adds a **new construction path** for the [[DSPyTools|`dspy.Tool`]] primitive. This is the wiki's first concrete demonstration that the DSPy abstractions are **portable across tool origin**.

## Why this matters

- **First external tool-source protocol the wiki records.** Prior DSPy ingests ([[dspy-tools]] above all) treated tools as locally-defined Python callables. MCP is the **first** documented case of tools coming from a registry the agent didn't author. The conceptual shift — tool definition is decoupled from tool consumption — is more important than any specific protocol detail.

- **Open standard, multi-stack reach.** Unlike a proprietary tool-spec format (e.g. [[openai|OpenAI]]'s Assistants tool schema or Anthropic's `tool_use` JSON), MCP is **published openly** and has multiple independent client implementations. The wiki's [[2604.25850-agentic-harness-engineering|Agentic Harness Engineering]] critique argues tools and middleware are load-bearing; MCP is the standardized middleware layer that argument points at.

- **Async-first by design.** The protocol is asynchronous end-to-end. Frameworks that consume MCP inherit that constraint — see [[dspy-mcp]]'s requirement that [[react|`dspy.ReAct`]] be invoked via `.acall(...)`. The [[DSPyTools|`tool.acall(...)`]] surface introduced on [[dspy-tools]] (page 7) finds its primary motivating use case here.

- **Resolves the [[ModelContextProtocol]] forward reference.** Every prior DSPy ingest — [[DSPy]] / [[DSPyTools]] / [[dspy-learn-index]] / [[dspy-tools]] — carried `[[ModelContextProtocol]]` as a forward reference. This concept page is the canonical anchor.

- **Distinct from [[DSPyMCP]].** The DSPy-specific binding is its own concept (the `dspy.Tool.from_mcp_tool(...)` class-method plus the recommended `async with` usage pattern). This page records the protocol *itself*, framework-agnostically; [[DSPyMCP]] records DSPy's integration with it. The split mirrors the [[LiteLLM]] / [[DSPyLM]] precedent — protocol/library at the upstream end, framework binding at the downstream end.

## Agentic Design Patterns (Gulli) perspective ([[agentic-design-patterns-ch10-mcp]])

[[AntonioGulli|Gulli's]] [[AgenticDesignPatterns|*Agentic Design Patterns*]] devotes its **Chapter 10** to MCP, framing it as pattern #10 of 21 and the *standardized* answer to the [[ToolUse|Tool Use]] (Ch 5) and [[FunctionCalling|function-calling]] problem. The DSPy-derived material above covers the protocol mechanics; the ADP chapter adds the following framings:

### The "universal adapter" framing

Gulli's headline metaphor: MCP is "a universal adapter that allows any LLM to plug into any external system, database, or tool without a custom integration for each one." Restated as the canonical analogy against function calling: function calling is *"a specific set of custom-built tools, like a particular wrench and screwdriver"* (efficient for a fixed workshop), while MCP is *"a universal, standardized power outlet system"* — it doesn't provide the tools, but lets any compliant tool from any manufacturer plug in, enabling a dynamic, ever-expanding workshop.

### MCP vs. tool function calling — the five-axis table

The chapter's most-cited artifact is a side-by-side contrast (this complements, with the same conclusion as, the wiki's [[FunctionCalling]] coverage):

| Feature | Tool Function Calling | Model Context Protocol |
|---|---|---|
| **Standardization** | Proprietary, vendor-specific; format/implementation differ across LLM providers | Open, standardized protocol; interoperability across LLMs and tools |
| **Scope** | A direct mechanism for an LLM to request execution of one predefined function | A broader framework for how LLMs and external tools discover and communicate |
| **Architecture** | One-to-one between the LLM and the app's tool-handling logic | Client-server; LLM-powered clients connect to many MCP servers |
| **Discovery** | The LLM is explicitly told which tools exist for a given conversation | **Dynamic discovery** — a client can query a server to see its capabilities |
| **Reusability** | Integrations tightly coupled to the specific app + LLM | Standalone, reusable MCP servers any compliant app can access |

Bottom line: *"For simple applications, specific tools are enough; for complex, interconnected AI systems that need to adapt, a universal standard like MCP is essential."*

### The four-role component model

Gulli decomposes the client-server architecture into four roles (the wiki's DSPy material above describes the *lifecycle*; this is the *component view*):

1. **Large Language Model (LLM)** — the core intelligence that plans and decides when to access external information or act.
2. **MCP Client** — an application/wrapper around the LLM; translates the LLM's intent into a standardized request, and discovers/connects/communicates with servers.
3. **MCP Server** — the gateway to the external world; exposes tools/resources/prompts, each server typically scoped to one domain (a DB, an email service, a public API).
4. **Optional Third-Party (3P) Service** — the actual external tool/app/data source the server fronts (proprietary DB, SaaS platform, public weather API).

The five-step interaction flow: **Discovery** (client queries server → manifest of tools like `send_email`, resources like `customer_database`, prompts) → **Request Formulation** → **Client Communication** → **Server Execution** (authenticate, validate, run via underlying software) → **Response and Context Update**.

### The three primitives, sharply defined

Gulli draws the cleanest line in the wiki between the three MCP primitives by their *semantics*, not just their API category:

- **Resource** — *static data* (a PDF file, a database record). Read-only.
- **Tool** — an *executable function that performs an action* (sending an email, querying an API). Has side effects.
- **Prompt** — a *template that guides the LLM* in how to interact with a resource or tool, ensuring structured, effective interaction.

### The API-design caveat (a contribution unique to this source)

The chapter's most distinctive argument is a warning the DSPy material doesn't make: **MCP is a contract for an "agentic interface," but its effectiveness depends on the design of the APIs it exposes.** Two failure modes:

1. **Wrapping bad APIs.** Naively MCP-wrapping a legacy API (e.g., a ticketing API that returns tickets one-by-one) makes an agent slow and inaccurate at scale; the underlying API should add *deterministic* features (filtering, sorting). *"Agents do not magically replace deterministic workflows; they often require stronger deterministic support to succeed."*
2. **Agent-unfriendly data formats.** MCP does not enforce that data is agent-parseable. An MCP server returning PDFs is "mostly useless" if the agent can't parse PDF; better to return Markdown. Developers must consider not just the connection but the *nature of the data exchanged*.

This is a notable counterpoint to MCP-evangelism: the protocol standardizes the *plumbing*, not the *quality* of what flows through it.

### Additional considerations

The chapter enumerates evaluation dimensions: **Security** (auth/authz are mandatory for any tool-exposing protocol), **Implementation complexity** (SDKs from [[anthropic|Anthropic]] or [[FastMCP]] abstract the boilerplate), **Error handling** (the protocol must surface failures — tool errors, unavailable servers, invalid requests — so the LLM can retry/adapt), **Local vs. Remote servers** (local for speed/sensitive data; remote for shared scalable org access), **On-demand vs. Batch** processing, and the **Transport mechanism** (JSON-RPC over STDIO locally; Streamable HTTP + SSE remotely — matching the transports the DSPy material documents).

### MCP vs. A2A (boundary note)

Gulli treats MCP strictly as the **agent ↔ tool/data** (vertical) protocol. The book's *separate* [[InterAgentCommunication|Inter-Agent Communication]] pattern (Ch 15) covers **agent ↔ agent** (horizontal) coordination via [[A2AProtocol|Google's A2A protocol]]. MCP and A2A are complementary layers — MCP standardizes how an agent reaches its tools; A2A standardizes how agents coordinate with each other. Ch 15 confirms this symmetric framing from the A2A side: *"While MCP focuses on structuring context for agents and their interaction with external data and tools, A2A facilitates coordination and communication among agents."* Notably both protocols share a JSON-RPC lineage ([[JSONRPC|A2A uses JSON-RPC 2.0]]; MCP uses JSON-RPC-style `tools/call`). Neither chapter conflates them.

### Hands-on: Google ADK + FastMCP

The chapter's runnable examples use [[GoogleADK|Google ADK]]:
- **Consuming** a local filesystem MCP server: an `LlmAgent` (`gemini-2.0-flash`) is given an `MCPToolset` whose `connection_params=StdioServerParameters(command='npx', args=['-y', '@modelcontextprotocol/server-filesystem', TARGET_FOLDER_PATH])`. `npx` runs Node.js-distributed community MCP servers; `uvx` is the Python-isolated-env analog. An optional `tool_filter=[...]` restricts which server tools are exposed.
- **Authoring** a server with [[FastMCP]]: `from fastmcp import FastMCP, Client`; `@mcp_server.tool` decorates a Python function (its docstring + type hints become the tool's schema via **automatic schema generation**); `mcp_server.run(transport="http", host="127.0.0.1", port=8000)` serves it over HTTP. An ADK client then connects via `HttpServerParameters(url="http://localhost:8000")`.

## Connections

- [[anthropic|Anthropic]] — the originating organization; MCP is one of Anthropic's open-standard contributions to the agent ecosystem.
- [[DSPyMCP]] — the DSPy-specific binding; lighter-weight concept page focused on `dspy.Tool.from_mcp_tool(...)` and the `async with` usage pattern.
- [[dspy-mcp]] — canonical source for the DSPy integration (DSPy *Learn* page 8 of 13).
- [[dspy-mcp-tutorial]] — **first whole-program MCP server in the wiki**: an airline-domain [[FastMCP]] server (~150 lines, seven `@mcp.tool()` functions over five [[Pydantic]] models) driven from a [[react|`dspy.ReAct`]] agent. Worked-example complement to [[dspy-mcp]]'s API-surface reference.
- [[FastMCP]] — the Python decorator-style helper for authoring MCP servers in the official SDK; first wiki-corpus appearance via [[dspy-mcp-tutorial]].
- [[DSPy]] — one of several MCP-aware client frameworks.
- [[DSPyTools]] — the typed-tool abstraction MCP-converted tools land in.
- [[react|ReAct]] — the canonical [[DSPyModules|Module]] consuming MCP tools in both DSPy code examples.
- [[DSPyPredict]] — the manual-handling alternative; MCP-converted tools work with the same `tools: list[dspy.Tool]` Signature pattern.
- [[DSPySignatures]] — typed I/O contract; unchanged by MCP.
- [[DSPyAdapters]] — wire-format layer; unaware of tool origin.
- [[DSPyProgrammingModel]] — the four-concerns design; MCP composes through it without modifying it.
- [[ClaudeCode|Claude Code]] — Anthropic's coding agent; another MCP client; demonstrates the protocol's cross-framework reach.
- [[LanguageModel]] — the consumer of the tools MCP exposes.
- [[ToolUse]] — the wiki's pre-existing tool-use concept; MCP is the protocol-level realization.
- [[FunctionCall]] — the C-language *function-call* concept; MCP tool calls are the prompt-level analog over a JSON-RPC transport.
- [[2604.25850-agentic-harness-engineering|Agentic Harness Engineering]] — argues tools / middleware / long-term memory are the load-bearing layer for agent capability; MCP is the standardized middleware story.
- [[2604.21590-agenticqwen|AgenticQwen]] — names tool use as a core agentic capability; MCP is one realization of the tool-source side of that capability.
- [[DeepResearch]] / [[agentic-design-patterns-ch06-planning|ADP Ch 6 (Planning)]] — the **OpenAI Deep Research API** lists MCP as its *extensibility* mechanism: custom MCP tools let the research agent connect to private knowledge bases / internal data, blending public web research with proprietary information.
- [[LiteLLM]] — the upstream provider-abstraction layer for LMs; the [[LiteLLM]] / [[DSPyLM]] split is the architectural precedent for the [[ModelContextProtocol]] / [[DSPyMCP]] split.
- [[DSPyLM]] — the LM-client analog; MCP plays the same role for tool sources that LiteLLM/[[DSPyLM]] play for LM providers — provider-abstraction one layer down from the framework's typed abstraction.
- [[openai|OpenAI]] — provider whose function-calling API serves as an alternative (proprietary) tool-spec format MCP supersedes for cross-stack portability.
- [[AgenticDesignPatterns]] — Gulli's book; MCP is its Chapter 10 / pattern #10 of 21.
- [[AgenticDesignPattern]] — the meta-concept; MCP is one of the catalogued patterns.
- [[agentic-design-patterns-ch10-mcp]] — ADP Ch 10 source; adds the universal-adapter framing, five-axis MCP-vs-function-calling table, four-role component model, the API-design caveat, and the Google-ADK/FastMCP hands-on receipts.
- [[GoogleADK|Google ADK]] — the framework Gulli uses to demonstrate consuming and exposing MCP servers (`MCPToolset`).
- [[gemini|Gemini]] — the model driving the ADK MCP examples.
- [[InterAgentCommunication]] — the complementary agent-to-agent (A2A) pattern (Ch 15); MCP is agent-to-tool, A2A is agent-to-agent.
- [[A2AProtocol]] — Google's concrete agent↔agent protocol; the horizontal counterpart to MCP's vertical agent↔tool reach.
- [[agentic-design-patterns-ch15-a2a]] — ADP Ch 15 source; confirms the MCP-vs-A2A boundary from the A2A side.
- [[FunctionCalling]] — the proprietary mechanism MCP is contrasted against in Ch 10's five-axis table.
