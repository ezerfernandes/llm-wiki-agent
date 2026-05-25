---
title: "Instruction Data Synthesis"
type: concept
tags: [dataset-engineering, synthetic-data, sft, instruction-tuning]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Instruction Data Synthesis

**AI-generated (instruction, response) pairs** for [[SupervisedFinetuning|SFT]] / instruction tuning. Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], this is the most common form of [[AIPoweredDataSynthesis|AI-powered data synthesis]] — because instruction data is "the most effort to produce" of all post-training data formats.

## Split by who-generates-what

| Pattern | Use case |
|---|---|
| AI instructions + AI responses | Maximum scale; needs strong verification (Alpaca, Cosmopedia) |
| AI instructions + human responses | Hard-to-write responses; rare-domain (medical, legal) |
| Human instructions + AI responses | Standard "answer at scale" pattern |
| Reverse: existing content → AI prompts | [[ReverseInstruction\|Reverse instruction]] — best for long-form content |

## Instruction-generation tactics

To ensure coverage:

- Start with a topic / keyword list — AI generates N instructions per item.
- Start with a template list — AI generates N examples per template.
- AI can generate both the topic list and the templates.

[[UltraChat]] example (Ding et al. 2023): asked ChatGPT for 30 topics about daily life → 30-50 subtopics each → instructions + responses per subtopic.

## Response-generation tactics

- Single response per instruction (standard).
- Multiple responses per instruction (used for [[PreferenceFinetuning|preference]] data generation).

## Long-content problem

AI struggles with high-quality long responses more than short instructions — the longer the response, the more hallucination surface. **[[ReverseInstruction|Reverse instruction]] solves this**: start with verified long content (stories, Wikipedia, books); have AI generate matching prompts.

## Iterative bootstrapping

Li et al. (2023) recipe:

1. Start with seed examples; train a weak model.
2. Use the weak model to generate instructions for high-quality content.
3. Finetune the weak model on the new instruction data.
4. Repeat.

This bootstraps a model upward without manual annotation — though Ch 8 cautions whether unbounded recursive bootstrapping is practical remains an open question (see [[ModelCollapse]]).

## Long-context finetuning data synthesis

To extend a model from 8K to 128K tokens:

- Split long documents into chunks under 8K.
- For each chunk, generate (question, answer) pairs.
- Use the **original full document** as context for the QA pair — training the model on long contexts even though the QA pair was generated on a short chunk.

## Connections

- [[AIPoweredDataSynthesis]] — parent.
- [[ReverseInstruction]] — the long-content variant.
- [[AlpacaDataset]] / [[UltraChat]] / [[MetaMath]] / [[Cosmopedia]] — canonical synthetic instruction datasets.
- [[SelfInstruct]] — the seed-instruction-synthesis approach used by Alpaca.
- [[SupervisedFinetuning]] / [[InstructDataset]] — the downstream consumers.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
