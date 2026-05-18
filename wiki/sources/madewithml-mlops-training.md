---
title: "Made With ML — Distributed Training"
type: source
tags: [mlops, made-with-ml, training, ray-train, llm-finetuning]
date: 2026-05-15
source_file: raw/madewithml/mlops-training.md
---

## Summary
The training lesson fine-tunes a pretrained [[SciBERT]] LLM ([[bert]] encoder, `allenai/scibert_scivocab_uncased`) on the content-tagging task using [[RayTrain]] for multi-worker distributed training. It first benchmarks generative LLMs ([[GPT35]], [[GPT4]]) zero-shot and few-shot via the OpenAI API, then builds a `FinetunedLLM` (BertModel + dropout + linear head) with a `CustomPreprocessor`, a custom `collate_fn` for padding, a `TorchTrainer` with `train_loop_per_worker`, observability via Ray Dashboard + TensorBoard, and an inference loop using `TorchPredictor.from_checkpoint`. GPT-4 few-shot achieves F1 ~0.93; the fine-tuned scibert ends in the same range at a fraction of the size.

## Key Claims
- Modeling iteration ladder: chance → rules → simple features (TF-IDF) → embeddings (CNN/RNN/Transformer) → weigh tradeoffs → revisit baselines as data grows.
- For unstructured text data the course skips rule-based baselines and goes directly to fine-tuning a pretrained LLM (BERT-class).
- Generative-LLM benchmark on the holdout: zero-shot GPT-3.5 F1=0.78, zero-shot GPT-4 F1=0.93, few-shot GPT-3.5 F1=0.84, few-shot GPT-4 F1=0.93.
- Reasons to care about open-source LLMs: data ownership, ability to fine-tune actual weights, and freedom to optimize inference (quantization, pruning).
- [[RayTrain]] is chosen over PyTorch DDP or Horovod because it scales across machines with minimal code changes versus the single-machine training script.
- The architecture combines a frozen-ish pretrained BertModel returning a 768-dim pooled vector, a Dropout(p=0.5), and a `Linear(768, num_classes=4)` classification head.
- A `CustomPreprocessor` subclass of Ray's `Preprocessor` learns `class_to_index` in `_fit` and applies the previous lesson's `preprocess()` in `_transform_pandas`.
- Output predictions can hallucinate tags outside the approved label set; a `clean_predictions` post-processor defaults unknown outputs to `"other"`.

## Key Quotes
> "With distributed training, there will be a head node that's responsible for orchestrating the training process. While the worker nodes that will be responsible for training the model and communicating results back to the head node. From a user's perspective, Ray abstracts away all of this complexity."

> "Our best model is GPT 4 with few shot learning at an f1 score of ~93%. We will see, in the rest of the course, how fine-tuning an LLM with a proper training dataset to change the actual weights of the last N layers (as opposed to the hard prompt tuning here) will yield similar/slightly better results to GPT 4 (at a fraction of the model size and inference costs)."

## Connections
- [[MadeWithML]] — parent course.
- [[GokuMohandas]] — author.
- [[Anyscale]] — publisher.
- [[Ray]] — distributed runtime.
- [[RayTrain]] — distributed training framework used.
- [[PyTorch]] — model layer and training-loop framework.
- [[HuggingFaceTransformers]] — provides `BertModel`, `BertTokenizer`.
- [[SciBERT]] — pretrained model fine-tuned on the task.
- [[bert]] — base architecture family.
- [[transformer]] — underlying neural architecture.
- [[LLMFineTuning]] — the lesson's core technique.
- [[ZeroShotLearning]] — benchmarked with GPT-3.5/GPT-4.
- [[FewShotLearning]] — benchmarked with in-context examples.
- [[openai]] — provider of the benchmarked closed models.
- [[GPT4]] — strongest benchmarked LLM (F1=0.93).
- [[GPT35]] — secondary benchmarked LLM.
- [[Llama2]] — open-source alternative referenced.
- [[Falcon40B]] — open-source alternative referenced.
- [[meta]] — Llama 2 publisher.
- [[DistributedTraining]] — broader paradigm.
- [[PyTorchDDP]] — alternative framework mentioned.
- [[Horovod]] — alternative framework mentioned.
- [[CrossEntropyLoss]] — implicit loss for multiclass classification.
- [[DropoutRegularization]] — `Dropout(p=0.5)` in the model head.
- [[AttentionMask]] — used during tokenization and forward pass.
- [[Hallucination]] — addressed via `clean_predictions` default-to-other.
- [[Reproducibility]] — `set_seeds` covers numpy/random/torch/cuda + PYTHONHASHSEED.
- [[F1Score]] — primary evaluation metric.

## Contradictions
- None identified.
