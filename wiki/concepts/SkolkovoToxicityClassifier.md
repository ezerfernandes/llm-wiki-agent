---
title: "Skolkovo Toxicity Classifier"
type: concept
tags: [model, classifier, safety, toxicity]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Skolkovo Toxicity Classifier

A **specialized toxicity classifier** from the Skolkovo Institute of Science and Technology. Cited by [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]] alongside [[FacebookHateSpeech|Facebook's hate-speech model]] and [[PerspectiveAPI]] as examples of cheap specialized [[Safety|safety]] classifiers that beat general-purpose [[LLMAsAJudge|AI judges]] on cost.

Originally developed for human-generated content; repurposable for AI outputs since toxicity detection generalizes across producers.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[Safety]] — what it scores.
- [[FacebookHateSpeech]] / [[PerspectiveAPI]] — sibling specialized classifiers.
- [[LlamaGuard]] / [[OpenAIModeration]] — competing LM-based approaches.
