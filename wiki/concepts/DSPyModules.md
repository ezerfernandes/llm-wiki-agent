---
title: "DSPy Modules"
type: concept
tags: [dspy, llm-programming, modules, composition, prompting-technique, framework, async]
sources: [dspy-modules, dspy-programming-overview, dspy-signatures, dspy-language-models, dspy-learn-index, dspy-custom-module, dspy-ai-text-game-tutorial, dspy-sample-code-generation-tutorial, dspy-email-extraction-tutorial, dspy-async-tutorial, dspy-streaming-tutorial, dspy-saving-tutorial]
last_updated: 2026-05-24
---

# DSPy Modules

**A DSPy Module is a *building block for programs that use LMs* — a generalized prompting technique wrapped as a callable Python object with learnable parameters, parameterized over an arbitrary [[DSPySignatures|Signature]].** Modules are the third of the four orthogonal axes [[DSPyProgrammingModel|the DSPy Programming Model]] factors out of a conventional prompt (alongside [[DSPySignatures|Signatures]], [[DSPyAdapters|Adapters]], and [[DSPyOptimizers|Optimizers]]) — specifically the **swappable strategy** layer that consumes a stable Signature and decides *how* to ask the LM to produce its outputs. This concept page records the abstraction itself; [[dspy-modules|the Modules page]] (page 5 of 13 of the DSPy *Learn* documentation) is the canonical source.

## What a Module *is*

The page's opening sentence is load-bearing:

> "A DSPy module is a building block for programs that use LMs."

Four properties make it more than "a callable that takes a Signature":

1. **Generalized over signatures.** *"Each built-in module abstracts a prompting technique (like chain of thought or ReAct). Crucially, they are generalized to handle any signature."* `dspy.ChainOfThought` is not a CoT prompt — it is **the** CoT strategy, applicable to any `question -> answer`, `document -> summary`, or `context, question -> response: list[str]` Signature.

2. **Has learnable parameters.** *"A DSPy module has learnable parameters (i.e., the little pieces comprising the prompt and the LM weights) and can be invoked (called) to process inputs and return outputs."* The parameters are instructions, demonstrations (few-shot exemplars), and — for finetuning paths — LM weights. This is what [[DSPyOptimizers|Optimizers]] later tune.

3. **Composes into bigger modules.** *"Multiple modules can be composed into bigger modules (programs)."* A program *is* a Module — same class, same `forward()` contract, same `Prediction` return type.

4. **PyTorch-shaped, not LangChain-shaped.** *"DSPy modules are inspired directly by NN modules in PyTorch, but applied to LM programs."* No chain DSL, no runnable, no graph builder — just `__init__` registering sub-modules as attributes and `forward()` defining the dataflow.

## The two-step usage pattern

[[dspy-modules|The Modules page]] enforces a strict two-step usage:

1. **Declare** — pass a [[DSPySignatures|Signature]] (and optional config kwargs like `temperature=0.7`, `max_tokens`, or for [[react|`dspy.ReAct`]] a `tools=[...]` list):

   ```python
   classify = dspy.Predict('sentence -> sentiment: bool')
   classify = dspy.ChainOfThought('question -> answer', temperature=0.7)
   react    = dspy.ReAct('question -> answer: float', tools=[evaluate_math, search_wikipedia])
   ```

2. **Call** — invoke with input arguments **by name**; access output fields as attributes on the returned [[DSPyPrediction|`Prediction`]] object:

   ```python
   response = classify(sentence="it's a charming and often affecting journey.")
   print(response.sentiment)   # True
   ```

The declared Signature **survives** the choice of Module — swapping `dspy.Predict` for `dspy.ChainOfThought` does not require touching the Signature.

## The taxonomy of built-in modules

[[dspy-modules|The Modules page]] enumerates **seven** built-in modules. Five are `dspy.Module` subclasses; one is a function-style aggregator; one is a recursive-context primitive:

