# HuggingFace LLM Course — Chapter 7: Classical NLP tasks
Source: https://huggingface.co/learn/llm-course/chapter7/
Sections: 1,2,3,4,5,6,7,8
---

## Section 1: Introduction

# Introduction[[introduction]]

In [Chapter 3](/course/chapter3), you saw how to fine-tune a model for text classification. In this chapter, we will tackle the following common language tasks that are essential for working with both traditional NLP models and modern LLMs:

- Token classification
- Masked language modeling (like BERT)
- Summarization
- Translation
- Causal language modeling pretraining (like GPT-2)
- Question answering

These fundamental tasks form the foundation of how Large Language Models (LLMs) work and understanding them is crucial for effectively working with today's most advanced language models.

To do this, you'll need to leverage everything you learned about the `Trainer` API and the Accelerate library in Chapter 3, the Datasets library in Chapter 5, and the Tokenizers library in Chapter 6. We'll also upload our results to the Model Hub, like we did in Chapter 4, so this is really the chapter where everything comes together.

Each section can be read independently and will show you how to train a model with the `Trainer` API or with your own training loop, using Accelerate. The `Trainer` API is great for fine-tuning or training your model without worrying about what's going on behind the scenes, while the training loop with `Accelerate` will let you customize any part you want more easily.

> If you read the sections in sequence, you will notice that they have quite a bit of code and prose in common. The repetition is intentional, to allow you to dip in (or come back later) to any task that interests you and find a complete working example.

---

## Section 2: Token classification

# Token classification[[token-classification]]

The first application we'll explore is token classification. This generic task encompasses any problem that can be formulated as "attributing a label to each token in a sentence," such as:

- **Named entity recognition (NER)**: Find the entities (such as persons, locations, or organizations) in a sentence. This can be formulated as attributing a label to each token by having one class per entity and one class for "no entity."
- **Part-of-speech tagging (POS)**: Mark each word in a sentence as corresponding to a particular part of speech (such as noun, verb, adjective, etc.).
- **Chunking**: Find the tokens that belong to the same entity. This task (which can be combined with POS or NER) can be formulated as attributing one label (usually `B-`) to any tokens that are at the beginning of a chunk, another label (usually `I-`) to tokens that are inside a chunk, and a third label (usually `O`) to tokens that don't belong to any chunk.

In this section, we will fine-tune a model (BERT) on a NER task.

## Preparing the data

