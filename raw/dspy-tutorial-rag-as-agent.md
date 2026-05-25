# Building RAG as Agent — DSPy Tutorial

Source: https://dspy.ai/tutorials/agents/ (fetched 2026-05-24)

## Overview

This tutorial demonstrates constructing a retrieval-augmented generation system as an intelligent agent using DSPy's ReAct module. The system performs multi-hop search across Wikipedia to identify relevant documents for fact-checking complex claims.

The task: given a claim from the HoVer benchmark, return all Wikipedia titles needed to verify or refute it. HoVer requires multi-hop reasoning — the tutorial filters to three-hop claims only.

## Architecture

### Language model setup

```python
import dspy

llama3b = dspy.LM('<provider>/Llama-3.2-3B-Instruct', temperature=0.7)
gpt4o = dspy.LM('openai/gpt-4o', temperature=0.7)

dspy.configure(lm=llama3b)
```

The agent runs on Llama-3.2-3B-Instruct as the student / inference model. GPT-4o serves as the **teacher** during optimization — invoked "a very small number of times" to bootstrap demonstrations and propose instructions.

### Tools

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

Two complementary tools: `search_wikipedia` returns the top-5 documents in full plus titles-only for positions 5–30 (cheap exploration of the title space); `lookup_wikipedia` returns the full Wikipedia article text for a specified title (deep verification on a candidate).

### Agent

```python
instructions = "Find all Wikipedia titles relevant to verifying (or refuting) the claim."
signature = dspy.Signature("claim -> titles: list[str]", instructions)
react = dspy.ReAct(signature, tools=[search_wikipedia, lookup_wikipedia], max_iters=20)
```

`dspy.ReAct` runs the think-act-observe loop for up to 20 iterations. The Signature is two-field (`claim` in, `titles` out); the tool list is the action surface.

## Dataset

```python
import random
from dspy.datasets import DataLoader

kwargs = dict(fields=("claim", "supporting_facts", "hpqa_id", "num_hops"),
              input_keys=("claim",))
hover = DataLoader().from_huggingface(dataset_name="vincentkoc/hover-parquet",
                                      split="train", trust_remote_code=True, **kwargs)

hpqa_ids = set()
hover = [
    dspy.Example(claim=x.claim, titles=list(set([y["key"] for y in x.supporting_facts]))).with_inputs("claim")
    for x in hover
    if x["num_hops"] == 3 and x["hpqa_id"] not in hpqa_ids and not hpqa_ids.add(x["hpqa_id"])
]

random.Random(0).shuffle(hover)
trainset, devset, testset = hover[:100], hover[100:200], hover[650:]
```

Filtered to three-hop claims, deduplicated by `hpqa_id`, shuffled with seed 0. **100 train / 100 dev / remainder test.** Each example has exactly 3 gold titles.

## Metric

```python
def top5_recall(example, pred, trace=None):
    gold_titles = example.titles
    recall = sum(x in pred.titles[:5] for x in gold_titles) / len(gold_titles)
    if trace is not None:
        return recall >= 1.0
    return recall
```

`top5_recall` measures the fraction of gold pages (always 3) retrieved in the top-5 titles returned by the agent. **Dual-mode**: during optimization (`trace is not None`) it returns a strict boolean (perfect recall only); during evaluation (`trace is None`) it returns the decimal score.

## Evaluation harness

```python
evaluate = dspy.Evaluate(devset=devset, metric=top5_recall, num_threads=16,
                         display_progress=True, display_table=5)
```

## Optimization

```python
kwargs = dict(teacher_settings=dict(lm=gpt4o), prompt_model=gpt4o, max_errors=999)
tp = dspy.MIPROv2(metric=top5_recall, auto="medium", num_threads=16, **kwargs)
optimized_react = tp.compile(react, trainset=trainset, max_bootstrapped_demos=3,
                             max_labeled_demos=0)
```

`dspy.MIPROv2` jointly optimizes the two internal prompts inside `dspy.ReAct`. Configuration:
- `teacher_settings=dict(lm=gpt4o)` — GPT-4o is the demo-bootstrapping teacher
- `prompt_model=gpt4o` — GPT-4o is the instruction proposer
- `auto="medium"` — medium-difficulty preset
- `max_errors=999` — permit many failures during exploration (small student model is brittle)
- `max_bootstrapped_demos=3, max_labeled_demos=0` — up to 3 teacher-generated demos; no human-labeled demos

## Results

| Stage | top5_recall on dev |
|---|---|
| Unoptimized Llama-3.2-3B agent | **8%** |
| MIPROv2-optimized | **≈41.67%** |

**~5× improvement** from prompt optimization alone — same student model, same tools, same metric. The optimization uses GPT-4o as teacher only during compilation; inference is pure Llama-3.2-3B.

## MLflow integration

```python
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("DSPy")
mlflow.dspy.autolog()
```

`mlflow.dspy.autolog()` produces per-call trace spans for every `dspy.Module` invocation — visualizes the full think-act-observe trajectory in the MLflow UI. Tracks evaluation metrics across optimization iterations.

## Save / load

```python
optimized_react.save("optimized_react.json")
loaded_react = dspy.ReAct("claim -> titles: list[str]", tools=[search_wikipedia,
                          lookup_wikipedia], max_iters=20)
loaded_react.load("optimized_react.json")
```

Plain-text JSON serialization. Reload requires reconstructing the `dspy.ReAct` with the same Signature and tools, then calling `.load(path)` to restore the optimized instructions and demonstrations.

## Key claims

- **Small open models are unreliable as agents out-of-the-box.** Llama-3.2-3B "is not very reliable out of the box for long or complex agent loops" — 8% recall confirms this on three-hop fact-checking.
- **Prompt optimization recovers most of the gap.** ~5× recall improvement (8% → 41.67%) from MIPROv2 alone, no weight tuning.
- **Teacher/student decoupling enables cheap inference.** GPT-4o is invoked only during compilation; deployment runs entirely on Llama-3.2-3B.
- **Dual-mode metrics support bootstrapping.** The same `top5_recall` function returns boolean during optimization (for strict demo filtering) and decimal during evaluation — the standard DSPy `trace is None` pattern.

## Inspecting learned prompts

Use `dspy.inspect_history(n=2)` to view the optimized prompts and the agent's reasoning trajectory. The tutorial does not document the specific instructions MIPROv2 produces — they emerge from the grounded-proposal stage based on the program code, training data, and bootstrap traces.
