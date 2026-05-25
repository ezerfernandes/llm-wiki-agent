---
title: "Chen et al. 2019 — Gmail Smart Compose"
type: entity
tags: [paper, gmail, autocomplete, privacy, llm]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Chen et al. 2019 — Gmail Smart Compose

[[google|Google]] paper describing the **Gmail Smart Compose / auto-complete model**, *trained on users' emails*. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the canonical example of a deployed model trained on private data — where [[TrainingDataExtraction|training-data extraction]] would reveal real personal information.

## Why Ch 5 cites it

The paper is invoked as an illustrative example for the **privacy violation** risk class of [[InformationExtraction|information extraction]] attacks:

> "Many models are trained on private data. For example, Gmail's auto-complete model is trained on users' emails (Chen et al., 2019). Extracting the model's training data can potentially reveal these private emails." — Ch 5

If you can extract training data from a foundation model, and that training data includes emails, then by extraction you can read other users' emails — *without breaking into the Gmail database*.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[google|Google]] — Gmail's parent company.
- [[InformationExtraction]] / [[TrainingDataExtraction]] — the threat the paper exemplifies as a target.
