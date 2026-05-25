# HuggingFace LLM Course — Chapter 6: The 🤗 Tokenizers library
Source: https://huggingface.co/learn/llm-course/chapter6/
Sections: 1,2,3,3b,4,5,6,7,8,9

---

## Section 1: Introduction

In [Chapter 3](/course/chapter3), we looked at how to fine-tune a model on a given task. When we do that, we use the same tokenizer that the model was pretrained with -- but what do we do when we want to train a model from scratch? In these cases, using a tokenizer that was pretrained on a corpus from another domain or language is typically suboptimal. For example, a tokenizer that's trained on an English corpus will perform poorly on a corpus of Japanese texts because the use of spaces and punctuation is very different in the two languages.

In this chapter, you will learn how to train a brand new tokenizer on a corpus of texts, so it can then be used to pretrain a language model. This will all be done with the help of the [🤗 Tokenizers](https://github.com/huggingface/tokenizers) library, which provides the "fast" tokenizers in the [🤗 Transformers](https://github.com/huggingface/transformers) library. We'll take a close look at the features that this library provides, and explore how the fast tokenizers differ from the "slow" versions.

Topics we will cover include:

* How to train a new tokenizer similar to the one used by a given checkpoint on a new corpus of texts
* The special features of fast tokenizers
* The differences between the three main subword tokenization algorithms used in NLP today
* How to build a tokenizer from scratch with the 🤗 Tokenizers library and train it on some data

The techniques introduced in this chapter will prepare you for the section in [Chapter 7](/course/chapter7/6) where we look at creating a language model for Python source code. Let's start by looking at what it means to "train" a tokenizer in the first place.

---

## Section 2: Training a new tokenizer from an old one

If a language model is not available in the language you are interested in, or if your corpus is very different from the one your language model was trained on, you will most likely want to retrain the model from scratch using a tokenizer adapted to your data. That will require training a new tokenizer on your dataset. But what exactly does that mean? When we first looked at tokenizers in [Chapter 2](/course/chapter2), we saw that most Transformer models use a _subword tokenization algorithm_. To identify which subwords are of interest and occur most frequently in the corpus at hand, the tokenizer needs to take a hard look at all the texts in the corpus -- a process we call *training*. The exact rules that govern this training depend on the type of tokenizer used, and we'll go over the three main algorithms later in this chapter.

> ⚠️ Training a tokenizer is not the same as training a model! Model training uses stochastic gradient descent to make the loss a little bit smaller for each batch. It's randomized by nature (meaning you have to set some seeds to get the same results when doing the same training twice). Training a tokenizer is a statistical process that tries to identify which subwords are the best to pick for a given corpus, and the exact rules used to pick them depend on the tokenization algorithm. It's deterministic, meaning you always get the same results when training with the same algorithm on the same corpus.

### Assembling a corpus

There's a very simple API in 🤗 Transformers that you can use to train a new tokenizer with the same characteristics as an existing one: `AutoTokenizer.train_new_from_iterator()`. To see this in action, let's say we want to train GPT-2 from scratch, but in a language other than English. Our first task will be to gather lots of data in that language in a training corpus. To provide examples everyone will be able to understand, we won't use a language like Russian or Chinese here, but rather a specialized English language: Python code.

The [🤗 Datasets](https://github.com/huggingface/datasets) library can help us assemble a corpus of Python source code. We'll use the usual `load_dataset()` function to download and cache the [CodeSearchNet](https://huggingface.co/datasets/code_search_net) dataset.

```py
from datasets import load_dataset
raw_datasets = load_dataset("code_search_net", "python")
```

```py
raw_datasets["train"]
```

```python out
Dataset({
    features: ['repository_name', 'func_path_in_repository', 'func_name', 'whole_func_string', 'language',
      'func_code_string', 'func_code_tokens', 'func_documentation_string', 'func_documentation_tokens', 'split_name',
      'func_code_url'
    ],
    num_rows: 412178
})
```

Use a Python generator (parentheses, not brackets) so the dataset isn't loaded into RAM:

```py
training_corpus = (
    raw_datasets["train"][i : i + 1000]["whole_func_string"]
    for i in range(0, len(raw_datasets["train"]), 1000)
)
```

Generators can only be used once, so wrap in a function:

```py
def get_training_corpus():
    return (
        raw_datasets["train"][i : i + 1000]["whole_func_string"]
        for i in range(0, len(raw_datasets["train"]), 1000)
    )
```

Or use `yield`:

```py
def get_training_corpus():
    dataset = raw_datasets["train"]
    for start_idx in range(0, len(dataset), 1000):
        samples = dataset[start_idx : start_idx + 1000]
        yield samples["whole_func_string"]
```

### Training a new tokenizer

```py
from transformers import AutoTokenizer
old_tokenizer = AutoTokenizer.from_pretrained("gpt2")
```

Inspect how GPT-2's tokenizer treats a function:

```py
example = '''def add_numbers(a, b):
    """Add the two numbers `a` and `b`."""
    return a + b'''
tokens = old_tokenizer.tokenize(example)
```

```python out
['def', 'Ġadd', '_', 'n', 'umbers', '(', 'a', ',', 'Ġb', '):', 'Ċ', 'Ġ', 'Ġ', 'Ġ', 'Ġ"""', 'Add', 'Ġthe', 'Ġtwo',
 'Ġnumbers', 'Ġ`', 'a', '`', 'Ġand', 'Ġ`', 'b', '`', '."', '""', 'Ċ', 'Ġ', 'Ġ', 'Ġ', 'Ġreturn', 'Ġa', 'Ġ+', 'Ġb']
```

`Ġ` denotes spaces, `Ċ` denotes newlines. Train a new tokenizer on the Python corpus:

```py
tokenizer = old_tokenizer.train_new_from_iterator(training_corpus, 52000)
```

This took 1 min 16 s on a Ryzen 9 3900X for 1.6 GB of texts. Note: `train_new_from_iterator()` only works with a fast tokenizer. The 🤗 Tokenizers library provides Python bindings to Rust code for parallelizable operations; pure-Python tokenizer training would be excruciatingly slow.

After training, the new tokenizer produces compact tokens specific to Python (e.g., `ĊĠĠĠ` for one indentation level, `Ġ"""` for docstring start, correct splitting on `_`):

```python out
['def', 'Ġadd', '_', 'numbers', '(', 'a', ',', 'Ġb', '):', 'ĊĠĠĠ', 'Ġ"""', 'Add', 'Ġthe', 'Ġtwo', 'Ġnumbers', 'Ġ`',
 'a', '`', 'Ġand', 'Ġ`', 'b', '`."""', 'ĊĠĠĠ', 'Ġreturn', 'Ġa', 'Ġ+', 'Ġb']
```

The new tokenizer used 27 tokens vs 36 for the old one. It also correctly splits camelCase: `LinearLayer` -> `["ĠLinear", "Layer"]`, and handles double indentation `ĊĠĠĠĠĠĠĠ`.

### Saving the tokenizer

```py
tokenizer.save_pretrained("code-search-net-tokenizer")
```

Login and push to the Hub:

```python
from huggingface_hub import notebook_login
notebook_login()
```

or `huggingface-cli login`, then:

```py
tokenizer.push_to_hub("code-search-net-tokenizer")
tokenizer = AutoTokenizer.from_pretrained("huggingface-course/code-search-net-tokenizer")
```

---

## Section 3: Fast tokenizers' special powers

Tokenizers in 🤗 Transformers backed by 🤗 Tokenizers can do much more than tokenize/decode. We will reproduce the `token-classification` (NER) and `question-answering` pipelines manually.

Slow tokenizers are written in Python inside 🤗 Transformers; fast versions are provided by 🤗 Tokenizers (Rust). Timing on Drug Review Dataset:

|               | Fast tokenizer | Slow tokenizer |
|:-------------:|:--------------:|:--------------:|
| `batched=True`  | 10.8s        | 4min41s        |
| `batched=False` | 59.2s        | 5min3s         |

> ⚠️ For a single sentence, fast may actually be slower; the advantage shows when tokenizing many texts in parallel.

### Batch encoding

The tokenizer returns a `BatchEncoding` object — a dict subclass with extra methods for fast tokenizers. Key feature: **offset mapping** — the span of original text each token came from.

```py
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
example = "My name is Sylvain and I work at Hugging Face in Brooklyn."
encoding = tokenizer(example)
print(type(encoding))  # transformers.tokenization_utils_base.BatchEncoding
```

Check whether tokenizer is fast:

```python
tokenizer.is_fast        # True
encoding.is_fast         # True
```

Get tokens directly (no ID→token conversion):

```py
encoding.tokens()
# ['[CLS]', 'My', 'name', 'is', 'S', '##yl', '##va', '##in', 'and', 'I', 'work', 'at', 'Hu', '##gging', 'Face',
#  'in', 'Brooklyn', '.', '[SEP]']
```

Map tokens back to original words via `word_ids()`:

```py
encoding.word_ids()
# [None, 0, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, None]
```

`[CLS]`/`[SEP]` map to `None`. Useful for NER/POS label propagation and whole-word masking. Works for any fast tokenizer (not just `##`-prefixed ones).

Map any word/token to characters and vice versa:

```py
start, end = encoding.word_to_chars(3)
example[start:end]   # 'Sylvain'
```

Other methods: `sentence_ids()`, `token_to_chars()`, `char_to_word()`, `char_to_token()`.

### Inside the token-classification pipeline

Default model is `dbmdz/bert-large-cased-finetuned-conll03-english`.

```py
from transformers import pipeline
token_classifier = pipeline("token-classification")
token_classifier("My name is Sylvain and I work at Hugging Face in Brooklyn.")
# returns list of {entity, score, index, word, start, end}
```

`aggregation_strategy="simple"` groups consecutive `I-XXX` tokens — scores: `"simple"` (mean), `"first"` (first token score), `"max"` (max in entity), `"average"` (avg by word).

Reproduce manually:

```py
from transformers import AutoTokenizer, AutoModelForTokenClassification
model_checkpoint = "dbmdz/bert-large-cased-finetuned-conll03-english"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForTokenClassification.from_pretrained(model_checkpoint)
inputs = tokenizer(example, return_tensors="pt")
outputs = model(**inputs)
# inputs.input_ids.shape = torch.Size([1, 19])
# outputs.logits.shape = torch.Size([1, 19, 9])

import torch
probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)[0].tolist()
predictions = outputs.logits.argmax(dim=-1)[0].tolist()
```

Labels: `id2label = {0:'O',1:'B-MISC',2:'I-MISC',3:'B-PER',4:'I-PER',5:'B-ORG',6:'I-ORG',7:'B-LOC',8:'I-LOC'}`.

Two formats: **IOB1** (B- only separates same-type adjacents) and **IOB2** (B- starts every entity). The model used IOB1, so `S ##yl ##va ##in` are all `I-PER`.

Get character offsets:

```py
inputs_with_offsets = tokenizer(example, return_offsets_mapping=True)
inputs_with_offsets["offset_mapping"]
# [(0,0),(0,2),(3,7),(8,10),(11,12),(12,14),(14,16),(16,18),(19,22),(23,24),(25,29),(30,32),
#  (33,35),(35,40),(41,45),(46,48),(49,57),(57,58),(0,0)]
```

`(0,0)` reserved for special tokens. Use offsets to enrich predictions with `start`/`end`.

### Grouping entities

With offsets, just take the span from the first to the last token of a grouped entity — works regardless of tokenizer style (BPE, WordPiece, SentencePiece):

```py
import numpy as np
results = []
inputs_with_offsets = tokenizer(example, return_offsets_mapping=True)
tokens = inputs_with_offsets.tokens()
offsets = inputs_with_offsets["offset_mapping"]

idx = 0
while idx < len(predictions):
    pred = predictions[idx]
    label = model.config.id2label[pred]
    if label != "O":
        label = label[2:]  # strip B- / I-
        start, _ = offsets[idx]
        all_scores = []
        while (idx < len(predictions)
               and model.config.id2label[predictions[idx]] == f"I-{label}"):
            all_scores.append(probabilities[idx][pred])
            _, end = offsets[idx]
            idx += 1
        score = np.mean(all_scores).item()
        word = example[start:end]
        results.append({"entity_group": label, "score": score,
                        "word": word, "start": start, "end": end})
    idx += 1
```

---

## Section 3b: Fast tokenizers in the QA pipeline

### Using the question-answering pipeline

```py
from transformers import pipeline
question_answerer = pipeline("question-answering")
context = "🤗 Transformers is backed by the three most popular deep learning libraries — Jax, PyTorch, and TensorFlow ..."
question = "Which deep learning libraries back 🤗 Transformers?"
question_answerer(question=question, context=context)
# {'score': 0.97773, 'start': 78, 'end': 105, 'answer': 'Jax, PyTorch and TensorFlow'}
```

Unlike other pipelines, QA can deal with very long contexts (splits into chunks).

### Using a model for question answering

Default checkpoint: `distilbert-base-cased-distilled-squad`.

```py
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
model_checkpoint = "distilbert-base-cased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForQuestionAnswering.from_pretrained(model_checkpoint)
inputs = tokenizer(question, context, return_tensors="pt")
outputs = model(**inputs)
```

Question first, then context as a pair. QA model outputs two logit tensors: `start_logits` and `end_logits`.

Mask non-context positions (everything except `sequence_ids == 1`) with `-10000`, but keep `[CLS]` (some models use it to say "answer not in context"). Apply softmax.

```py
sequence_ids = inputs.sequence_ids()
mask = [i != 1 for i in sequence_ids]
mask[0] = False
mask = torch.tensor(mask)[None]
start_logits[mask] = -10000
end_logits[mask] = -10000
start_probabilities = torch.nn.functional.softmax(start_logits, dim=-1)[0]
end_probabilities   = torch.nn.functional.softmax(end_logits,   dim=-1)[0]
```

Compute outer product, mask lower-triangle (require `start_index <= end_index`) via `torch.triu`, take argmax:

```py
scores = start_probabilities[:, None] * end_probabilities[None, :]
scores = torch.triu(scores)
max_index = scores.argmax().item()
start_index = max_index // scores.shape[1]
end_index   = max_index  % scores.shape[1]
```

Convert token indices to character spans via offsets:

```py
inputs_with_offsets = tokenizer(question, context, return_offsets_mapping=True)
offsets = inputs_with_offsets["offset_mapping"]
start_char, _ = offsets[start_index]
_, end_char   = offsets[end_index]
answer = context[start_char:end_char]
```

### Handling long contexts

If `len(input_ids) > 384`, truncate. Strategy `"only_second"` keeps the question intact. But the answer may then be cut. Solution: chunk with overlap using `return_overflowing_tokens=True` and `stride`:

```py
inputs = tokenizer(sentence, truncation=True,
                   return_overflowing_tokens=True, max_length=6, stride=2)
```

This produces sliding windows; `overflow_to_sample_mapping` maps each chunk back to its source sample.

Pipeline defaults: `max_length=384`, `stride=128`. Full pipeline:

```py
inputs = tokenizer(
    question, long_context,
    stride=128, max_length=384,
    padding="longest", truncation="only_second",
    return_overflowing_tokens=True, return_offsets_mapping=True,
)
_ = inputs.pop("overflow_to_sample_mapping")
offsets = inputs.pop("offset_mapping")
inputs = inputs.convert_to_tensors("pt")
```

Apply masking (also mask `[PAD]` via `attention_mask == 0`), softmax, then loop over chunks scoring start/end candidates with `torch.triu`. Map best (start, end) tokens back to chars via the per-chunk offsets:

```python out
[(0, 18, 0.33867), (173, 184, 0.97149)]
# -> {'answer': 'Jax, PyTorch and TensorFlow', 'start': 1892, 'end': 1919, 'score': 0.97149}
```

---

## Section 4: Normalization and pre-tokenization

Two preprocessing steps before the model:

### Normalization

Cleanup: removing whitespace, lowercasing, removing accents, Unicode normalization (NFC, NFKC, NFD, NFKD).

```py
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
print(type(tokenizer.backend_tokenizer))
# tokenizers.Tokenizer
print(tokenizer.backend_tokenizer.normalizer.normalize_str("Héllò hôw are ü?"))
# 'hello how are u?'
```

### Pre-tokenization

Splits text into words (the boundaries within which subwords are learned).

```py
tokenizer.backend_tokenizer.pre_tokenizer.pre_tokenize_str("Hello, how are  you?")
# BERT: splits on whitespace + punctuation, collapses double space
# [('Hello',(0,5)),(',',(5,6)),('how',(7,10)),('are',(11,14)),('you',(16,19)),('?',(19,20))]
```

GPT-2 keeps spaces as `Ġ`:

```python out
[('Hello',(0,5)),(',',(5,6)),('Ġhow',(6,10)),('Ġare',(10,14)),('Ġ',(14,15)),('Ġyou',(15,19)),('?',(19,20))]
```

T5 (SentencePiece): only splits on whitespace, uses `▁`, adds leading space:

```python out
[('▁Hello,',(0,6)),('▁how',(7,10)),('▁are',(11,14)),('▁you?',(16,20))]
```

### SentencePiece

Treats text as a Unicode stream, replaces spaces with `▁`. Used with Unigram needs no pre-tokenization step — works for languages without spaces (Chinese, Japanese). Tokenization is **reversible**: concat tokens, replace `▁` with space. BERT's tokenizer is NOT reversible because it collapses repeated spaces.

### Algorithm overview

| Model | BPE | WordPiece | Unigram |
|:----:|:---:|:---------:|:------:|
| Training | Small vocab + learn merge rules | Small vocab + learn merge rules | Large vocab + learn token removals |
| Step | Merge most common pair | Merge pair with best score (freq_pair / (freq_a × freq_b)) | Remove tokens minimizing loss on whole corpus |
| Learns | Merges + vocab | Just vocab | Vocab with score per token |
| Encoding | Split into chars, apply merges in order | Longest-prefix-match in vocab, repeat | Most likely segmentation per scores (Viterbi) |

---

## Section 5: Byte-Pair Encoding tokenization

BPE was a compression algorithm later used by OpenAI for GPT. Used by GPT, GPT-2, RoBERTa, BART, DeBERTa.

### Training algorithm

After normalization + pre-tokenization, compute unique words and base vocabulary (all symbols / characters used). Example corpus `"hug","pug","pun","bun","hugs"` → base vocab `["b","g","h","n","p","s","u"]`. Real BPE base includes all ASCII (plus possibly Unicode). Out-of-base chars → unknown token. **Byte-level BPE** (GPT-2/RoBERTa) avoids this by tokenizing bytes (256 base) — no unknown tokens.

Iteratively: find most frequent pair, add it as a merge rule, repeat.

With frequencies `("hug",10),("pug",5),("pun",12),("bun",4),("hugs",5)`:
- `("u","g")` appears 20 times → merge → vocab adds `"ug"`.
- Next most frequent `("u","n")` (16) → adds `"un"`.
- Then `("h","ug")` (15) → adds `"hug"`.

### Tokenization algorithm

Normalize → pre-tokenize → split into chars → apply merge rules in order.

- `"bug"` → `["b","ug"]`
- `"mug"` → `["[UNK]","ug"]` (m not in base)
- `"thug"` → `["[UNK]","hug"]`

### Implementing BPE

```python
corpus = [
    "This is the Hugging Face Course.",
    "This chapter is about tokenization.",
    "This section shows several tokenizer algorithms.",
    "Hopefully, you will be able to understand how they are trained and generate tokens.",
]
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")

from collections import defaultdict
word_freqs = defaultdict(int)
for text in corpus:
    words_with_offsets = tokenizer.backend_tokenizer.pre_tokenizer.pre_tokenize_str(text)
    new_words = [word for word, offset in words_with_offsets]
    for word in new_words:
        word_freqs[word] += 1

alphabet = []
for word in word_freqs.keys():
    for letter in word:
        if letter not in alphabet:
            alphabet.append(letter)
alphabet.sort()

vocab = ["<|endoftext|>"] + alphabet.copy()
splits = {word: [c for c in word] for word in word_freqs.keys()}

def compute_pair_freqs(splits):
    pair_freqs = defaultdict(int)
    for word, freq in word_freqs.items():
        split = splits[word]
        if len(split) == 1: continue
        for i in range(len(split) - 1):
            pair = (split[i], split[i+1])
            pair_freqs[pair] += freq
    return pair_freqs

def merge_pair(a, b, splits):
    for word in word_freqs:
        split = splits[word]
        if len(split) == 1: continue
        i = 0
        while i < len(split) - 1:
            if split[i] == a and split[i+1] == b:
                split = split[:i] + [a + b] + split[i+2:]
            else:
                i += 1
        splits[word] = split
    return splits

vocab_size = 50
merges = {}
while len(vocab) < vocab_size:
    pair_freqs = compute_pair_freqs(splits)
    best_pair, max_freq = "", None
    for pair, freq in pair_freqs.items():
        if max_freq is None or max_freq < freq:
            best_pair, max_freq = pair, freq
    splits = merge_pair(*best_pair, splits)
    merges[best_pair] = best_pair[0] + best_pair[1]
    vocab.append(best_pair[0] + best_pair[1])
```

Tokenize new text:

```python
def tokenize(text):
    pre_tokenize_result = tokenizer._tokenizer.pre_tokenizer.pre_tokenize_str(text)
    pre_tokenized_text = [word for word, offset in pre_tokenize_result]
    splits = [[l for l in word] for word in pre_tokenized_text]
    for pair, merge in merges.items():
        for idx, split in enumerate(splits):
            i = 0
            while i < len(split) - 1:
                if split[i] == pair[0] and split[i+1] == pair[1]:
                    split = split[:i] + [merge] + split[i+2:]
                else:
                    i += 1
            splits[idx] = split
    return sum(splits, [])
```

Note: byte-level BPE means GPT-2 has no unknown token; this naive impl would error on unknown chars.

---

## Section 6: WordPiece tokenization

Developed by Google for BERT; reused by DistilBERT, MobileBERT, Funnel Transformers, MPNET. Training is similar to BPE; **tokenization is different**. Google never open-sourced the training implementation — the description is best guess.

### Training algorithm

Start from small vocab including the special tokens and base alphabet. Add WordPiece prefix `##` to all non-leading characters: `"word"` → `w ##o ##r ##d`. Base alphabet = leading chars + `##` + inner chars.

Pair selection uses a **score**:

$$\mathrm{score} = \frac{\mathrm{freq\_of\_pair}}{\mathrm{freq\_of\_first} \times \mathrm{freq\_of\_second}}$$

Prioritizes pairs where the parts are individually less frequent. Example: `("un","##able")` won't be merged eagerly even if frequent, because both parts are common; `("hu","##gging")` merges fast because parts are rare.

Same `"hug","pug","pun","bun","hugs"` corpus, splits become `("h","##u","##g"), ...`. Highest-frequency pair `("##u","##g")` scores only 1/36; best is `("##g","##s")` at 1/20 → merge to `"##gs"` (drop `##` between).

### Tokenization algorithm

WordPiece **only saves the vocabulary**, not the merges. Longest-prefix-match in vocab, then continue on remainder with `##` prefix.

- `"hugs"` → `["hug","##s"]` (longest match `"hug"` then `"##s"`).
- BPE on same vocab would give `["hu","##gs"]`.
- `"bugs"` → `["b","##u","##gs"]`.
- `"mug"` → `["[UNK]"]` (no leading char match → whole word unknown, unlike BPE which only marks the missing char).

### Implementing WordPiece

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

alphabet = []
for word in word_freqs.keys():
    if word[0] not in alphabet:
        alphabet.append(word[0])
    for letter in word[1:]:
        if f"##{letter}" not in alphabet:
            alphabet.append(f"##{letter}")
alphabet.sort()
vocab = ["[PAD]","[UNK]","[CLS]","[SEP]","[MASK]"] + alphabet.copy()
splits = {word: [c if i == 0 else f"##{c}" for i, c in enumerate(word)]
          for word in word_freqs.keys()}

def compute_pair_scores(splits):
    letter_freqs = defaultdict(int); pair_freqs = defaultdict(int)
    for word, freq in word_freqs.items():
        split = splits[word]
        if len(split) == 1:
            letter_freqs[split[0]] += freq; continue
        for i in range(len(split) - 1):
            pair = (split[i], split[i+1])
            letter_freqs[split[i]] += freq
            pair_freqs[pair] += freq
        letter_freqs[split[-1]] += freq
    return {pair: freq / (letter_freqs[pair[0]] * letter_freqs[pair[1]])
            for pair, freq in pair_freqs.items()}

def encode_word(word):
    tokens = []
    while len(word) > 0:
        i = len(word)
        while i > 0 and word[:i] not in vocab:
            i -= 1
        if i == 0: return ["[UNK]"]
        tokens.append(word[:i])
        word = word[i:]
        if len(word) > 0: word = f"##{word}"
    return tokens
```

Note: 🤗 Tokenizers does not actually train WordPiece — it uses BPE training and applies WordPiece tokenization at inference. So `train_new_from_iterator()` won't reproduce this exactly.

---

## Section 7: Unigram tokenization

Used with SentencePiece; powers AlBERT, T5, mBART, Big Bird, XLNet.

### Training algorithm

Unigram works in reverse: starts with a **big** vocab and **removes** tokens. Initial vocab options: most common substrings of pre-tokenized words, or BPE with large vocab size.

At each step, compute corpus loss; for each token, compute increase in loss if removed; remove the bottom *p%* (typically 10–20%) — never remove base characters. Repeat until target size.

### Tokenization algorithm

Unigram model: token probability is independent of context. P(token) = freq(token) / Σ freq. Probability of a segmentation = product of token probabilities.

Frequencies for `("hug",10),("pug",5),("pun",12),("bun",4),("hugs",5)`:

```
("h",15) ("u",36) ("g",20) ("hu",15) ("ug",20) ("p",17) ("pu",17) ("n",16)
("un",16) ("b",4) ("bu",4) ("s",5) ("hug",15) ("gs",5) ("ugs",5)
```

Sum = 210. P("ug") = 20/210.

Segmentations of `"pug"`:
- `["p","u","g"]` = 5/210 × 36/210 × 20/210 = 0.000389
- `["p","ug"]` = 5/210 × 20/210 = 0.0022676
- `["pu","g"]` = 5/210 × 20/210 = 0.0022676

Fewer-token segmentations win. To find best segmentation in general: **Viterbi algorithm** — graph where branches are vocab subwords with their probabilities; for each position keep the best score reaching it; backtrack.

Example for `"unhug"`:
```
Char 0 (u): "u" (0.171429)
Char 1 (n): "un" (0.076191)
Char 2 (h): "un" "h" (0.005442)
Char 3 (u): "un" "hu" (0.005442)
Char 4 (g): "un" "hug" (0.005442)
```
→ `["un","hug"]`.

### Back to training

Corpus loss = Σ freq(word) × (−log P(best_segmentation(word))). For example corpus, loss ≈ 169.8. Removing `"pu"` doesn't change tokenizations (equivalence) → 0 loss change. Removing `"hug"` forces `"hu","g"` and `"hu","gs"` → loss rises by ≈ 23.5.

### Implementing Unigram

Use `xlnet-base-cased` for pre-tokenization. Build initial vocab from char_freqs + top-300 subwords:

```python
char_freqs = defaultdict(int); subwords_freqs = defaultdict(int)
for word, freq in word_freqs.items():
    for i in range(len(word)):
        char_freqs[word[i]] += freq
        for j in range(i + 2, len(word) + 1):
            subwords_freqs[word[i:j]] += freq
sorted_subwords = sorted(subwords_freqs.items(), key=lambda x: x[1], reverse=True)
token_freqs = dict(list(char_freqs.items()) + sorted_subwords[:300 - len(char_freqs)])

from math import log
total = sum(token_freqs.values())
model = {tok: -log(freq / total) for tok, freq in token_freqs.items()}
```

SentencePiece uses Enhanced Suffix Array (ESA) for an efficient initial vocab.

Viterbi:

```python
def encode_word(word, model):
    best_segmentations = [{"start":0,"score":1}] + [
        {"start":None,"score":None} for _ in range(len(word))]
    for start_idx in range(len(word)):
        best_score_at_start = best_segmentations[start_idx]["score"]
        for end_idx in range(start_idx + 1, len(word) + 1):
            token = word[start_idx:end_idx]
            if token in model and best_score_at_start is not None:
                score = model[token] + best_score_at_start
                if (best_segmentations[end_idx]["score"] is None
                    or best_segmentations[end_idx]["score"] > score):
                    best_segmentations[end_idx] = {"start": start_idx, "score": score}
    segmentation = best_segmentations[-1]
    if segmentation["score"] is None: return ["<unk>"], None
    score = segmentation["score"]; start = segmentation["start"]; end = len(word)
    tokens = []
    while start != 0:
        tokens.insert(0, word[start:end])
        next_start = best_segmentations[start]["start"]
        end = start; start = next_start
    tokens.insert(0, word[start:end])
    return tokens, score
```

Pruning loop:

```python
percent_to_remove = 0.1
while len(model) > 100:
    scores = compute_scores(model)
    sorted_scores = sorted(scores.items(), key=lambda x: x[1])
    for i in range(int(len(model) * percent_to_remove)):
        _ = token_freqs.pop(sorted_scores[i][0])
    total = sum(token_freqs.values())
    model = {t: -log(f/total) for t,f in token_freqs.items()}
```

SentencePiece approximates loss-without-token-X by replacing X with its segmentation in remaining vocab — so all scores can be computed at once alongside model loss.

To decode SentencePiece output, concatenate tokens and replace `▁` with space.

---

## Section 8: Building a tokenizer, block by block

Tokenization pipeline = Normalization + Pre-tokenization + Model + Post-processing.

The `tokenizers` library exposes submodules:
- `normalizers` — `Normalizer` types
- `pre_tokenizers` — `PreTokenizer` types
- `models` — `BPE`, `WordPiece`, `Unigram`
- `trainers` — one per model
- `post_processors` — `PostProcessor` types
- `decoders` — `Decoder` types

### Acquiring a corpus

```python
from datasets import load_dataset
dataset = load_dataset("wikitext", name="wikitext-2-raw-v1", split="train")
def get_training_corpus():
    for i in range(0, len(dataset), 1000):
        yield dataset[i : i + 1000]["text"]
```

Or write a single text file:

```python
with open("wikitext-2.txt", "w", encoding="utf-8") as f:
    for i in range(len(dataset)):
        f.write(dataset[i]["text"] + "\n")
```

### Building a WordPiece tokenizer from scratch (BERT)

```python
from tokenizers import (decoders, models, normalizers, pre_tokenizers,
                        processors, trainers, Tokenizer)

tokenizer = Tokenizer(models.WordPiece(unk_token="[UNK]"))

# Normalizer — pre-built BertNormalizer:
tokenizer.normalizer = normalizers.BertNormalizer(lowercase=True)
# Or compose by hand:
tokenizer.normalizer = normalizers.Sequence(
    [normalizers.NFD(), normalizers.Lowercase(), normalizers.StripAccents()]
)

# Pre-tokenizer — pre-built:
tokenizer.pre_tokenizer = pre_tokenizers.BertPreTokenizer()
# Or from scratch:
tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()
# Whitespace splits on whitespace + non-word chars; WhitespaceSplit only on whitespace.
# Compose with Sequence:
pre_tokenizer = pre_tokenizers.Sequence(
    [pre_tokenizers.WhitespaceSplit(), pre_tokenizers.Punctuation()]
)

# Trainer (must declare special tokens explicitly!):
special_tokens = ["[UNK]","[PAD]","[CLS]","[SEP]","[MASK]"]
trainer = trainers.WordPieceTrainer(vocab_size=25000, special_tokens=special_tokens)

# Train:
tokenizer.train_from_iterator(get_training_corpus(), trainer=trainer)
# Or:
tokenizer.model = models.WordPiece(unk_token="[UNK]")
tokenizer.train(["wikitext-2.txt"], trainer=trainer)

encoding = tokenizer.encode("Let's test this tokenizer.")
# ['let', "'", 's', 'test', 'this', 'tok', '##eni', '##zer', '.']
```

`Encoding` attrs: `ids`, `type_ids`, `tokens`, `offsets`, `attention_mask`, `special_tokens_mask`, `overflowing`.

Post-processing with `TemplateProcessing`:

```python
cls_token_id = tokenizer.token_to_id("[CLS]")
sep_token_id = tokenizer.token_to_id("[SEP]")
tokenizer.post_processor = processors.TemplateProcessing(
    single=f"[CLS]:0 $A:0 [SEP]:0",
    pair=f"[CLS]:0 $A:0 [SEP]:0 $B:1 [SEP]:1",
    special_tokens=[("[CLS]", cls_token_id), ("[SEP]", sep_token_id)],
)
```

Decoder + save:

```python
tokenizer.decoder = decoders.WordPiece(prefix="##")
tokenizer.save("tokenizer.json")
new_tokenizer = Tokenizer.from_file("tokenizer.json")
```

Wrap for 🤗 Transformers:

```python
from transformers import PreTrainedTokenizerFast
wrapped_tokenizer = PreTrainedTokenizerFast(
    tokenizer_object=tokenizer,
    unk_token="[UNK]", pad_token="[PAD]",
    cls_token="[CLS]", sep_token="[SEP]", mask_token="[MASK]",
)
# Or use BertTokenizerFast(tokenizer_object=tokenizer).
```

### Building a BPE tokenizer from scratch (GPT-2)

```python
tokenizer = Tokenizer(models.BPE())
# No normalizer for GPT-2; no unk_token needed (byte-level).
tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
trainer = trainers.BpeTrainer(vocab_size=25000, special_tokens=["<|endoftext|>"])
tokenizer.train_from_iterator(get_training_corpus(), trainer=trainer)

tokenizer.post_processor = processors.ByteLevel(trim_offsets=False)
# trim_offsets=False keeps the leading space inside the offset of 'Ġ'-prefixed tokens.

tokenizer.decoder = decoders.ByteLevel()
# Wrap with PreTrainedTokenizerFast or GPT2TokenizerFast.
```

### Building a Unigram tokenizer from scratch (XLNet)

```python
tokenizer = Tokenizer(models.Unigram())

from tokenizers import Regex
tokenizer.normalizer = normalizers.Sequence([
    normalizers.Replace("``", '"'),
    normalizers.Replace("''", '"'),
    normalizers.NFKD(),
    normalizers.StripAccents(),
    normalizers.Replace(Regex(" {2,}"), " "),
])
tokenizer.pre_tokenizer = pre_tokenizers.Metaspace()

special_tokens = ["<cls>","<sep>","<unk>","<pad>","<mask>","<s>","</s>"]
trainer = trainers.UnigramTrainer(
    vocab_size=25000, special_tokens=special_tokens, unk_token="<unk>"
)
# UnigramTrainer extra args: shrinking_factor (0.75), max_piece_length (16).

tokenizer.train_from_iterator(get_training_corpus(), trainer=trainer)

cls_token_id = tokenizer.token_to_id("<cls>")
sep_token_id = tokenizer.token_to_id("<sep>")
tokenizer.post_processor = processors.TemplateProcessing(
    single="$A:0 <sep>:0 <cls>:2",
    pair="$A:0 <sep>:0 $B:1 <sep>:1 <cls>:2",
    special_tokens=[("<sep>", sep_token_id), ("<cls>", cls_token_id)],
)
tokenizer.decoder = decoders.Metaspace()
```

XLNet appends `<cls>` (type id 2) and pads on the left:

```python
from transformers import PreTrainedTokenizerFast
wrapped_tokenizer = PreTrainedTokenizerFast(
    tokenizer_object=tokenizer,
    bos_token="<s>", eos_token="</s>",
    unk_token="<unk>", pad_token="<pad>",
    cls_token="<cls>", sep_token="<sep>", mask_token="<mask>",
    padding_side="left",
)
# Or XLNetTokenizerFast(tokenizer_object=tokenizer).
```

---

## Section 9: Tokenizers, check!

Great job finishing this chapter! After this deep dive into tokenizers, you should:

- Be able to train a new tokenizer using an old one as a template
- Understand how to use offsets to map tokens' positions to their original span of text
- Know the differences between BPE, WordPiece, and Unigram
- Be able to mix and match the blocks provided by the 🤗 Tokenizers library to build your own tokenizer
- Be able to use that tokenizer inside the 🤗 Transformers library