| Module | Strategy | Signature expansion |
|---|---|---|
| **[[DSPyPredict\|`dspy.Predict`]]** | Basic predictor. The **minimal primitive** every other module is built on top of. Stores instructions, demonstrations, and LM-weight updates. | None — identity case. |
| **[[ChainOfThought\|`dspy.ChainOfThought`]]** | *"Teaches the LM to think step-by-step before committing to the signature's response."* The wiki's existing [[ChainOfThought]] concept page covers the underlying technique; DSPy's wrapping adds the **swap-in-for-`Predict` for quality** recipe. | Adds a `reasoning` field before the output. |
| **[[DSPyProgramOfThought\|`dspy.ProgramOfThought`]]** | *"Teaches the LM to output code, whose execution results will dictate the response."* The code-execution counterpart to CoT. | Code-and-execution slots. |
| **[[react\|`dspy.ReAct`]]** | *"An agent that can use tools to implement the given signature."* Takes a `tools=[...]` kwarg of Python callables. The wiki's existing [[react|ReAct]] concept page covers the technique; DSPy's wrapping is the *typed-Signature-driven* form. | Tool-call slots. |
| **[[DSPyMultiChainComparison\|`dspy.MultiChainComparison`]]** | *"Can compare multiple outputs from `ChainOfThought` to produce a final prediction."* The N-CoT-with-aggregation pattern. | Comparison-of-outputs scaffolding. |
| **[[DSPyRecursiveLanguageModel\|`dspy.RLM`]]** | **Recursive Language Model.** *"Explores large contexts through a sandboxed Python REPL with recursive sub-LLM calls. Use when context is too large to fit in the prompt effectively."* The framework's answer to context-overflow. | Recursive sub-call orchestration. |
| **[[DSPyMajority\|`dspy.majority`]]** | Function-style. *"Can do basic voting to return the most popular response from a set of predictions."* Operates **on a set of `Prediction` objects** — does not take a Signature; not declared, only called. | N/A — aggregator, not a module. |

The taxonomy's organizing principle: **all six `dspy.Module` subclasses are wrappers over `dspy.Predict` that expand the user's [[DSPySignatures|signature]] under the hood with whatever extra fields the strategy requires.** This is the [[dspy-signatures|*modules-expand-signatures*]] mechanism from the Signatures page, **operationalized** on the Module side. The user declares `'question -> answer'`; `dspy.ChainOfThought` declares to the wire `question -> reasoning, answer`; the user never sees the intermediate field unless they ask for it.

## Composing modules into programs

DSPy's composition story is **plain Python**:

> "DSPy is just Python code that uses modules in any control flow you like, with a little magic internally at `compile` time to trace your LM calls. What this means is that, you can just call the modules freely."

The canonical multi-hop search example from [[dspy-modules|the Modules page]] is the template:

```python
class Hop(dspy.Module):
    def __init__(self, num_docs=10, num_hops=4):
        self.num_docs, self.num_hops = num_docs, num_hops
        self.generate_query = dspy.ChainOfThought('claim, notes -> query')
        self.append_notes  = dspy.ChainOfThought(
            'claim, notes, context -> new_notes: list[str], titles: list[str]'
        )

    def forward(self, claim: str) -> list[str]:
        notes, titles = [], []
        for _ in range(self.num_hops):
            query = self.generate_query(claim=claim, notes=notes).query
            context = search(query, k=self.num_docs)
            prediction = self.append_notes(claim=claim, notes=notes, context=context)
            notes.extend(prediction.new_notes)
            titles.extend(prediction.titles)
        return dspy.Prediction(notes=notes, titles=list(set(titles)))

hop = Hop()
hop(claim="Stephen Curry is the best 3 pointer shooter ever in the human history")
```

Three structural commitments:

