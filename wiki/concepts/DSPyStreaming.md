---
title: "DSPy Streaming"
type: concept
tags: [dspy, streaming, async, token-streaming, status-streaming, observability, framework]
sources: [dspy-streaming-tutorial, dspy-deployment-tutorial]
last_updated: 2026-05-24
---

# DSPy Streaming

**DSPy Streaming is the framework-wide token-and-status streaming surface of [[DSPy]] — `dspy.streamify(program, stream_listeners=[...])` to wrap any [[DSPyModules|`dspy.Module`]] into a generator, `dspy.streaming.StreamListener(signature_field_name=...)` to pull a single `str`-typed [[DSPySignatures|Signature]] output from the LM token side-channel, `dspy.streaming.StatusMessageProvider` to emit lifecycle events on the same generator.** It is **orthogonal** to the [[DSPyProgrammingModel|four-concerns decomposition]] (Signature / Module / Adapter / Optimizer) — a parallel transport layer over the same four artifacts. Sibling axis to [[DSPyAsync|async dispatch]]: both are production-shaped surfaces that ride on the same async-native [[LiteLLM]] substrate, but with different wrapping idioms (wrapper function for streaming, `acall` method for async). Canonical source: [[dspy-streaming-tutorial|the Streaming tutorial]] at `https://dspy.ai/tutorials/streaming/`.

## The two streaming axes

| Axis | Wrapper / Listener | Yielded type | Purpose |
|---|---|---|---|
| Output token streaming | `dspy.streamify(...)` + `StreamListener(signature_field_name=...)` | `dspy.streaming.StreamResponse(predict_name, signature_field_name, chunk)` | Progressive token-by-token rendering of `str`-typed output fields |
| Intermediate status streaming | `status_message_provider=` kwarg on `dspy.streamify(...)` + `StatusMessageProvider` subclass | `dspy.streaming.StatusMessage(message)` | Lifecycle observability — LM / Module / Tool start and end |
| Terminal (both axes) | (implicit) | `dspy.Prediction(...)` | The program's final structured output, last item on the stream |

Every consumer routes the same three-type union: `StreamResponse | StatusMessage | Prediction`.

## Sidecar architecture

> *"streaming is implemented in a sidecar fashion: we enable streaming on the LM so that LM outputs a stream of tokens. We send these tokens to a side channel, which is being continuously read by the user-defined listeners."* — [[dspy-streaming-tutorial]]

