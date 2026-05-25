---
title: "DSPy Tutorial — Use MCP Tools in DSPy (Airline Agent)"
type: source
tags: [dspy, tutorial, mcp, model-context-protocol, fastmcp, react, agent, tools, customer-service, pydantic, async, stdio, anthropic, airline]
date: 2026-05-24
source_file: raw/dspy-mcp-tutorial.md
---

## Summary

The [[DSPy]] **"Use MCP tools in DSPy"** tutorial ([dspy.ai/tutorials/mcp](https://dspy.ai/tutorials/mcp/)) is the canonical end-to-end **applied receipt** for the [[DSPyMCP|DSPy ⇄ MCP binding]]: a complete worked example that stands up a custom **[[FastMCP]] server** exposing a seven-tool airline domain ([[Pydantic]] models for `Date` / `UserProfile` / `Flight` / `Itinerary` / `Ticket`) over a **stdio transport**, then drives it from a [[react|`dspy.ReAct`]] agent whose Signature is **two fields** (`user_request: str` → `process_result: str`) and whose tool list is built by **`dspy.Tool.from_mcp_tool(session, tool)` over `session.list_tools()`**. Where the [[dspy-mcp|DSPy Learn — MCP page]] (page 8 of 13) defined the **API surface** for the integration with two minimal happy-path snippets (one stdio, one streamable-HTTP), this tutorial supplies the **whole-system worked example** — the full server source, the full client/agent script, the launch command (`python mcp_server.py` in one process, `python dspy_mcp_agent.py` in another), and the framing claim that **MCP-routed tools compose identically to locally-defined tools** once they cross the `from_mcp_tool` boundary.

The tutorial is the **applied counterpart** to two prior wiki pages: it is the **MCP variant** of [[dspy-customer-service-agent|the Customer Service Agent tutorial]] (same airline domain, same five Pydantic classes, same seven tools, same two-field Signature — but tools now sit behind an MCP server instead of being passed as plain Python callables) and the **whole-program demonstration** of [[dspy-mcp|the Learn — MCP page]]'s API. **First wiki-corpus appearance of [[FastMCP]]** — the `mcp.server.fastmcp.FastMCP` decorator-style helper that lets a Python file declare an MCP server with `mcp = FastMCP("Airline Agent")` + `@mcp.tool()` per function. **First wiki-corpus demonstration of `@mcp.tool()` annotated functions composing transparently through DSPy** — the same Python function definitions that would work as direct `dspy.ReAct(..., tools=[fn])` arguments in [[dspy-customer-service-agent|the customer-service-agent tutorial]] become MCP-server tools with **one decorator** and reach the agent through **one conversion call**.

The tutorial's three load-bearing structural claims:

1. **MCP servers can be written in ~150 lines of Python** — [[FastMCP]] reduces the protocol-server side of the integration to *"decorate the tool function, run the file."* No JSON-RPC wiring, no schema authoring, no transport setup; the decorator introspects type hints (including [[Pydantic]] models) to build the wire schema automatically.
2. **The agent code is `from_mcp_tool` plus a normal [[DSPyTools|`dspy.Tool`]] consumption pattern** — once `dspy_tools = [dspy.Tool.from_mcp_tool(session, t) for t in tools.tools]`, every downstream line is indistinguishable from a non-MCP DSPy agent.
3. **The whole agent invocation lives inside the `async with` stdio session block** — confirming the [[DSPyMCP|session-lifetime contract]] [[dspy-mcp|the Learn page]] states: the `dspy.ReAct(...).acall(...)` call sits at the bottom of the nested `async with stdio_client(...) as ...:` / `async with ClientSession(...) as session:` blocks, not outside them.

## Key Claims

- **[[FastMCP]] is the canonical Python entrypoint to MCP server authoring.** *"from `mcp.server.fastmcp` import FastMCP"* — the server is declared as `mcp = FastMCP("Airline Agent")`, tools are registered with `@mcp.tool()` decorators on plain Python functions with type hints + docstrings, and the file runs with `mcp.run()`. The decorator does all schema work — no manual `inputSchema` JSON authoring, no manual `register_tool(...)` calls.

- **[[Pydantic]] models compose through the MCP wire protocol.** The seven tools' signatures accept and return `Date`, `UserProfile`, `Flight`, `Itinerary` Pydantic models; [[FastMCP]] serializes the model as JSON Schema on the way out (the LM sees a typed parameter schema), and the resulting `dspy.Tool.args` on the DSPy side preserves the schema. *"Somehow LLM is bad at specifying `datetime.datetime`"* — the tutorial's inline comment justifying the custom `Date(year, month, day, hour)` BaseModel over Python's built-in `datetime` — is a **load-bearing applied-LM finding** about model-friendly type design: LLMs reliably emit integer-field Pydantic models but unreliably emit ISO-8601 strings parseable as `datetime.datetime`.

- **The seven tools cover a complete CRUD-plus-escalation surface.** The set: `fetch_flight_info(date, origin, destination)` (lookup), `fetch_itinerary(confirmation_number)` (lookup), `pick_flight(flights: list[Flight])` (a *helper* tool the LM can call to delegate the duration/price ordering to deterministic code), `book_itinerary(flight, user_profile)` (create, returns `confirmation_number`), `cancel_itinerary(confirmation_number, user_profile)` (delete, raises on miss), `get_user_info(name)` (lookup), `file_ticket(user_request, user_profile)` (escalation — the *human-handoff* tool, returns a 6-char `ticket_id`). The shape matches [[CustomerServiceAgent|the customer-service-agent pattern]]'s **lookup / mutation / escalation** decomposition exactly — the MCP packaging changes the **deployment surface**, not the **information architecture**.

- **`pick_flight` shows a tool-as-deterministic-utility pattern.** *"Pick up the best flight that matches users' request. Sorted by `(duration, price)`."* The LM is **not** asked to compare floats and break ties; it calls `pick_flight(flights=[...])` and the deterministic Python sort returns the winner. This is a small but instructive design move — pushing **ordering / comparison / tie-breaking** out of the LM and into a tool — that scales the pattern from "tool = external API call" to "tool = any function we'd rather have deterministic code execute than have the LM reason through."

- **`pick_flight`'s body shows a defensive double-dispatch over `dict | BaseModel`.** *"`x.get('duration') if isinstance(x, dict) else x.duration`"* — the tutorial's tool body accommodates **both** shapes the MCP wire layer might deliver: a Pydantic model (when DSPy preserves the type) or a plain dict (when the round-trip through JSON loses the class binding). This is a **first-of-its-kind wiki-corpus DSPy receipt for serialization-boundary defensive coding** — every prior DSPy tutorial that passed [[Pydantic]] objects between layers (e.g. [[dspy-customer-service-agent]]) used direct function calls where the class binding survives; MCP introduces a serialization boundary that the tool author must accommodate.

- **The stdio transport is the recommended pattern for local tool servers.** Both fetch attempts above and [[dspy-mcp|the Learn page]] document streamable HTTP as the alternative; this tutorial uses stdio exclusively — `command="python", args=["script_tmp/mcp_server.py"]` — and the rationale is implicit: for a local tool server bundled with the agent, stdio avoids HTTP-port management and authorization layers. The hosted-notebook incompatibility ("This tutorial cannot be run in hosted IPython notebooks like Google Colab or Databricks notebooks") is a direct consequence — stdio child-process spawn is unsupported in those sandboxes.

- **The agent script's `async with` nesting matches the [[DSPyMCP|session-lifetime contract]] verbatim.** *"`async with stdio_client(server_params) as (read, write): / async with ClientSession(read, write) as session: / await session.initialize() / tools = await session.list_tools() / dspy_tools = [dspy.Tool.from_mcp_tool(session, tool) for tool in tools.tools] / react = dspy.ReAct(DSPyAirlineCustomerService, tools=dspy_tools) / result = await react.acall(user_request=user_request)`"*. The `dspy.ReAct(...)` constructor **and** the `.acall(...)` invocation **and** the `await` for the result all sit inside the innermost `async with` block — the agent is not just *invoked* inside the session, it is *constructed* inside the session.

- **The same LM config carries over from the rest of DSPy.** `dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))` — identical to [[dspy-customer-service-agent|the customer-service-agent tutorial]] and to most [[dspy-learn-index|Learn-corpus]] examples. MCP integration does not require an LM-config change; the LM client is unaware that tools are MCP-routed.

- **Sample request: `"please help me book a flight from SFO to JFK on 09/01/2025, my name is Adam"`** — the same canonical request shape as [[dspy-customer-service-agent|the customer-service-agent tutorial]], confirming the **applied-equivalence** of the two receipts. The expected trajectory: `get_user_info("Adam")` → `fetch_flight_info(...)` → `pick_flight(...)` → `book_itinerary(...)` → emit `process_result` with the confirmation number.

- **Two-process launch model.** The tutorial is explicit: *"`python path_to_your_working_directory/mcp_server.py`"* runs the server as a long-lived process; *"`python path_to_your_working_directory/dspy_mcp_agent.py`"* runs the agent script (which itself spawns the server as a stdio child via `StdioServerParameters(command="python", args=[...])`). The "long-lived server" framing in the prose is slightly misleading for the stdio case — the actual stdio transport in the agent code spawns its **own** server child process, so the manual `python mcp_server.py` is conceptually for demonstration / smoke-test only.

## Key Quotes

> *"MCP, standing for Model Context Protocol, is an open protocol that standardizes how applications provide context to LLMs."* — opening one-line definition; identical to [[dspy-mcp|the Learn page]]'s framing.

> *"In this guide, we will walk you through how to use MCP tools in DSPy. For demonstration purposes, we will build an airline service agent that can help users book flights and modify or cancel existing bookings."* — explicit reuse of the airline domain from [[dspy-customer-service-agent|the customer-service-agent tutorial]].

> *"This tutorial cannot be run in hosted IPython notebooks like Google Colab or Databricks notebooks. To run the code, you will need to follow the guide to write code on your local device. The code is tested on macOS and should work the same way in Linux environments."* — load-bearing platform constraint; stdio transport requires local subprocess spawn. **First explicit hosted-notebook-incompatibility callout in the DSPy tutorial corpus.**

> *"DSPy provides an API `dspy.Tool` as the standard tool interface. Let's convert all the MCP tools to `dspy.Tool`."* — the tutorial's framing of the one-line conversion as the *entire* integration surface.

> *"`ReAct` stands for 'reasoning and acting,' which asks the LLM to decide whether to call a tool or wrap up the process."* — restates the canonical [[react|ReAct]] mechanism from [[Yao2022|Yao et al. 2022]] verbatim from [[dspy-customer-service-agent|the customer-service-agent tutorial]].

> *"In the context of MCP support, DSPy provides a simple interface for interacting with MCP tools, giving you the flexibility to implement any functionality you need."* — closing claim positioning DSPy as a thin client over an open ecosystem.

> *"Somehow LLM is bad at specifying `datetime.datetime`"* — inline code comment on the `Date(BaseModel)` definition. A small but generalizable applied finding about LM-friendly type design.

## Code Receipts

### Receipt 1 — `FastMCP` server header

```python
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel

mcp = FastMCP("Airline Agent")
```

Three imports, one constructor — the entire server-side scaffolding before tool definitions.

### Receipt 2 — `@mcp.tool()` decorator pattern

```python
@mcp.tool()
def fetch_flight_info(date: Date, origin: str, destination: str):
    """Fetch flight information from origin to destination on the given date"""
    flights = []

    for flight_id, flight in flight_database.items():
        if (
            flight.date_time.year == date.year
            and flight.date_time.month == date.month
            and flight.date_time.day == date.day
            and flight.origin == origin
            and flight.destination == destination
        ):
            flights.append(flight)
    return flights
```

The decorator + docstring + type hints together supply everything the MCP wire protocol needs — the function is **otherwise unchanged** from what a plain `dspy.ReAct(..., tools=[fetch_flight_info])` call would consume.

### Receipt 3 — Tool conversion loop

```python
async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        tools = await session.list_tools()

        dspy_tools = []
        for tool in tools.tools:
            dspy_tools.append(dspy.Tool.from_mcp_tool(session, tool))
```

The four-line block (initialize → list → convert) is the entire MCP-aware footprint of the agent code.

### Receipt 4 — Agent construction + invocation

```python
react = dspy.ReAct(DSPyAirlineCustomerService, tools=dspy_tools)
result = await react.acall(user_request=user_request)
```

Two lines, both inside the `async with ClientSession(...)` block. The `dspy.ReAct(...)` constructor takes the converted MCP tools indistinguishably from how it would take local Python callables (cf. [[dspy-customer-service-agent]]).

### Receipt 5 — `StdioServerParameters` setup

```python
server_params = StdioServerParameters(
    command="python",
    args=["path_to_your_working_directory/mcp_server.py"],
    env=None,
)
```

The `command` / `args` / `env` triple mirrors `subprocess.Popen` semantics — the `mcp` SDK spawns the server file as a child process and pipes stdin/stdout for the JSON-RPC transport.

### Receipt 6 — `pick_flight` deterministic helper

```python
@mcp.tool()
def pick_flight(flights: list[Flight]):
    """Pick up the best flight that matches users' request."""
    sorted_flights = sorted(
        flights,
        key=lambda x: (
            x.get("duration") if isinstance(x, dict) else x.duration,
            x.get("price") if isinstance(x, dict) else x.price,
        ),
    )
    return sorted_flights[0]
```

The `dict | BaseModel` double-dispatch is the **serialization-boundary defensive coding** pattern — a wire round-trip may downgrade the Pydantic model to a plain dict, and the tool must handle both.

## Connections

- [[DSPy]] — the framework whose MCP integration this tutorial demonstrates end-to-end.
- [[DSPyMCP]] — the DSPy ⇄ MCP binding concept; this tutorial is the **canonical applied receipt** for the integration the binding documents. **Update needed:** the existing [[DSPyMCP]] concept page should list this tutorial alongside [[dspy-mcp]] as a second source (API-surface vs whole-program decomposition).
- [[ModelContextProtocol]] — the framework-agnostic MCP protocol concept; this tutorial is the **first whole-program MCP-server worked example** in the corpus (the [[dspy-mcp|Learn page]]'s examples were API-surface snippets only). **Update needed:** add this tutorial as a second source.
- [[FastMCP]] — **entity page minted by this ingest.** The `mcp.server.fastmcp.FastMCP` helper that lets a Python file declare an MCP server with one decorator per tool; first wiki-corpus appearance.
- [[dspy-mcp]] — the [[DSPyMCP|DSPy Learn — MCP page]] (page 8 of 13); this tutorial is its applied counterpart (server-side and full-agent worked example vs API-surface reference docs).
- [[dspy-customer-service-agent]] — the **non-MCP variant** of the same airline domain. The five [[Pydantic]] classes are identical (`Date`, `UserProfile`, `Flight`, `Itinerary`, `Ticket`); the seven tools are identical except `pick_flight` is split out as a helper (the prior tutorial folded that ordering into the LM's `fetch_flight_info → book_itinerary` reasoning). The Signature is byte-identical (`class DSPyAirlineCustomerService(dspy.Signature)` with `user_request: str` → `process_result: str`). The diff is **packaging**, not **information architecture**.
- [[CustomerServiceAgent]] — the application-pattern concept; the MCP variant fits the **same** pattern (lookup / mutation / escalation tools, two-field Signature, [[react|ReAct]] loop) with a different tool-transport substrate.
- [[react|ReAct]] — the canonical [[DSPyModules|Module]] consuming the converted MCP tools; `dspy.ReAct(...).acall(...)` is invoked once per agent run.
- [[DSPyTools]] — the typed-tool abstraction that `from_mcp_tool` constructs into; the resulting tool list is consumed identically to a list of local Python functions.
- [[DSPyPredict]] — the manual-handling alternative; MCP-converted tools fit the same `tools: list[dspy.Tool]` Signature input.
- [[DSPySignatures]] — class-based `DSPyAirlineCustomerService` Signature with two fields and a docstring scoping the agent's role.
- [[DSPyPrediction]] — the agent return type; carries `trajectory` + `reasoning` + `process_result`.
- [[DSPyLM]] — `dspy.LM("openai/gpt-4o-mini")` as the underlying LM client.
- [[DSPyAdapters]] — the wire-format layer; the Adapter sees a typed `dspy.Tool` and is unaware that the execution callback routes through an MCP session.
- [[Pydantic]] — the five domain classes (`Date`, `UserProfile`, `Flight`, `Itinerary`, `Ticket`); compose through the MCP wire protocol via [[FastMCP]]'s automatic JSON Schema generation.
- [[anthropic|Anthropic]] — originator of the MCP protocol.
- [[openai|OpenAI]] — provider of `gpt-4o-mini`, the LM used in the tutorial.
- [[dspy-learn-index]] — parent Learn index; the [[dspy-mcp|MCP page]] this tutorial complements is item 7 in the Programming-stage sub-topics.
- [[ToolUse]] — generic tool-use concept; MCP is one protocol-level realization, this tutorial is one applied receipt.
- [[DSPyAsync]] — DSPy's async surface; this tutorial's `async`/`await` discipline is mandated by MCP's async-only execution model and slots directly into the framework-wide async story.
- `asyncio.run(run("..."))` is the script's entrypoint — first wiki-corpus DSPy receipt to use the bare-`asyncio.run(...)` driver for an MCP-routed agent.

## Contradictions

None. The tutorial **extends** every prior MCP-and-DSPy ingest:

- [[dspy-mcp|The Learn — MCP page]] documented `dspy.Tool.from_mcp_tool` with two minimal snippets (stdio + streamable-HTTP); this tutorial supplies the **whole-program** receipt — the full server source, the full agent script, the launch commands. The two pages compose: the Learn page is the API reference, this tutorial is the worked example.

- [[dspy-customer-service-agent|The Customer Service Agent tutorial]] showed the airline domain with tools as plain Python callables passed directly to `dspy.ReAct`; this tutorial shows the **same** domain with tools wrapped in `@mcp.tool()` decorators and reached via `dspy.Tool.from_mcp_tool`. The diff isolates the **MCP packaging layer** as the only variable — confirming [[DSPyMCP|the binding's]] claim that *"MCP-converted tools are indistinguishable from local-function tools after conversion"*.

- [[dspy-tools|The Tools page]]'s `dspy.Tool` design was justified in part by claiming it would accommodate non-Python-function tool sources. This tutorial is the **first whole-program corpus demonstration** that the design holds — a complete agent runs against tools whose origin is an external server process the agent doesn't author.

Three productive sharpenings of the wiki's prior framing:

1. **[[FastMCP]] is the canonical Python MCP-server author surface.** The wiki had not previously distinguished `mcp.server.fastmcp.FastMCP` from the broader [[ModelContextProtocol|MCP]] protocol; this tutorial introduces it as the *decorator-style helper* that reduces server authoring to the same ergonomic level as Flask / FastAPI route declaration.

2. **`pick_flight` formalizes the "deterministic utility tool" subpattern.** Prior wiki tools-as-functions framing treated tools as **external-resource accessors** (APIs, databases, retrievers). `pick_flight` is internal Python (sort by duration then price) exposed as a tool — pushing ordering / comparison into deterministic code rather than asking the LM to do it. This is a small but recurring pattern worth naming.

3. **The `dict | BaseModel` double-dispatch idiom is the first serialization-boundary receipt in the corpus.** Prior DSPy tutorials passed [[Pydantic]] objects between functions where class binding survived. MCP introduces a JSON wire boundary; the tutorial's *"`x.get('duration') if isinstance(x, dict) else x.duration`"* pattern is the standard accommodation. This is worth capturing as a portable applied-LM/serialization guideline for future ingests.
