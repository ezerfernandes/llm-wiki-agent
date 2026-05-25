---
title: "DSPy Tutorial — Building RAG as Agent"
type: source
tags: [dspy, tutorial, react, agent, rag, multi-hop, hover, mipro, optimization, llama, mlflow]
date: 2026-05-24
source_file: raw/dspy-tutorial-rag-as-agent.md
---

## Summary

The [[DSPy]] **Building RAG as Agent** tutorial ([dspy.ai/tutorials/agents](https://dspy.ai/tutorials/agents/)) is the canonical end-to-end receipt for **a [[react|`dspy.ReAct`]] multi-hop retrieval agent over [[HoVer]], optimized end-to-end by [[MIPROv2]] with [[OpenAI|GPT-4o]] as teacher and [[Llama|Llama-3.2-3B-Instruct]] as student**. Where the [[dspy-customer-service-agent|Customer Service Agent tutorial]] showed a seven-tool agent over a typed [[Pydantic]] domain with no optimization stage, this tutorial fills the **complementary slot**: a *two-tool* agent over an *open-domain Wikipedia retrieval* task with a **full bootstrap-and-optimize pipeline that lifts dev recall from 8% to 41.67% — a 5× improvement on a frozen 3B-parameter student**.

The tutorial is the **third wiki-corpus DSPy tutorial** (after [[dspy-conversation-history]] and [[dspy-customer-service-agent]]) and the **first DSPy tutorial in the wiki that ships an end-to-end [[MIPROv2]] optimization run with measured before/after numbers on an open-domain task**. It is structurally important because it pairs three pieces the wiki has so far only carried separately:

1. **[[react|`dspy.ReAct`]] over real retrieval tools** (Wikipedia search + lookup) — the *open-domain* counterpart to the [[dspy-customer-service-agent|airline domain's]] closed-typed tool surface
2. **[[MIPROv2]] with explicit teacher/student decoupling** (`teacher_settings=dict(lm=gpt4o), prompt_model=gpt4o`) — the **first wiki receipt where the teacher model differs from the deployed student model**, operationalizing the cost-of-deployment vs cost-of-compilation split
3. **[[HoVer]] three-hop subset as the optimization target** — connects MIPROv2 back to the same benchmark [[2406.11695-mipro|the original MIPRO paper]] used as the deepest-pipeline task (4 modules, 4 LM calls in the paper; here folded into one [[react|ReAct]] loop with two tools)

The tutorial's three load-bearing structural claims:

1. **Small open-weights models require optimization to be usable as agents.** Llama-3.2-3B-Instruct as the agent LM achieves only **8% top5_recall** on three-hop HoVer claims out of the box — the tutorial frames this as the canonical *"not very reliable out of the box for long or complex agent loops"* failure mode.
2. **[[MIPROv2]] recovers ~5× the baseline performance via prompt optimization alone — no weight tuning.** After optimization with `auto="medium"`, `max_bootstrapped_demos=3`, `max_labeled_demos=0`, GPT-4o teacher: **~41.67% top5_recall** on the same dev set, same model, same tools.
3. **Teacher/student decoupling makes optimization economically viable.** GPT-4o is invoked *"a very small number of times"* during compilation (instruction proposal + demo bootstrapping); deployment runs entirely on the 3B Llama. The wiki's first explicit instance of *"the expensive model writes the prompts; the cheap model runs them"*.

## Key Claims

- **Llama-3.2-3B-Instruct is a viable agent student model once optimized.** The 8% → 41.67% lift is the wiki's first quantitative demonstration of small-model rehabilitation through prompt optimization. **5× improvement on the same student**.

- **`dspy.ReAct` accepts a `max_iters` kwarg controlling the think-act-observe loop depth.** *"`dspy.ReAct(signature, tools=[search_wikipedia, lookup_wikipedia], max_iters=20)`"* — the [[react|ReAct]] page's mechanism description gains a concrete bound: 20 iterations for three-hop HoVer claims. The [[dspy-customer-service-agent|Customer Service Agent tutorial]] did not exercise this parameter.

- **MIPROv2's `teacher_settings` and `prompt_model` are distinct kwargs.** `teacher_settings=dict(lm=gpt4o)` configures the **demo-bootstrapping teacher** (which model runs the program to collect successful traces); `prompt_model=gpt4o` configures the **instruction proposer** (which model writes candidate instructions in the [[MIPROv2|grounded-proposal stage]]). Both default to the configured task LM if unset. The tutorial uses GPT-4o for both — the *all-teacher-where-it-matters* pattern.

- **`max_errors=999` is the operational knob for brittle students.** *"`kwargs = dict(teacher_settings=dict(lm=gpt4o), prompt_model=gpt4o, max_errors=999)`"* — the small student misformats / loops / fails to terminate often enough during exploration that MIPROv2's default error budget would abort optimization. Setting `max_errors=999` lets the optimizer push through. **First wiki receipt to surface this kwarg.**

- **`max_bootstrapped_demos=3, max_labeled_demos=0`** is the *small-student / GPT-4o-teacher* preset. Three demos is the upper bound on what fits in the brittle student's context; zero labeled demos because the dataset has no chain-of-thought labels — only `(claim, gold_titles)` pairs.

- **The custom `top5_recall` metric is dual-mode.** *"`if trace is not None: return recall >= 1.0`"* — during optimization, the metric returns a strict **boolean** (perfect recall only); during evaluation it returns the **decimal** recall score. This is the canonical [[DSPyMetrics|DSPy metric dual-mode pattern]] from page 11 of the *Learn* corpus, here applied to a **list-membership recall metric** rather than the more common exact-match or [[SemanticF1|SemanticF1]] surfaces.

- **Two complementary tools span the retrieval action surface.** `search_wikipedia(query)` returns top-5 documents in full plus **titles-only for positions 5–30** — cheap exploration of the title space. `lookup_wikipedia(title)` returns the **full page text** for a specified title — deep verification on a candidate. The agent learns to alternate between exploration (search) and exploitation (lookup) over the ReAct loop.

- **HoVer is filtered to three-hop claims for the optimization target.** *"`if x["num_hops"] == 3`"* — the dataset is sliced to the hardest subset (three Wikipedia pages needed per claim) before train/dev/test allocation (100/100/remainder). The gold_titles count is constant at 3, which makes the `recall / len(gold_titles)` denominator stable across examples.

- **Plain-text JSON save/load preserves the optimized program.** `optimized_react.save("optimized_react.json")` then `loaded_react = dspy.ReAct("claim -> titles: list[str]", tools=[...], max_iters=20); loaded_react.load("optimized_react.json")` — reload requires **reconstructing the same Signature + tool list**, then loading restores the optimized instructions and demonstrations. Consistent with the [[dspy-optimizers|Optimizers page's]] *"writing code instead of strings"* discipline.

- **`mlflow.dspy.autolog()` traces the full think-act-observe trajectory.** Per-call spans for every reasoning step, tool call, and observation visualized as a tree in the [[MLflow]] UI — the [[react|ReAct]]-specific application of [[MLflow|MLflow's]] DSPy integration first documented in [[dspy-custom-module]]. Track evaluation metrics across optimization iterations.

## Key Quotes

> *"Find all Wikipedia titles relevant to verifying (or refuting) the claim."* — the agent's natural-language instruction, passed as the second argument to `dspy.Signature(...)`. The whole task scoping happens in one sentence.

> *"Returns top-5 results and then the titles of the top-5 to top-30 results."* — the `search_wikipedia` docstring; the agent reads this as the tool description.

> *"Returns the text of the Wikipedia page, if it exists."* — the `lookup_wikipedia` docstring. Both tool docstrings are deliberately short — the [[dspy-tools|Tools page]]'s design rules say docstrings should be clear and detailed; this tutorial demonstrates that *clear* can mean *short* when the function is genuinely simple.

> Baseline performance was *"8%"* recall; after MIPROv2 optimization, *"approximately 41.67%"* recall. The 5× lift is the tutorial's headline result.

> The 3B model *"is not very reliable out of the box for long or complex agent loops"* — but the speed/cost advantage justifies the optimization investment.

## Code Receipts

### Receipt 1 — Two-model configuration

```python
import dspy

llama3b = dspy.LM('<provider>/Llama-3.2-3B-Instruct', temperature=0.7)
gpt4o = dspy.LM('openai/gpt-4o', temperature=0.7)

dspy.configure(lm=llama3b)  # student is the global LM
```

### Receipt 2 — Two retrieval tools

```python
def search_wikipedia(query: str) -> list[str]:
    """Returns top-5 results and then the titles of the top-5 to top-30 results."""
    topK = search(query, 30)
    titles, topK = [f"`{x.split(' | ')[0]}`" for x in topK[5:30]], topK[:5]
    return topK + [f"Other retrieved pages have titles: {', '.join(titles)}."]

def lookup_wikipedia(title: str) -> str:
    """Returns the text of the Wikipedia page, if it exists."""
    if title in DOCS:
        return DOCS[title]
    results = [x for x in search(title, 10) if x.startswith(title + " | ")]
    if not results:
        return f"No Wikipedia page found for title: {title}"
    return results[0]
```

### Receipt 3 — `dspy.ReAct` with `max_iters=20`

```python
instructions = "Find all Wikipedia titles relevant to verifying (or refuting) the claim."
signature = dspy.Signature("claim -> titles: list[str]", instructions)
react = dspy.ReAct(signature, tools=[search_wikipedia, lookup_wikipedia], max_iters=20)
```

### Receipt 4 — Dual-mode `top5_recall` metric

```python
def top5_recall(example, pred, trace=None):
    gold_titles = example.titles
    recall = sum(x in pred.titles[:5] for x in gold_titles) / len(gold_titles)
    if trace is not None:
        return recall >= 1.0
    return recall
```

### Receipt 5 — MIPROv2 with teacher/student decoupling

```python
kwargs = dict(teacher_settings=dict(lm=gpt4o), prompt_model=gpt4o, max_errors=999)
tp = dspy.MIPROv2(metric=top5_recall, auto="medium", num_threads=16, **kwargs)
optimized_react = tp.compile(react, trainset=trainset,
                             max_bootstrapped_demos=3, max_labeled_demos=0)
```

### Receipt 6 — Save / reload

```python
optimized_react.save("optimized_react.json")

loaded_react = dspy.ReAct("claim -> titles: list[str]",
                          tools=[search_wikipedia, lookup_wikipedia], max_iters=20)
loaded_react.load("optimized_react.json")
```

## Position in the DSPy tutorial corpus

| Tutorial | Domain | Tools | Optimization | Headline metric |
|---|---|---|---|---|
| [[dspy-conversation-history]] | Multi-turn chat | (none) | — | — |
| [[dspy-customer-service-agent]] | Airline ([[Pydantic]] typed) | 7 (lookup/mutate/escalate) | — | — |
| **This tutorial** | Wikipedia retrieval ([[HoVer]] 3-hop) | **2** (search + lookup) | **[[MIPROv2]] `auto="medium"`** | **top5_recall 8% → 41.67%** |
| [[dspy-rag-tutorial]] | Tech-domain QA ([[RAGQAArenaTech]]) | (CoT retrieval) | [[MIPROv2]] `auto="medium"` | [[SemanticF1]] 55.5% → 61.1% |

This tutorial is the **first DSPy tutorial in the wiki that combines [[react|`dspy.ReAct`]] + [[MIPROv2]] + measured before/after numbers + cross-model teacher/student decoupling**. The [[dspy-optimizers|Optimizers page]]'s [[react|ReAct]]+HotPotQA receipt (24% → 51% with `auto="light"`) is the closest sibling, but uses GPT-4o-mini as a single model, not a teacher/student pair.

## Cross-tutorial structural confirmations

- **[[react|`dspy.ReAct`]] composes with any retrieval tool surface.** Three independent receipts now confirm this: the [[dspy-modules|Modules page's]] [[ColBERTv2|ColBERTv2]] example (calculator + Wikipedia abstracts), the [[dspy-customer-service-agent|Customer Service Agent's]] seven Pydantic-typed tools, and this tutorial's two custom Wikipedia search/lookup tools. The action surface is open under tool implementation.
- **[[MIPROv2]] with `auto="medium"` is the *workhorse preset* for serious optimization runs.** Three receipts in the wiki now use it: the [[dspy-optimizers|Optimizers page's]] RAG-on-StackExchange (53% → 61%), the [[dspy-rag-tutorial|RAG tutorial]]'s tech-QA (55.5% → 61.1%), and this tutorial's ReAct-on-HoVer (8% → 41.67%). **Medium is the default for cross-model optimization runs.**
- **`trace is None` dual-mode is the universal DSPy metric pattern.** This tutorial's `top5_recall` confirms the [[DSPyMetrics|`(example, pred, trace) -> score`]] contract for **list-membership recall** — extending the wiki's prior dual-mode receipts (exact-match, [[SemanticF1]], validate_hops).

## Connections

- [[DSPy]] — framework; this tutorial is the first to demonstrate cross-model teacher/student optimization
- [[react|ReAct]] — the agent module the tutorial builds on; first receipt with `max_iters=20`
- [[MIPROv2]] — the optimizer; first wiki receipt with explicit `teacher_settings=` + `prompt_model=` decoupling + `max_errors=999`
- [[HoVer]] — the benchmark; first wiki receipt where HoVer is the *optimization target* (not just an evaluation target as in [[2406.11695-mipro|MIPRO paper]] / [[2507.19457-gepa|GEPA]])
- [[MultiHopRAG]] — the broader task class this tutorial instantiates
- [[Llama]] — the student model (Llama-3.2-3B-Instruct)
- [[OpenAI|GPT-4o]] — the teacher / prompt-proposer model
- [[MLflow]] — the experiment-tracking surface; `mlflow.dspy.autolog()` traces the ReAct trajectory
- [[DSPyMetrics]] — dual-mode `top5_recall` confirms the `(example, pred, trace) -> score` contract for list-recall metrics
- [[DSPyOptimizers]] — catalog the optimizer lives in
- [[DSPyExample]] — `dspy.Example(claim=..., titles=[...]).with_inputs("claim")` is the data primitive
- [[DSPyEvaluate]] — `dspy.Evaluate(devset=devset, metric=top5_recall, num_threads=16, ...)`
- [[dspy-customer-service-agent]] — sibling DSPy tutorial: typed-domain agent without optimization stage; complementary structural slot
- [[dspy-conversation-history]] — sibling DSPy tutorial: multi-turn chat without tools or optimization
- [[dspy-rag-tutorial]] — sibling RAG tutorial; uses MIPROv2 `auto="medium"` like this tutorial but with [[ChainOfThought]] not [[react|ReAct]] and [[SemanticF1]] not list-recall
- [[dspy-optimizers]] — page-13 of *Learn*; canonical optimizer catalog the tutorial draws from
- [[2406.11695-mipro]] — the MIPRO paper; uses HoVer as one of seven benchmarks (4-module pipeline vs this tutorial's single ReAct loop)
- [[BootstrapFewShot]] / [[BootstrapFewShotWithRandomSearch]] — demos-only optimizers MIPROv2 generalizes

## Contradictions

None — this tutorial is consistent with the [[2406.11695-mipro|MIPRO paper's]] finding that MIPROv2 dominates on HoVer; the magnitude of the lift (8% → 41.67%, 5×) is larger than the paper's 30.2 → 44.7 (1.5×) because the paper used [[Llama3_8BInstruct|Llama-3-8B]] as the task LM (a larger and more capable student) so had less headroom. The 3B student in this tutorial has more room to gain from optimization.
