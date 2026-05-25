---
title: "Model Adaptation"
type: concept
tags: [ai-engineering, adaptation, prompt-engineering, finetuning]
sources: [ai-engineering-ch01-intro, ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Model Adaptation

**The umbrella term for techniques that tailor a pretrained [[FoundationModel|foundation model]] to a specific application's needs.** Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]], model adaptation is the central activity of [[AIEngineering|AI engineering]] — what *"working with foundation models"* actually means in practice. Huyen splits adaptation techniques into two families based on whether they update model weights.

## Two families

### 1. [[PromptBasedAdaptation|Prompt-based techniques]] — no weight updates

You adapt the model **by giving it instructions and context** rather than changing the model itself.

- **[[PromptEngineering|Prompt engineering]]** — craft instructions, few-shot examples, system messages.
- **[[rag|RAG]]** — supplement prompts with retrieved data (e.g., a database of customer reviews).
- Easier to get started, less data needed, lets you experiment across many models.
- May not suffice for complex tasks or strict performance bars.

### 2. [[FineTuning|Finetuning]] — weight updates

You adapt the model **by making changes to the model itself.**

- Requires training data and compute.
- Can improve quality, latency, and cost significantly.
- Necessary when prompt-based techniques can't reach the [[UsefulnessThreshold|usefulness threshold]] — especially for adapting to tasks not seen during pretraining.

## Data scaling

- **Pretraining from scratch** → most data (1M+ examples, months of compute).
- **Finetuning** → middle (thousands–tens of thousands of examples).
- **Prompt engineering** → least (10 examples and a weekend).

Huyen's rule of thumb: *"ten examples and one weekend versus 1 million examples and six months"* captures the cost asymmetry that makes [[AIEngineering|AI engineering]] viable for non-frontier-lab teams.

## Why adaptation is the right framing

Per [[SamAltman|Sam Altman]] (quoted in Ch 1): the resources to develop foundation models from scratch belong to a handful of corporations, governments, and well-funded labs. *"The biggest opportunity for the vast majority of people will be to adapt these models for specific applications."* Model adaptation is the central technical activity of the AI-engineering discipline.

## When you'd still want a task-specific model

- **Cheaper inference** — task-specific models can be much smaller, faster, and cheaper to run.
- **Latency-critical** workloads.
- **Specialized data** that doesn't appear in general pretraining corpora.

Huyen frames this as the **buy-or-build question** that every team must answer.

## Connections

- [[PromptEngineering]] / [[rag]] / [[FineTuning]] — the three core adaptation techniques.
- [[FoundationModel]] — the substrate.
- [[AIEngineering]] — the discipline organized around adaptation.
- [[AIEngineeringVsMLEngineering]] — adaptation is what most distinguishes AI engineering from ML engineering.
- [[UsefulnessThreshold]] — the bar adaptation has to clear.
- [[ai-engineering-ch01-intro]] — primary source.

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

Ch 7 is the deep dive on the **finetuning branch** of model adaptation. [[ChipHuyen|Huyen]] sharpens the decision tree from Ch 1:

### The adaptation cascade (Ch 7's prescription)

1. **Prompting alone** — best practices from Ch 5; systematically version prompts.
2. **Few-shot prompting** — 1–50 examples.
3. **[[rag|RAG]] with [[BM25]]** — start with term-based retrieval; jump to embedding-based only if needed.
4. **Finetuning** — only after the above, and only for [[BehaviorBasedFailure|behavior-based failures]].
5. **RAG + finetuning combined** — the last 5–10%.

### When finetuning beats prompting (Ch 7)

- Domain-specific syntaxes/styles that off-the-shelf models miss (less popular SQL dialects).
- [[StructuredOutputs|Structured outputs]] for domain-specific languages with few internet examples.
- [[BiasMitigationFinetuning|Bias mitigation]] via curated data.
- Cost optimization — replace a large prompt+model with a smaller finetuned model.

### When NOT to finetune (Ch 7)

- Early-stage experimentation (start with prompts).
- When base models are improving faster than your finetune cadence.
- When prompt experiments haven't been systematic.
- For information-based failures (use RAG instead).
