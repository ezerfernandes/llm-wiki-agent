---
title: "DSPy Tutorial — Multi-Hop Search (MIPROv2 over HoVer with Llama-3.1-8B)"
type: source
tags: [dspy, tutorial, miprov2, multi-hop, hover, bm25, llama, gpt-4o, prompt-optimization, retrieval]
date: 2026-05-24
source_file: raw/dspy-multihop-search-tutorial.md
---

## Summary

Official [[DSPy]] tutorial at `https://dspy.ai/tutorials/multihop_search/` that demonstrates the **prompt-space joint optimization** of a fixed-depth multi-hop retrieval program ([[Hop]]) on the [[HoVer]] three-hop subset, using [[MIPROv2|`dspy.MIPROv2`]] with [[Llama|Llama-3.1-8B-Instruct]] as the student and [[GPT4o|GPT-4o]] as both the **instruction proposer** and the **bootstrap-demo teacher**. **Third wiki receipt of [[HoVer]] under a DSPy optimizer** — completes the prompt-vs-weight HoVer comparison table: [[dspy-tutorial-rag-as-agent|MIPROv2 over `dspy.ReAct`]] (Llama-3.2-3B, `top5_recall` 8 → 41.67), [[dspy-rl-multihop-tutorial|ArborGRPO over `ResearchHop`]] (Qwen2.5-1.5B, per-page recall 61.8 → 66.2), **this tutorial: MIPROv2 over `Hop` (Llama-3.1-8B, `top5_recall` 31.3 → 59.1)**. **Headline number**: ~$5 of GPT-4o calls lift Llama-3.1-8B from **31.3% → 59.1% top5_recall** (+27.8 pts, **1.89× relative**) on a 4-hop / 10-docs-per-hop retrieval program over a 5.2M-abstract 2017 Wikipedia [[BM25|BM25]] index. **First wiki receipts within this tutorial**: [[Hop]] as the **4-hop generate-query / append-notes program shape** with `list[str]` typed output fields (`new_notes: list[str], titles: list[str]`) — distinct from [[ResearchHop]]'s 2-hop string-field shape; `vincentkoc/hover-parquet` as the parquet-backed [[HoVer]] [[HuggingFace]] dataset variant (prior receipts used `hover-nlp/hover`); the **dual-mode metric protocol** where `top5_recall(...)` returns a float for `dspy.Evaluate` but `recall >= 1.0` (boolean) when `trace is not None` — the **bootstrap-only-perfect-recall** discipline that filters which trajectories become MIPROv2 demos; the **`prompt_model=gpt4o, teacher_settings=dict(lm=gpt4o)`** kwarg pair as the explicit two-role GPT-4o binding (proposer + teacher); `minibatch_size=40, minibatch_full_eval_steps=4` as the MIPROv2 Bayesian-search mini-batch schedule for this task; `max_bootstrapped_demos=4, max_labeled_demos=4` as the **balanced 4/4 demo budget** (vs the [[dspy-tutorial-rag-as-agent|RAG-as-agent tutorial's]] `max_bootstrapped_demos=3, max_labeled_demos=0`); the deduplicated 200/300/remainder split (vs prior receipts' 600/300/300 and 100/100/remainder); **inline string-form Signatures with typed output fields** (`'claim, notes, context -> new_notes: list[str], titles: list[str]'`) — first wiki receipt of typed-output inline syntax in a [[chainofthought|ChainOfThought]] call. **Thirteenth wiki-corpus DSPy tutorial**.

## Key Claims

- **`Hop(num_docs=10, num_hops=4)` is the canonical multi-hop search program shape in the official DSPy tutorial corpus.** Two [[chainofthought|`dspy.ChainOfThought`]] sub-modules (`generate_query` and `append_notes`) wired in a hop-loop `forward(...)`, same structural template as [[ResearchHop]] but with **four hops × ten documents** instead of two hops × four documents (10× the retrieval budget per call). The [[ResearchHop]] page is best read as **the 2-hop simplification of this 4-hop program**, designed for the smaller Qwen-1.5B student and the on-policy RL rollout budget; the original `Hop` retains the headroom of the larger Llama-3.1-8B prompt-optimization target.

- **Title deduplication happens at program output, not at retrieval time.** `return dspy.Prediction(notes=notes, titles=list(set(titles)))` — the 4-hop loop accumulates a flat title list across hops, then deduplicates at the end. This is the **first wiki receipt of program-level deduplication via `list(set(...))`** inside a `dspy.Module.forward(...)` return — the metric (`top5_recall`) consumes `pred.titles[:5]`, and the set conversion guarantees five **distinct** titles get evaluated rather than five potentially-duplicated retrievals.

- **The metric is the same dual-mode `top5_recall` as [[dspy-tutorial-rag-as-agent|the RAG-as-agent tutorial]] — but with `recall >= 1.0` as the bootstrap gate.** Both tutorials use the trace-based dual-return idiom (`if trace is not None: return recall >= 1.0`), and both gate bootstrap demos on **perfect recall** (every gold title appears in the top-5). This is the **MIPROv2-on-HoVer bootstrap discipline** — only fully-successful trajectories propagate into the demo bank, which **constrains demo quality at the cost of demo quantity**. Sibling DSPy tutorials with `recall >= 0.5` or `recall >= 0.7` would admit partially-successful trajectories; HoVer's three-gold-title structure makes perfect-recall a tractable gate.

- **GPT-4o plays both proposer and teacher roles in the same compile() call.** `models = dict(prompt_model=gpt4o, teacher_settings=dict(lm=gpt4o))` — the **first DSPy tutorial in the wiki to pass both `prompt_model` and `teacher_settings.lm` as the same model** in one `MIPROv2(...)` constructor. The two roles are conceptually distinct ([[MIPROv2]] uses `prompt_model` for the natural-language instruction proposer stage and `teacher_settings.lm` for the bootstrap-demo collection stage), but operationally collapsing them to GPT-4o is the **$5-budget rationalization**: one paid API surface covers both proposer cost (a few dozen instruction candidates) and teacher cost (a few dozen bootstrap rollouts on the train split).

- **The 4/4 balanced demo budget is the operational shape.** `max_bootstrapped_demos=4, max_labeled_demos=4` — four GPT-4o-generated demos and four train-set-label demos per Signature. Contrast: [[dspy-tutorial-rag-as-agent|the RAG-as-agent tutorial]] used `max_bootstrapped_demos=3, max_labeled_demos=0` (bootstrap-only). The 4+4 balance gives **eight in-context exemplars** per `Hop` sub-Signature — the upper end of the prompt-budget envelope MIPROv2 explores during Bayesian search.

- **`minibatch_size=40, minibatch_full_eval_steps=4` are the Bayesian-search schedule kwargs.** Mini-batches of 40 examples evaluate candidate (instruction, demo-set) tuples cheaply; every 4 mini-batch steps the top candidates get a full devset re-evaluation. This is the **first wiki receipt of the explicit `minibatch_size` / `minibatch_full_eval_steps` MIPROv2 surface** — prior MIPROv2 tutorials ([[dspy-tutorial-math]], [[dspy-rag-tutorial]], [[dspy-entity-extraction-tutorial]]) used `auto="medium"` without surfacing the mini-batch sub-controls.

- **`vincentkoc/hover-parquet` is the parquet-backed HoVer variant.** Distinct from `hover-nlp/hover` (used by [[dspy-rl-multihop-tutorial]]) — same upstream HoVer dataset but parquet-format for faster `DataLoader().from_huggingface(...)` ingestion. The `trust_remote_code=True` flag is required. The deduplication pattern `not hpqa_ids.add(x["hpqa_id"])` (using `set.add()`'s `None` return value to keep the comprehension condition truthy) is a **Python-idiomatic one-liner dedup** the tutorial reproduces verbatim from upstream DSPy examples.

- **The 200/300/remainder split is a deliberate budget point, not a sampling default.** 200 train (small enough for `$5` of GPT-4o calls), 300 dev (large enough for stable MIPROv2 mini-batch evaluation at `minibatch_size=40`), `hover[650:]` test (~1000+ examples — never evaluated in the tutorial but allocated for downstream use). The 150-example gap between dev-end (500) and test-start (650) is **deliberate buffer** — no documented rationale, but it prevents accidental dev/test leakage from off-by-N indexing bugs.

- **Inline string-form Signatures support typed output fields.** `dspy.ChainOfThought('claim, notes, context -> new_notes: list[str], titles: list[str]')` — first wiki receipt of **type annotations in inline-string Signatures inside a ChainOfThought call**. Prior receipts used either fully untyped strings (`'claim, notes -> query'`) or full `dspy.Signature(...)` class bodies for typed outputs. The inline typed-output form is the **terse middle path** — keeps the four-concerns decomposition intact ([[DSPySignatures|Signature]] still declared inline at module-construction time) while letting MIPROv2 propose instructions that respect the `list[str]` output contract.

- **First-hop bootstrap from the claim is absent here.** Unlike [[ResearchHop]] (which uses the raw claim as hop-0 query: `query = (... if hop_idx else claim)`), `Hop` calls `self.generate_query(...)` on **every hop**, including hop 0 with `notes=[]`. The trade-off: `Hop` spends one extra LM call per example (hop-0 query generation) but lets the optimizer rewrite the first query — important when the claim's surface text is a poor BM25 query but a paraphrased version retrieves better. With MIPROv2 optimizing the `generate_query` Signature, this extra call is **where the lift lives**.

- **Last-hop early-exit is absent here.** Unlike [[ResearchHop]] (which skips `append_notes` on the final hop), `Hop` calls `append_notes` on **every hop** including the last. Four hops → four `generate_query` + four `append_notes` = **eight LM calls per `Hop(...)` invocation**, vs [[ResearchHop]]'s three (two queries + one append-notes, with hop-0-query and last-append-notes skipped). The 8× LM-call budget per example is what allows the title list to grow to 40+ candidates before dedup — and what makes the **`top5_recall`** metric meaningful (the program can over-retrieve and let the program-level `list(set(titles))` + metric-level `[:5]` slice select the best).

- **The 31.3% → 59.1% lift is 1.89× — the largest single-run lift in the wiki's MIPROv2 corpus for a multi-hop retrieval task with a >7B student.** Comparable lifts: [[dspy-tutorial-math]] (74.0 → 88.57, 1.20×) on `gpt-4o-mini`; [[dspy-rag-tutorial]] (42 → 61.1, 1.46×) on `gpt-4o-mini`; [[dspy-tutorial-rag-as-agent]] (8 → 41.67, **5.21×** — the largest, but on a 3B student with a free-ranging ReAct loop that started near-zero). The 1.89× lift on a 4-hop fixed-shape program is **the headline data point for prompt-optimizing fixed-depth retrieval pipelines on mid-size open-weights models**.

- **The Llama-3.1-8B student pins the wiki's third DSPy student-size point.** Prior DSPy student sizes documented in the wiki: 1.5B ([[dspy-rl-multihop-tutorial]], [[dspy-tutorial-rl-papillon]]), 3B ([[dspy-tutorial-rag-as-agent]]), 8B (the [[2406.11695-mipro|MIPRO paper]], this tutorial), `gpt-4o-mini` (most other tutorials). The 1.5B / 3B / 8B / `gpt-4o-mini` ladder now has explicit MIPROv2 receipts at every rung.

- **The `bm25s` retriever is reused from [[dspy-rl-multihop-tutorial]] verbatim** (`k1=0.9, b=0.4` over the same 2017 Wikipedia abstracts). **The wiki now has two DSPy tutorials sharing one retriever stack** — strong evidence that `bm25s` is the default DSPy lightweight retrieval substrate for in-process corpus indexing on tutorial-scale corpora. Distinct from the network-bound [[ColBERTv2]] used by [[dspy-custom-module]] / [[dspy-tutorial-rag-as-agent]].

## Key Quotes

> *"we'll take a claim and produce a list titles: list[str]"* — on the program's I/O contract.

> *"make some $5 worth of calls to GPT-4o to optimize Llama-3.1-8B"* — on the prompt-optimization budget framing.

## Code Receipt — minimum reproducible program

```python
import dspy
import random
import bm25s, Stemmer
from dspy.datasets import DataLoader

lm = dspy.LM('<your_provider>/Llama-3.1-8B-Instruct', max_tokens=3000)
gpt4o = dspy.LM('openai/gpt-4o', max_tokens=3000)
dspy.configure(lm=lm)

# BM25S retriever over 5.2M Wikipedia 2017 abstracts
stemmer = Stemmer.Stemmer("english")
corpus_tokens = bm25s.tokenize(corpus, stopwords="en", stemmer=stemmer)
retriever = bm25s.BM25(k1=0.9, b=0.4)
retriever.index(corpus_tokens)

def search(query: str, k: int) -> list[str]:
    tokens = bm25s.tokenize(query, stopwords="en", stemmer=stemmer, show_progress=False)
    results, scores = retriever.retrieve(tokens, k=k, n_threads=1, show_progress=False)
    return {corpus[doc]: float(score) for doc, score in zip(results[0], scores[0])}

class Hop(dspy.Module):
    def __init__(self, num_docs=10, num_hops=4):
        self.num_docs, self.num_hops = num_docs, num_hops
        self.generate_query = dspy.ChainOfThought('claim, notes -> query')
        self.append_notes = dspy.ChainOfThought(
            'claim, notes, context -> new_notes: list[str], titles: list[str]')

    def forward(self, claim: str) -> list[str]:
        notes, titles = [], []
        for _ in range(self.num_hops):
            query = self.generate_query(claim=claim, notes=notes).query
            context = search(query, k=self.num_docs)
            prediction = self.append_notes(claim=claim, notes=notes, context=context)
            notes.extend(prediction.new_notes)
            titles.extend(prediction.titles)
        return dspy.Prediction(notes=notes, titles=list(set(titles)))

# HoVer 3-hop subset
kwargs = dict(fields=("claim", "supporting_facts", "hpqa_id", "num_hops"),
              input_keys=("claim",))
hover = DataLoader().from_huggingface(
    dataset_name="vincentkoc/hover-parquet", split="train",
    trust_remote_code=True, **kwargs)

hpqa_ids = set()
hover = [
    dspy.Example(claim=x.claim,
                 titles=list(set([y["key"] for y in x.supporting_facts]))).with_inputs("claim")
    for x in hover
    if x["num_hops"] == 3 and x["hpqa_id"] not in hpqa_ids
       and not hpqa_ids.add(x["hpqa_id"])
]
random.Random(0).shuffle(hover)
trainset, devset, testset = hover[:200], hover[200:500], hover[650:]

def top5_recall(example, pred, trace=None):
    gold_titles = example.titles
    recall = sum(x in pred.titles[:5] for x in gold_titles) / len(gold_titles)
    if trace is not None:
        return recall >= 1.0
    return recall

evaluate = dspy.Evaluate(devset=devset, metric=top5_recall, num_threads=16,
                          display_progress=True, display_table=5)

models = dict(prompt_model=gpt4o, teacher_settings=dict(lm=gpt4o))
tp = dspy.MIPROv2(metric=top5_recall, auto="medium", num_threads=16, **models)

kwargs = dict(minibatch_size=40, minibatch_full_eval_steps=4)
optimized = tp.compile(Hop(), trainset=trainset,
                       max_bootstrapped_demos=4, max_labeled_demos=4, **kwargs)
```

## HoVer Tutorial Trilogy — wiki state after this ingest

The wiki now hosts **three distinct HoVer DSPy receipts** spanning the prompt-vs-weight axis × program-shape axis:

| Axis | [[dspy-tutorial-rag-as-agent]] | **this tutorial** | [[dspy-rl-multihop-tutorial]] |
|---|---|---|---|
| Optimizer | [[MIPROv2]] `auto="medium"` + teacher | **[[MIPROv2]] `auto="medium"` + proposer + teacher** | [[ArborGRPO]] (DAPO, LoRA r=8) |
| Regime | prompt-space | **prompt-space** | weight-space (on-policy RL) |
| Program | `dspy.ReAct(..., max_iters=20)` | **`Hop(num_docs=10, num_hops=4)`** | [[ResearchHop|`ResearchHop(num_docs=4, num_hops=2)`]] |
| Sub-modules | 1 (ReAct loop) | **2 (`generate_query`, `append_notes`)** | 2 (`generate_query`, `append_notes`) |
| LM calls per claim | up to 20 (`max_iters`) | **8** (4 hops × 2 sub-modules) | 3 (2 queries − 1 bootstrap + 1 append-notes) |
| Student | [[Llama|Llama-3.2-3B-Instruct]] | **[[Llama|Llama-3.1-8B-Instruct]]** | [[Qwen|Qwen2.5-1.5B-Instruct]] |
| Teacher / proposer | GPT-4o (demos only) | **GPT-4o (demos + instructions)** | — (RL, no teacher) |
| Retriever | [[ColBERTv2]] (hosted) | **[[bm25s]] + [[PyStemmer]] (in-process)** | [[bm25s]] + [[PyStemmer]] (in-process) |
| Corpus | ColBERTv2 Wikipedia | **5.2M 2017 abstracts** | 5M 2017 abstracts |
| HoVer split | `hover-nlp/hover` 3-hop dedup, 100/100/rem | **`vincentkoc/hover-parquet` 3-hop dedup, 200/300/rem** | `hover-nlp/hover` 3-hop dedup, 600/300/300 |
| Metric | `top5_recall` (gold titles in top-5) | **`top5_recall` (gold titles in top-5)** | per-page title recall (gold ∩ retrieved / |gold|) |
| Bootstrap gate | `recall >= 0.5` | **`recall >= 1.0`** | — |
| Demo budget | `max_bootstrapped_demos=3, max_labeled_demos=0` | **`max_bootstrapped_demos=4, max_labeled_demos=4`** | `exclude_demos=True` |
| Baseline → optimized | **8 → 41.67** (5.21×) | **31.3 → 59.1** (1.89×) | 61.8 → 66.2 (1.07×) |
| Compute | cheap MIPROv2 run | **~$5 of GPT-4o** | ~18 h on 4 GPUs |

The trilogy operationalizes the [[2507.19457-gepa|GEPA paper's]] central thesis on the same benchmark: **prompt-space wins on cost/quality** on HoVer (the two MIPROv2 receipts deliver 5.21× and 1.89× lifts cheaply; the [[ArborGRPO|ArborGRPO]] receipt delivers 1.07× at 18 GPU-hours).

## Position in the DSPy Tutorial Corpus

**Thirteenth wiki-corpus DSPy tutorial.** Coverage along the **optimizer / training-regime axis** is now:

| Tutorial | Optimizer | Regime | Student | Task | Lift |
|---|---|---|---|---|---|
| [[dspy-tutorial-math]] | [[MIPROv2]] `auto="medium"` | prompt-space | gpt-4o-mini | MATH-algebra | 74.0 → 88.57 (1.20×) |
| [[dspy-rag-tutorial]] | [[MIPROv2]] `auto="medium"` | prompt-space | gpt-4o-mini | StackExchange RAG | 42 → 61.1 (1.46×) |
| [[dspy-entity-extraction-tutorial]] | [[MIPROv2]] `auto="medium"` | prompt-space | gpt-4o-mini | CoNLL-2003 NER | 86 → 93 (1.08×) |
| [[dspy-tutorial-rag-as-agent]] | [[MIPROv2]] `auto="medium"` + teacher | prompt-space | Llama-3.2-3B | HoVer ReAct | 8 → 41.67 (5.21×) |
| **dspy-multihop-search-tutorial** *(this page)* | **[[MIPROv2]] `auto="medium"` + proposer + teacher** | **prompt-space** | **Llama-3.1-8B** | **HoVer 4-hop `Hop`** | **31.3 → 59.1 (1.89×)** |
| [[dspy-tutorial-rl-papillon]] | [[ArborGRPO]] (DAPO, LoRA r=8) | weight-space (RL) | 1.5B local | PUPA / [[PAPILLON]] | 54.6 → 60.0 |
| [[dspy-rl-multihop-tutorial]] | [[ArborGRPO]] (DAPO, LoRA r=8) | weight-space (RL) | Qwen2.5-1.5B | HoVer 2-hop `ResearchHop` | 61.8 → 66.2 |

**What this tutorial uniquely contributes** to the DSPy tutorial corpus:

1. **Third HoVer receipt** — completes the prompt-vs-weight × program-shape comparison on a single benchmark.
2. **First MIPROv2 receipt with both `prompt_model` and `teacher_settings.lm` explicitly bound to the same model.**
3. **First wiki receipt of `minibatch_size=40, minibatch_full_eval_steps=4`** as configured MIPROv2 kwargs (vs `auto="medium"` defaults).
4. **First wiki receipt of `max_bootstrapped_demos=4, max_labeled_demos=4`** balanced demo budget.
5. **First wiki receipt of the [[Hop]] 4-hop / 10-docs program shape** with typed `list[str]` output Signatures.
6. **First wiki receipt of inline-string typed-output Signatures** (`'... -> new_notes: list[str], titles: list[str]'`) inside a [[chainofthought|`dspy.ChainOfThought`]] call.
7. **First wiki receipt of the `recall >= 1.0` perfect-recall bootstrap gate.**
8. **First wiki receipt of `vincentkoc/hover-parquet`** as the parquet-format HoVer variant.
9. **Second DSPy tutorial to reuse the `bm25s` + 2017 Wikipedia abstracts retrieval stack** (after [[dspy-rl-multihop-tutorial]]) — strong evidence the stack is the default DSPy lightweight retrieval substrate for tutorial-scale corpora.
10. **First wiki receipt of the `$5 of GPT-4o` budget framing** for MIPROv2 on a multi-hop retrieval task.
11. **Pins the 8B-parameter open-weights student-size point** in the DSPy tutorial corpus — fills the gap between the [[dspy-tutorial-rag-as-agent|3B (Llama-3.2)]] and [[2406.11695-mipro|paper-era 8B (Llama-3)]] rungs.

## Connections

- [[DSPy]] — the framework being demonstrated.
- [[chainofthought|`dspy.ChainOfThought`]] — the sub-module used twice inside `Hop`.
- [[DSPyModules]] — `Hop` is a `dspy.Module` subclass; **first wiki receipt of typed-output inline-string Signatures inside a ChainOfThought constructor call.**
- [[DSPySignatures]] — inline-string Signature form with `list[str]` type annotations.
- [[DSPyLM]] — `dspy.LM('<provider>/Llama-3.1-8B-Instruct', max_tokens=3000)` and `dspy.LM('openai/gpt-4o', max_tokens=3000)` are the two LM bindings.
- [[DSPyOptimizers]] / [[DSPyOptimization]] — the optimizer catalog.
- [[MIPROv2]] — the optimizer; this tutorial extends the wiki's MIPROv2 corpus with the explicit `prompt_model` / `teacher_settings.lm` pair, the `minibatch_size` / `minibatch_full_eval_steps` schedule kwargs, and the 4/4 balanced demo budget.
- [[BayesianOptimization]] — MIPROv2's discrete-search procedure that the mini-batch kwargs configure.
- [[DSPyMetrics]] — `top5_recall(example, pred, trace=None)` is a [[DSPyMetrics|DSPy metric]] with the dual-mode `if trace is not None` bootstrap-gate idiom.
- [[DSPyEvaluate]] — `dspy.Evaluate(devset=..., metric=top5_recall, ...)` is the evaluation harness.
- [[Hop]] — **new concept page.** The 4-hop generate-query / append-notes program shape introduced by this tutorial.
- [[ResearchHop]] — sibling 2-hop program from [[dspy-rl-multihop-tutorial]]; structural twin with smaller hop count and 4-doc-per-hop retrieval budget.
- [[HoVer]] — the benchmark; this tutorial uses the same 3-hop subset filter as both sibling HoVer tutorials but with a different HF source repo (`vincentkoc/hover-parquet`) and different split (200/300/remainder).
- [[BM25]] — the retriever family.
- [[bm25s]] — the Python BM25 implementation; **second wiki receipt** after [[dspy-rl-multihop-tutorial]] (same `k1=0.9, b=0.4` config, same 2017 Wikipedia corpus).
- [[PyStemmer]] — the C-backed snowball stemmer; second receipt.
- [[Llama|Llama-3.1-8B-Instruct]] — the student LM; first DSPy-tutorial receipt of this specific Llama-3.1 8B variant (vs the [[2406.11695-mipro|MIPRO paper's]] Llama-3-8B and [[dspy-tutorial-rag-as-agent|RAG-as-agent's]] Llama-3.2-3B).
- [[GPT4o]] — the proposer + teacher LM.
- [[HuggingFace]] — host of `vincentkoc/hover-parquet` and the Wikipedia abstracts corpus.
- [[MultiHopQA]] — task type.
- [[MultiHopRAG]] — the architectural pattern `Hop` instantiates (sequential queries, each depending on prior notes).
- [[dspy-data]] — the [[DSPy]] data API page; `DataLoader().from_huggingface(...)` is documented there.
- [[dspy-tutorial-rag-as-agent]] — sibling HoVer tutorial; uses [[MIPROv2]] over [[react|`dspy.ReAct`]] with a 3B student. The two MIPROv2-on-HoVer tutorials together establish the **program-shape sensitivity** of MIPROv2 lifts on the same benchmark.
- [[dspy-rl-multihop-tutorial]] — sibling HoVer tutorial; uses [[ArborGRPO]] over [[ResearchHop]] with a 1.5B student. The two-hop simplification of this tutorial's four-hop program.
- [[2406.11695-mipro]] — the MIPRO paper that introduced HoVer as the deepest-pipeline benchmark in the [[DSPyOptimizerBenchmark]] (4 modules, 4 LM calls). This tutorial's `Hop` is a **structural sibling** of the paper's 4-module HoVer pipeline (`num_hops=4` × 2 sub-modules = 8 LM calls — twice the paper's count, because the paper merged generate-query+append-notes into single hops).
- [[2507.19457-gepa]] — the GEPA paper that argues prompt-space optimizers beat GRPO on compound-AI-system tasks; this tutorial is the **clean operational evidence** for that thesis on HoVer (1.89× MIPROv2 lift vs 1.07× ArborGRPO lift on the same benchmark family).
- [[MLflow]] — referenced for autologging tracing.
- [[DSPySaving]] — referenced for program persistence.

## Contradictions

None with the existing wiki — the tutorial slots cleanly between [[dspy-tutorial-rag-as-agent]] (smaller student, smaller program) and [[2406.11695-mipro|the MIPRO paper]] (same student size, different program decomposition). One **historical reconciliation**: the [[ResearchHop]] page describes `ResearchHop` as **"the 2-hop generate-query / append-notes program"** — this tutorial reveals that the upstream design is `Hop(num_docs=10, num_hops=4)`, and `ResearchHop` is the simplified 2-hop variant tailored for the RL rollout budget. The [[ResearchHop]] concept page is updated with this lineage note.

## Scope-Limit Gaps

- **No test-set evaluation.** The 31.3% → 59.1% lift is **devset**; testset is allocated (`hover[650:]`) but never evaluated. Same dev-selection-bias risk as [[dspy-rl-multihop-tutorial]].
- **No ablation on `num_hops` / `num_docs`.** `num_docs=10, num_hops=4` is presented as a default; the tutorial doesn't show the 2-hop or 8-hop sensitivity.
- **No comparison to [[ResearchHop]] on the same dataset / split.** The 2-hop simplification would be a useful upper-bound check on the MIPROv2 lift's program-shape dependence.
- **No comparison to [[dspy-tutorial-rag-as-agent|the RAG-as-agent tutorial's]] ReAct-loop variant on Llama-3.1-8B.** ReAct on the larger student model would clarify how much of `Hop`'s lift comes from the fixed-shape control flow vs the larger student.
- **`$5 of GPT-4o`** is a budget rationalization, not an itemized cost. No per-stage breakdown (proposer cost vs teacher-bootstrap cost vs Bayesian-search mini-batch cost), no wall-clock disclosure, no token-count comparison to the [[dspy-rl-multihop-tutorial|18-h 4-GPU GRPO run]].
- **No streaming / observability integration.** [[DSPyStreaming]] and [[DSPyObservability]] composing over `Hop` is not exercised.
- **No deployment recipe.** The optimized `Hop` is called once on `devset[0]` for a sample output; no `program.save(...)` / `dspy.load(...)` round-trip, no MLflow logging beyond the autolog reference, no serving recipe.
- **No data-leakage / contamination check.** Llama-3.1-8B's pretraining data plausibly includes the [[HoVer]] dataset and the 2017 Wikipedia dump; the 31.3% baseline could include memorized title recall.
- **No discussion of why `vincentkoc/hover-parquet` is preferred over the canonical `hover-nlp/hover`.** Likely parquet-format speed, but the tutorial does not surface the rationale.
- **No reward-shaping discussion.** `top5_recall` is binary at depth 5; no smoothed @-k variant, no penalty for redundant retrieval calls across hops, no per-hop credit decomposition.
- **No exploration of the `prompt_model != teacher_settings.lm` asymmetric case.** The tutorial collapses both to GPT-4o; a smaller/cheaper proposer (e.g., Llama-3.1-70B for instructions, GPT-4o only for bootstrap demos) is unexplored.
