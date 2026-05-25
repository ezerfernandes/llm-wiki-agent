---
title: "DSPy Tutorial — Retrieval-Augmented Generation"
type: source
tags: [dspy, tutorial, rag, mipro, optimization, semantic-f1, rag-qa-arena]
date: 2026-05-22
source_file: https://dspy.ai/tutorials/rag/
---

## Summary

**Fourth wiki-corpus [[DSPy]] tutorial** (after [[dspy-conversation-history]], [[dspy-customer-service-agent]], and [[dspy-custom-module]]) — and the **canonical end-to-end RAG receipt** for the framework: a three-stage walk from a baseline [[chainofthought|`dspy.ChainOfThought`]] (42% [[SemanticF1]]) → an embedding-retrieval [[rag|RAG]] module wrapping [[chainofthought|CoT]] over `k=5` retrieved technical documents (55.5%) → [[MIPROv2|`dspy.MIPROv2`]] `auto="medium"` joint instruction + demonstration optimization (61.1%). The tutorial is the **first wiki-corpus DSPy receipt to combine all four artifacts** ([[DSPySignatures|Signatures]] / [[DSPyModules|Modules]] / [[DSPyMetrics|Metrics]] / [[DSPyOptimizers|Optimizers]]) end-to-end on a single task, and the **first to ground the [[2406.11695-mipro|MIPRO paper's]] 53→61% RAG receipt** ([[MIPROv2]] catalog page) in a concrete dataset ([[RAGQAArenaTech]]) and embedding stack ([[openai|OpenAI]] `text-embedding-3-small` + truncated-to-6K-character technical corpus).

## Key Claims

- **Three-stage performance ladder**: baseline `dspy.ChainOfThought` ≈ **42%** [[SemanticF1|semantic F1]] → embedding-retrieval RAG module ≈ **55.5%** → MIPROv2-optimized RAG ≈ **61.1%**. The +13 / +6 split argues that **architecture** (RAG vs no-RAG) buys more than **optimization** (prompt search over the same RAG architecture) — but optimization on top of architecture is additive.
- **`SemanticF1` is an LLM-as-judge metric, not surface F1**. The metric measures *"how well system responses cover the key facts present in the gold-standard answers"* by decomposing each answer into atomic claims and grading recall + precision over claim coverage. This is an instance of [[dspy-metrics|the AI-feedback metric pattern]] (`class Assess(dspy.Signature)` + N `dspy.Predict(Assess)` invocations summed and thresholded).
- **The RAG corpus is 28,000 technical documents** downsampled from a larger set, each **truncated to 6,000 characters** to keep prompt envelopes bounded. Embeddings are pre-computed with [[openai|OpenAI]] `text-embedding-3-small`; top-`k=5` documents retrieved per query.
- **MIPROv2 `auto="medium"` is the recommended preset** for this scale (~1,000-example dataset, multi-stage RAG program). Optimization run: **~20–30 minutes, ~$1.50** — concrete instance of the [[dspy-optimizers|operating-cost ballpark]] DSPy's Optimizers page promises ($2 typical / cents-to-tens-of-dollars range).
- **Saving and loading**: optimized programs persist as **plain-text JSON** (`program.save("file.json")` / `dspy.load("file.json")`) — inspectable, diffable, version-controllable. Restates [[dspy-optimizers|the Optimizers page's]] *"The resulting file is in plain-text JSON format. ... You can always read it and see what the optimizer generated"* commitment.
- **Parallel evaluation**: `dspy.Evaluate(devset=..., metric=..., num_threads=24, display_progress=True, display_table=5)` — thread-parallel dev-set evaluation with progress display and inline tabular results. Operationalizes [[DSPyEvaluate|`dspy.Evaluate`]] at the worked-receipt level.
- **Cost tracking**: monitor expenses via the language model's `lm.history` ([[DSPyLM]]) — `sum([x['cost'] for x in lm.history if x['cost'] is not None])` and `dspy.Prediction.get_lm_usage()` (`dspy.configure(track_usage=True)`).
- **The further-improvement menu** the tutorial closes with names **five axes for going beyond 61.1%**: alternative system architectures (multi-hop retrieval), different optimizer families, **inference-time scaling through ensembling** ([[DSPyMajority|`dspy.majority`]]), **model distillation** to reduce serving cost ([[BootstrapFinetune|`dspy.BootstrapFinetune`]]), and **iterative metric refinement** based on actual system outputs (the [[DSPyEvaluation|recursive-self-improvement claim]] at the metric layer).

## Key Quotes

> *"DSPy is a machine learning framework... we'll build a small question-answering system on technical topics, starting from a basic predict and progressively adding retrieval and prompt optimization."*

> *"The metric `SemanticF1` measures how well the system response covers the key facts present in the gold-standard answer."*

> *"The RAG module retrieves the top 5 most relevant documents per query."*

> *"Optimization with `MIPROv2` typically requires 20–30 minutes and costs around $1.50."*

> *"Programs can be saved and loaded as JSON for reproducibility."*

> *"You can monitor expenses via the language model's history."* — context: `dspy.LM.history` per-call telemetry exposes `cost`, `usage`, `prompt`, `messages`, `outputs` for every call the program made.

## The three programs in order

### 1. Baseline — bare `dspy.ChainOfThought`

```python
import dspy

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

cot = dspy.ChainOfThought("question -> response")
cot(question="What is the role of a load balancer in a web application?")
```

A single LM call wrapped by [[chainofthought|`dspy.ChainOfThought`]] — adds a `reasoning` field but does **not** retrieve any documents. The tutorial uses this as the **42% [[SemanticF1|F1]] baseline** the RAG module has to beat.

### 2. RAG — `class RAG(dspy.Module)` with embedding retrieval

```python
class RAG(dspy.Module):
    def __init__(self, num_docs=5):
        self.num_docs = num_docs
        self.respond = dspy.ChainOfThought("context, question -> response")

    def forward(self, question):
        context = search(question, k=self.num_docs)   # top-k embedding retrieval
        return self.respond(context=context, question=question)
```

Embedding-retrieval RAG over the 28K downsampled technical corpus. The `search(...)` helper wraps [[openai|OpenAI]] `text-embedding-3-small` embeddings + a precomputed nearest-neighbor index ([[Faiss|FAISS]] optional). [[MIPROv2|Same architecture]] as Receipt 2 on [[dspy-optimizers|the Optimizers page]] (StackExchange corpus there; RAG-QA Arena Tech here). Reaches **~55.5% [[SemanticF1|F1]]** — a **+13 point** improvement over the baseline.

### 3. Optimized RAG — `dspy.MIPROv2(auto="medium")`

```python
from dspy.evaluate import SemanticF1

tp = dspy.MIPROv2(metric=SemanticF1(), auto="medium", num_threads=24)
optimized_rag = tp.compile(
    RAG(),
    trainset=trainset,
    max_bootstrapped_demos=2,
    max_labeled_demos=2,
)
optimized_rag.save("optimized_rag.json")
```

Joint instruction + demonstration tuning via [[MIPROv2|`dspy.MIPROv2`]] with [[BayesianOptimization|Bayesian Optimization]] (TPE surrogate) over the candidate space; **`auto="medium"`** preset (the mid-budget configuration between `light` and `heavy`). Reaches **~61.1% [[SemanticF1|F1]]** — a **+6 point** improvement on top of the un-optimized RAG, and a **+19 point** improvement over the baseline. Optimization run: ~20–30 min, ~$1.50.

## Dataset

**[[RAGQAArenaTech]]** — the *"Tech"* split of the [[RAGQAArena]] benchmark (Han et al., 2024). ~1,000 question-answer pairs over technical topics (programming, system administration, web development, etc.). The tutorial splits into:

| Split | Size | Role |
|---|---|---|
| Train | 200 | [[MIPROv2|MIPROv2]] training set + bootstrap-demo source |
| Dev | 300 | Metric tracking during optimization |
| Test | 500 | Held-out final evaluation |

The 200-example train + 300-example dev is below the [[dspy-optimization-overview|Optimization Overview's]] *300-example target* but above the **30-example floor** ("substantial value out of 30 examples"). Train/val = 200/300 ≈ **40/60** — closer to conventional ML than the page-12-recommended **20/80** prompt-optimization split, but within the same order of magnitude.

## Connections

- [[DSPy]] — the framework. The tutorial is the **fourth** DSPy tutorial in the corpus (after the three rung-2/3/4 application templates) and the **first to combine all four [[DSPyProgrammingModel|Programming-Model artifacts]] end-to-end** on a single task with measurable per-stage gains.
- [[rag|RAG]] — the canonical retrieval-augmented generation pattern; this is the wiki's **first DSPy RAG receipt anchored to a measurable benchmark with optimization** (the [[dspy-custom-module|Custom Module tutorial's]] RAG was a worked code listing without dev-set numbers; this one supplies the 42→55.5→61.1 progression).
- [[MIPROv2]] — the optimizer. The tutorial's 55.5→61.1 jump is the **second worked instance** of the Receipt 2 pattern from [[dspy-optimizers|the Optimizers page]] (the first was StackExchange 53→61); confirms the *"~$1.50, ~20–30 min, ~6 points"* operating envelope of `auto="medium"` on a multi-stage RAG program.
- [[SemanticF1]] — the metric. The tutorial is the **canonical worked source** for `dspy.evaluate.SemanticF1()`, an [[llmasjudge|LLM-as-judge]] [[DSPyMetrics|metric]] that decomposes each answer into atomic claims and grades coverage. Promoted from inline mention on [[MIPROv2]] / [[dspy-optimizers]] to a paper-anchored concept page.
- [[RAGQAArenaTech]] — the dataset. ~1K technical-domain QA pairs (Tech split of RAG-QA Arena); 200/300/500 train/dev/test.
- [[chainofthought|ChainOfThought]] — the substrate Module the tutorial wraps in both the baseline and the RAG program; the [[dspy-programming-overview|*start simple* default]] in action.
- [[DSPyModules]] — the `class RAG(dspy.Module)` shape (`__init__` + `forward` PyTorch contract); identical template to [[dspy-custom-module|the Custom Module tutorial]] and [[dspy-customer-service-agent|the Customer Service Agent]], applied to a measurable RAG benchmark.
- [[DSPyEvaluate]] — `dspy.Evaluate(devset=..., metric=..., num_threads=24)` parallel dev-set harness; canonical worked usage.
- [[DSPyMetrics]] — `SemanticF1` is a DSPy program ([[llmasjudge|LLM-as-judge]] rubric) and therefore **recursively optimizable** ([[DSPyEvaluation|Step 4]] of the four-step evaluation loop).
- [[BootstrapFinetune]] — named in the tutorial's *further improvements* menu as the **distillation path** for reducing serving cost after a working program is achieved; the [[dspy-optimizers|five-rule getting-started rubric's]] *post-success* slot.
- [[DSPyMajority]] — named in the *further improvements* menu as the **ensembling path** (inference-time scaling by sampling N reasoning paths and majority-voting).
- [[MLflow]] — the recommended tracing backend; the tutorial reiterates [[dspy-custom-module|the Custom Module tutorial's]] `mlflow.dspy.autolog()` opt-in for visualizing the multi-stage program's behavior.
- [[openai|OpenAI]] — provider for both the generation model (`gpt-4o-mini`) and the embedding model (`text-embedding-3-small`).
- [[ColBERTv2]] — the alternative retriever the [[dspy-custom-module|Custom Module tutorial]] uses (Wikipedia 2017 abstracts via the public endpoint); this RAG tutorial switches to dense [[openai|OpenAI]] embeddings + a local corpus instead.
- [[2604.14585-prompt-optimization-coin-flip]] — supplies the **2026 empirical caveat**: optimization helps reliably only on tasks with [[CanButDoesntPattern|exploitable output structure]] (the *"can but doesn't"* pattern); free-form QA may sit in the regime where optimization gains are fragile. The +6 RAG-tutorial gain is above the paper's 2-pt headroom threshold, so the tutorial's optimization win is consistent with the diagnostic — but the +6 is on a **specific** dataset / model / optimizer combination, and the [[ModelSpecificityShelfLife|model-specificity caveat]] applies.
- [[dspy-custom-module]] — sibling tutorial; established the `class RAG(dspy.Module)` template against a public Wikipedia retriever. This tutorial extends it to embedding retrieval + a measurable benchmark + optimization.
- [[dspy-conversation-history]] / [[dspy-customer-service-agent]] — the other two DSPy tutorials in the corpus; together with this RAG tutorial they cover the application stack rungs 2–4 plus the **optimization-with-metric** dimension that the application-template tutorials deferred.

## Contradictions

None with prior wiki content. The tutorial **strengthens** rather than weakens the [[MIPROv2|MIPROv2]] / [[2406.11695-mipro|MIPRO paper]] line — it is a second independent worked instance of the *"`auto="medium"` lifts a multi-stage RAG program by ~6 points for ~$1.50"* operating envelope. The [[2604.14585-prompt-optimization-coin-flip|coin-flip paper's]] caveat applies but is **not contradicted**: a +6 gain on a non-free-form claim-coverage metric is above the 2-pt headroom threshold the paper's diagnostic recommends as a precondition for invoking expensive optimization.
