---
title: "DSPy Async"
type: concept
tags: [dspy, async, asyncio, concurrency, llm-programming, framework, asyncify]
sources: [dspy-async-tutorial, dspy-tools, dspy-yahoo-finance-react-tutorial, dspy-mcp, dspy-streaming-tutorial, dspy-deployment-tutorial]
last_updated: 2026-05-24
---

# DSPy Async

**DSPy Async is the framework-wide async-programming surface of [[DSPy]] — `acall()` on every built-in [[DSPyModules|Module]], `aforward()` as the async counterpart to `forward()` on custom subclasses, `tool.acall(...)` on every [[DSPyTools|`dspy.Tool`]], and a `allow_tool_async_sync_conversion` opt-in flag (per-block or process-wide) for sync code that needs to invoke async tools.** It is **orthogonal** to the [[DSPyProgrammingModel|four-concerns decomposition]] ([[DSPySignatures|Signature]] / [[DSPyModules|Module]] / [[DSPyAdapters|Adapter]] / [[DSPyOptimizers|Optimizer]]) — not a fifth concern, but a parallel async dispatch layer over the same four. Canonical source: [[dspy-async-tutorial|the Async tutorial]] at `https://dspy.ai/tutorials/async/`.

## The five async surfaces

| Surface | Sync form | Async form | First wiki receipt |
|---|---|---|---|
| Built-in module call | `module(...)` | `await module.acall(...)` | [[dspy-async-tutorial]] |
| Custom module entry | `def forward(self, ...)` | `async def aforward(self, ...)` | [[dspy-async-tutorial]] |
| Tool invocation | `tool(...)` | `await tool.acall(...)` | [[dspy-tools]] |
| Sync-from-async tools | (n/a) | `dspy.context(allow_tool_async_sync_conversion=True)` *or* `dspy.configure(allow_tool_async_sync_conversion=True)` | [[dspy-tools]] (context) / [[dspy-yahoo-finance-react-tutorial]] (configure) |
| Sync-program-to-async-callable | `program(...)` | `await dspy.asyncify(program)(...)` (thread-pool dispatch; pool size = `async_max_workers`) | [[dspy-deployment-tutorial]] |

The symmetry — `__call__ → acall`, `forward → aforward`, `tool(...) → tool.acall(...)` — is the framework's commitment to **preserving the sync API shape under the async axis**. A program migrating from sync to async changes the verb (`call` → `await acall`) but not the noun (the [[DSPySignatures|Signature]] / [[DSPyModules|Module]] / [[DSPyTools|Tool]] structure).

## `acall()` is universal on modules

[[dspy-async-tutorial|The Async tutorial]] establishes — for the first time in the wiki — that `acall()` is **not** Tools-specific. Every built-in [[DSPyModules|Module]] exposes it:

- [[DSPyPredict|`dspy.Predict`]] — `await predict.acall(question=...)`.
- [[chainofthought|`dspy.ChainOfThought`]] — `await cot.acall(...)`.
- [[react|`dspy.ReAct`]] — `await agent.acall(...)`. The agent also routes tool calls through `.acall(...)` automatically.
- [[DSPyProgramOfThought|`dspy.ProgramOfThought`]], [[DSPyMultiChainComparison|`dspy.MultiChainComparison`]], [[DSPyRecursiveLanguageModel|`dspy.RLM`]] — by extension (each is built over [[DSPyPredict|`dspy.Predict`]]).

```python
import dspy, asyncio

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))
predict = dspy.Predict("question->answer")

async def main():
    output = await predict.acall(question="why did a chicken cross the kitchen?")
    print(output)

asyncio.run(main())
```

The wiki's prior framing — implicit in [[DSPyTools|the Tools concept page]] — treated `acall` as a Tools-side feature. This is corrected: **`acall` is module-wide; tools inherit it because they're another callable.**

## `aforward()` — async logic for custom modules

Custom `dspy.Module` subclasses define async control flow by implementing `aforward(self, ...)` instead of (or in addition to) `forward(self, ...)`:

```python
class MyModule(dspy.Module):
    def __init__(self):
        self.predict1 = dspy.ChainOfThought("question->answer")
        self.predict2 = dspy.ChainOfThought("answer->simplified_answer")

    async def aforward(self, question, **kwargs):
        answer = await self.predict1.acall(question=question)
        return await self.predict2.acall(answer=answer)
```

Three structural commitments — direct lifts from the [[DSPyModules|sync `forward()` contract]]:

