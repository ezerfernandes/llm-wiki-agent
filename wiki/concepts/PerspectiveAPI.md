---
title: "Perspective API"
type: concept
tags: [api, safety, toxicity, classifier]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Perspective API

A **specialized toxicity-classification API** developed by [[Jigsaw]] (Google's subsidiary). Cited by [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]] as one of the canonical examples of cheap specialized [[Safety|safety]] classifiers that beat general-purpose [[LLMAsAJudge|AI judges]] on cost:

> "These specialized models tend to be much smaller, faster, and cheaper than general-purpose AI judges. Examples of these models are Facebook's hate speech detection model, the Skolkovo Institute's toxicity classifier, and Perspective API."

## What it does

Given a piece of text, returns probability scores for attributes like *toxicity, severe toxicity, identity attack, insult, profanity, threat, sexually explicit*. Designed for moderating online comments — repurposable for AI-generated text since toxicity detection generalizes across producers.

## Position

Sibling to [[FacebookHateSpeech]] and [[SkolkovoToxicityClassifier]] in the specialized-classifier landscape. Each is cheaper than running GPT-4 as a moderation judge, at the cost of being constrained to one task.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[Jigsaw]] — authoring organization.
- [[Safety]] — what it scores.
- [[FacebookHateSpeech]] / [[SkolkovoToxicityClassifier]] — sibling specialized classifiers.
- [[OpenAIModeration]] / [[LlamaGuard]] — competing approaches that use general LMs.
