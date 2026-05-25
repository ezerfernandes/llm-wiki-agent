---
title: "DSPy Adapters"
type: concept
tags: [dspy, llm-programming, adapters, formatting, parsing, structured-output, framework]
sources: [dspy-adapters, dspy-programming-overview, dspy-learn-index, dspy-email-extraction-tutorial, dspy-streaming-tutorial]
last_updated: 2026-05-24
---

# DSPy Adapters

**A DSPy Adapter is *"the bridge between `dspy.Predict` and the actual Language Model (LM)"*** — the formatting / parsing layer that sits between a typed [[DSPySignatures|Signature]] and the wire format the [[DSPyLM|LM]] understands. Adapters are the **third** of the four orthogonal axes [[DSPyProgrammingModel|the DSPy Programming Model]] factors out of a conventional prompt (alongside [[DSPySignatures|Signatures]], [[DSPyModules|Modules]], and [[DSPyOptimizers|Optimizers]]). This concept page records the abstraction itself; [[dspy-adapters|the Adapters page]] (page 6 of 13 of the DSPy *Learn* documentation) is the canonical source.

## What an Adapter *is*

The page's opening sentence is load-bearing:

> "Adapters function as the bridge between `dspy.Predict` and the actual Language Model (LM)."

An Adapter has **three** responsibilities the rest of DSPy cannot do generically:

1. **Convert a [[DSPySignatures|Signature]] into a system message** that defines the task.
2. **Format input data** — multi-turn messages, role assignments, demo injection, conversation history, function calls, and DSPy-special types ([[DSPyTools|`Tool`]], `dspy.Image`, `dspy.History`) — into the LM's request shape.
3. **Parse LM responses** into structured [[DSPyPrediction|`dspy.Prediction`]] instances.

Two introspection hooks make the Adapter visible to the user:

- `adapter.format(signature, demos, inputs)` returns the full multi-turn message list the LM is about to be called with.
- `adapter.format_system_message(signature)` returns only the system message a Signature produces.

The Adapter is the **single funnel** through which every DSPy-typed value crosses into the LM's wire format — [[DSPyTools|Tools]], multi-modal `dspy.Image` inputs, conversational `dspy.History`, [[Pydantic|pydantic]] model outputs, and `typing` composites all flow through the same `format()` / `parse()` pair.

## The six-step processing flow

The page enumerates the end-to-end call sequence:

1. User invokes a [[DSPyModules|DSPy module]] with inputs.
2. Inner [[DSPyPredict|`dspy.Predict`]] calls `Adapter.format()`.
3. Adapter converts signature, inputs, and demonstrations into multi-turn messages.
4. Language model generates response.
5. `Adapter.parse()` transforms the response into structured outputs.
6. Caller receives parsed results.

This is the layer the Programming Overview's *"formats the inputs in certain ways and requests outputs in a form it can parse accurately"* concern names; the page is its API-level operationalization.

## Configuration: global and block-local

Adapters are bound to the rest of the program through **two thread-safe channels**, mirroring the [[DSPyLM|LM]] bind modes:

```python
import dspy

# Global default
dspy.configure(adapter=dspy.ChatAdapter())

# Block-local override
with dspy.context(adapter=dspy.JSONAdapter()):
    ...
```

When no adapter is specified, DSPy defaults to **`ChatAdapter`**. The configuration channel is deliberately separated from `dspy.LM` construction — the same LM can be paired with different adapters without recreating the client.

## Built-in adapters

The framework ships **four** built-in adapters; the *Learn* page covers two in depth and names two in passing:

| Adapter | Wire format | Compatibility | Best for |
|---|---|---|---|
| **`dspy.ChatAdapter`** (default) | Field delimiters `[[ ## field_name ## ]]` in plain text; JSON schemas inlined in system instructions for non-primitive types; automatic `JSONAdapter` fallback on parse failure | **Universal** — *"Works with all language models."* | Small / open-source models; mixed-provider portability; any model that lacks `response_format` |
| **`dspy.JSONAdapter`** | Native LM `response_format` parameter; LM returns a JSON object containing every output field | Models supporting the `response_format` parameter (frontier OpenAI / Anthropic / Gemini; **not** small open-source models) | Latency-sensitive paths; native-structured-output models |
| **`dspy.XMLAdapter`** | XML-formatted I/O (API-reference only on the *Learn* page; no worked example) | Models that parse / emit XML cleanly | Specialized XML-document workflows |
| **`dspy.TwoStepAdapter`** | Two-step extract-then-format workflow (API-reference only on the *Learn* page; no worked example) | Reasoning-then-formatting pipelines | When extraction and formatting want to be decoupled within one Module call |

