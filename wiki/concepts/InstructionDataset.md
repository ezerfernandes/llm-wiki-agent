---
title: "Instruction Dataset"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning]
last_updated: 2026-05-22
---

## Definition
Dataset of instruction-answer pairs used as the training data for SFT.

## In LLM Engineer's Handbook
A dataset where every sample is a pair of an instruction (model input) and an answer (expected output), optionally augmented with a system meta-prompt and an input data field. Used as training data for [[SupervisedFinetuning]]. Quality dimensions per [[leh-ch05-supervised-fine-tuning]]: accuracy, diversity, complexity. Pipeline stages: curation, [[RuleBasedFiltering]], [[DataDeduplication]], [[DataDecontamination]], quality evaluation ([[LLMAsAJudge]] / [[RewardModel]]), exploration ([[TopicClustering]]), generation ([[EvolInstruct]] / [[UltraFeedback]]), augmentation.
