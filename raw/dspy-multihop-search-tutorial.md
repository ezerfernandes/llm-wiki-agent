# DSPy Tutorial — Multi-Hop Search (MIPROv2 over HoVer)

Source: https://dspy.ai/tutorials/multihop_search/

## Overview

Tutorial demonstrates building a `dspy.Module` for multi-hop retrieval — a system that iteratively searches and gathers evidence across multiple Wikipedia pages to verify complex claims. Given a claim, the program produces a `list[str]` of page titles through iterative retrieval cycles.

Core architecture: the `Hop` module composes two sub-modules:
- `generate_query`: produces search queries based on accumulated notes
- `append_notes`: extracts relevant information and titles from retrieved documents

## Infrastructure Setup

- **Student LM**: `<provider>/Llama-3.1-8B-Instruct` (primary)
- **Teacher / proposer LM**: `openai/gpt-4o`
- **Retrieval engine**: `bm25s` (Python BM25) over **5.2 million Wikipedia abstracts** (2017 snapshot)
- **Dataset**: HoVer (fact-checking claims requiring 3 hops) — `vincentkoc/hover-parquet` Hugging Face repo
- **Train/Dev/Test split**: 200 / 300 / remainder

## LM Configuration

```python
import dspy

lm = dspy.LM('<your_provider>/Llama-3.1-8B-Instruct', max_tokens=3000)
gpt4o = dspy.LM('openai/gpt-4o', max_tokens=3000)

dspy.configure(lm=lm)
```

## BM25S Retriever Setup

```python
import bm25s
import Stemmer

stemmer = Stemmer.Stemmer("english")
corpus_tokens = bm25s.tokenize(corpus, stopwords="en", stemmer=stemmer)

retriever = bm25s.BM25(k1=0.9, b=0.4)
retriever.index(corpus_tokens)

def search(query: str, k: int) -> list[str]:
    tokens = bm25s.tokenize(query, stopwords="en", stemmer=stemmer, show_progress=False)
    results, scores = retriever.retrieve(tokens, k=k, n_threads=1, show_progress=False)
    run = {corpus[doc]: float(score) for doc, score in zip(results[0], scores[0])}
    return run
```

## Hop Module

```python
class Hop(dspy.Module):
    def __init__(self, num_docs=10, num_hops=4):
        self.num_docs, self.num_hops = num_docs, num_hops
        self.generate_query = dspy.ChainOfThought('claim, notes -> query')
        self.append_notes = dspy.ChainOfThought('claim, notes, context -> new_notes: list[str], titles: list[str]')

    def forward(self, claim: str) -> list[str]:
        notes = []
        titles = []

        for _ in range(self.num_hops):
            query = self.generate_query(claim=claim, notes=notes).query
            context = search(query, k=self.num_docs)
            prediction = self.append_notes(claim=claim, notes=notes, context=context)
            notes.extend(prediction.new_notes)
            titles.extend(prediction.titles)

        return dspy.Prediction(notes=notes, titles=list(set(titles)))
```

## Dataset Loading

```python
import random
from dspy.datasets import DataLoader

kwargs = dict(fields=("claim", "supporting_facts", "hpqa_id", "num_hops"), input_keys=("claim",))
hover = DataLoader().from_huggingface(dataset_name="vincentkoc/hover-parquet", split="train", trust_remote_code=True, **kwargs)

hpqa_ids = set()
hover = [
    dspy.Example(claim=x.claim, titles=list(set([y["key"] for y in x.supporting_facts]))).with_inputs("claim")
    for x in hover
    if x["num_hops"] == 3 and x["hpqa_id"] not in hpqa_ids and not hpqa_ids.add(x["hpqa_id"])
]

random.Random(0).shuffle(hover)
trainset, devset, testset = hover[:200], hover[200:500], hover[650:]
```

## Evaluation Metric

```python
def top5_recall(example, pred, trace=None):
    gold_titles = example.titles
    recall = sum(x in pred.titles[:5] for x in gold_titles) / len(gold_titles)

    if trace is not None:
        return recall >= 1.0

    return recall

evaluate = dspy.Evaluate(devset=devset, metric=top5_recall, num_threads=16,
                          display_progress=True, display_table=5)
```

Metric dual-mode: returns a float `recall` for evaluation, but returns a boolean `recall >= 1.0` when `trace is not None` (i.e. during bootstrapping — only perfect-recall examples become demos).

## MIPROv2 Compilation

```python
models = dict(prompt_model=gpt4o, teacher_settings=dict(lm=gpt4o))
tp = dspy.MIPROv2(metric=top5_recall, auto="medium", num_threads=16, **models)

kwargs = dict(minibatch_size=40, minibatch_full_eval_steps=4)
optimized = tp.compile(Hop(), trainset=trainset, max_bootstrapped_demos=4, max_labeled_demos=4, **kwargs)
```

Configuration: `auto="medium"`, GPT-4o as both `prompt_model` (instruction proposer) and `teacher_settings.lm` (bootstrap-demo teacher). The tutorial budgets the GPT-4o spend at "make some $5 worth of calls to GPT-4o to optimize Llama-3.1-8B".

## Performance

| Stage | top5_recall |
|---|---|
| Baseline (unoptimized) | 31.3% |
| After MIPROv2 | **59.1%** |

Nearly doubled performance.

## Sample Output

For a claim about "Up Against It" (Beatles script), the optimized system retrieved:

```
['Up Against It', 'Bernard-Marie Koltès', 'The Beatles', 'Joe Orton']
```

## Persistence and Tracing

Tutorial references:
- MLflow autologging via `mlflow.dspy.autolog()` for trace + experiment tracking
- `program.save(...)` / `program.load(...)` for JSON-format persistence
- MLflow artifact load via `mlflow.artifacts.download_artifacts(...)`
