---
title: "DSPy Learn — Modules"
type: source
tags: [dspy, llm-programming, modules, composition, prompting-technique]
date: 2026-05-17
source_file: raw/dspy-modules.md
---

## Summary

**Page 5 of 13** of the [[DSPy]] *Learn* documentation. **Defines** the second of the four orthogonal artifacts [[DSPyProgrammingModel|the Programming Model]] factors out of a conventional prompt — the **Module**: *"a building block for programs that use LMs"*, where *"each built-in module abstracts a prompting technique"* and the same module is *"generalized to handle any signature."* The page enumerates the seven built-in modules ([[DSPyPredict|`dspy.Predict`]], `dspy.ChainOfThought`, `dspy.ProgramOfThought`, `dspy.ReAct`, `dspy.MultiChainComparison`, `dspy.RLM`, plus the function-style `dspy.majority`), demonstrates **composing** modules into bigger programs via `class MyProgram(dspy.Module)` with `__init__` + `forward`, and documents the [[DSPyVersion|2.6.16+]] `track_usage=True` / `prediction.get_lm_usage()` telemetry surface. Pairs directly with [[dspy-signatures]] — Signatures are the *stable interface*, Modules are the *swappable strategy* that consumes that interface and decides what extra fields (e.g. `reasoning`) to inject under the hood.

## Key Claims

- **A Module is a generalized prompting technique.** *"Each built-in module abstracts a prompting technique (like chain of thought or ReAct). Crucially, they are generalized to handle any signature."* This is the page's load-bearing definitional move — chain-of-thought, ReAct, and program-of-thought are not three different prompts but **one strategy each**, parameterized over an arbitrary [[DSPySignatures|Signature]].

- **Modules have learnable parameters.** *"A DSPy module has learnable parameters (i.e., the little pieces comprising the prompt and the LM weights) and can be invoked (called) to process inputs and return outputs."* The parameters are what [[DSPyOptimizers|Optimizers]] later tune — instructions, demonstrations, and (for finetuning optimizers) LM weights. This is what makes a Module *more than a function*.

- **`dspy.Predict` is the minimal primitive.** *"Internally, all other DSPy modules are built using `dspy.Predict`."* Every other module is a wrapper over `dspy.Predict` that **expands the user's [[DSPySignatures|signature]] under the hood** with whatever extra fields the strategy requires (`reasoning` for CoT, code-and-execution slots for ProgramOfThought, tool-call slots for ReAct). The page operationalizes this on its `'sentence -> sentiment: bool'` example.

- **Two-step usage pattern.** *"To use a module, we first **declare** it by giving it a signature. Then we **call** the module with the input arguments, and extract the output fields."* Declaration takes the Signature + per-instance config kwargs (`temperature=0.7`, `max_tokens`, etc.); the call takes the input arguments by name; the returned `Prediction(...)` object exposes the output fields as attributes.

- **`dspy.ChainOfThought` injects a `reasoning` field.** *"The `dspy.ChainOfThought` module will generally inject a `reasoning` before the output field(s) of your signature."* This concretizes the *modules-expand-signatures* mechanism that [[dspy-signatures|the Signatures page]] introduced: a user-declared `'question -> answer'` Signature returns a `Prediction` object with both `response.reasoning` and `response.answer`. The user never declared `reasoning`.

