---
title: "DSPy Tutorial — Streaming"
type: source
tags: [dspy, tutorial, streaming, async, token-streaming, status-streaming, framework]
date: 2026-05-24
source_file: raw/dspy-streaming-tutorial.md
---

## Summary

Short, single-page [[DSPy]] tutorial at `https://dspy.ai/tutorials/streaming/` that **canonicalizes the framework's streaming surface** — a sidecar-architecture token-streaming layer that composes orthogonally over [[DSPyModules|every Module]] without changing the [[DSPyProgrammingModel|four-concerns decomposition]]. Three load-bearing items **new to the wiki corpus** with this ingest: (1) **`dspy.streamify(program, stream_listeners=[...])`** — the single wrapper that lifts any [[DSPyModules|`dspy.Module`]] from sync `__call__` to a streaming generator (async by default, sync on `async_streaming=False`); (2) **`dspy.streaming.StreamListener(signature_field_name=...)`** — the per-field listener that pulls a single `str`-typed [[DSPySignatures|Signature]] output from the LM's token side-channel, yielding `StreamResponse(predict_name, signature_field_name, chunk)` objects with `allow_reuse=True` for loop-bodied modules ([[react|`dspy.ReAct`]]) and an explicit `(predict, predict_name)` disambiguation for **duplicate field names across sub-modules**; (3) **`dspy.streaming.StatusMessageProvider`** — a six-hook subclass-and-override surface (`lm_start/end`, `module_start/end`, `tool_start/end`) that emits `StatusMessage(message=...)` objects through the **same generator** as the token chunks, so a UI consumer reads a single typed stream of `StreamResponse | Prediction | StatusMessage`. The tutorial also documents three operational subtleties: streaming is **disabled by cache hit** (only the final `Prediction` arrives when the LM call is cached); `StreamResponse` chunks are **buffered until the next field appears** (last chunk is usually multi-token because finalization is detected by field-boundary in the adapter, not by special token); and the streamed field must be of **type `str`** — non-string [[DSPySignatures|Signature]] outputs are not streamable.

## Key Claims

- **`dspy.streamify(program, stream_listeners=[...])` is the universal streaming entry.** Wraps **any** [[DSPyModules|`dspy.Module`]] — minimal [[DSPyPredict|`dspy.Predict`]], [[chainofthought|`dspy.ChainOfThought`]], [[react|`dspy.ReAct`]], custom subclasses — into a generator producing typed chunks. The wrapper is **orthogonal** to the [[DSPyProgrammingModel|four-concerns decomposition]] (Signature / Module / Adapter / Optimizer); none of the underlying artifacts need streaming-aware code. First wiki receipt of `dspy.streamify`. The framework's API symmetry with [[DSPyAsync|the async wrapping pattern]] (`acall` / `aforward`) is **not** a wrapping operation — `streamify` produces a new callable, whereas `acall` is a method on the existing callable. Two different mechanisms for two different transport shapes (single-await vs streaming-iteration).

- **Streaming is sidecar over LM tokens, not in-band.** The tutorial's structural disclosure: *"streaming is implemented in a sidecar fashion: we enable streaming on the LM so that LM outputs a stream of tokens. We send these tokens to a side channel, which is being continuously read by the user-defined listeners."* The LM is the producer; listeners are the consumers; the side channel is buffered. The [[DSPyAdapters|Adapter]] is in the loop — *"Listeners' internal mechanism changes according to the adapter behind the scene"* — because field-boundary detection depends on the adapter's wire format ([[DSPyAdapters|`ChatAdapter`]] delimiter `[[ ## field_name ## ]]` vs [[DSPyAdapters|`JSONAdapter`]] structured JSON). **First wiki receipt that the Adapter affects streaming behavior** — the [[DSPyAdapters|Adapters page]] documented only formatting/parsing, not stream segmentation.

