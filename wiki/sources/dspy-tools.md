---
title: "DSPy Learn — Tools"
type: source
tags: [dspy, llm-programming, tools, function-calling, agents, react, async]
date: 2026-05-17
source_file: raw/dspy-tools.md
---

## Summary

**Page 7 of 13** of the [[DSPy]] *Learn* documentation. Defines the **Tools** sub-system — the primitive [[DSPy]] uses to let an [[DSPyLM|LM]] invoke external Python functions. The page presents **two equal-status approaches**: **(1)** the **fully-managed** [[react|`dspy.ReAct`]] [[DSPyModules|Module]] (the framework owns the think-act-observe loop, the tool dispatch, and the error recovery — *"automatic reasoning and tool selection"*) and **(2)** **manual handling** via the [[DSPyTools|`dspy.Tool`]] wrapper plus the `dspy.ToolCalls` model-output type (the user owns the loop and the dispatch — *"precise control over execution"*). Documents the [[DSPyTools|`dspy.Tool`]] surface (`.name` / `.desc` / `.args` / `str(tool)` derived from the wrapped function's name, docstring, and type hints), the `ToolCall.execute()` API with three lookup modes (automatic-by-name / explicit `functions={}` dict / explicit `functions=[]` `Tool` list — requires **DSPy 3.0.4b2+**), the **native function-calling** opt-in (`use_native_function_calling=` kwarg on [[DSPyAdapters|`dspy.ChatAdapter`]] / [[DSPyAdapters|`dspy.JSONAdapter`]] — defaults to **off** for `ChatAdapter`, **on** for `JSONAdapter`, with automatic text-parse fallback for models that don't support it), and **async tools** (`tool.acall(...)` recommended; `with dspy.context(allow_tool_async_sync_conversion=True):` for calling async tools from sync code). **Resolves the long-standing forward reference [[DSPyTools]]** carried by every prior DSPy ingest since the corpus opened on 2026-05-17.

## Key Claims

- **Two equal-status approaches, not a primary-and-alternative.** The page presents `dspy.ReAct` and manual handling as **paired** options — *"DSPy offers two ways to implement tool-using agents"* — and closes with a When-to-Use decision rubric that gives manual handling four concrete advantages (precise control / custom error handling / latency / void-return tools). This **promotes** the *Learn* corpus's prior framing in which [[react|`dspy.ReAct`]] was the canonical tool-using Module on [[dspy-modules]] (page 5); the Tools page makes the manual handling path equally first-class.

- **`dspy.ReAct` is the fully-managed wrapper.** [[react|`dspy.ReAct`]] takes `signature=...`, `tools=[...]` (plain Python callables), and `max_iters=...`, and returns a `Prediction` carrying both the final output field(s) and a **`trajectory`** field — *"complete reasoning trajectory tracking"* — recording every reasoning step and every tool call made. *"Multiple sequential tool calls capability"* and *"built-in error recovery"* are framework responsibilities, not user-code responsibilities.

- **The manual-handling Signature pattern.** Manual handling declares a [[DSPySignatures|Signature]] with **two fields the user normally wouldn't write themselves** — `tools: list[dspy.Tool] = dspy.InputField()` (the toolset is **passed in at call time**, not baked into the Module) and `outputs: dspy.ToolCalls = dspy.OutputField()` (the LM emits a structured list of tool invocations, **not** the final answer). The user then runs `dspy.Predict(ToolSignature)`, iterates `response.outputs.tool_calls`, and calls `.execute()` on each — the **loop is the user's**, not the framework's.

- **`dspy.Tool` exposes four properties.** The wrapper exposes `.name` (= the wrapped function's `__name__`), `.desc` (= the function's docstring — what the LM sees to decide *when* to call), `.args` (= a parameter schema built from type hints + defaults), and `str(tool)` (= the canonical text representation included in the prompt). This is the **DSPy-side** of the function-calling abstraction every LM provider exposes.

- **Three tool-function design rules.** The page makes the **prompt-engineering side of tool design explicit**: (1) write clear, detailed docstrings (the LM uses them to pick the right tool); (2) use explicit type hints (the LM uses them to fill in arguments); (3) prefer basic types (`str` / `int` / `bool` / `dict` / `list`) or [[Pydantic|Pydantic]] models. The worked `good_tool` example shows the full pattern — `Args:` / `Returns:` Google-style docstring + explicit type hints + sensible defaults + an empty-string guard.

