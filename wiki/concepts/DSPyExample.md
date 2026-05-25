---
title: "DSPy Example"
type: concept
tags: [dspy, llm-programming, data, dataset, evaluation, example, primitive]
sources: [dspy-data, dspy-modules, dspy-evaluation-overview]
last_updated: 2026-05-24
---

# DSPy Example

**`dspy.Example`** is the **data-side primitive** of [[DSPy]] — the typed Python dict-with-utilities that holds a single datapoint in a training, development, or test set. It is to the data layer what [[DSPyPredict|`dspy.Predict`]] is to the strategy layer: the minimal class every other data artifact decomposes to. The canonical source is the [[dspy-data|Data Handling]] page (page 10 of 13 of the *Learn* section); this concept page captures the abstraction.

The single most important structural fact about `dspy.Example` is that **[[DSPyPrediction|`dspy.Prediction`]] is a subclass of it**. *"Your DSPy modules will return values of the type `Prediction`, which is a special sub-class of `Example`."* The data the program **reads** and the data the program **produces** share a class hierarchy — which is what makes the [[DSPyMetrics|metric]]'s `(example, prediction) -> score` contract type-symmetric (both arguments expose the same dot-access / `inputs()` / `labels()` surface).

## Shape

A `dspy.Example(...)` instance has four load-bearing properties:

1. **Dict-like field storage with arbitrary keys and value types.** *"Examples can have any field keys and any value types, though usually values are strings."* The framework imposes **no schema** — the schema is supplied separately by the [[DSPySignatures|Signature]] of the [[DSPyModules|Module]] that will consume the example. The user invents the field names; the framework does not enforce them.

   ```python
   qa_pair = dspy.Example(question="This is a question?", answer="This is an answer.")
   trainset = [dspy.Example(report="LONG REPORT 1", summary="short summary 1"), ...]
   ```

2. **Dot-notation field access.** *"Values can be accessed using the `.` (dot) operator."* `qa_pair.question` rather than `qa_pair["question"]`. This is identical to the [[DSPyPrediction|`Prediction`]] field-access discipline — the `dspy.ChainOfThought` user reads `.reasoning` and `.answer` from the returned `Prediction` the same way the metric author reads `.answer` from the ground-truth `Example`.

3. **`input_keys` tagging.** Every `Example` carries an attached `input_keys` set — either `None` (untagged) or a set like `{'question'}` — that declares which fields function as **inputs** to the program. The remaining fields are implicitly **labels or metadata**. The tagging is **attached metadata**, not a structural partition — the same `Example` can be re-tagged for different program calls. The `(input_keys=...)` segment of the `__repr__` makes the tagging visible:

   ```
   Example({'question': 'This is a question?', 'answer': 'This is an answer.'}) (input_keys=None)
   ```

   vs after `.with_inputs("question")`:

   ```
   Example({'question': 'This is a question?', 'answer': 'This is an answer.'}) (input_keys={'question'})
   ```

4. **Functional-update API.** `with_inputs(...)` returns a **new** `Example`; it does not mutate the original. The functional-update discipline is consistent with DSPy's broader thread-safety story ([[DSPyLM|`dspy.LM`]] bind modes, [[DSPyAdapters|adapter]] bind modes — the data layer follows the same pattern).

## The four-method API

| Method | Form | Returns | Purpose |
|---|---|---|---|
| **Construction** | `dspy.Example(field1=v1, field2=v2, ...)` | `Example` | Build a datapoint with arbitrary keyword fields. |
| **Field access** | `ex.field_name` | the value | Dot-notation read. |
| **Tag inputs** | `ex.with_inputs("field1", "field2", ...)` | new `Example` | Mark which fields are inputs; non-mutating. |
| **Inputs view** | `ex.inputs()` | new `Example` (only input fields) | Pass to the program. |
| **Labels view** | `ex.labels()` | new `Example` (only non-input fields) | Pass to the [[DSPyMetrics|metric]]. |

That is the complete surface the [[dspy-data|Data Handling]] page documents. The framework adds nothing else to the data layer — datasets are plain `list[dspy.Example]` and splits are plain Python slicing.

## The canonical idiom