1. **Sub-modules are `self.*` attributes.** `self.generate_query` and `self.append_notes` are how the framework later **enumerates** the program's learnable parameters (named-parameter / named-predictor walks).
2. **`forward()` is the entry point.** Calling `hop(...)` routes through `__call__` which routes through `forward(...)`. The control flow inside `forward` is arbitrary Python — loops, conditionals, recursion, retrieval calls, anything.
3. **Return is a `dspy.Prediction(...)`.** Wrapping the result this way preserves the *Module returns a typed Prediction object* contract that every built-in module honors, so the bigger module composes the same way its sub-modules do.

## Custom-module starting template

The [[dspy-custom-module|Custom Module tutorial]] supplies the **minimum-viable starting template** the [[dspy-modules|Modules *Learn* page]]'s `Hop` example generalizes:

```python
class MyProgram(dspy.Module):
    def __init__(self, ...):
        # Define attributes and sub-modules here
        ...

    def forward(self, input_name1, input_name2, ...):
        # Implement your program's logic here
        ...
```

Four positions the tutorial commits to beyond what [[dspy-modules|the Modules page]] explicitly states:

1. ***"`forward()` is unconstrained Python."*** *"You are not limited to calling only other DSPy modules; you can also integrate any standard Python functions, such as those for interacting with Langchain/Agno agents, MCP tools, database handlers, and more."*
2. ***"Call the module instance directly, not `forward()` explicitly."*** *"The `__call__` method handles necessary internal processing before executing the `forward` logic"* — `__call__` is the **trace point** for [[DSPyOptimizers|optimizer]] replay, [[MLflow]] auto-logging, [[DSPyHistory|history]] threading, and [[DSPyPrediction|`Prediction.get_lm_usage()`]] accounting.
3. ***"Custom modules unlock framework features."*** Code outside a `dspy.Module` subclass is invisible to `named_predictors()` / `named_parameters()` introspection — [[DSPyOptimizers|optimizers]] cannot tune sub-modules that are not declared as `self.*` attributes.
4. ***"DSPy is easy to migrate to and easy to migrate off."*** The framework boundary is unusually thin precisely because `forward` is plain Python.

The tutorial's worked receipt is a **non-iterative three-stage [[rag|RAG]] program** (`dspy.Predict(QueryGenerator)` → `dspy.ColBERTv2(...)` → [[chainofthought|`dspy.ChainOfThought("question,context->answer")`]]). It complements [[dspy-modules|the Modules page's]] iterative `Hop` example by covering the simpler **single-pass** composition shape; together they bracket the typical complexity range of a `dspy.Module.forward()` body.

## Parameter introspection

The page does not explicitly enumerate the introspection API, but composition makes it observable. Every `dspy.Module` subclass walks its `self.*` attributes to expose two iterables that [[DSPyOptimizers|Optimizers]] read against:

- **`named_parameters()`** — `(name, learnable_parameter)` pairs across all sub-modules transitively. Used by weight-tuning optimizers.
- **`named_predictors()`** — `(name, predictor)` pairs, where each predictor is the `dspy.Predict` instance somewhere down the tree. Used by prompt-tuning optimizers ([[BootstrapFewShot]], [[MIPROv2]], etc.) to know which prompts they may rewrite and which demonstrations they may inject.

These mirror PyTorch's `nn.Module.named_parameters()` API exactly — another instance of the *"inspired directly by NN modules in PyTorch"* commitment.

## LM-usage tracking

From DSPy **2.6.16**, every `dspy.Prediction` carries provenance for the LM calls that produced it:

```python
dspy.configure(lm=dspy.LM('openai/gpt-4o-mini', cache=False), track_usage=True)

program = MyProgram()
output  = program(question="What is the capital of France?")
print(output.get_lm_usage())
# {'openai/gpt-4o-mini': {'prompt_tokens': 260, 'completion_tokens': 61, 'total_tokens': 321, ...}}
```

Three load-bearing details:

