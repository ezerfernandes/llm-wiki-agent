---
title: "DSPy Tools"
type: concept
tags: [dspy, llm-programming, tools, function-calling, agents, async, framework]
sources: [dspy-tools, dspy-modules, dspy-adapters, dspy-learn-index, dspy-mcp, dspy-yahoo-finance-react-tutorial, dspy-async-tutorial, dspy-tool-use-tutorial]
last_updated: 2026-05-24
---

# DSPy Tools

**A DSPy Tool is `dspy.Tool` — a typed wrapper around a Python function that lets a [[DSPyLM|language model]] *invoke* the function as part of a [[DSPy]] program**. The wrapper exposes the function's name, docstring, and type-hinted parameter schema in the form an [[DSPyAdapters|Adapter]] can emit into a prompt (or hand off to a provider's native function-calling channel), and the matching `dspy.ToolCalls` output type carries the LM's requested invocations back into Python for execution. `dspy.Tool` is the **fifth DSPy-special type** in the [[DSPySignatures|Signature]] type system (alongside `dspy.Image`, `dspy.History`, and the seventh-page `dspy.ToolCalls`), and the substrate the tool-using [[DSPyModules|Modules]] — [[react|`dspy.ReAct`]] above all — compose against. This concept page records the abstraction itself; [[dspy-tools|the Tools page]] (page 7 of 13 of the DSPy *Learn* documentation) is the canonical source.

## What a Tool *is*

A `dspy.Tool` wrapper turns a plain Python callable into a value the framework can:

- **Describe to the LM** — by serializing `.name` / `.desc` / `.args` into a tool-spec message (either as text the LM is told to follow, or as a native function-calling schema the provider parses directly).
- **Pass through a [[DSPySignatures|Signature]]** — `tools: list[dspy.Tool]` is a legal Signature input field; the toolset is **runtime-determined**, not Module-baked.
- **Execute on the LM's behalf** — once the LM emits a `dspy.ToolCalls` output, `call.execute(...)` resolves each requested tool against either the calling scope, an explicit `functions={}` dict, or an explicit `functions=[Tool,...]` list, and runs it.

```python
def my_function(param1: str, param2: int = 5) -> str:
    """A sample function with parameters."""
    return f"Processed {param1} with value {param2}"

tool = dspy.Tool(my_function)
print(tool.name)    # "my_function"
print(tool.desc)    # The function's docstring
print(tool.args)    # Parameter schema (built from type hints + defaults)
print(str(tool))    # Full tool description the LM sees
```

Properties:

| Property | What it is | Where it comes from |
|---|---|---|
| `name` | Tool identifier | `fn.__name__` |
| `desc` | Tool description | `fn.__doc__` (the docstring) |
| `args` | Parameter schema | Type hints + default values |
| `str(tool)` | Canonical text representation | Composed from the three above |

These four surfaces are **what the LM sees**. The docstring and type hints are not optional comments — they are the **prompt-engineering interface** for tool selection. The page's [[dspy-tools|design-guidance section]] is explicit: *"write clear, detailed docstrings; use explicit type hints; prefer basic parameter types (`str`, `int`, `bool`, `dict`, `list`) or [[Pydantic|Pydantic]] models."*

## `dspy.ToolCalls` — the model-output side

When a [[DSPySignatures|Signature]] declares `outputs: dspy.ToolCalls = dspy.OutputField()`, the LM is asked to return a structured list of tool invocations rather than a final answer. Each `call` in `response.outputs.tool_calls` has:

- `call.name` — the tool the LM is asking to invoke.
- `call.args` — the keyword-argument dictionary the LM produced (parsed from native function-calling or text, depending on the [[DSPyAdapters|Adapter]] configuration).
- `call.execute(...)` — runs the tool. Three lookup modes:

```python
# Option 1: automatic discovery — looks up by name in the calling scope
result = call.execute()

# Option 2: explicit functions dict
result = call.execute(functions={"weather": weather, "calculator": calculator})

# Option 3: explicit Tool-object list
result = call.execute(functions=[dspy.Tool(weather), dspy.Tool(calculator)])
```

The `.execute()` method requires **DSPy 3.0.4b2 or later** — the only version-gated feature on the Tools page.

## The two equal-status approaches

[[dspy-tools|The Tools page]] presents two **paired** approaches to tool-using agents — not a primary-and-alternative pairing:

