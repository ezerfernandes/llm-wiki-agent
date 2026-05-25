---
title: "ResearchHop"
type: concept
tags: [dspy, multi-hop, retrieval, program-pattern, chainofthought]
sources: [dspy-rl-multihop-tutorial, dspy-multihop-search-tutorial]
last_updated: 2026-05-24
---

# ResearchHop

**`ResearchHop`** is the 2-hop generate-query / append-notes [[DSPyModules|`dspy.Module`]] program introduced by [[dspy-rl-multihop-tutorial|the DSPy `rl_multihop` tutorial]] as the **student program** for online [[grpo|GRPO]] training via [[ArborGRPO]]. Distinct from the [[dspy-tutorial-rag-as-agent|RAG-as-agent tutorial's]] free-ranging [[react|`dspy.ReAct`]] loop — `ResearchHop` is a **fixed-depth iterative-retrieval program** with two `dspy.ChainOfThought` sub-modules wired in a hop-loop `forward(...)`.

> **Lineage note (added by [[dspy-multihop-search-tutorial]]):** `ResearchHop` is the **2-hop simplification of [[Hop|`Hop(num_docs=10, num_hops=4)`]]** — the canonical multi-hop search program from the official DSPy `multihop_search` tutorial. Both programs share the same generate-query / append-notes / search structural template; `ResearchHop` differs by (a) cutting `num_hops` from 4 to 2, (b) cutting `num_docs` from 10 to 4, (c) adding a first-hop bootstrap (raw claim as hop-0 query), (d) adding a last-hop early-exit (skip terminal `append_notes`), and (e) using untyped string output Signatures (`new_key_facts`) instead of `Hop`'s typed `list[str]` outputs. The cuts collapse LM calls from 8 to 3 per claim — the ~63% reduction is what makes [[ArborGRPO|on-policy GRPO]] rollout budgets feasible on a 1.5B Qwen student.

## Program shape

```python
class ResearchHop(dspy.Module):
    def __init__(self, num_docs, num_hops):
        self.num_docs, self.num_hops = num_docs, num_hops
        self.generate_query = dspy.ChainOfThought(
            dspy.Signature("claim, key_facts -> followup_search_query", instr1))
        self.append_notes = dspy.ChainOfThought(
            dspy.Signature("claim, key_facts, new_search_results -> new_key_facts", instr2))

    def forward(self, claim: str):
        key_facts, retrieved_docs = [], []
        for hop_idx in range(self.num_hops):
            query = (self.generate_query(claim=claim, key_facts=key_facts).followup_search_query
                     if hop_idx else claim)
            search_results = search(query, k=self.num_docs)
            retrieved_docs.extend(search_results)
            if hop_idx == self.num_hops - 1:
                break
            prediction = self.append_notes(claim=claim, key_facts=key_facts,
                                           new_search_results=search_results)
            key_facts.append(prediction.new_key_facts)
        return dspy.Prediction(key_facts=key_facts, retrieved_docs=retrieved_docs)
```

Tutorial uses `ResearchHop(num_docs=4, num_hops=2)`: each hop retrieves 4 BM25 documents; two hops total (one bootstrap from the claim, one follow-up driven by `key_facts`).

## Two sub-Signatures

- **`generate_query`**: `(claim, key_facts) -> followup_search_query`. Natural-language instruction: *"Given a claim and some key facts, generate a follow-up search query to find the next most essential clue towards verifying or refuting the claim."*
- **`append_notes`**: `(claim, key_facts, new_search_results) -> new_key_facts`. Natural-language instruction: *"Given a claim, some key facts, and new search results, identify any new learnings from the new search results, which will extend the key facts known so far about whether the claim is true or false."*

Both sub-modules are [[chainofthought|`dspy.ChainOfThought`]] wrappers, so each gets an injected `reasoning` field before its declared output.

## First-hop bootstrap

The `if hop_idx else claim` ternary uses the **raw claim** as the first-hop query — no `generate_query` call on hop 0. Saves one LM call per example and grounds the first retrieval in the literal claim text. Subsequent hops use `generate_query(...)` to synthesize a follow-up query from the claim + accumulated `key_facts`.

## Last-hop early exit

`if hop_idx == self.num_hops - 1: break` skips the `append_notes` synthesis on the final hop — the program has the documents it needs; no point updating `key_facts` past the last retrieval. Saves one LM call per example.

## Position in DSPy program patterns

| Pattern | Example | Distinguishing feature |
|---|---|---|
| Free-form agent loop | [[dspy-tutorial-rag-as-agent|`dspy.ReAct(..., max_iters=20)`]] | LM chooses when to stop; tools as actions. |
| **Fixed-depth iterative retrieval** | **`ResearchHop`** | **Hardcoded hop count; deterministic control flow.** |
| Single-shot CoT | [[dspy-tutorial-math]] | One sub-module, one call. |
| Multi-Signature pipeline | [[dspy-email-extraction-tutorial]] | Sequential diamond; not iterative. |

The fixed-depth pattern is the **right choice when**:
- the hop count is known a priori (HoVer-3-hop claims need ≤3 retrievals);
- the LM control is unreliable (a 1.5B Qwen student cannot be trusted to stop a free ReAct loop);
- the reward is on the *retrieval output*, not on terminal-state correctness — so the loop should run to completion every time.

## Reward integration via [[ArborGRPO]]

The tutorial pairs `ResearchHop` with a deterministic title-recall metric:

```python
def recall(example, pred, trace=None):
    gold_titles = example.titles
    retrieved_titles = [doc.split(" | ")[0] for doc in pred.retrieved_docs]
    return sum(x in retrieved_titles for x in set(gold_titles)) / len(gold_titles)
```

GRPO consumes this metric as the **scalar reward signal**. Both `generate_query` and `append_notes` get gradient updates propagated through their underlying LoRA-adapter weights — one scalar reward per rollout, distributed across two sub-modules' worth of LM tokens.

## Connections

- [[DSPy]] / [[DSPyModules]] — host framework / module abstraction.
- [[chainofthought|`dspy.ChainOfThought`]] — the sub-module type used twice.
- [[DSPySignatures]] — inline string-form Signatures with natural-language instructions as the second argument.
- [[BM25]] / [[bm25s]] / [[PyStemmer]] — the retrieval substrate.
- [[ArborGRPO]] — the optimizer this program is the canonical student of.
- [[grpo|GRPO]] — the RL algorithm.
- [[DAPO]] — the GRPO loss variant.
- [[HoVer]] — the benchmark.
- [[MultiHopRAG]] — the architectural pattern `ResearchHop` instantiates (sequential queries, each depending on prior results).
- [[MultiHopQA]] — task family.
- [[dspy-rl-multihop-tutorial]] — the canonical receipt.
- [[Hop]] — **structural parent**; the 4-hop / 10-docs-per-hop program from [[dspy-multihop-search-tutorial]] that `ResearchHop` simplifies for the on-policy RL rollout budget.
- [[dspy-multihop-search-tutorial]] — the [[MIPROv2]] prompt-optimization sibling tutorial that uses [[Hop]] on the same [[HoVer]] benchmark.
- [[react|`dspy.ReAct`]] — the free-form-agent alternative used by [[dspy-tutorial-rag-as-agent]].
- [[dspy-custom-module]] — the 3-stage `generate_query → retrieve → generate_answer` RAG template; `ResearchHop` is the **iterative extension** of that pattern (`generate_query → retrieve → append_notes → repeat`).
- [[PAPILLON]] — sibling [[ArborGRPO]] training target; different task shape (privacy delegation, not retrieval).