- **`StreamResponse` is a three-field tuple uniquely identifying a streamed chunk.** `predict_name` (from `program.named_predictors()` — `'self'` when the streamed program is a leaf [[DSPyPredict|`dspy.Predict`]], otherwise the attribute name of the sub-predictor like `'predict1'` or `'predict.predict'` for a nested module); `signature_field_name` (the output field name on the [[DSPySignatures|Signature]]); `chunk` (the token string, with arbitrary chunk granularity). The `(predict_name, signature_field_name)` pair is the **unique identifier** of a stream — both halves are needed because the same `signature_field_name` can occur on multiple sub-Predicts in a composite [[DSPyModules|Module]]. This is the first wiki receipt of `named_predictors()` as the **public stream-identity surface**, not just an [[DSPyOptimizers|Optimizer]]-internal enumeration ([[DSPyModules|the Modules page]] documented it for Optimizer consumption only).

- **The streamed field must be `str`.** *"The only requirement is that the streamed field must be of type `str`"* — the [[DSPySignatures|Signature]] type system's five tiers (basic Python, typing composites, Pydantic, nested types, DSPy-special types) collapse to a single permitted streaming tier. `list[str]`, `dict[str, int]`, [[Pydantic]] models, and DSPy-special types ([[DSPyHistory|`dspy.History`]], `dspy.Image`) are **not** streamable. The constraint is structural: container/JSON outputs can only be parsed once complete; only flat string outputs admit incremental delivery. This narrows the streaming target set to user-facing prose fields (`answer`, `reasoning`, `next_thought`, free-text scenes) — exactly the fields a UI needs to render progressively.

- **`StreamResponse` chunks are buffered until field finalization.** The tutorial's structural disclosure: *"because usually we cannot decide if a field has finalized until seeing the next field, the listener buffers the output tokens before sending to the final generator, which is why you will usually see the last chunk of type `StreamResponse` has more than one token."* The listener cannot detect end-of-field on the current field's terminator alone (the [[DSPyAdapters|adapter]]-specific delimiter is the start of the *next* field); so it buffers one extra token-worth of lookahead, flushed when the next field begins. **Operational implication**: a UI rendering `chunk` by `chunk` will see a multi-token tail, not a token-by-token reveal of the final words. This is a fidelity loss the tutorial documents without apology — the alternative would be unsound finalization signals.

- **Cache hit bypasses token streaming.** *"When a cached result is found, the stream will skip individual tokens and only yield the final `Prediction`"* — the cache layer ([[DSPyLM|`dspy.LM`]]'s default-on caching, configurable via `dspy.LM(..., cache=False)` as the multi-field example shows) **does not synthesize a fake token stream** to maintain UI consistency. The generator yields the final [[DSPyPrediction|`Prediction`]] directly. **Operational implication**: a developer testing streaming with default caching will see no streaming on the second run; the multi-field example sets `cache=False` deliberately. The [[DSPyLM|LM page's]] cache-as-default discipline is the surface that creates this expectation gap.

- **`allow_reuse=True` is required for loop-bodied modules.** *"By default, a `StreamListener` automatically closes itself after completing a single streaming session. This design helps prevent performance issues, since every token is broadcast to all configured stream listeners."* The single-fire default is a performance choice (broadcast-to-every-listener has O(listeners) per-token cost); the `allow_reuse=True` opt-in unlocks streaming across *every* iteration of a [[react|`dspy.ReAct`]] think-act-observe loop. The canonical ReAct stream-target is the implicit `next_thought` field — the field [[react|`dspy.ReAct`]] adds to the user's [[DSPySignatures|Signature]] for each iteration of the trajectory. **First wiki receipt of `next_thought` as a public field name on [[react|`dspy.ReAct`]]'s expanded Signature** — the [[react|`dspy.ReAct`]] page documented `trajectory`/`reasoning`/user-fields on the returned [[DSPyPrediction|`Prediction`]] but not the per-iteration `next_thought` field.

- **Duplicate field names disambiguated by `(predict, predict_name)`.** When two sub-Predicts of a composite [[DSPyModules|Module]] both expose an `answer` field, the listener must be wired with both the `predict=` object reference and the `predict_name=` string label — otherwise the listener cannot route. This is the **first wiki receipt** of a structural limitation in the listener's auto-routing: it can find a field by name alone if the name is unique across the program, but not when collisions exist. The tutorial's example (`predict1: question->answer`, `predict2: question, answer->answer, score`) is the canonical collision pattern — two predictors with the same output field name.