1. **Per-model aggregation.** The return is `{provider/model: {token-counts}}` — naturally handles multi-LM programs (a `dspy.context(lm=...)` block-local swap shows up under its own key).
2. **Sub-module calls roll up.** A `MyProgram` whose `forward()` calls `self.predict1` and `self.predict2` produces **one** `get_lm_usage()` dict covering both LM calls.
3. **Cached responses don't count.** *"When using DSPy's caching features (either in-memory or on-disk via litellm), cached responses won't count toward usage statistics."* The second call to the same question with `cache=True` returns `{}`. This is the cost-accounting contract [[DSPyOptimizers|Optimizers]] read against.

## Async entry — `acall()` and `aforward()`

[[dspy-async-tutorial|The Async tutorial]] makes explicit that **every built-in Module exposes `acall()`** — the async counterpart to `__call__` — and that **custom `dspy.Module` subclasses define async logic by overriding `aforward(self, ...)`** instead of (or in addition to) `forward(self, ...)`:

```python
class MyModule(dspy.Module):
    def __init__(self):
        self.predict1 = dspy.ChainOfThought("question->answer")
        self.predict2 = dspy.ChainOfThought("answer->simplified_answer")

    async def aforward(self, question, **kwargs):
        answer = await self.predict1.acall(question=question)
        return await self.predict2.acall(answer=answer)
```

The `forward → aforward` mirror is a further lift from the [[PyTorch]] *override-the-entry-method* idiom — same `__init__` + `self.*` sub-module registration, async-suffixed verb. The `named_predictors()` / `named_parameters()` walks see `aforward`-routed programs identically to `forward`-routed ones; [[DSPyOptimizers|Optimizers]] tune both. **Async DSPy ≠ concurrent DSPy by default** — chained `await predict.acall(...)` calls run **sequentially**; users must reach for `asyncio.gather(...)` to get parallel sub-predictions. See [[DSPyAsync]] for the framework-wide pattern.

## Position in the DSPy stack

Modules sit one level **below** Signatures in the user-facing API and one level **above** Adapters in the call stack:

```
Signature        (user-written; the stable interface)
   ↓ consumed by
Module           (user-chosen strategy: Predict / ChainOfThought / ReAct / ...)
   ↓ formats via
Adapter
   ↓ calls
dspy.LM
   ↓ routes through
LiteLLM
   ↓ to
Provider         (OpenAI / Anthropic / Gemini / SGLang / Ollama / ...)
```

The Module is what **expands the Signature under the hood** — adds `reasoning` for CoT, tool-call slots for ReAct, code-and-execution slots for ProgramOfThought — without forcing the user to declare those intermediate fields.

## Why this matters

- **Operationalizes the *module-logic* concern of [[DSPyProgrammingModel|the Programming Model]].** The Programming Overview *names* the four orthogonal artifacts; this is the page that turns the third of them into a typed Python API surface. Together with [[DSPySignatures]] (page 4 of 13), it completes the user-facing API the [[DSPyProgrammingModel|Programming Model]] promises.

- **Decouples "prompting technique" from "task."** The wiki's pre-existing concept pages [[ChainOfThought]] and [[react|ReAct]] cover the **techniques** as research-paper-level ideas. DSPy's contribution is that *each technique is the same code regardless of the task* — `dspy.ChainOfThought('question -> answer')` and `dspy.ChainOfThought('claim, notes, context -> new_notes: list[str], titles: list[str]')` are the same Module class, applied to two different Signatures. The decoupling has no analog in the hand-written-prompt world.

