# HuggingFace LLM Course — Chapter 3: Fine-tuning a pretrained model
Source: https://huggingface.co/learn/llm-course/chapter3/
Sections: 1,2,3,4,5,6
---

## Section 1: Introduction

# Introduction[[introduction]]

In [Chapter 2](/course/chapter2) we explored how to use tokenizers and pretrained models to make predictions. But what if you want to fine-tune a pretrained model to solve a specific task? That's the topic of this chapter! You will learn:

* How to prepare a large dataset from the Hub using the latest 🤗 Datasets features
* How to use the high-level `Trainer` API to fine-tune a model with modern best practices
* How to implement a custom training loop with optimization techniques
* How to leverage the 🤗 Accelerate library to easily run distributed training on any setup
* How to apply current fine-tuning best practices for maximum performance

> [!TIP]
> 📚 **Essential Resources**: Before starting, you might want to review the [🤗 Datasets documentation](https://huggingface.co/docs/datasets/) for data processing.

This chapter will also serve as an introduction to some Hugging Face libraries beyond the 🤗 Transformers library! We'll see how libraries like 🤗 Datasets, 🤗 Tokenizers, 🤗 Accelerate, and 🤗 Evaluate can help you train models more efficiently and effectively.

Each of the main sections in this chapter will teach you something different:
- **Section 2**: Learn modern data preprocessing techniques and efficient dataset handling
- **Section 3**: Master the powerful Trainer API with all its latest features
- **Section 4**: Implement training loops from scratch and understand distributed training with Accelerate

By the end of this chapter, you'll be able to fine-tune models on your own datasets using both high-level APIs and custom training loops, applying the latest best practices in the field.

> [!TIP]
> 🎯 **What You'll Build**: By the end of this chapter, you'll have fine-tuned a BERT model for text classification and understand how to adapt the techniques to your own datasets and tasks.

This chapter focuses exclusively on **PyTorch**, as it has become the standard framework for modern deep learning research and production. We'll use the latest APIs and best practices from the Hugging Face ecosystem.

To upload your trained models to the Hugging Face Hub, you will need a Hugging Face account: [create an account](https://huggingface.co/join)

---

## Section 2: Processing the data

# Processing the data[[processing-the-data]]

Continuing with the example from the [previous chapter](/course/chapter2), here is how we would train a sequence classifier on one batch:

```python
import torch
from torch.optim import AdamW
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Same as before
checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
sequences = [
    "I've been waiting for a HuggingFace course my whole life.",
    "This course is amazing!",
]
batch = tokenizer(sequences, padding=True, truncation=True, return_tensors="pt")

# This is new
batch["labels"] = torch.tensor([1, 1])

optimizer = AdamW(model.parameters())
loss = model(**batch).loss
loss.backward()
optimizer.step()
```

Of course, just training the model on two sentences is not going to yield very good results. To get better results, you will need to prepare a bigger dataset.

In this section we will use as an example the MRPC (Microsoft Research Paraphrase Corpus) dataset, introduced in a [paper](https://www.aclweb.org/anthology/I05-5002.pdf) by William B. Dolan and Chris Brockett. The dataset consists of 5,801 pairs of sentences, with a label indicating if they are paraphrases or not (i.e., if both sentences mean the same thing). We've selected it for this chapter because it's a small dataset, so it's easy to experiment with training on it.

### Loading a dataset from the Hub[[loading-a-dataset-from-the-hub]]

The Hub doesn't just contain models; it also has multiple datasets in lots of different languages. You can browse the datasets [here](https://huggingface.co/datasets), and we recommend you try to load and process a new dataset once you have gone through this section (see the general documentation [here](https://huggingface.co/docs/datasets/loading)). But for now, let's focus on the MRPC dataset! This is one of the 10 datasets composing the [GLUE benchmark](https://gluebenchmark.com/), which is an academic benchmark that is used to measure the performance of ML models across 10 different text classification tasks.

The 🤗 Datasets library provides a very simple command to download and cache a dataset on the Hub. We can download the MRPC dataset like this:

```py
from datasets import load_dataset

raw_datasets = load_dataset("glue", "mrpc")
raw_datasets
```

```python out
DatasetDict({
    train: Dataset({
        features: ['sentence1', 'sentence2', 'label', 'idx'],
        num_rows: 3668
    })
    validation: Dataset({
        features: ['sentence1', 'sentence2', 'label', 'idx'],
        num_rows: 408
    })
    test: Dataset({
        features: ['sentence1', 'sentence2', 'label', 'idx'],
        num_rows: 1725
    })
})
```

We get a `DatasetDict` object containing train/validation/test splits. We can access pairs by indexing:

```py
raw_train_dataset = raw_datasets["train"]
raw_train_dataset[0]
```

```python out
{'idx': 0,
 'label': 1,
 'sentence1': 'Amrozi accused his brother , whom he called " the witness " , of deliberately distorting his evidence .',
 'sentence2': 'Referring to him as only " the witness " , Amrozi accused his brother of deliberately distorting his evidence .'}
```

Labels are integers. To know which integer corresponds to which label:

```py
raw_train_dataset.features
```

```python out
{'sentence1': Value(dtype='string', id=None),
 'sentence2': Value(dtype='string', id=None),
 'label': ClassLabel(num_classes=2, names=['not_equivalent', 'equivalent'], names_file=None, id=None),
 'idx': Value(dtype='int32', id=None)}
```

`label` is of type `ClassLabel`: `0` corresponds to `not_equivalent`, `1` to `equivalent`.

### Preprocessing a dataset[[preprocessing-a-dataset]]

```py
from transformers import AutoTokenizer

checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
tokenized_sentences_1 = tokenizer(raw_datasets["train"]["sentence1"])
tokenized_sentences_2 = tokenizer(raw_datasets["train"]["sentence2"])
```

The tokenizer can also take a pair of sequences:

```py
inputs = tokenizer("This is the first sentence.", "This is the second one.")
inputs
```

```python out
{
  'input_ids': [101, 2023, 2003, 1996, 2034, 6251, 1012, 102, 2023, 2003, 1996, 2117, 2028, 1012, 102],
  'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
  'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}
```

`token_type_ids` tells the model which part of the input is the first sentence and which is the second.

Decoding the IDs:

```py
tokenizer.convert_ids_to_tokens(inputs["input_ids"])
```

```python out
['[CLS]', 'this', 'is', 'the', 'first', 'sentence', '.', '[SEP]', 'this', 'is', 'the', 'second', 'one', '.', '[SEP]']
```

BERT expects: `[CLS] sentence1 [SEP] sentence2 [SEP]`. Models like DistilBERT don't return `token_type_ids` because they weren't pretrained with them.

BERT is pretrained with token type IDs because of its additional **next sentence prediction** objective (in addition to **masked language modeling**). The model is given pairs of sentences and asked to predict whether the second follows the first.

To tokenize the whole dataset, use `Dataset.map()`:

```py
def tokenize_function(example):
    return tokenizer(example["sentence1"], example["sentence2"], truncation=True)
```

Padding is left out — better to pad per-batch (dynamic padding).

```py
tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
tokenized_datasets
```

```python out
DatasetDict({
    train: Dataset({
        features: ['attention_mask', 'idx', 'input_ids', 'label', 'sentence1', 'sentence2', 'token_type_ids'],
        num_rows: 3668
    })
    validation: Dataset({
        features: ['attention_mask', 'idx', 'input_ids', 'label', 'sentence1', 'sentence2', 'token_type_ids'],
        num_rows: 408
    })
    test: Dataset({
        features: ['attention_mask', 'idx', 'input_ids', 'label', 'sentence1', 'sentence2', 'token_type_ids'],
        num_rows: 1725
    })
})
```

You can use `num_proc` for multiprocessing. Fast tokenizers (Rust-backed via 🤗 Tokenizers) already use multiple threads with `batched=True`.

##### Dynamic padding[[dynamic-padding]]

The function that puts samples together inside a batch is the *collate function* — passed as `collate_fn` to a `DataLoader`. We use `DataCollatorWithPadding`:

```py
from transformers import DataCollatorWithPadding

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
```

Test:

```py
samples = tokenized_datasets["train"][:8]
samples = {k: v for k, v in samples.items() if k not in ["idx", "sentence1", "sentence2"]}
[len(x) for x in samples["input_ids"]]
```

```python out
[50, 59, 47, 67, 59, 50, 62, 32]
```

Dynamic padding pads to the max length within each batch (67 here), not the entire dataset.

```py
batch = data_collator(samples)
{k: v.shape for k, v in batch.items()}
```

```python out
{'attention_mask': torch.Size([8, 67]),
 'input_ids': torch.Size([8, 67]),
 'token_type_ids': torch.Size([8, 67]),
 'labels': torch.Size([8])}
```

Note: TPUs prefer fixed shapes; dynamic padding can cause problems there.

---

## Section 3: Fine-tuning a model with the Trainer API

# Fine-tuning a model with the Trainer API[[fine-tuning-a-model-with-the-trainer-api]]

🤗 Transformers provides a `Trainer` class to help you fine-tune any of the pretrained models on your dataset.

Recap of preprocessing:

```py
from datasets import load_dataset
from transformers import AutoTokenizer, DataCollatorWithPadding

raw_datasets = load_dataset("glue", "mrpc")
checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

def tokenize_function(example):
    return tokenizer(example["sentence1"], example["sentence2"], truncation=True)

tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
```

### Training[[training]]

Define a `TrainingArguments` class with all hyperparameters. Only required argument: output directory.

```py
from transformers import TrainingArguments

training_args = TrainingArguments("test-trainer")
```

Pass `push_to_hub=True` to upload to the Hub during training.

Define the model:

```py
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)
```

You'll get a warning: BERT's pretraining head is discarded and a new classification head with randomly initialized weights is added.

Define the `Trainer`:

```py
from transformers import Trainer

trainer = Trainer(
    model,
    training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    processing_class=tokenizer,
)
```

`processing_class` (newer parameter) tells the Trainer which tokenizer to use. When a tokenizer is passed, the default `data_collator` becomes `DataCollatorWithPadding`.

Train:

```py
trainer.train()
```

Reports training loss every 500 steps but won't tell you performance because:
1. `eval_strategy` not set to `"steps"` or `"epoch"`.
2. No `compute_metrics()` function provided.

### Evaluation[[evaluation]]

```py
predictions = trainer.predict(tokenized_datasets["validation"])
print(predictions.predictions.shape, predictions.label_ids.shape)
```

```python out
(408, 2) (408,)
```

`predict()` returns a named tuple: `predictions`, `label_ids`, `metrics`. `predictions` are logits.

```py
import numpy as np

preds = np.argmax(predictions.predictions, axis=-1)
```

Use the 🤗 Evaluate library:

```py
import evaluate

metric = evaluate.load("glue", "mrpc")
metric.compute(predictions=preds, references=predictions.label_ids)
```

```python out
{'accuracy': 0.8578431372549019, 'f1': 0.8996539792387542}
```

85.78% accuracy and 89.97 F1 — close to the BERT paper's reported 88.9 F1.

Final `compute_metrics()`:

```py
def compute_metrics(eval_preds):
    metric = evaluate.load("glue", "mrpc")
    logits, labels = eval_preds
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)
```

New Trainer with epoch-based evaluation:

```py
training_args = TrainingArguments("test-trainer", eval_strategy="epoch")
model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)

trainer = Trainer(
    model,
    training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    processing_class=tokenizer,
    compute_metrics=compute_metrics,
)
```

```py
trainer.train()
```

### Advanced Training Features[[advanced-training-features]]

**Mixed Precision Training** — `fp16=True`:

```py
training_args = TrainingArguments(
    "test-trainer",
    eval_strategy="epoch",
    fp16=True,  # Enable mixed precision
)
```

**Gradient Accumulation**:

```py
training_args = TrainingArguments(
    "test-trainer",
    eval_strategy="epoch",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,  # Effective batch size = 4 * 4 = 16
)
```

**Learning Rate Scheduling**:

```py
training_args = TrainingArguments(
    "test-trainer",
    eval_strategy="epoch",
    learning_rate=2e-5,
    lr_scheduler_type="cosine",
)
```

The `Trainer` works out of the box on multiple GPUs or TPUs.

---

## Section 4: A full training loop

# A full training loop[[a-full-training]]

Implementing the same fine-tuning without `Trainer` — a custom PyTorch loop.

```py
from datasets import load_dataset
from transformers import AutoTokenizer, DataCollatorWithPadding

raw_datasets = load_dataset("glue", "mrpc")
checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

def tokenize_function(example):
    return tokenizer(example["sentence1"], example["sentence2"], truncation=True)

tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
```

### Prepare for training[[prepare-for-training]]

Postprocessing before building DataLoaders:
- Remove unused columns (`sentence1`, `sentence2`, `idx`)
- Rename `label` to `labels`
- Set format to PyTorch tensors

```py
tokenized_datasets = tokenized_datasets.remove_columns(["sentence1", "sentence2", "idx"])
tokenized_datasets = tokenized_datasets.rename_column("label", "labels")
tokenized_datasets.set_format("torch")
tokenized_datasets["train"].column_names
```

```python
["attention_mask", "input_ids", "labels", "token_type_ids"]
```

DataLoaders:

```py
from torch.utils.data import DataLoader

train_dataloader = DataLoader(
    tokenized_datasets["train"], shuffle=True, batch_size=8, collate_fn=data_collator
)
eval_dataloader = DataLoader(
    tokenized_datasets["validation"], batch_size=8, collate_fn=data_collator
)
```

Inspect a batch:

```py
for batch in train_dataloader:
    break
{k: v.shape for k, v in batch.items()}
```

```python out
{'attention_mask': torch.Size([8, 65]),
 'input_ids': torch.Size([8, 65]),
 'labels': torch.Size([8]),
 'token_type_ids': torch.Size([8, 65])}
```

Model:

```py
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)
```

Sanity check:

```py
outputs = model(**batch)
print(outputs.loss, outputs.logits.shape)
```

```python out
tensor(0.5441, grad_fn=) torch.Size([8, 2])
```

All 🤗 Transformers models return the loss when `labels` are provided.

Optimizer — `AdamW` (Adam with proper decoupled weight decay regularization, from Loshchilov & Hutter 2017):

```py
from torch.optim import AdamW

optimizer = AdamW(model.parameters(), lr=5e-5)
```

Learning rate scheduler — linear decay from 5e-5 to 0 over 3 epochs (Trainer default):

```py
from transformers import get_scheduler

num_epochs = 3
num_training_steps = num_epochs * len(train_dataloader)
lr_scheduler = get_scheduler(
    "linear",
    optimizer=optimizer,
    num_warmup_steps=0,
    num_training_steps=num_training_steps,
)
print(num_training_steps)
```

```python out
1377
```

### The training loop[[the-training-loop]]

Device:

```py
import torch

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
model.to(device)
device
```

```python out
device(type='cuda')
```

Loop:

```py
from tqdm.auto import tqdm

progress_bar = tqdm(range(num_training_steps))

model.train()
for epoch in range(num_epochs):
    for batch in train_dataloader:
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()

        optimizer.step()
        lr_scheduler.step()
        optimizer.zero_grad()
        progress_bar.update(1)
```

Modern training optimizations to consider:
- **Gradient Clipping**: `torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)` before `optimizer.step()`
- **Mixed Precision**: `torch.cuda.amp.autocast()` and `GradScaler`
- **Gradient Accumulation**
- **Checkpointing**

### The evaluation loop[[the-evaluation-loop]]

Metrics can accumulate batches via `add_batch()`, then `compute()`:

```py
import evaluate

metric = evaluate.load("glue", "mrpc")
model.eval()
for batch in eval_dataloader:
    batch = {k: v.to(device) for k, v in batch.items()}
    with torch.no_grad():
        outputs = model(**batch)

    logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1)
    metric.add_batch(predictions=predictions, references=batch["labels"])

metric.compute()
```

```python out
{'accuracy': 0.8431372549019608, 'f1': 0.8907849829351535}
```

### Supercharge your training loop with 🤗 Accelerate[[supercharge-your-training-loop-with-accelerate]]

🤗 Accelerate handles distributed training, mixed precision, and device placement automatically. Minimal changes:

```py
from accelerate import Accelerator
from torch.optim import AdamW
from transformers import AutoModelForSequenceClassification, get_scheduler

accelerator = Accelerator()

model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)
optimizer = AdamW(model.parameters(), lr=3e-5)

train_dl, eval_dl, model, optimizer = accelerator.prepare(
    train_dataloader, eval_dataloader, model, optimizer
)

num_epochs = 3
num_training_steps = num_epochs * len(train_dl)
lr_scheduler = get_scheduler(
    "linear",
    optimizer=optimizer,
    num_warmup_steps=0,
    num_training_steps=num_training_steps,
)

progress_bar = tqdm(range(num_training_steps))

model.train()
for epoch in range(num_epochs):
    for batch in train_dl:
        outputs = model(**batch)
        loss = outputs.loss
        accelerator.backward(loss)

        optimizer.step()
        lr_scheduler.step()
        optimizer.zero_grad()
        progress_bar.update(1)
```

Key changes:
1. Import `Accelerator` and instantiate one.
2. Send dataloaders, model, optimizer through `accelerator.prepare()`.
3. Remove `.to(device)` calls.
4. Replace `loss.backward()` with `accelerator.backward(loss)`.

For Cloud TPUs, pad samples to a fixed length via `padding="max_length"` and `max_length`.

Run with:

```bash
accelerate config
accelerate launch train.py
```

In notebooks:

```python
from accelerate import notebook_launcher

notebook_launcher(training_function)
```

### Next Steps and Best Practices[[next-steps-and-best-practices]]

- **Model Evaluation**: Use multiple metrics via 🤗 Evaluate.
- **Hyperparameter Tuning**: Optuna or Ray Tune.
- **Model Monitoring**: Track curves and validation performance.
- **Model Sharing**: Push to the Hugging Face Hub.
- **Efficiency**: Gradient checkpointing, LoRA / AdaLoRA, quantization.

---

## Section 5: Understanding Learning Curves

# Understanding Learning Curves[[understanding-learning-curves]]

## What are Learning Curves?[[what-are-learning-curves]]

Learning curves are visual representations of your model's performance metrics over time during training. Two key curves:

- **Loss curves**: Show error over training steps/epochs
- **Accuracy curves**: Show percentage of correct predictions over training steps/epochs

Metrics are computed per batch and logged to disk. Tools like [Weights & Biases](https://wandb.ai/) visualize them.

### Loss Curves[[loss-curves]]

- **High initial loss**: Model starts without optimization
- **Decreasing loss**: As training progresses
- **Convergence**: Loss stabilizes at low value

Example using W&B:

```python
from transformers import Trainer, TrainingArguments
import wandb

wandb.init(project="transformer-fine-tuning", name="bert-mrpc-analysis")

training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="steps",
    eval_steps=50,
    save_steps=100,
    logging_steps=10,
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    report_to="wandb",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    processing_class=tokenizer,
    compute_metrics=compute_metrics,
)

trainer.train()
```

### Accuracy Curves[[accuracy-curves]]

- **Start low**, **increase with training**, **may show plateaus**.

Accuracy curves are "steppy" because accuracy is discrete: small confidence improvements don't change the final prediction until a threshold is crossed.

### Convergence[[convergence]]

When loss/accuracy stabilize and level off — model has learned the patterns.

## Interpreting Learning Curve Patterns[[interpreting-learning-curve-patterns]]

### Healthy Learning Curves[[healthy-learning-curves]]

Characteristics:
- **Smooth decline in loss** (training & validation)
- **Close training/validation performance** — small gap
- **Convergence**

Accuracy plateaus example: binary cat/dog classifier predicts 0.3 for dog (truth=1) → rounded to 0, wrong. Next step 0.4 → still wrong, loss decreased but accuracy unchanged. Accuracy only jumps when prediction crosses 0.5.

### Practical Examples[[practical-examples]]

#### During Training[[during-training]]

Monitor:
1. **Loss convergence**: still decreasing or plateaued?
2. **Overfitting signs**: validation loss increasing while training loss decreases
3. **Learning rate**: erratic (too high) or flat (too low)?
4. **Stability**: sudden spikes/drops

#### After Training[[after-training]]

Analyze:
1. **Final performance**
2. **Efficiency**: could fewer epochs work?
3. **Generalization**: gap between train/val
4. **Trends**: would more training help?

#### Overfitting[[overfitting]]

**Symptoms:**
- Training loss decreases while validation loss increases or plateaus
- Large gap between training and validation accuracy
- Training accuracy much higher than validation

**Solutions:**
- **Regularization**: dropout, weight decay
- **Early stopping**
- **Data augmentation**
- **Reduce model complexity**

Early stopping example:

```python
from transformers import EarlyStoppingCallback

training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="steps",
    eval_steps=100,
    save_strategy="steps",
    save_steps=100,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
    num_train_epochs=10,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    processing_class=tokenizer,
    compute_metrics=compute_metrics,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=3)],
)
```

#### 2. Underfitting[[underfitting]]

Causes: model too small, LR too low, dataset too small, poor regularization.

**Symptoms:**
- Both training and validation loss remain high
- Performance plateaus early
- Training accuracy lower than expected

**Solutions:**
- Increase model capacity
- Train longer
- Adjust learning rate
- Check data quality

```python
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./results",
    -num_train_epochs=5,
    +num_train_epochs=10,
)
```

#### 3. Erratic Learning Curves[[erratic-learning-curves]]

Causes: LR too high, batch size too small, poor regularization, noisy data.

**Symptoms:**
- Frequent fluctuations in loss/accuracy
- High variance, oscillation

**Solutions:**
- Lower learning rate
- Increase batch size
- Gradient clipping
- Better data preprocessing

```python
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./results",
    -learning_rate=1e-5,
    +learning_rate=1e-4,
    -per_device_train_batch_size=16,
    +per_device_train_batch_size=32,
)
```

## Key Takeaways[[key-takeaways]]

- Learning curves are essential for understanding training progress
- Monitor both loss and accuracy (different characteristics)
- Overfitting: diverging train/val performance
- Underfitting: poor performance on both
- W&B makes tracking easy
- Early stopping + regularization handle most issues

---

## Section 6: Fine-tuning, Check!

# Fine-tuning, Check![[fine-tuning-check]]

Recap — in this chapter you:

* Learned about datasets on the [Hub](https://huggingface.co/datasets) and modern data processing techniques
* Learned to load and preprocess datasets efficiently, including dynamic padding and data collators
* Implemented fine-tuning and evaluation using the high-level `Trainer` API
* Implemented a complete custom training loop from scratch with PyTorch
* Used 🤗 Accelerate for multi-GPU/TPU training
* Applied modern optimization techniques like mixed precision training and gradient accumulation

Pro tips:
- Start with a strong baseline using the `Trainer` API before custom loops
- Use the 🤗 Hub to find pretrained models close to your task
- Monitor with proper evaluation metrics; save checkpoints
- Share your work with the community
