# DSPy — MCP (Model Context Protocol)

Source: https://dspy.ai/learn/programming/mcp/
Section: DSPy *Learn* documentation — page 8 of 13
Captured: 2026-05-17

---

## Overview

The Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to language models. DSPy provides support for MCP, allowing you to leverage MCP-compatible tools and services seamlessly within your DSPy programs.

MCP enables you to:

- **Use standardized tools** — Connect to a growing ecosystem of MCP servers that expose tools, resources, and prompts.
- **Share tools across stacks** — Reuse the same tool implementation across different AI frameworks.
- **Simplify integration** — Skip the boilerplate of writing custom integrations for each external service.

DSPy doesn't manage MCP server connections directly. Instead, you connect to an MCP server using the `mcp` library, then convert the server's tools into DSPy tools with `dspy.Tool.from_mcp_tool`.

---

## Installation

```bash
pip install -U "dspy[mcp]"
```

This installs DSPy together with the `mcp` Python SDK.

---

## Connecting to an MCP server

There are two common ways to connect to an MCP server: **streamable HTTP** (for remote servers) and **stdio** (for local processes).

### Streamable HTTP (remote servers)

Use `streamablehttp_client` from `mcp.client.streamable_http` for remote MCP servers reachable over HTTP.

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

### Stdio (local processes)

Use `stdio_client` and `StdioServerParameters` from `mcp.client.stdio` to spawn and communicate with a local MCP server process over its stdin/stdout.

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

---

## Converting MCP tools to DSPy tools

`dspy.Tool.from_mcp_tool(session, tool)` is the bridge between the MCP world and DSPy. It takes a live `ClientSession` and an MCP tool descriptor (as returned by `session.list_tools()`) and returns a `dspy.Tool` that:

- preserves the tool's name and description,
- preserves the parameter schema (including types and argument descriptions),
- routes execution back through the MCP session asynchronously.

You can use the converted `dspy.Tool` instances anywhere DSPy expects tools — inside `dspy.ReAct`, in a custom `dspy.Predict` signature with a `tools: list[dspy.Tool]` input field, or directly via `await dspy_tool.acall(...)`.

```python
mcp_tool = response.tools[0]
dspy_tool = dspy.Tool.from_mcp_tool(session, mcp_tool)
result = await dspy_tool.acall(param1="value", param2=123)
```

---

## Notes

- MCP tool calls are **asynchronous** — use `await` and `dspy.ReAct(...).acall(...)`.
- The MCP `ClientSession` must remain open for the duration of any tool calls — keep your agent invocation inside the `async with` block.
- Both transports (`streamablehttp_client`, `stdio_client`) use the same `ClientSession` API once the connection is established, so the conversion code is identical.

---

## See also

- [Model Context Protocol specification](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- DSPy MCP tutorial
- DSPy Tools documentation