- **Establishes the *swappable strategy* axis.** A swap from `dspy.Predict` to `dspy.ChainOfThought` to `dspy.ProgramOfThought` is **two characters of source code** (the constructor name) and does not modify the Signature, the LM, the Adapter, or the Optimizer. This is the concrete form of [[dspy-programming-overview|the Programming Overview's]] *"swap one module for another without modifying the signature"* portability claim.

- **`dspy.Predict` is the minimal primitive.** *"Internally, all other DSPy modules are built using `dspy.Predict`."* This is the wiki's first record of DSPy's claim that **every** strategy decomposes to a `Predict` plus a signature expansion — the framework has one prompting primitive, not seven. [[DSPyPredict]] is the dedicated concept page.

- **Composition is plain Python.** No DAG DSL, no chain builder, no runnable abstraction. A multi-module DSPy program is a normal `dspy.Module` subclass whose `forward()` is normal Python — loops, conditionals, retrieval calls, recursion. The framework's only compile-time intervention is **tracing** the LM calls so [[DSPyOptimizers|Optimizers]] can later replay them.

- **`track_usage=True` is the cost-accounting hook.** Per-call provenance with cache-aware aggregation is what makes [[DSPyOptimizers|Optimizer]] runs (which call modules thousands of times across the search) cost-trackable. This is a framework-level capability — [[LiteLLM]]'s cache discipline propagates through `dspy.LM` into `dspy.Prediction.get_lm_usage()`.

- **`dspy.RLM` is the framework's context-overflow primitive.** Most LLM frameworks treat long contexts as a model-side problem (longer context windows, retrieval, summarization). DSPy carries **recursion** as a first-class module — sandboxed Python REPL plus recursive sub-LLM calls — for the case where the prompt itself is too large. This complements rather than replaces retrieval (which still appears as a `search(...)` call inside `forward()`).

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-custom-module]] — **entry-point template**: canonical *"`class MyProgram(dspy.Module)` with `__init__` + `forward`"* how-to with a three-stage RAG worked receipt ([[DSPyPredict|`dspy.Predict(QueryGenerator)`]] → [[ColBERTv2|`dspy.ColBERTv2`]] → [[chainofthought|`dspy.ChainOfThought("question,context->answer")`]]); commits to the *unconstrained `forward()`* and *call-the-instance-not-`forward()`* positions.
- [[dspy-ai-text-game-tutorial]] — minimal multi-sub-module composition: three [[chainofthought|`dspy.ChainOfThought`]] sub-modules (`generate_scene`, `evaluate_action`, `generate_outcome`) under one `GameAI(dspy.Module)` with `forward()` orchestrating the interactive loop.
- [[dspy-email-extraction-tutorial]] — **diamond-shaped** four-Signature pipeline inside `EmailProcessor(dspy.Module)` (classifier → entity-extractor + action-generator; entity-extractor → summarizer + action-generator); first wiki receipt of a `dspy.Prediction(...)` constructor-style fan-in with >10 kwargs.
- [[dspy-rag-tutorial]] — three-stage RAG walk built around module *swap-without-touching-Signature*: baseline [[chainofthought|`dspy.ChainOfThought`]] → optimized → composed; lifts [[SemanticF1]] from 42% to 61.1%.
- [[dspy-customer-service-agent]] — canonical [[react|`dspy.ReAct`]] receipt: multi-tool agent over a typed airline domain; `tools=[...]` of plain Python callables auto-wrapped into `dspy.Tool` by the Module.
- [[dspy-tutorial-program-of-thought]] — [[DSPyProgramOfThought|`dspy.ProgramOfThought`]] strategy module swap from [[chainofthought|`dspy.ChainOfThought`]] (one-character constructor change) and a `MultiHopSearchWithPoT(dspy.Module)` composition mixing both.
- [[dspy-multihop-search-tutorial]] — the canonical `Hop(dspy.Module)` multi-hop retrieval example from [[dspy-modules|the Modules page]], optimized end-to-end by [[MIPROv2|`dspy.MIPROv2`]] on [[HoVer]].
- [[dspy-async-tutorial]] — `aforward(self, ...)` as the async dual of `forward`; every built-in Module exposes `acall()`; `named_predictors()` / `named_parameters()` walks see async-routed programs identically to sync.

## Connections

