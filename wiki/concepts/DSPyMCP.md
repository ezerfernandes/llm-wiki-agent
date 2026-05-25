---
title: "DSPy MCP Integration"
type: concept
tags: [dspy, mcp, model-context-protocol, tools, function-calling, agents, async, framework]
sources: [dspy-mcp, dspy-mcp-tutorial, dspy-tools, dspy-learn-index]
last_updated: 2026-05-24
---

# DSPy MCP Integration

**The DSPy MCP integration is the framework-specific binding between [[ModelContextProtocol|MCP]] `ClientSession`s and [[DSPyTools|`dspy.Tool`]] instances.** It rests on a single class-method — `dspy.Tool.from_mcp_tool(session, tool)` — that converts an MCP-side tool descriptor into a `dspy.Tool` the rest of DSPy can consume without any further MCP-aware code. This concept page records the DSPy-specific binding; [[ModelContextProtocol]] is the protocol-level concept page. The two split mirrors the [[LiteLLM]] / [[DSPyLM]] precedent — the upstream-protocol page records what the protocol *is*; this page records how DSPy *consumes* it.

## The integration in one line

```python
dspy_tools = [dspy.Tool.from_mcp_tool(session, tool) for tool in response.tools]
```

That's the entire DSPy-side surface. Every other line in the [[dspy-mcp|page-8 examples]] is either standard `mcp` SDK lifecycle (`async with stdio_client(...)`, `await session.initialize()`, `await session.list_tools()`) or standard [[DSPyTools|DSPy Tools]] code ([[react|`dspy.ReAct`]] consumption, `dspy.Signature` declarations).

## Installation

```bash
pip install -U "dspy[mcp]"
```

The `mcp` extra installs DSPy together with the [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk). It is **opt-in** — base DSPy does not pull in the MCP SDK as a hard dependency, consistent with DSPy's pattern of feature-gated optional installs.

## The framework boundary

[[dspy-mcp|The MCP page]] is explicit about the division of responsibility:

> *"DSPy doesn't manage MCP server connections directly. Instead, you connect to an MCP server using the `mcp` library, then convert the server's tools into DSPy tools with `dspy.Tool.from_mcp_tool`."*

| Layer | Owner | Surface |
|---|---|---|
| Transport (stdio / streamable HTTP) | `mcp` SDK | `stdio_client(...)`, `streamablehttp_client(...)` |
| Session lifecycle | `mcp` SDK | `ClientSession(read, write)`, `session.initialize()`, `session.list_tools()`, `session.call_tool(...)` |
| Tool conversion | **DSPy** | **`dspy.Tool.from_mcp_tool(session, tool)`** |
| Tool consumption | DSPy | [[react\|`dspy.ReAct`]], [[DSPyPredict\|`dspy.Predict`]] with `tools: list[dspy.Tool]`, direct `dspy_tool.acall(...)` |

The boundary is sharp: the `mcp` SDK does **all** the protocol work; DSPy does **none** of it. DSPy's contribution is the **conversion layer** — taking an MCP tool descriptor (a JSON-shaped dict from the wire protocol) plus a live session, and producing a typed [[DSPyTools|`dspy.Tool`]] instance whose execution callback routes back through the session asynchronously.

## What `from_mcp_tool` preserves

The conversion preserves every property [[DSPyTools|`dspy.Tool`]] exposes:

| Property | Comes from | Why DSPy needs it |
|---|---|---|
| `name` | MCP tool's `name` field | LM picks the tool by name in the response |
| `desc` | MCP tool's `description` field | LM uses the description to decide *when* to call the tool |
| `args` | MCP tool's `inputSchema` (JSON Schema) | LM uses the schema to fill in arguments |
| `str(tool)` | Composed from above | Canonical text representation in the prompt |
| async execution callback | Bound to `session.call_tool(name, args)` | Routes the LM's call back through the MCP wire protocol |

