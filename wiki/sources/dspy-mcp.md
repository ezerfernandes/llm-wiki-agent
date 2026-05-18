---
title: "DSPy Learn — MCP"
type: source
tags: [dspy, llm-programming, mcp, model-context-protocol, tools, function-calling, agents, async, anthropic]
date: 2026-05-17
source_file: raw/dspy-mcp.md
---

## Summary

**Page 8 of 13** of the [[DSPy]] *Learn* documentation. Defines DSPy's integration with the **[[ModelContextProtocol|Model Context Protocol (MCP)]]** — [[anthropic|Anthropic]]'s open protocol that standardizes how applications expose tools, resources, and context to language models. The page's framing claim is that **DSPy does not manage MCP server connections directly**; instead the user opens an MCP `ClientSession` via the `mcp` Python SDK and uses **`dspy.Tool.from_mcp_tool(session, tool)`** to convert each MCP-side tool descriptor into a [[DSPyTools|`dspy.Tool`]] instance. The converted tools then compose through every existing DSPy pathway — [[react|`dspy.ReAct`]] as the canonical entry point — without any further MCP-aware code. Two transports are documented: **streamable HTTP** (for remote MCP servers, via `streamablehttp_client`) and **stdio** (for spawned local processes, via `stdio_client` + `StdioServerParameters`). Both expose the same `ClientSession` API; the conversion code is identical across transports. All MCP-routed tool execution is **asynchronous** — `dspy.ReAct(...).acall(...)` is required, and the `async with` block bounding the `ClientSession` must remain open for the duration of the agent invocation. Installation is `pip install -U "dspy[mcp]"`. **Resolves the long-standing forward reference [[ModelContextProtocol]]** carried by [[DSPy]] / [[DSPyTools]] / [[dspy-learn-index]] / [[dspy-tools]] since the corpus opened.

## Key Claims

- **MCP is the open protocol; DSPy is one client.** *"The Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to language models."* The protocol is **framework-agnostic** — the same MCP server can serve [[DSPy]], a hand-written agent, [[ClaudeCode|Claude Code]], or any other MCP-aware client. DSPy's role is to **consume** MCP-exposed tools, not to define them.

- **Three motivations for using MCP through DSPy.** The page enumerates: (1) *"Use standardized tools"* — connect to the growing MCP server ecosystem; (2) *"Share tools across stacks"* — the same MCP tool implementation serves multiple AI frameworks without per-framework re-wrapping; (3) *"Simplify integration"* — skip the boilerplate of writing custom per-service integrations. The unifying claim: tool definition is **decoupled** from tool consumption.

- **DSPy does not manage MCP connections.** *"DSPy doesn't manage MCP server connections directly. Instead, you connect to an MCP server using the `mcp` library, then convert the server's tools into DSPy tools with `dspy.Tool.from_mcp_tool`."* The separation is deliberate — connection lifecycle (open / close / re-connect / authenticate) is the `mcp` SDK's responsibility; DSPy's responsibility starts once the session is open and tools have been listed.

- **`dspy.Tool.from_mcp_tool(session, tool)` is the bridge.** A single class-method converts an MCP tool descriptor into a [[DSPyTools|`dspy.Tool`]] instance. The conversion preserves: the tool's name; its docstring / description; the parameter schema (types + argument descriptions); and binds the asynchronous execution callback back through the `ClientSession`. After conversion, the resulting `dspy.Tool` is **indistinguishable** from a `dspy.Tool` built from a local Python function — it composes through every DSPy pathway ([[react|`dspy.ReAct`]], manual `dspy.Predict(ToolSignature)`, direct `tool.acall(...)`).

- **Two transports, identical client code.** The page documents (a) **streamable HTTP** via `streamablehttp_client("http://localhost:8000/mcp")` for remote servers, and (b) **stdio** via `stdio_client(server_params)` for local processes (`StdioServerParameters(command="python", args=[...], env=None)`). Both return a `(read, write)` stream pair that `ClientSession(read, write)` wraps; from there the code path — `await session.initialize()` → `response = await session.list_tools()` → list-comprehension over `dspy.Tool.from_mcp_tool(session, tool)` — is **byte-identical** between transports. This is a deliberate API symmetry the MCP SDK enforces.