- **Status streaming is the second axis, layered over the same generator.** `StatusMessageProvider` is a subclass-and-override surface: six hook methods (`lm_start_status_message` / `lm_end_status_message` / `module_start_status_message` / `module_end_status_message` / `tool_start_status_message` / `tool_end_status_message`), each returning a `str` injected into the stream as a `dspy.streaming.StatusMessage(message=...)`. The consumer routes by `isinstance(chunk, ...)` against three types: `StreamResponse` (tokens), `Prediction` (final), `StatusMessage` (status). **The status axis is decoupled from the token axis** — a program can opt into either or both. The six-hook namespace covers the three execution surfaces every DSPy program crosses: [[DSPyLM|LM]] calls, [[DSPyModules|Module]] entries/exits, [[DSPyTools|Tool]] invocations. The hook names match the three [[DSPyProgrammingModel|Programming Model]] artifacts that **do** execute (Signature is declarative; Adapter is transparent; Optimizer is compile-time — so neither has streaming hooks). **First wiki receipt of `StatusMessageProvider` and `StatusMessage` types.**

- **`async_streaming=False` flips to a sync generator.** The default is `async for` — *"By default calling a streamified DSPy program produces an async generator"* — for the same operational reason [[DSPyAsync|`acall`]] returns an awaitable: the underlying LM token stream is async-native via [[LiteLLM]]. The `async_streaming=False` opt-in produces a plain Python iterator (`for chunk in output: ...`). The choice is symmetric to [[DSPyAsync|the sync-vs-async decision rubric]] — sync for prototyping / scripts / notebook simplicity, async for high-QPS services and concurrent UIs. **First wiki receipt** of `async_streaming` as a `streamify` kwarg; reinforces [[DSPyAsync|the async-by-default direction]] of the framework's production-shaped surfaces.

- **The `predict_name` namespace is dotted for nested modules.** The status-streaming example's output shows `predict_name='predict.predict'` for the inner [[chainofthought|`dspy.ChainOfThought`]] sub-Module inside a composite `MyModule`. The `named_predictors()` enumeration walks attribute-by-attribute (`self.predict` is the [[chainofthought|`dspy.ChainOfThought`]]; its internal `.predict` attribute is the [[DSPyPredict|`dspy.Predict`]] inside CoT), so the dotted path identifies the leaf-Predict. **Operational implication for UI routing**: a listener filtering by `predict_name == 'predict'` would miss the inner field; the canonical match key is the **leaf** path. This makes the listener-side filtering brittle against [[DSPyModules|Module]]-internal restructuring — a future DSPy refactor that renames an internal attribute breaks listener filters relying on dotted paths.

## Key Quotes

> "DSPy Streaming consists of two parts: Output Token Streaming … Intermediate Status Streaming" — opening framing; the two-axis decomposition the rest of the page operationalizes.

> "DSPy's token streaming feature works with any module in your pipeline, not just the final output." — universality claim; streaming is not a final-output-only feature.

> "The only requirement is that the streamed field must be of type `str`." — the **single** structural constraint, narrowing the [[DSPySignatures|five-tier type system]] to one tier for the streaming axis.

> "streaming is implemented in a sidecar fashion: we enable streaming on the LM so that LM outputs a stream of tokens. We send these tokens to a side channel, which is being continuously read by the user-defined listeners." — the **architectural disclosure**; explains why listeners compose orthogonally to the program's structure.

> "Listeners' internal mechanism changes according to the adapter behind the scene" — the [[DSPyAdapters|Adapter]] is in the streaming loop; field-boundary detection is adapter-specific.

> "because usually we cannot decide if a field has finalized until seeing the next field, the listener buffers the output tokens before sending to the final generator, which is why you will usually see the last chunk of type `StreamResponse` has more than one token." — the **fidelity-loss disclosure**; the framework's structural reason for non-token-perfect tails.