We use the [CoNLL-2003 dataset](https://huggingface.co/datasets/conll2003), which contains news stories from Reuters.

```py
from datasets import load_dataset
raw_datasets = load_dataset("conll2003")
```

```python out
DatasetDict({
    train: Dataset({features: ['chunk_tags', 'id', 'ner_tags', 'pos_tags', 'tokens'], num_rows: 14041})
    validation: Dataset({features: [...], num_rows: 3250})
    test: Dataset({features: [...], num_rows: 3453})
})
```

The dataset contains labels for NER, POS, and chunking. Inputs are pre-tokenized lists of words. Example:

```py
raw_datasets["train"][0]["tokens"]
# ['EU', 'rejects', 'German', 'call', 'to', 'boycott', 'British', 'lamb', '.']
raw_datasets["train"][0]["ner_tags"]
# [3, 0, 7, 0, 0, 0, 7, 0, 0]
```

Label names:
```py
label_names = ['O', 'B-PER', 'I-PER', 'B-ORG', 'I-ORG', 'B-LOC', 'I-LOC', 'B-MISC', 'I-MISC']
```

- `O` — no entity
- `B-PER`/`I-PER` — person entity beginning / inside
- `B-ORG`/`I-ORG` — organization
- `B-LOC`/`I-LOC` — location
- `B-MISC`/`I-MISC` — miscellaneous

Decoding example yields: `EU(B-ORG) rejects(O) German(B-MISC) call(O) ... British(B-MISC) lamb(O) .(O)`. Multi-word entities like "European Union" / "Werner Zwingmann" get `B-` for the first word and `I-` for the rest.

## Processing the data

Tokenize pre-tokenized input with `is_split_into_words=True`:

```py
from transformers import AutoTokenizer
model_checkpoint = "bert-base-cased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
inputs = tokenizer(raw_datasets["train"][0]["tokens"], is_split_into_words=True)
inputs.tokens()
# ['[CLS]', 'EU', 'rejects', 'German', 'call', 'to', 'boycott', 'British', 'la', '##mb', '.', '[SEP]']
```

The word `lamb` is split into `la`/`##mb`, introducing a mismatch between tokens and labels. Use `inputs.word_ids()` (fast tokenizer feature) to align labels:

```python
def align_labels_with_tokens(labels, word_ids):
    new_labels = []
    current_word = None
    for word_id in word_ids:
        if word_id != current_word:
            current_word = word_id
            label = -100 if word_id is None else labels[word_id]
            new_labels.append(label)
        elif word_id is None:
            new_labels.append(-100)
        else:
            label = labels[word_id]
            # If the label is B-XXX we change it to I-XXX
            if label % 2 == 1:
                label += 1
            new_labels.append(label)
    return new_labels
```

Special tokens are labeled `-100` (ignored in cross-entropy loss). Subsequent subtokens inherit the word label, with `B-` → `I-`.

Batched preprocessing:

```py
def tokenize_and_align_labels(examples):
    tokenized_inputs = tokenizer(examples["tokens"], truncation=True, is_split_into_words=True)
    all_labels = examples["ner_tags"]
    new_labels = []
    for i, labels in enumerate(all_labels):
        word_ids = tokenized_inputs.word_ids(i)
        new_labels.append(align_labels_with_tokens(labels, word_ids))
    tokenized_inputs["labels"] = new_labels
    return tokenized_inputs

tokenized_datasets = raw_datasets.map(tokenize_and_align_labels, batched=True, remove_columns=raw_datasets["train"].column_names)
```

## Data collation

Use `DataCollatorForTokenClassification` — it pads labels with `-100` so they match input padding.

```py
from transformers import DataCollatorForTokenClassification
data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)
```

## Metrics

Use **seqeval** loaded via `evaluate.load("seqeval")`. Decoded predictions and references (excluding `-100`) are passed; the metric returns per-entity precision/recall/F1 and overall scores.

```py
def compute_metrics(eval_preds):
    logits, labels = eval_preds
    predictions = np.argmax(logits, axis=-1)
    true_labels = [[label_names[l] for l in label if l != -100] for label in labels]
    true_predictions = [
        [label_names[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    all_metrics = metric.compute(predictions=true_predictions, references=true_labels)
    return {
        "precision": all_metrics["overall_precision"],
        "recall": all_metrics["overall_recall"],
        "f1": all_metrics["overall_f1"],
        "accuracy": all_metrics["overall_accuracy"],
    }
```

Reported example results: LOC F1 0.91, MISC F1 0.74, ORG F1 0.88, PER F1 0.95, overall F1 0.89, accuracy 0.97.

## Model & training

```py
from transformers import AutoModelForTokenClassification
id2label = {i: label for i, label in enumerate(label_names)}
label2id = {v: k for k, v in id2label.items()}
model = AutoModelForTokenClassification.from_pretrained(model_checkpoint, id2label=id2label, label2id=label2id)
```

Warning: wrong `num_labels` causes obscure "CUDA error: device-side assert triggered" — verify `model.config.num_labels == 9`.

```py
from transformers import TrainingArguments, Trainer
args = TrainingArguments(
    "bert-finetuned-ner",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    num_train_epochs=3,
    weight_decay=0.01,
    push_to_hub=True,
)
trainer = Trainer(
    model=model, args=args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    compute_metrics=compute_metrics,
    processing_class=tokenizer,
)
trainer.train()
```

## Custom training loop with Accelerate

Key steps: `DataLoader`s with `data_collator`, `AdamW(lr=2e-5)`, `accelerator.prepare(...)`, linear LR scheduler, training loop with `accelerator.backward(loss)`. Evaluation requires `accelerator.pad_across_processes(...)` before `gather()` because two processes may pad to different shapes.

```py
def postprocess(predictions, labels):
    predictions = predictions.detach().cpu().clone().numpy()
    labels = labels.detach().cpu().clone().numpy()
    true_labels = [[label_names[l] for l in label if l != -100] for label in labels]
    true_predictions = [[label_names[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)]
    return true_labels, true_predictions
```

## Pipeline use

```py
from transformers import pipeline
token_classifier = pipeline("token-classification", model="huggingface-course/bert-finetuned-ner", aggregation_strategy="simple")
token_classifier("My name is Sylvain and I work at Hugging Face in Brooklyn.")
# [{'entity_group': 'PER', ...}, {'entity_group': 'ORG', 'word': 'Hugging Face', ...}, {'entity_group': 'LOC', 'word': 'Brooklyn', ...}]
```

---

## Section 3: Fine-tuning a masked language model

# Fine-tuning a masked language model[[fine-tuning-a-masked-language-model]]

For many NLP applications, take a pretrained Transformer and fine-tune it directly on your task. But if your corpus is domain-specific (legal contracts, scientific articles), a vanilla BERT will treat domain words as rare tokens — performance suffers. Fine-tuning the language model on in-domain data first is **domain adaptation**. Popularized in 2018 by [ULMFiT](https://arxiv.org/abs/1801.06146) (LSTM-based). Here we do the same with a Transformer.

## Picking a model

Use [DistilBERT](https://huggingface.co/distilbert-base-uncased), a smaller variant trained via [knowledge distillation](https://en.wikipedia.org/wiki/Knowledge_distillation). About 67M params vs. BERT base's 110M — ~2x faster.

```python
from transformers import AutoModelForMaskedLM
model_checkpoint = "distilbert-base-uncased"
model = AutoModelForMaskedLM.from_pretrained(model_checkpoint)
```

Quick fill-mask check:

```python
text = "This is a great [MASK]."
inputs = tokenizer(text, return_tensors="pt")
token_logits = model(**inputs).logits
mask_token_index = torch.where(inputs["input_ids"] == tokenizer.mask_token_id)[1]
mask_token_logits = token_logits[0, mask_token_index, :]
top_5_tokens = torch.topk(mask_token_logits, 5, dim=1).indices[0].tolist()
# >>> This is a great deal. / success. / adventure. / idea. / feat.
```

## Dataset: IMDb

```python
imdb_dataset = load_dataset("imdb")
# DatasetDict: train 25000, test 25000, unsupervised 50000
```

## Preprocessing — concatenate & chunk

For both auto-regressive and masked LM, the common preprocessing step is to concatenate all examples and split into equal-sized chunks. Avoid truncating individual examples (loses info).

```python
def tokenize_function(examples):
    result = tokenizer(examples["text"])
    if tokenizer.is_fast:
        result["word_ids"] = [result.word_ids(i) for i in range(len(result["input_ids"]))]
    return result

tokenized_datasets = imdb_dataset.map(tokenize_function, batched=True, remove_columns=["text", "label"])
```

`tokenizer.model_max_length` is 512 for DistilBERT. For Colab GPUs, use a smaller `chunk_size = 128`:

```python
def group_texts(examples):
    concatenated_examples = {k: sum(examples[k], []) for k in examples.keys()}
    total_length = len(concatenated_examples[list(examples.keys())[0]])
    total_length = (total_length // chunk_size) * chunk_size
    result = {
        k: [t[i : i + chunk_size] for i in range(0, total_length, chunk_size)]
        for k, t in concatenated_examples.items()
    }
    result["labels"] = result["input_ids"].copy()
    return result

lm_datasets = tokenized_datasets.map(group_texts, batched=True)
```

The `labels` column is a copy of `input_ids` — MLM masks tokens on the fly and trains the model to predict the originals.

## Data collator with random masking

```python
from transformers import DataCollatorForLanguageModeling
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm_probability=0.15)
```

15% mask rate matches BERT. Each batch gets a fresh random mask.

### Whole word masking

Mask all subword tokens of a randomly-chosen word together:

```py
import collections, numpy as np
from transformers import default_data_collator
wwm_probability = 0.2

def whole_word_masking_data_collator(features):
    for feature in features:
        word_ids = feature.pop("word_ids")
        mapping = collections.defaultdict(list)
        current_word_index = -1
        current_word = None
        for idx, word_id in enumerate(word_ids):
            if word_id is not None:
                if word_id != current_word:
                    current_word = word_id
                    current_word_index += 1
                mapping[current_word_index].append(idx)
        mask = np.random.binomial(1, wwm_probability, (len(mapping),))
        input_ids = feature["input_ids"]
        labels = feature["labels"]
        new_labels = [-100] * len(labels)
        for word_id in np.where(mask)[0]:
            word_id = word_id.item()
            for idx in mapping[word_id]:
                new_labels[idx] = labels[idx]
                input_ids[idx] = tokenizer.mask_token_id
        feature["labels"] = new_labels
    return default_data_collator(features)
```

## Perplexity

Perplexity = exponential of cross-entropy loss. Lower is better.

```python
import math
eval_results = trainer.evaluate()
print(f">>> Perplexity: {math.exp(eval_results['eval_loss']):.2f}")
# Before fine-tuning: 21.75
# After fine-tuning:  11.32
```

## Accelerate training loop

To make perplexity reproducible across runs, mask the test set **once**:

```python
def insert_random_mask(batch):
    features = [dict(zip(batch, t)) for t in zip(*batch.values())]
    masked_inputs = data_collator(features)
    return {"masked_" + k: v.numpy() for k, v in masked_inputs.items()}

eval_dataset = downsampled_dataset["test"].map(insert_random_mask, batched=True, remove_columns=downsampled_dataset["test"].column_names)
```

Use `default_data_collator` for the eval `DataLoader`. Training loop accumulates losses and computes perplexity per epoch.

Final epoch perplexities: 11.40, 10.90, 10.73.

## Pipeline use

```python
from transformers import pipeline
mask_filler = pipeline("fill-mask", model="huggingface-course/distilbert-base-uncased-finetuned-imdb")
preds = mask_filler("This is a great [MASK]")
# this is a great movie / film / story / movies / character.
```

Domain adaptation works — model now associates "great" with movie-domain terms.

---

## Section 4: Translation

# Translation[[translation]]

A sequence-to-sequence task — one sequence in, another sequence out. Close to summarization. Similar techniques apply to style transfer and generative question answering.

We fine-tune a Marian `Helsinki-NLP/opus-mt-en-fr` model (pretrained on the [Opus](https://opus.nlpl.eu/) corpus, which includes KDE4) on the [KDE4 dataset](https://huggingface.co/datasets/kde4) — localized files for [KDE apps](https://apps.kde.org/). 92 languages available.

## Dataset

```py
from datasets import load_dataset
raw_datasets = load_dataset("kde4", lang1="en", lang2="fr")
# train: 210173 pairs
split_datasets = raw_datasets["train"].train_test_split(train_size=0.9, seed=20)
split_datasets["validation"] = split_datasets.pop("test")
```

KDE4 fully translates tech terms ("threads" → "fils de discussion", "plugin" → "module d'extension"). Pretrained Marian leaves them as English — fine-tuning should fix that.

## Tokenization with text_target

Use `text_target=` to tokenize French labels properly:

```py
inputs = tokenizer(en_sentence, text_target=fr_sentence)
# input_ids → English IDs; labels → French IDs
```

Forgetting `text_target` makes the English tokenizer butcher the French sentence (e.g. `["▁Par","▁dé","f","aut",",",...]` vs proper `["▁Par","▁défaut",...]`).

```python
max_length = 128
def preprocess_function(examples):
    inputs = [ex["en"] for ex in examples["translation"]]
    targets = [ex["fr"] for ex in examples["translation"]]
    model_inputs = tokenizer(inputs, text_target=targets, max_length=max_length, truncation=True)
    return model_inputs
```

T5 models need a prefix like `"translate: English to French:"`. Multilingual tokenizers (mBART, mBART-50, M2M100) need `tokenizer.src_lang` / `tokenizer.tgt_lang` set.

## Model & data collator

```py
from transformers import AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq
model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)
```

`DataCollatorForSeq2Seq` pads labels with `-100` and creates `decoder_input_ids` (labels shifted right with a special start token).

```python out
batch.keys()  # dict_keys(['attention_mask', 'input_ids', 'labels', 'decoder_input_ids'])
batch["decoder_input_ids"][0]
# tensor([59513, 577, 5891, 2, ...])  # 59513 = pad/start token prepended
```

## Metric: SacreBLEU

[BLEU](https://en.wikipedia.org/wiki/BLEU) (Papineni 2002) measures word-overlap with reference translations, with brevity penalty and repetition penalty. Weakness: expects pre-tokenized text. [SacreBLEU](https://github.com/mjpost/sacrebleu) standardizes tokenization for cross-model comparison.

```py
!pip install sacrebleu
import evaluate
metric = evaluate.load("sacrebleu")
predictions = ["This plugin lets you translate web pages between several languages automatically."]
references = [["This plugin allows you to automatically translate web pages between several languages."]]
metric.compute(predictions=predictions, references=references)
# {'score': 46.75, 'counts': [11,6,4,3], 'totals': [12,11,10,9], 'precisions': [...], 'bp': 0.92, ...}
```

References are a **list of lists** (multiple acceptable translations per source).

```python
def compute_metrics(eval_preds):
    preds, labels = eval_preds
    if isinstance(preds, tuple):
        preds = preds[0]
    decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    decoded_preds = [pred.strip() for pred in decoded_preds]
    decoded_labels = [[label.strip()] for label in decoded_labels]
    result = metric.compute(predictions=decoded_preds, references=decoded_labels)
    return {"bleu": result["score"]}
```

## Seq2SeqTrainer

```python
from transformers import Seq2SeqTrainingArguments, Seq2SeqTrainer
args = Seq2SeqTrainingArguments(
    "marian-finetuned-kde4-en-to-fr",
    evaluation_strategy="no",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=32,
    per_device_eval_batch_size=64,
    weight_decay=0.01,
    save_total_limit=3,
    num_train_epochs=3,
    predict_with_generate=True,
    fp16=True,
    push_to_hub=True,
)
trainer = Seq2SeqTrainer(model, args, train_dataset=..., eval_dataset=..., data_collator=data_collator, tokenizer=tokenizer, compute_metrics=compute_metrics)
trainer.evaluate(max_length=max_length)
# Before: eval_bleu 39.27
trainer.train()
trainer.evaluate(max_length=max_length)
# After: eval_bleu 52.94  (14-point improvement)
```

`predict_with_generate=True` is essential — without it the trainer compares argmax(logits) per position to references (teacher-forced), not real autoregressive generation.

```py
trainer.push_to_hub(tags="translation", commit_message="Training complete")
```

## Accelerate training loop

Use `accelerator.unwrap_model(model).generate(...)` for evaluation. Pad predictions and labels across processes:

```py
generated_tokens = accelerator.pad_across_processes(generated_tokens, dim=1, pad_index=tokenizer.pad_token_id)
labels = accelerator.pad_across_processes(labels, dim=1, pad_index=-100)
```

Results: epoch 0 BLEU 53.47, epoch 1 54.24, epoch 2 54.44.

## Pipeline use

```py
translator = pipeline("translation", model="huggingface-course/marian-finetuned-kde4-en-to-fr")
translator("Default to expanded threads")
# [{'translation_text': 'Par défaut, développer les fils de discussion'}]
```

---

## Section 5: Summarization

# Summarization[[summarization]]

Bilingual English+Spanish summarizer using **mT5** on the [Multilingual Amazon Reviews Corpus](https://huggingface.co/datasets/amazon_reviews_multi). Use review titles as target summaries.

## Multilingual corpus

```python
spanish_dataset = load_dataset("amazon_reviews_multi", "es")
english_dataset = load_dataset("amazon_reviews_multi", "en")
# 200k train / 5k val / 5k test per language
```

Filter to book reviews (`product_category in {"book","digital_ebook_purchase"}`), concatenate English+Spanish, filter titles ≤ 2 words (avoid degenerate 1-word labels).

## Models for summarization

| Model | Description | Multilingual |
|---|---|---|
| GPT-2 | Auto-regressive; can summarize by appending "TL;DR" | No |
| PEGASUS | Pretrains by predicting masked sentences in multi-sentence texts | No |
| T5 | Text-to-text universal Transformer (`summarize: ARTICLE`) | No |
| mT5 | Multilingual T5 on mC4 (101 languages) | Yes |
| BART | Encoder-decoder reconstructing corrupted input (BERT+GPT-2 schemes) | No |
| mBART-50 | Multilingual BART (50 languages) | Yes |

mT5 uses no prefix but inherits T5's text-to-text versatility.

## Tokenization

```python
model_checkpoint = "google/mt5-small"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
```

mT5 uses SentencePiece Unigram (Chapter 6) — agnostic to whitespace/accents/punctuation, great for multilingual.

```python
max_input_length = 512
max_target_length = 30
def preprocess_function(examples):
    model_inputs = tokenizer(examples["review_body"], max_length=max_input_length, truncation=True)
    labels = tokenizer(examples["review_title"], max_length=max_target_length, truncation=True)
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs
```

## Metric: ROUGE

[ROUGE](https://en.wikipedia.org/wiki/ROUGE_(metric)) (Recall-Oriented Understudy for Gisting Evaluation). Compute precision/recall/F1 over n-gram overlap with reference summary.

- **Recall** = overlap / |reference|
- **Precision** = overlap / |generated|

Variants:
- `rouge1` — unigram overlap
- `rouge2` — bigram overlap
- `rougeL` — longest common subsequence per sentence
- `rougeLsum` — LCS over whole summary

```py
!pip install rouge_score
import evaluate
rouge_score = evaluate.load("rouge")
scores = rouge_score.compute(predictions=[generated_summary], references=[reference_summary])
# scores["rouge1"].mid  → Score(precision=0.86, recall=1.0, fmeasure=0.92)
```

Returns confidence intervals (`low`/`mid`/`high`).

## Lead-3 baseline

Take the first 3 sentences using `nltk.sent_tokenize`. Baseline ROUGE on validation: rouge1 16.74, rouge2 8.83, rougeL 15.6, rougeLsum 15.96.

```python
from nltk.tokenize import sent_tokenize
def three_sentence_summary(text):
    return "\n".join(sent_tokenize(text)[:3])
```

## Fine-tuning with Seq2SeqTrainer

```python
args = Seq2SeqTrainingArguments(
    output_dir=f"{model_name}-finetuned-amazon-en-es",
    evaluation_strategy="epoch",
    learning_rate=5.6e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    weight_decay=0.01,
    save_total_limit=3,
    num_train_epochs=8,
    predict_with_generate=True,
    logging_steps=logging_steps,
    push_to_hub=True,
)
```

`compute_metrics` decodes preds/labels, runs `sent_tokenize` to split sentences with newlines (ROUGE expects this), then computes `rouge_score.compute(..., use_stemmer=True)`.

After 8 epochs: eval_rouge1 16.97, rouge2 8.30, rougeL 16.84, rougeLsum 16.85. Beats lead-3 baseline.

```py
trainer.push_to_hub(commit_message="Training complete", tags="summarization")
```

## Accelerate version

Same pattern as translation: use `accelerator.unwrap_model(model).generate(...)`, pad across processes, add batches to `rouge_score.add_batch`, compute at end of epoch.

```py
for epoch in range(num_train_epochs):
    # train ...
    # eval ...
    result = rouge_score.compute()
    result = {key: value.mid.fmeasure * 100 for key, value in result.items()}
    print(f"Epoch {epoch}:", result)
```

10-epoch progression: rouge1 from 5.63 → 14.12, rouge2 from 1.16 → 7.01.

## Pipeline use

```python
summarizer = pipeline("summarization", model="huggingface-course/mt5-small-finetuned-amazon-en-es")
# Bilingual: also summarizes Spanish reviews. Performs abstractive summarization.
```

---

## Section 6: Training a causal language model from scratch

# Training a causal language model from scratch[[training-a-causal-language-model-from-scratch]]

Train a new model (not fine-tune). Useful when data is very different from existing pretraining corpora — musical notes, DNA, programming languages. Auto-regressive / causal LMs (GPT-2 family) handle text generation.

We build a scaled-down GPT-2 for **Python data science autocomplete** — completing one-liners using `matplotlib`, `seaborn`, `pandas`, `scikit-learn`.

## Gathering data

Start from `codeparrot` (180GB, ~20M Python files from GitHub). Filter by keyword presence:

```py
def any_keyword_in_string(string, keywords):
    for keyword in keywords:
        if keyword in string:
            return True
    return False

filters = ["pandas", "sklearn", "matplotlib", "seaborn"]
```

Use streaming to avoid downloading the full corpus. ~3% of files match → ~6GB / 600k Python scripts. Or load pre-filtered:

```py
ds_train = load_dataset("huggingface-course/codeparrot-ds-train", split="train")  # 606,720 rows
ds_valid = load_dataset("huggingface-course/codeparrot-ds-valid", split="validation")  # 3,322 rows
```

## Preparing the dataset

```py
context_length = 128
tokenizer = AutoTokenizer.from_pretrained("huggingface-course/code-search-net-tokenizer")

outputs = tokenizer(
    raw_datasets["train"][:2]["content"],
    truncation=True,
    max_length=context_length,
    return_overflowing_tokens=True,
    return_length=True,
)
```

Use `return_overflowing_tokens` to chunk long files into multiple training examples (rather than truncating). Drop chunks shorter than `context_length` (we have plenty of data). `Dataset.map(batched=True)` allows one-to-many mapping (`remove_columns=...` to drop original).

Final: 16.7M training examples × 128 tokens ≈ 2.1B tokens (vs GPT-3 300B, Codex 100B).

## Initialize new GPT-2

```py
from transformers import AutoTokenizer, GPT2LMHeadModel, AutoConfig
config = AutoConfig.from_pretrained(
    "gpt2",
    vocab_size=len(tokenizer),
    n_ctx=context_length,
    bos_token_id=tokenizer.bos_token_id,
    eos_token_id=tokenizer.eos_token_id,
)
model = GPT2LMHeadModel(config)
# 124.2M parameters — same shape as small GPT-2
```

First time **not** using `from_pretrained()` — random init.

## Data collator for CLM

```py
tokenizer.pad_token = tokenizer.eos_token
data_collator = DataCollatorForLanguageModeling(tokenizer, mlm=False)
```

`mlm=False` switches from MLM to causal LM. Labels are the inputs (shifted internally by the model). Collator just copies `input_ids` → `labels`.

## Training with Trainer

```py
args = TrainingArguments(
    output_dir="codeparrot-ds",
    per_device_train_batch_size=32,
    per_device_eval_batch_size=32,
    evaluation_strategy="steps",
    eval_steps=5_000,
    logging_steps=5_000,
    gradient_accumulation_steps=8,
    num_train_epochs=1,
    weight_decay=0.1,
    warmup_steps=1_000,
    lr_scheduler_type="cosine",
    learning_rate=5e-4,
    save_steps=5_000,
    fp16=True,
    push_to_hub=True,
)
```

Effective batch size = 32 * 8 = 256 via gradient accumulation. Cosine LR schedule with warmup.

20h on full set / 2h on subset.

## Code generation example

```py
pipe = pipeline("text-generation", model="huggingface-course/codeparrot-ds", device=device)
txt = """
# create some data
x = np.random.randn(100)
y = np.random.randn(100)

# create scatter plot with x, y
"""
print(pipe(txt, num_return_sequences=1)[0]["generated_text"])
# → plt.scatter(x, y)
```

Model also handles `pd.DataFrame`, `groupby`, `RandomForestRegressor`.

## Training with Accelerate — custom loss

To bias training toward samples that use data science libraries, weight by frequency of keytokens (`plt`, `pd`, `sk`, `fit`, `predict` and their whitespace-prefixed variants):

```py
def keytoken_weighted_loss(inputs, logits, keytoken_ids, alpha=1.0):
    # Shift so that tokens [n:] predict tokens [n+1:]
    shift_labels = inputs[..., 1:].contiguous()
    shift_logits = logits[..., :-1, :].contiguous()
    loss_fct = CrossEntropyLoss(reduction="none")
    loss = loss_fct(shift_logits.view(-1, shift_logits.size(-1)), shift_labels.view(-1))
    loss_per_sample = loss.view(shift_logits.size(0), shift_logits.size(1)).mean(axis=1)
    weights = torch.stack([(inputs == kt).float() for kt in keytoken_ids]).sum((0, 2))
    weights = alpha * (1.0 + weights)
    weighted_loss = (loss_per_sample * weights).mean()
    return weighted_loss
```

Training loop adds gradient clipping (`accelerator.clip_grad_norm_(model.parameters(), 1.0)`), gradient accumulation, and periodic evaluation/save/push.

---

## Section 7: Question answering

# Question answering[[question-answering]]

**Extractive** QA: identify answers as **spans of text** in a context document. Fine-tune BERT on [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) (questions on Wikipedia articles).

> Encoder-only models (BERT) excel at factoid QA but fare poorly on open-ended questions. For *generative* QA, use encoder-decoder models (T5, BART).

## SQuAD dataset

```py
raw_datasets = load_dataset("squad")
# train: 87,599 / validation: 10,570
# features: id, title, context, question, answers
# answers: {"text": [...], "answer_start": [int...]}
```

Training: one answer per question. Validation: multiple acceptable answers per question.

## Tokenization with sliding window

Combined input format: `[CLS] question [SEP] context [SEP]`. Long contexts → split into multiple features via sliding window.

```py
inputs = tokenizer(
    question, context,
    max_length=100,
    truncation="only_second",  # truncate context, not question
    stride=50,
    return_overflowing_tokens=True,
    return_offsets_mapping=True,
)
# inputs["overflow_to_sample_mapping"] maps each chunk to source example
```

Labels:
- `(0, 0)` if answer not in this chunk → model predicts `[CLS]`
- `(start_token, end_token)` otherwise — token indices of answer span

Compute by finding the chunk's context boundary via `sequence_ids()`, then locating answer characters via `offset_mapping`:

```py
max_length = 384
stride = 128

def preprocess_training_examples(examples):
    questions = [q.strip() for q in examples["question"]]
    inputs = tokenizer(
        questions, examples["context"],
        max_length=max_length, truncation="only_second",
        stride=stride,
        return_overflowing_tokens=True,
        return_offsets_mapping=True,
        padding="max_length",
    )
    offset_mapping = inputs.pop("offset_mapping")
    sample_map = inputs.pop("overflow_to_sample_mapping")
    answers = examples["answers"]
    start_positions, end_positions = [], []
    for i, offset in enumerate(offset_mapping):
        sample_idx = sample_map[i]
        answer = answers[sample_idx]
        start_char = answer["answer_start"][0]
        end_char = start_char + len(answer["text"][0])
        sequence_ids = inputs.sequence_ids(i)
        # find context boundary
        idx = 0
        while sequence_ids[idx] != 1: idx += 1
        context_start = idx
        while sequence_ids[idx] == 1: idx += 1
        context_end = idx - 1
        if offset[context_start][0] > start_char or offset[context_end][1] < end_char:
            start_positions.append(0); end_positions.append(0)
        else:
            idx = context_start
            while idx <= context_end and offset[idx][0] <= start_char: idx += 1
            start_positions.append(idx - 1)
            idx = context_end
            while idx >= context_start and offset[idx][1] >= end_char: idx -= 1
            end_positions.append(idx + 1)
    inputs["start_positions"] = start_positions
    inputs["end_positions"] = end_positions
    return inputs
```

87,599 examples → 88,729 training features (~1000 features added by sliding window).

## Validation processing

Keep `offset_mapping` and `example_id`, mask question offsets to `None`:

```py
def preprocess_validation_examples(examples):
    # ... same tokenization ...
    sample_map = inputs.pop("overflow_to_sample_mapping")
    example_ids = []
    for i in range(len(inputs["input_ids"])):
        sample_idx = sample_map[i]
        example_ids.append(examples["id"][sample_idx])
        sequence_ids = inputs.sequence_ids(i)
        offset = inputs["offset_mapping"][i]
        inputs["offset_mapping"][i] = [
            o if sequence_ids[k] == 1 else None for k, o in enumerate(offset)
        ]
    inputs["example_id"] = example_ids
    return inputs
```

## Post-processing — span extraction

Model outputs `start_logits` / `end_logits` per token. For each example:
1. Find all features belonging to the example
2. Take top `n_best=20` start indices and top `n_best=20` end indices per feature
3. For each (start, end) pair, skip if outside context, end<start, or length > `max_answer_length=30`
4. Score = `start_logit + end_logit` (sum, since softmax is monotonic; sum equivalent to log(probs · probs))
5. Pick best across all features of the example

```py
n_best = 20
max_answer_length = 30

def compute_metrics(start_logits, end_logits, features, examples):
    example_to_features = collections.defaultdict(list)
    for idx, feature in enumerate(features):
        example_to_features[feature["example_id"]].append(idx)
    predicted_answers = []
    for example in tqdm(examples):
        example_id = example["id"]
        context = example["context"]
        answers = []
        for feature_index in example_to_features[example_id]:
            start_logit = start_logits[feature_index]
            end_logit = end_logits[feature_index]
            offsets = features[feature_index]["offset_mapping"]
            start_indexes = np.argsort(start_logit)[-1 : -n_best - 1 : -1].tolist()
            end_indexes = np.argsort(end_logit)[-1 : -n_best - 1 : -1].tolist()
            for start_index in start_indexes:
                for end_index in end_indexes:
                    if offsets[start_index] is None or offsets[end_index] is None: continue
                    if end_index < start_index or end_index - start_index + 1 > max_answer_length: continue
                    answers.append({
                        "text": context[offsets[start_index][0] : offsets[end_index][1]],
                        "logit_score": start_logit[start_index] + end_logit[end_index],
                    })
        if len(answers) > 0:
            best_answer = max(answers, key=lambda x: x["logit_score"])
            predicted_answers.append({"id": example_id, "prediction_text": best_answer["text"]})
        else:
            predicted_answers.append({"id": example_id, "prediction_text": ""})
    theoretical_answers = [{"id": ex["id"], "answers": ex["answers"]} for ex in examples]
    return metric.compute(predictions=predicted_answers, references=theoretical_answers)
```

## Metric: SQuAD (exact match + F1)

```py
metric = evaluate.load("squad")
# {'exact_match': 83.0, 'f1': 88.25} on small eval set
```

## Training

```py
model = AutoModelForQuestionAnswering.from_pretrained(model_checkpoint)
args = TrainingArguments(
    "bert-finetuned-squad",
    evaluation_strategy="no",
    save_strategy="epoch",
    learning_rate=2e-5,
    num_train_epochs=3,
    weight_decay=0.01,
    fp16=True,
    push_to_hub=True,
)
trainer = Trainer(model=model, args=args, train_dataset=train_dataset, eval_dataset=validation_dataset, tokenizer=tokenizer)
trainer.train()
predictions, _, _ = trainer.predict(validation_dataset)
start_logits, end_logits = predictions
compute_metrics(start_logits, end_logits, validation_dataset, raw_datasets["validation"])
# {'exact_match': 81.18, 'f1': 88.67}  (vs BERT paper: 80.8 / 88.5)
```

## Accelerate training loop

Manual loop with regular evaluation. Gather start/end logits across processes, concatenate, truncate to `len(validation_dataset)`, run `compute_metrics`.

```py
for epoch in range(num_train_epochs):
    # training ...
    model.eval()
    start_logits, end_logits = [], []
    for batch in tqdm(eval_dataloader):
        with torch.no_grad():
            outputs = model(**batch)
        start_logits.append(accelerator.gather(outputs.start_logits).cpu().numpy())
        end_logits.append(accelerator.gather(outputs.end_logits).cpu().numpy())
    start_logits = np.concatenate(start_logits)[: len(validation_dataset)]
    end_logits = np.concatenate(end_logits)[: len(validation_dataset)]
    metrics = compute_metrics(start_logits, end_logits, validation_dataset, raw_datasets["validation"])
    print(f"epoch {epoch}:", metrics)
```

## Pipeline use

```py
question_answerer = pipeline("question-answering", model="huggingface-course/bert-finetuned-squad")
question_answerer(question="Which deep learning libraries back Transformers?", context="...")
# {'score': 0.998, 'start': 78, 'end': 105, 'answer': 'Jax, PyTorch and TensorFlow'}
```

---

## Section 8: Mastering LLMs

# Mastering LLMs[[mastering-llms]]

You now have the knowledge and tools to tackle almost any language task with Transformers and the Hugging Face ecosystem.

## From NLP to LLMs

While traditional NLP tasks remain core building blocks, LLMs have revolutionized the field:

- Handle multiple tasks without task-specific fine-tuning
- Excel at instruction following and context adaptation
- Generate coherent, contextually appropriate text
- Perform reasoning and complex problem solving (chain-of-thought)

Foundational NLP skills — tokenization, model architectures, fine-tuning approaches, evaluation metrics — remain essential for working with LLMs effectively.

## After this chapter you should:

* Know which architectures (encoder / decoder / encoder-decoder) suit each task
* Understand pretraining vs fine-tuning
* Train Transformer models using `Trainer` + Accelerate or TensorFlow/Keras
* Understand the meaning and limitations of ROUGE and BLEU for text generation
* Use fine-tuned models on the Hub or with `pipeline`
* Appreciate how LLMs build on traditional NLP

Next chapter: debugging Transformer models and asking for help effectively.
