---
title: "DSPy Learn — Index"
type: source
tags: [dspy, documentation, framework, llm-programming]
date: 2026-05-17
source_file: raw/dspy-learn-index.md
---

# DSPy Learn — Index

Top-level index page of the [[DSPy]] *Learn* documentation section ([dspy.ai/learn/](https://dspy.ai/learn/)). Frames DSPy as a small learnable API for building AI systems and organizes the learning path into a strict **three-stage model**: **Programming → Evaluation → Optimization**. The page is page 1 of 13 in the Learn section; the remaining 12 pages (Programming Overview, Language Models, [[DSPySignatures|Signatures]], [[DSPyModules|Modules]], [[DSPyAdapters|Adapters]], [[DSPyTools|Tools]], [[ModelContextProtocol|MCP]], Evaluation Overview, Data Handling, [[DSPyMetrics|Metrics]], Optimization Overview, [[DSPyOptimizers|Optimizers]]) each cover one stage-component in detail.

## Summary

DSPy structures the development of LLM-based AI systems as three sequential stages — **Programming** (define the task, its constraints, an initial pipeline), **Evaluation** (collect a dev set, define a metric, measure the system), and **Optimization** (use DSPy optimizers to tune prompts or weights). The page argues the order is load-bearing: "it's unproductive to launch optimization runs using a poorly designed program or a bad metric." The Learn section's thirteen pages are partitioned across these three stages, and the index page serves as the entry point pointing to each.

## Key Claims

- **DSPy provides a small, learnable API for building AI systems** through an iterative development process. Scope is *programming* AI systems, not training base models.
- **Three-stage model.** Stage 1 — **Programming**: "defining your task, its constraints, exploring a few examples, and using that to inform your initial pipeline design." Stage 2 — **Evaluation**: "collect an initial development set, define your DSPy metric, and use these to iterate on your system more systematically." Stage 3 — **Optimization**: "use DSPy optimizers to tune the prompts or weights in your program."
- **Stage order matters.** "It's unproductive to launch optimization runs using a poorly designed program or a bad metric" — Optimization presupposes Evaluation, which presupposes Programming.
- **Programming covers seven sub-topics**: Programming Overview, Language Models, [[DSPySignatures|Signatures]], [[DSPyModules|Modules]], [[DSPyAdapters|Adapters]], [[DSPyTools|Tools]], [[ModelContextProtocol|MCP]].
- **Evaluation covers three sub-topics**: Evaluation Overview, Data Handling, [[DSPyMetrics|Metrics]].
- **Optimization covers two sub-topics**: Optimization Overview, [[DSPyOptimizers|Optimizers]].
- **Tune prompts *or* weights.** The Optimization stage explicitly allows for both prompt-only tuning (the more common DSPy use case) and weight-level tuning (when fine-tuning is available), placing DSPy in the *both-axes* design space.

## Key Quotes

> "defining your task, its constraints, exploring a few examples, and using that to inform your initial pipeline design" — Programming stage definition

> "collect an initial development set, define your DSPy metric, and use these to iterate on your system more systematically" — Evaluation stage definition

> "use DSPy optimizers to tune the prompts or weights in your program" — Optimization stage definition

> "it's unproductive to launch optimization runs using a poorly designed program or a bad metric" — the stage-order discipline

## Connections

- [[DSPy]] — the framework whose Learn documentation this page heads. Entity page created with this ingest.
- [[DSPySignatures]] — declarative input-output spec; covered in the *Signatures* sub-page of Learn (forward reference for the next ingest).
- [[DSPyModules]] — composable program-building blocks; covered in the *Modules* sub-page (forward reference).
- [[DSPyOptimizers]] — prompt / weight tuners that drive the Optimization stage (forward reference to the *Optimizers* sub-page).
- [[DSPyAdapters]], [[DSPyTools]], [[DSPyMetrics]] — sub-page forward references for Adapters, Tools, and Metrics respectively.
- [[ModelContextProtocol|MCP]] — referenced as one of the Programming sub-pages; the Anthropic-introduced protocol for tool/context plumbing.
- [[LanguageModel]] — the *Language Models* sub-page is the integration layer between DSPy and underlying LMs.
- [[PromptEngineering]] — DSPy's prompt-tuning optimizers automate part of what hand-written prompt engineering does manually; an explicit alternative-mechanism relation.
- [[2604.25850-agentic-harness-engineering]] — already in the wiki and explicitly counterposes itself against "DSPy-style instruction tuning" (the source flags this in its *Connections* section); this ingest gives that prior reference a wiki target.

## Contradictions

- None at the index-page level. The Learn index is a high-level framing page with no claims that conflict with existing wiki content; it simply names DSPy and previews its sub-pages. Any contradictions with the wiki's view of LLM-programming abstractions (e.g. *vs.* [[2604.25850-agentic-harness-engineering|harness engineering]] or [[2605.03310-coordination-architectural-layer|coordination as architectural layer]]) will surface in the later sub-page ingests where DSPy's actual mechanisms (Signatures / Modules / Optimizers) are described in detail.
