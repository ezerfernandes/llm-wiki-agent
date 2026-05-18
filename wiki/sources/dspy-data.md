---
title: "DSPy Learn — Data Handling"
type: source
tags: [dspy, llm-programming, evaluation, data, dataset, example, development-set]
date: 2026-05-17
source_file: raw/dspy-data.md
---

# DSPy Learn — Data Handling

## Summary

**Page 10 of 13** of the [[DSPy]] *Learn* documentation; **second page of the [[DSPyEvaluation|Evaluation stage]]** of the [[dspy-learn-index|three-stage Programming → Evaluation → Optimization]] model. The [[dspy-evaluation-overview|Evaluation Overview]] (page 9) operationalized the stage as a four-step iterative loop and explicitly forward-referenced this page to expand **Step 1** — *"collect an initial development set"* — into the concrete **data container** the rest of the framework reads from. This page is short and load-bearing in the same way [[dspy-language-models]] was for the *"swap the LM"* claim: it minimally defines the data primitive every other DSPy artifact composes against. The canonical claim is that **DSPy's data primitive is a typed Python dict-with-utilities** — [[DSPyExample|`dspy.Example`]] — that (a) accepts arbitrary field names and value types, (b) carries an **input/label separation** as an attached `input_keys` set rather than a structural divide, and (c) is the **same class** that [[DSPyPrediction|`dspy.Prediction`]] specializes for module outputs. The page also commits the framework to the **train / dev / test** three-set convention inherited from supervised ML — *"DSPy is a machine learning framework, so working in it involves training sets, development sets, and test sets"* — and to the **inputs-only sufficiency** claim — *"You can use DSPy effectively without any intermediate or final labels, but you will need at least a few example inputs"* — which is the data-side mirror of [[dspy-evaluation-overview|the Evaluation Overview's]] *intermediate-step labels are almost never needed* commitment. Mints two concept pages: [[DSPyExample]] (the data primitive) and [[DSPyData]] (the dataset / split convention the Evaluation stage assumes).

## Key Claims

- **DSPy is a machine learning framework, not an ad-hoc prompt SDK.** The page opens with the framing claim that working in DSPy *"involves training sets, development sets, and test sets"* — the conventional supervised-ML three-set convention. This is consistent with the [[dspy-learn-index|three-stage model]]'s *Programming → Evaluation → Optimization* order: a [[DSPyOptimizers|DSPy Optimizer]] is **trained** on a dev set the way an ML model is trained on a training set, and the test set is **held out** for final assessment after optimization. The page locates DSPy inside the supervised-ML tradition rather than presenting it as a separate paradigm.