- **`ToolCall.execute()` has three lookup modes.** The `call.execute(...)` API resolves `call.name` against either (1) the **calling scope** automatically (no `functions=` kwarg — relies on the function being in scope), (2) an explicit `functions={"name": fn, ...}` **dictionary**, or (3) an explicit `functions=[dspy.Tool(fn), ...]` **list of `Tool` objects**. The three modes share the same API — the framework picks the lookup strategy from the kwarg shape. **Requires DSPy 3.0.4b2 or later** (the page's only version-gated feature).

- **Native function-calling is per-Adapter, not per-Module.** [[DSPyTools|Tool]] dispatch composes through the [[DSPyAdapters|Adapter]] axis — the choice of "native function-calling vs text-parsing" is configured at Adapter construction time via the `use_native_function_calling=` kwarg. Adapter defaults: **`ChatAdapter`** defaults to **off** (text-based parsing — works with every LM); **`JSONAdapter`** defaults to **on** (native function-calling). Either default can be overridden at construction. *"DSPy automatically falls back to text-based parsing if the model doesn't support native function-calling"* — the same automatic-recovery discipline [[DSPyAdapters|`ChatAdapter`]] applies to JSON parsing.

- **The Adapter-level Tool plumbing confirms the Adapters-page claim.** [[dspy-adapters|The Adapters page]] (page 6) listed *"converting DSPy types (`Tool`, `Image`, etc.) into prompt messages"* as an [[DSPyAdapters|Adapter]] responsibility. This page **operationalizes** that claim: the `use_native_function_calling=` kwarg lives on the Adapter, not on `dspy.ReAct`; the [[DSPyTools|Tool]]-list ↔ LM-wire-format mapping is the Adapter's job. The Tools sub-system is **not a parallel pipeline** to the rest of DSPy — it composes through the same four-concerns decomposition.

- **Async tools are first-class.** `dspy.Tool(async_fn)` wraps `async def` functions; `await tool.acall(**kwargs)` is the recommended sync-API form. For sync call-sites that need to invoke async tools, the **`dspy.context(allow_tool_async_sync_conversion=True)`** block transparently runs the coroutine on an internal event loop — a deliberate ergonomic opt-in, off by default to avoid surprising sync code with implicit async execution.

- **The When-to-Use decision rubric.** *"Choose `dspy.ReAct` when: automatic reasoning and tool selection are desired; tasks require multiple sequential tool calls; built-in error recovery is beneficial; focus on tool implementation over orchestration is preferred."* *"Choose manual handling when: precise execution control is necessary; custom error-handling logic is required; latency minimization matters; tools return no values (void functions)."* The **void-return** case is the most informative — `dspy.ReAct`'s loop depends on observations to feed back into the next reasoning step; void tools (e.g., logging, side-effects without return) don't fit cleanly and motivate the manual path.

## Key Quotes

> "DSPy offers two ways to implement tool-using agents" — opening framing; positions [[react|`dspy.ReAct`]] and manual handling as **paired** options, not primary-and-alternative.

> "`dspy.ReAct` implements the Reasoning-and-Acting pattern: the LM iteratively reasons about the situation and decides which tool to call next." — the canonical one-line definition of [[react|ReAct]] inside DSPy.

> "Complete reasoning trajectory tracking" — the `Prediction.trajectory` field that [[react|`dspy.ReAct`]] returns alongside the final answer.

> "Requires DSPy 3.0.4b2 or later for the `ToolCall.execute()` method." — the one version-gated feature on the page; the manual-handling path is newer than [[react|`dspy.ReAct`]].

> "DSPy automatically falls back to text-based parsing if the model doesn't support native function-calling." — the automatic-recovery discipline at the [[DSPyAdapters|Adapter]] / [[DSPyTools|Tool]] boundary; parallels [[dspy-adapters|`ChatAdapter`]]'s automatic [[DSPyAdapters|`JSONAdapter`]] fallback on parse failure.

> "Tools return no values (void functions)" — the most informative case in the When-to-Use rubric for manual handling; void tools don't fit [[react|`dspy.ReAct`]]'s observation-feedback loop.

## Code Examples

The `dspy.ReAct` happy path:

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

The manual-handling path:

```python
import dspy

class ToolSignature(dspy.Signature):
    """Signature for manual tool handling."""
    question: str = dspy.InputField()
    tools: list[dspy.Tool] = dspy.InputField()
    outputs: dspy.ToolCalls = dspy.OutputField()

def weather(city: str) -> str:
    """Get weather information for a city."""
    return f"The weather in {city} is sunny"

def calculator(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        result = eval(expression)
        return f"The result is {result}"
    except Exception:
        return "Invalid expression"

tools = {
    "weather": dspy.Tool(weather),
    "calculator": dspy.Tool(calculator),
}

predictor = dspy.Predict(ToolSignature)

response = predictor(
    question="What's the weather in New York?",
    tools=list(tools.values()),
)

for call in response.outputs.tool_calls:
    result = call.execute()
    print(f"Tool: {call.name}")
    print(f"Args: {call.args}")
    print(f"Result: {result}")
```

Inspecting a `dspy.Tool`:

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

The three `execute()` lookup modes:

```python
for call in response.outputs.tool_calls:
    # Option 1: automatic discovery
    result = call.execute()

    # Option 2: pass tools as dict
    result = call.execute(functions={"weather": weather, "calculator": calculator})

    # Option 3: pass Tool objects as list
    result = call.execute(functions=[dspy.Tool(weather), dspy.Tool(calculator)])
```

Native function-calling at the [[DSPyAdapters|Adapter]] layer:

```python
import dspy

chat_adapter_native = dspy.ChatAdapter(use_native_function_calling=True)
json_adapter_manual = dspy.JSONAdapter(use_native_function_calling=False)

dspy.configure(
    lm=dspy.LM(model="openai/gpt-4o"),
    adapter=chat_adapter_native,
)
```

Async tools with `tool.acall(...)`:

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

…and the sync-from-async opt-in:

```python
with dspy.context(allow_tool_async_sync_conversion=True):
    result = tool(city="New York")
```

The well-designed-tool template:

```python
def good_tool(city: str, units: str = "celsius") -> str:
    """
    Get weather information for a specific city.

    Args:
        city: The name of the city to get weather for
        units: Temperature units, either 'celsius' or 'fahrenheit'

    Returns:
        A string describing the current weather conditions
    """
    if not city.strip():
        return "Error: City name cannot be empty"
    return f"Weather in {city}: 25°{units[0].upper()}, sunny"
```

## Connections

- [[DSPy]] — the framework whose Tools sub-system this page defines. Page 7 of 13 of *Learn*.
- [[DSPyTools]] — **concept page minted by this ingest.** The canonical wiki anchor for the `dspy.Tool` abstraction and the manual-handling `dspy.ToolCalls` path; **resolves the long-standing forward reference** carried by [[DSPy]] / [[DSPyProgrammingModel]] / [[DSPySignatures]] / [[DSPyLM]] / [[DSPyModules]] / [[DSPyAdapters]] / [[react|ReAct]] / [[dspy-learn-index]] / [[dspy-programming-overview]] / [[dspy-language-models]] / [[dspy-signatures]] / [[dspy-modules]] / [[dspy-adapters]] since the corpus opened on 2026-05-17.
- [[react|ReAct]] — the **think-act-observe** prompting pattern [[react|`dspy.ReAct`]] implements; the page extends [[react|the existing ReAct concept page]] with the *manual-vs-managed* duality it inherits from the Tools page.
- [[DSPyModules]] — the parent abstraction; [[react|`dspy.ReAct`]] is one of the seven built-in [[DSPyModules|Modules]].
- [[DSPyPredict]] — the minimal primitive the manual-handling path is built on top of (`predictor = dspy.Predict(ToolSignature)`).
- [[DSPySignatures]] — the typed I/O contract that names the `tools: list[dspy.Tool]` input field and the `outputs: dspy.ToolCalls` output field; the manual-handling pattern is a Signature-shape recipe.
- [[DSPyAdapters]] — the wire-format layer where native-vs-text function calling is configured (`use_native_function_calling=` kwarg). The [[dspy-adapters|Adapters page]]'s claim that *"the Adapter converts `Tool` / `Image` / `History` into prompt messages"* is operationalized here.
- [[DSPyPrediction]] — the typed return object of both paths; for [[react|`dspy.ReAct`]] it carries an extra `trajectory` field.
- [[DSPyProgrammingModel]] — the four-concerns design philosophy that runs through the Tools sub-system: [[DSPySignatures|Signature]] declares the tool-list input + tool-calls output; [[DSPyModules|Module]] picks the strategy ([[react|`dspy.ReAct`]] vs manual); [[DSPyAdapters|Adapter]] picks the wire format (native vs text); [[DSPyOptimizers|Optimizer]] tunes the prompts and demos that govern tool selection.
- [[DSPyLM]] — the underlying LM client; native function-calling routes through the provider's native channel, plumbed via [[LiteLLM]].
- [[LiteLLM]] — the upstream provider-abstraction; native function-calling parameters are routed through LiteLLM's per-provider mappings.
- [[ModelContextProtocol]] — DSPy integrates with MCP (page 8 of 13, forward reference); MCP servers expose tools that compose through the same [[DSPyTools|`dspy.Tool`]] abstraction.
- [[DSPyOptimizers]] — forward reference (page 13 of 13); Optimizers tune the prompts and demonstrations that govern *which* tools the LM chooses to call and *how* it formulates the arguments.
- [[2604.25850-agentic-harness-engineering|Agentic Harness Engineering]] — the contemporary critique of *"DSPy-style instruction tuning"*; the harness paper's argument is that tools / middleware / long-term memory are the load-bearing components, not the system prompt. The Tools page is the wiki's **first explicit DSPy treatment of the tools layer** that critique points at — DSPy *does* have a tools abstraction; the critique sharpens to *who tunes it and how*.
- [[2604.21590-agenticqwen|AgenticQwen]] — names CoT and [[react|ReAct]] as baseline tool-use foundations; the DSPy Tools page is the framework-level operationalization of the [[react|ReAct]] baseline.
- [[FunctionCall]] — the wiki's existing C-language *function-call* concept (runtime semantics; per-frame stack discipline); the LM-side tool-call is the **prompt-level analog** — same `function_name(arg1=...)` syntactic shape, different execution substrate (LM prompt + dispatch, not stack-frame + jump). The two are **not the same concept** and should not be conflated; the link is for cross-disambiguation only.
- [[Pydantic]] — the page's design guidance — *"prefer basic parameter types (`str`, `int`, `bool`, `dict`, `list`) or Pydantic models"* — names Pydantic as the recommended escape hatch for complex tool parameter shapes. Forward reference.

## Contradictions

None. The Tools page **extends** every prior DSPy ingest:

- [[dspy-modules]] introduced [[react|`dspy.ReAct`]] as one of the seven built-in [[DSPyModules|Modules]] (the *tool-using agent* row). This page **adds** the manual-handling path as an equal-status alternative — `dspy.Predict(ToolSignature)` is the same `dspy.Predict` primitive, with a Signature whose input field is `list[dspy.Tool]` and whose output field is `dspy.ToolCalls`. The seven-built-ins enumeration on the Modules page is unchanged; manual handling is a Signature-shape recipe, not a new Module.
- [[dspy-adapters]] listed *"converting DSPy types (`Tool`, `Image`, etc.) into prompt messages"* as an [[DSPyAdapters|Adapter]] responsibility. This page **operationalizes** that claim by surfacing the `use_native_function_calling=` kwarg at the Adapter constructor — confirming the Adapter is the single funnel through which the [[DSPyTools|Tool]] axis crosses into the LM's wire format.
- [[dspy-signatures]] documented `dspy.Image` and `dspy.History` as DSPy-special types; this page adds `dspy.Tool` and `dspy.ToolCalls` to that family — they're typed primitives, not stringly-typed conventions, and they participate in the same Signature / Adapter / LM chain.
- [[dspy-language-models]]'s LM-agnostic claim acquires a **second** model-capability scoping (after [[dspy-adapters|`JSONAdapter`]]'s `response_format` requirement): native function-calling depends on the model implementing it. DSPy's automatic-fallback-to-text-parsing means the *"swap the LM"* portability still holds — but only because the framework absorbs the capability gap.