```python
import dspy

# 1. Build a few examples with arbitrary fields
qa_pair = dspy.Example(question="This is a question?", answer="This is an answer.")

# 2. Tag which field is the input
tagged = qa_pair.with_inputs("question")

# 3. Partition for use
inputs_only = tagged.inputs()   # Example({'question': '...'}) (input_keys={'question'})
labels_only = tagged.labels()   # Example({'answer': '...'})    (input_keys=None)

# 4. Build a training set as a plain list
trainset = [
    dspy.Example(question="What's the capital of France?", answer="Paris").with_inputs("question"),
    dspy.Example(question="What's 2 + 2?",                  answer="4"    ).with_inputs("question"),
    # ...
]
```

The list comprehension form — `[dspy.Example(...).with_inputs(...) for row in rows]` — is the canonical way to convert a [[HuggingFace|HuggingFace]] dataset, a Python dict-row iterator, or a CSV/JSON loader into a DSPy dataset.

## `with_inputs(...)` is warn-not-fail

*"Multiple Inputs; be careful about marking your labels as inputs, unless you mean it."*

The framework does **not** check whether a tagged input is actually a label. The discipline is on the developer:

```python
# Valid but dangerous — promotes the label into an input, silently leaks the answer
qa_pair.with_inputs("question", "answer")
```

This is consistent with DSPy's broader warn-not-fail discipline ([[DSPySignatures|Signature]] input-type checking is warn-not-fail; `dspy.configure(warn_on_type_mismatch=False)` opts out). The framework prioritizes prototyping ergonomics; correctness is the developer's responsibility.

## The `inputs()` / `labels()` partition is non-destructive

Both methods return **new** `Example` objects:

```python
article_summary = dspy.Example(article="...", summary="...").with_inputs("article")

input_key_only      = article_summary.inputs()   # Example({'article': '...'}) (input_keys={'article'})
non_input_key_only  = article_summary.labels()   # Example({'summary': '...'}) (input_keys=None)
```

Note that **`labels()`'s return has `input_keys=None`** — the returned `Example` carries no fields that were inputs, so its own `input_keys` tagging is reset. This is what makes the labels view safe to pass to a [[DSPyMetrics|metric]] that may itself attempt to call `.with_inputs(...)` on the example for its own internal program.

## Why `Example` ↔ `Prediction` inheritance matters

Three structural consequences flow from `Prediction(Example)`:

| Consequence | Mechanism |
|---|---|
| **Type-symmetric metric contract.** | A metric is `(example, prediction) -> score`. Both arguments are `Example`s, so the metric author writes `example.answer == prediction.answer` with no class-aware branching. |
| **The same `with_inputs / inputs / labels` surface on both ends.** | A [[DSPyMetrics|metric]] that is itself a [[DSPyModules|`dspy.Module`]] (the long-form-task regime per [[dspy-evaluation-overview]]) can call `prediction.with_inputs(...)` to feed the prediction into its own internal program — without distinguishing whether it came from a dataset or a Module call. |
| **`dspy.Prediction` reuses every `Example` utility for free.** | Field-access by dot, `__repr__` showing `(input_keys=...)`, `inputs()` / `labels()` partition — all inherited. The `Prediction`-specific surface ([[DSPyPrediction|`get_lm_usage()`]] from DSPy 2.6.16+) is the only delta. |

## Position in the framework

| Layer | Primitive | Source page |
|---|---|---|
| **Strategy / control flow** | [[DSPyPredict|`dspy.Predict`]] | [[dspy-modules]] (page 5) |
| **Schema / typing** | [[DSPySignatures|Signature]] | [[dspy-signatures]] (page 4) |
| **Wire format / parsing** | [[DSPyAdapters|Adapter]] | [[dspy-adapters]] (page 6) |
| **External tool invocation** | [[DSPyTools|`dspy.Tool`]] / `ToolCalls` | [[dspy-tools]] (page 7) |
| **Provider plumbing** | [[DSPyLM|`dspy.LM`]] | [[dspy-language-models]] (page 3) |
| **Data — input** | **`dspy.Example`** | **[[dspy-data]] (page 10)** |
| **Data — output** | [[DSPyPrediction|`dspy.Prediction`]] | [[dspy-modules]] (page 5) |
| **Measurement** | [[DSPyMetrics|Metric]] | [[dspy-metrics]] (page 11, forward ref) |
| **Search** | [[DSPyOptimizers|Optimizer]] | [[dspy-optimizers]] (page 13, forward ref) |