### 1. `dspy.ReAct` — fully managed

[[react|`dspy.ReAct`]] is the framework-owned think-act-observe loop:

```python
import dspy

def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"The weather in {city} is sunny and 75°F"

def search_web(query: str) -> str:
    """Search the web for information."""
    return f"Search results for '{query}': [relevant information...]"

react_agent = dspy.ReAct(
    signature="question -> answer",
    tools=[get_weather, search_web],
    max_iters=5,
)

result = react_agent(question="What's the weather like in Tokyo?")
print(result.answer)
print("Tool calls made:", result.trajectory)
```

Three properties:

- **Plain Python callables are auto-wrapped.** The `tools=[...]` kwarg accepts ordinary functions; the framework wraps each in a `dspy.Tool` under the hood.
- **The loop is the framework's.** `max_iters` bounds it; the LM controls termination.
- **The return carries a `trajectory` field.** Every reasoning step and every tool call made is recorded — *"complete reasoning trajectory tracking."*

### 2. Manual handling — user owns the loop

The manual path uses [[DSPyPredict|`dspy.Predict`]] directly with a [[DSPySignatures|Signature]] whose input includes a `tools` field and whose output is a `dspy.ToolCalls`:

```python
import dspy

class ToolSignature(dspy.Signature):
    """Signature for manual tool handling."""
    question: str = dspy.InputField()
    tools: list[dspy.Tool] = dspy.InputField()
    outputs: dspy.ToolCalls = dspy.OutputField()

predictor = dspy.Predict(ToolSignature)

response = predictor(
    question="What's the weather in New York?",
    tools=list(tools.values()),
)

for call in response.outputs.tool_calls:
    result = call.execute()
```

Three properties:

- **Single LM call, no built-in loop.** The user iterates `response.outputs.tool_calls` and decides what to do with each — including building a multi-turn loop manually if the task needs it.
- **The toolset is a runtime input.** `tools: list[dspy.Tool]` is a [[DSPySignatures|Signature]] input field — different invocations can pass different toolsets without modifying the Signature or the Module.
- **Void-return tools are first-class.** [[react|`dspy.ReAct`]]'s loop expects each observation to feed back into the next reasoning step; the manual path has no such expectation — tools can be side-effect-only.

## When to use which

[[dspy-tools|The Tools page]]'s decision rubric:

| Choose `dspy.ReAct` when | Choose manual handling when |
|---|---|
| Automatic reasoning and tool selection are desired | Precise execution control is necessary |
| Tasks require multiple sequential tool calls | Custom error-handling logic is required |
| Built-in error recovery is beneficial | Latency minimization matters |
| Focus on tool implementation over orchestration is preferred | Tools return no values (void functions) |