- **Three types of values per example: inputs, intermediate labels, final label.** *"For each example in your data, we distinguish typically between three types of values: the inputs, the intermediate labels, and the final label."* This is a load-bearing typology because it interacts with [[DSPyMetrics|metrics]] (page 11) in a structured way: **inputs** are what the program sees, **final labels** are what the metric scores against (when the metric is reference-based), and **intermediate labels** are what the user almost never needs to supply (per [[dspy-evaluation-overview|the Evaluation Overview]]'s *"You almost never need labels for the intermediate steps in your program in DSPy"*). The three-type split is *typological* — not every example has all three.

- **Inputs-only sufficiency: a few example inputs are enough to use DSPy.** *"You can use DSPy effectively without any intermediate or final labels, but you will need at least a few example inputs."* This is the data-side mirror of [[dspy-evaluation-overview|the Evaluation Overview's]] *intermediate-step labels are almost never needed* claim and the bridge to **reference-free metrics** ([[llmasjudge|LLM-as-judge]] over a rubric, or any heuristic on the output itself). The minimum viable DSPy dataset is **a few inputs, no labels** — labels become required only when the chosen metric is reference-based (exact-match, F1, BLEU).

- **The core data type is `dspy.Example`.** *"The core data type for data in DSPy is `Example`."* Every datapoint in a training / dev / test set is an `Example`. This is the *data-side* primitive that pairs with the [[DSPyPredict|`dspy.Predict`]] *strategy-side* primitive: just as every [[DSPyModules|Module]] decomposes to a `Predict`, every dataset element decomposes to an `Example`.

- **`Example` is a typed dict-with-utilities.** *"DSPy `Examples` are similar to Python `dicts` but have a few useful utilities."* The page does not claim `Example` *is* a dict — it claims `Example` is **like** a dict with extra structure. The two utilities the page demonstrates are (a) **dot-notation access** (`qa_pair.question` rather than `qa_pair["question"]`) and (b) **input-key tagging** (the `with_inputs()` method and the derived `inputs()` / `labels()` accessors). The `(input_keys=None)` printout in every `Example.__repr__()` is the framework's load-bearing UI for *"this example has not yet declared which fields are inputs."*

- **`Prediction` is a sub-class of `Example`.** *"Your DSPy modules will return values of the type `Prediction`, which is a special sub-class of `Example`."* This is a structurally important inheritance: the **same class hierarchy** carries both *data the program reads from* (`Example` in a dataset) and *data the program produces* (`Prediction` returned by `forward()`). The [[DSPyMetrics|metric's]] `(example, prediction) -> score` contract is therefore type-symmetric — both arguments have the same dict-with-utilities surface; the metric just compares their fields. This is why a metric can be written as a single function over both — they share `.attribute` access and the same `inputs()` / `labels()` partition.

- **Arbitrary field names and value types.** *"Examples can have any field keys and any value types, though usually values are strings."* `Example` imposes **no schema**. The schema is supplied **separately** by the [[DSPySignatures|Signature]] the calling [[DSPyModules|Module]] consumes — `Example` is the *runtime data container* and `Signature` is the *type declaration*. The page's two examples make this concrete: a `Example(question=..., answer=...)` for QA, a `Example(report="LONG REPORT 1", summary="short summary 1")` for summarization. The user invents the field names; the framework does not enforce them.

- **Datasets are just Python lists of `Example`s.** *"You can now express your training set for example as: `trainset = [dspy.Example(report=..., summary=...), ...]`"* DSPy does **not** introduce a `Dataset` class. The dataset is a plain `list[dspy.Example]` — iteration, slicing, indexing, and `len()` are inherited from Python's list. This is consistent with DSPy's *plain-Python* discipline ([[dspy-modules|the Modules page]]: *"DSPy is just Python code that uses modules in any control flow you like"*) — the dataset is just a list, and train/dev/test splits are just **slices of that list**.

- **`with_inputs()` is the input/label separator.** *"The `Example` objects have a `with_inputs()` method, which can mark specific fields as inputs. (The rest are just metadata or labels.)"* Unlike conventional ML where `(X, y)` is a structural tuple, DSPy puts inputs and labels in the **same** `Example` and tags which fields are inputs with `with_inputs("field1", "field2", ...)`. The remaining fields are *implicitly* labels or metadata. This is the data-side reflex of [[DSPyProgrammingModel|the Programming Model's]] *"the program defines what's an input, the data declares which fields fill those inputs"* — the Signature names the input field, the Example tags the same field name as `input_keys`, and the framework wires them together.

- **`with_inputs()` returns a new Example, not a mutation.** Examination of the page's printout confirms: `qa_pair.with_inputs("question")` returns an `Example` whose `input_keys={'question'}` while the original `qa_pair` still prints with `input_keys=None`. The functional-update discipline is consistent with DSPy's broader thread-safety story ([[DSPyLM|`dspy.LM`]] bind modes — `configure(...)` global vs `context(...)` block-local; [[DSPyAdapters|adapters]] same; here the data layer also avoids in-place mutation).

- **`with_inputs()` accepts multiple input fields — with a warning.** *"Multiple Inputs; be careful about marking your labels as inputs, unless you mean it."* The page is explicit that `with_inputs("question", "answer")` is a *valid* but *dangerous* call — the developer could accidentally promote a label into an input and silently leak the answer. The framework does not check; the discipline is on the developer. This is a recurring DSPy pattern (warn-not-fail input type-checking, opt-out via `warn_on_type_mismatch`) — *"prototyping-first, correctness through discipline, not through fences."*

- **Dot-notation field access.** *"Values can be accessed using the `.` (dot) operator. You can access the value of key `name` in defined object `Example(name="John Doe", job="sleep")` through `object.name`."* This is **identical** to [[DSPyPrediction|`dspy.Prediction`]]'s field-access discipline (a `Prediction` from `dspy.ChainOfThought` exposes `.reasoning` and `.answer` the same way). The metric-function author writes `example.answer == prediction.answer` rather than `example["answer"] == prediction["answer"]` — the dot operator is the canonical surface across the framework.

- **`inputs()` and `labels()` are the input/label partition accessors.** *"To access or exclude certain keys, use `inputs()` and `labels()` methods to return new `Example` objects containing only input or non-input keys, respectively."* Both return **new** `Example`s; the partition is non-destructive. The page's worked example: `article_summary.inputs()` returns `Example({'article': '...'}) (input_keys={'article'})` and `article_summary.labels()` returns `Example({'summary': '...'}) (input_keys=None)` — note that **`labels()`'s return has `input_keys=None`**, not the original tagging — because the returned `Example` has no fields that were inputs in the partition. This is the canonical *"give me only the inputs to feed into the program / only the labels to feed into the metric"* surface.

## Key Quotes

> "DSPy is a machine learning framework, so working in it involves training sets, development sets, and test sets." — opening framing claim; locates DSPy inside the supervised-ML tradition.

> "For each example in your data, we distinguish typically between three types of values: the inputs, the intermediate labels, and the final label." — the three-type per-example typology.

> "You can use DSPy effectively without any intermediate or final labels, but you will need at least a few example inputs." — the **inputs-only sufficiency** claim; the data-side mirror of *intermediate-step labels are almost never needed*.

> "The core data type for data in DSPy is `Example`. You will use **Examples** to represent items in your training set and test set." — the canonical data-primitive declaration.

> "DSPy **Examples** are similar to Python `dict`s but have a few useful utilities. Your DSPy modules will return values of the type `Prediction`, which is a special sub-class of `Example`." — `Example` ↔ `Prediction` class-hierarchy commitment.

> "Examples can have any field keys and any value types, though usually values are strings." — no-schema-by-default; the [[DSPySignatures|Signature]] provides schema, the `Example` provides values.

> "In traditional ML, there are separated 'inputs' and 'labels'. In DSPy, the `Example` objects have a `with_inputs()` method, which can mark specific fields as inputs. (The rest are just metadata or labels.)" — input/label tagging as **attached metadata**, not structural partition.

> "Multiple Inputs; be careful about marking your labels as inputs, unless you mean it." — the warn-not-fail discipline at the data layer.

> "Values can be accessed using the `.` (dot) operator." — the dot-notation field-access convention shared with [[DSPyPrediction|`dspy.Prediction`]].

> "To access or exclude certain keys, use `inputs()` and `labels()` methods to return new `Example` objects containing only input or non-input keys, respectively." — the input/label partition accessors; both non-destructive.

## The `dspy.Example` API surface (this page)

The page documents a compact surface — the data-handling chapter is **deliberately minimal**, mirroring [[dspy-evaluation-overview|the Evaluation Overview's]] *"data first, metric second"* discipline. The complete API the page introduces:

| Operation | Form | Returns | Purpose |
|---|---|---|---|
| Construction | `dspy.Example(field1=v1, field2=v2, ...)` | `Example` | Build a datapoint with arbitrary fields. |
| Field access | `ex.field_name` | the value | Dot-notation read. |
| Tag inputs | `ex.with_inputs("field1", "field2")` | new `Example` | Mark which fields are inputs; non-mutating. |
| Inputs view | `ex.inputs()` | new `Example` with only input fields | Pass to the program (the [[DSPyModules|Module]]). |
| Labels view | `ex.labels()` | new `Example` with only non-input fields | Pass to the [[DSPyMetrics|metric]] for scoring. |
| Repr | `print(ex)` | `Example({...}) (input_keys=...)` | Shows both the dict and the input-key tagging. |

What the page does **not** introduce — and which the wiki should treat as *deliberately scope-limited rather than absent*:

- A `Dataset` class (datasets are plain `list[dspy.Example]`).
- Slicing helpers (`trainset[:50]` etc. is just Python list slicing).
- Loaders from HuggingFace / CSV / JSON (mentioned in passing by [[dspy-evaluation-overview|the Evaluation Overview]] as a data-sourcing option but not API-documented here).
- Train/dev/test split helpers (deferred — the page asserts the three-set convention but does not provide a `train_test_split(...)` API; users construct splits manually).
- A `Prediction`-specific surface (already documented on [[DSPyPrediction]] as the [[DSPyModules|Module]]-return type).

The deliberate scope-limit is consistent with DSPy's *small-surface-area* discipline — the framework adds primitives only when they are not already in Python.

## How this page closes the Evaluation Overview's forward reference

[[dspy-evaluation-overview|The Evaluation Overview]] (page 9) committed the framework to a **four-step iterative-evaluation loop** whose first step was *"collect an initial development set"* of 20–200 examples. The Overview did **not** define what a *"development set"* concretely **is** in DSPy terms — it deferred to a forward reference [[DSPyData]] that the wiki carried explicitly. This page **resolves** that forward reference by:

1. **Naming the data primitive** — [[DSPyExample|`dspy.Example`]] — that fills a development set.
2. **Naming the dataset shape** — a plain `list[dspy.Example]`.
3. **Naming the input/label partition mechanism** — `with_inputs()` plus `inputs()` / `labels()` accessors — that the metric layer (page 11) will consume.
4. **Confirming the three-set convention** — *train, dev, test* — that the [[DSPyOptimizers|Optimizers]] (page 13) will consume.

The page is short by design — the Evaluation stage's data discipline is small precisely because DSPy reuses Python's list / dict semantics for everything that does not need framework-level machinery. The framework-level contributions on the data layer are exactly two: the `Example` class (with its `with_inputs` / `inputs` / `labels` / dot-access utilities) and its `Prediction` subclass (already documented on [[DSPyPrediction]]).

## Three load-bearing commitments

The Data Handling page makes three non-trivial commitments worth recording explicitly:

### Commitment 1: Datasets are plain Python lists

Unlike PyTorch (`torch.utils.data.Dataset`), TensorFlow (`tf.data.Dataset`), or HuggingFace (`datasets.Dataset`), DSPy does **not** introduce a `Dataset` class. A training set is a `list[dspy.Example]`. This is a deliberate *minimal-API* choice consistent with [[dspy-modules|the Modules page's]] *"DSPy is just Python code"* discipline — the framework adds a class only when Python's built-ins don't fit. For datasets, lists fit: iteration, slicing, indexing, `len()`, `random.shuffle(...)`, list comprehensions all work directly.

The consequence: **train/dev/test splits are just slicing**. The wiki should treat the standard idiom as `trainset = examples[:80]; devset = examples[80:100]; testset = examples[100:]` — *plain Python*, not framework API.

### Commitment 2: Input/label tagging is attached, not structural

In conventional supervised ML, an example is a `(X, y)` tuple — the partition is structural. In DSPy, an example is a single `Example(...)` carrying **all** fields with `input_keys` as **attached metadata** (the `(input_keys={...})` printout). The structural consequence: the same `Example` can be tagged differently for different program calls. The same `Example(article=..., summary=...)` can be:

- `.with_inputs("article")` to feed an article-to-summary program.
- `.with_inputs("article", "summary")` to feed a *(careful!)* refinement program that also takes the prior summary.
- `.with_inputs()` (no inputs) to expose both fields as labels for a metric.

This is a richer model than `(X, y)` and is consistent with the *typed-but-loosely-coupled* discipline that runs through DSPy.

### Commitment 3: Inputs-only sufficiency

*"You can use DSPy effectively without any intermediate or final labels, but you will need at least a few example inputs."*

The minimum viable DSPy dataset is **inputs only, no labels**. The wiki should treat this as the data-side mirror of [[dspy-evaluation-overview|the Evaluation Overview's]] *intermediate-step labels are almost never needed* commitment — together, the two commitments authorize a development style in which the user collects 20–200 *inputs* (no labels) and uses a **reference-free** metric (an [[llmasjudge|LLM-as-judge]] rubric or a heuristic on the output) to evaluate the program. This makes the data-collection cost of starting with DSPy genuinely small.

## Connections

- [[DSPy]] — the framework whose data primitive this page defines.
- [[dspy-learn-index]] — the three-stage Programming → Evaluation → Optimization model; this page is **page 10 of 13**, **second page** of the Evaluation stage.
- [[dspy-evaluation-overview]] — page 9; the Evaluation-stage entry point that forward-referenced this page to expand Step 1 of the iterative-evaluation loop into the [[DSPyExample|`dspy.Example`]] mechanics.
- [[DSPyEvaluation]] — the canonical concept for DSPy's evaluation philosophy; this page provides the data primitive every dev-set / train-set / test-set artifact decomposes to.
- [[DSPyData]] — the canonical concept page minted by this ingest for the dataset / split / data-handling convention.
- [[DSPyExample]] — the canonical concept page minted by this ingest for the `dspy.Example` data primitive itself.
- [[DSPyPrediction]] — the `Example`-subclass that [[DSPyModules|Modules]] return; shares the dot-access / `inputs()` / `labels()` surface, which is what makes the [[DSPyMetrics|metric]]'s `(example, prediction) -> score` contract type-symmetric.
- [[DSPyMetrics]] — **forward reference to page 11 of 13**; will consume both an `Example` (as ground truth) and a `Prediction` (as the system's output) under the `(example, prediction) -> score` signature. Owned by a sibling ingest.
- [[DSPyOptimizers]] — **forward reference to page 13 of 13**; trains on the dev set this page defines; the test set is held out for final assessment.
- [[DSPySignatures]] — the schema layer that names which fields an [[DSPyModules|Module]] consumes as inputs; the `Example.with_inputs(...)` call tags the matching fields on the data side. Together they wire the program to the data.
- [[DSPyModules]] — consumes the `inputs()`-view of an `Example` as kwargs to `forward(...)`; returns a [[DSPyPrediction|`Prediction`]] (an `Example` subclass).
- [[DSPyProgrammingModel]] — the separation-of-concerns philosophy this page extends to the data layer: data is *attached-tagged*, not structurally partitioned.
- [[ChainOfThought]] — produces a [[DSPyPrediction|`Prediction`]] whose `Example`-inherited surface lets `with_inputs(...)` / `inputs()` / `labels()` interoperate.
- [[react|ReAct]] — same.
- [[DSPyPredict]] — the strategy-side primitive paired with [[DSPyExample|`dspy.Example`]] as the data-side primitive.
- [[ModelEvaluation]] — the general wiki concept this DSPy-specific data discipline specializes; introduces the train/dev/test convention DSPy inherits.
- [[OfflineEvaluation]] — the regime DSPy's dev set operates in; the wiki's first concrete DSPy data primitive for offline evaluation.
- [[HuggingFace]] — named in [[dspy-evaluation-overview|the Evaluation Overview]] as a primary public-dataset source for the *"adjacent public datasets"* data-sourcing option; DSPy itself does not provide a loader — the user is expected to construct `list[dspy.Example]` from HuggingFace's `datasets.Dataset` manually.
- [[DevelopmentSet]] — the 20–200-example dev set [[dspy-evaluation-overview|the Evaluation Overview]] names; this page provides the concrete `list[dspy.Example]` shape it takes. Forward reference if not yet minted.
- [[Python]] — the host language whose `dict` and `list` primitives DSPy reuses for `Example` (dict-like) and dataset (list).
- [[PromptEngineering]] — the manual baseline DSPy displaces; in the manual workflow, "examples" are strings in a prompt template, not typed [[DSPyExample|`Example`]] objects with input-key tagging.
- [[dspy-programming-overview]] — page 2; the *"start simple, then grow"* discipline restated at the data layer: start with a few `Example`s, no labels, a reference-free metric, and grow the dataset/labels only when the metric demands it.
- [[dspy-modules]] — page 5; defines [[DSPyModules|Module]] and [[DSPyPrediction|Prediction]] (the `Example` subclass). This page completes the data-side pair.

## Contradictions

- **None new.** The Data Handling page is consistent with every prior DSPy ingest:
  - It **confirms** the [[dspy-learn-index|three-stage model]]'s ordering — data is collected during the Evaluation stage, after a runnable Programming-stage pipeline exists.
  - It **confirms** [[dspy-evaluation-overview|the Evaluation Overview's]] *intermediate-step labels are almost never needed* commitment by mirroring it at the data layer (*"at least a few example inputs"*).
  - It **extends** [[DSPyPrediction|the Prediction concept]] by establishing the parent-class relationship — `Prediction` is an `Example` subclass — which retroactively explains why a `Prediction`'s dot-access / field-attribute surface looks exactly like an `Example`'s. This was implicit in [[dspy-modules]] but is **named** here.
  - It **vindicates** [[DSPyProgrammingModel|the Programming Model's]] *small-API* discipline by introducing exactly **one** new class (`Example`) and **zero** dataset / loader / splitter classes on the data layer.
- **One framing nuance to track.** The page is silent on **how** the dev set is split from the train set and test set — *"DSPy is a machine learning framework, so working in it involves training sets, development sets, and test sets"* asserts the three-set convention but does not specify proportions, randomization, or stratification. The wiki should treat this as **deferred** rather than absent — likely to be addressed in [[DSPyOptimizers|the Optimizers page]] (page 13) where the train/dev distinction becomes operationally consequential (the Optimizer fits on the train set, the dev set picks the best candidate).