Three productive clarifications of the wiki's prior framing:

1. **The wiki's existing [[react|ReAct]] concept page treats `dspy.ReAct` as the canonical DSPy tool-use entry point.** This page promotes that framing — `dspy.ReAct` *is* DSPy's fully-managed entry point — and adds a co-equal manual path that the [[react|ReAct]] page should record. The [[react|ReAct]] page is extended in-place rather than duplicated as a `DSPyReAct` page, consistent with [[dspy-modules]]'s precedent.

2. **The Tools axis is composable, not isolated.** The four-concerns decomposition [[DSPyProgrammingModel|the Programming Model]] proposes survives the introduction of Tools: [[DSPySignatures|Signature]] / [[DSPyModules|Module]] / [[DSPyAdapters|Adapter]] / [[DSPyOptimizers|Optimizer]] each have a role in how tools are declared, dispatched, formatted on the wire, and tuned. The Tools sub-system is **not** a parallel pipeline.

3. **The void-return tool case is the page's most distinctive guidance.** *"Tools return no values (void functions)"* as a reason to choose manual handling is non-obvious — most tool-use literature implicitly assumes observation-returning tools. The Tools page's explicit recognition of void tools (logging, side-effects, fire-and-forget actions) is a small but consequential framework-design choice the wiki should preserve.
