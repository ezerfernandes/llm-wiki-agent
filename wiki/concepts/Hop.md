---
title: "Hop"
type: concept
tags: [dspy, multi-hop, retrieval, program-pattern, chainofthought, hover]
sources: [dspy-multihop-search-tutorial]
last_updated: 2026-05-24
---

# Hop

**`Hop`** is the **4-hop generate-query / append-notes** [[DSPyModules|`dspy.Module`]] program introduced by [[dspy-multihop-search-tutorial|the official DSPy multi-hop search tutorial]] as the **canonical student program** for [[MIPROv2|`dspy.MIPROv2`]] prompt-optimization on [[HoVer]] three-hop claim verification. The **structural parent** of [[ResearchHop]] — `Hop` is the 4-hop / 10-docs-per-hop original; [[ResearchHop]] is the 2-hop / 4-docs-per-hop simplification tailored for [[ArborGRPO]] RL rollout budgets.

## Program shape

```python
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
```

`Hop(num_docs=10, num_hops=4)`: each hop retrieves 10 [[BM25|BM25]] documents; four hops total. **Every hop calls both sub-modules** — no first-hop bootstrap, no last-hop early-exit. Eight LM calls per `Hop(...)` invocation (4 × `generate_query` + 4 × `append_notes`).

## Two sub-Signatures

- **`generate_query`**: `(claim, notes) -> query` (no type annotations on outputs — string is inferred). Untyped inline-string [[DSPySignatures|Signature]] form.
- **`append_notes`**: `(claim, notes, context) -> new_notes: list[str], titles: list[str]`. **First wiki receipt of inline-string typed-output Signatures** — both output fields carry `list[str]` annotations. [[chainofthought|`dspy.ChainOfThought`]] respects the type contract during parsing.

## Distinguishing properties

### Every-hop query generation

Unlike [[ResearchHop]] (which uses the raw claim as hop-0 query: `query = (... if hop_idx else claim)`), `Hop` calls `self.generate_query(...)` on **every hop**, including hop 0 with `notes=[]`. This costs one extra LM call per example but lets the optimizer rewrite the first query — important when the claim's surface text is a poor BM25 query but a paraphrased version retrieves better. With MIPROv2 optimizing the `generate_query` Signature, this extra call is where part of the lift lives.

### Every-hop note appending