1. **Sub-modules are `self.*` attributes.** Same as `forward()` — the framework's `named_parameters()` / `named_predictors()` walks see them identically. [[DSPyOptimizers|Optimizers]] can still tune `aforward`-routed programs.
2. **`aforward()` is unconstrained async Python.** Loops, conditionals, retrieval calls, recursion, `asyncio.gather(...)` — anything legal in async Python.
3. **Return is a [[DSPyPrediction|`dspy.Prediction(...)`]] (or compatible).** Composability through `dspy.Prediction` is preserved.

### Async DSPy ≠ concurrent DSPy

The canonical custom-module example chains two predictions **sequentially**:

```python
answer = await self.predict1.acall(question=question)
return await self.predict2.acall(answer=answer)
```

The tutorial's own in-code comment is explicit: *"Execute predictions sequentially but asynchronously"*. The event loop is unblocked (other coroutines can run while we wait on `predict1`), but `predict2` does **not** start until `predict1` finishes. Independent sub-predictions that the user wants to run concurrently must be wrapped explicitly:

```python
async def aforward(self, q1, q2):
    a1, a2 = await asyncio.gather(
        self.predict.acall(question=q1),
        self.predict.acall(question=q2),
    )
    return dspy.Prediction(a1=a1, a2=a2)
```