- **MCP tool execution is asynchronous.** All examples use `async def main()`, `async with` context managers, and `await react_agent.acall(...)`. *"MCP tool calls are asynchronous"* — there is no sync path for MCP-routed tools. This composes with [[DSPyTools|`dspy.Tool`]]'s `tool.acall(...)` async API (documented on [[dspy-tools|page 7]]) and with the [[DSPyTools|`dspy.context(allow_tool_async_sync_conversion=True)`]] opt-in for sync-from-async invocation if absolutely required.

- **Session lifetime is load-bearing.** The `async with stdio_client(server_params) as (read, write):` / `async with ClientSession(read, write) as session:` block must remain open for the duration of any tool calls. Once the block exits, the session is closed and further tool invocations will fail. This shapes the **agent-invocation-inside-the-session** code pattern both examples use — the [[react|`dspy.ReAct`]] call sits at the bottom of the nested `async with` blocks, not outside them.

- **Installation: `pip install -U "dspy[mcp]"`.** The MCP extra installs DSPy together with the `mcp` Python SDK. The SDK is **not** a DSPy hard dependency — the extra is opt-in, consistent with DSPy's pattern of feature-gated optional installs.

- **MCP servers can carry arbitrary tools.** The `QuestionAnswer` stdio example shows a math-tool MCP server (the agent answers *"What is 25 + 17?"* via converted tools); the `TaskSignature` HTTP example shows a weather-tool MCP server. The protocol is **content-agnostic** — any Python callable an MCP server author chooses to expose becomes a [[DSPyTools|`dspy.Tool`]] after conversion.

## Key Quotes

> "The Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to language models." — opening definition of MCP.

> "DSPy doesn't manage MCP server connections directly. Instead, you connect to an MCP server using the `mcp` library, then convert the server's tools into DSPy tools with `dspy.Tool.from_mcp_tool`." — the separation-of-concerns disclosure.

> "Use standardized tools / Share tools across stacks / Simplify integration." — the three motivations the page commits MCP to delivering.

> "MCP tool calls are asynchronous." — the load-bearing constraint that propagates through every code example on the page.

## Code Examples

The streamable-HTTP happy path (remote MCP server):

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

The stdio happy path (local MCP server process):

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

Direct conversion + invocation (without `dspy.ReAct`):

```python
mcp_tool = response.tools[0]
dspy_tool = dspy.Tool.from_mcp_tool(session, mcp_tool)
result = await dspy_tool.acall(param1="value", param2=123)
```

## Connections