The page works `ChatAdapter` and `JSONAdapter` end-to-end on the **same** [[DSPySignatures|Signature]] (`NewsQA` with a `list[pydantic.BaseModel]` output); the only delta between the two example runs is the `adapter=` kwarg. This is the page's most explicit *swap-the-adapter-without-touching-the-signature* demonstration — the concrete payoff of [[DSPyProgrammingModel|the Programming Model's]] separation-of-concerns claim at the Adapter axis.

### `ChatAdapter` — the universal-compatibility default

`ChatAdapter`'s mechanism is **textual field delimiters**: each input and output field is wrapped in a `[[ ## field_name ## ]]` marker on both the input side (the LM sees inputs in delimiter form) and the output side (the LM is asked to emit fields in the same delimiter form). For non-primitive types (pydantic models, `list[...]`, `dict[...]`), the JSON schema is inlined into the system instructions so the LM knows the expected structure.

Two properties are non-obvious:

- **Automatic `JSONAdapter` fallback.** If `ChatAdapter`'s delimiter-based parse fails, the framework **automatically** retries through `JSONAdapter`. The *"universal compatibility"* property is therefore partly upheld by an automatic recovery mechanism, not solely by the delimiter encoding.
- **Verbosity trade-off.** The delimiters and inlined JSON schemas inflate the output token count compared to `JSONAdapter`'s response-format path. The page records the trade-off as *"more boilerplate output tokens compared to other adapters."*

### `JSONAdapter` — the native-structured-output channel

