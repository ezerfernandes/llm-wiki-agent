---
title: "Amazon"
type: entity
tags: [company, cloud, ai]
sources: [d2l-preface, d2l-hyperparameter-optimization, d2l-recommender-systems, d2l-appendix-tools, 2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# Amazon

Amazon and its cloud-computing subsidiary **Amazon Web Services (AWS)**. Cited in [[d2l-preface]] as the original employer of D2L co-authors [[MuLi]] and [[AlexanderSmola]], the backer of the [[MXNet]] framework (the original D2L primary framework), and the funder of the book's writing — preface explicitly thanks Wen-Ming Ye, George Karypis, Swami Sivasubramanian, Peter DeSantis, Adam Selipsky, and Andy Jassy.

The preface also uses Amazon as a 1990s example of a "successful database-driven web application" whose ecosystem-of-frameworks story it draws a parallel with for deep learning.

## Connections
- [[MuLi]], [[AlexanderSmola]], [[AstonZhang]] — D2L authors affiliated with AWS at time of writing.
- [[MXNet]] — AWS's preferred deep-learning framework; original D2L primary framework.
- [[AmazonS3]], [[AmazonRedshift]], [[Kinesis]] — existing wiki sub-entities for specific AWS services.
- [[d2l-preface]] — first source citing Amazon directly.
- [[d2l-hyperparameter-optimization]] — Amazon-authored ([[AaronKlein]], [[MatthiasSeeger]], [[CedricArchambeau]]) guest chapter; introduces [[SyneTune]], Amazon's open-source distributed HPO library.
- [[d2l-appendix-tools]] — D2L's operational appendix walks through running the book on [[AmazonSageMaker]] (managed GPU notebook) and [[AmazonEC2]] (raw VM with manual CUDA install); both bottom out in the [[d2l-installation]] runbook.

## GenAI research arm

- [[AWSGenerativeAIInnovationCenter]] — Amazon's GenAI applied-research unit. Lead institution on [[2604.14585-prompt-optimization-coin-flip]] (the wiki's first paper from this unit) — a controlled empirical audit of [[PromptOptimization|prompt optimization]] in [[CompoundAISystem|compound AI systems]] that established the **49% coin-flip failure rate** and the [[CompoundAIDiagnostic|two-stage diagnostic framework]].
- [[AmazonNovaLite]] — Amazon's budget-tier LM; evaluated as a cross-vendor executor in the same study alongside [[ClaudeHaiku45|Anthropic's Claude Haiku 4.5]].