- [[DSPy]] — the framework whose **third** orthogonal artifact this concept *is*.
- [[dspy-modules]] — canonical source for the API surface (DSPy *Learn* page 5 of 13).
- [[DSPyProgrammingModel]] — names *module logic* as the third of four orthogonal artifacts; this concept page is the API-level definition.
- [[DSPySignatures]] — the **stable interface** every Module consumes. Pair these two concept pages — Signatures define *what* the I/O is, Modules define *how* the LM is asked to produce it.
- [[DSPyPredict]] — concept page for the minimal primitive (`dspy.Predict`); every other module is a wrapper over it.
- [[ChainOfThought]] — the wiki's existing CoT concept page; `dspy.ChainOfThought` is its DSPy implementation. **Extended in-place** on this ingest with a *DSPy implementation* section; no separate `DSPyChainOfThought` page minted.
- [[react|ReAct]] — the wiki's existing ReAct stub; `dspy.ReAct` is its DSPy implementation. **Promoted from stub** on this ingest with a *DSPy implementation* section; no separate `DSPyReAct` page minted.
- [[DSPyProgramOfThought]] — concept page for `dspy.ProgramOfThought` (output code, execute, return result).
- [[DSPyMultiChainComparison]] — concept page for `dspy.MultiChainComparison` (compare N CoT outputs).
- [[DSPyRecursiveLanguageModel]] — concept page for `dspy.RLM` (recursive sub-LLM calls in a sandboxed REPL for over-context cases).
- [[DSPyMajority]] — concept page for `dspy.majority` (the function-style voter).
- [[DSPyPrediction]] — concept page for the typed `Prediction(...)` object every Module call returns; carries the optional `reasoning` slot and the `get_lm_usage()` cost-accounting method.
- [[DSPyAdapters]] — the layer **below** Modules in the call stack; translates a Module's expanded Signature into the actual LM messages. Forward reference (page 6 of 13).
- [[DSPyTools]] — `dspy.ReAct`'s `tools=[...]` kwarg routes through the Tools sub-system. Forward reference (page 6/7 of 13).
- [[DSPyLM]] — every Module call routes through the configured `dspy.LM`. *"DSPy is just Python code…with a little magic internally at compile time to trace your LM calls"* — the LM is what gets called and traced.
- [[DSPyOptimizers]] — the consumers of Modules' learnable parameters (instructions / demonstrations / LM weights). `named_parameters()` and `named_predictors()` are the introspection surface they read against. Forward reference (page 13 of 13).
- [[PyTorch]] — DSPy modules *"are inspired directly by NN modules in PyTorch"*. The `__init__` + `forward(...)` + `named_parameters()` pattern is a direct lift.
- [[LiteLLM]] — `track_usage=True`'s cache-aware accounting inherits from LiteLLM's wire layer. Cached responses returning `{}` is the visible consequence.
- [[ColBERTv2]] — the retriever the page uses in its RAG and ReAct examples. Forward reference; named only.
- [[LanguageModel]] — the underlying NLP concept; a Module is a *prompting-technique wrapper* around an LM call.
- [[PromptEngineering]] — the discipline DSPy positions itself against. A Module *is* the prompt engineer's technique, but in a typed, swappable, optimizable form.
- [[CompositionalCapacity]] — the [[AgenticAI]] DAG framework's bounded-$C(\mathcal{G})$ regime; a `class MyProgram(dspy.Module)` is a concrete instance of the bounded compositional substrate.
- [[LLMModuloFramework]] — Modules are the *candidate-generator* layer of an LLM-Modulo system; [[DSPyMetrics|Metrics]] are the *critic* layer.
- [[2604.25850-agentic-harness-engineering]] — counter-positioning paper; its critique of "DSPy-style instruction tuning" lands at this Module / [[DSPySignatures|Signature]] / [[DSPyAdapters|Adapter]] / [[DSPyOptimizers|Optimizer]] level. Lee et al. argue the load-bearing axis is the *harness* (tools, middleware, memory), not the four prompt-level concerns DSPy names.
- [[DSPyAsync]] — `acall` / `aforward` are the async-axis duals of `__call__` / `forward`; the four-concerns decomposition is unchanged under async dispatch.
- [[dspy-async-tutorial]] — canonical source for `aforward()` as the async `forward()` and for `acall()` universality across built-in Modules.
