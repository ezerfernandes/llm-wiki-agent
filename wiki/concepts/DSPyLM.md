---
title: "DSPy LM"
type: concept
tags: [dspy, llm-programming, lm-client, framework]
sources: [dspy-language-models]
last_updated: 2026-05-17
---

# DSPy LM

**`dspy.LM`** is [[DSPy]]'s **universal LM-client abstraction** — a single Python class that wraps every supported provider behind one initializer signature and one set of call semantics, so that a DSPy program never imports a provider-specific SDK. The class is the concrete payoff of [[DSPyProgrammingModel|the DSPy Programming Model's]] *"separation of concerns on the LM axis"* claim: under DSPy, the LM is a **swappable artifact** with a stable interface, not a hard-wired call to `openai.chat.completions.create()` or `anthropic.messages.create()`. This concept page records the abstraction itself; [[dspy-language-models|the Language Models page]] is the canonical source.

## The class as API

A `dspy.LM` is constructed with a **`provider/model-name`** model string and a provider-appropriate authentication kwarg, and is then bound to the rest of the program through one of two **thread-safe** bind modes:

```python
import dspy

lm = dspy.LM('openai/gpt-4o-mini', api_key='YOUR_OPENAI_API_KEY')
dspy.configure(lm=lm)                       # global default

with dspy.context(lm=dspy.LM('openai/gpt-3.5-turbo')):
    ...                                     # block-local override
```

The `provider/` prefix is what selects between OpenAI vs Anthropic vs Gemini vs SGLang vs Ollama vs Anyscale vs Together AI vs Azure vs any [[OpenAICompatibleEndpoint|OpenAI-compatible endpoint]]; the rest of the program — [[DSPySignatures|Signatures]], [[DSPyModules|Modules]], [[DSPyOptimizers|Optimizers]] — never sees this distinction.

## What the abstraction wraps

[[dspy-language-models|The Language Models page]] is explicit that the per-provider plumbing under `dspy.LM` is **[[LiteLLM]]**: *"DSPy supports dozens of LLM providers via LiteLLM."* `dspy.LM` is therefore best understood as a thin facade — provider authentication, request shaping, and response parsing are LiteLLM's job; `dspy.LM` adds four DSPy-specific things on top:

| Capability | Mechanism | Purpose |
|---|---|---|
| **Caching** | On by default, `cache=False` to disable | Reproducibility; cost containment for repeated calls |
| **Cache-busting** | `rollout_id=N` (OpenAI / Databricks) | Deterministic sampling — same `(rollout_id, temperature)` is cached, different `rollout_id` at `temperature > 0` yields a different sample |
| **History / telemetry** | `lm.history[-1].keys() == {prompt, messages, kwargs, response, outputs, usage, cost, timestamp, uuid, model, response_model, model_type}` | Per-call audit, cost accounting, replay for [[DSPyOptimizers|Optimizers]] |
| **Adapter integration** | [[DSPyAdapters|Adapters]] format the [[DSPySignatures|Signature]] into the messages the LM is called with, and parse the response back into typed outputs | Closes the *typed-program ↔ string-API* gap |

## The two bind modes

[[dspy-language-models|The Language Models page]] documents exactly two ways to wire a `dspy.LM` into a program — both **thread-safe**, and both deliberately separated from the LM construction itself:

1. **Global** — `dspy.configure(lm=lm)`. Sets the framework-wide default. Every [[DSPyPredict|`dspy.Predict`]] / [[ChainOfThought|`dspy.ChainOfThought`]] / [[react|`dspy.ReAct`]] call uses this LM unless overridden.
2. **Block-local** — `with dspy.context(lm=other_lm): ...`. Overrides the global default inside the block; restores it on exit. The page demonstrates the **multi-LM pattern** with this construct — `gpt-4o-mini` as the global default, `gpt-3.5-turbo` swapped in for a specific call inside a `dspy.context` block.

