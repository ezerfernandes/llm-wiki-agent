---
title: "DSPy Tutorial — Building AI Applications by Customizing DSPy Modules"
type: source
tags: [dspy, tutorial, modules, custom-module, rag, colbert, mlflow]
date: 2026-05-22
source_file: raw/dspy-custom-module.md
---

## Summary

The [[DSPy]] **Building AI Applications by Customizing DSPy Modules** tutorial ([dspy.ai/tutorials/custom_module](https://dspy.ai/tutorials/custom_module/)) is the canonical **how-to** for writing a custom `class MyProgram(dspy.Module)` — the same composition pattern [[dspy-modules|the Modules *Learn* page]] showcases via `Hop`, restated here for the user who wants the **minimum-viable starting template** for any [[DSPy]] [[GenerativeAI|GenAI]] application. The tutorial commits to four positions: (1) **subclass `dspy.Module` and implement `__init__` + `forward`** — the two-method contract that mirrors PyTorch's `nn.Module`; (2) **`forward()` is unconstrained Python** — *"you are not limited to calling only other DSPy modules"* — any function call (Langchain agents, Agno agents, MCP tools, database handlers, REST clients) composes inside it; (3) **call the module instance directly, not `forward()`** — *"the `__call__` method handles necessary internal processing before executing the `forward` logic"*; (4) **building as a custom module unlocks framework features** — [[DSPyOptimizers|DSPy Optimizer]] introspection and [[MLflow]] DSPy tracing both walk the `self.*` sub-module attributes set in `__init__`. The worked receipt is a **three-stage [[rag|RAG]]** program (`QueryGenerator` [[DSPySignatures|Signature]] → `dspy.ColBERTv2` Wikipedia retrieval → [[chainofthought|`dspy.ChainOfThought`]] answer synthesis) — the wiki's first end-to-end RAG code listing inside a [[DSPyModules|`dspy.Module`]] subclass, and the canonical anchor for the public **[[ColBERTv2|`http://20.102.90.50:2017/wiki17_abstracts`]]** ColBERTv2 endpoint that the [[dspy-modules|Modules page]] and [[react|ReAct]] / [[hotpotqa|HotPotQA]] examples all assume but never document.

This tutorial is the **third wiki-corpus [[DSPy]] tutorial** (after [[dspy-conversation-history]] and [[dspy-customer-service-agent]]) and the **first** to anchor on the custom-`dspy.Module` subclass shape itself rather than on a downstream application (chatbot, agent). It fills the **template-vs-receipt** gap on rung 2 of the DSPy application stack — every prior wiki-corpus reference to "your custom `dspy.Module`" pointed at [[dspy-modules|the Modules *Learn* page]] which framed composition through `Hop` (multi-hop search with iteration). This tutorial supplies the **simpler, non-iterative composition shape** (three sub-modules called once each, no loop) most new DSPy users start from.

## Key Claims

- **Subclass `dspy.Module` and implement two methods: `__init__` and `forward`.** *"`__init__`: This is the constructor, where you define the attributes and sub-modules of your program. `forward`: This method contains the core logic of your DSPy program."* The two-method contract is the **minimum viable** custom module — declare sub-modules as `self.*` attributes in `__init__`, run them in `forward`. This mirrors PyTorch `nn.Module`'s `__init__` + `forward` contract exactly (the inspiration the [[dspy-modules|Modules page]] explicitly credits).

- **`forward()` is unconstrained Python.** *"Within the `forward()` method, you are not limited to calling only other DSPy modules; you can also integrate any standard Python functions, such as those for interacting with Langchain/Agno agents, MCP tools, database handlers, and more."* The tutorial's most explicit statement of the **DSPy-is-just-Python** thesis at the [[DSPyModules|Module]] level. The framework does not impose a DSL inside `forward()`; arbitrary Python (loops, conditionals, recursion, external API calls, retrieval, side effects) is supported. This is the framework-level escape hatch that makes [[DSPy]] **easy to migrate to from other frameworks or vanilla SDK usage, and easy to migrate off because essentially it's just python code**.

- **Call the module instance directly — not `forward()` explicitly.** *"When invoking a custom DSPy module, you should use the module instance directly (which calls the `__call__` method internally), rather than calling the `forward()` method explicitly. The `__call__` method handles necessary internal processing before executing the `forward` logic."* This is a **load-bearing discipline** the [[dspy-modules|Modules page]] only implies (every example uses `hop(claim=...)` not `hop.forward(claim=...)`). The internal processing `__call__` adds includes: tracing for [[DSPyOptimizers|optimizer]] replay, [[MLflow]] auto-logging, [[DSPyHistory|history]] threading, and the LM-usage accounting `dspy.Prediction.get_lm_usage()` exposes.

- **Custom modules unlock framework features.** *"We highly recommend putting your logic with a custom module so that you can use other DSPy features, like DSPy optimizer or MLflow DSPy tracing."* Two named consequences: (i) **[[DSPyOptimizers|DSPy Optimizers]]** walk the `self.*` sub-module attributes via `named_predictors()` / `named_parameters()` to discover what they can tune — code that runs sub-modules directly without wrapping them in a `dspy.Module` subclass is **invisible to the optimizer**; (ii) **[[MLflow]] DSPy tracing** auto-logs every sub-module call inside a custom module, producing the per-step trace tree the *MLflow DSPy* integration visualizes. **Plain-function pipelines** (or **inline sub-module use** outside any `dspy.Module`) get neither.

- **MLflow integration is a four-step opt-in.** *"You can set up MLflow easily by following the four steps below."* (i) `pip install mlflow>=3.0.0`; (ii) launch the MLflow UI on a separate process (`mlflow ui --port 5000 --backend-store-uri sqlite:///mlruns.db`); (iii) `mlflow.set_tracking_uri("http://localhost:5000")` + `mlflow.set_experiment("DSPy")`; (iv) `mlflow.dspy.autolog()`. The autolog hook is the **bridge layer** — once enabled, every `__call__` on a [[DSPyModules|`dspy.Module`]] subclass produces a trace span in the MLflow backend. **[[Databricks]] owns [[MLflow]]**; this is the second [[Databricks]] product to appear in the [[DSPy]] line (after [[MateiZaharia]]'s Databricks affiliation as senior author on [[2406.11695-mipro|MIPRO]] / [[2507.19457-gepa|GEPA]]).

- **The canonical three-stage RAG receipt: `dspy.Predict(QueryGenerator)` → `dspy.ColBERTv2(...)` → `dspy.ChainOfThought("question,context->answer")`.** The tutorial's worked example is the wiki's first **complete code listing** of a [[rag|RAG]] pipeline inside a custom `dspy.Module`:

  ```python
  class QueryGenerator(dspy.Signature):
      """Generate a query based on question to fetch relevant context"""
      question: str = dspy.InputField()
      query: str = dspy.OutputField()

  def search_wikipedia(query: str) -> list[str]:
      """Query ColBERT endpoint, which is a knowledge source based on wikipedia data"""
      results = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')(query, k=1)
      return [x["text"] for x in results]

  class RAG(dspy.Module):
      def __init__(self):
          self.query_generator = dspy.Predict(QueryGenerator)
          self.answer_generator = dspy.ChainOfThought("question,context->answer")

      def forward(self, question, **kwargs):
          query = self.query_generator(question=question).query
          context = search_wikipedia(query)[0]
          return self.answer_generator(question=question, context=context).answer
  ```

  Three structural commitments visible in this listing: (a) **a class-based `dspy.Signature`** (`QueryGenerator`) for the **first** sub-module sits alongside **an inline string signature** (`"question,context->answer"`) for the **second** — confirming both [[DSPySignatures|Signature]] declaration styles compose freely in the same `dspy.Module`; (b) the **retrieval call is a plain Python function** (`search_wikipedia`) wrapping `dspy.ColBERTv2(...)(query, k=1)` — not registered as a sub-module — so [[DSPyOptimizers|optimizers]] do **not** see retrieval as a tunable parameter; (c) the `forward` method **unwraps** sub-module outputs by attribute access (`.query`, `.answer`) — calling a sub-module returns a [[DSPyPrediction|`Prediction`]] from which the caller pulls the field of interest, rather than passing the whole `Prediction` forward.

- **The public ColBERTv2 Wikipedia endpoint is `http://20.102.90.50:2017/wiki17_abstracts`.** *"`dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')(query, k=1)`"* — the canonical public retrieval endpoint that the [[dspy-modules|Modules page]], the [[hotpotqa|HotPotQA]] examples, and the [[react|ReAct]] tutorial all assume but never spell out. The endpoint serves the [[ColBERTv2]] index built over Wikipedia 2017 abstracts — the same corpus [[hotpotqa|HotPotQA]] is built on, which is why the wiki's [[DSPy]] / [[react|ReAct]] / [[MIPROv2]] / [[GEPA]] examples reliably use it as the retrieval substrate. **First wiki-corpus page to anchor the endpoint URL.**

- **`dspy.ColBERTv2(url=...)` is a callable wrapper, not a `dspy.Module` subclass.** The construction-then-call pattern `dspy.ColBERTv2(url='...')(query, k=1)` distinguishes [[ColBERTv2]] from the LM-call modules — it is a thin retrieval-client wrapper around the [[ColBERTv2]] HTTP endpoint, not a learnable sub-module. Returns a list of `{"text": ..., ...}` dicts; `k` is the top-`k` retrieval depth. Because the wrapper is **not** registered as `self.<name>` inside `RAG.__init__`, an [[DSPyOptimizers|optimizer]] sees no retrieval parameter — retrieval depth, endpoint, and ranker are **fixed** from the optimizer's perspective.

- **DSPy's design philosophy: programming, not prompting.** *"DSPy is a lightweight authoring and optimization framework, and our focus is to resolve the mess of prompt engineering by transforming prompting (string in, string out) LLM into programming LLM (structured inputs in, structured outputs out) for robust AI system."* The tutorial's closing recap of [[dspy-programming-overview|the Programming Overview's]] central thesis — *writing code instead of strings*. Adds the new framing **string-in-string-out → structured-input-to-structured-output** as a one-line operational summary of the framework's value proposition.

- **DSPy does not standardize agent shape.** *"While we provide pre-built modules which have custom prompting logic like `dspy.ChainOfThought` for reasoning, `dspy.ReAct` for tool calling agent to facilitate building your AI applications, we don't aim at standardizing how you build agents."* The tutorial's explicit **anti-standardization** commitment — DSPy is not [[LangChain]] / [[LlamaIndex]] / [[autogen]]; it does not impose a *Chain* / *Index* / *AgentExecutor* abstraction on top of [[DSPyModules|Module]]. The `forward` method is the entire surface area for agent shape, and inside it the developer writes plain Python.

- **The migration claim: easy to migrate to, easy to migrate off.** *"DSPy is easy to migrate to from other frameworks or vanilla SDK usage, and easy to migrate off because essentially it's just python code."* The **bidirectional portability** claim at the framework boundary. Migrating *to* DSPy is a refactor of existing Python LM-call code into `forward()` plus typed `dspy.Signature` declarations; migrating *off* is the inverse — strip the `dspy.Module` subclass, inline the sub-module calls. Because there is no DSL, no DAG, no orchestration layer, no graph builder, the migration boundaries are unusually thin.

## Key Quotes

> *"A DSPy module is the building block for DSPy programs. Each built-in module abstracts a prompting technique (like chain of thought or ReAct). Crucially, they are generalized to handle any signature. A DSPy module has learnable parameters (i.e., the little pieces comprising the prompt and the LM weights) and can be invoked (called) to process inputs and return outputs. Multiple modules can be composed into bigger modules (programs). DSPy modules are inspired directly by NN modules in PyTorch, but applied to LM programs."* — the tutorial's three-bullet definition of [[DSPyModules|Modules]], lifted verbatim from [[dspy-modules|the Modules *Learn* page]]. The repetition is deliberate: the tutorial restates the definition before showing the custom-module recipe so the reader can read the tutorial standalone.

> *"Although you can build a DSPy program without implementing a custom module, we highly recommend putting your logic with a custom module so that you can use other DSPy features, like DSPy optimizer or MLflow DSPy tracing."* — the framework-feature-unlock claim. The recommendation is operationally load-bearing — plain-function pipelines lose **two** framework capabilities ([[DSPyOptimizers|optimization]] and [[MLflow]] tracing) the moment the developer steps outside a `dspy.Module` subclass.

> *"`__init__`: This is the constructor, where you define the attributes and sub-modules of your program. `forward`: This method contains the core logic of your DSPy program."* — the two-method contract. The framework's commitment to a PyTorch-shaped, not LangChain-shaped, surface.

> *"Within the `forward()` method, you are not limited to calling only other DSPy modules; you can also integrate any standard Python functions, such as those for interacting with Langchain/Agno agents, MCP tools, database handlers, and more."* — the *unconstrained-`forward`* commitment. Names **four** integration surfaces (Langchain, Agno, MCP, database handlers) by example; the underlying claim covers any Python-callable.

> *"When invoking a custom DSPy module, you should use the module instance directly (which calls the `__call__` method internally), rather than calling the `forward()` method explicitly. The `__call__` method handles necessary internal processing before executing the `forward` logic."* — the call-the-instance discipline. The *"necessary internal processing"* phrase is the framework's commitment to keeping the `__call__` → `forward` indirection as the **trace point** for optimizer replay + [[MLflow]] auto-logging.

> *"DSPy is a lightweight authoring and optimization framework, and our focus is to resolve the mess of prompt engineering by transforming prompting (string in, string out) LLM into programming LLM (structured inputs in, structured outputs out) for robust AI system."* — the *string-in-string-out → structured-input-to-structured-output* operational summary of [[dspy-programming-overview|the Programming Overview's]] *writing code instead of strings* thesis.

> *"In DSPy, your application logic simply goes to the `forward` method of your custom Module, which doesn't have any constraint as long as you are writing python code. With this layout, DSPy is easy to migrate to from other frameworks or vanilla SDK usage, and easy to migrate off because essentially it's just python code."* — the bidirectional portability claim.

## Code Receipts

### Receipt 1 — Custom-module template

```python
class MyProgram(dspy.Module):

    def __init__(self, ...):
        # Define attributes and sub-modules here
        {constructor_code}

    def forward(self, input_name1, input_name2, ...):
        # Implement your program's logic here
        {custom_logic_code}
```

The **minimum-viable starting template** every DSPy program is shaped from. Two methods: `__init__` declares sub-modules as `self.*` attributes; `forward` runs them. Everything else is application-specific.

### Receipt 2 — Three-stage RAG

```python
import dspy

class QueryGenerator(dspy.Signature):
    """Generate a query based on question to fetch relevant context"""
    question: str = dspy.InputField()
    query: str = dspy.OutputField()

def search_wikipedia(query: str) -> list[str]:
    """Query ColBERT endpoint, which is a knowledge source based on wikipedia data"""
    results = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')(query, k=1)
    return [x["text"] for x in results]

class RAG(dspy.Module):
    def __init__(self):
        self.query_generator = dspy.Predict(QueryGenerator)
        self.answer_generator = dspy.ChainOfThought("question,context->answer")

    def forward(self, question, **kwargs):
        query = self.query_generator(question=question).query
        context = search_wikipedia(query)[0]
        return self.answer_generator(question=question, context=context).answer
```

Five load-bearing details: (i) one sub-module is declared via a **class-based** [[DSPySignatures|Signature]] (`QueryGenerator`), the other via an **inline string** signature (`"question,context->answer"`); (ii) retrieval is a **plain Python function** wrapping `dspy.ColBERTv2(url=...)(query, k=1)`, not registered as a sub-module; (iii) the canonical public ColBERTv2 endpoint is `http://20.102.90.50:2017/wiki17_abstracts`; (iv) `forward` **unwraps** sub-module outputs by attribute access (`.query`, `.answer`); (v) `**kwargs` in `forward(self, question, **kwargs)` is the tutorial's defensive default — `dspy.Module` may receive metadata kwargs (e.g. demo selection) the user code doesn't need to acknowledge.

### Receipt 3 — Configure and call

```python
import os

os.environ["OPENAI_API_KEY"] = "{your_openai_api_key}"

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))
rag = RAG()
print(rag(question="Is Lebron James the basketball GOAT?"))
```

Three commits: (i) global LM config via `dspy.configure(lm=dspy.LM(...))` — the [[DSPyLM|`dspy.LM`]] client mediates between [[DSPyModules|Modules]] and the [[LiteLLM]] / provider layer; (ii) **module instantiation** is parameterless here (`RAG()`) — the only construction concern is sub-module wiring inside `__init__`; (iii) **call the instance, not `forward`** — `rag(question=...)` routes through `__call__` and produces the trace + LM-usage accounting + (if configured) the MLflow span. The example LM is **`gpt-4o-mini`** — the same model the [[dspy-conversation-history]] tutorial uses.

### Receipt 4 — MLflow setup

```python
%pip install mlflow>=3.0.0
```

```bash
mlflow ui --port 5000 --backend-store-uri sqlite:///mlruns.db
```

```python
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("DSPy")
mlflow.dspy.autolog()
```

Four-step opt-in for [[MLflow]] DSPy tracing. The fourth step — `mlflow.dspy.autolog()` — is the bridge: every `__call__` on a [[DSPyModules|`dspy.Module`]] subclass after this point produces a trace span in the MLflow backend, visualized as a per-step tree in the MLflow UI.

## Connections

- [[DSPy]] — the framework this tutorial scopes. Updated in place with a new *"Custom modules: the canonical starting template"* section + tracked-sources frontmatter addition.
- [[dspy-conversation-history]] — first wiki-corpus DSPy tutorial. Sibling tutorial; uses the same `gpt-4o-mini` example LM. Scopes a single-sub-module application (`dspy.Predict` + `dspy.History`); this tutorial scopes **three** sub-modules in a non-iterative pipeline.
- [[dspy-customer-service-agent]] — second wiki-corpus DSPy tutorial. Scopes a [[react|`dspy.ReAct`]] application with seven tools and a typed [[Pydantic]] domain; this tutorial scopes a custom `dspy.Module` subclass with three sub-modules. Together with this tutorial, fills out the application-stack ladder from custom-module template (rung 2) to multi-tool agent (rung 4).
- [[dspy-modules]] — canonical *Learn*-page source for the [[DSPyModules|Module]] abstraction (page 5 of 13). Defines the composition pattern via the multi-hop `Hop` example; **this tutorial restates the composition recipe for the minimum-viable non-iterative case** (three sub-modules called once each).
- [[DSPyModules]] — concept-level anchor for the [[DSPyModules|Module]] abstraction. **Extended in place** with a new *"Custom-module starting template"* section pointing at this tutorial as the canonical worked receipt for the rung-2 shape.
- [[DSPyPredict]] — concept-level anchor for the minimal `dspy.Predict` primitive; used here as the **first** sub-module in the RAG pipeline (driving the `QueryGenerator` Signature).
- [[chainofthought]] / [[chainofthought]] — concept-level anchor for [[chainofthought|chain-of-thought]] reasoning; used here as the **second** sub-module via the inline string Signature `"question,context->answer"`. The wiki's first record of [[chainofthought|`dspy.ChainOfThought`]] inside a custom `dspy.Module` with an inline string signature pulled from `forward`.
- [[DSPySignatures]] — concept-level anchor for [[DSPySignatures|Signatures]]. The tutorial demonstrates **both** Signature styles (class-based + inline-string) inside one `dspy.Module` subclass.
- [[ColBERTv2]] — concept-level anchor for the [[ColBERTv2|ColBERTv2 retriever]] (Khattab, Santhanam et al. 2022 — the late-interaction retrieval model). **Promoted from forward reference**; this tutorial supplies the canonical public Wikipedia 2017 abstracts endpoint URL.
- [[rag|RAG]] — the application pattern this tutorial's worked example implements. Extended in place with this tutorial's canonical three-stage receipt as the simplest reference RAG inside a `dspy.Module`.
- [[MLflow]] — the LLMOps tracing / experiment-tracking tool [[Databricks]] maintains. The tutorial gives the **first wiki-corpus DSPy-specific MLflow integration recipe** (the four-step opt-in + `mlflow.dspy.autolog()` bridge hook).
- [[Databricks]] — entity that owns [[MLflow]] and employs [[MateiZaharia]] (senior author on [[2406.11695-mipro|MIPRO]] / [[2507.19457-gepa|GEPA]]). The MLflow tracing recipe is the second [[Databricks]]-touchpoint in the DSPy line, after the optimizer-paper authorships.
- [[DSPyOptimizers]] — the optimizer family that walks `self.*` sub-module attributes via `named_predictors()` / `named_parameters()`. The tutorial's framework-feature-unlock claim is operationally load-bearing for this layer — code outside a `dspy.Module` subclass is invisible to the optimizer.
- [[DSPyPrediction]] — the typed `Prediction` object every sub-module call returns. The `forward` body's attribute access (`.query`, `.answer`) is the canonical receipt for **unwrapping** a `Prediction` field into the next sub-module's input.
- [[DSPyLM]] — the LM-client layer `dspy.configure(lm=dspy.LM(...))` configures. Sits below the [[DSPyModules|Module]] in the call stack; the call `dspy.LM("openai/gpt-4o-mini")` is the canonical model-config commit.
- [[hotpotqa|HotPotQA]] — the canonical Wikipedia-2017-based multi-hop QA dataset; uses the **same** ColBERTv2 endpoint as this tutorial. The wiki's [[MIPROv2]] / [[2507.19457-gepa|GEPA]] / [[react|ReAct]] examples all assume the endpoint that this tutorial documents.
- [[react|ReAct]] — named in the tutorial as the canonical tool-calling agent module. The customer-service-agent tutorial ([[dspy-customer-service-agent]]) is the wiki's reference ReAct receipt; this tutorial is the reference **non-ReAct** custom-module receipt.
- [[LangChain]] — named in the tutorial as an example of the kind of external framework `forward()` can integrate with. Not a DSPy dependency.
- [[ModelContextProtocol|MCP]] — named in the tutorial as an example of external tool-source that `forward()` can integrate. The [[DSPyMCP]] binding (`dspy.Tool.from_mcp_tool`) is the canonical surface.
- [[PyTorch]] — the architectural inspiration for `dspy.Module`'s `__init__` + `forward` contract. *"DSPy modules are inspired directly by NN modules in PyTorch, but applied to LM programs."*
- [[GenerativeAI]] — the application class the tutorial scopes (*"how to build a GenAI application"*).

## Contradictions

No contradictions with prior wiki content. The tutorial restates the [[DSPyModules|Module]] definition and composition pattern from [[dspy-modules|the Modules *Learn* page]] without contradiction, and supplies the worked RAG receipt as the minimum-viable instance of the [[dspy-modules|Hop]] multi-hop composition pattern (one-pass instead of iterative). The ColBERTv2 endpoint URL `http://20.102.90.50:2017/wiki17_abstracts` is consistent with the [[hotpotqa|HotPotQA]] and [[MIPROv2]] / [[GEPA]] examples' implicit assumption.

## Scope Limits

- **No optimization.** The tutorial stops at the un-optimized `RAG()` instance. No `dspy.MIPROv2(...).compile(rag, ...)` call, no metric, no dev set, no [[DSPyOptimizers|optimizer]] receipt. The *"why customize"* framing names DSPy Optimizer as a framework feature unlocked by the custom-module shape but does not exercise it.
- **No evaluation.** No `dspy.Evaluate(...)` call, no metric definition, no train/dev split. The reader gets the build-time recipe but no measurement loop.
- **No multi-hop / loop.** The worked `RAG` runs each sub-module exactly once; the [[dspy-modules|Modules page's]] `Hop` example covers the iterative case.
- **No history / multi-turn.** The `RAG` is single-shot; the [[dspy-conversation-history]] tutorial covers multi-turn.
- **No tools / agent.** The `RAG` calls retrieval as a Python function, not a [[DSPyTools|`dspy.Tool`]] inside [[react|`dspy.ReAct`]]; the [[dspy-customer-service-agent]] tutorial covers the multi-tool agent shape.
- **Endpoint trust.** The `http://20.102.90.50:2017/wiki17_abstracts` ColBERTv2 endpoint is a **public unauthenticated HTTP endpoint** on a Stanford-side server; a production deployment would self-host the [[ColBERTv2]] index and adapter.
- **MLflow scope.** The MLflow recipe is **local-only** (`http://localhost:5000` + `sqlite:///mlruns.db`); production [[MLflow]] deployments use [[Databricks]]-managed or self-hosted shared backends.