> "When a cached result is found, the stream will skip individual tokens and only yield the final `Prediction`." — cache-bypass behavior; not a synthesized stream.

> "By default, a `StreamListener` automatically closes itself after completing a single streaming session. This design helps prevent performance issues, since every token is broadcast to all configured stream listeners, and having too many active listeners can introduce significant overhead." — performance disclosure; explains why `allow_reuse=True` is opt-in.

> "By default calling a streamified DSPy program produces an async generator. In order to get back a sync generator, you can set the flag `async_streaming=False`." — the sync/async toggle; async is the default for the same reason [[DSPyAsync|`acall`]] is — the underlying token stream is async-native.

## Code Examples

Basic token streaming on `dspy.Predict`:

```python
import os, asyncio, dspy

os.environ["OPENAI_API_KEY"] = "your_api_key"
dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

predict = dspy.Predict("question->answer")
stream_predict = dspy.streamify(
    predict,
    stream_listeners=[dspy.streaming.StreamListener(signature_field_name="answer")],
)

async def main():
    async for chunk in stream_predict(question="Why did a chicken cross the kitchen?"):
        if isinstance(chunk, dspy.streaming.StreamResponse):
            print(f"{chunk.signature_field_name}: {chunk.chunk}")
        elif isinstance(chunk, dspy.Prediction):
            print("FINAL:", chunk)

asyncio.run(main())
```

Multi-field streaming inside a composite Module — note `cache=False`:

```python
lm = dspy.LM("openai/gpt-4o-mini", cache=False)
dspy.configure(lm=lm)

class MyModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.predict1 = dspy.Predict("question->answer")
        self.predict2 = dspy.Predict("answer->simplified_answer")

    def forward(self, question, **kwargs):
        return self.predict2(answer=self.predict1(question=question))

stream_predict = dspy.streamify(
    MyModule(),
    stream_listeners=[
        dspy.streaming.StreamListener(signature_field_name="answer"),
        dspy.streaming.StreamListener(signature_field_name="simplified_answer"),
    ],
)
```

Loop-bodied module — ReAct streaming `next_thought` across every iteration:

```python
react = dspy.ReAct("question->answer", tools=[fetch_user_info, get_sports_news])
stream_react = dspy.streamify(
    react,
    stream_listeners=[
        dspy.streaming.StreamListener(signature_field_name="next_thought", allow_reuse=True),
    ],
)
```

Duplicate field names — explicit `(predict, predict_name)` disambiguation:

```python
class MyModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.predict1 = dspy.Predict("question->answer")
        self.predict2 = dspy.Predict("question, answer->answer, score")

stream_listeners = [
    dspy.streaming.StreamListener(
        signature_field_name="answer", predict=predict.predict1, predict_name="predict1"),
    dspy.streaming.StreamListener(
        signature_field_name="answer", predict=predict.predict2, predict_name="predict2"),
]
```

Status streaming — subclass `StatusMessageProvider`, override the hooks you care about:

```python
class MyStatusMessageProvider(dspy.streaming.StatusMessageProvider):
    def tool_start_status_message(self, instance, inputs):
        return f"Calling Tool {instance.name} with inputs {inputs}..."

    def tool_end_status_message(self, outputs):
        return f"Tool finished with output: {outputs}!"

stream_predict = dspy.streamify(
    program,
    stream_listeners=[dspy.streaming.StreamListener(signature_field_name="reasoning")],
    status_message_provider=MyStatusMessageProvider(),
)

# Consumer routes three types:
async for chunk in stream_predict(num=3):
    if isinstance(chunk, dspy.streaming.StreamResponse): ...
    elif isinstance(chunk, dspy.Prediction): ...
    elif isinstance(chunk, dspy.streaming.StatusMessage): ...
```

Sync streaming — `async_streaming=False`:

```python
stream_predict = dspy.streamify(
    predict,
    stream_listeners=[dspy.streaming.StreamListener(signature_field_name="answer")],
    async_streaming=False,
)
for chunk in stream_predict(question="..."):
    ...
```

## Connections