The user-facing result is that a `dspy.Tool` built via `from_mcp_tool(...)` is **indistinguishable** from a `dspy.Tool` built from a local Python function. The same Signature input field types apply (`tools: list[dspy.Tool] = dspy.InputField()`); the same Adapter machinery formats them into prompts; the same [[react|`dspy.ReAct`]] consumption pattern works.

## The two canonical usage patterns

### Streamable HTTP (remote MCP server)

```python
import asyncio
import dspy
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main():
    async with streamablehttp_client("http://localhost:8000/mcp") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            response = await session.list_tools()

            dspy_tools = [
                dspy.Tool.from_mcp_tool(session, tool)
                for tool in response.tools
            ]

            class TaskSignature(dspy.Signature):
                task: str = dspy.InputField()
                result: str = dspy.OutputField()

            react_agent = dspy.ReAct(
                signature=TaskSignature,
                tools=dspy_tools,
                max_iters=5,
            )

            result = await react_agent.acall(task="Check the weather in Tokyo")
            print(result.result)


asyncio.run(main())
```

### stdio (local MCP server process)

```python
import asyncio
import dspy
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["path/to/your/mcp_server.py"],
        env=None,
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            response = await session.list_tools()

            dspy_tools = [
                dspy.Tool.from_mcp_tool(session, tool)
                for tool in response.tools
            ]

            class QuestionAnswer(dspy.Signature):
                """Answer questions using available tools."""

                question: str = dspy.InputField()
                answer: str = dspy.OutputField()

            react_agent = dspy.ReAct(
                signature=QuestionAnswer,
                tools=dspy_tools,
                max_iters=5,
            )

            result = await react_agent.acall(question="What is 25 + 17?")
            print(result.answer)


asyncio.run(main())
```

The two examples are **byte-identical** after the transport-specific connection line. This is intentional — [[ModelContextProtocol|MCP]]'s transport abstraction is uniform once a session exists.

## Three rules the integration imposes

### 1. Use `.acall(...)`, not the sync form

All MCP tool execution is asynchronous (see [[ModelContextProtocol]] for why). When MCP-routed tools are in a [[react|`dspy.ReAct`]] agent's toolset, the sync `react_agent(...)` form **will not work** — calls into the MCP session would block on awaitable returns. The framework provides `react_agent.acall(...)` for exactly this case.

If absolutely required, the [[DSPyTools|`dspy.context(allow_tool_async_sync_conversion=True)`]] opt-in from [[dspy-tools|page 7]] can run an MCP tool from sync code by transparently spinning up an event loop — but the recommended pattern is async all the way down.

### 2. Keep the agent invocation *inside* the session

The `async with` block bounding the `ClientSession` must remain open for the duration of any tool calls. Once the block exits, the session closes and further invocations fail. This means the [[react|`dspy.ReAct`]] call **must** sit at the bottom of the nested `async with` blocks, **not** outside them:

```python
# WRONG — session closes before the agent runs
async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        dspy_tools = [dspy.Tool.from_mcp_tool(session, t) for t in (await session.list_tools()).tools]

react_agent = dspy.ReAct(signature=..., tools=dspy_tools)
result = await react_agent.acall(...)   # ← session is already closed; tool calls will fail

# RIGHT — agent runs inside the session
async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        dspy_tools = [dspy.Tool.from_mcp_tool(session, t) for t in (await session.list_tools()).tools]
        react_agent = dspy.ReAct(signature=..., tools=dspy_tools)
        result = await react_agent.acall(...)
```

This is an inversion of control compared to a sync `react_agent(...)` that returns and lets the caller move on; the agent invocation becomes a *participant in the session's lifetime*, not an event after it.

### 3. The toolset is fixed for the lifetime of the session

`session.list_tools()` is called once per session in the recommended pattern. If the MCP server's catalog changes mid-session, the [[DSPyTools|`dspy.Tool`]] list will not reflect it until a new `list_tools()` call (and a fresh round of `from_mcp_tool(...)` conversions). For most agent use cases this is fine — tool catalogs are typically stable per deployment — but it's a constraint to know about.

