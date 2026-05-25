---
title: "Evol-Instruct"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning, leh-ch07-evaluating-llms, ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

## Definition
LLM-driven instruction augmentation that evolves prompts in-depth (complexity) and in-breadth (diversity).

## In LLM Engineer's Handbook
Evol-Instruct (WizardLM team) uses a powerful LLM to evolve simple instructions into harder ones, then regenerates answers. In-depth strategies: constraints, deepening, concretizing, increasing reasoning steps, complicating input. In-breadth: generate new instructions in the same domain. [[leh-ch05-supervised-fine-tuning]] (Table 5.4) gives the AutoEvol rewriter prompt (Zeng et al. 2024, arXiv:2406.00770); [[leh-ch07-evaluating-llms]] cites it as the inspiration for Ragas's synthetic test-set generation.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

Within Ch 8's [[InstructionDataSynthesis|instruction data synthesis]] taxonomy, Evol-Instruct is one of the canonical *seed-expansion* techniques sitting alongside [[SelfInstruct|Self-Instruct]] — the difference being that Evol-Instruct iteratively *evolves* instructions in depth and breadth, whereas Self-Instruct primarily samples and rewrites in flat distribution.

Both produce synthetic [[InstructDataset|instruction datasets]] suitable for [[SupervisedFinetuning|SFT]] and both rely on a strong base model as the synthesis engine. See [[AIPoweredDataSynthesis]] for the full Ch 8 taxonomy.