`Example` is the *data-input* primitive at the bottom-left of the framework's call stack — every [[DSPyModules|Module]] consumes one (or many) `Example`s via `.inputs()`-view kwargs, every [[DSPyMetrics|metric]] consumes one as ground truth, every [[DSPyOptimizers|Optimizer]] consumes a `list[dspy.Example]` as its training data.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-conversation-history]] — `dspy.Example(..., history=dspy.History(messages=[...]))`: the canonical multi-turn shape; receipt demonstrates that `Example` accepts **any** typed field (here a structured [[DSPyHistory|`dspy.History`]] object), not just strings.
- [[dspy-entity-extraction-tutorial]] — canonical HuggingFace → DSPy idiom: `[dspy.Example(tokens=row["tokens"], expected_extracted_people=extract_people(row)).with_inputs("tokens") for row in conll_dataset]`.
- [[dspy-tool-use-tutorial]] — multi-field training-set shape: `dspy.Example(question=..., answer=..., functions=...).with_inputs("question", "functions")` over [[ToolHop]]; tags **two** fields as inputs.
- [[dspy-tutorial-rag-as-agent]] — `dspy.Example(claim=..., titles=[...]).with_inputs("claim")` over [[HoVer]]; demonstrates list-valued label fields (a list of gold titles) consumed by a custom dual-mode `top5_recall` metric.
- [[dspy-saving-tutorial]] — edge-case receipt for the `Prediction(Example)` inheritance: state-only `program.load(path)` materializes saved demos as plain Python `dict`s rather than typed `dspy.Example` instances — the only wiki tutorial that surfaces this serialization-side asymmetry.

## Connections

- [[DSPy]] — the framework whose data primitive this concept records.
- [[dspy-data]] — canonical source (page 10 of 13). Mints this page.
- [[DSPyData]] — the sibling concept page (the dataset / split convention `Example`s populate); the data-handling discipline at the *collection* layer, where this page records the data-handling discipline at the *primitive* layer.
- [[DSPyPrediction]] — the `Example`-subclass [[DSPyModules|Modules]] return. Shares the dot-access and `inputs()` / `labels()` surface; the inheritance is what makes the metric's `(example, prediction) -> score` contract type-symmetric.
- [[DSPyEvaluation]] — the Evaluation stage; the dev-set's elements are `Example`s.
- [[dspy-evaluation-overview]] — page 9; introduces the four-step iterative-evaluation loop whose Step 1 (collect dev set) is operationalized by *this* primitive.
- [[DSPyMetrics]] — forward reference to page 11; consumes `(example, prediction)` where both are `Example`s. The metric reads `example.field` to get ground-truth values.
- [[DSPyOptimizers]] — forward reference to page 13; consumes a `list[dspy.Example]` as the training data the search runs over.
- [[DSPyModules]] — consumes an `Example`'s `inputs()`-view as kwargs to `forward(...)`.
- [[DSPyPredict]] — the strategy-side primitive `Example` is the data-side counterpart of.
- [[DSPySignatures]] — the schema layer that names which fields a Module expects as inputs; `Example.with_inputs(...)` tags the matching field names on the data side.
- [[DSPyProgrammingModel]] — the separation-of-concerns philosophy this primitive extends to the data layer: data is *attached-tagged*, not structurally partitioned.
- [[HuggingFace]] — named in [[dspy-evaluation-overview]] as a primary public-dataset source; the canonical idiom is to construct `[dspy.Example(**row).with_inputs(...) for row in hf_dataset]`.
- [[ModelEvaluation]] / [[OfflineEvaluation]] — the general / specific evaluation regimes DSPy's data primitive serves.
- [[Python]] — the host language whose `dict` and `list` primitives DSPy reuses; `Example` is dict-like, datasets are lists.
- [[dspy-modules]] — page 5; defines [[DSPyPrediction|`dspy.Prediction`]] as the Module-return type and (implicitly) its `Example` parentage. This page makes the inheritance explicit.
