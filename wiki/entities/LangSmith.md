---
title: "LangSmith"
type: entity
tags: [tool, prompt-monitoring, observability, llmops]
sources: [leh-ch02-tooling-and-installation, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

## What it is
LangSmith is the commercial LLM observability and evaluation platform built by the [[LangChain]] team. It captures traces, datasets, and evaluation runs for LangChain-based applications.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) lists LangSmith among the prompt-monitoring alternatives to [[Opik]] — alongside [[Langfuse]] and [[Galileo]] — but the authors prefer Opik for tighter integration with their Comet ML experiment-tracking stack.

## Connections
- [[LangChain]] — same vendor.
- [[Opik]] — chosen prompt-monitoring tool.
- [[Langfuse]] / [[Galileo]] — peers.
- [[PromptMonitoring]] — discipline.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 names LangSmith specifically for its **[[RequestTrace|request-trace]] visualization**. Figure 10-11 in the chapter shows a LangSmith trace of a request's path through an AI application — every component hit, every tool called, latency per step.

LangSmith is Ch 10's canonical example of the kind of tooling AI observability requires that goes beyond traditional infrastructure observability: AI traces have to surface the *application semantics* (which prompt template was used, which documents were retrieved, what intermediate outputs the chain produced) and not just CPU / network metrics.
