# DSPy Learn — Tools

Source URL: https://dspy.ai/learn/programming/tools/
Fetched: 2026-05-17 (page 7 of 13 of the DSPy *Learn* section).

---

## Main Approaches

DSPy offers two primary methods for implementing tool-using agents:

1. **`dspy.ReAct`** — Fully automated reasoning and tool selection (the framework picks and executes tools for you).
2. **Manual tool handling** — Direct orchestration control via `dspy.Tool` and `dspy.ToolCalls`.

## Approach 1: `dspy.ReAct` (Fully Managed)

`dspy.ReAct` implements the Reasoning-and-Acting pattern: the LM iteratively reasons about the situation and decides which tool to call next. The framework handles the loop, the tool dispatch, the observation feed-back, and the error recovery.

Key features:

- Automatic reasoning through problem steps.
- Intelligent tool selection based on context.
- Multiple sequential tool calls capability.
- Built-in error recovery mechanisms.
- Complete reasoning trajectory tracking.

Basic usage:

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

Parameters:

- `signature` — input/output specification (a DSPy Signature; inline or class-based).
- `tools` — list of plain Python callables (or `dspy.Tool` wrappers).
- `max_iters` — maximum number of think-act-observe iterations.

The returned `Prediction` carries the final `answer` plus a `trajectory` field that records every reasoning step and every tool call made.

## Approach 2: Manual Tool Handling

When you want explicit orchestration — your own loop, your own error handling, your own latency budgeting — DSPy exposes two types you can wire together yourself:

- `dspy.Tool` — wrapper around a Python function the LM can be informed about.
- `dspy.ToolCalls` — the model-output type representing a list of requested tool invocations.

Requires DSPy 3.0.4b2 or later for the `ToolCall.execute()` method.

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

The Signature declares `tools: list[dspy.Tool]` as an **input** field and `outputs: dspy.ToolCalls` as the **output** field — i.e., the available toolset is passed in at call time, and the LM's job is to produce a list of tool invocations.

## `dspy.Tool` — what the wrapper exposes

The `dspy.Tool` wrapper makes regular Python functions compatible with DSPy's prompt-formatting and execution pipeline.

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

- `name` — function identifier (defaults to `__name__`).
- `desc` — docstring documentation (used by the LM to decide *when* to call).
- `args` — parameter schema derived from type hints.
- `str(tool)` — the canonical text representation the prompt includes.

### Tool-function design best practices

- Write clear, detailed docstrings — the LM uses them to pick the right tool.
- Use explicit type hints on every parameter and on the return.
- Prefer basic parameter types (`str`, `int`, `bool`, `dict`, `list`) or Pydantic models — these convert cleanly to the JSON-schema form the LM sees.

Example of a well-designed tool function:

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

## `dspy.ToolCalls` — the model-output type

`dspy.ToolCalls` represents the model's structured output when a tool-call-producing Signature is run. Each element of `response.outputs.tool_calls` carries:

- `name` — the tool identifier the LM asked to invoke.
- `args` — the keyword-argument dictionary the LM produced.

Execution options:

```python
for call in response.outputs.tool_calls:
    # Option 1: automatic discovery — looks up the function by name
    #           in the calling scope.
    result = call.execute()

    # Option 2: pass an explicit function dictionary
    result = call.execute(functions={"weather": weather, "calculator": calculator})

    # Option 3: pass a list of dspy.Tool objects
    result = call.execute(functions=[dspy.Tool(weather), dspy.Tool(calculator)])

    print(f"Result: {result}")
```

The same `call.execute(...)` API handles all three lookup modes — the framework resolves the requested `call.name` against whichever container was passed in.

## Native Tool Calling

DSPy adapters can use the underlying LM provider's **native function-calling** channel (OpenAI's tool-calls, Anthropic's tool-use, Gemini's function-calling) instead of parsing tool calls out of plain text.

Adapter defaults:

- `dspy.ChatAdapter` — `use_native_function_calling=False` (text-based parsing of tool calls).
- `dspy.JSONAdapter` — `use_native_function_calling=True` (native function-calling).

Either default can be overridden:

```python
import dspy

# ChatAdapter with native function calling enabled
chat_adapter_native = dspy.ChatAdapter(use_native_function_calling=True)

# JSONAdapter with native function calling disabled
json_adapter_manual = dspy.JSONAdapter(use_native_function_calling=False)

dspy.configure(
    lm=dspy.LM(model="openai/gpt-4o"),
    adapter=chat_adapter_native,
)
```

If the configured model does not support native function-calling, DSPy automatically falls back to text-based parsing.

## Async Tools

DSPy supports both synchronous and asynchronous tool functions.

### Using `acall` (recommended for async code)

```python
import asyncio
import dspy

async def async_weather(city: str) -> str:
    """Get weather information asynchronously."""
    await asyncio.sleep(0.1)
    return f"The weather in {city} is sunny"

tool = dspy.Tool(async_weather)

result = await tool.acall(city="New York")
print(result)
```

### Calling async tools from sync code

A context flag lets sync code transparently call an async tool — the framework runs the coroutine on an internal event loop:

```python
import asyncio
import dspy

async def async_weather(city: str) -> str:
    """Get weather information asynchronously."""
    await asyncio.sleep(0.1)
    return f"The weather in {city} is sunny"

tool = dspy.Tool(async_weather)

with dspy.context(allow_tool_async_sync_conversion=True):
    result = tool(city="New York")
    print(result)
```

## When to Use Each Approach

**Choose `dspy.ReAct` when:**

- Automatic reasoning and tool selection are desired.
- Tasks require multiple sequential tool calls.
- Built-in error recovery is beneficial.
- Focus on tool implementation over orchestration is preferred.

**Choose manual handling when:**

- Precise execution control is necessary.
- Custom error-handling logic is required.
- Latency minimization matters.
- Tools return no values (void functions).
