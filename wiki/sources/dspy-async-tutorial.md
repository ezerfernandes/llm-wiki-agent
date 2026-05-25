---
title: "DSPy Tutorial — Async Programming"
type: source
tags: [dspy, tutorial, async, asyncio, concurrency, scalability, framework]
date: 2026-05-24
source_file: raw/dspy-async-tutorial.md
---

## Summary

Short, single-page [[DSPy]] tutorial at `https://dspy.ai/tutorials/async/` that **canonicalizes the async-programming surface across the whole DSPy stack** — not just at the [[DSPyTools|Tools]] axis the [[dspy-tools|Tools page]] (page 7 of 13 of *Learn*) already documented. Three load-bearing items that are **new to the wiki corpus** with this ingest: (1) **`acall()` is universal on every built-in [[DSPyModules|Module]]** — `dspy.Predict("question->answer").acall(...)`, `dspy.ChainOfThought(...).acall(...)`, `dspy.ReAct(...).acall(...)`; (2) **`aforward()` is the async counterpart to `forward()` on custom `dspy.Module` subclasses** — the framework's mirror of [[PyTorch]]'s *override-the-forward-method* idiom, lifted into async-Python; (3) **an explicit sync-vs-async decision rubric** distinguishing *prototyping / research / small-to-medium apps / debuggability* (sync) from *high-QPS services / async-only tools / concurrent requests / production scalability* (async), with a candid trade-offs paragraph naming *complex error handling*, *potential for subtle bugs*, *intricate code structures*, and *notebook-vs-script runtime differences*. The tutorial also **re-confirms** two surfaces previously documented elsewhere in the corpus: `tool.acall(...)` (canonical async-tool form — first documented by [[dspy-tools]]) and `allow_tool_async_sync_conversion=True` configurable either per-block via `dspy.context(...)` ([[dspy-tools]]) or process-wide via `dspy.configure(...)` ([[dspy-yahoo-finance-react-tutorial]] — first receipt). **First wiki anchor for the broader [[DSPyAsync]] pattern.**

## Key Claims

- **`acall()` is the universal async entry on built-in DSPy modules.** The tutorial demonstrates `dspy.Predict("question->answer").acall(question=...)` as the canonical first example — *not* a Tools-only or [[DSPyMCP|MCP]]-only API. By extension every [[DSPyModules|built-in module]] ([[chainofthought|`dspy.ChainOfThought`]], [[react|`dspy.ReAct`]], [[DSPyProgramOfThought|`dspy.ProgramOfThought`]], [[DSPyMultiChainComparison|`dspy.MultiChainComparison`]], [[DSPyRecursiveLanguageModel|`dspy.RLM`]]) exposes `acall()` — they're all [[DSPyPredict|`dspy.Predict`]]-derived, and the async surface is inherited. This is the **first wiki receipt that `acall()` is module-wide, not tool-specific**.

- **`aforward()` is the async `forward()`.** Custom `dspy.Module` subclasses define async logic by implementing `aforward(self, ...)` instead of `forward(self, ...)`. The framework routes `__call__` to `forward()` and `acall()` to `aforward()` symmetrically — the `__init__` and the `self.*` sub-module registration are unchanged. This is the **first wiki receipt of `aforward()`**.

- **Async DSPy ≠ concurrent DSPy by default.** The custom-module example chains `await self.predict1.acall(question=question)` then `await self.predict2.acall(answer=answer)` — **sequential** execution, *"asynchronously"* in the sense that the event loop is not blocked but not in the sense that the two predictions run in parallel. The tutorial's own comment is explicit: *"Execute predictions sequentially but asynchronously"*. To get concurrent execution the user must spawn `asyncio.gather(...)` / `asyncio.create_task(...)` themselves — the framework does not implicitly parallelize independent sub-predictions inside `aforward()`. This is a non-trivial expectation gap the tutorial pre-empts in a single comment.

- **Explicit sync-vs-async decision rubric — four reasons each.** *Sync:* prototyping, research / experimental work, small-to-medium apps, debuggability preference. *Async:* high-QPS service deployment, async-only tool integration, concurrent-request handling, production scalability. The rubric is **framework-authored guidance**, not folk wisdom — DSPy's docs explicitly tell the user when sync is the right call. The four-and-four symmetry mirrors the [[dspy-tools|Tools page's]] four-and-four `dspy.ReAct`-vs-manual rubric, suggesting an authoring convention.

