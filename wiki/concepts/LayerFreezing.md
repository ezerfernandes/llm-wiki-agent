---
title: "Layer Freezing"
type: concept
tags: [fine-tuning, training, parameter-efficient, transfer-learning]
sources: [hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Layer Freezing

**Layer freezing** is the practice of marking specific parameters of a pretrained model as **non-trainable** during fine-tuning by setting `param.requires_grad = False`. Trades quality for compute / time. The canonical alternative to [[PEFT]] / [[lora|LoRA]] for reducing fine-tuning cost.

Per [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]:

> *"We could choose to only freeze certain layers to speed up computing but still allow the main model to learn from the classification task. Generally, we want frozen layers to be followed by trainable layers."*

## The idiom (Hugging Face Transformers)

```python
for name, param in model.named_parameters():
    if name.startswith("classifier"):
        param.requires_grad = True   # trainable head
    else:
        param.requires_grad = False  # frozen backbone
```

Or by parameter index:

```python
# Freeze first 165 parameters; train block 11 + classifier
for index, (name, param) in enumerate(model.named_parameters()):
    if index < 165:
        param.requires_grad = False
```

## Ch 11's empirical ladder (Rotten Tomatoes, 1 epoch, `bert-base-cased`)

| Regime | F1 | Trade-off |
|---|---|---|
| Train all (no freezing) | **0.85** | Slowest, best |
| Freeze blocks 0–9, train block 11 + head | **0.80** | Much faster, ≈95% of full-FT quality |
| Freeze backbone + embeddings, train only head | **0.63** | Fastest, but big quality drop |

The figure 11-7 result: *"Training only the first five encoder blocks ... is enough to almost reach the performance of training all encoder blocks."* Diminishing returns up the encoder stack — the upper blocks carry most of the task-relevant signal.

## Design rule

*"Generally, we want frozen layers to be followed by trainable layers."* — Ch 11. Don't sandwich frozen layers between trainable layers. The intuition: gradients flowing through a frozen block can't update its weights, so the layers above it must absorb all the adaptation; sandwiching freezes everywhere upstream of any frozen block.

## When freezing's payoff scales

*"When you are training for multiple epochs, the difference (in training time and resources) between freezing and not freezing often becomes larger."* — Ch 11. For one-epoch quick experiments the gap is modest; for multi-epoch production runs, freezing can save real money.

## Layer freezing vs PEFT

| Approach | Trainable params | Quality (vs full FT on GLUE) |
|---|---|---|
| Full fine-tuning | 100% | 100% (baseline) |
| [[PartialFinetuning|Partial FT]] / layer freezing | ~25% (Houlsby et al. 2019, BERT-large) | ~100% |
| [[lora|LoRA]] | 0.0027% of GPT-3 | ~100% |

Per [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]: partial FT is *"parameter-inefficient"* compared to LoRA — needs ~25% of params to match what LoRA does with 0.0027%. Layer freezing remains useful as a **simple, no-extra-libraries** way to reduce training cost when LoRA isn't an option (e.g., small encoder models where the LoRA savings are negligible).

## Connections

- [[hands-on-llm-ch11-fine-tuning-representation-models]] — primary source.
- [[PartialFinetuning]] — the broader concept.
- [[FineTuning]] / [[FullFinetuning]] — parent operations.
- [[lora]] / [[PEFT]] — modern parameter-efficient alternatives.
- [[gradualunfreezing]] — Howard & Ruder 2018 schedule that gradually unfreezes layers over training.
- [[bert]] — Ch 11's worked target model (12 encoder blocks).
- [[FineTuningBert]] — the broader BERT fine-tuning template.
