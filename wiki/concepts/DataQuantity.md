---
title: "Data Quantity"
type: concept
tags: [dataset-engineering, data-curation, finetuning]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Data Quantity

The dimension of dataset design that asks "**how much data do you need?**" Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], it is one of the three orthogonal data-design axes alongside [[DataQuality|quality]] and [[DataCoverage|coverage]]. [[ChipHuyen|Huyen]]'s framing: "Asking how much data you need is like asking how much money you need. The answer varies widely from one situation to the next."

## The realistic range

| Setting | Examples |
|---|---|
| One-shot finetuning experiments | **1** (Jeremy Howard + Jonathan Whitaker showed LLMs can learn from a single example) |
| Quick validation | 50–100 examples |
| Small PEFT finetune | hundreds–thousands |
| Full finetuning | tens of thousands–millions |
| [[LIMA]] reference | 1,000 curated |
| [[Llama|Llama 2]] pre-training | **2 trillion tokens** ≈ 1 billion examples @ 2K tokens each |
| [[Llama|Llama 3]] pre-training | **15 trillion tokens** |

## The three multipliers on "how much"

Per Ch 8, beyond quality and coverage, three factors set data demand:

1. **Finetuning technique** — full finetuning needs **orders of magnitude more** data than [[PEFT|PEFT]] like [[lora|LoRA]]. Tens of thousands → full FT; few hundred → PEFT.
2. **Task complexity** — sentiment classification needs less than financial-filings QA.
3. **Base-model performance** — closer base → fewer examples needed. **More advanced models give better small-data gains** — OpenAI experiment: at 100 examples, GPT-4 ≫ Babbage; at 550K examples, all converge.

## The diminishing-returns curve

Performance gain per additional example shrinks as the dataset grows. The first 1,000 examples might add 10 points of accuracy; the next 1,000 might add 5. Plot performance vs dataset size on subsets (25% / 50% / 100%) to forecast the gain from doubling your data:

- **Steep slope** → doubling pays off.
- **Plateau slope** → doubling won't help; either improve quality / coverage or switch technique.

## The validation start

> "Before investing in curating a large dataset, you might want to start with a small, well-crafted dataset (e.g., 50 examples) to see if finetuning can improve the model. ... If no improvement is observed with small data, a bigger dataset will rarely do the trick."

## The heuristic

**Small data → PEFT on big base model. Large data → full FT on small base model.**

## [[Ossification|Ossification]] — when more data backfires

At millions-of-examples scale, finetuning a pre-trained model can underperform **training from scratch** because pre-training "ossified" the weights (Hernandez et al. 2021). Smaller models are more susceptible. This is the rare regime where more data points back toward training from scratch.

## Cost-constrained quantity

> "If you budget $10,000 for data annotation and each example costs $2 to annotate, you can have at most 5,000 examples."

Data and compute trade off against each other in any fixed budget. The chapter recommends balancing them rather than always maximizing data.

## Connections

- [[DataQuality]] / [[DataCoverage]] — the other two design axes.
- [[FineTuning]] / [[FullFinetuning]] / [[PEFT]] / [[lora|LoRA]] — the technique that multiplies how much data is "enough".
- [[Ossification]] — the rare regime where more data + finetuning loses to training-from-scratch.
- [[LIMA]] — the canonical small-data evidence.
- [[DataFlywheel]] — the strategic-quantity argument: capture user data to grow over time.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