## Direct `tool.acall(...)` (without `dspy.ReAct`)

The converted `dspy.Tool` instances work outside of [[react|`dspy.ReAct`]] too. They can be invoked directly:

```python
mcp_tool = response.tools[0]
dspy_tool = dspy.Tool.from_mcp_tool(session, mcp_tool)
result = await dspy_tool.acall(param1="value", param2=123)
```

This is the same `tool.acall(...)` API documented on [[dspy-tools|page 7]] — the MCP-converted tool composes through it identically. Use cases: unit-testing the MCP tool from DSPy code without standing up a full agent; building a manual-handling [[DSPyPredict|`dspy.Predict`]] loop where the user owns the tool dispatch.

## Composition with the four-concerns decomposition

The DSPy MCP integration touches **one** of [[DSPyProgrammingModel|the Programming Model's]] four artifacts — [[DSPyTools|Tools]] — and leaves the other three unchanged:

| Concern | MCP effect |
|---|---|
| **[[DSPySignatures\|Signature]]** | None. MCP-converted tools fit the `tools: list[dspy.Tool]` input field already documented on [[dspy-tools]]. |
| **[[DSPyModules\|Module]]** | None. [[react\|`dspy.ReAct`]] consumes MCP-converted tools the same way it consumes locally-defined ones. |
| **[[DSPyAdapters\|Adapter]]** | None. The Adapter sees a typed `dspy.Tool` and is unaware that it routes through an MCP session. |
| **[[DSPyOptimizers\|Optimizer]]** | None. Optimizers tune prompts and demos; tool origin is invisible to them. |
| **[[DSPyTools\|Tools]]** | **Extended.** `dspy.Tool` gains a second construction path: `from_mcp_tool(session, mcp_tool)` alongside the existing `dspy.Tool(local_python_function)` form. |

This is the first concrete demonstration in the [[dspy-learn-index|Learn corpus]] that DSPy's abstractions are **portable across tool origin** — the same Signature / Module / Adapter / Optimizer code works against local-function tools and MCP-server tools interchangeably.

## Why this matters

- **First external tool-source binding in the DSPy corpus.** Prior pages treated tools as locally-defined Python functions. MCP is the first protocol-level tool source the framework documents; the integration shows the existing [[DSPyTools|`dspy.Tool`]] abstraction was designed to accommodate this without redesign.

- **Resolves the [[ModelContextProtocol]] forward reference (jointly with the protocol page).** Every prior DSPy ingest — [[DSPy]] / [[DSPyTools]] / [[dspy-learn-index]] / [[dspy-tools]] — carried `[[ModelContextProtocol]]` as a forward reference. This page (the DSPy binding) and [[ModelContextProtocol]] (the protocol itself) together resolve it.

- **Confirms the [[DSPyTools|`dspy.Tool`]] design is open under tool origin.** The page-7 [[dspy-tools|Tools]] documentation introduced `dspy.Tool` as a wrapper around a Python function. Page 8's `dspy.Tool.from_mcp_tool(...)` shows the wrapper was **always** an abstract typed-tool primitive that happened to accept Python functions as one origin — the MCP integration didn't require a new abstraction.

- **Asynchrony becomes load-bearing.** The [[dspy-tools|page-7]] async-tool surface (`tool.acall(...)`, `dspy.context(allow_tool_async_sync_conversion=True)`) was previously a corner-case feature. MCP integration **requires** it — all MCP calls are async. The page-7 design is vindicated by the page-8 use case.

- **Lighter-weight than the protocol page.** This concept treats `dspy.Tool.from_mcp_tool(...)` as the first-class abstraction; [[ModelContextProtocol]] treats the protocol itself as first-class. Splitting them follows the [[LiteLLM]] / [[DSPyLM]] precedent — protocol/library page upstream, framework binding page downstream.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-custom-module]] — names **MCP tools** as one of four example integration surfaces (Langchain / Agno / MCP / database handlers) the *unconstrained `forward()`* contract supports; positions `dspy.Tool.from_mcp_tool(...)` as a drop-in inside a custom `class MyProgram(dspy.Module)`.
- [[dspy-async-tutorial]] — documents the async-tool surface (`tool.acall(...)`, `allow_tool_async_sync_conversion=True`) the MCP binding **requires** end-to-end; vindicates the async-tool design as load-bearing rather than corner-case.
- [[dspy-yahoo-finance-react-tutorial]] — sibling **third-construction-path** receipt (`Tool.from_langchain(...)`) that confirms `dspy.Tool` is the single integration point across plain-Python / MCP / LangChain tool origins; useful contrast for the MCP-specific binding.
- [[dspy-mcp-tutorial]] — **canonical end-to-end MCP receipt**: stands up a [[FastMCP]] server with a seven-tool airline domain, drives it from `dspy.ReAct(...).acall(...)` through `dspy.Tool.from_mcp_tool(session, tool)` inside nested `async with stdio_client(...)` / `ClientSession(...)` blocks; confirms the three rules (`.acall(...)` only, agent invocation inside the session, toolset fixed per session).

