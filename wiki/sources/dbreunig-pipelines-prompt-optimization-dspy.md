---
title: "Pipelines & Prompt Optimization with DSPy (Breunig 2024)"
type: source
tags: [dspy, mipro, prompt-optimization, ollama, llama, tutorial, blog-post, classification, third-party]
date: 2024-12-12
source_file: raw/dbreunig-pipelines-prompt-optimization-dspy.md
sources: []
last_updated: 2026-05-24
---

# Pipelines & Prompt Optimization with DSPy — Drew Breunig (2024-12-12)

A **practitioner blog post** by [[DrewBreunig|Drew Breunig]] walking through [[DSPy]] end-to-end on a historic-event classification task with [[MIPROv2|`dspy.MIPROv2`]] over a fully **local-laptop** stack ([[Ollama]] + [[Llama|Llama 3.2 1b]] as the task LM, [[Llama|Llama 3.3 70b]] as the prompt-proposer and the synthetic-trainset generator). The **first wiki-corpus third-party DSPy tutorial** (the prior DSPy corpus is Stanford's own *Learn* docs plus academic papers), and the **first DSPy receipt in the wiki to run entirely on local Ollama models** — every prior worked receipt ([[dspy-optimizers|Optimizers]] page's HotPotQA/StackExchange, [[dspy-rag-tutorial|RAG tutorial]]'s RAG-QA Arena Tech) used [[openai|OpenAI]] `gpt-4o-mini` as the task LM.

## Summary

Breunig found [[DSPy]] while looking for a framework to build a small agent for his weather-forecasting site. He demonstrates DSPy on a single small task — categorizing Wikipedia-sourced historic-event descriptions into 11 fixed buckets — and shows that [[MIPROv2|`dspy.MIPROv2`]] with `auto="light"` and `max_bootstrapped_demos=0, max_labeled_demos=0` (the **0-shot mode** the [[dspy-optimizers|Optimizers page]] documents) lifts [[Llama|Llama 3.2 1b]]'s accuracy from **51.9% → 63.0%**, by writing task-specific context into the system prompt. He then runs a **two-model variant** — `prompt_model=Llama 3.3, task_model=Llama 3.2 1b` — that reduces overfitting and produces qualitatively better instructions at slightly lower numerical accuracy (**62%**). Final pitch: *"there's something really clean and freeing about ceding the details and nuance of the prompt back to an LLM."*

## Key Claims

- **DSPy reframes prompting as programming** — *"the framework for programming—rather than prompting—language models"* — letting users describe inputs/outputs declaratively and letting the framework synthesize the actual prompt. (Matches [[DSPyProgrammingModel|the Programming Model's]] *"writing code instead of strings"* thesis.)
- **The class-based [[DSPySignatures|Signature]] + `typing.Literal[...]` enum is the idiomatic DSPy classification pattern** — Breunig's `Categorize` Signature declares `category: Literal["Wars and Conflicts", ..., "Famous Personalities and Achievements"] = dspy.OutputField()` plus a `confidence: float = dspy.OutputField()`. The [[DSPySignatures|Signatures page]] documents `typing.Literal` as the canonical closed-set-classification idiom; this is a worked third-party application of it.
- **[[DSPyPredict|`dspy.Predict`]] generates the system + user prompts automatically** — Breunig dumps the generated prompt to show the user that DSPy ships a full instruction block ("Given the fields `event`, produce the fields `category`, `confidence`. Follow the following format: ..."), with no human prompt-writing required. Concrete demonstration of the [[DSPyPredict|`Predict`-as-minimal-primitive]] claim.
- **Small open-weight models can be brought up by optimization rather than by model swap.** [[Llama|Llama 3.2 1b]] starts at **51.9%** accuracy on the task; [[Llama|Llama 3.3 70b]] is higher but **~10× slower**. The performance gap reflected *"the smaller model's limited contextual knowledge rather than prompting deficiencies"* — i.e., the small model knew the task but lacked the world knowledge to identify obscure events. [[MIPROv2|`dspy.MIPROv2`]] closed roughly half the gap by injecting task-specific context into the prompt (**51.9% → 63.0%**).
- **The `prompt_model` / `task_model` split is a load-bearing API knob.** Passing `prompt_model=` (large model used to draft candidate instructions) separately from `task_model=` (small model the candidates are evaluated against) **reduces overfitting** and yields *"more generalizable prompting instructions"*. This is a [[MIPROv2|MIPROv2]] feature the existing wiki MIPRO pages did not document explicitly — Breunig is the corpus's canonical receipt for it.
- **Synthetic trainsets from a larger LM are a viable bootstrap path** — Breunig generated his **300-example** trainset by running [[Llama|Llama 3.3 70b]] over Wikipedia event descriptions and used its outputs as ground truth, then trained the 1b model against that. Matches the [[dspy-optimization-overview|Optimization Overview's]] *"aim for at least 300 examples"* target and adds a synthetic-data-generation pattern.
- **The 0-shot MIPROv2 mode is invoked via `max_labeled_demos=0, max_bootstrapped_demos=0`.** Concrete confirmation of the [[dspy-optimizers|Optimizers page's]] *"If you prefer to do instruction optimization only (i.e., you want to keep your prompt 0-shot), use `MIPROv2` configured for 0-shot optimization"* rubric — the configuration is exactly these two kwargs set to zero.
- **`auto="light"` is enough to see real gains on a single-stage classifier.** The [[dspy-optimizers|Optimizers page]] uses `auto="light"` for the HotPotQA receipt (24%→51%) and `auto="medium"` for the RAG receipt (53%→61%); Breunig's `auto="light"` on a simpler single-Module classifier (51.9%→63.0%) further confirms the budget-vs-task-complexity heuristic.
- **Optimized programs persist as plain-text JSON** — `optimized_classify.save("optimized_event_classifier.json")` — matches the [[dspy-optimizers|Optimizers page's]] *"The resulting file is in plain-text JSON format. ... You can always read it and see what the optimizer generated"* inspectability commitment.

## Key Quotes

> *"DSPy: the framework for programming—rather than prompting—language models."* — DSPy's tagline, the framing Breunig anchors the post on.

> *"There's something really clean and freeing about ceding the details and nuance of the prompt back to an LLM."* — Breunig, closing pitch.

> *"The performance gap reflected the smaller model's limited contextual knowledge rather than prompting deficiencies."* — Breunig's diagnostic for why a bigger model beat the small one on accuracy. **The contrapositive licenses the optimization play**: if the gap were prompting-only, [[MIPROv2|MIPROv2]] would close more of it.

## Code receipts on the page

### Receipt 1 — Single-model `Predict` baseline

```python
import dspy
from typing import Literal

lm = dspy.LM('ollama_chat/llama3.2:1b', api_base='http://localhost:11434')
dspy.configure(lm=lm)

class Categorize(dspy.Signature):
    """Classify historic events."""
    event: str = dspy.InputField()
    category: Literal[
        "Wars and Conflicts", "Politics and Governance", "Science and Innovation",
        "Cultural and Artistic Movements", "Exploration and Discovery", "Economic Events",
        "Social Movements", "Man-Made Disasters and Accidents",
        "Natural Disasters and Climate", "Sports and Entertainment",
        "Famous Personalities and Achievements"
    ] = dspy.OutputField()
    confidence: float = dspy.OutputField()

classify = dspy.Predict(Categorize)
```

→ **51.9%** accuracy on the task (Llama 3.2 1b, no optimization).

### Receipt 2 — Single-model 0-shot [[MIPROv2|MIPROv2]] optimization

```python
def validate_category(example, prediction, trace=None):
    return prediction.category == example.category

tp = dspy.MIPROv2(metric=validate_category, auto="light")
optimized_classify = tp.compile(classify, trainset=trainset,
                                max_labeled_demos=0,
                                max_bootstrapped_demos=0)
```

→ **63.0%** accuracy (Llama 3.2 1b, MIPROv2 light, 0-shot mode). +11.1 absolute. Some overfitting noted.

### Receipt 3 — Two-model 0-shot MIPROv2 (small evaluator, large proposer)

```python
lm = dspy.LM('ollama_chat/llama3.2:1b', api_base='http://localhost:11434')
prompt_gen_lm = dspy.LM('ollama_chat/llama3.3', api_base='http://localhost:11434')

tp = dspy.MIPROv2(metric=validate_category, auto="light",
                  prompt_model=prompt_gen_lm, task_model=lm)
optimized_classify = tp.compile(classify, trainset=trainset,
                                max_labeled_demos=0,
                                max_bootstrapped_demos=0)
```

→ **62%** accuracy. Slightly lower numerical score than Receipt 2, but *qualitatively better* and more generalizable instructions; less overfitting.

### Receipt 4 — Persist the optimized program

```python
optimized_classify.save("optimized_event_classifier.json")
```

## Connections

- [[DSPy]] — the framework. This is the **first third-party DSPy tutorial in the wiki**, complementing the Stanford *Learn* corpus and DSPy-anchored academic papers.
- [[DrewBreunig]] — the author. New entity minted by this ingest.
- [[Ollama]] — the local-laptop runtime; **first wiki receipt to run a full MIPROv2 optimization loop entirely against Ollama-hosted models** (no managed-API calls).
- [[Llama]] — both LMs in the receipts are Llama 3.x via Ollama (`llama3.2:1b` task model, `llama3.3` prompt-proposer).
- [[DSPyLM]] — the `dspy.LM('ollama_chat/...')` client construction matches [[dspy-language-models|the Language Models page]]'s local-laptop regime exactly.
- [[DSPySignatures]] — the class-based `Categorize` Signature with `typing.Literal[...]` enum is a worked instance of the [[DSPySignatures|Signatures page]]'s closed-set-classification idiom.
- [[DSPyPredict]] — `dspy.Predict(Categorize)` is the minimal primitive Breunig builds on; the post's prompt-dump demonstrates the [[DSPyPredict|`Predict`-generates-the-system-prompt]] mechanism for a third-party audience.
- [[DSPyModules]] — `dspy.Predict` is the foundational Module the post uses; no composition into a bigger `dspy.Module` subclass — single-stage program.
- [[DSPyMetrics]] — `validate_category(example, prediction, trace=None) -> bool` matches the canonical `(example, pred, trace=None) -> score` contract from [[dspy-metrics|the Metrics page]]; the `trace=None` default and `bool` return type are exactly what [[MIPROv2|MIPROv2]]'s dual-purpose `trace` argument expects.
- [[MIPROv2]] — the optimizer used in Receipts 2 and 3. **Adds a new receipt to the wiki's MIPROv2 catalog**: single-stage classifier, 0-shot mode, `auto="light"`, on local Ollama, **51.9% → 63.0%** (Llama 3.2 1b). Also documents the `prompt_model=` / `task_model=` kwarg split as a real MIPROv2 API surface — a detail not previously surfaced in the wiki's MIPRO pages.
- [[DSPyOptimizers]] — confirms the catalog's *"0-shot prompts → `MIPROv2` (0-shot mode)"* rule via `max_labeled_demos=0, max_bootstrapped_demos=0`; confirms the *plain-text JSON save/load* commitment via `optimized_classify.save("optimized_event_classifier.json")`.
- [[DSPyOptimization]] — Breunig's **300-example synthetic trainset generated by a larger LM** is a worked instance of the [[dspy-optimization-overview|Optimization Overview's]] *"aim for at least 300 examples"* target and supplies a synthetic-data-generation pattern not previously surfaced.
- [[DSPyProgrammingModel]] — the post is structured around the *"writing code instead of strings"* thesis; the prompt-dump receipt is the most accessible explanation of the framework's four-concern decomposition the wiki has from a third-party author.
- [[PromptOptimization]] — concrete third-party demonstration that optimization can substitute for model-size scaling in the narrow case where the gap is prompting-knowable.
- [[FewShotLearning]] — Breunig deliberately *opts out* of few-shot demos (`max_bootstrapped_demos=0, max_labeled_demos=0`) — i.e., the post is the wiki's clearest receipt of MIPROv2 used in **pure-instruction-tuning** mode without any demo-side parameter.

## Contradictions

- None with the existing wiki. The post is a **practitioner-level receipt** that adds confirmations and new code examples without contradicting any [[DSPy]] / [[MIPROv2]] / [[DSPyOptimization]] / [[DSPyOptimizers]] claim. The numerical results (Llama 3.2 1b lifted from 51.9% to 63.0% on an open-class classification task with `auto="light"`) sit comfortably inside the existing receipt envelopes ([[MIPROv2|MIPROv2 Receipt 1]]: HotPotQA 24%→51%, `auto="light"`; [[MIPROv2|Receipt 2]]: RAG 53%→61%, `auto="medium"`).

## Open questions the post does not answer

- **What was the prompt that the optimization produced?** Breunig describes qualitative improvements in the two-model variant's prompt but does not include the final optimized instruction string in the post. Would be useful for a future ingest of the underlying repo/notebook.
- **How much did the optimization cost (wall-clock + token volume)?** No timing data for the MIPROv2 runs, only for the per-call inference difference between Llama 3.2 1b and Llama 3.3 70b.
- **Why does Receipt 3 score lower than Receipt 2 numerically?** Breunig attributes this to reduced overfitting on the validation set, but does not show a held-out test set comparison that would back the *"more generalizable"* claim quantitatively.