- [[DSPy]] — the framework whose streaming surface this tutorial canonicalizes.
- [[DSPyStreaming]] — **concept page minted by this ingest.** The canonical wiki anchor for the framework-wide streaming pattern (`streamify` / `StreamListener` / `StreamResponse` / `StatusMessageProvider` / `StatusMessage`). Cross-axis sibling to [[DSPyAsync]] (one wraps to a streaming generator, the other adds an awaitable entry point — same async-native substrate, different transport shape).
- [[DSPyAsync]] — `streamify` returns an async generator by default for the same operational reason [[DSPyAsync|`acall`]] returns an awaitable: [[LiteLLM]]'s token stream is async-native. The `async_streaming=False` opt-in mirrors the sync-from-async-tool conversion paths. The streaming axis **depends on** the async substrate even when the public surface is sync.
- [[DSPyModules]] — `streamify` accepts any [[DSPyModules|`dspy.Module`]]; `named_predictors()` produces the `predict_name` namespace listeners filter on. Extends [[DSPyModules|the Modules page]] in place with a streaming-routing note.
- [[DSPyPredict]] — the minimal primitive a `StreamListener` targets; when `streamify` wraps a leaf [[DSPyPredict|`dspy.Predict`]], the `predict_name` is `'self'`.
- [[DSPySignatures]] — the streamed field must be `str`-typed; the five-tier type system collapses to one tier for the streaming axis. Container, [[Pydantic]], nested, and DSPy-special types ([[DSPyHistory|`dspy.History`]], `dspy.Image`) are **not** streamable.
- [[DSPyAdapters]] — *"Listeners' internal mechanism changes according to the adapter behind the scene"*; field-boundary detection is adapter-specific. The [[DSPyAdapters|ChatAdapter]] delimiter (`[[ ## field_name ## ]]`) is the canonical stream-segmentation signal. **First wiki receipt that the Adapter is in the streaming loop.**
- [[DSPyLM]] — the LM is the streaming **producer**; default-on caching short-circuits the stream (cache hit yields only the final [[DSPyPrediction|`Prediction`]]); `dspy.LM(..., cache=False)` is the canonical workaround when testing streaming.
- [[DSPyPrediction]] — the terminal chunk on every stream; `isinstance(chunk, dspy.Prediction)` is the canonical end-of-stream signal in the consumer loop.
- [[DSPyTools]] — `tool_start_status_message` / `tool_end_status_message` hooks surface tool-call boundaries through the status stream. The status-streaming example wraps a [[DSPyTools|`dspy.Tool(lambda x: 2*x, name='double_the_number')`]] alongside a [[chainofthought|`dspy.ChainOfThought`]] sub-Module — composing the tool axis with the token axis through the same generator.
- [[react|ReAct]] — the canonical loop-bodied module for which `allow_reuse=True` was designed; the implicit `next_thought` field is the canonical per-iteration stream target. **First wiki receipt of `next_thought` as a [[react|`dspy.ReAct`]] expanded-Signature field name.**
- [[chainofthought|ChainOfThought]] — the canonical streaming target for the `reasoning` field is the CoT-injected one; the status-streaming example uses it explicitly. The nested `predict_name='predict.predict'` in the sample output is the [[chainofthought|`dspy.ChainOfThought`]]-inside-`MyModule` path.
- [[DSPyHistory]] — explicitly **not streamable** under the `str`-only constraint; `dspy.History` is a DSPy-special type with `messages: list[dict[str, Any]]`.
- [[LiteLLM]] — the upstream provider abstraction whose per-provider streaming-capable wire layer makes `streamify` work without per-provider DSPy code. The async-native substrate that `async_streaming=True` (default) and `async_streaming=False` both ride on.
- [[ServerSentEvents]] — the prevalent web-layer transport for token streaming; `streamify`'s sync/async generators are the natural Python-side feeds for SSE responses. Forward-reference for production deployment.
- [[WebSockets]] — the bidirectional alternative; status-streaming + token-streaming over the same generator maps cleanly to a WS message stream.
- [[dspy-async-tutorial]] — the sibling tutorial on the async axis; the two pages canonicalize the two production-shaping orthogonal surfaces (async transport + streaming transport). Same `dspy.LM("openai/gpt-4o-mini")` choice, same `dspy.configure(...)` bootstrapping, same composability-with-everything claim.
- [[dspy-tools]] — page 7 of 13 of [[DSPy]] *Learn*; documents `tool_*` hooks indirectly via the `dspy.Tool` instance; this tutorial gives them their first wiki-receipt status-streaming use.
- [[dspy-modules]] — page 5 of 13; documented `named_predictors()` for [[DSPyOptimizers|Optimizer]] consumption; this tutorial promotes it to the **public stream-identity surface**.
- [[dspy-adapters]] — page 6 of 13; documented [[DSPyAdapters|`ChatAdapter`]]/[[DSPyAdapters|`JSONAdapter`]] field-delimiter conventions; this tutorial discloses that the delimiter is **the signal listeners use to segment streams**.

