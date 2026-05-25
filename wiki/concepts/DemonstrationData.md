---
title: "Demonstration Data"
type: concept
tags: [post-training, sft, dataset]
sources: [ai-engineering-ch02-foundation-models, ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Demonstration Data

The **(prompt, response) pairs** used as training input for [[SupervisedFinetuning|supervised finetuning]]. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "Such examples follow the format (prompt, response) and are called demonstration data. Some people refer to this process as [[BehaviorCloning|behavior cloning]]: you demonstrate how the model should behave, and the model clones this behavior."

## Composition

Demonstration data should contain **the range of requests you want the model to handle**: question answering, summarization, translation, classification, brainstorming, etc. The distribution OpenAI used for InstructGPT (per Ch 2 Figure 2-12) reflects this multi-task mix.

## Examples (InstructGPT, from Ch 2 Table 2-6)

| Prompt (excerpt) | Labeler's response (excerpt) |
|---|---|
| *"Serendipity means ... Use the word in a sentence."* | *"Running into Margaret and being introduced to Tom was a fortunate stroke of serendipity."* |
| *"ELI5: What's the cause of the 'anxiety lump' ...?"* | *"The anxiety lump in your throat is caused by muscular tension keeping your glottis dilated..."* |

These are not simple categorical labels — **they require critical thinking, information gathering, and judgment** about the appropriateness of the user's requests.

## Why labeler quality matters

> "Good teachers are important for humans to learn. Similarly, good labelers are important for AIs to learn how to conduct intelligent conversations." — Ch 2

InstructGPT labelers: ≈90% college-educated, ≥1/3 with master's degrees. ≈$10/pair × 13K pairs = $130K (Ch 2) — and that excludes design, recruiting, and quality control costs.

## Quantity vs cost trade-off

- **InstructGPT**: 13,000 (prompt, response) pairs × ~$10 each ≈ $130,000.
- **[[LAION]]**: 13,500 *volunteers* produced 10,000 conversations / 161,443 messages / 35 languages — much larger but demographically skewed (90% male per self-report).
- **DeepMind Gopher**: filtered web data heuristically for `[A]: [paragraph] [B]: [paragraph]` patterns — even cheaper, no manual labeling.
- **AI-generated synthetic demonstrations** — Ch 8 discusses this in depth.

## Connections
- [[SupervisedFinetuning]] — the stage that consumes demonstration data.
- [[BehaviorCloning]] — the SFT learning paradigm.
- [[ComparisonData]] — the preference-stage data format (winner/loser pairs).
- [[LAION]] — the volunteer-labeled conversation dataset.
- [[DatasetEngineering]] — the broader discipline.
- [[ai-engineering-ch02-foundation-models]] — primary source.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

Ch 8 expands the demonstration-data picture in three ways:

### Single-turn vs multi-turn

> "Single-turn data helps train a model to respond to individual instructions. Multi-turn data, on the other hand, teaches the model how to solve tasks — many real-world tasks involve back-and-forth."

Single-turn is easier to obtain; multi-turn requires purpose-built scenarios. [[UltraChat]] is Ch 8's example of synthetic multi-turn demonstration data.

### Special demonstration formats

- **[[chainofthought|CoT]] demonstration data** — example responses include step-by-step reasoning. Chun et al. (2024) showed nearly doubling accuracy on certain CoT tasks. **Less common than other instruction datasets** because step-by-step responses are tedious.
- **[[ToolUse|Tool-use]] demonstration data** — multi-message turns with headers specifying source and destination (Llama 3's multi-message chat format, Dubey et al. 2024). Often synthesized via [[Simulation]] because AI's optimal tool patterns differ from humans'.

### Removing demonstration data, not just adding

Per Ch 8's "unlearning bad behaviors" example: a chatbot annoying users with unsolicited rewriting suggestions can be fixed by **removing** the training examples that demonstrate that behavior, not just by adding new ones. Demonstration data curation is bidirectional.

### Synthetic demonstration data

Ch 8's deepest extension to Ch 2: the (prompt, response) pair can be AI-generated, with [[AlpacaDataset|Alpaca]], [[UltraChat]], [[Cosmopedia]], [[MetaMath]] as canonical examples. The [[InstructionDataSynthesis]] page captures this more fully.