- **`dspy.Predict` is recommended as a swap-in upgrade.** *"In many cases, simply swapping `dspy.ChainOfThought` in place of `dspy.Predict` improves quality."* This is the empirical force behind [[dspy-programming-overview|the Programming Overview's]] *"start simple, then grow"* discipline at the Module-swap level.

- **Seven built-in modules, one taxonomy.** The page enumerates the full built-in module list:

  | Module | Strategy | Adds to signature |
  |---|---|---|
  | **`dspy.Predict`** | Basic predictor. Stores instructions + demonstrations + LM-weight updates. | Nothing — the identity case. |
  | **`dspy.ChainOfThought`** | *"Teaches the LM to think step-by-step before committing to the signature's response."* | `reasoning` field before the output. |
  | **`dspy.ProgramOfThought`** | *"Teaches the LM to output code, whose execution results will dictate the response."* | Code-and-execution slots. |
  | **`dspy.ReAct`** | *"An agent that can use tools to implement the given signature."* | Tool-call slots; takes `tools=[...]` kwarg. |
  | **`dspy.MultiChainComparison`** | *"Compare multiple outputs from `ChainOfThought` to produce a final prediction."* | Comparison-of-outputs scaffolding. |
  | **`dspy.RLM`** | **Recursive Language Model.** *"Explores large contexts through a sandboxed Python REPL with recursive sub-LLM calls. Use when context is too large to fit in the prompt effectively."* | Recursive sub-call orchestration. |
  | **`dspy.majority`** | Function-style. *"Can do basic voting to return the most popular response from a set of predictions."* | Not a module — operates on a set of `Prediction` objects. |

- **Composition is plain Python.** *"DSPy is just Python code that uses modules in any control flow you like, with a little magic internally at `compile` time to trace your LM calls. What this means is that, you can just call the modules freely."* There is no framework-specific DAG construct; a multi-module program is a `dspy.Module` subclass whose `__init__` instantiates sub-modules and whose `forward(...)` calls them. The framework's compile-time trace is the only piece of magic.

- **Composition pattern: `class MyProgram(dspy.Module)`.** The canonical multi-hop search example:

  ```python
  class Hop(dspy.Module):
      def __init__(self, num_docs=10, num_hops=4):
          self.num_docs, self.num_hops = num_docs, num_hops
          self.generate_query = dspy.ChainOfThought('claim, notes -> query')
          self.append_notes  = dspy.ChainOfThought('claim, notes, context -> new_notes: list[str], titles: list[str]')

      def forward(self, claim: str) -> list[str]:
          notes, titles = [], []
          for _ in range(self.num_hops):
              query = self.generate_query(claim=claim, notes=notes).query
              context = search(query, k=self.num_docs)
              prediction = self.append_notes(claim=claim, notes=notes, context=context)
              notes.extend(prediction.new_notes)
              titles.extend(prediction.titles)
          return dspy.Prediction(notes=notes, titles=list(set(titles)))
  ```

  Three structural commitments: sub-modules live as attributes on `self` (so the framework can later enumerate them), `forward(...)` is the entry point invoked via `__call__`, and the return value is a `dspy.Prediction(...)` so downstream callers get the same `Prediction` ergonomics any built-in module returns.

- **Five canonical worked examples.** The page works through five problem domains using only built-in modules: **math** (`dspy.ChainOfThought('question -> answer: float')`), **RAG** (`dspy.ChainOfThought('context, question -> response')` over a ColBERTv2 retriever), **classification** with `Literal[...]` (`class Classify(dspy.Signature)`), **information extraction** (one-line `'text -> title, headings: list[str], entities_and_metadata: list[dict[str, str]]'`), and **agents** (`dspy.ReAct("question -> answer: float", tools=[evaluate_math, search_wikipedia])`). Each is a sharper reading of *"modules are generalized over any signature."*

- **LM-usage tracking is framework-level.** From DSPy 2.6.16, `dspy.configure(track_usage=True)` plus `prediction.get_lm_usage()` returns a `{provider/model: {prompt_tokens, completion_tokens, total_tokens, ...details}}` dict aggregating **every LM call** the program made, including sub-module calls inside `forward()`. **Cached responses do not count** — *"When using DSPy's caching features (either in-memory or on-disk via litellm), cached responses won't count toward usage statistics"* — so a second call to the same `question="What is the capital of Zambia?"` returns `{}`. This is the cost-accounting hook [[DSPyOptimizers|Optimizers]] read against.

## Key Quotes

> "A DSPy module is a building block for programs that use LMs." — opening definition

> "Each built-in module abstracts a prompting technique (like chain of thought or ReAct). Crucially, they are generalized to handle any signature." — the page's load-bearing decoupling claim

> "DSPy modules are inspired directly by NN modules in PyTorch, but applied to LM programs." — the page's framing of the abstraction's lineage

> "Internally, all other DSPy modules are built using `dspy.Predict`." — `dspy.Predict` as the minimal primitive

> "In many cases, simply swapping `dspy.ChainOfThought` in place of `dspy.Predict` improves quality." — the empirical content of the *start-simple-then-grow* discipline at the module-swap level

> "The `dspy.ChainOfThought` module will generally inject a `reasoning` before the output field(s) of your signature." — the modules-expand-signatures mechanism, concretized

> "DSPy is just Python code that uses modules in any control flow you like, with a little magic internally at `compile` time to trace your LM calls." — composition is plain Python

## Connections

- [[DSPy]] — the framework whose **second** orthogonal artifact this page defines. Page 5 of 13 of *Learn*.
- [[DSPyModules]] — **concept page minted by this ingest.** The canonical wiki anchor for the Module abstraction; **resolves the long-standing forward reference** carried by [[DSPy]] / [[DSPyProgrammingModel]] / [[DSPySignatures]] / [[DSPyLM]] / [[dspy-learn-index]] / [[dspy-programming-overview]] / [[dspy-language-models]].
- [[DSPyPredict]] — concept page minted by this ingest for `dspy.Predict`, the minimal primitive every other module is built on top of.
- [[DSPyProgrammingModel]] — names *module logic* as the third of four orthogonal artifacts; this page is the API-level definition.
- [[DSPySignatures]] — Signatures are the **stable interface**; Modules are the **swappable strategy**. The two pages pair directly — Signatures define *what* a module's I/O is, Modules define *how* a Signature gets implemented.
- [[DSPyLM]] — every module call routes through the configured `dspy.LM`; the page's worked examples assume an LM already bound via `dspy.configure(...)`.
- [[ChainOfThought]] — `dspy.ChainOfThought` is the page's most-used module. **In-place extension** on this ingest adds a *DSPy implementation* section recording the *"adds a `reasoning` field"* behavior and the *swap-in-for-`Predict`* recommendation; no separate `DSPyChainOfThought` page minted.
- [[react|ReAct]] — `dspy.ReAct` is the page's agent example. **In-place extension** on this ingest promotes the stub to a full concept page with a *DSPy implementation* section.
- [[DSPyProgramOfThought]] — concept page minted by this ingest. `dspy.ProgramOfThought` is the *output-code-then-execute* strategy; named on the page but with no worked example.
- [[DSPyMultiChainComparison]] — concept page minted by this ingest. The *compare-N-CoT-outputs* aggregator.
- [[DSPyRecursiveLanguageModel]] — concept page minted by this ingest. `dspy.RLM` — the **Recursive Language Model** strategy for contexts that don't fit in the prompt; uses a sandboxed Python REPL with recursive sub-LLM calls.
- [[DSPyMajority]] — concept page minted by this ingest. The function-style `dspy.majority(...)` voter; the page's only non-`dspy.Module` building block.
- [[DSPyPrediction]] — concept page minted by this ingest. The typed return-object every Module call produces, with attribute access for each output field, the optional `reasoning` slot, and the `get_lm_usage()` cost-accounting method.
- [[DSPyOptimizers]] — the consumers of a Module's *learnable parameters* (instructions / demonstrations / LM weights). Forward reference (page 13 of 13).
- [[DSPyTools]] — `dspy.ReAct`'s `tools=[...]` kwarg is the entry point for the Tools sub-system. Forward reference (page 6 of 13).
- [[PyTorch]] — the page's explicit precedent: *"DSPy modules are inspired directly by NN modules in PyTorch."*
- [[ColBERTv2]] — the retriever used in the page's RAG and ReAct examples (`dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')`). Forward reference; named only.
- [[LiteLLM]] — *"When using DSPy's caching features (either in-memory or on-disk via litellm), cached responses won't count toward usage statistics."* The `track_usage` plumbing inherits its cache-aware accounting from LiteLLM's wire layer.

## Contradictions

None. The page **extends** rather than contradicts every prior DSPy ingest:

- [[dspy-signatures]] showed *modules expand signatures under the hood*; this page is the **module-side** of that contract — listing exactly which modules add what.
- [[dspy-programming-overview]] named *module logic* as one of four concerns; this page **defines** the artifact that concern points at.
- [[dspy-language-models]] showed the LM is swappable; this page shows the *strategy* is **also** swappable — and both swaps leave the Signature unchanged.

Three productive **clarifications** of prior ambient framing:

1. **Modules are PyTorch-shaped, not LangChain-shaped.** The page is explicit that DSPy modules are *"inspired directly by NN modules in PyTorch"* — typed `__init__` + `forward(...)` + sub-module-as-attribute, **not** a chain / runnable / graph DSL. This sharpens the wiki's framework-comparison vocabulary.

2. **`dspy.Predict` ≠ no-op.** Every prior page used `dspy.Predict` as the minimal module without making explicit that *it stores instructions, demonstrations, and LM-weight updates*. The Modules page makes that learnable-parameter store concrete — and is why `dspy.Predict` is a meaningful module to optimize, not just a thin LM wrapper.

3. **`dspy.majority` is a function, not a module.** The page singles this out — *"We also have some function-style modules"* — but operationally `dspy.majority` operates on a set of `Prediction` objects rather than being declared with a Signature and called with inputs. Worth flagging because it does not fit the *Signature → Module → Prediction* shape the rest of the page establishes.