The [[DSPyLM|LM]] is the **producer** (token-by-token via [[LiteLLM]]'s streaming wire layer); the side channel is **buffered**; the user-declared `StreamListener` objects are the **consumers** that pull from the buffer and yield to the public generator. The program's structure ([[DSPyModules|Module]] composition, control flow inside `forward()`) is **unchanged** by streaming — `streamify` does not modify the program; it wraps it.

The [[DSPyAdapters|Adapter]] **is** in the streaming loop. Field-boundary detection — the moment a listener decides *"the field I'm watching has finalized"* — depends on the adapter's wire format: [[DSPyAdapters|`ChatAdapter`]]'s delimiter `[[ ## field_name ## ]]` is the segmentation signal; [[DSPyAdapters|`JSONAdapter`]]'s structured JSON shape is a different signal. *"Listeners' internal mechanism changes according to the adapter behind the scene."*

## `dspy.streamify` — the universal entry

`dspy.streamify(program, stream_listeners=[...], status_message_provider=None, async_streaming=True)` wraps any [[DSPyModules|`dspy.Module`]] (minimal [[DSPyPredict|`dspy.Predict`]], [[chainofthought|`dspy.ChainOfThought`]], [[react|`dspy.ReAct`]], custom subclasses) and returns a callable that yields a generator instead of a single [[DSPyPrediction|`Prediction`]]:

```python
predict = dspy.Predict("question->answer")
stream_predict = dspy.streamify(
    predict,
    stream_listeners=[dspy.streaming.StreamListener(signature_field_name="answer")],
)

async for chunk in stream_predict(question="..."):
    if isinstance(chunk, dspy.streaming.StreamResponse): ...
    elif isinstance(chunk, dspy.Prediction): ...
```

Four kwargs surface the two axes:

- `stream_listeners=[...]` — the per-field listener list. Zero listeners is legal (the program still runs; only the final `Prediction` is yielded — degraded to non-streaming).
- `status_message_provider=...` — optional `StatusMessageProvider` subclass instance for lifecycle events.
- `async_streaming=True` — the default; flip to `False` for a plain Python iterator over the same underlying async stream.

## `StreamListener` — per-field token pull

```python
dspy.streaming.StreamListener(
    signature_field_name="answer",         # required — the output field to pull
    predict=None,                          # optional — for duplicate field names
    predict_name=None,                     # optional — for duplicate field names
    allow_reuse=False,                     # opt-in for loop-bodied modules
)
```

Three structural properties:

1. **The streamed field must be `str`-typed.** The [[DSPySignatures|Signature]]'s five-tier type system (basic Python / typing composites / [[Pydantic]] / nested types / DSPy-special) collapses to one tier for streaming. `list[str]`, `dict[str, int]`, [[Pydantic]] models, [[DSPyHistory|`dspy.History`]], `dspy.Image` are **not streamable** — their parse semantics demand the complete structure.

2. **Listeners auto-close after one streaming session.** Single-fire by default for performance — every token is broadcast to every listener (O(listeners) per-token cost). `allow_reuse=True` opts into multi-fire behavior, required for streaming fields produced inside a loop ([[react|`dspy.ReAct`]]'s implicit `next_thought` field is the canonical case).

3. **Duplicate field names need explicit `(predict, predict_name)` disambiguation.** When two sub-Predicts of a composite [[DSPyModules|Module]] both expose an `answer` field, the listener cannot route by name alone. Wire both the `predict=` object reference (the sub-Predict attribute) and the `predict_name=` string label (the attribute name).

## `StreamResponse` — the chunk envelope

```python
StreamResponse(
    predict_name="self",            # from program.named_predictors() — dotted for nested
    signature_field_name="answer",  # the output field name on the Signature
    chunk="To get",                 # the token string; may be multi-token on the last chunk
)
```

The `(predict_name, signature_field_name)` pair is the **unique identifier** of the stream — both halves are needed because the same `signature_field_name` can occur on multiple sub-Predicts.

`predict_name` is derived from `program.named_predictors()`:
- Leaf [[DSPyPredict|`dspy.Predict`]] wrapped directly → `predict_name='self'`.
- Sub-Predict inside a composite — attribute name → `predict_name='predict1'`.
- Nested sub-Module's leaf Predict — dotted path → `predict_name='predict.predict'` (e.g., the [[DSPyPredict|`dspy.Predict`]] inside a [[chainofthought|`dspy.ChainOfThought`]] inside the outer `MyModule`).

Chunks are **buffered until field finalization** — the listener cannot detect end-of-field on the current token alone; it waits for the next field's delimiter. *"The last chunk of type `StreamResponse` has more than one token"* is a structural property, not a bug.

## `StatusMessageProvider` — six hooks across three execution surfaces

```python
class MyProvider(dspy.streaming.StatusMessageProvider):
    def lm_start_status_message(self, instance, inputs):     return "..."
    def lm_end_status_message(self, outputs):                return "..."
    def module_start_status_message(self, instance, inputs): return "..."
    def module_end_status_message(self, outputs):            return "..."
    def tool_start_status_message(self, instance, inputs):   return "..."
    def tool_end_status_message(self, outputs):              return "..."
```

The six-hook namespace covers the **three execution surfaces** every DSPy program crosses:

- **[[DSPyLM|LM]] calls** — `lm_start_status_message` / `lm_end_status_message`.
- **[[DSPyModules|Module]] entries / exits** — `module_start_status_message` / `module_end_status_message`.
- **[[DSPyTools|Tool]] invocations** — `tool_start_status_message` / `tool_end_status_message`.

[[DSPySignatures|Signatures]] are declarative; [[DSPyAdapters|Adapters]] are transparent; [[DSPyOptimizers|Optimizers]] run at compile time — so none of the other three [[DSPyProgrammingModel|Programming Model]] artifacts has a status hook. Each hook returns a `str` injected into the stream as `dspy.streaming.StatusMessage(message=...)`. Override only the hooks you care about; defaults are no-op (no message emitted).

## Cache hit bypasses token streaming

The default-on caching of [[DSPyLM|`dspy.LM`]] short-circuits the stream: *"When a cached result is found, the stream will skip individual tokens and only yield the final `Prediction`."* The framework does **not** synthesize a fake token stream to preserve UI consistency.

**Operational implication**: developers testing streaming with default caching see no streaming on the second run. Workaround: `dspy.LM("openai/gpt-4o-mini", cache=False)` (the [[dspy-streaming-tutorial|multi-field example]] uses this deliberately).

## Sync vs async — `async_streaming` flag

`async_streaming=True` (default) returns an **async generator**, consumed with `async for`. `async_streaming=False` returns a **plain Python iterator**, consumed with `for`. Both ride on the same async-native [[LiteLLM]] substrate; the sync mode is a wrapper that internally drives the event loop.

The async-by-default direction mirrors [[DSPyAsync|the framework's async-shaped surface]]: production deployments with concurrent UIs default to async; sync is the prototyping / script / notebook ergonomic.

## Consumer pattern — the three-type union

Every streaming consumer routes the same three types:

```python
async for chunk in stream_predict(...):
    if isinstance(chunk, dspy.streaming.StreamResponse):
        # token chunk — render progressively
        ...
    elif isinstance(chunk, dspy.streaming.StatusMessage):
        # lifecycle event — log / update UI status
        ...
    elif isinstance(chunk, dspy.Prediction):
        # terminal — the final structured output
        return_value = chunk
```

`isinstance(chunk, dspy.Prediction)` is the **end-of-stream signal**; there is no separate sentinel.

## Constraints and gaps

- **Only `str` fields stream.** Container, [[Pydantic]], nested, and DSPy-special types ([[DSPyHistory|`dspy.History`]], `dspy.Image`) are out of scope.
- **Last chunk is multi-token.** The buffered-until-next-field discipline means token-perfect tails are not achievable.
- **Cache hits stream nothing.** Test with `cache=False`.
- **`predict_name` is dotted and brittle.** Listener filters relying on dotted paths break under [[DSPyModules|Module]]-internal refactors.
- **Six hooks, no error/retry hooks.** The status surface covers LM/Module/Tool **success** boundaries; failure events are not framework-emitted (consumer must observe via try/except around `async for`).

## Cross-axis composition

Streaming composes orthogonally with every other DSPy axis:

- **[[DSPyAsync|Async]]** — `streamify` returns async by default; the streaming and async axes share the [[LiteLLM]] async-native substrate.
- **[[DSPyOptimizers|Optimizers]]** — optimization happens at compile time; the optimized program is streamable the same way the unoptimized one is.
- **[[DSPyAdapters|Adapters]]** — the adapter chooses the field-segmentation signal; switching adapter changes listener internal mechanism but not the public interface.
- **[[DSPyModules|Module]] composition** — `streamify` wraps any [[DSPyModules|Module]] regardless of internal sub-Module composition; `named_predictors()` produces the routing namespace.
- **[[react|ReAct]]** — `allow_reuse=True` + the `next_thought` field; tools surface through the status stream's tool hooks.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-streaming-tutorial]] — canonical receipt: `dspy.streamify(...)`, `StreamListener(signature_field_name=...)`, `StatusMessageProvider` six-hook surface, and the `StreamResponse | StatusMessage | Prediction` consumer union.
- [[dspy-deployment-tutorial]] — production-shape composition: `dspy.streamify(dspy.asyncify(program))` piped through `dspy.utils.streaming.streaming_response` into a [[FastAPI]] `StreamingResponse(..., media_type="text/event-stream")`.
- [[dspy-output-refinement-tutorial]] — surfaces the open question of how `dspy.streamify` interacts with [[DSPyRefine|`dspy.Refine`]] / [[DSPyBestOfN|`dspy.BestOfN`]] (per-rollout chunks vs only the selected prediction — unspecified in the tutorial).
- [[dspy-image-generation-prompting-tutorial]] — gap-acknowledging entry: the iterative image-prompt refinement loop is documented as having *"no streaming / async / observability composition"*, marking the absent `streamify` axis as a clean extension point.
- [[dspy-multihop-search-tutorial]] — long-running MIPROv2 compile + multi-hop `Hop` program where `StatusMessageProvider` lifecycle events would naturally surface per-hop progress; the tutorial flags this as a gap.
- [[dspy-rl-multihop-tutorial]] — same gap as above on the [[grpo|GRPO]]-trained variant; long RL rollouts are the prototypical workload where status messages over the streaming axis carry their weight.

## Related concepts

- [[DSPyAsync]] — sibling production-shape concept. Streaming **is** async by default; sync is a wrapper.
- [[DSPyLM]] — the streaming producer; cache discipline shapes streaming behavior.
- [[DSPyAdapters]] — in the streaming loop for field segmentation.
- [[DSPyModules]] — `named_predictors()` namespace; `streamify` accepts any Module.
- [[DSPyPredict]] — leaf streaming target; `predict_name='self'` when streamified directly.
- [[DSPySignatures]] — five-tier type system; only `str` tier streams.
- [[DSPyPrediction]] — terminal chunk; canonical end-of-stream signal.
- [[DSPyTools]] — surfaces in the status stream's tool hooks; not a streaming target (tools return structured values, not progressive tokens).
- [[chainofthought|ChainOfThought]] — canonical `reasoning` streaming target.
- [[react|ReAct]] — canonical `allow_reuse=True` use case via the implicit `next_thought` field.
- [[DSPyHistory]] — explicitly not streamable (DSPy-special type).
- [[LiteLLM]] — async-native streaming wire layer.
- [[ServerSentEvents]] / [[WebSockets]] — natural transports for the streaming generator at the web layer.

## Web-transport receipt — `dspy.utils.streaming.streaming_response`

[[dspy-deployment-tutorial|The Deployment tutorial]] **closes the forward reference** to *"natural transports for the streaming generator at the web layer"* with a concrete recipe:

```python
from dspy.utils.streaming import streaming_response
from fastapi.responses import StreamingResponse

streaming_dspy_program = dspy.streamify(dspy.asyncify(dspy.ChainOfThought("question -> answer")))

@app.post("/predict/stream")
async def stream(question: Question):
    stream = streaming_dspy_program(question=question.text)
    return StreamingResponse(streaming_response(stream), media_type="text/event-stream")
```

Two pieces of glue:

- **`dspy.utils.streaming.streaming_response(stream)`** — converts the DSPy async stream (`StreamResponse | StatusMessage | Prediction` union) into properly framed [[ServerSentEvents|SSE]] text. Hides the `data: ...\n\n` line-framing the EventSource API expects.
- **`fastapi.responses.StreamingResponse(..., media_type="text/event-stream")`** — the [[FastAPI]] side; the `text/event-stream` MIME type is the SSE protocol marker browsers and proxies route on.

Composition with [[DSPyAsync|asyncify]] is the canonical production stack: `dspy.streamify(dspy.asyncify(program))` — the asyncify wrapper handles sync programs running inside an async service; streamify produces the chunk-by-chunk generator the SSE transport consumes.