## Contradictions

None. The tutorial **extends** every prior DSPy ingest along an orthogonal streaming axis:

- [[dspy-tools]]'s `dspy.Tool` is **promoted** here as a status-streaming target via `tool_start_status_message` / `tool_end_status_message`. The Tools-side observability surface is the status stream's tool hooks — a strict extension, not a conflict.
- [[dspy-modules]]'s `named_predictors()` enumeration — documented as the [[DSPyOptimizers|Optimizer]]-side surface for walking learnable sub-Predicts — is **promoted** to the public stream-identity namespace. No contradiction; the API was always public, only its second use case is new.
- [[dspy-adapters]]'s field-delimiter discipline (`[[ ## field_name ## ]]`) — documented as the parser's anchor — is **disclosed** here as also the listener's segmentation signal. The [[DSPyAdapters|Adapter]] is in the streaming loop in a way the Adapters page did not enumerate. No contradiction, only a structural disclosure.
- [[DSPyAsync]]'s production-shape claim (sync for prototyping, async for production) **composes** with the streaming axis: `async_streaming=True` is the default for the same reason `acall` is the production-readiness signal. **Streaming is async-native** even when surfaced as a sync iterator (the `async_streaming=False` path is a sync wrapper over the same async substrate).
- [[DSPyLM]]'s cache-as-default discipline is **load-bearing context** for understanding the cache-bypass behavior. No contradiction; the [[DSPyLM|LM page]] documented cache-as-default and this tutorial documents the streaming-specific implication.
- [[DSPyHistory]] / [[DSPySignatures]]'s five-tier type system **survives** the streaming axis: only the `str` tier is streamable. The tutorial does not contradict the five-tier framing; it narrows the streaming-eligible subset.

Three productive clarifications:

1. **Streaming and async are different mechanisms over the same async substrate.** [[DSPyAsync|`acall`]] is a *method* on the existing callable (`module.acall(...)` returns an awaitable that resolves to a single [[DSPyPrediction|`Prediction`]]); `streamify` is a *wrapper function* that produces a new callable returning a generator. They compose: a `streamify(program, async_streaming=True)` consumer uses `async for`, which is structurally async; but the underlying mechanism is different. The framework's symmetry is `async-ness-by-default for production-shaped surfaces`, not `same wrapping idiom for both`.

2. **The `str`-only streaming constraint is a fundamental structural property, not an implementation gap.** Container types ([[Pydantic]] / `list[str]` / nested) cannot stream because their parse semantics demand the whole structure; partial JSON is not interpretable. The tutorial does not promise future support; the constraint follows from typed I/O. UI designers should target free-text fields (`answer`, `reasoning`, `next_thought`, narrative outputs) for progressive rendering and accept that structured outputs render whole on stream completion.

3. **`StatusMessage` is the framework-authored observability surface, but it costs an extra type-check.** Every consumer must add a third `isinstance(chunk, dspy.streaming.StatusMessage)` branch — the third type joining `StreamResponse` and `Prediction` on the same generator. The tutorial pre-empts this in every code example. **The three-type union** (`StreamResponse | Prediction | StatusMessage`) is the canonical streaming consumer interface; an extension point for future framework-emitted types (e.g., trace events, error/retry events) is implicit but not promised.
