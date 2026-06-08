---
title: "FastMCP"
type: entity
tags: [tool, library, python, mcp, model-context-protocol, server, framework, open-source, anthropic-ecosystem]
sources: [dspy-mcp-tutorial, agentic-design-patterns-ch10-mcp]
last_updated: 2026-06-07
---

## What it is

**FastMCP** is the canonical Python helper for authoring **[[ModelContextProtocol|MCP]] servers** with a decorator-style API. Imported as `from mcp.server.fastmcp import FastMCP`, it lets a single Python file declare an MCP server in three lines (`mcp = FastMCP("Server Name")`) plus one `@mcp.tool()` decorator per tool function and a single `mcp.run()` call at the bottom. The helper introspects the decorated function's name, docstring, and type hints (including [[Pydantic]] `BaseModel` subclasses) to build the JSON Schema the MCP wire protocol exposes to clients — no manual `inputSchema` authoring required. FastMCP is part of the **[[anthropic|Anthropic]]-stewarded official Python MCP SDK** (`pip install mcp`) and is the recommended entry point for ad-hoc / first-party MCP servers, in contrast to the lower-level `mcp.server` core API.

The ergonomics target is the same as Flask / FastAPI route declaration — *"decorate the function, run the file"* — applied to MCP tool registration instead of HTTP endpoint registration. The naming nods to FastAPI's *"fast development"* framing.

## In the corpus

- [[dspy-mcp-tutorial]] (Use MCP Tools in DSPy / Airline Agent) — **first wiki-corpus appearance.** Declares a complete seven-tool airline-domain MCP server in ~150 lines: `mcp = FastMCP("Airline Agent")` at the top, `@mcp.tool()` on each of `fetch_flight_info` / `fetch_itinerary` / `pick_flight` / `book_itinerary` / `cancel_itinerary` / `get_user_info` / `file_ticket`, `mcp.run()` at the bottom. Tools accept and return [[Pydantic]] models (`Date`, `UserProfile`, `Flight`, `Itinerary`, `Ticket`); FastMCP serializes them as JSON Schema for the wire protocol.

## In Agentic Design Patterns (Gulli), Ch 10 ([[agentic-design-patterns-ch10-mcp]])

[[AntonioGulli|Gulli's]] [[AgenticDesignPatterns|*Agentic Design Patterns*]] Chapter 10 ([[ModelContextProtocol|MCP]]) uses FastMCP as its server-authoring example, describing it as *"a high-level Python framework designed to streamline the development of MCP servers"* that provides an abstraction layer over protocol complexity. The chapter emphasizes the same load-bearing feature the DSPy tutorial showed — **automatic schema generation** that "intelligently interprets Python function signatures, type hints, and documentation strings to construct necessary AI model interface specifications" — plus two architectural capabilities not exercised in the DSPy material: **server composition** and **proxying** (modular multi-component systems and integration of existing services).

Two provenance/API differences worth noting vs. the existing DSPy-derived description above:

- **Import path & API.** The ADP example uses `from fastmcp import FastMCP, Client` (top-level `fastmcp` package) and the `@mcp_server.tool` decorator, then serves over HTTP with `mcp_server.run(transport="http", host="127.0.0.1", port=8000)`. The DSPy tutorial used `from mcp.server.fastmcp import FastMCP` (the path inside the official `mcp` SDK) with STDIO. These are the standalone-`fastmcp`-package vs. official-SDK-vendored views of the same project.
- **Provenance framing.** ADP's References cite FastMCP at **`github.com/jlowin/fastmcp`** (jlowin's independently-stewarded project) and list *"Anthropic or FastMCP"* as **separate** SDK providers — whereas the table below frames FastMCP as part of the Anthropic-stewarded official SDK. Both are reconcilable (FastMCP's high-level API was upstreamed into the official `mcp` package while the standalone `jlowin/fastmcp` continues independently); the existing claim is preserved.

**ADK consumption (Ch 10).** A [[GoogleADK|Google ADK]] `LlmAgent` consumes a running FastMCP HTTP server via `MCPToolset(connection_params=HttpServerParameters(url="http://localhost:8000"))`, optionally restricting the surface with `tool_filter=['greet']`. This is the ADK-side analog of the DSPy `from_mcp_tool` consumption path.

## The decorator pattern

```python
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel

mcp = FastMCP("Airline Agent")


@mcp.tool()
def get_user_info(name: str):
    """Fetch the user profile from database with given name."""
    return user_database.get(name)


if __name__ == "__main__":
    mcp.run()
```

The decorator reads the function's `__name__` (→ tool name), its docstring (→ tool description), and its type-hinted parameters (→ `inputSchema`). The return type is inferred at call time and JSON-serialized for the wire response.

## Relationship to the broader MCP stack

| Layer | Component | Owner |
|---|---|---|
| Protocol | [[ModelContextProtocol|MCP]] specification | [[anthropic\|Anthropic]] (open standard) |
| Server SDK — low level | `mcp.server` (manual tool registration) | Official Python SDK |
| Server SDK — **high level** | **`mcp.server.fastmcp.FastMCP`** (decorator API) | **Official Python SDK** |
| Client SDK | `mcp.ClientSession`, `mcp.client.stdio.stdio_client`, `mcp.client.streamable_http.streamablehttp_client` | Official Python SDK |
| DSPy binding | [[DSPyMCP\|`dspy.Tool.from_mcp_tool(session, tool)`]] | DSPy |

FastMCP is **server-side only**; the corresponding DSPy-side consumption is [[DSPyMCP|`dspy.Tool.from_mcp_tool`]]. The two compose without either knowing about the other — FastMCP authors a tool catalog the wire protocol describes; `from_mcp_tool` consumes that catalog into typed [[DSPyTools|`dspy.Tool`]] instances.

## Connections

- [[ModelContextProtocol]] — the protocol FastMCP implements server-side.
- [[DSPyMCP]] — the DSPy client-side binding that consumes FastMCP-authored tools.
- [[anthropic|Anthropic]] — steward of the official Python MCP SDK.
- [[Pydantic]] — tool parameter type system; FastMCP auto-serializes Pydantic models as JSON Schema.
- [[Python]] — language.
- [[ToolUse]] — broader tool-use concept; FastMCP is a server-author surface for it.
- [[dspy-mcp-tutorial]] — canonical wiki source for the FastMCP receipt.
- [[dspy-mcp]] — DSPy *Learn* MCP page (client-side reference docs).
- [[agentic-design-patterns-ch10-mcp]] — ADP Ch 10; uses FastMCP (`@mcp_server.tool` + HTTP transport) for the server-authoring example, consumed by a Google ADK agent.
- [[GoogleADK|Google ADK]] — consumes a FastMCP HTTP server via `MCPToolset` + `HttpServerParameters` in ADP Ch 10.
- [[AgenticDesignPatterns]] — Gulli's book; Ch 10 demonstrates FastMCP.
