---
title: "DSPy Data Handling"
type: concept
tags: [dspy, llm-programming, data, dataset, evaluation, training-set, development-set, test-set]
sources: [dspy-data, dspy-evaluation-overview, dspy-learn-index]
last_updated: 2026-05-24
---

# DSPy Data Handling

**DSPy Data Handling** is the data-collection-and-splitting discipline that operationalizes **Step 1** of [[DSPyEvaluation|DSPy's four-step iterative-evaluation loop]] — *"collect an initial development set."* The canonical source is the [[dspy-data|Data Handling]] page (page 10 of 13 of the *Learn* section); the discipline is the **dataset-layer** companion to [[DSPyExample|`dspy.Example`]] (the data-primitive layer).

Where [[DSPyExample]] records the individual datapoint, **DSPyData** records the conventions that govern collections of datapoints — the three-set (train / dev / test) convention DSPy inherits from supervised ML, the *"datasets are plain Python lists"* discipline, the *inputs-only sufficiency* commitment, and the interface to the next stage's [[DSPyOptimizers|Optimizers]] and [[DSPyMetrics|Metrics]].

## The framing commitment: DSPy is a machine learning framework

*"DSPy is a machine learning framework, so working in it involves training sets, development sets, and test sets."*

This is the opening commitment of the [[dspy-data|Data Handling]] page and a load-bearing claim. DSPy locates itself **inside** the supervised-ML tradition rather than presenting itself as a separate paradigm. The consequences:

- A [[DSPyOptimizers|DSPy Optimizer]] is **trained** on a training set the way an ML model is trained on a training set.
- A **development set** is held out for candidate-selection during optimization (which candidate program wins).
- A **test set** is held out for final assessment after optimization (what is the final score on data the search never saw).

The [[dspy-learn-index|three-stage model]] — Programming → Evaluation → Optimization — is **the ML-training cycle applied to LLM programs**: write the program (architecture), measure it (validate), tune it (train). The data-handling page is where that framing becomes operationally concrete.

## The three types of per-example values

*"For each example in your data, we distinguish typically between three types of values: the inputs, the intermediate labels, and the final label."*

| Value type | What it is | Required when |
|---|---|---|
| **Inputs** | The fields the program reads (e.g. `question`, `article`) | *Always.* At least a few example inputs are required. |
| **Intermediate labels** | Ground truth for intermediate steps (`reasoning`, `trajectory`) | *Almost never.* The metric scores final outputs; intermediate-step quality is the [[DSPyOptimizers|Optimizer's]] job to discover. |
| **Final labels** | Ground truth for the program's final output (`answer`, `summary`) | *Only when the metric is reference-based* (exact-match, F1, BLEU). Reference-free metrics ([[llmasjudge|LLM-as-judge]] over a rubric) need none. |

The typology interacts with the [[DSPyMetrics|metric]] (page 11): the **shape** of the data the developer collects is determined by the chosen metric, not by the model. This is the data-side mirror of [[dspy-evaluation-overview|the Evaluation Overview's]] claim *"Depending on your metric, you either just need inputs and no labels at all, or you need inputs and the final outputs of your system."*

## Inputs-only sufficiency

*"You can use DSPy effectively without any intermediate or final labels, but you will need at least a few example inputs."*

The minimum viable DSPy dataset is **inputs only, no labels**. This is a load-bearing data-collection commitment because it lowers the start-up cost of using DSPy for a new task:

- Collect 20–200 *inputs* (from a deployed demo, a manual labeling pass, an adjacent [[HuggingFace|HuggingFace]] dataset, or naturally-occurring StackExchange-style content).
- Write a reference-free metric (an [[llmasjudge|LLM-as-judge]] rubric or a heuristic on the output).
- Evaluate the program.

No final-label collection is required. This is the data-side mirror of [[dspy-evaluation-overview|the Evaluation Overview's]] *intermediate-step labels are almost never needed* commitment. Together, the two commitments authorize a development style in which the developer collects only inputs and uses an executable rubric to score the program's outputs.

## Datasets are plain Python lists

Unlike PyTorch (`torch.utils.data.Dataset`), TensorFlow (`tf.data.Dataset`), or HuggingFace (`datasets.Dataset`), **DSPy does not introduce a `Dataset` class**. A dataset is a plain `list[dspy.Example]`:

```python
trainset = [dspy.Example(report="LONG REPORT 1", summary="short summary 1"), ...]
```

The consequences:

- **Iteration / slicing / indexing / `len()`** are inherited from Python's list.
- **Train/dev/test splits are just slices**: `trainset = examples[:80]; devset = examples[80:100]; testset = examples[100:]`. The framework supplies no `train_test_split(...)` helper — the user is expected to use plain Python (or [[ScikitLearn|scikit-learn]]'s helper, or [[HuggingFace|HuggingFace]] `datasets.train_test_split`, or random.shuffle + slicing).
- **Shuffling / sampling / filtering** are plain `random.shuffle(...)`, `random.sample(...)`, list comprehensions.

This is consistent with [[dspy-modules|the Modules page's]] *"DSPy is just Python code"* discipline: the framework adds a class only when Python's built-ins don't fit. For datasets, lists fit.

The canonical idiom for converting external data into a DSPy dataset is the list comprehension:

```python
trainset = [dspy.Example(**row).with_inputs("question") for row in hf_dataset]
```

## The dev-set size regime

[[dspy-evaluation-overview|The Evaluation Overview]] committed the framework to a **20–200-example dev-set regime**: *"Even 20 input examples of your task can be useful, though 200 goes a long way."* This page does **not** restate the numbers, but its three-set framing presupposes them — a dev set of 50–200 `Example`s plus a held-out test set is the operational shape every later DSPy artifact assumes.

The 20-example floor is the smallest dev set that can usefully discriminate among pipeline designs and establish a baseline. The 200-example ceiling marks diminishing returns for dev-set-scale work — beyond that, additional labeling pays off mainly at the [[DSPyOptimizers|optimization]] stage (more training examples for the search to fit on) rather than the evaluation stage.

## Four ranked data-sourcing options

[[dspy-evaluation-overview|The Evaluation Overview]] lists four ranked options for collecting the initial development set. This concept page records them as the canonical data-acquisition protocol:

1. **Adjacent public datasets** — *"You can probably find datasets that are adjacent to your task on, say, [[HuggingFace|HuggingFace datasets]] or in a naturally occurring source like StackExchange."* This is the first-line option because it is the cheapest. The user constructs `[dspy.Example(**row).with_inputs(...) for row in hf_dataset]` to convert.
2. **Permissive-license re-use** — *"If there's data whose licenses are permissive enough, we suggest you use them."*
3. **Manual labeling** — *"you can label a few examples by hand."* Feasible at the 20–200 scale.
4. **Deployed-demo collection** — *"start deploying a demo of your system and collect initial data that way."* The user-facing instance of the program serves as a data-collection harness.

## Input/label tagging on the data side

DSPy's data layer uses [[DSPyExample|`with_inputs(...)`]] tagging rather than the structural `(X, y)` partition of conventional ML. The reasons (from the dataset-layer perspective):

- **Same `Example` for multiple program-call shapes.** A single `Example(article=..., summary=...)` can be tagged `.with_inputs("article")` for an article-to-summary program *and* `.with_inputs()` (no inputs — both fields are labels) for a metric that scores summary quality.
- **Functional update preserves the original.** `ex.with_inputs(...)` returns a new `Example`; the dataset can be re-tagged for different evaluations without copy/mutate gymnastics.
- **The metric layer can read both fields.** A [[DSPyMetrics|metric]] that takes `(example, prediction)` reads `example.answer` (ground truth) and `prediction.answer` (predicted) directly — the partition is for **program input**, not for **metric input**.

The discipline is **warn-not-fail**: tagging a label as an input (`with_inputs("question", "answer")`) is valid Python that silently leaks the answer. The framework prioritizes prototyping ergonomics over fences.

## The data-layer ↔ evaluation-layer interface

The next page in the *Learn* section ([[dspy-metrics]], page 11) will document the `(example, prediction) -> score` metric contract. This concept page makes the **data-side half** of that contract explicit:

| Metric kind | Required example fields |
|---|---|
| **Reference-free** (rubric / heuristic on the output alone) | Inputs only — `with_inputs("question")` style. |
| **Reference-based** (exact-match, F1, BLEU) | Inputs + final-output labels — `dspy.Example(question=..., answer=...).with_inputs("question")`. |
| **Multi-property DSPy-program metric** ([[llmasjudge|LLM-as-judge]]) | Inputs + optionally labels; the judge program may consume labels or be fully reference-free. |

The metric author reads `example.field` for ground truth; the program author passes `example.inputs()` as kwargs to `forward(...)`. Both views are derived from the *same* `Example` instance.

## The data-layer ↔ optimization-layer interface

The third page in the *Learn* section's Evaluation/Optimization arc ([[dspy-optimizers]], page 13, forward reference) will document how [[DSPyOptimizers|Optimizers]] consume datasets. This concept page makes the **data-side half** of that contract explicit:

- The **training set** is the `list[dspy.Example]` the Optimizer fits on. Each Example must have its inputs tagged with `.with_inputs(...)` so the Optimizer can pass them to the program under search.
- The **development set** is the held-out `list[dspy.Example]` the Optimizer uses to **select** the winning candidate program. Same tagging requirement.
- The **test set** is the further held-out `list[dspy.Example]` used **after** optimization to assess the final program. The Optimizer never sees this.

The Optimizer expects each Example to have inputs tagged because the search loop is essentially `for ex in trainset: prediction = program(**ex.inputs()); score = metric(ex, prediction)`. Without `.with_inputs(...)`, the framework cannot know which fields to pass to `forward(...)`.

## What DSPy does *not* introduce on the data layer

The deliberate scope-limit of the [[dspy-data|Data Handling]] page is consistent with DSPy's *small-API* discipline. The framework does **not** introduce:

- A `Dataset` class — datasets are `list[dspy.Example]`.
- A `train_test_split(...)` helper — splits are Python slicing.
- Loaders from HuggingFace / CSV / JSON — list comprehensions over external loaders.
- A `DataLoader` (batching / shuffling) — batching is the [[DSPyOptimizers|Optimizer's]] responsibility, not the dataset's.
- A `Dataset.with_inputs(...)` that broadcasts to all elements — the per-example `with_inputs(...)` is applied via list comprehension.

The framework adds **exactly one** class on the data layer: [[DSPyExample|`dspy.Example`]]. Everything else reuses Python.

## Three load-bearing commitments

The Data Handling page commits the framework to three non-trivial positions:

### Commitment 1: Datasets are plain Python lists

No `Dataset` class. The data layer reuses Python's `list` for collections and `dict`-like surface for elements (via `Example`). This is the *smallest possible API surface* compatible with the three-set discipline.

### Commitment 2: Input/label tagging is attached, not structural

`with_inputs(...)` adds metadata to an `Example`; it does not partition the data into `(X, y)`. The same `Example` can be tagged differently for different program calls. This is a richer model than conventional ML's structural tuples and is consistent with DSPy's *typed-but-loosely-coupled* discipline.

### Commitment 3: Inputs-only sufficiency

The minimum viable DSPy dataset is inputs alone, no labels. This is the data-side mirror of [[dspy-evaluation-overview|the Evaluation Overview's]] *intermediate-step labels are almost never needed* commitment. Together, the two commitments authorize a development style in which the data-collection cost is minimized — collect 20–200 inputs, write a reference-free rubric, evaluate the program.

## Position in the wiki

DSPy Data Handling sits between two adjacent wiki notions:

- **vs. [[ModelEvaluation]] (the general concept).** Model Evaluation is *"measuring model quality on a held-out set"* — a general ML notion. DSPyData specializes it to the DSPy-specific operational discipline (20–200-example dev set, `list[dspy.Example]` shape, `with_inputs(...)` tagging, inputs-only sufficiency).
- **vs. [[DSPyExample]] (the primitive).** DSPyData is the dataset-collection-and-splitting layer; [[DSPyExample]] is the per-datapoint layer. The two are paired the way [[DSPyModules]] (composition) is paired with [[DSPyPredict]] (the unit Module).

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-conversation-history]] — minimal conversational-task dataset shape: a `list[dspy.Example]` where each `Example` carries a `history` field plus the current-turn input; no train/dev/test split (Programming-stage-only tutorial).
- [[dspy-tutorial-classification-finetuning]] — full three-set discipline over Banking77: `DataLoader.from_huggingface(...)` → `[dspy.Example(x, label=CLASSES[x.label]).with_inputs("text") for x in ...]` + an **unlabeled** trainset variant for [[BootstrapFinetune|`dspy.BootstrapFinetune`]]; vindicates the *inputs-only sufficiency* commitment.

## Connections

- [[DSPy]] — the framework whose data-collection discipline this concept records.
- [[dspy-data]] — canonical source (page 10 of 13). Mints this page.
- [[DSPyExample]] — the per-datapoint primitive this concept's datasets are made of.
- [[DSPyEvaluation]] — the Evaluation stage; this concept expands Step 1 of the four-step iterative-evaluation loop.
- [[dspy-evaluation-overview]] — page 9; introduces the four-step loop, the 20–200-example dev-set regime, the four ranked data-sourcing options, and the intermediate-step-label exemption. This concept inherits all four from it.
- [[DSPyMetrics]] — forward reference to page 11; consumes `(example, prediction)` pairs. The data-shape requirements (inputs-only vs inputs+labels) are determined by the metric.
- [[DSPyOptimizers]] — forward reference to page 13; consumes the train/dev/test split this concept defines. The Optimizer fits on the train set, selects on the dev set, and is assessed on the test set.
- [[DSPyPrediction]] — the `Example`-subclass [[DSPyModules|Modules]] return; the metric's second argument.
- [[DSPyModules]] — consumes an `Example`'s `inputs()`-view as `forward(...)` kwargs.
- [[DSPySignatures]] — the schema layer that names which fields a Module's `forward(...)` expects; `Example.with_inputs(...)` tags the matching field names on the data side.
- [[DSPyProgrammingModel]] — the separation-of-concerns philosophy this discipline extends to the data layer.
- [[dspy-learn-index]] — the three-stage model whose Evaluation stage this concept's dataset discipline serves.
- [[HuggingFace]] — the primary public-dataset source for the *"adjacent public datasets"* sourcing option; the canonical conversion is `[dspy.Example(**row).with_inputs(...) for row in hf_dataset]`.
- [[DevelopmentSet]] — the 20–200-example dev set [[dspy-evaluation-overview]] names; this concept records the concrete `list[dspy.Example]` shape it takes. Forward reference if not yet minted.
- [[ModelEvaluation]] — the general concept this DSPy-specific discipline specializes; introduces the train/dev/test convention DSPy inherits.
- [[OfflineEvaluation]] — the regime DSPy data operates in; the wiki's first concrete DSPy data-collection discipline for offline evaluation.
- [[OnlineEvaluation]] — out of scope; the [[dspy-evaluation-overview|Evaluation Overview]] does not address live-traffic data collection.
- [[llmasjudge|LLM-as-judge]] — the long-form-task metric regime; works against inputs-only datasets, vindicating the inputs-only-sufficiency commitment.
- [[PromptEngineering]] — the manual baseline DSPy displaces; in the manual workflow, "examples" are strings in a prompt template, not typed `list[dspy.Example]` with input-key tagging.
- [[Python]] — the host language whose `list` primitive DSPy reuses for datasets; the lack of a DSPy `Dataset` class is intentional and reuses Python's iteration / slicing / `len()` directly.
- [[dspy-modules]] — page 5; defines [[DSPyPrediction|`dspy.Prediction`]] (the Module-return type). The metric reads ground truth from an `Example` and prediction from a `Prediction` — both share the [[DSPyExample|`Example`]] class hierarchy.
- [[dspy-programming-overview]] — page 2; the *"start simple, then grow"* discipline restated at the data layer.
