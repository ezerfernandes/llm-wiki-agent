# HuggingFace LLM Course — Chapter 5: The 🤗 Datasets library
Source: https://huggingface.co/learn/llm-course/chapter5/
Sections: 1,2,3,4,5,6,7
---

## Section 1: Introduction

# Introduction[[introduction]]

In [Chapter 3](/course/chapter3) you got your first taste of the 🤗 Datasets library and saw that there were three main steps when it came to fine-tuning a model:

1. Load a dataset from the Hugging Face Hub.
2. Preprocess the data with `Dataset.map()`.
3. Load and compute metrics.

But this is just scratching the surface of what 🤗 Datasets can do! In this chapter, we will take a deep dive into the library. Along the way, we'll find answers to the following questions:

* What do you do when your dataset is not on the Hub?
* How can you slice and dice a dataset? (And what if you _really_ need to use Pandas?)
* What do you do when your dataset is huge and will melt your laptop's RAM?
* What the heck are "memory mapping" and Apache Arrow?
* How can you create your own dataset and push it to the Hub?

The techniques you learn here will prepare you for the advanced tokenization and fine-tuning tasks in [Chapter 6](/course/chapter6) and [Chapter 7](/course/chapter7) -- so grab a coffee and let's get started!

---

## Section 2: What if my dataset isn't on the Hub?

# What if my dataset isn't on the Hub?[[what-if-my-dataset-isnt-on-the-hub]]

