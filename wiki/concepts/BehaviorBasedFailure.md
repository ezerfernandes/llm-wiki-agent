---
title: "Behavior-Based Failure"
type: concept
tags: [failure-modes, finetuning, rag]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Behavior-Based Failure

A model failure mode where **the model produces factually correct but malformed, irrelevant, or stylistically wrong output**. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], this is one of two failure-mode categories that drive the RAG-vs-finetuning decision (the other being [[InformationBasedFailure]]).

## Examples from Ch 7

- **Factually correct but task-irrelevant**: *"You ask the model to generate technical specifications for a software project to provide to your engineering teams. While accurate, the generated specs lack the details your teams need."*
- **Wrong output format**: *"You asked the model to write HTML code, but the generated code didn't compile, it might be because the model wasn't sufficiently exposed to HTML in its training data."*
- **Wrong domain syntax**: model good at standard SQL but fails on a less common SQL dialect.
- **Tone / style mismatches** that prompt engineering can't fully fix.

## The fix: [[FineTuning|finetuning]], not RAG

Per Ch 7's core rule — **"finetuning is for form, and RAG is for facts"** — behavior-based failures call for finetuning. The model already has the relevant facts; what it needs is **exposure to the target form/style/syntax**.

[[StructuredOutputs|Structured outputs]] are the cleanest case: when off-the-shelf models can't reliably emit a domain-specific language, finetuning on examples of that DSL is the recommended fix.

## Connection to [[SemanticParsing|semantic parsing]]

> "Semantic parsing is a category of tasks whose success hinges on the model's ability to generate outputs in the expected format and, therefore, often requires finetuning." — Ch 7

Semantic parsing — converting natural language to structured outputs like JSON, YAML, SQL — is the canonical behavior-based-failure domain.

## Connections

- [[InformationBasedFailure]] — the sibling failure category that calls for [[rag|RAG]] instead.
- [[FineTuning]] — the fix.
- [[StructuredOutputs]] / [[SemanticParsing]] — the canonical sub-domains.
- [[ai-engineering-ch07-finetuning]] — primary source.
