# Async DSPy Programming

> Source: https://dspy.ai/tutorials/async/ — fetched 2026-05-24

DSPy has native support for asynchronous programming, allowing you to build more efficient and scalable applications. This tutorial covers how to use async functionality in DSPy, including built-in modules, tools, and custom modules.

## Why use async?

- Concurrent operations improve performance.
- Resource utilization becomes more efficient.
- I/O-bound operations experience reduced latency.
- Applications gain enhanced scalability for handling multiple simultaneous requests.

## When to use sync vs async

**Use synchronous programming when:**
- Prototyping and exploratory development.
- Doing research and experimental work.
- Developing small-to-medium applications.
- You prefer straightforward, easier-to-debug code.

**Use asynchronous programming when:**
- Deploying high-throughput services (high QPS demands).
- Working with async-only tools.
- Handling concurrent requests.
- Building production services that require significant scalability.

**Trade-offs:** complex error handling, potential for subtle bugs, more intricate code structures, and runtime environment differences between interactive notebooks (Jupyter, Colab) and standard Python environments.

## Working with async — built-in modules

All DSPy modules expose an `acall()` method that mirrors their synchronous `__call__` interface.

```python
import dspy
import asyncio
import os

os.environ["OPENAI_API_KEY"] = "your_api_key"

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))
predict = dspy.Predict("question->answer")

async def main():
    # Use acall() for async execution
    output = await predict.acall(question="why did a chicken cross the kitchen?")
    print(output)

asyncio.run(main())
```

## Working with async tools

`dspy.Tool` accepts async functions; call them with `acall()`.

```python
import asyncio
import dspy
import os

os.environ["OPENAI_API_KEY"] = "your_api_key"

async def foo(x):
    # Simulate an async operation
    await asyncio.sleep(0.1)
    print(f"I get: {x}")

tool = dspy.Tool(foo)

async def main():
    await tool.acall(x=2)

asyncio.run(main())
```

The tutorial notes that `ReAct` automatically calls its tools via their `acall()` methods, so async tools compose into the `dspy.ReAct` agent without any extra wiring.

### Calling async tools from sync code

Two options:

**1. Context manager (per-block opt-in):**

```python
with dspy.context(allow_tool_async_sync_conversion=True):
    result = tool(x=5)
```

**2. Global configuration (process-wide opt-in):**

```python
dspy.configure(allow_tool_async_sync_conversion=True)
result = tool(x=5)
```

Both forms run the coroutine on an internal event loop; the flag is off by default to avoid surprising sync code with implicit async execution.

## Writing custom async modules

Implement `aforward()` on a `dspy.Module` subclass — the async counterpart to `forward()`.

```python
import dspy
import asyncio
import os

os.environ["OPENAI_API_KEY"] = "your_api_key"
dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

class MyModule(dspy.Module):
    def __init__(self):
        self.predict1 = dspy.ChainOfThought("question->answer")
        self.predict2 = dspy.ChainOfThought("answer->simplified_answer")

    async def aforward(self, question, **kwargs):
        # Execute predictions sequentially but asynchronously
        answer = await self.predict1.acall(question=question)
        return await self.predict2.acall(answer=answer)

async def main():
    mod = MyModule()
    result = await mod.acall(question="Why did a chicken cross the kitchen?")
    print(result)

asyncio.run(main())
```

## Key API surface

- **`Module.acall(...)`** — async counterpart to `__call__`. Available on every built-in module.
- **`Module.aforward(...)`** — async counterpart to `forward()`. Defined on custom `dspy.Module` subclasses for async logic.
- **`Tool.acall(...)`** — async tool invocation; recommended for async-wrapped callables.
- **`dspy.context(allow_tool_async_sync_conversion=True)`** — per-block opt-in for sync code that needs to invoke async tools.
- **`dspy.configure(allow_tool_async_sync_conversion=True)`** — global opt-in equivalent.

## Related documentation

- [Tools — Async Tools](https://dspy.ai/learn/programming/tools/#async-tools)
- `dspy.ReAct` invokes its tools via `acall()`; see Tools page for the full async-tool surface.