This is the *coding interface* over [[DSPyProgrammingModel|the Programming Model's]] *"swap the LM without changing the rest of your logic"* portability claim: the swap is **two lines of code**, not a refactor.

## Three deployment regimes the same API spans

| Regime | Example string | Backing service |
|---|---|---|
| **Managed API** | `openai/gpt-4o-mini`, `anthropic/claude-sonnet-4-5-20250929`, `gemini/gemini-2.5-pro-preview-03-25`, `vertex_ai/gemini-2.0-flash`, `databricks/databricks-meta-llama-3-1-70b-instruct`, `anyscale/mistralai/Mistral-7B-Instruct-v0.1`, `together_ai/togethercomputer/llama-2-70b-chat`, `azure/<deployment_name>` | Cloud provider |
| **Self-hosted GPU** | `openai/meta-llama/Meta-Llama-3-8B-Instruct` + `api_base=http://localhost:7501/v1` | [[SGLang]] OpenAI-compatible server |
| **Local laptop** | `ollama_chat/llama3.2` + `api_base=http://localhost:11434` | [[Ollama]] local runtime |

The OpenAI-compatible-endpoint pattern is the **escape hatch**: any provider exposing an OpenAI-shaped HTTP surface is reachable by prefixing the model name with `openai/` and pointing `api_base` at the provider URL. SGLang relies on this by design.

## Direct and module-mediated calls share one LM

The same `lm` object answers both styles of call:

```python
lm("Say this is a test!", temperature=0.7)              # direct positional
lm(messages=[{"role": "user", "content": "..."}])       # direct messages

qa = dspy.ChainOfThought('question -> answer')          # module-mediated
qa(question="...")                                       # routes through the configured LM
```

Both paths share the same caching, history, and [[DSPyAdapters|Adapter]] machinery. This is what lets the *Programming Overview's* "start simple" advice scale — a single-`ChainOfThought` program and a hand-rolled `lm(...)` call are equivalent at the LM-client layer.

## Configuring generation

Generation parameters can be set at **construction time** as defaults, or **per-call** to override:

```python
gpt = dspy.LM('openai/gpt-4o-mini',
              temperature=0.9, max_tokens=3000, stop=None, cache=False)  # defaults

# per-call override via the lm() interface
gpt("Say this is a test!", rollout_id=1, temperature=1.0)

# per-call override via dspy.Predict's config kwarg
predict = dspy.Predict("question -> answer")
predict(question="What is 1 + 52?", config={"rollout_id": 5, "temperature": 1.0})
```

The `config={...}` channel is how generation parameters flow from a [[DSPyModules|Module]] down to the bound LM without forcing a `dspy.context` swap.

## The Responses-API escape valve

`dspy.LM(..., model_type="responses")` routes calls through OpenAI's *Responses* API instead of the *Chat Completions* API — a per-LM dial for reasoning models (gpt-5 / o-series) that expose richer reasoning / structured-output surfaces. The rest of DSPy is unchanged; only the wire protocol the LM-client layer speaks differs.

## Why this matters

- **Operationalizes the *"swap the LM"* claim.** [[dspy-programming-overview|The Programming Overview]] **asserts** the LM is a swappable axis; `dspy.LM` is the line of code that **makes it true**. The four orthogonal artifacts named on [[DSPyProgrammingModel]] are not all equally legible from the API — Signatures are visible to the user, Optimizers are invoked explicitly, Adapters are mostly hidden — but the LM axis is the **most concrete and most user-facing** swap, which is why this page lands first in the Programming-sub-stage sequence.
- **Decouples the program from the SDK.** The same DSPy program runs unchanged across a managed API, a self-hosted GPU, and a local laptop. No `if provider == 'anthropic': ...` branches; no `try: openai.... except ...:` fallbacks. The branching has been pushed down into [[LiteLLM]].
- **Caching / history are framework-level, not provider-level.** Provider SDKs do not generally offer transparent caching or unified per-call history; DSPy adds them at the `dspy.LM` layer so they survive provider swaps. This is what [[DSPyOptimizers|Optimizers]] later depend on for replay / cost-tracked search.
- **`rollout_id` is the deterministic sampling handle.** Reconciles the *reproducibility-by-default* policy with *I-do-actually-want-variance* — a problem every LM-app framework has to solve. DSPy's answer is: **make non-determinism part of the cache key**, so it stays reproducible.

## Connections

- [[DSPy]] — the framework whose LM-client surface this abstraction *is*.
- [[dspy-language-models]] — canonical source for the `dspy.LM` API surface (page 3 of 13 of DSPy *Learn*).
- [[dspy-programming-overview]] — the *"swap the LM without changing the rest of your logic"* portability claim this concept page operationalizes.
- [[DSPyProgrammingModel]] — the four-concerns decomposition that names the LM as one of the four orthogonal swappable axes.
- [[DSPyAdapters]] — the layer **between** `dspy.LM` and [[DSPySignatures|Signatures]] that translates the typed program into the messages the LM is called with. Forward reference to page 6 of 13.
- [[DSPyModules]] — [[ChainOfThought|`dspy.ChainOfThought`]] / [[DSPyPredict|`dspy.Predict`]] / [[react|`dspy.ReAct`]] are the callers of the configured LM. Forward reference to page 5 of 13.
- [[DSPyOptimizers]] — consume `lm.history` for cost-tracked replay during prompt search. Forward reference to page 13 of 13.
- [[LanguageModel]] — the underlying NLP concept; `dspy.LM` is the client surface over a deployed instance of an LM.
- [[LiteLLM]] — the actual provider-abstraction SDK `dspy.LM` routes through. The page's *"DSPy supports dozens of LLM providers via LiteLLM"* makes this an explicit upstream dependency.
- [[Ollama]] — the local-laptop deployment regime `dspy.LM` spans (`ollama_chat/llama3.2`).
- [[SGLang]] — the self-hosted-GPU deployment regime `dspy.LM` spans (OpenAI-compatible endpoint at `http://localhost:7501/v1`).
- [[openai|OpenAI]] — managed-provider example; also the source of the Responses API the `model_type="responses"` opt-in targets.
- [[anthropic|Anthropic]] / [[gemini|Gemini]] / [[Databricks]] / [[Anyscale]] / [[TogetherAI|Together AI]] — additional managed-provider examples spanned by the same API.
