---
title: "FastMCP"
type: entity
tags: [tool, library, python, mcp, model-context-protocol, server, framework, open-source, anthropic-ecosystem]
sources: [dspy-mcp-tutorial]
last_updated: 2026-05-24
---

## What it is

**FastMCP** is the canonical Python helper for authoring **[[ModelContextProtocol|MCP]] servers** with a decorator-style API. Imported as `from mcp.server.fastmcp import FastMCP`, it lets a single Python file declare an MCP server in three lines (`mcp = FastMCP("Server Name")`) plus one `@mcp.tool()` decorator per tool function and a single `mcp.run()` call at the bottom. The helper introspects the decorated function's name, docstring, and type hints (including [[Pydantic]] `BaseModel` subclasses) to build the JSON Schema the MCP wire protocol exposes to clients — no manual `inputSchema` authoring required. FastMCP is part of the **[[anthropic|Anthropic]]-stewarded official Python MCP SDK** (`pip install mcp`) and is the recommended entry point for ad-hoc / first-party MCP servers, in contrast to the lower-level `mcp.server` core API.

The ergonomics target is the same as Flask / FastAPI route declaration — *"decorate the function, run the file"* — applied to MCP tool registration instead of HTTP endpoint registration. The naming nods to FastAPI's *"fast development"* framing.

## In the corpus

- [[dspy-mcp-tutorial]] (Use MCP Tools in DSPy / Airline Agent) — **first wiki-corpus appearance.** Declares a complete seven-tool airline-domain MCP server in ~150 lines: `mcp = FastMCP("Airline Agent")` at the top, `@mcp.tool()` on each of `fetch_flight_info` / `fetch_itinerary` / `pick_flight` / `book_itinerary` / `cancel_itinerary` / `get_user_info` / `file_ticket`, `mcp.run()` at the bottom. Tools accept and return [[Pydantic]] models (`Date`, `UserProfile`, `Flight`, `Itinerary`, `Ticket`); FastMCP serializes them as JSON Schema for the wire protocol.

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