- **Async trade-offs are stated, not hidden.** *"Complex error handling, potential subtle bugs, intricate code structures, and runtime environment differences between interactive notebooks (Jupyter, Colab) and standard Python environments."* The notebook-runtime gotcha is the most operationally distinctive — Jupyter / Colab run their own event loops, so `asyncio.run(main())` either fails or behaves differently than in a `.py` script (`nest_asyncio` / direct `await` at the cell level work; top-level `asyncio.run` does not). The tutorial doesn't elaborate but flagging the difference is itself a kindness.

- **Two sync-from-async-tool conversion paths.** (1) `with dspy.context(allow_tool_async_sync_conversion=True): result = tool(x=5)` — per-block opt-in; appropriate when most of the code is sync and only specific call-sites need async tools. (2) `dspy.configure(allow_tool_async_sync_conversion=True); result = tool(x=5)` — process-wide opt-in; appropriate when most tools in the program are async-backed ([[LangChain]] community tools commonly are — [[dspy-yahoo-finance-react-tutorial|the Yahoo Finance tutorial]] uses this form). The tutorial is the **canonical source** documenting both forms side-by-side; the [[dspy-tools|Tools page]] only showed the context-manager form.

- **`tool.acall(...)` is the recommended async-tool invocation.** Documented in [[dspy-tools|the Tools page]] as well; re-stated here to integrate into the async-only flow. The pairing is: write `async def foo(x): ...` → wrap with `dspy.Tool(foo)` → invoke with `await tool.acall(x=2)`. The implicit recommendation is to **prefer `acall()` to relying on `allow_tool_async_sync_conversion`** when the call site is already async.

- **`ReAct` calls its tools via `acall()` automatically.** The tutorial's *Related Documentation* footer notes — re-stating [[react|`dspy.ReAct`]]'s implementation contract — that the agent automatically invokes its tools via their `acall()` methods. Two consequences: (a) async tools compose into a [[react|`dspy.ReAct`]] agent without any extra wiring; (b) [[ModelContextProtocol|MCP]]-routed tools (which require `.acall(...)` end-to-end per [[DSPyMCP]]) are first-class inside [[react|`dspy.ReAct`]] for the same reason.

## Key Quotes

> "DSPy has native support for asynchronous programming, allowing you to build more efficient and scalable applications." — opening framing; positions async as a **native** feature, not a layer.

> "All DSPy modules expose an `acall()` method that mirrors their synchronous `__call__` interface." — the universal-module claim; the wiki's prior receipts treated `acall` as a Tools-only API.

> "Execute predictions sequentially but asynchronously" — the in-code comment on the custom-module example; the **expectation-management** moment that distinguishes async DSPy from concurrent DSPy.

> "Use synchronous programming when: Prototyping and exploratory development." — first item in the framework-authored sync-vs-async rubric; sync remains the right default for most users.

> "Trade-offs: complex error handling, potential for subtle bugs, more intricate code structures, and runtime environment differences between interactive notebooks (Jupyter, Colab) and standard Python environments." — the candor moment; async is documented as a deliberate cost-benefit choice, not the One True Way.

> "`ReAct` automatically calls its tools via their `acall()` methods." — the agent-side composition guarantee; explains why no extra wiring is needed.

## Code Examples

Async predict — the minimal idiom:

```python
import dspy
import asyncio
import os

os.environ["OPENAI_API_KEY"] = "your_api_key"

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))
predict = dspy.Predict("question->answer")

async def main():
    output = await predict.acall(question="why did a chicken cross the kitchen?")
    print(output)

asyncio.run(main())
```

Async tool — the I/O-bound idiom:

```python
import asyncio
import dspy
import os

os.environ["OPENAI_API_KEY"] = "your_api_key"

async def foo(x):
    await asyncio.sleep(0.1)
    print(f"I get: {x}")

tool = dspy.Tool(foo)

async def main():
    await tool.acall(x=2)

asyncio.run(main())
```

