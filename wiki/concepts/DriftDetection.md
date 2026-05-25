---
title: "Drift Detection"
type: concept
tags: [observability, monitoring, drift, llm-app]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Drift Detection

**The observability sub-discipline of catching when *some part of the AI application's behavior has changed* — even when nothing was visibly deployed.** Per [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]]: *"The more parts a system has, the more things that can change."*

Ch 10 names three drift sources specific to AI apps. They are distinct from the classical ML notions of [[ConceptDrift|concept drift]] / [[DataDrift|data drift]] / [[TargetDrift|target drift]] — those are about the *world* shifting; drift detection in this chapter is about the *system* shifting.

## Three drift sources in AI applications

### 1. System-prompt drift

> *"There are many reasons why your application's system prompt might change without your knowing. The system prompt could've been built on top of a prompt template, and that prompt template was updated. A coworker could've found a typo and fixed it."* — Ch 10

**Defense**: *"a simple logic should be sufficient to catch when your application's system prompt changes."* Hash the rendered system prompt at deploy time; alert on diffs.

### 2. User-behavior drift

> *"Over time, users adapt their behaviors to the technology. … People living in areas with self-driving cars have already figured out how to bully self-driving cars into giving them the right of way (Liu et al., 2020). … Your users might learn to write instructions to make the responses more concise. This might cause a gradual drop in response length over time."* — Ch 10

**Defense**: longitudinal monitoring of input statistics (length, structure, vocabulary). A gradual shift in metrics whose cause isn't system-side often *is* user-behavior drift. Investigation needed to localize.

### 3. [[SilentModelUpdate|Silent underlying-model updates]]

> *"When using a model through an API, it's possible that the API remains unchanged while the underlying model is updated. … Model providers might not always disclose these updates, leaving it to you to detect any changes."* — Ch 10

The canonical incidents:

- **Chen et al. (2023)** observed notable differences in benchmark scores between the March 2023 and June 2023 versions of GPT-4 and GPT-3.5 — same API endpoint.
- **[[Voiceflow]]** reported a **10% performance drop** switching from `gpt-3.5-turbo-0301` to `gpt-3.5-turbo-1106`.

**Defense**: pin to versioned endpoints when possible; maintain a small held-out evaluation set that runs continuously against production traffic; alert on metric shifts.

## Why drift detection is non-optional for AI apps

A classical web app's behavior is fixed by its code. An AI app's behavior is a product of code × prompt × model × user-input distribution. Three of those four can drift without a deploy. Without explicit drift detection, [[MTTD]] for these failure modes is effectively infinite — the application keeps working from the infrastructure's perspective.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[SilentModelUpdate]] — the most operationally painful drift source.
- [[Voiceflow]] — case study.
- [[ConceptDrift]] / [[DataDrift]] / [[TargetDrift]] — classical-ML sibling notions (about the world, not the system).
- [[observability]] / [[Monitoring]] — parent disciplines.
- [[MTTD]] — drift detection lowers MTTD on this class of failure.
- [[Evaluation]] — held-out eval-on-prod-traffic is the defensive pattern.
