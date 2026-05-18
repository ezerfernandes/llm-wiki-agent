---
title: "DSPy Tools"
type: concept
tags: [dspy, llm-programming, tools, function-calling, agents, async, framework]
sources: [dspy-tools, dspy-modules, dspy-adapters, dspy-learn-index, dspy-mcp]
last_updated: 2026-05-17
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