## Connections

- [[ModelContextProtocol]] — the protocol-level concept this binding consumes; framework-agnostic anchor.
- [[dspy-mcp]] — canonical source for the DSPy integration (DSPy *Learn* page 8 of 13).
- [[dspy-mcp-tutorial]] — **applied whole-program receipt** for the binding. Stands up a [[FastMCP]] server with seven airline-domain tools, drives it from `dspy.ReAct(...).acall(...)` through `dspy.Tool.from_mcp_tool(session, tool)`. Confirms the API-surface claims from [[dspy-mcp]] with a runnable end-to-end script. **MCP variant** of [[dspy-customer-service-agent]] — same airline domain, MCP packaging.
- [[FastMCP]] — the canonical Python MCP-server author surface paired with this DSPy-side client binding.
- [[DSPy]] — the framework whose MCP binding this page documents.
- [[DSPyTools]] — the typed-tool abstraction `from_mcp_tool` constructs into; `dspy.Tool` gains a second construction path here.
- [[react|ReAct]] — the canonical [[DSPyModules|Module]] consuming MCP-converted tools; the [[dspy-mcp]] page's two examples both use `dspy.ReAct(...).acall(...)`.
- [[DSPyPredict]] — the manual-handling alternative; MCP-converted tools fit the same `tools: list[dspy.Tool]` Signature pattern from [[dspy-tools]].
- [[DSPySignatures]] — typed I/O contract; class-based Signatures (`class TaskSignature`, `class QuestionAnswer`) are used in both examples.
- [[DSPyModules]] — the parent abstraction.
- [[DSPyAdapters]] — wire-format layer; unaware of MCP origin.
- [[DSPyLM]] — LM-client analog one layer up; LiteLLM/[[DSPyLM]] is to LM providers what MCP/[[DSPyMCP]] is to tool sources.
- [[DSPyProgrammingModel]] — four-concerns decomposition; MCP composes through it without modifying it.
- [[anthropic|Anthropic]] — originator of MCP; the upstream protocol owner.
- [[dspy-tools]] — sibling page-7 [[DSPyTools|Tools]] sub-system definition; the [[DSPyTools|`dspy.Tool`]] / `dspy.ToolCalls` abstractions the MCP integration extends.
- [[dspy-learn-index]] — parent Learn index page; MCP is listed as the seventh Programming-stage sub-topic.
- [[ClaudeCode|Claude Code]] — [[anthropic|Anthropic]]'s own MCP client; demonstrates protocol portability across frameworks.
- [[LiteLLM]] — architectural precedent for the protocol/binding split.
- [[ToolUse]] — pre-existing tool-use concept; MCP is the protocol-level realization, this page is its DSPy binding.