`JSONAdapter` formats inputs the same way `ChatAdapter` does, but requests the LM emit a single JSON object whose keys are the [[DSPySignatures|Signature's]] output field names. The mechanism is the LM provider's native `response_format` parameter (OpenAI's structured output, Anthropic's tool-call schema, Gemini's JSON mode) plumbed through [[LiteLLM]].

Two properties scope `JSONAdapter`'s applicability:

- **Latency advantage.** *"Minimal boilerplate in the LM response results in faster responses."* No delimiter framing in the output means fewer generated tokens.
- **Model-capability gate.** *"Requires models supporting the `response_format` parameter; incompatible with smaller open-source models lacking this capability."* This is the **first explicit model-capability scoping** in the DSPy *Learn* corpus — `dspy.LM`'s *"swap the LM"* portability is not unconditional at the wire-format layer.

## Worked example: same Signature, two adapters

The page demonstrates `NewsQA` — a [[DSPySignatures|Signature]] with a `list[ScienceNews]` output where `ScienceNews` is a `pydantic.BaseModel` — under both adapters:

```python
import dspy
import pydantic


class ScienceNews(pydantic.BaseModel):
    text: str
    scientists_involved: list[str]


class NewsQA(dspy.Signature):
    """Get news about the given science field"""

    science_field: str = dspy.InputField()
    year: int = dspy.InputField()
    num_of_outputs: int = dspy.InputField()
    news: list[ScienceNews] = dspy.OutputField(desc="science news")


# Run under ChatAdapter
dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"), adapter=dspy.ChatAdapter())
predict = dspy.Predict(NewsQA)
predict(science_field="Computer Theory", year=2022, num_of_outputs=1)
dspy.inspect_history()

# Run under JSONAdapter — same Signature, same Module, same LM
dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"), adapter=dspy.JSONAdapter())
predict(science_field="Computer Theory", year=2022, num_of_outputs=1)
dspy.inspect_history()
```

`dspy.inspect_history()` shows the wire-format delta between the two runs: `ChatAdapter` produces a delimiter-framed text response with the JSON schema in the system message; `JSONAdapter` produces a single JSON object in the response body via the LM's native structured-output channel. The [[DSPySignatures|Signature]], the [[DSPyModules|Module]] (`dspy.Predict`), and the [[DSPyLM|LM]] are **unchanged** — only the wire format differs.

## Custom adapters

The page is explicit that custom adapter development is supported — users can subclass the framework's `Adapter` base class and override `format()` / `parse()` to implement specialized wire formats. The page does not work a custom-adapter example.

## Position in the DSPy stack

The Adapter sits **below** the [[DSPyModules|Module]] and **above** the [[DSPyLM|LM]] in the call stack:

```
Signature (user-written, typed I/O contract)
   ↓ consumed by
Module (dspy.Predict / dspy.ChainOfThought / dspy.ReAct / …)
   ↓ delegates wire-format to
Adapter (dspy.ChatAdapter / dspy.JSONAdapter / dspy.XMLAdapter / dspy.TwoStepAdapter / custom)
   ↓ calls
dspy.LM (provider/model-name)
   ↓ routes through
LiteLLM
   ↓ to
Provider (OpenAI / Anthropic / Gemini / SGLang / Ollama / …)
```

Each step below the [[DSPySignatures|Signature]] is **swappable without touching the Signature**. The Adapter axis is the **third** independent swap dimension after Module and LM — and unlike those two, it's mostly invisible to user code (the default `ChatAdapter` handles most cases). The Adapter is therefore the *least user-facing* of the four orthogonal artifacts, even though it's the one that does the actual *prompt-engineering work* the rest of the framework abstracts over.

## Why this matters

- **Operationalizes the *adapter* concern of [[DSPyProgrammingModel|the Programming Model]].** The Programming Overview *names* the four orthogonal artifacts in the abstract; this is the page that turns the third of them into a typed Python API surface. The Adapter is the **single concrete layer** where prompt-engineering decisions (delimiter choice, JSON schema injection, response-format usage) live in DSPy — every other artifact treats wire format as a black box.
- **Closes the *typed-program ↔ string-API* gap.** A [[DSPySignatures|Signature]] is a typed Python object; an LM accepts strings or messages. The Adapter is what makes the round trip possible — formatting the typed Signature + demos + inputs into messages on the way in, parsing the textual response back into a typed `Prediction` on the way out. Without the Adapter, the rest of the four-concerns decomposition collapses.
- **Names the *first explicit model-capability boundary*.** `JSONAdapter`'s `response_format` requirement is the first place in the [[dspy-learn-index|Learn corpus]] where the *"swap the LM"* portability is scoped to a specific model capability. The Adapter axis is therefore where the wiki's *DSPy is LM-agnostic* claim acquires its first qualification.
- **`Tool` / `Image` / `History` conversion lives here, not in the Module.** A small but consequential implementation detail: the page lists *"Converting DSPy types (`Tool`, `Image`, etc.) into prompt messages"* as an Adapter responsibility. This means the [[DSPyTools|Tools]] artifact (page 7) and the multi-modal `dspy.Image` primitive (introduced on [[dspy-signatures]]) **compose through the Adapter** — not through a separate sub-system inside `dspy.ReAct` or `dspy.Predict`. The Adapter is the single funnel through which every DSPy-typed value crosses into the LM's wire format.
- **`ChatAdapter`'s `JSONAdapter` fallback is a hidden recovery mechanism.** The default-adapter's *"universal compatibility"* claim is partly upheld by an automatic retry path — not purely by the delimiter encoding. This sharpens the wiki's reading of DSPy's robustness story: failures at the Adapter layer are partly *fungible across formats*.
- **Adapter swaps are syntactically minimal.** The page's `NewsQA` example shows that swapping from `ChatAdapter` to `JSONAdapter` is a **one-kwarg edit** to `dspy.configure(...)`; the Signature, the Module, the LM, and the call site are unchanged. This is the third concrete *"swap N, leave M unchanged"* receipt in the wiki (after [[DSPyLM|`dspy.LM`]]'s LM-swap and [[DSPyModules|`dspy.Module`]]'s strategy-swap).

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-observability-tutorial]] — `dspy.inspect_history()` surfaces the exact messages the Adapter produced; the entry-level way to *see* what `ChatAdapter` is emitting on the wire.
- [[dspy-conversation-history]] — `dspy.History` is one of the DSPy-special types the Adapter knows how to fold into multi-turn messages; receipt of the Adapter's *special-type conversion* responsibility.
- [[dspy-image-generation-prompting-tutorial]] — `dspy.Image` inputs / outputs flow through the Adapter's `format()` path; receipt of *multi-modal types convert through the Adapter, not the Module*.
- [[dspy-customer-service-agent]] — `dspy.Tool` objects from a `dspy.ReAct` are serialized into the prompt by the Adapter; canonical *Tool conversion lives in the Adapter* receipt.
- [[dspy-streaming-tutorial]] — `StreamListener`s key on Adapter-emitted field delimiters (`[[ ## field_name ## ]]`); the streaming layer is *only* possible because the Adapter framing is deterministic.
- [[dspy-mcp-tutorial]] — MCP `dspy.Tool` wrappers cross into the LM's wire format through the same Adapter funnel; extends the Tool-conversion property to externally-defined tools.
- [[dspy-async-tutorial]] — receipt that `Adapter.format()` / `Adapter.parse()` are async-aware; the four-concerns decomposition survives the async surface unchanged.
- [[dspy-deployment-tutorial]] — production-serving regime where `dspy.JSONAdapter`'s `response_format`-native path becomes the latency-sensitive choice; receipt of the *Adapter swap as a one-kwarg edit* in a deployed program.

## Connections

- [[DSPy]] — the framework whose third orthogonal artifact this concept *is*.
- [[dspy-adapters]] — canonical source for the API surface (DSPy *Learn* page 6 of 13).
- [[dspy-programming-overview]] — names the *adapter* concern in the abstract as one of the four orthogonal artifacts a conventional prompt entangles; this concept page is the concrete definition that concern points at.
- [[dspy-learn-index]] — parent Learn index page; lists *Adapters* as the fourth Programming-stage sub-topic.
- [[DSPyProgrammingModel]] — the *separation-of-concerns* design philosophy. The Adapter is the third of the four orthogonal artifacts; this concept page is its API-level definition.
- [[DSPySignatures]] — the **upstream** artifact the Adapter consumes. A Signature is the typed contract; the Adapter is the layer that translates that contract into the LM's wire format and back. The Signature is *what*; the Adapter is *how on the wire*.
- [[DSPyLM]] — the **downstream** artifact the Adapter calls into. The Adapter formats the Signature into messages the configured `dspy.LM` sends, then parses the LM response before the [[DSPyPrediction|`Prediction`]] is returned.
- [[DSPyModules]] — every Module's call chain runs through `Adapter.format()` → `dspy.LM` → `Adapter.parse()`. The Module decides *what* to ask the LM; the Adapter decides *how* to encode the ask.
- [[DSPyPredict]] — the inner-most caller of `Adapter.format()` / `Adapter.parse()`; the page's three-task list is framed from `dspy.Predict`'s perspective.
- [[DSPyPrediction]] — the typed output `Adapter.parse()` produces.
- [[DSPyTools]] — Tools are one of the special types the Adapter converts into prompt messages. Forward reference (page 7 of 13).
- [[DSPyOptimizers]] — Optimizers tune the *prompts* the Adapter produces (instructions / demonstrations); the Adapter is therefore the layer Optimizer-tuned content actually reaches the LM through. Forward reference (page 13 of 13).
- [[LiteLLM]] — the provider-abstraction layer the `response_format` parameter `JSONAdapter` depends on is plumbed through.
- [[Pydantic]] — the page's `NewsQA` worked example uses a `pydantic.BaseModel` as the element type of a `list[...]` output; the Adapter is responsible for emitting the JSON schema (`ChatAdapter`) or invoking the LM's `response_format` (`JSONAdapter`).
- [[LanguageModel]] — the underlying NLP concept; the Adapter is the wire-format-side of the program-↔-LM interface.
- [[PromptEngineering]] — the discipline DSPy positions itself against. The Adapter is the **only** DSPy artifact that contains explicit prompt-engineering decisions (delimiter choice, schema injection, response-format usage); the rest of the framework treats wire format as a black box delegated to the Adapter.
- [[StructuredOutput]] — the broader LM-engineering concept `JSONAdapter` operationalizes. Forward reference.
