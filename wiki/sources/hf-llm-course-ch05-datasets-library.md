---
title: "HuggingFace LLM Course — Ch 5: The 🤗 Datasets library"
type: source
tags: [hf-llm-course, course, datasets, faiss, semantic-search, data-engineering]
date: 2026-05-23
source_file: raw/hf-llm-course/ch05-datasets-library.md
---

## Summary

Chapter 5 of the HuggingFace LLM Course is a deep dive into the 🤗 [[Datasets]] library, covering everything beyond the basic Hub-load-then-map flow introduced in Chapter 3. It teaches loading from local/remote files in CSV/TSV/JSON/JSONL/text/pandas formats via `load_dataset()`, slicing-and-dicing with `Dataset.map()`/`filter()`/`shuffle()`/`select()`/`sort()`/`unique()`/`rename_column()`, and switching output format to/from Pandas via `Dataset.set_format()` for interop. It then explains how 🤗 Datasets handles big data without melting RAM via [[MemoryMapping]] backed by [[ApacheArrow]], and how to consume datasets too large for disk via [[DatasetStreaming]] (`streaming=True` returning an [[IterableDataset]]). Finally it walks through creating a brand-new dataset from the GitHub REST API (the `huggingface/datasets` repository's own issues), pushing it to the Hub with `push_to_hub()`, and building a semantic search engine over the resulting issue+comment corpus using `sentence-transformers/multi-qa-mpnet-base-dot-v1` embeddings + a [[FAISS]] index via `Dataset.add_faiss_index()` / `Dataset.get_nearest_examples()`.

## Key Claims

- 🤗 Datasets supports loading CSV/TSV (`csv`), text (`text`), JSON/JSONL (`json`), and pickled DataFrames (`pandas`) via `load_dataset()` with a `data_files` argument that accepts a path, list, glob, dict-of-splits, or remote URL.
- Loading scripts auto-decompress GZIP, ZIP, and TAR inputs, so you can point `data_files` directly at compressed archives.
- `Dataset.map()` with `batched=True` is essential for unlocking the Rust-backed parallelism of [[FastTokenizers]]; benchmark shows fast+batched is ~30× faster than slow+unbatched.
- `Dataset.map()` parallelizes via `num_proc`, but mixing `num_proc` with fast tokenizers + `batched=True` is generally counterproductive.
- With `batched=True`, a map function can change the number of rows (e.g., chunking long sequences via `return_overflowing_tokens=True`); old columns must be dropped via `remove_columns` or replicated using `overflow_to_sample_mapping`.
- `Dataset.set_format("pandas")` swaps only the **output** format; the underlying storage stays Apache Arrow and `__getitem__()` now returns DataFrames.
- 🤗 Datasets loads a ~20 GB PubMed Abstracts subset of the Pile while using a tiny fraction of that in RAM, because each dataset is a memory-mapped Arrow file — directly contradicting Wes McKinney's "5–10× RAM" Pandas rule of thumb.
- Memory-mapped files can be shared across processes, which is what makes `Dataset.map()` parallelism cheap.
- `streaming=True` returns an `IterableDataset` that downloads/decodes lazily; you iterate with `next(iter(...))`, shuffle with a bounded `buffer_size`, slice with `take()`/`skip()`, and combine streams with `interleave_datasets()`.
- A custom dataset can be built from scratch — e.g., fetching GitHub issues via the REST API (60/h unauth, 5,000/h with a personal access token), turning them into a `Dataset`, augmenting via `Dataset.map()` (here, fetching comments per issue), and publishing via `push_to_hub()`.
- GitHub's REST API treats every PR as an issue, but not vice versa — use the `pull_request` field (None ⇒ ordinary issue) to discriminate.
- Semantic search beats keyword search by computing similarity between **embedding vectors** rather than literal token overlap; this requires a pooling strategy (e.g., **CLS pooling**, taking `last_hidden_state[:, 0]`).
- `sentence-transformers/multi-qa-mpnet-base-dot-v1` is the recommended checkpoint for **asymmetric semantic search** (short query, longer documents).
- [[FAISS]] (Facebook AI Similarity Search) is integrated directly into 🤗 Datasets via `Dataset.add_faiss_index(column=...)` and queried via `Dataset.get_nearest_examples(column, query_embedding, k=...)`.
- Embeddings must be NumPy arrays (not Torch/TF tensors) to be FAISS-indexable inside a 🤗 Dataset.

## Key Quotes

> "🤗 Datasets treats each dataset as a memory-mapped file, which provides a mapping between RAM and filesystem storage that allows the library to access and operate on elements of the dataset without needing to fully load it into memory." — Section 4

> "Using a fast tokenizer with the `batched=True` option is 30 times faster than its slow counterpart with no batching … behind the scenes the tokenization code is executed in Rust, which is a language that makes it easy to parallelize code execution." — Section 3

> "Instead of the familiar `Dataset` that we've encountered elsewhere in this chapter, the object returned with `streaming=True` is an `IterableDataset`. As the name suggests, to access the elements of an `IterableDataset` we need to iterate over it." — Section 4

> "GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request." — Section 5

> "Our use case is an example of asymmetric semantic search because we have a short query whose answer we'd like to find in a longer document." — Section 6

## Code & Patterns

### `load_dataset()` — local, remote, compressed, multi-split

```python
from datasets import load_dataset

# JSON with a nested `data` field (e.g., SQuAD)
squad_it = load_dataset("json", data_files="SQuAD_it-train.json", field="data")

# Multiple splits at once (paths or URLs, optionally compressed)
data_files = {
    "train": "https://github.com/crux82/squad-it/raw/master/SQuAD_it-train.json.gz",
    "test":  "https://github.com/crux82/squad-it/raw/master/SQuAD_it-test.json.gz",
}
squad_it = load_dataset("json", data_files=data_files, field="data")

# TSV via the csv loader
drug = load_dataset("csv",
                    data_files={"train": "drugsComTrain_raw.tsv",
                                "test":  "drugsComTest_raw.tsv"},
                    delimiter="\t")
```

### `Dataset.map()` patterns

```python
# Add a derived column
def compute_review_length(example):
    return {"review_length": len(example["review"].split())}
drug = drug.map(compute_review_length)

# Batched + list-comp (parallelism via Arrow vectorization)
drug = drug.map(lambda x: {"review": [html.unescape(o) for o in x["review"]]},
                batched=True)

# Multiprocessing (NOT recommended with fast tokenizers + batched=True)
drug = drug.map(tokenize_fn, batched=True, num_proc=8)

# Map that changes row count (chunked tokenization)
def tokenize_and_split(examples):
    result = tokenizer(examples["review"], truncation=True, max_length=128,
                       return_overflowing_tokens=True)
    sample_map = result.pop("overflow_to_sample_mapping")
    for key, values in examples.items():
        result[key] = [values[i] for i in sample_map]
    return result
```

### Apache Arrow ↔ Pandas

```python
drug.set_format("pandas")          # only changes __getitem__ return type
train_df = drug["train"][:]        # full-slice to materialize a DataFrame
freq_dataset = Dataset.from_pandas(frequencies)
drug.reset_format()                # back to arrow
```

### Persistence

```python
drug_clean.save_to_disk("drug-reviews")             # Arrow (multi-file dir)
drug_clean.to_csv("drug-reviews-train.csv")         # one CSV per split
drug_clean.to_json("drug-reviews-train.jsonl")      # JSON Lines
drug_reloaded = load_from_disk("drug-reviews")
```

### Memory-mapped Big Data + Streaming

```python
# Memory-mapped load — 19.5 GB on disk, fits without melting RAM
pubmed = load_dataset("json", data_files=url, split="train")

# Streaming load — never fully materialized
pubmed_stream = load_dataset("json", data_files=url, split="train", streaming=True)
next(iter(pubmed_stream))

# Stream-only shuffle (bounded buffer)
shuffled = pubmed_stream.shuffle(buffer_size=10_000, seed=42)

# Slice analogues
head = pubmed_stream.take(5)
tail = pubmed_stream.skip(1000)

# Combine multiple streams
from datasets import interleave_datasets
combined = interleave_datasets([pubmed_stream, law_stream])
```

### Build a dataset from GitHub + push to Hub

```python
issues_dataset = load_dataset("json", data_files="datasets-issues.jsonl", split="train")
issues_dataset = issues_dataset.map(
    lambda x: {"is_pull_request": x["pull_request"] is not None}
)
issues_dataset = issues_dataset.map(
    lambda x: {"comments": get_comments(x["number"])}
)
issues_dataset.push_to_hub("github-issues")
```

### Semantic search with FAISS

```python
# CLS pooling -> 768-d vector
def cls_pooling(model_output):
    return model_output.last_hidden_state[:, 0]

def get_embeddings(text_list):
    enc = tokenizer(text_list, padding=True, truncation=True, return_tensors="pt")
    enc = {k: v.to(device) for k, v in enc.items()}
    return cls_pooling(model(**enc))

emb = comments_dataset.map(
    lambda x: {"embeddings": get_embeddings(x["text"]).detach().cpu().numpy()[0]}
)
emb.add_faiss_index(column="embeddings")

q_emb = get_embeddings(["How can I load a dataset offline?"]).cpu().detach().numpy()
scores, samples = emb.get_nearest_examples("embeddings", q_emb, k=5)
```

## Connections

- [[Datasets]] (HuggingFace library) — primary subject; this chapter is its canonical tutorial.
- [[ApacheArrow]] — underlying columnar memory format behind every `Dataset` object.
- [[MemoryMapping]] — the OS feature that lets 20 GB datasets live in 5,678 MB of RSS.
- [[DatasetStreaming]] — `streaming=True` mode for corpora bigger than disk (e.g., the full 825 GB Pile).
- [[IterableDataset]] — the streaming counterpart of `Dataset`; iterator semantics, buffered shuffle, `take`/`skip`.
- [[SemanticSearch]] — embedding-based retrieval that section 6 builds end-to-end.
- [[FAISS]] — vector similarity index used to make semantic search practical at scale.
- [[CLSPooling]] / [[ClsToken]] — pooling strategy used to turn token embeddings into a sentence vector.
- [[SentenceTransformers]] — library family that the `multi-qa-mpnet-base-dot-v1` checkpoint comes from.
- [[FastTokenizers]] — Rust-backed tokenizers that benefit dramatically from `Dataset.map(batched=True)`.
- [[ThePile]] / [[EleutherAI]] — the 825 GB corpus used to demonstrate memory mapping and streaming.
- [[PubMed]] — source of the 15M-abstract Pile subset used in section 4.
- [[SQuADIt]] — Italian QA dataset used as the section 2 local/remote loading example.
- [[DrugReviewDataset]] / [[UCIMLRepository]] — TSV dataset used throughout section 3.
- [[GitHubIssuesDataset]] — the meta dataset of `huggingface/datasets` issues built in section 5.
- [[GitHubRESTAPI]] — data source for building the GitHub issues dataset.
- [[HuggingFaceHub]] — push/pull target for custom datasets via `push_to_hub()`.
- [[BERT]] / [[GPT2]] — motivating examples for "huge corpora won't fit in RAM."
- [[JSONLines]] — line-delimited JSON used as the canonical streaming format.
- [[Zstandard]] — compression used by the Pile subsets.
- [[Pandas]] — `Dataset.set_format("pandas")` interop and `DataFrame.explode()` for row-multiplication.
- [[FineTuning]] (Chapter 3) — prerequisite that introduced `load_dataset` + `Dataset.map` at a basic level.
- [[Chapter6Tokenizers]] / [[Chapter7NLPTasks]] — the next chapters that build on this foundation.

## Contradictions

- Implicitly contradicts the popular Wes McKinney/Pandas heuristic that "you typically need 5 to 10 times as much RAM as the size of your dataset" — the chapter explicitly cites this rule and shows that Arrow-based memory mapping breaks it.
- The chapter recommends `Dataset.map(batched=True, num_proc=...)` for slow tokenizers but warns *against* combining `num_proc` with fast tokenizers + `batched=True` — a nuance worth flagging if other wiki pages on data-pipeline parallelism assume "more procs is always better."