Unlike [[ResearchHop]] (which skips `append_notes` on the final hop), `Hop` calls `append_notes` on **every hop** including the last. The final-hop `append_notes` call is structurally wasted (the program returns the title list, not the notes; one more `append_notes` call doesn't add to retrieval) — but the tutorial keeps it for **uniform control flow**, which MIPROv2's instruction proposer benefits from (every hop is structurally identical, so one instruction set generalizes).

### Output-level title deduplication

`return dspy.Prediction(notes=notes, titles=list(set(titles)))` — the 4-hop loop accumulates a flat title list across hops, then deduplicates at the `forward` return. **First wiki receipt of program-level `list(set(...))` dedup inside a `dspy.Module.forward(...)` return.** The metric (`top5_recall`) consumes `pred.titles[:5]`, and the set conversion guarantees five **distinct** titles get evaluated rather than five potentially-duplicated retrievals.

Order is not preserved by `set(...)` — the `[:5]` slice picks an arbitrary five. This is acceptable for `top5_recall` because the metric is **set-membership-based** (gold-titles-in-retrieved-set), not rank-based.

### Typed output Signatures

`'... -> new_notes: list[str], titles: list[str]'` is the **terse middle path** between fully-untyped inline strings (`'claim, notes -> query'`) and full `dspy.Signature(...)` class bodies. Keeps the [[DSPyProgrammingModel|four-concerns decomposition]] intact (Signature still declared inline at module-construction time) while letting MIPROv2 propose instructions that respect the `list[str]` output contract.

## Hop vs ResearchHop — structural diff

| Axis | **`Hop`** ([[dspy-multihop-search-tutorial|this tutorial]]) | [[ResearchHop|`ResearchHop`]] ([[dspy-rl-multihop-tutorial]]) |
|---|---|---|
| `num_hops` default | **4** | 2 |
| `num_docs` default | **10** | 4 |
| LM calls per claim | **8** (4 × query + 4 × append-notes) | 3 (1 + 2 − 0 with hop-0 bootstrap + last-hop early-exit) |
| Hop-0 query | **`generate_query(...)`** with empty notes | **raw claim** (skip `generate_query`) |
| Last-hop append-notes | **called** | **skipped** |
| `append_notes` output | **`new_notes: list[str], titles: list[str]`** (typed) | `new_key_facts` (untyped string) |
| Title accumulation | **`titles` field in `append_notes` output** | **`doc.split(" | ")[0]`** at metric time |
| Output dedup | **`list(set(titles))` in `forward`** | none (handled by metric's `set(gold_titles)`) |
| Optimizer it serves | [[MIPROv2]] (prompt-space) | [[ArborGRPO]] (weight-space RL) |

The two programs are **non-trivially different student-program shapes** for the same task family. The choice between them is **optimizer-driven**: the larger LM-call budget of `Hop` is acceptable when prompt-optimizing (a few hundred MIPROv2 mini-batch evaluations) but prohibitive when collecting thousands of on-policy rollouts ([[ResearchHop]] cuts the rollout cost by ~63% per example).

## Reward integration via [[MIPROv2]]

The tutorial pairs `Hop` with the dual-mode `top5_recall` metric:

```python
def top5_recall(example, pred, trace=None):
    gold_titles = example.titles
    recall = sum(x in pred.titles[:5] for x in gold_titles) / len(gold_titles)
    if trace is not None:
        return recall >= 1.0  # bootstrap gate: only perfect-recall trajectories become demos
    return recall
```

MIPROv2 consumes this metric in **two modes**:
- During [[DSPyEvaluate|evaluation]] (`trace is None`): scalar `recall ∈ [0, 1]`.
- During **bootstrap-demo collection** (`trace is not None`): boolean `recall >= 1.0` — **only trajectories that retrieve every gold title in the top-5 become demos**. The perfect-recall gate is **stricter** than the typical `recall >= 0.5` threshold and reflects HoVer's three-gold-title structure (perfect recall is tractable).

## Position in DSPy program patterns

| Pattern | Example | Distinguishing feature |
|---|---|---|
| Free-form agent loop | [[dspy-tutorial-rag-as-agent|`dspy.ReAct(..., max_iters=20)`]] | LM chooses when to stop; tools as actions. |
| **Fixed-depth iterative retrieval (deep)** | **`Hop(num_docs=10, num_hops=4)`** | **8 LM calls; typed-output Signatures; output-level dedup.** |
| Fixed-depth iterative retrieval (shallow) | [[ResearchHop|`ResearchHop(num_docs=4, num_hops=2)`]] | 3 LM calls; untyped Signatures; metric-level dedup. |
| Single-shot CoT | [[dspy-tutorial-math]] | One sub-module, one call. |
| Multi-Signature pipeline | [[dspy-email-extraction-tutorial]] | Sequential diamond; not iterative. |

## Headline numbers

On [[HoVer]] three-hop subset (200 train / 300 dev / remainder test, `vincentkoc/hover-parquet`):

| Stage | top5_recall (devset) |
|---|---|
| Baseline (unoptimized Llama-3.1-8B) | 31.3% |
| After [[MIPROv2]] `auto="medium"` | **59.1%** |

1.89× relative lift on `$5 of GPT-4o` — the largest single-run MIPROv2 lift in the wiki's DSPy corpus for a multi-hop retrieval task with a >7B-parameter student.

## Connections

- [[DSPy]] / [[DSPyModules]] — host framework / module abstraction.
- [[chainofthought|`dspy.ChainOfThought`]] — the sub-module type used twice.
- [[DSPySignatures]] — **first wiki receipt of inline-string typed-output Signatures** (`'... -> new_notes: list[str], titles: list[str]'`).
- [[BM25]] / [[bm25s]] / [[PyStemmer]] — the retrieval substrate (same `bm25s.BM25(k1=0.9, b=0.4)` as [[ResearchHop]]'s receipt).
- [[MIPROv2]] — the optimizer this program is the canonical student of.
- [[BayesianOptimization]] — MIPROv2's search procedure.
- [[HoVer]] — the benchmark.
- [[MultiHopRAG]] — the architectural pattern `Hop` instantiates.
- [[MultiHopQA]] — task family.
- [[ResearchHop]] — the 2-hop simplification of this program (different optimizer target: [[ArborGRPO]]).
- [[dspy-multihop-search-tutorial]] — the canonical receipt.
- [[react|`dspy.ReAct`]] — the free-form-agent alternative used by [[dspy-tutorial-rag-as-agent]] on the same benchmark.
- [[dspy-custom-module]] — the 3-stage `generate_query → retrieve → generate_answer` RAG template; `Hop` is the **iterative extension** of that pattern with a typed-output append-notes step and output-level dedup.
- [[Llama|Llama-3.1-8B-Instruct]] — the student LM the tutorial trains.
- [[GPT4o]] — the proposer + teacher LM.