The **void-return** case is the most informative of the four manual-path advantages — most tool-use literature implicitly assumes observation-returning tools. [[dspy-tools|The page's]] explicit recognition of void tools (logging, telemetry emission, side-effect-only actions) is a small but consequential framework-design point.

## Native function calling

The [[DSPyAdapters|Adapter]] axis controls whether tools cross into the LM via **native function calling** (OpenAI's `tools` parameter, Anthropic's `tool_use`, Gemini's function-calling) or via **text-based parsing** (the LM is prompted to emit tool calls in the Adapter's serialization format, then the framework parses them).

Adapter defaults:

| Adapter | `use_native_function_calling` default |
|---|---|
| [[DSPyAdapters\|`dspy.ChatAdapter`]] | `False` (text-based parsing) |
| [[DSPyAdapters\|`dspy.JSONAdapter`]] | `True` (native function calling) |

Either default is overridable at construction time:

```python
chat_adapter_native = dspy.ChatAdapter(use_native_function_calling=True)
json_adapter_manual = dspy.JSONAdapter(use_native_function_calling=False)

dspy.configure(
    lm=dspy.LM(model="openai/gpt-4o"),
    adapter=chat_adapter_native,
)
```

**Automatic fallback.** If the configured model does not support native function calling, the framework automatically falls back to text-based parsing — the same automatic-recovery discipline [[DSPyAdapters|`ChatAdapter`]] applies to its [[DSPyAdapters|`JSONAdapter`]] parse-failure path. This is the **second model-capability scoping** in the [[dspy-learn-index|Learn corpus]] (after [[DSPyAdapters|`JSONAdapter`]]'s `response_format` requirement) — and the second time the framework absorbs the gap behind an automatic fallback rather than failing.

## Async tools

`dspy.Tool` works on both sync and async callables. The recommended async-call form is `tool.acall(...)`:

```python
import asyncio
import dspy

async def async_weather(city: str) -> str:
    """Get weather information asynchronously."""
    await asyncio.sleep(0.1)
    return f"The weather in {city} is sunny"

tool = dspy.Tool(async_weather)
result = await tool.acall(city="New York")
```

For sync call-sites that need to invoke async tools, the framework provides an opt-in context flag:

```python
with dspy.context(allow_tool_async_sync_conversion=True):
    result = tool(city="New York")
```

The flag is **off by default** — sync code that accidentally invokes an async tool would otherwise return a coroutine without surfacing the mismatch. Making the sync-from-async path explicit is a deliberate ergonomic choice.

## Tool origin is decoupled from tool consumption ([[ModelContextProtocol|MCP]])

The `dspy.Tool` wrapper is **not** locked to local Python functions. A second construction path — `dspy.Tool.from_mcp_tool(session, mcp_tool)` ([[dspy-mcp]], page 8 of 13) — converts a [[ModelContextProtocol|Model Context Protocol]] tool descriptor (from a remote or local MCP server) into a `dspy.Tool` instance whose execution callback routes asynchronously back through the open MCP `ClientSession`. The resulting `dspy.Tool` is **indistinguishable** from a locally-built one: it composes through [[react|`dspy.ReAct`]], through manual [[DSPyPredict|`dspy.Predict`]] with `tools: list[dspy.Tool]` input, and through direct `tool.acall(...)` invocation. The only operational constraint is that MCP-routed tools require `.acall(...)` (MCP execution is async end-to-end) and the agent invocation must live inside the `async with` MCP session block. See [[DSPyMCP]] for the DSPy-specific binding and [[ModelContextProtocol]] for the protocol itself.

This vindicates the page-7 async-tool surface (`tool.acall(...)`, `dspy.context(allow_tool_async_sync_conversion=True)`) as **load-bearing infrastructure**, not a corner-case feature — MCP integration *requires* it.

## Third construction path — `Tool.from_langchain(...)` ([[LangChain]] bridge)

Added by [[dspy-yahoo-finance-react-tutorial|the Yahoo Finance ReAct tutorial]]: a third documented construction path that converts a [[LangChain]] tool instance into a `dspy.Tool`:

```python
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from dspy.adapters.types.tool import Tool

yahoo_finance_tool = YahooFinanceNewsTool()
finance_news_tool = Tool.from_langchain(yahoo_finance_tool)
```

The resulting `Tool` instance is **indistinguishable** in downstream composition from an auto-wrapped plain-callable tool or an MCP-derived one — [[react|`dspy.ReAct`]] consumes it in the same `tools=[...]` list, [[DSPyAdapters|Adapters]] serialize it the same way, manual [[DSPyPredict|`dspy.Predict`]] with `tools: list[dspy.Tool]` input accepts it. **`dspy.Tool` is therefore the single integration point between DSPy and the external tool ecosystem** — plain Python, [[ModelContextProtocol|MCP]] servers, and [[LangChain]] community tools all collapse to the same downstream type.

Construction paths after this tutorial:

| Path | Source | First-receipt wiki page |
|---|---|---|
| Auto-wrap plain Python callable (`dspy.ReAct(tools=[fn])` / `dspy.Tool(fn)`) | function + docstring + type hints | [[dspy-tools]] / [[react]] |
| `Tool.from_mcp_tool(session, mcp_tool)` | [[ModelContextProtocol\|MCP]] server descriptor | [[dspy-mcp]] / [[DSPyMCP]] |
| `Tool.from_langchain(langchain_tool)` | [[LangChain]] tool instance | [[dspy-yahoo-finance-react-tutorial]] |
| **Raw-callable dict via Signature input field** (no `dspy.Tool` wrapper) | `inspect.signature` + `inspect.getdoc` + author-controlled `dict[str, Any]` schema | [[dspy-tool-use-tutorial]] / [[HandRolledReAct]] |

## Fourth construction path — per-question raw-callable dict (no `dspy.Tool`)

The [[dspy-tool-use-tutorial|DSPy tool-use tutorial]] introduces a **fourth tool-construction path** that **bypasses `dspy.Tool` entirely**: the agent receives a per-question Python `dict[str, callable]` as an input field, the author computes tool metadata via stdlib `inspect.signature(...)` + `inspect.getdoc(...)`, and the metadata is presented to the LM as a `dict[str, Any]` Signature field. This is the **runtime-varying tool-set** path — appropriate when:

1. Tool sets vary per example (e.g. [[ToolHop]] ships a different `functions` list per datapoint).
2. The tool metadata schema needs author control (e.g. you want to omit certain fields or add custom annotations).
3. Tool runtimes need sandbox wrapping (e.g. [[func_timeout|`@func_set_timeout(10)`]] for untrusted code) — easier to bolt on at the loop level than inside `dspy.Tool`.

The tutorial's recipe:

```python
def fn_metadata(func):
    signature = inspect.signature(func)
    docstring = inspect.getdoc(func) or "No docstring."
    return dict(function_name=func.__name__, arguments=str(signature), docstring=docstring)

# Then in the agent:
tools = {fn_name: fn_metadata(fn) for fn_name, fn in functions.items()}
pred = self.react(question=question, trajectory=trajectory, functions=tools)
```

The Signature output emits `next_selected_fn: str` (the tool name) and `args: dict[str, Any]` (the tool arguments); the agent's `forward()` method dispatches into the real callable dict by name. **`dspy.Tool` is not in the loop** — the manual pattern preserves all of DSPy's optimizer composability (the program is still a `dspy.Module`) while losing the framework's native-function-calling Adapter hook. Trade is explicit: more author control for less framework support.

See [[HandRolledReAct]] for the broader pattern, and [[dspy-tool-use-tutorial]] for the canonical [[SIMBA]]-optimized receipt.

The tutorial also documents that `allow_tool_async_sync_conversion=True` can be set **process-wide** via `dspy.configure(...)` — not only inside a `with dspy.context(...)` block as the page-7 example shows. The configure-time form is appropriate when most tools in a program are async-backed (LangChain community tools commonly are).

## How Tools compose through the four-concerns decomposition

The Tools sub-system is **not** a parallel pipeline next to the rest of [[DSPy]] — it threads through [[DSPyProgrammingModel|the Programming Model's]] four orthogonal artifacts:

| Concern | Tool-side role |
|---|---|
| **[[DSPySignatures\|Signature]]** | Declares `tools: list[dspy.Tool]` input field and `outputs: dspy.ToolCalls` output field (manual path); or accepts an implicit tool-expansion under [[react\|`dspy.ReAct`]] (managed path). |
| **[[DSPyModules\|Module]]** | Picks the strategy: managed via [[react\|`dspy.ReAct`]] (think-act-observe loop) vs manual via [[DSPyPredict\|`dspy.Predict`]] (single LM call, user-owned loop). |
| **[[DSPyAdapters\|Adapter]]** | Picks the wire format: native function calling (`use_native_function_calling=True`) vs text-based parsing. Converts `Tool` / `ToolCalls` instances into the LM's request shape and back. |
| **[[DSPyOptimizers\|Optimizer]]** | Tunes the prompts and demonstrations that govern *which* tools the LM chooses to call and *how* it formulates the arguments. (Forward reference — page 13.) |

This composability is what makes the Tools sub-system a **first-class citizen** of [[DSPy]]'s typed-program design rather than a separately-built agent layer. The Adapter responsibility — *"converting DSPy types (`Tool`, `Image`, etc.) into prompt messages"* — that [[dspy-adapters|the Adapters page]] flagged is operationalized here: the `use_native_function_calling=` kwarg lives on the Adapter, not on `dspy.ReAct` or `dspy.Predict`.

## Why this matters

- **Resolves the long-standing [[DSPyTools]] forward reference.** Every prior DSPy ingest — [[DSPy]] / [[DSPyProgrammingModel]] / [[DSPySignatures]] / [[DSPyLM]] / [[DSPyModules]] / [[DSPyAdapters]] / [[react|ReAct]] / [[dspy-learn-index]] / [[dspy-programming-overview]] / [[dspy-language-models]] / [[dspy-signatures]] / [[dspy-modules]] / [[dspy-adapters]] — carried `[[DSPyTools]]` as a forward reference. The Tools page is what those references point at; this concept page is the canonical anchor.
- **Promotes manual tool handling to equal-status alongside `dspy.ReAct`.** The [[dspy-modules|Modules page]] documented [[react|`dspy.ReAct`]] as the canonical tool-using [[DSPyModules|Module]]; the Tools page sharpens that to a **paired** rubric — managed vs manual — with concrete advantages on each side. The four manual-path advantages (precise control / custom error handling / latency / void-return tools) are non-trivial; the wiki's prior framing in which [[react|`dspy.ReAct`]] was the default-and-only entry point was incomplete.
- **Confirms the Adapter is the single funnel for typed values.** [[dspy-adapters|The Adapters page]] claimed *"the Adapter converts `Tool` / `Image` / `History` into prompt messages"*; the Tools page operationalizes that claim by placing the `use_native_function_calling=` kwarg on the [[DSPyAdapters|Adapter]] constructor — not on `dspy.ReAct`. Tool dispatch composes through the four-concerns decomposition, not around it.
- **Adds the second model-capability scoping to the Learn corpus.** [[DSPyAdapters|`JSONAdapter`]]'s `response_format` requirement was the first; native function calling is the second. In both cases, the framework absorbs the gap behind an automatic fallback to text-based parsing — the *"swap the LM"* portability claim from [[dspy-language-models]] is upheld by the framework's recovery discipline, not by every LM uniformly implementing the same capabilities.
- **`dspy.Tool` is the fifth DSPy-special type.** Together with [[DSPySignatures|`dspy.Image`]] (multi-modal input), `dspy.History` (conversational context), `dspy.ToolCalls` (model-output container), and `dspy.Prediction` (the universal return type), `dspy.Tool` is one of the typed primitives the framework provides on top of Python's `typing` / [[Pydantic]] / dataclasses surface. The DSPy type system is therefore **larger than the Signatures page documented** — the Tools page adds two more types (`Tool` and `ToolCalls`) the wiki should record.
- **Async tools are first-class, not retro-fitted.** The `tool.acall(...)` method and the `dspy.context(allow_tool_async_sync_conversion=True)` opt-in show async tool use is a deliberate framework feature, not an extension. This matters for production deployments where I/O-bound tools (retrieval, web requests, database calls) benefit from async dispatch.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-custom-module]] — names tool integration (Langchain / Agno / **MCP** / database handlers) as one of four example surfaces the *unconstrained `forward()`* contract supports; entry-point for the *tools-are-just-Python-callables* claim.
- [[dspy-yahoo-finance-react-tutorial]] — simplest multi-tool [[react|`dspy.ReAct`]] starter; mixes two plain Python callables (`get_stock_price`, `compare_stocks`) with a [[LangChain]]-bridged tool (`YahooFinanceNewsTool`) via the **third construction path** `Tool.from_langchain(...)`.
- [[dspy-customer-service-agent]] — multi-tool [[react|`dspy.ReAct`]] over a typed airline domain; canonical receipt for **`tools=[...]` of plain Python callables** auto-wrapped into `dspy.Tool` instances by [[react|`dspy.ReAct`]].
- [[dspy-mcp-tutorial]] — **second construction path** `dspy.Tool.from_mcp_tool(session, tool)` over a seven-tool [[FastMCP]] server; confirms `dspy.Tool` is open under tool origin and `tool.acall(...)` is load-bearing infrastructure.
- [[dspy-mem0-react-tutorial]] — wraps memory CRUD (`store_memory`, `search_memories`, `get_all_memories`) plus personalization helpers as `dspy.ReAct` tools; **memory-is-a-tool** pattern — Mem0 persistence exposed entirely through the `tools=[...]` axis with `user_id` arguments for multi-tenancy.
- [[dspy-async-tutorial]] — canonical source for the async-tool surface (`tool.acall(...)`, the `allow_tool_async_sync_conversion=True` context flag) and async [[react|`dspy.ReAct`]].
- [[dspy-streaming-tutorial]] — `StatusMessageProvider.tool_start_status_message` / `tool_end_status_message` hooks surface `dspy.Tool` invocation boundaries through the status-streaming generator; composes the tool axis with the token axis.
- [[dspy-observability-tutorial]] — `BaseCallback.on_tool_start` / `on_tool_end` capture every `dspy.Tool` invocation in the tier-3 custom-instrumentation tier; tutorial diagnoses a stale-retrieval bug via [[MLflow]] traces and fixes it by swapping the [[ColBERTv2]] retriever for a [[Tavily]]-wrapped `dspy.Tool`.
- [[dspy-tool-use-tutorial]] — **fourth construction path** that bypasses `dspy.Tool` entirely: per-question raw `dict[str, callable]` Signature field with `inspect.signature` / `inspect.getdoc` metadata, optimized end-to-end on [[ToolHop]] via [[SIMBA|`dspy.SIMBA`]]; canonical [[HandRolledReAct|hand-rolled ReAct]] receipt.

## Connections

- [[DSPy]] — the framework whose Tools sub-system this concept *is*.
- [[dspy-tools]] — canonical source for the API surface (DSPy *Learn* page 7 of 13).
- [[dspy-learn-index]] — parent Learn index page; lists *Tools* as the sixth Programming-stage sub-topic.
- [[DSPyProgrammingModel]] — the four-concerns design philosophy; the Tools sub-system composes through all four artifacts.
- [[DSPySignatures]] — the typed I/O contract; `tools: list[dspy.Tool]` is a legal input field and `outputs: dspy.ToolCalls` is a legal output field.
- [[DSPyModules]] — the swappable-strategy abstraction; [[react|`dspy.ReAct`]] is the canonical tool-using built-in.
- [[react|ReAct]] — the think-act-observe prompting pattern [[react|`dspy.ReAct`]] implements; extended in-place with the manual-vs-managed duality from this page rather than duplicated as a `DSPyReAct` concept.
- [[DSPyPredict]] — the minimal primitive the manual-handling path is built on top of.
- [[DSPyAdapters]] — the wire-format layer where native-vs-text function calling is configured (`use_native_function_calling=` kwarg); the single funnel through which `Tool` / `ToolCalls` cross into the LM's request shape.
- [[DSPyLM]] — the underlying LM client; native function-calling routes through the provider's native channel.
- [[DSPyPrediction]] — the typed return; [[react|`dspy.ReAct`]] adds a `trajectory` field recording the think-act-observe steps.
- [[DSPyOptimizers]] — forward reference; Optimizers tune the prompts and demos governing tool selection and argument formulation.
- [[ModelContextProtocol]] — the [[anthropic|Anthropic]]-authored open protocol for external tool sources; `dspy.Tool.from_mcp_tool(...)` converts MCP-side tools into `dspy.Tool` instances that compose through every existing DSPy pathway. Forward reference **resolved** by [[dspy-mcp]] (page 8 of 13).
- [[DSPyMCP]] — the DSPy-specific MCP binding; canonical wiki anchor for the `dspy.Tool.from_mcp_tool(...)` construction path and the `async with` session-lifetime contract.
- [[dspy-mcp]] — canonical source for the MCP integration (DSPy *Learn* page 8 of 13).
- [[LiteLLM]] — the upstream provider-abstraction; native function-calling parameters route through LiteLLM's per-provider mappings.
- [[Pydantic]] — the recommended escape hatch for complex tool parameter shapes (*"prefer basic parameter types or Pydantic models"*).
- [[2604.25850-agentic-harness-engineering|Agentic Harness Engineering]] — the contemporary critique of *"DSPy-style instruction tuning"*; the harness paper's argument is that tools / middleware / long-term memory are load-bearing. DSPy's Tools sub-system is the framework-level treatment of that layer.
- [[2604.21590-agenticqwen|AgenticQwen]] — names CoT and [[react|ReAct]] as baseline tool-use foundations; `dspy.Tool` + [[react|`dspy.ReAct`]] is the DSPy operationalization of the ReAct baseline.
- [[FunctionCall]] — the wiki's pre-existing C-language *function-call* concept (stack-frame + jump runtime semantics); the LM-side tool call is the **prompt-level analog** — same `function_name(arg=value)` syntactic shape, different execution substrate. Cross-disambiguation link only; the two concepts are not interchangeable.
- [[DSPyAsync]] — `tool.acall(...)` and `allow_tool_async_sync_conversion=True` (both per-block `dspy.context(...)` and process-wide `dspy.configure(...)` forms) are special cases of the framework-wide async pattern; the Tools-side async surface is documented here, the framework-wide pattern at [[DSPyAsync]].
- [[dspy-async-tutorial]] — canonical source positioning `tool.acall` and the conversion flag inside the broader async-programming surface.
