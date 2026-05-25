---
title: "AI-Powered Data Synthesis"
type: concept
tags: [dataset-engineering, synthetic-data, llm, ai-generation]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# AI-Powered Data Synthesis

Using **AI models themselves to generate training data**. Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], this is the modern subclass of [[DataSynthesis|data synthesis]] — distinct from [[RuleBasedDataSynthesis|rule-based]] (templates) and [[Simulation|simulation]] traditional approaches, and made viable only once LLMs could generate human-indistinguishable text.

## Techniques surveyed in Ch 8

| Technique | Example |
|---|---|
| **Paraphrasing** | "How to reset my password?" → 3 variants |
| **[[Backtranslation\|Back-translation]]** | X (English) → Y (Lao) → X' (English); compare X' to X to verify Y |
| **[[CodeBackTranslation\|Code back-translation]]** | code → AI explanation → AI-regenerated code → faithfulness check (Llama 3) |
| **[[InstructionDataSynthesis\|Instruction synthesis]]** | AI generates (instruction, response) pairs |
| **[[ReverseInstruction\|Reverse instruction]]** | Start from high-quality content; AI generates a matching prompt |
| **AI-simulated APIs** | [[StableToolBench]] for tool-use training |
| **Self-play** | [[OpenAIDota2\|Dota 2]], AlphaGo — agent generates its own data |
| **Programming-language translation** | Llama 3 SFT data extended to additional languages |

## Synthetic datasets that became canonical

- **[[AlpacaDataset|Alpaca]]** — 175 seed → 52K via text-davinci-003.
- **[[UltraChat]]** — ChatGPT-driven topic tree, multi-turn dialogue.
- **[[MetaMath]]** — MATH + GSM-8K rewritten 15K → 400K.
- **[[Cosmopedia]]** — 25B tokens of synthetic textbooks/blogs/stories via Mixtral-8x7B.
- **[[AlphaGeometry]]** — 100M synthetic geometry problems.
- **[[Nemotron4|Nemotron-4 340B]]** — 98% synthetic data in post-training.

## Why post-training, not pre-training

> "AI can generate data for both pre-training and post-training, though synthetic data is intentionally included much more often in post-training than in pre-training."

Two reasons:

1. Pre-training's goal is to add knowledge; AI is better at restructuring existing knowledge than introducing new knowledge.
2. Post-training (instruction + preference) data is **the most expensive** to produce manually, so the ROI of synthesis is highest there.

## The Llama 3 coding pipeline (Ch 8 case study)

Combines three AI-synthesis methods:

1. Generate problem descriptions across diverse topics.
2. Generate solutions in multiple languages with CoT reasoning.
3. Generate unit tests + run linters/parsers; fix errors via prompted self-revision.
4. Translate code across languages; filter failures.
5. Generate conversations about code (explanation + documentation); filter via back-translation.

Result: **2.7 million synthetic coding examples** for Llama 3.1 SFT.

## Verification is the bottleneck

Per Ch 8: "Most of the synthetic data used to train Llama 3 is coding-related" — because coding is **functionally verifiable**. Domains where verification is harder synthesize less successfully.

## Connections

- [[DataSynthesis]] — parent concept.
- [[RuleBasedDataSynthesis]] / [[Simulation]] — the two traditional sibling techniques.
- [[InstructionDataSynthesis]] / [[ReverseInstruction]] / [[Backtranslation]] / [[CodeBackTranslation]] — sub-techniques.
- [[knowledgedistillation]] — the canonical AI-generated-data use case.
- [[ModelCollapse]] / [[SuperficialImitation]] — the limits of AI-generated data.
- [[FirstPositionBias]] — verification-time bias mitigation.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