You know how to use the [Hugging Face Hub](https://huggingface.co/datasets) to download datasets, but you'll often find yourself working with data that is stored either on your laptop or on a remote server. In this section we'll show you how 🤗 Datasets can be used to load datasets that aren't available on the Hugging Face Hub.

## Working with local and remote datasets

🤗 Datasets provides loading scripts to handle the loading of local and remote datasets. It supports several common data formats, such as:

|    Data format     | Loading script |                         Example                         |
| :----------------: | :------------: | :-----------------------------------------------------: |
|     CSV & TSV      |     `csv`      |     `load_dataset("csv", data_files="my_file.csv")`     |
|     Text files     |     `text`     |    `load_dataset("text", data_files="my_file.txt")`     |
| JSON & JSON Lines  |     `json`     |   `load_dataset("json", data_files="my_file.jsonl")`    |
| Pickled DataFrames |    `pandas`    | `load_dataset("pandas", data_files="my_dataframe.pkl")` |

As shown in the table, for each data format we just need to specify the type of loading script in the `load_dataset()` function, along with a `data_files` argument that specifies the path to one or more files.

## Loading a local dataset

For this example we'll use the [SQuAD-it dataset](https://github.com/crux82/squad-it/), which is a large-scale dataset for question answering in Italian.

The training and test splits are hosted on GitHub, so we can download them with a simple `wget` command:

```python
!wget https://github.com/crux82/squad-it/raw/master/SQuAD_it-train.json.gz
!wget https://github.com/crux82/squad-it/raw/master/SQuAD_it-test.json.gz
```

This will download two compressed files called *SQuAD_it-train.json.gz* and *SQuAD_it-test.json.gz*, which we can decompress with the Linux `gzip` command:

```python
!gzip -dkv SQuAD_it-*.json.gz
```

```bash
SQuAD_it-test.json.gz:	   87.4% -- replaced with SQuAD_it-test.json
SQuAD_it-train.json.gz:	   82.2% -- replaced with SQuAD_it-train.json
```

To load a JSON file with the `load_dataset()` function, we just need to know if we're dealing with ordinary JSON or JSON Lines. Like many question answering datasets, SQuAD-it uses the nested format, with all the text stored in a `data` field. This means we can load the dataset by specifying the `field` argument:

```py
from datasets import load_dataset

squad_it_dataset = load_dataset("json", data_files="SQuAD_it-train.json", field="data")
```

By default, loading local files creates a `DatasetDict` object with a `train` split:

```py
squad_it_dataset
```

```python out
DatasetDict({
    train: Dataset({
        features: ['title', 'paragraphs'],
        num_rows: 442
    })
})
```

We can view one example by indexing into the `train` split:

```py
squad_it_dataset["train"][0]
```

```python out
{
    "title": "Terremoto del Sichuan del 2008",
    "paragraphs": [
        {
            "context": "Il terremoto del Sichuan del 2008 o il terremoto...",
            "qas": [
                {
                    "answers": [{"answer_start": 29, "text": "2008"}],
                    "id": "56cdca7862d2951400fa6826",
                    "question": "In quale anno si è verificato il terremoto nel Sichuan?",
                },
                ...
            ],
        },
        ...
    ],
}
```

To include both train and test splits in a single `DatasetDict`, provide a dictionary to `data_files`:

```py
data_files = {"train": "SQuAD_it-train.json", "test": "SQuAD_it-test.json"}
squad_it_dataset = load_dataset("json", data_files=data_files, field="data")
squad_it_dataset
```

```python out
DatasetDict({
    train: Dataset({
        features: ['title', 'paragraphs'],
        num_rows: 442
    })
    test: Dataset({
        features: ['title', 'paragraphs'],
        num_rows: 48
    })
})
```

> [!TIP]
> The `data_files` argument of the `load_dataset()` function can be a single file path, a list of file paths, or a dictionary mapping split names to file paths. You can also glob files (e.g., `data_files="*.json"`).

The loading scripts in 🤗 Datasets actually support **automatic decompression** of input files, so we could have skipped `gzip` by pointing `data_files` directly to compressed files (GZIP, ZIP, TAR):

```py
data_files = {"train": "SQuAD_it-train.json.gz", "test": "SQuAD_it-test.json.gz"}
squad_it_dataset = load_dataset("json", data_files=data_files, field="data")
```

## Loading a remote dataset

Loading remote files is just as simple — point `data_files` at one or more URLs:

```py
url = "https://github.com/crux82/squad-it/raw/master/"
data_files = {
    "train": url + "SQuAD_it-train.json.gz",
    "test": url + "SQuAD_it-test.json.gz",
}
squad_it_dataset = load_dataset("json", data_files=data_files, field="data")
```

---

## Section 3: Time to slice and dice

# Time to slice and dice[[time-to-slice-and-dice]]

Most of the time, the data you work with won't be perfectly prepared for training models. In this section we'll explore the various features that 🤗 Datasets provides to clean up your datasets.

## Slicing and dicing our data

Similar to Pandas, 🤗 Datasets provides several functions to manipulate the contents of `Dataset` and `DatasetDict` objects.

For this example we'll use the [Drug Review Dataset](https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Drugs.com%29) from the UC Irvine Machine Learning Repository, which contains patient reviews on drugs, conditions treated, and 10-star ratings.

```py
!wget "https://archive.ics.uci.edu/ml/machine-learning-databases/00462/drugsCom_raw.zip"
!unzip drugsCom_raw.zip
```

TSV is a variant of CSV using tabs as separator — load via the `csv` script with `delimiter`:

```py
from datasets import load_dataset

data_files = {"train": "drugsComTrain_raw.tsv", "test": "drugsComTest_raw.tsv"}
# \t is the tab character in Python
drug_dataset = load_dataset("csv", data_files=data_files, delimiter="\t")
```

Grab a random sample to feel the data by chaining `Dataset.shuffle()` and `Dataset.select()`:

```py
drug_sample = drug_dataset["train"].shuffle(seed=42).select(range(1000))
# Peek at the first few examples
drug_sample[:3]
```

```python out
{'Unnamed: 0': [87571, 178045, 80482],
 'drugName': ['Naproxen', 'Duloxetine', 'Mobic'],
 'condition': ['Gout, Acute', 'ibromyalgia', 'Inflammatory Conditions'],
 'review': ['"like the previous person mention, I&#039;m a strong believer of aleve, ..."', ...],
 'rating': [9.0, 3.0, 10.0],
 'date': ['September 2, 2015', 'November 7, 2011', 'June 5, 2013'],
 'usefulCount': [36, 13, 128]}
```

Quirks noted:
* The `Unnamed: 0` column looks like an anonymized patient ID.
* The `condition` column has mixed case.
* The reviews contain `\r\n` line separators and HTML character codes like `&#039;`.

Verify the patient ID hypothesis with `Dataset.unique()`:

```py
for split in drug_dataset.keys():
    assert len(drug_dataset[split]) == len(drug_dataset[split].unique("Unnamed: 0"))
```

Rename the column across both splits with `DatasetDict.rename_column()`:

```py
drug_dataset = drug_dataset.rename_column(
    original_column_name="Unnamed: 0", new_column_name="patient_id"
)
```

Normalize the `condition` labels with `Dataset.map()`:

```py
def lowercase_condition(example):
    return {"condition": example["condition"].lower()}

drug_dataset.map(lowercase_condition)
```

```python out
AttributeError: 'NoneType' object has no attribute 'lower'
```

Some entries are `None`. Drop them with `Dataset.filter()` plus a **lambda function**:

```py
drug_dataset = drug_dataset.filter(lambda x: x["condition"] is not None)
drug_dataset = drug_dataset.map(lowercase_condition)
# Check that lowercasing worked
drug_dataset["train"]["condition"][:3]
```

```python out
['left ventricular dysfunction', 'adhd', 'birth control']
```

## Creating new columns

Compute the review length (word count) and add it as a new column via `Dataset.map()`:

```py
def compute_review_length(example):
    return {"review_length": len(example["review"].split())}

drug_dataset = drug_dataset.map(compute_review_length)
```

Inspect extremes by `Dataset.sort()`:

```py
drug_dataset["train"].sort("review_length")[:3]
```

> [!TIP]
> 🙋 An alternative way to add new columns is `Dataset.add_column()`, accepting a Python list or NumPy array.

Filter out reviews under 30 words:

```py
drug_dataset = drug_dataset.filter(lambda x: x["review_length"] > 30)
print(drug_dataset.num_rows)
```

```python out
{'train': 138514, 'test': 46108}
```

Unescape HTML character codes with Python's `html` module + `Dataset.map()`:

```py
import html

drug_dataset = drug_dataset.map(lambda x: {"review": html.unescape(x["review"])})
```

## The `map()` method's superpowers

`Dataset.map()` takes a `batched=True` argument that sends batches of examples (default 1,000) to the map function. The function receives a dict where each value is a **list of values**.

```python
new_drug_dataset = drug_dataset.map(
    lambda x: {"review": [html.unescape(o) for o in x["review"]]}, batched=True
)
```

`batched=True` is essential to unlock the speed of **fast tokenizers** (Rust-backed):

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

def tokenize_function(examples):
    return tokenizer(examples["review"], truncation=True)
```

Benchmark (fast vs. slow tokenizer, with vs. without batching, with vs. without `num_proc=8`):

Options         | Fast tokenizer | Slow tokenizer
:--------------:|:--------------:|:-------------:
`batched=True`  | 10.8s          | 4min41s
`batched=False` | 59.2s          | 5min3s
`batched=True`, `num_proc=8`  | 6.52s          | 41.3s
`batched=False`, `num_proc=8` | 9.49s          | 45.2s

> [!TIP]
> Using `num_proc` to speed up processing is usually a great idea, as long as the function isn't already doing multiprocessing of its own. Don't combine `num_proc` with fast tokenizers + `batched=True` — usually slower.

With `batched=True` you can **change the number of elements** in your dataset — useful when one example yields multiple training features (e.g., long-context chunking via `return_overflowing_tokens=True`):

```py
def tokenize_and_split(examples):
    return tokenizer(
        examples["review"],
        truncation=True,
        max_length=128,
        return_overflowing_tokens=True,
    )
```

Testing on one example shows it splits into two features of length 128 and 49. Applying to the full dataset throws `ArrowInvalid: Column 1 named condition expected length 1463 but got length 1000`. Two fixes:

**Fix 1 — drop old columns:**

```py
tokenized_dataset = drug_dataset.map(
    tokenize_and_split, batched=True, remove_columns=drug_dataset["train"].column_names
)
len(tokenized_dataset["train"]), len(drug_dataset["train"])
# (206772, 138514)
```

**Fix 2 — repeat old columns using `overflow_to_sample_mapping`:**

```py
def tokenize_and_split(examples):
    result = tokenizer(
        examples["review"],
        truncation=True,
        max_length=128,
        return_overflowing_tokens=True,
    )
    # Extract mapping between new and old indices
    sample_map = result.pop("overflow_to_sample_mapping")
    for key, values in examples.items():
        result[key] = [values[i] for i in sample_map]
    return result

tokenized_dataset = drug_dataset.map(tokenize_and_split, batched=True)
```

## From `Dataset`s to `DataFrame`s and back

`Dataset.set_format()` changes only the _output format_ (not the underlying Apache Arrow _data format_). Switch to Pandas:

```py
drug_dataset.set_format("pandas")
drug_dataset["train"][:3]   # returns a pandas.DataFrame
train_df = drug_dataset["train"][:]
```

> [!TIP]
> 🚨 Under the hood, `Dataset.set_format()` changes the return format for `__getitem__()`. To create a `pandas.DataFrame` for the full split you must slice the whole dataset.

Compute class frequency:

```py
frequencies = (
    train_df["condition"]
    .value_counts()
    .to_frame()
    .reset_index()
    .rename(columns={"index": "condition", "count": "frequency"})
)
frequencies.head()
```

Go back to a `Dataset`:

```py
from datasets import Dataset

freq_dataset = Dataset.from_pandas(frequencies)
```

Reset format with `drug_dataset.reset_format()` (back to `"arrow"`).

## Creating a validation set

`Dataset.train_test_split()` (scikit-learn-style) splits a training set:

```py
drug_dataset_clean = drug_dataset["train"].train_test_split(train_size=0.8, seed=42)
# Rename the default "test" split to "validation"
drug_dataset_clean["validation"] = drug_dataset_clean.pop("test")
# Add the "test" set to our `DatasetDict`
drug_dataset_clean["test"] = drug_dataset["test"]
```

## Saving a dataset

🤗 Datasets caches everything, but you can persist explicitly:

| Data format |        Function        |
| :---------: | :--------------------: |
|    Arrow    | `Dataset.save_to_disk()` |
|     CSV     |    `Dataset.to_csv()`    |
|    JSON     |   `Dataset.to_json()`    |

```py
drug_dataset_clean.save_to_disk("drug-reviews")
```

Layout:

```
drug-reviews/
├── dataset_dict.json
├── test
│   ├── dataset.arrow
│   ├── dataset_info.json
│   └── state.json
├── train
│   ├── dataset.arrow
│   ├── dataset_info.json
│   ├── indices.arrow
│   └── state.json
└── validation
    ├── dataset.arrow
    ├── dataset_info.json
    ├── indices.arrow
    └── state.json
```

Reload:

```py
from datasets import load_from_disk

drug_dataset_reloaded = load_from_disk("drug-reviews")
```

For CSV/JSON, iterate over splits:

```py
for split, dataset in drug_dataset_clean.items():
    dataset.to_json(f"drug-reviews-{split}.jsonl")
```

Each row is stored as one JSON line ([JSON Lines format](https://jsonlines.org)).

---

## Section 4: Big data? 🤗 Datasets to the rescue!

# Big data? 🤗 Datasets to the rescue![[big-data-datasets-to-the-rescue]]

Multi-gigabyte datasets are common when pretraining models like BERT or GPT-2. WebText (GPT-2 training corpus) is 40 GB of text from 8M documents.

🤗 Datasets has been designed to overcome these limits. It frees you from memory management by treating datasets as **memory-mapped files**, and from hard drive limits by **streaming**.

This section uses the **Pile** — an 825 GB English text corpus by EleutherAI, available in 14 GB chunks.

## What is the Pile?

The Pile spans scientific articles, GitHub code, filtered web text, etc. We start with the **PubMed Abstracts** subset (15M biomedical abstracts), distributed in JSON Lines compressed with `zstandard`:

```py
!pip install zstandard
```

```py
from datasets import load_dataset

# This takes a few minutes to run, so go grab a tea or coffee while you wait :)
data_files = "https://the-eye.eu/public/AI/pile_preliminary_components/PUBMED_title_abstracts_2019_baseline.jsonl.zst"
pubmed_dataset = load_dataset("json", data_files=data_files, split="train")
pubmed_dataset
```

```python out
Dataset({
    features: ['meta', 'text'],
    num_rows: 15518009
})
```

```py
pubmed_dataset[0]
```

```python out
{'meta': {'pmid': 11409574, 'language': 'eng'},
 'text': 'Epidemiology of hypoxaemia in children with acute lower respiratory infection. ...'}
```

> [!TIP]
> ✎ By default, 🤗 Datasets will decompress files needed to load a dataset. Pass `DownloadConfig(delete_extracted=True)` to `download_config` to save disk.

## The magic of memory mapping

Check RAM with `psutil`:

```python
!pip install psutil
```

```py
import psutil

# Process.memory_info is expressed in bytes, so convert to megabytes
print(f"RAM used: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} MB")
```

```python out
RAM used: 5678.33 MB
```

Compare with on-disk size:

```py
print(f"Dataset size in bytes: {pubmed_dataset.dataset_size}")
size_gb = pubmed_dataset.dataset_size / (1024**3)
print(f"Dataset size (cache file) : {size_gb:.2f} GB")
```

```python out
Dataset size in bytes : 20979437051
Dataset size (cache file) : 19.54 GB
```

A ~20 GB dataset accessed with much less RAM! This contradicts Wes McKinney's Pandas rule of thumb (5–10x dataset size in RAM).

🤗 Datasets treats each dataset as a [memory-mapped file](https://en.wikipedia.org/wiki/Memory-mapped_file). Memory-mapped files can be shared across processes (enabling `Dataset.map()` parallelism without copying data). Backed by **Apache Arrow** and `pyarrow`.

Speed test:

```py
import timeit

code_snippet = """batch_size = 1000

for idx in range(0, len(pubmed_dataset), batch_size):
    _ = pubmed_dataset[idx:idx + batch_size]
"""

time = timeit.timeit(stmt=code_snippet, number=1, globals=globals())
print(
    f"Iterated over {len(pubmed_dataset)} examples (about {size_gb:.1f} GB) in "
    f"{time:.1f}s, i.e. {size_gb/time:.3f} GB/s"
)
```

```python out
'Iterated over 15518009 examples (about 19.5 GB) in 64.2s, i.e. 0.304 GB/s'
```

## Streaming datasets

For datasets too large for disk (the full Pile is 825 GB), use `streaming=True`:

```py
pubmed_dataset_streamed = load_dataset(
    "json", data_files=data_files, split="train", streaming=True
)
```

This returns an `IterableDataset`. Access elements by iteration:

```py
next(iter(pubmed_dataset_streamed))
```

```python out
{'meta': {'pmid': 11409574, 'language': 'eng'},
 'text': 'Epidemiology of hypoxaemia in children with acute lower respiratory infection. ...'}
```

`IterableDataset.map()` works on the fly:

```py
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
tokenized_dataset = pubmed_dataset_streamed.map(lambda x: tokenizer(x["text"]))
next(iter(tokenized_dataset))
```

```python out
{'input_ids': [101, 4958, 5178, 4328, 6779, ...], 'attention_mask': [1, 1, 1, 1, 1, ...]}
```

> [!TIP]
> 💡 To speed up streaming tokenization use `batched=True` (default batch size 1,000).

**Streaming shuffle uses a buffer**:

```py
shuffled_dataset = pubmed_dataset_streamed.shuffle(buffer_size=10_000, seed=42)
next(iter(shuffled_dataset))
```

`IterableDataset.take()` and `IterableDataset.skip()` are stream-friendly analogues of `Dataset.select()`:

```py
dataset_head = pubmed_dataset_streamed.take(5)
list(dataset_head)
```

Create streaming train/validation splits:

```py
# Skip the first 1,000 examples and include the rest in the training set
train_dataset = shuffled_dataset.skip(1000)
# Take the first 1,000 examples for the validation set
validation_dataset = shuffled_dataset.take(1000)
```

**Combine multiple streams** with `interleave_datasets()`:

```py
law_dataset_streamed = load_dataset(
    "json",
    data_files="https://the-eye.eu/public/AI/pile_preliminary_components/FreeLaw_Opinions.jsonl.zst",
    split="train",
    streaming=True,
)
```

```py
from itertools import islice
from datasets import interleave_datasets

combined_dataset = interleave_datasets([pubmed_dataset_streamed, law_dataset_streamed])
list(islice(combined_dataset, 2))
```

Stream the full 825 GB Pile:

```py
base_url = "https://the-eye.eu/public/AI/pile/"
data_files = {
    "train": [base_url + "train/" + f"{idx:02d}.jsonl.zst" for idx in range(30)],
    "validation": base_url + "val.jsonl.zst",
    "test": base_url + "test.jsonl.zst",
}
pile_dataset = load_dataset("json", data_files=data_files, streaming=True)
next(iter(pile_dataset["train"]))
```

---

## Section 5: Creating your own dataset

# Creating your own dataset[[creating-your-own-dataset]]

Sometimes the dataset you need doesn't exist. This section builds a corpus of **GitHub issues** from the 🤗 Datasets repo (meta!). Uses include:

* Exploring how long it takes to close open issues/PRs
* Training a **multilabel classifier** that tags issues with metadata
* Creating a semantic search engine to find issues matching a user query

## Getting the data

At time of writing the repo had 331 open and 668 closed issues. We use the [GitHub REST API](https://docs.github.com/en/rest) `Issues` endpoint and the `requests` library:

```python
!pip install requests
```

```py
import requests

url = "https://api.github.com/repos/huggingface/datasets/issues?page=1&per_page=1"
response = requests.get(url)
response.status_code
```

```python out
200
```

```py
response.json()
```

Sample payload (truncated):

```python out
[{'url': 'https://api.github.com/repos/huggingface/datasets/issues/2792',
  ...
  'number': 2792,
  'title': 'Update GooAQ',
  'user': {'login': 'bhavitvyamalik', ...},
  'labels': [],
  'state': 'open',
  ...
  'pull_request': {'url': ..., 'html_url': ..., 'diff_url': ..., 'patch_url': ...},
  'body': '[GooAQ](https://github.com/allenai/gooaq) dataset was recently updated ...',
  ...}]
```

Unauthenticated requests are rate-limited to 60/hour. With a **personal access token**, you get 5,000/hour:

```py
GITHUB_TOKEN = xxx  # Copy your GitHub token here
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
```

> [!WARNING]
> ⚠️ Do not share a notebook with your `GITHUB_TOKEN` pasted in it. Store the token in a *.env* file and load with `python-dotenv`.

`fetch_issues()` paginates through the API with rate-limit handling:

```py
import time
import math
from pathlib import Path
import pandas as pd
from tqdm.notebook import tqdm

def fetch_issues(
    owner="huggingface",
    repo="datasets",
    num_issues=10_000,
    rate_limit=5_000,
    issues_path=Path("."),
):
    if not issues_path.is_dir():
        issues_path.mkdir(exist_ok=True)

    batch = []
    all_issues = []
    per_page = 100  # Number of issues to return per page
    num_pages = math.ceil(num_issues / per_page)
    base_url = "https://api.github.com/repos"

    for page in tqdm(range(num_pages)):
        # Query with state=all to get both open and closed issues
        query = f"issues?page={page}&per_page={per_page}&state=all"
        issues = requests.get(f"{base_url}/{owner}/{repo}/{query}", headers=headers)
        batch.extend(issues.json())

        if len(batch) > rate_limit and len(all_issues) < num_issues:
            all_issues.extend(batch)
            batch = []
            print(f"Reached GitHub rate limit. Sleeping for one hour ...")
            time.sleep(60 * 60 + 1)

    all_issues.extend(batch)
    df = pd.DataFrame.from_records(all_issues)
    df.to_json(f"{issues_path}/{repo}-issues.jsonl", orient="records", lines=True)
    print(f"Downloaded all the issues for {repo}! Dataset stored at {issues_path}/{repo}-issues.jsonl")
```

Load it locally:

```py
issues_dataset = load_dataset("json", data_files="datasets-issues.jsonl", split="train")
```

> GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request. Use the `pull_request` key to tell them apart.

## Cleaning up the data

```py
sample = issues_dataset.shuffle(seed=666).select(range(3))

for url, pr in zip(sample["html_url"], sample["pull_request"]):
    print(f">> URL: {url}")
    print(f">> Pull request: {pr}\n")
```

Pull requests carry a dict in `pull_request`; ordinary issues have `None`. Add an `is_pull_request` column:

```py
issues_dataset = issues_dataset.map(
    lambda x: {"is_pull_request": False if x["pull_request"] is None else True}
)
```

## Augmenting the dataset

Issue comments live at a separate endpoint:

```py
issue_number = 2792
url = f"https://api.github.com/repos/huggingface/datasets/issues/{issue_number}/comments"
response = requests.get(url, headers=headers)
response.json()
```

Function to fetch comment bodies:

```py
def get_comments(issue_number):
    url = f"https://api.github.com/repos/huggingface/datasets/issues/{issue_number}/comments"
    response = requests.get(url, headers=headers)
    return [r["body"] for r in response.json()]
```

Add a `comments` column:

```py
# Depending on your internet connection, this can take a few minutes...
issues_with_comments_dataset = issues_dataset.map(
    lambda x: {"comments": get_comments(x["number"])}
)
```

## Uploading the dataset to the Hugging Face Hub

```py
from huggingface_hub import notebook_login

notebook_login()
```

```bash
huggingface-cli login
```

```py
issues_with_comments_dataset.push_to_hub("github-issues")
```

Anyone can then download via:

```py
remote_dataset = load_dataset("lewtun/github-issues", split="train")
remote_dataset
```

```python out
Dataset({
    features: ['url', 'repository_url', 'labels_url', 'comments_url', 'events_url', 'html_url', 'id', 'node_id', 'number', 'title', 'user', 'labels', 'state', 'locked', 'assignee', 'assignees', 'milestone', 'comments', 'created_at', 'updated_at', 'closed_at', 'author_association', 'active_lock_reason', 'pull_request', 'body', 'performed_via_github_app', 'is_pull_request'],
    num_rows: 2855
})
```

## Creating a dataset card

A **dataset card** (`README.md`) is essential. Two steps:

1. Use the `datasets-tagging` application to create YAML metadata tags.
2. Read the 🤗 Datasets [README guide](https://github.com/huggingface/datasets/blob/master/templates/README_guide.md) and fill in the card.

---

## Section 6: Semantic search with FAISS

# Semantic search with FAISS[[semantic-search-with-faiss]]

Build a semantic search engine over the GitHub issues corpus.

## Using embeddings for semantic search

Transformer LMs produce **embedding vectors** per token. We can **pool** these into a single vector for a sentence/paragraph/document. Similarity (e.g., dot product) finds the closest documents to a query — better than keyword matching.

## Loading and preparing the dataset

```py
from datasets import load_dataset

issues_dataset = load_dataset("lewtun/github-issues", split="train")
```

Filter out pull requests + commentless rows:

```py
issues_dataset = issues_dataset.filter(
    lambda x: (x["is_pull_request"] == False and len(x["comments"]) > 0)
)
# 771 rows
```

Drop unneeded columns:

```py
columns = issues_dataset.column_names
columns_to_keep = ["title", "body", "html_url", "comments"]
columns_to_remove = set(columns_to_keep).symmetric_difference(columns)
issues_dataset = issues_dataset.remove_columns(columns_to_remove)
```

**Explode** the `comments` column (one row per comment) — easier in Pandas:

```py
issues_dataset.set_format("pandas")
df = issues_dataset[:]
comments_df = df.explode("comments", ignore_index=True)
```

Back to a `Dataset`:

```py
from datasets import Dataset

comments_dataset = Dataset.from_pandas(comments_df)
# 2842 rows
```

Add a `comment_length` column and filter short comments:

```py
comments_dataset = comments_dataset.map(
    lambda x: {"comment_length": len(x["comments"].split())}
)
comments_dataset = comments_dataset.filter(lambda x: x["comment_length"] > 15)
# 2098 rows
```

Concatenate title + body + comment into a single `text` column:

```py
def concatenate_text(examples):
    return {
        "text": examples["title"]
        + " \n "
        + examples["body"]
        + " \n "
        + examples["comments"]
    }

comments_dataset = comments_dataset.map(concatenate_text)
```

## Creating text embeddings

Use `sentence-transformers/multi-qa-mpnet-base-dot-v1` — chosen because the search is **asymmetric** (short query, longer document).

PyTorch:

```py
from transformers import AutoTokenizer, AutoModel

model_ckpt = "sentence-transformers/multi-qa-mpnet-base-dot-v1"
tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
model = AutoModel.from_pretrained(model_ckpt)

import torch
device = torch.device("cuda")
model.to(device)
```

TensorFlow (`from_pt=True` converts PyTorch weights automatically):

```py
from transformers import AutoTokenizer, TFAutoModel

model_ckpt = "sentence-transformers/multi-qa-mpnet-base-dot-v1"
tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
model = TFAutoModel.from_pretrained(model_ckpt, from_pt=True)
```

**CLS pooling**:

```py
def cls_pooling(model_output):
    return model_output.last_hidden_state[:, 0]
```

Embedding helper (PyTorch):

```py
def get_embeddings(text_list):
    encoded_input = tokenizer(
        text_list, padding=True, truncation=True, return_tensors="pt"
    )
    encoded_input = {k: v.to(device) for k, v in encoded_input.items()}
    model_output = model(**encoded_input)
    return cls_pooling(model_output)

embedding = get_embeddings(comments_dataset["text"][0])
embedding.shape  # torch.Size([1, 768])
```

Embed the whole corpus into a new column:

```py
embeddings_dataset = comments_dataset.map(
    lambda x: {"embeddings": get_embeddings(x["text"]).detach().cpu().numpy()[0]}
)
```

TF variant uses `.numpy()[0]`.

## Using FAISS for efficient similarity search

**FAISS** (Facebook AI Similarity Search) provides efficient algorithms to search/cluster embedding vectors. 🤗 Datasets integrates via `Dataset.add_faiss_index()`:

```py
embeddings_dataset.add_faiss_index(column="embeddings")
```

Query:

```py
question = "How can I load a dataset offline?"
question_embedding = get_embeddings([question]).cpu().detach().numpy()
question_embedding.shape  # (1, 768)
```

```py
scores, samples = embeddings_dataset.get_nearest_examples(
    "embeddings", question_embedding, k=5
)
```

Sort and inspect:

```py
import pandas as pd

samples_df = pd.DataFrame.from_dict(samples)
samples_df["scores"] = scores
samples_df.sort_values("scores", ascending=False, inplace=True)

for _, row in samples_df.iterrows():
    print(f"COMMENT: {row.comments}")
    print(f"SCORE: {row.scores}")
    print(f"TITLE: {row.title}")
    print(f"URL: {row.html_url}")
    print("=" * 50)
    print()
```

Top matches surface the issue `Discussion using datasets in offline mode` (#824), suggesting `load_from_disk`/`save_to_disk` workarounds.

---

## Section 7: 🤗 Datasets, check!

# 🤗 Datasets, check![[datasets-check]]

With knowledge from this chapter you should be able to:

- Load datasets from anywhere — the Hub, your laptop, or a remote server.
- Wrangle your data using `Dataset.map()` and `Dataset.filter()`.
- Quickly switch formats (Pandas, NumPy, PyTorch, TensorFlow, JAX) via `Dataset.set_format()`.
- Create your own dataset and push it to the Hub.
- Embed documents with a Transformer model and build a semantic search engine using FAISS.

In Chapter 7, all of this powers core NLP task deep dives.