- [[DSPy]] — the framework whose MCP integration this page defines. Page 8 of 13 of *Learn*.
- [[DSPyTools]] — the typed `dspy.Tool` wrapper this page extends with the `from_mcp_tool` class-method; MCP is the **first external tool-source protocol** documented in the corpus.
- [[ModelContextProtocol]] — **concept page minted by this ingest.** The canonical wiki anchor for the [[anthropic|Anthropic]]-introduced open protocol; **resolves the long-standing forward reference** carried by [[DSPy]] / [[DSPyTools]] / [[dspy-learn-index]] / [[dspy-tools]] since the corpus opened on 2026-05-17.
- [[DSPyMCP]] — **concept page minted by this ingest.** The DSPy-specific binding between MCP `ClientSession`s and [[DSPyTools|`dspy.Tool`]] instances; lighter-weight than the protocol page, treats `dspy.Tool.from_mcp_tool` as a first-class abstraction.
- [[anthropic|Anthropic]] — originator of the MCP protocol (the wiki's pre-existing Anthropic entity page is updated in-place with the MCP attribution).
- [[react|ReAct]] — the canonical [[DSPyModules|Module]] both examples use; `dspy.ReAct(...).acall(...)` is the recommended consumption pattern for MCP-routed tools because MCP execution is asynchronous.
- [[DSPyPredict]] — the manual-handling alternative; MCP-converted tools can be used in the same `tools: list[dspy.Tool]` Signature input documented on [[dspy-tools]].
- [[DSPySignatures]] — both examples declare class-based Signatures (`class TaskSignature(dspy.Signature)`, `class QuestionAnswer(dspy.Signature)`); the MCP integration composes through the standard Signature surface.
- [[DSPyModules]] — `dspy.ReAct` (one of the seven built-in Modules) is the consumption point for MCP tools.
- [[DSPyAdapters]] — the wire-format layer; native function-calling vs text-parsing applies identically to MCP-routed tools (the Adapter is unaware of the tool's *origin*; it sees only the typed `dspy.Tool` interface).
- [[DSPyLM]] — the underlying LM client; LM-side function-calling is unaffected by tool origin.
- [[DSPyProgrammingModel]] — the four-concerns design philosophy; MCP integration is a **Signature-side** (and execution-side) extension that composes through the existing artifacts without modifying them.
- [[dspy-tools]] — the prior-page [[DSPyTools|Tools]] sub-system definition; MCP is the **first external tool-source** that demonstrates the Tools abstraction is portable across origin.
- [[dspy-learn-index]] — parent Learn index page; lists MCP as the seventh Programming-stage sub-topic.
- [[ClaudeCode|Claude Code]] — [[anthropic|Anthropic]]'s own MCP client; demonstrates the protocol's cross-framework reach (Claude Code consumes MCP servers; DSPy consumes MCP servers; the same server serves both).
- [[ToolUse]] — the wiki's pre-existing tool-use concept; MCP is a tool-discovery and tool-execution protocol layered on top.
- [[FunctionCall]] — the wiki's pre-existing C-language *function-call* concept (runtime semantics); MCP tool calls are the **prompt-level analog** — same name + args shape, different execution substrate (LM prompt + MCP RPC, not stack-frame + jump).
- [[2604.25850-agentic-harness-engineering|Agentic Harness Engineering]] — the contemporary critique of *"DSPy-style instruction tuning"* argues tools / middleware / long-term memory are the load-bearing components. MCP is the standardized **tool-discovery layer** the critique points at — the layer that lets one tool implementation serve many agents.

## Contradictions

None. The MCP page **extends** every prior DSPy ingest:

- [[dspy-tools]] introduced `dspy.Tool` as a wrapper around a Python function. This page **adds** `dspy.Tool.from_mcp_tool(session, tool)` as a *second construction path* — `dspy.Tool` is no longer purely a *local-function wrapper*, it's a typed adapter to any tool source the framework can talk to. The wiki's prior framing of `dspy.Tool` as *"a typed wrapper around a Python function"* is generalized to *"a typed wrapper around a tool — Python function, MCP-server tool, or any future origin."*

- [[dspy-modules]] showed [[react|`dspy.ReAct`]] consuming `tools=[fn1, fn2, ...]` (plain Python callables auto-wrapped to `dspy.Tool`). This page shows [[react|`dspy.ReAct`]] consuming `tools=[dspy_tool, ...]` where each `dspy_tool` was already converted from MCP. The `tools=` kwarg is **polymorphic over the construction path**.

- [[dspy-language-models|`dspy.LM`]] / [[LiteLLM]]'s LM-agnosticism story acquires a sibling: the same DSPy program can swap **LMs** (via [[DSPyLM]]) *and* swap **tool sources** (via MCP) without modifying the [[DSPySignatures|Signature]] or the [[DSPyModules|Module]] code. The portability story extends from LMs to tools.

- The asynchronous-tools work introduced on [[dspy-tools]] (page 7) — `tool.acall(...)`, `dspy.context(allow_tool_async_sync_conversion=True)` — finds its **primary motivating use case** here: MCP tool execution is **strictly async**. The Tools-page async surface is not a corner-case feature; it's load-bearing infrastructure for the MCP integration.

Three productive sharpenings of the wiki's prior framing:

1. **Tool origin is decoupled from tool consumption.** [[dspy-tools]] documented the [[DSPyTools|`dspy.Tool`]] / `dspy.ToolCalls` surface but treated tools as locally-defined Python functions. MCP is the first concrete demonstration that the same abstraction supports **external tool registries** — a protocol-defined tool ecosystem the agent didn't author.

2. **MCP is the protocol; DSPy is one client.** The wiki should record MCP as a **framework-agnostic concept** (its own concept page [[ModelContextProtocol]]) distinct from DSPy's specific binding ([[DSPyMCP]]). This mirrors the [[LiteLLM]] precedent where the upstream provider-abstraction layer got its own entity page distinct from [[DSPyLM]]'s DSPy-specific client.

3. **Session lifetime is a new framework-user contract.** Prior DSPy code paths assumed eternally-available tools (functions are always callable). MCP introduces a **session-scoped tool registry** that closes when the `async with` block exits. The agent invocation must live **inside** the session — an inversion of control compared to a synchronous `react_agent(...)` call that returns and lets the caller move on.
