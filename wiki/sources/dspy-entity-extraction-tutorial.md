---
title: "DSPy Tutorial — Entity Extraction"
type: source
tags: [dspy, tutorial, entity-extraction, ner, conll2003, mipro, chain-of-thought, optimization]
date: 2026-05-24
source_file: raw/dspy-entity-extraction-tutorial.md
---

## Summary

The [[DSPy]] **Entity Extraction** tutorial ([dspy.ai/tutorials/entity_extraction](https://dspy.ai/tutorials/entity_extraction/)) is the canonical source for **how [[DSPy]] frames a classical NLP token-classification task as an [[DSPyModules|LM-program]] optimized end-to-end against a metric**. The task is **person extraction from the [[CoNLL2003|CoNLL-2003]] dataset**: given a list of pre-tokenized words, return the subset that refer to specific people (CoNLL `ner_tags ∈ {1, 2}` — `B-PER` + `I-PER`). The tutorial demonstrates DSPy's complete program-evaluate-optimize loop on a **200-example test slice**: a [[DSPySignatures|Signature]] (`tokens: list[str] -> extracted_people: list[str]`) wrapped in [[ChainOfThought|`dspy.ChainOfThought`]] hits **86.0% exact-match** as a zero-shot baseline; **one pass of [[MIPROv2|`dspy.MIPROv2`]] with `auto="medium"` and `max_bootstrapped_demos=4`** lifts it to **93.0%** — a **+7-point absolute improvement** with no manual prompt engineering. Total LLM spend: **$0.26 USD** (LiteLLM-reported, `openai/gpt-4o-mini`).

This is the **first wiki-corpus page to scope DSPy at the classical-NLP token-classification application layer** — every prior DSPy ingest scoped either toy benchmarks ([[hotpotqa|HotPotQA]] / [[GSM8K]] / [[Iris]] / [[Banking77]]), conversational / agent shapes ([[dspy-conversation-history|chatbot]], [[dspy-customer-service-agent|customer-service agent]]), or research papers ([[2406.11695-mipro|MIPRO]] / [[2507.19457-gepa|GEPA]] / [[2312.13382-dspy-assertions|Assertions]]). The entity-extraction tutorial is the **NER-shaped counterpart** — same DSPy machinery, but the application is the canonical sequence-labeling task that [[NamedEntityRecognition|encoder-based NER]] (e.g., `bert-base-cased` + [[BIOTagging|BIO]] head, as in [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]) has owned for over two decades.

The tutorial is also the **only wiki-corpus DSPy receipt that uses [[CoNLL2003|CoNLL-2003]] as the eval surface** — the encoder-fine-tuning corpus uses CoNLL-2003 for [[FineTuningBert|BERT-style token classification]]; this tutorial uses it for **decoder-LM prompt-optimization** on the same dataset. The two approaches are now juxtaposable on the same benchmark.

## Key Claims

- **DSPy reframes NER as a list-in → list-out [[DSPySignatures|Signature]], not a per-token BIO-tag classification.** The [[DSPySignatures|Signature]] `tokens: list[str] -> extracted_people: list[str]` outputs the **subset** of input tokens that are persons — *"do not combine multiple tokens into a single value"* (signature docstring) — bypassing the [[BIOTagging|B-/I-/O- label scheme]] entirely. The model is responsible for token-level selection; the framework is responsible for typed I/O and prompt synthesis.

- **The four CoNLL `ner_tags` person codes collapse to two.** The tutorial's helper `extract_people_entities(...)` filters `ner_tag in (1, 2)` — the `B-PER` (1) and `I-PER` (2) codes — and returns the matching tokens; the other seven CoNLL codes (`O`, `B-ORG`, `I-ORG`, `B-LOC`, `I-LOC`, `B-MISC`, `I-MISC`) are not used. This is **task-narrowing**, not a CoNLL re-labeling: the same dataset can be re-sliced for organizations or locations by changing the tag filter.

- **The entire DSPy program is four lines of code.** Signature class (5 lines including docstring + two field declarations), `people_extractor = dspy.ChainOfThought(PeopleExtraction)`, `lm = dspy.LM(model="openai/gpt-4o-mini")`, `dspy.configure(lm=lm)`. No prompt template, no few-shot examples, no per-task tuning — DSPy synthesizes the prompt from the [[DSPySignatures|Signature]].

- **The metric is exact-match list equality.** `extraction_correctness_metric(example, prediction, trace=None) -> bool` returns `prediction.extracted_people == example.expected_extracted_people` — a strict ordered-list comparison. This is the **simple-metric** regime of [[dspy-metrics|page 11]]: a one-line scalar comparison, no LM-as-judge needed. **Trade-off**: case-mismatches and ordering differences count as failures (visible in the failure cases — row 0 `[CHINA]` expected, baseline returned `[JAPAN, CHINA]`; row 4 `[]` expected, baseline returned `[China, Uzbekistan]`).

- **Baseline 86.0% → MIPROv2 93.0% on 200-example test set.** The optimizer call is canonical [[MIPROv2|MIPROv2]]: `dspy.MIPROv2(metric=extraction_correctness_metric, auto="medium")` + `mipro_optimizer.compile(people_extractor, trainset=train_set, max_bootstrapped_demos=4, minibatch=False)`. The training set is the **first 50 examples** of CoNLL `train`; the test set is the **first 200 examples** of CoNLL `test`. The +7-point lift matches the **"can but doesn't" pattern** the [[2604.14585-prompt-optimization-coin-flip|2026 Coin-Flip framework]] formalizes: the LM zero-shot defaults to extracting any capitalized token (including countries — `JAPAN`, `CHINA`) regardless of person/non-person semantics; optimization installs the **"persons only, not locations or organizations"** discrimination that the LM has the capability for but doesn't default to.

- **MIPROv2 injects both instructions and few-shot demos.** The inspected optimized prompt (`dspy.inspect_history(n=1)`) shows MIPROv2 added a **rewritten task instruction** — *"In a high-stakes situation where accurate identification of individuals is critical for regulatory compliance and public health communication, extract contiguous tokens referring to specific people from the provided list of string tokens. Ensure that you output each identified individual as separate tokens..."* — and **four bootstrapped few-shot examples** (`max_bootstrapped_demos=4`). The instruction's domain framing (*"regulatory compliance and public health communication"*) is a synthesized proposer hallucination — the actual CoNLL-2003 data is mostly sports / financial / political news from 1996 Reuters — but the framing serves the structural goal of scoping the task to *persons only*. This is the [[MIPROv2|MIPROv2 jointly-optimizes-instructions-and-demos]] axis in action.

- **DSPy tracks LM cost via [[LiteLLM|LiteLLM]]'s pricing layer.** `cost = sum([x['cost'] for x in lm.history if x['cost'] is not None])` returns the per-call cost summed across the entire `lm.history` log — the same `lm.history` log [[DSPyLM|page 3 of *Learn*]] documented (`prompt / messages / kwargs / response / outputs / usage / cost / timestamp / uuid / model / response_model / model_type` fields). For this tutorial's full run (baseline eval + MIPROv2 compile + post-eval): **$0.26362742999999983 USD** on `openai/gpt-4o-mini`. Cost-tracking is **not** opt-in — DSPy populates `cost` automatically for every LM call routed through [[LiteLLM|LiteLLM]]-supported providers.

- **Optimized programs save as plain JSON.** `optimized_people_extractor.save("optimized_extractor.json")` writes the optimizer-tuned instructions + demos as a single JSON file. Loading is the dual: construct a fresh `dspy.ChainOfThought(PeopleExtraction)` then `.load(path)`. This is consistent with DSPy's [[DSPyProgrammingModel|*"writing code instead of strings"*]] discipline — the **optimized artifact is human-inspectable text**, not a binary blob. Same convention [[dspy-optimizers|page 13]] documented at the catalog level.

- **MLflow autolog is an opt-in, not a default.** Four-step setup (`pip install mlflow>=2.20` → `mlflow ui --port 5000` → `mlflow.set_tracking_uri(...)` + `mlflow.set_experiment("DSPy")` → `mlflow.dspy.autolog()`) enables trace visualization of every LM call inside the DSPy program. A second opt-in `with mlflow.start_run(run_name="extractor_evaluation"):` block enables persistent evaluation-result + score logging via `mlflow.log_metric("exact_match", result.score)` + `mlflow.log_table(...)`. Same [[MLflow|MLflow]] integration recipe [[dspy-custom-module|the Custom Module tutorial]] used; the entity-extraction tutorial confirms it's a cross-tutorial pattern, not Custom-Module-specific.

## Key Quotes

> *"This tutorial demonstrates how to perform entity extraction using the CoNLL-2003 dataset with DSPy. The focus is on extracting entities referring to people."* — opening scope statement; positions this as the canonical DSPy NER receipt.

> *"Extract contiguous tokens referring to specific people, if any, from a list of string tokens. Output a list of tokens. In other words, do not combine multiple tokens into a single value."* — the [[DSPySignatures|Signature]] docstring. The **"do not combine"** clause is the load-bearing instruction: it forces `["David", "Campese"]` output rather than `["David Campese"]` — token-level selection, not span-level extraction.

> *"DSPy includes powerful optimizers that can improve the quality of your system. Here, we use DSPy's MIPROv2 optimizer to: Automatically tune the program's language model (LM) prompt by 1. using the LM to adjust the prompt's instructions and 2. building few-shot examples from the training dataset that are augmented with reasoning generated from `dspy.ChainOfThought`."* — operational definition of [[MIPROv2|MIPROv2]] as **joint instruction + demo optimizer** — confirms the two-axis tuning the [[2406.11695-mipro|MIPRO paper]] formalized.

> *"After optimization, we re-evaluate the program on the test set to measure improvements... we see that accuracy of the program on the test dataset has improved significantly."* — baseline 86.0% → optimized 93.0%; +7 absolute points.

> *"DSPy allows you to track the cost of your programs. The following code demonstrates how to obtain the cost of all LM calls made by the DSPy extractor program so far."* — the cost-tracking surface is **explicitly documented as part of the DSPy programming model**, not a debugging afterthought.

> *"DSPy supports saving and loading programs, enabling you to reuse optimized systems without the need to re-optimize from scratch. This feature is especially useful for deploying your programs in production environments or sharing them with collaborators."* — the **production-deployment** framing of the save/load API.

> *"By leveraging structured inputs and outputs, we ensured that the system was easy to understand and improve. The optimization process allowed us to quickly improve performance without manually crafting prompts or tweaking parameters."* — the tutorial's closing thesis statement, restating the DSPy programming-model claim.

## Code Receipts

### Receipt 1 — Dataset preparation

```python
import os, tempfile
from datasets import load_dataset
import dspy

def load_conll_dataset() -> dict:
    with tempfile.TemporaryDirectory() as temp_dir:
        os.environ["HF_DATASETS_CACHE"] = temp_dir
        return load_dataset("conll2003", trust_remote_code=True)

def extract_people_entities(data_row):
    return [
        token
        for token, ner_tag in zip(data_row["tokens"], data_row["ner_tags"])
        if ner_tag in (1, 2)  # B-PER, I-PER
    ]

def prepare_dataset(data_split, start, end):
    return [
        dspy.Example(
            tokens=row["tokens"],
            expected_extracted_people=extract_people_entities(row),
        ).with_inputs("tokens")
        for row in data_split.select(range(start, end))
    ]

dataset = load_conll_dataset()
train_set = prepare_dataset(dataset["train"], 0, 50)
test_set  = prepare_dataset(dataset["test"], 0, 200)
```

### Receipt 2 — Program + LM

```python
class PeopleExtraction(dspy.Signature):
    """Extract contiguous tokens referring to specific people, if any, from a list of string tokens.
    Output a list of tokens. In other words, do not combine multiple tokens into a single value."""
    tokens: list[str] = dspy.InputField(desc="tokenized text")
    extracted_people: list[str] = dspy.OutputField(
        desc="all tokens referring to specific people extracted from the tokenized text"
    )

people_extractor = dspy.ChainOfThought(PeopleExtraction)
dspy.configure(lm=dspy.LM(model="openai/gpt-4o-mini"))
```

### Receipt 3 — Metric + eval harness

```python
def extraction_correctness_metric(example, prediction, trace=None) -> bool:
    return prediction.extracted_people == example.expected_extracted_people

evaluate_correctness = dspy.Evaluate(
    devset=test_set,
    metric=extraction_correctness_metric,
    num_threads=24,
    display_progress=True,
    display_table=True,
)

evaluate_correctness(people_extractor, devset=test_set)   # 86.0%
```

### Receipt 4 — MIPROv2 optimization

```python
mipro_optimizer = dspy.MIPROv2(
    metric=extraction_correctness_metric,
    auto="medium",
)
optimized_people_extractor = mipro_optimizer.compile(
    people_extractor,
    trainset=train_set,
    max_bootstrapped_demos=4,
    minibatch=False,
)
evaluate_correctness(optimized_people_extractor, devset=test_set)   # 93.0%
```

### Receipt 5 — Inspect + cost + save/load

```python
dspy.inspect_history(n=1)                                # shows optimized prompt + demos
cost = sum(x['cost'] for x in lm.history if x['cost'])   # $0.26 USD
optimized_people_extractor.save("optimized_extractor.json")

loaded = dspy.ChainOfThought(PeopleExtraction)
loaded.load("optimized_extractor.json")
loaded(tokens=["Italy", "recalled", "Marcello", "Cuttitta"]).extracted_people
# -> ['Marcello', 'Cuttitta']
```

## Connections

- **[[DSPy]]** — entity. Extends [[DSPy]]'s wiki footprint with a token-classification application slice — first DSPy receipt anchored to [[CoNLL2003|CoNLL-2003]].
- **[[CoNLL2003]]** — entity. Re-used as a benchmark — this time for **decoder-LM prompt optimization** rather than [[FineTuningBert|encoder fine-tuning]]. The juxtaposition with [[hands-on-llm-ch11-fine-tuning-representation-models|Ch 11 of *Hands-On LLMs*]] (BERT-base-cased on the same dataset) is now the wiki's first **encoder-vs-decoder-LM head-to-head receipt on a classical NER benchmark**.
- **[[NamedEntityRecognition]]** — concept. The task family. The DSPy framing — list-in / list-out, person-only, no [[BIOTagging|BIO]] head — is the **decoder-LM alternative** to the [[NamedEntityRecognition|encoder-NER]] template the wiki documents elsewhere.
- **[[EntityExtraction]]** — concept (newly minted). The umbrella for *"return the subset of input tokens / spans that mention an entity of interest"* as distinct from [[NamedEntityRecognition|NER]] (which traditionally assigns a label to **every** token). The DSPy tutorial scopes this surface.
- **[[ChainOfThought]]** — concept. The [[DSPyModules|Module]] the [[DSPySignatures|Signature]] is wrapped in. The tutorial demonstrates [[ChainOfThought|`dspy.ChainOfThought`]]'s **signature-expansion** behavior — the user declares `tokens -> extracted_people`, but the optimized prompt also produces a `rationale` field. Same mechanism [[dspy-modules|page 5]] documented.
- **[[MIPROv2]]** — concept. The optimizer applied. **+7-point lift from 86.0 → 93.0** on a 50-example training set with `auto="medium"` is added to the [[MIPROv2|MIPROv2 worked-receipts]] section alongside the [[2406.11695-mipro|MIPRO paper benchmark]] (HotPotQA / Iris / etc.) and the [[2025-bionlp-archehr-qa-neural|ArchEHR-QA clinical-QA]] receipt.
- **[[DSPySignatures]]** — concept. The `tokens: list[str] -> extracted_people: list[str]` Signature is the wiki's first **list-typed input + list-typed output** receipt. Confirms the [[dspy-signatures|five-tier type system]]'s `list[...]` `typing` composite tier is composable on both sides.
- **[[DSPyEvaluate]]** — concept. `dspy.Evaluate(devset=..., metric=..., num_threads=24, display_progress=True, display_table=True)` is the canonical four-kwarg construction signature [[dspy-metrics|page 11]] documents.
- **[[DSPyMetrics]]** — concept. `extraction_correctness_metric(example, prediction, trace=None) -> bool` is a **simple metric** in the [[dspy-metrics|page 11]] taxonomy — exact-match list equality, no LM-as-judge.
- **[[DSPyExample]]** — concept. `dspy.Example(tokens=..., expected_extracted_people=...).with_inputs("tokens")` is the canonical [[DSPyExample]] construction + input-tagging pattern.
- **[[DSPyLM]]** — concept. `dspy.LM(model="openai/gpt-4o-mini")` + `dspy.configure(lm=lm)` is the canonical [[DSPyLM]] global-bind pattern.
- **[[DSPyOptimization]]** — concept. The full **program → metric → training set → optimized program** loop [[dspy-optimization-overview|page 12]] formalized — this tutorial is a complete worked instance.
- **[[BayesianOptimization]]** — concept. The discrete-search procedure inside [[MIPROv2|MIPROv2]]. Not directly invoked at the API level — the user calls `dspy.MIPROv2(auto="medium")` and BO runs underneath.
- **[[PromptOptimization]]** — concept. The general framework [[MIPROv2|MIPROv2]] instantiates.
- **[[LiteLLM]]** — entity. The cost-tracking pricing data the `lm.history[i]['cost']` field reports comes from [[LiteLLM|LiteLLM]]'s pricing database.
- **[[MLflow]]** — entity. The opt-in tracing + experiment-tracking integration. `mlflow.dspy.autolog()` + `mlflow.dspy.log_model(...)` for program persistence with frozen environment metadata.
- **[[openai|OpenAI]]** — entity. `gpt-4o-mini` is the demo LM.
- **[[gpt-4o]]** — entity. The mini variant of the [[gpt-4o]] family.
- **[[HuggingFace]]** — entity. The `datasets` library is the data-access layer (`load_dataset("conll2003", trust_remote_code=True)`).
- **[[BIOTagging]]** — concept. The label scheme the tutorial **bypasses** — CoNLL stores `ner_tags` in BIO form, but the DSPy program never sees them as BIO; the `extract_people_entities` helper collapses `B-PER` + `I-PER` codes to a token-subset list before the DSPy program is invoked.
- **[[dspy-conversation-history]]**, **[[dspy-customer-service-agent]]** — sibling tutorials. This entity-extraction tutorial is the **third wiki-corpus DSPy tutorial** after these two; fills the **classical-NLP token-classification rung** in the DSPy application stack between **chatbot-state** and **agent-tools** rungs.
- **[[2406.11695-mipro|MIPRO paper]]** — the formal source for [[MIPROv2]]. The tutorial supplies a worked CoNLL-2003 instance of the algorithm the paper benchmarked on HotPotQA / Iris / etc.
- **[[2604.14585-prompt-optimization-coin-flip]]** — the [[CanButDoesntPattern|"can but doesn't" pattern]] paper. The +7-point lift here fits the pattern's predicted regime — the LM **can** distinguish persons from locations (Werner Zwingmann ✓; European Union ✗) but doesn't zero-shot default to that discrimination; MIPROv2 installs it.
- **[[hands-on-llm-ch11-fine-tuning-representation-models]]** — the wiki's encoder-NER receipt on the same [[CoNLL2003|CoNLL-2003]] dataset. The two pages now juxtapose **encoder-fine-tuning** and **decoder-LM prompt optimization** on identical data.
- **[[dspy-optimizers]]** — sibling. Page 13 of *Learn*; the catalog this tutorial picks one optimizer from.
- **[[dspy-metrics]]** — sibling. Page 11 of *Learn*; defines the metric-function contract this tutorial instantiates as `extraction_correctness_metric`.

## Contradictions

None with existing wiki content. The tutorial **complements** the corpus:

- The **86.0 → 93.0 +7-point lift** on a 200-example test set with 50 training examples is **within range** of the [[MIPROv2|MIPROv2 benchmark]] table on [[2406.11695-mipro|MIPRO]] (5/7 tasks improved by up to 13 absolute points on Llama-3-8B with GPT-3.5 as proposer) — no contradiction, just a different model pairing (`gpt-4o-mini` as both task LM and proposer).
- The cost-tracking surface (`lm.history[i]['cost']`) is consistent with the [[DSPyLM|page 3 of *Learn*]] disclosure that `lm.history` entries carry `cost` as one of their twelve fields — the tutorial supplies a worked sum-across-history pattern.
- The save/load surface (`optimized_extractor.json` plain-text JSON) is consistent with [[dspy-optimizers|page 13]]'s commitment that *"`optimized_program.save(path)` produces plain-text JSON — consistent with DSPy's writing-code-instead-of-strings discipline"*.

Soft tension: the tutorial's MIPROv2 synthesized instruction frames the task as *"In a high-stakes situation where accurate identification of individuals is critical for regulatory compliance and public health communication..."* — this is a **proposer hallucination** about task domain (CoNLL-2003 is 1996 Reuters news, not regulatory / health communication). This is not a tutorial error; it surfaces a known [[MIPROv2|MIPROv2]] proposer behavior — the [[LanguageModel|LM-proposer]] grounds prompt instructions in **plausible-sounding domain framings** that may not match the actual data, but the resulting prompts still optimize the metric. See the [[2604.14585-prompt-optimization-coin-flip|Coin-Flip]] discussion of *"why MIPRO succeeds when it does"* (output-structure scaffolding, not data-grounded semantics).

## Scope Limits

The tutorial is deliberately narrow. **Out of scope** (the tutorial does not address):

- **Span-level extraction** — the `do not combine multiple tokens` clause forces token-level output (`["David", "Campese"]`), not span-level (`["David Campese"]`). Span reconstruction (joining contiguous person tokens) is the developer's responsibility.
- **Other entity types** — only persons (`ner_tag ∈ {1, 2}`) are scoped. Organization / location / miscellaneous extraction is named in the *Next Steps* section but not implemented.
- **F1 / span-level evaluation** — the metric is **exact-list-match**, not [[seqeval|`seqeval`]] span-level F1 (the canonical [[CoNLL2003|CoNLL-2003]] eval metric). Strict list equality is harsher than F1 — case mismatches and order differences count as failures.
- **Generalization to longer sequences** — CoNLL-2003 sentences are short (often < 30 tokens). Performance on document-level extraction is not tested.
- **Comparison to encoder-NER baselines** — the tutorial does not benchmark against `bert-base-cased` + [[BIOTagging|BIO]] head on the same data. The [[hands-on-llm-ch11-fine-tuning-representation-models|Ch 11 of *Hands-On LLMs*]] page provides that comparison surface (encoder fine-tuning reports F1 in the 0.90–0.95 range on full CoNLL test set; this tutorial's 93.0% list-exact-match on a 200-example slice is **not** directly comparable due to the different metric).
- **Few-shot baselines** — the tutorial does not test [[BootstrapFewShot|`BootstrapFewShot`]] / [[BootstrapFewShotWithRandomSearch|BFRS]] as cheaper alternatives to [[MIPROv2|MIPROv2]] — the [[dspy-optimizers|page 13 rubric]] would recommend `BootstrapFewShot` for the 50-example training set; the tutorial jumps straight to [[MIPROv2|MIPROv2]] `auto="medium"`.
- **Multi-stage program** — the program is a **single [[ChainOfThought|CoT]] call**. Multi-stage extraction (e.g., NER then relation-extraction, or candidate-generation then filtering) is out of scope.
- **Cost-vs-quality Pareto** — the +7-point lift costs $0.26 (baseline eval + MIPROv2 compile + post-eval). The tutorial doesn't characterize the **marginal cost per accuracy point** or how it scales with `auto="light"` vs `"medium"` vs `"heavy"`.
- **MIPROv2 ablation** — instructions-only vs demos-only vs joint optimization is not tested. The [[2507.19457-gepa|GEPA]] paper argues instructions-only beats demos-only for instruction-following LMs in 2026; the tutorial doesn't engage that comparison.

## Position in the DSPy Tutorial Series

This is the **third tutorial-anchored** DSPy page in the wiki, after [[dspy-conversation-history]] (multi-turn chatbot state) and [[dspy-customer-service-agent]] (single-agent multi-tool task). It fills the **classical-NLP token-classification** rung:

| Application slice | DSPy primitives | Wiki anchor |
|---|---|---|
| Single LM call | [[DSPyPredict|`dspy.Predict`]] | [[dspy-modules]] |
| Single LM-program call | [[DSPyModules|`dspy.Module`]] subclass | [[dspy-modules]] |
| Multi-turn conversation | [[DSPyHistory|`dspy.History`]] in a Signature | [[dspy-conversation-history]] |
| **Classical-NLP token classification** | [[ChainOfThought|`dspy.ChainOfThought`]] + [[MIPROv2|`dspy.MIPROv2`]] + simple-metric | **this tutorial** |
| Single-agent multi-tool task | [[react|`dspy.ReAct`]] + 7-tool [[Pydantic]] domain | [[dspy-customer-service-agent]] |
| Multi-agent collaborative discourse | Custom multi-Module orchestration | [[2408.15232-co-storm|Co-STORM]] |
| Long-horizon RL'd agentic system | [[grpo|GRPO]] / [[GEPA]] over a [[CompoundAISystem|compound system]] | [[2407.10930-better-together]] / [[2507.19457-gepa]] |

The entity-extraction rung is the **simplest non-trivial DSPy optimization receipt in the corpus** — single [[DSPySignatures|Signature]], single Module, simple metric, single optimizer call — and now serves as the canonical *"DSPy 101"* shape for a classical-NLP task.