Two sync-from-async paths — side by side:

```python
# Option 1: per-block context manager
with dspy.context(allow_tool_async_sync_conversion=True):
    result = tool(x=5)

# Option 2: process-wide configuration
dspy.configure(allow_tool_async_sync_conversion=True)
result = tool(x=5)
```

Custom async module — `aforward()` instead of `forward()`:

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
        answer = await self.predict1.acall(question=question)
        return await self.predict2.acall(answer=answer)

async def main():
    mod = MyModule()
    result = await mod.acall(question="Why did a chicken cross the kitchen?")
    print(result)

asyncio.run(main())
```

## Connections

- [[DSPy]] — the framework whose async surface this tutorial canonicalizes.
- [[DSPyAsync]] — **concept page minted by this ingest.** The canonical wiki anchor for the framework-wide async pattern (`acall` / `aforward` / async tools / sync-conversion opt-in). Cross-axis sibling to [[DSPyTools]] (which documented only the Tool-side async surface).
- [[DSPyModules]] — `acall()` is universal on every built-in [[DSPyModules|Module]]; `aforward()` is the new async entry point on custom `dspy.Module` subclasses. Extends [[DSPyModules|the Modules concept page]] in place with an async-method note rather than minting a parallel `DSPyAsyncModule` page.
- [[DSPyPredict]] — the minimal primitive `acall()` is rooted in; every other module inherits `acall` because every other module is built over [[DSPyPredict|`dspy.Predict`]].
- [[DSPyTools]] — already documented `tool.acall(...)` and the per-block `dspy.context(allow_tool_async_sync_conversion=True)`. This tutorial **adds** the process-wide `dspy.configure(...)` form to the canonical async-tools surface and re-positions both inside the broader async pattern.
- [[react|ReAct]] — `dspy.ReAct` automatically invokes its tools via `acall()`; async tools compose into the agent with no extra wiring. The tutorial's footer makes this explicit.
- [[DSPyMCP]] / [[ModelContextProtocol]] — [[DSPyMCP|MCP]]-routed tools require `.acall(...)` end-to-end and the agent invocation must live inside `async with` MCP-session blocks. This tutorial is **the async-pattern source that makes the MCP integration's async-only requirement non-corner-case** — `acall` is the framework default, not a Tools-page corner.
- [[chainofthought|ChainOfThought]] — the example custom module uses two chained `dspy.ChainOfThought` predictions, demonstrating that CoT works under `acall()` exactly like under `__call__`.
- [[DSPyLM]] — every async module call routes through the configured `dspy.LM` and through [[LiteLLM]]'s async-capable wire layer. The portability claim from [[dspy-language-models|the LM page]] survives the async axis — *swap the LM* still holds because LiteLLM exposes async dispatch uniformly.
- [[LiteLLM]] — the upstream provider abstraction whose async-capable per-provider mappings make `acall` work without per-provider DSPy code.
- [[DSPyProgrammingModel]] — the four-concerns decomposition ([[DSPySignatures|Signature]] / [[DSPyModules|Module]] / [[DSPyAdapters|Adapter]] / [[DSPyOptimizers|Optimizer]]) is **unchanged** by the async axis; `acall` / `aforward` are orthogonal additions, not a fifth concern.
- [[AsyncComputation]] — the wiki's pre-existing concept page on async dispatch in deep-learning frameworks (PyTorch / MXNet / TF). Cross-disambiguation: that page is about **GPU-frontend / C++-backend** async dispatch; *this* tutorial is about **Python `asyncio` event-loop** async dispatch for I/O-bound LM calls. Different concerns, same word.
- [[AsynchronousInference]] — the wiki's pre-existing serving-archetype concept (queue-mediated, polling-based). Cross-disambiguation: that page is about **deployment topology** (client → queue → server); *this* tutorial is about **in-process Python async** semantics. The two compose — an async-inference endpoint server is plausibly built on `dspy.Module.aforward()` — but they are distinct concepts.
- [[PyTorch]] — DSPy modules are *"inspired directly by NN modules in PyTorch"* (per [[DSPyModules]]). The `forward → aforward` mirror is a **further** lift from the PyTorch tradition: PyTorch overrides `forward()`; async DSPy overrides `aforward()` — the override-the-entry-method idiom is preserved with the async-suffix convention.
- [[dspy-tools]] — page 7 of 13 of DSPy *Learn*; the canonical source for the Tools-side async surface (`tool.acall(...)`, `dspy.context(allow_tool_async_sync_conversion=True)`). This tutorial extends that surface to **all** modules.
- [[dspy-yahoo-finance-react-tutorial]] — first wiki receipt of process-wide `dspy.configure(allow_tool_async_sync_conversion=True)`. This tutorial is the canonical source that documents the process-wide form alongside the per-block form.
- [[dspy-mcp]] — [[ModelContextProtocol|MCP]] integration receipt; MCP tools require `.acall(...)` end-to-end. This tutorial's async pattern is **the substrate** the MCP integration depends on.
- [[Asyncio]] — Python's standard-library async-IO framework. Forward reference if not yet minted; named in every code block (`import asyncio`, `asyncio.run(...)`, `asyncio.sleep(...)`).
- [[Jupyter]] / [[GoogleColab]] — named in the trade-offs paragraph as runtime-environment outliers (their own event loops). Forward references.

## Contradictions

None. The tutorial **extends** every prior DSPy ingest along an orthogonal axis:

- [[dspy-tools]]'s Tools-side async surface (`tool.acall`, `dspy.context(allow_tool_async_sync_conversion=True)`) is **promoted to module-wide**: `acall()` is on every built-in module, not only on `dspy.Tool`. The Tools page's async section is a special case of this tutorial's general pattern, not an island.
- [[dspy-modules]]'s `dspy.Module` subclass template (`__init__` + `forward(self, ...)`) is **extended** by `aforward(self, ...)` for async logic. The two methods coexist on the same class; the framework dispatches based on which entry method (`__call__` vs `acall`) was used. **No contradiction** with the [[DSPyModules|Modules concept page's]] PyTorch-shaped framing — overriding `aforward` instead of `forward` is the same override-the-entry-method idiom one suffix later.
- [[dspy-yahoo-finance-react-tutorial]]'s process-wide `dspy.configure(allow_tool_async_sync_conversion=True)` form is **canonicalized** here as one of two equal-status sync-conversion paths. The Yahoo Finance tutorial's first-receipt of the configure-time form is consistent with this tutorial's side-by-side documentation of both forms.
- [[AsyncComputation]] and [[AsynchronousInference]] are **distinct concepts** and remain so — this tutorial sits at the Python-asyncio / in-process-LM-program layer, between the GPU-backend layer ([[AsyncComputation]]) and the deployment-topology layer ([[AsynchronousInference]]). The wiki's tri-layer disambiguation is reinforced, not collapsed.

Three productive clarifications:

1. **Async DSPy is not parallel DSPy.** The custom-module example's explicit *"sequentially but asynchronously"* comment is the framework's pre-empting of the common misconception. Users who want concurrent sub-predictions inside `aforward()` must reach for `asyncio.gather(...)` themselves — DSPy does not implicitly parallelize. This is consistent with [[DSPyModules]]'s framing that *"`forward()` is unconstrained Python"*: `aforward()` is *unconstrained async Python*, including the freedom to **not** spawn concurrent tasks.

2. **The notebook-runtime gotcha is the operational subtlety.** Jupyter / Colab cells run inside an existing event loop; `asyncio.run(main())` fails or misbehaves there but succeeds in `.py` scripts. The tutorial flags this without elaboration — wiki users encountering `RuntimeError: asyncio.run() cannot be called from a running event loop` in a notebook should know the tutorial's code is for `.py` scripts, not cells. (The notebook fix is to `await main()` at the top level of a cell, or use `nest_asyncio.apply()`.)

3. **`acall` is the production-services tell.** Sync DSPy is the right call for prototyping, research, and small-to-medium apps; the moment a DSPy program is fronted by a service handling concurrent requests, the migration target is `acall` end-to-end (not `dspy.context(allow_tool_async_sync_conversion=True)` glued around sync code). The tutorial's rubric is the framework's own *production-readiness* signal — `acall` plus `aforward` are not optimization, they are the production shape.
