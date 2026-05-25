---
title: "Reverse Instruction"
type: concept
tags: [dataset-engineering, synthetic-data, instruction-tuning]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Reverse Instruction

**Synthetic-instruction-data technique that fixes the response first and asks AI to generate the matching prompt.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], reverse instruction starts from existing high-quality long-form content (stories, books, Wikipedia articles) and uses AI to generate prompts that would elicit such content. Pioneers: Köksal et al. (2023), Li et al. (2023), Chen et al. (2023).

The wiki also has [[Backtranslation]] which is a more general AI-data-synthesis term covering both directions; reverse instruction is the specific application where the *response* is the high-quality artifact.

## Why it works

Long-form AI responses hallucinate more than short ones. By using **human-quality long content as the response**, the synthetic dataset avoids AI hallucination on the harder side of the (instruction, response) pair. The shorter prompt is the easier side for AI to generate accurately.

## Iterative-bootstrapping variant (Li et al. 2023)

1. Start with a small seed set; train a weak model.
2. Use the weak model to generate instructions for existing high-quality content.
3. Finetune the weak model on this new instruction data.
4. Repeat until desirable performance.

In theory, this enables continual self-improvement; in practice, [[ModelCollapse|model collapse]] and [[SuperficialImitation|superficial imitation]] are open risks.

## Relationship to model distillation

Reverse instruction can be used in a [[knowledgedistillation|distillation]] setup, but per Ch 8's caveat, **not all reverse-instruction bootstrapping is distillation**: when the teacher is smaller than the student (as in [[Nemotron4|Nemotron-4]], where Mixtral-8x7B teacher trained a 340B student), the operation is reverse-direction.

## Connections

- [[Backtranslation]] — broader sibling technique (translate any direction, verify by back-translation).
- [[AIPoweredDataSynthesis]] — parent category.
- [[InstructionDataSynthesis]] — the parent task.
- [[ReversePromptEngineering]] — unrelated namesake (security context, not data synthesis).
- [[Cosmopedia]] / [[MetaMath]] — datasets that use related synthesis approaches.
- [[knowledgedistillation]] — adjacent technique.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
