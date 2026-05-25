---
title: "Open Model"
type: concept
tags: [model-class, license, open-source]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Open Model

A model that ships with **both weights AND training data public**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "The term 'open model' is used for models that come with open data."

## Why open data matters

- **Retrain from scratch** with modifications to architecture, training process, or data itself.
- **Audit** — make sure data wasn't compromised or illegally acquired.
- **Understand** the model — its biases, capabilities, and limits trace back to its data.

> "Some use cases also required access to the training data for auditing purposes, for example, to make sure that the model wasn't trained on compromised or illegally acquired data."

## Practical reality

As of late 2024, fully-open models are a small minority of "open source" models. Most so-called open-source models are [[OpenWeight|open weight only]].

> "While [open data] sounds great in theory, in practice, it's challenging for any company to thoroughly inspect a dataset of the size typically used to train foundation models."

The data is technically inspectable, but inspecting trillions of tokens is its own engineering project.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[OpenWeight]] / [[OpenSourceModel]] / [[CommercialModel]] — sibling categories.
- [[ModelLicense]] — the license layer.
- [[DataContamination]] — what training-data inspection can detect.
- [[ModelBuildVsBuy]] — the decision framing.
