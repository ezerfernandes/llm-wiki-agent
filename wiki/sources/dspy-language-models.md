---
title: "DSPy Learn — Language Models"
type: source
tags: [dspy, documentation, framework, llm-programming, lm-client, litellm]
date: 2026-05-17
source_file: raw/dspy-language-models.md
---

# DSPy Learn — Language Models

Page 3 of 13 in the [[DSPy]] *Learn* documentation ([dspy.ai/learn/programming/language_models/](https://dspy.ai/learn/programming/language_models/)), and the page that operationalizes [[dspy-programming-overview|the Programming Overview's]] *"swap the LM without changing the rest of your logic"* portability claim. Where the [[dspy-programming-overview|Programming Overview]] argues that the LM is one of the four orthogonal axes a DSPy program decouples from the rest of its pipeline (alongside [[DSPyAdapters|adapter]], [[DSPyModules|module]] logic, and [[DSPyOptimizers|optimization]]), this page **shows you the API**: a single class — `dspy.LM` — wraps every supported provider behind a uniform `provider/model-name` model-string convention, all calls go through [LiteLLM](https://github.com/BerriAI/litellm) under the hood, and the LM is bound to the rest of the program either globally via `dspy.configure(lm=...)` or scoped to a code block via `dspy.context(lm=...)`. Mints the [[DSPyLM]] concept page for the load-bearing **LM-client abstraction** the page introduces.

## Summary

The Language Models page is DSPy's **LM-integration manual**. It establishes the `dspy.LM(provider/model-name, api_key=...)` initializer as the framework's single client-side LM entry point, demonstrates `dspy.configure(lm=lm)` as the global-default bind and `dspy.context(lm=lm)` as the thread-safe block-local override, walks through a dozen-plus providers — [[openai|OpenAI]], [[anthropic|Anthropic]], [[gemini|Google Gemini]], Vertex AI ([[google|GCP]]), [[Databricks]], [[SGLang]] (self-hosted GPU), [[Ollama]] (local laptop), [[Anyscale]], [[TogetherAI|Together AI]], Azure, and any [[OpenAICompatibleEndpoint|OpenAI-compatible endpoint]] — all routed through [[LiteLLM]], and documents three operational concerns the abstraction exposes: **caching** (on by default, with `cache=False` and `rollout_id` for bust-able variants), **per-call config** (`config={...}` at the [[DSPyModules|Predict]] level or kwargs at the `lm()` level override init-time defaults), and **history / cost telemetry** (`lm.history` records `prompt / messages / kwargs / response / outputs / usage / cost / timestamp / uuid / model / response_model / model_type` per call). Closes with the **Responses API** opt-in (`model_type="responses"`) for [[openai|OpenAI]]-style reasoning-model surfaces.

## Key Claims

- **`dspy.LM` is the universal LM client.** Every supported provider is accessed through a single class with a single initializer signature — `dspy.LM('provider/model-name', api_key=..., **kwargs)` — so the program never imports a provider-specific SDK. The provider string is the only thing that changes when re-targeting across providers. This is what operationalizes the [[dspy-programming-overview|Programming Overview's]] *"swap the LM without changing the rest of your logic"* portability claim into a concrete two-line code change (`dspy.LM('openai/gpt-4o-mini')` → `dspy.LM('anthropic/claude-sonnet-4-5-20250929')`).

- **DSPy routes through [[LiteLLM]] for provider plumbing.** The page is explicit: *"DSPy supports dozens of LLM providers via LiteLLM."* LiteLLM is the actual SDK doing per-provider authentication, request shaping, and response parsing; DSPy's `dspy.LM` is a thin wrapper that adds caching, history, and the framework's [[DSPyAdapters|Adapter]] integration on top. The named providers are LiteLLM's, not DSPy's — Anyscale, Together AI, Azure, and the OpenAI-compatible-endpoint pattern are explicitly demonstrated with `provider/model` strings that LiteLLM resolves.

- **Two bind modes — global and block-local — both thread-safe.** `dspy.configure(lm=lm)` sets the global default; `with dspy.context(lm=other_lm): ...` overrides it inside the block. Both are explicitly documented as thread-safe. This is what makes **multi-LM programs** ergonomic — e.g. cheap LM for a planner module, expensive LM for a critic module, swapped via a `dspy.context` boundary rather than passing `lm=` through every call.

- **The provider matrix covers managed APIs, self-hosted GPU, and local laptop.** The page demonstrates three deployment regimes with concrete recipes: **managed** (OpenAI / Anthropic / Gemini / Vertex AI / Databricks / Anyscale / Together AI / Azure), **self-hosted GPU** ([[SGLang]] launched with `python -m sglang.launch_server --model-path meta-llama/Meta-Llama-3-8B-Instruct`, then accessed via the `openai/...` prefix + `api_base=http://localhost:7501/v1`), and **local laptop** ([[Ollama]] launched with `ollama run llama3.2:1b`, then accessed via `ollama_chat/llama3.2` + `api_base=http://localhost:11434`). The single-class abstraction is the same across all three.

- **OpenAI-compatible endpoints are the escape hatch.** *"If your provider offers an OpenAI-compatible endpoint, just add an `openai/` prefix to your full model name."* This is the catch-all pattern for any provider not natively in LiteLLM's registry: prefix with `openai/`, set `api_base` to the provider URL, and the rest of DSPy works unchanged. SGLang uses this pattern by design (its server is OpenAI-compatible).

- **Direct LM calls and DSPy-module calls share one LM object.** *"It's easy to call the `lm` you configured above directly."* Both `lm("Say this is a test!", temperature=0.7)` and `lm(messages=[...])` are supported, in addition to the indirect call through `dspy.ChainOfThought('question -> answer')(question=...)`. Direct calls go through the same caching / history machinery as module-mediated calls.

- **Caching is on by default; `rollout_id` busts it deterministically.** *"By default, LMs in DSPy are cached. If you repeat the same call, you will get the same outputs."* `cache=False` disables caching globally for the LM; `rollout_id=N` is part of the cache key so repeated calls with the same `(rollout_id, temperature)` are cached, but a different `rollout_id` at `temperature > 0` yields a different sample. This is the framework's solution to the **reproducibility-vs-sampling** tension — reproducible by default, deliberately bust-able when you want variance. Note: `rollout_id` support is provider-specific (OpenAI and Databricks named explicitly).

- **`lm.history` is the per-call telemetry surface.** Every `dspy.LM` instance maintains a `history` list whose entries expose `dict_keys(['prompt', 'messages', 'kwargs', 'response', 'outputs', 'usage', 'cost', 'timestamp', 'uuid', 'model', 'response_model', 'model_type'])`. This is the wire-frame for cost accounting, debugging, and downstream replay — the same hook that [[DSPyOptimizers|Optimizers]] will use later to score / replay LM calls during prompt search.

- **The Responses API is an opt-in `model_type`.** `dspy.LM("openai/gpt-5-mini", model_type="responses", ...)` routes the call through OpenAI's [Responses API](https://platform.openai.com/docs/api-reference/responses) instead of the Chat Completions API. This is the page's nod to the OpenAI reasoning-model API surface (gpt-5 / o-series) without committing the rest of DSPy to it — `model_type` is a per-LM dial, not a framework-wide one.

## Key Quotes

> "The first step in any DSPy code is to set up your language model." — opening sentence; LM-configuration is **step zero** of the [[dspy-programming-overview|Programming]] stage.

> "DSPy supports dozens of LLM providers via [LiteLLM](https://github.com/BerriAI/litellm). Just follow their instructions for whichever provider you want." — names [[LiteLLM]] as the underlying provider-abstraction layer.

> "If your provider offers an OpenAI-compatible endpoint, just add an `openai/` prefix to your full model name." — the escape-hatch pattern for any provider not natively wired.

> "You can change the default LM globally with `dspy.configure` or change it inside a block of code with `dspy.context`. Using `dspy.configure` and `dspy.context` is thread-safe." — the **two bind modes**, both thread-safe.

> "By default, LMs in DSPy are cached. If you repeat the same call, you will get the same outputs. But you can turn off caching by setting `cache=False`." — caching default + opt-out.

> "Some inference providers (like OpenAI and Databricks) allow you to use a `rollout_id` parameter to bust the cache for a particular call to obtain different outputs." — `rollout_id` as the deterministic cache-bust handle.

> "Every LM object maintains the history of its interactions, including inputs, outputs, token usage (and $$$ cost), and metadata." — `lm.history` as the per-call telemetry surface.

## Connections

- [[DSPy]] — the framework whose LM-integration story this page documents. The page is the canonical anchor for the `dspy.LM` client abstraction, the `dspy.configure` / `dspy.context` bind story, and the [[LiteLLM]]-routed provider matrix.
- [[dspy-learn-index]] — parent Learn index (page 1 of 13). Names *Language Models* as the second Programming-stage sub-topic.
- [[dspy-programming-overview]] — parent page (page 2 of 13). The *"swap the LM without changing the rest of your logic"* portability claim that this page operationalizes.
- [[DSPyLM]] — concept page minted by this ingest; captures the **LM-client abstraction** itself (the `dspy.LM` class, the `provider/model-name` convention, the `dspy.configure` / `dspy.context` bind modes, caching / `rollout_id` / `lm.history` / `model_type`).
- [[DSPyProgrammingModel]] — the *separation-of-concerns* design philosophy this page makes concrete on the LM axis. The LM is one of the four orthogonal artifacts; this page is the proof-of-concept that the LM axis is in fact swappable in two lines of code.
- [[DSPyAdapters]] — the formatting / parsing layer that sits **between** `dspy.LM` and the user's [[DSPySignatures|Signature]]. The Language Models page deliberately stays at the LM-client layer and forward-references the *Adapters* sub-page (page 6 of 13) for translation-layer detail.
- [[DSPyModules]] — [[ChainOfThought|`dspy.ChainOfThought`]] and [[DSPyPredict|`dspy.Predict`]] are both demonstrated in the page's examples as the **callers** of the configured LM.
- [[DSPyOptimizers]] — `lm.history` is the per-call telemetry surface optimizers will later use to score / replay LM calls during prompt search. Forward reference.
- [[LanguageModel]] — the underlying NLP concept (joint-probability sequence model); `dspy.LM` is the client surface over a deployed instance of an LM.
- [[LiteLLM]] — the actual provider-abstraction SDK DSPy routes through. This page's *"DSPy supports dozens of LLM providers via LiteLLM"* is the explicit dependency declaration. Entity page minted by this ingest.
- [[Ollama]] — the local-laptop LM runner the page demonstrates (`ollama_chat/llama3.2` model string + `api_base=http://localhost:11434`). Entity page minted by this ingest.
- [[SGLang]] — the self-hosted-GPU server the page recommends for accurate open models (*"To host accurate open models on your own GPU(s), we recommend SGLang"*); accessed via the OpenAI-compatible-endpoint pattern. Entity page minted by this ingest.
- [[openai|OpenAI]] — managed-provider example (`openai/gpt-4o-mini`, `openai/gpt-3.5-turbo`, `openai/gpt-5-mini`); also the source of the Responses API surface the page's final section enables.
- [[anthropic|Anthropic]] — managed-provider example (`anthropic/claude-sonnet-4-5-20250929`).
- [[gemini|Gemini]] / [[google|Google]] — managed-provider examples (`gemini/gemini-2.5-pro-preview-03-25` and `vertex_ai/gemini-2.0-flash`).
- [[Databricks]] — managed-provider example (`databricks/databricks-meta-llama-3-1-70b-instruct`); paired with [[openai|OpenAI]] as the two providers explicitly named as supporting the `rollout_id` cache-bust handle.
- [[Anyscale]] — managed-provider example (`anyscale/mistralai/Mistral-7B-Instruct-v0.1`).
- [[TogetherAI|Together AI]] — managed-provider example (`together_ai/togethercomputer/llama-2-70b-chat`). Entity page minted by this ingest.
- [[microsoft|Microsoft]] / Azure — managed-provider example (`azure/<deployment_name>` + `api_key` + `api_base` + `api_version`); Azure OpenAI is the wire used.
- [[ChainOfThought]] — the *"start simple"* module from [[dspy-programming-overview|the Programming Overview]] is also this page's demonstration module (`qa = dspy.ChainOfThought('question -> answer')`).
- [[PromptCaching]] — DSPy's default-on caching of LM calls. Forward reference; the wiki may want a generic concept page for the LM-client-side caching pattern.

## Contradictions

- **No direct factual contradictions** with existing wiki content. The page extends — rather than contradicts — the wiki's existing DSPy framing:
  - The page **confirms** [[dspy-programming-overview|the Programming Overview's]] *"swap the LM"* portability claim with a concrete two-line code change, sharpening rather than disputing it.
  - The page **introduces** [[LiteLLM]] as the actual provider-abstraction layer DSPy routes through — a useful clarification of DSPy's *substrate* that the wiki had not yet recorded but that does not conflict with prior framing.
  - The provider list demonstrates [[anthropic|Anthropic]] and [[openai|OpenAI]] as **interchangeable peers** under DSPy's API, which is the same neutral framing the wiki's existing [[anthropic|Anthropic]] and [[openai|OpenAI]] entity pages take.
- **Mild positioning tension with [[2604.25850-agentic-harness-engineering|harness engineering]].** The Language Models page is the most concrete instance of DSPy's claim that *prompt-level* concerns can be swapped without touching the surrounding program. The harness-engineering paper's counter-position — that the *load-bearing* axes are surrounding tools / middleware / memory, not the LM call itself — is unaffected by this page's content; the two arguments still operate at different layers. Recorded already on [[DSPy]] / [[DSPyProgrammingModel]] / [[dspy-programming-overview]]; no new disagreement.