DSPy **does not** implicitly parallelize. This is consistent with the [[DSPyModules|Modules page's]] framing that *"`forward()` is unconstrained Python"* — `aforward()` is unconstrained *async* Python, with the same hands-off framework discipline.

## `dspy.asyncify` — the sync-to-async wrapper for web services

`acall` / `aforward` require the program to be **natively async**. For an existing sync DSPy program that needs to ride inside an async web service ([[FastAPI]], Starlette, Litestar), the framework supplies a third surface: `dspy.asyncify(program)`.

```python
dspy_program = dspy.ChainOfThought("question -> answer")
dspy_program = dspy.asyncify(dspy_program)

# later, inside an async handler
result = await dspy_program(question=question.text)
```

Three structural properties:

1. **Thread-pool dispatch, not event-loop dispatch.** *"Currently, this runs the dspy program on a separate thread and returns its result"* ([[dspy-deployment-tutorial]]). Distinct from `acall` (pure-async, no thread pool). The asyncify wrapper exists because the inner program may have **sync I/O** the event loop cannot suspend on.
2. **Pool size is configured by `dspy.configure(async_max_workers=N)`** — default 8. Tuning knob for concurrent-request capacity. Too small → requests queue; too large → memory pressure and rate-limit thrashing against the LM provider.
3. **No program-side change required.** A sync `dspy.Module` (or any built-in module composed sync-style) is asyncified in one line. Contrast: migrating to native `acall` requires `aforward()` rewrites for custom modules.

### When to use which

| Pattern | Program shape | Dispatch | Use when |
|---|---|---|---|
| `module(...)` | sync | sync | Prototyping, notebooks, scripts |
| `await module.acall(...)` | sync internals OK; called from async | event-loop | Async-native code; the program is awaited inside other async code |
| `await dspy.asyncify(program)(...)` | sync | thread pool | Existing sync program fronted by an async web service |
| `aforward()` override | async | event-loop | Custom-module logic that itself awaits sub-modules / tools |

The [[dspy-deployment-tutorial|deployment tutorial]] uses asyncify (not `acall`) for the [[FastAPI]] worked example — chosen because the inner program is a plain `dspy.ChainOfThought(...)` (sync), and rewriting to `aforward()` would be churn relative to the one-line `asyncify` wrap.

## Async tools and the sync-conversion opt-in

[[DSPyTools|`dspy.Tool`]] accepts `async def` functions; `tool.acall(...)` is the recommended invocation form:

```python
async def async_weather(city: str) -> str:
    """Get weather information asynchronously."""
    await asyncio.sleep(0.1)
    return f"The weather in {city} is sunny"

tool = dspy.Tool(async_weather)
result = await tool.acall(city="New York")
```

For sync call-sites that need to invoke async tools, two opt-in paths:

```python
# Per-block — appropriate when most code is sync
with dspy.context(allow_tool_async_sync_conversion=True):
    result = tool(city="New York")

# Process-wide — appropriate when most tools are async-backed (e.g. LangChain community tools)
dspy.configure(allow_tool_async_sync_conversion=True)
result = tool(city="New York")
```

The flag is **off by default** — sync code that accidentally invokes an async tool would otherwise return a coroutine without surfacing the mismatch. Making the sync-from-async path explicit is a deliberate ergonomic choice. See [[DSPyTools]] for the wire-level treatment.

## When to use async — the framework's own rubric

[[dspy-async-tutorial|The tutorial]] gives four-and-four guidance:

| Choose sync when | Choose async when |
|---|---|
| Prototyping and exploratory development | Deploying high-throughput services (high QPS) |
| Research and experimental work | Working with async-only tools |
| Small-to-medium applications | Handling concurrent requests |
| Preference for debuggable code | Production services requiring scalability |

The trade-offs paragraph is explicit: *"complex error handling, potential for subtle bugs, intricate code structures, and runtime environment differences between interactive notebooks (Jupyter, Colab) and standard Python environments."* Async is documented as a **deliberate cost-benefit choice**, not the One True Way — sync remains the right default for most users.

### The notebook-runtime gotcha

Jupyter and Google Colab run their own event loops; `asyncio.run(main())` from a notebook cell either fails with *"asyncio.run() cannot be called from a running event loop"* or behaves unexpectedly. The fix inside a notebook is to `await main()` at the top of a cell, or to apply `nest_asyncio.apply()`. The tutorial's example code is written for `.py` scripts; cell-form adaptation is the user's responsibility.

## Composition with the four-concerns decomposition

The async axis is **orthogonal** to [[DSPyProgrammingModel|the Programming Model's]] four concerns:

| Concern | Sync-axis role | Async-axis role |
|---|---|---|
| **[[DSPySignatures\|Signature]]** | Declares typed I/O | **Unchanged** — the same Signature is consumed by `__call__` and `acall`. |
| **[[DSPyModules\|Module]]** | Picks the strategy via `forward()` | Picks the strategy via `aforward()`. Built-in modules expose both. |
| **[[DSPyAdapters\|Adapter]]** | Translates Signature ↔ wire format | **Unchanged** — adapters work identically under async dispatch. |
| **[[DSPyOptimizers\|Optimizer]]** | Tunes prompts / demos / weights | **Unchanged** — `named_predictors()` / `named_parameters()` work on `aforward`-routed programs. |

This is what makes async a **first-class axis** in DSPy rather than a bolt-on: the rest of the framework is untouched by the async/sync choice.

## Why this matters

- **Production-readiness signal.** [[dspy-async-tutorial|The Async tutorial's]] sync-vs-async rubric tells the user *production scalability* is the migration trigger. A DSPy program fronted by a service handling concurrent requests should run `acall` end-to-end, not glue `dspy.context(allow_tool_async_sync_conversion=True)` around sync code. The async shape is the **production shape**.
- **MCP integration is async-only.** [[ModelContextProtocol|MCP]]-routed tools require `.acall(...)` end-to-end ([[DSPyMCP]]) and live inside `async with` session blocks. This concept page is the framework-level pattern those constraints inherit from — `acall` is the framework default, not an MCP corner case.
- **`tool.acall` is not a one-off.** The [[DSPyTools|Tools page]]'s async tools section, in isolation, looked like a Tools-axis ergonomic feature. Reading it through this concept page reframes it: tool async is a special case of **module async**, which is the framework's load-bearing async-dispatch story.
- **Override-the-entry-method, async edition.** `forward → aforward` is a direct lift from the [[PyTorch]] tradition with an async suffix. Anyone fluent in PyTorch's `forward()` discipline can write DSPy async modules without learning a new API shape — same `__init__` + `self.*` sub-modules, different verb. This is the same *"inspired directly by NN modules in PyTorch"* discipline [[DSPyModules]] documents.
- **Sequential-not-concurrent is the safe default.** The framework not implicitly parallelizing sub-predictions inside `aforward` is **conservative** in the same way unconstrained-Python `forward()` is conservative — DSPy refuses to fight the user's intent. Users who want concurrency reach for `asyncio.gather(...)`; users who want serial-but-non-blocking get it for free.

## Disambiguation — what "async" doesn't mean here

The wiki has two pre-existing *async*-named concepts that are **distinct** from DSPy Async:

| Concept | Layer | Concern |
|---|---|---|
| **[[AsyncComputation]]** | Deep-learning framework | GPU-backend / Python-frontend dispatch via a task queue ([[PyTorch]] / [[MXNet]] / [[TensorFlow]]). About GPU pipeline saturation. |
| **[[AsynchronousInference]]** | Deployment topology | Client → queue → server, polling or webhook return. About cost-vs-latency trade-offs for serving. |
| **DSPyAsync** *(this page)* | LM-program runtime | Python `asyncio` event-loop dispatch over I/O-bound LM calls. About concurrent request handling inside a DSPy program. |

The three compose orthogonally. An async-inference endpoint server (deployment-topology level) can be built on `dspy.Module.aforward()` (LM-program level) running on a GPU using async backend dispatch (framework level) — all three "async"es are simultaneously true, none redundant.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-async-tutorial]] — canonical receipt: `await predict.acall(...)` on every built-in Module, the custom-module `aforward(self, ...)` override, and the four-and-four sync-vs-async rubric.
- [[dspy-mcp-tutorial]] — async-only end-to-end MCP receipt; `tool.acall(...)` on every [[FastMCP]]-backed tool inside `async with` session lifetimes, with `dspy.ReAct.acall(...)` driving the loop.
- [[dspy-streaming-tutorial]] — sibling production-shape axis; `dspy.streamify(...)` returns an async generator by default, consumed with `async for` over the same [[LiteLLM]] async-native substrate.
- [[dspy-cache-tutorial]] — `dspy.configure_cache(...)` toggles apply identically to `acall`-routed programs; the three-layer cache sits below the async dispatch boundary.
- [[dspy-image-generation-prompting-tutorial]] — async image-generation prompting loop; the worked program awaits the FAL-side Flux Pro call inside the DSPy program shape.
- [[dspy-deployment-tutorial]] — canonical `dspy.asyncify(program)` receipt for fronting a sync `dspy.ChainOfThought` with [[FastAPI]] (thread-pool dispatch, `async_max_workers=8` default).

## Connections

- [[DSPy]] — the framework whose async surface this concept *is*.
- [[dspy-async-tutorial]] — canonical source (DSPy *Learn* / Tutorials).
- [[DSPyTools]] — the Tools axis already documented `tool.acall` and the `dspy.context(allow_tool_async_sync_conversion=True)` block-form; this concept page **subsumes** that documentation into the framework-wide async pattern.
- [[DSPyModules]] — `acall()` is universal on built-in [[DSPyModules|Modules]]; `aforward()` is the custom-module async entry point. Cross-link from this concept page; the [[DSPyModules|Modules concept page]] is extended in place with the async-method note rather than minting a parallel `DSPyAsyncModule` page.
- [[DSPyPredict]] — the minimal primitive `acall` is rooted in; every Module inherits the async surface because every Module is built over [[DSPyPredict|`dspy.Predict`]].
- [[react|ReAct]] — `dspy.ReAct` invokes its tools via `acall` automatically; async tools compose into the agent with no extra wiring.
- [[DSPyMCP]] / [[ModelContextProtocol]] — [[DSPyMCP|MCP]]-routed tools require `.acall(...)` end-to-end and `async with` session lifetimes. The MCP integration's async-only requirement is **a special case** of this concept page's general pattern.
- [[chainofthought|ChainOfThought]] — used in the canonical custom-module `aforward()` example; CoT works identically under `acall`.
- [[DSPyLM]] — every async module call routes through the configured `dspy.LM` and through [[LiteLLM]]'s async-capable wire layer.
- [[LiteLLM]] — the upstream provider abstraction whose async-capable per-provider mappings make `acall` work without per-provider DSPy code.
- [[DSPyAdapters]] — the wire-format layer is **unchanged** under async dispatch; adapters serialize the same way regardless of `__call__` vs `acall` entry.
- [[DSPyOptimizers]] — `named_predictors()` / `named_parameters()` walks work on `aforward`-routed programs; the optimizer axis is untouched by the async axis. Forward reference (page 13).
- [[DSPyProgrammingModel]] — the four-concerns decomposition survives intact; async is an orthogonal dispatch layer, not a fifth concern.
- [[PyTorch]] — `forward → aforward` is a direct lift from the PyTorch override-the-entry-method idiom. Same `__init__` + `self.*` sub-module registration discipline.
- [[AsyncComputation]] — **distinct concept** (GPU-backend dispatch); cross-disambiguation link only.
- [[AsynchronousInference]] — **distinct concept** (deployment topology); cross-disambiguation link only. The two compose with DSPy Async, but they are not the same thing.
- [[dspy-tools]] — page 7 of 13 of DSPy *Learn*; the Tools-side async surface this concept subsumes.
- [[dspy-yahoo-finance-react-tutorial]] — first wiki receipt of process-wide `dspy.configure(allow_tool_async_sync_conversion=True)`.
- [[dspy-mcp]] — [[ModelContextProtocol|MCP]] integration receipt; the async-only requirement is grounded in this concept page's pattern.
- [[LangChain]] — community tools commonly async-backed; the process-wide `dspy.configure(allow_tool_async_sync_conversion=True)` form is the recommended sync-from-LangChain-tool path per [[dspy-yahoo-finance-react-tutorial|the Yahoo Finance tutorial]].
- [[dspy-deployment-tutorial]] — first wiki receipt of `dspy.asyncify(...)`, the sync-program-to-async-callable wrapper. Closes the *production-deployment shape* gap [[dspy-async-tutorial]] named but did not exercise.
- [[FastAPI]] — the canonical async web service into which `asyncify`-wrapped programs ride.
