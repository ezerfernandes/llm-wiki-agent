---
title: "AI Engineering: Building Applications with Foundation Models"
type: source
tags: [book, foundation-models, ai-engineering, oreilly]
date: 2024-12-04
source_file: raw/papers/ai-engineering-chip-huyen.pdf
---

## Summary

[[ChipHuyen|Chip Huyen]]'s **AI Engineering** ([[OReilly|O'Reilly Media]], December 2024, ISBN 978-1-098-16630-4) is a practical, framework-oriented guide to building applications with foundation models. The book covers the end-to-end AI engineering process: understanding foundation models, evaluation methodology and evaluation of AI systems, prompt engineering, [[rag|RAG]] and [[Agent|agents]], [[Finetuning|finetuning]], dataset engineering, inference optimization, and architecture/user feedback. It is the spiritual successor to Huyen's *Designing Machine Learning Systems* (also O'Reilly) and positions [[AIEngineering|AI engineering]] as a distinct discipline from traditional ML engineering: it works *with* readily available foundation models rather than building models from scratch.

The book is **not a tutorial** — it provides a framework for selecting tools, trade-off analyses, and the questions to ask when evaluating a solution. It assumes basic familiarity with probability, ML concepts, neural networks, and standard metrics, but is accessible without prior ML background. Target audience: AI engineers, ML engineers, data scientists, engineering managers, technical product managers.

## Chapter Structure

The book follows the typical AI application development process. Each chapter is ingested as a separate source page:

1. [[ai-engineering-ch01-intro|Chapter 1 — Introduction to Building AI Applications with Foundation Models]] — the rise of AI engineering, use cases, planning, the AI engineering stack
2. [[ai-engineering-ch02-foundation-models|Chapter 2 — Understanding Foundation Models]] — training data, model architecture, scale, post-training, sampling
3. [[ai-engineering-ch03-evaluation-methodology|Chapter 3 — Evaluation Methodology]] — language modeling metrics, exact evaluation, AI-as-judge, comparative evaluation
4. [[ai-engineering-ch04-evaluate-ai-systems|Chapter 4 — Evaluate AI Systems]] — evaluation criteria, model selection, designing an evaluation pipeline
5. [[ai-engineering-ch05-prompt-engineering|Chapter 5 — Prompt Engineering]] — prompting techniques, prompt engineering best practices, prompt attacks and defenses
6. [[ai-engineering-ch06-rag-agents|Chapter 6 — RAG and Agents]] — retrieval-augmented generation, agentic patterns, tools, planning, memory
7. [[ai-engineering-ch07-finetuning|Chapter 7 — Finetuning]] — when to finetune, memory math, [[PEFT|PEFT]] / [[lora|LoRA]], merging, tactics
8. [[ai-engineering-ch08-dataset-engineering|Chapter 8 — Dataset Engineering]] — data curation, data synthesis, data quality, data augmentation
9. [[ai-engineering-ch09-inference-optimization|Chapter 9 — Inference Optimization]] — inference bottlenecks, model-level optimizations, service-level optimizations
10. [[ai-engineering-ch10-architecture-feedback|Chapter 10 — AI Engineering Architecture and User Feedback]] — application architecture, user feedback as evaluation signal

## Key Claims (book-level)

- **AI engineering is distinct from ML engineering.** AI engineering works with foundation models as a service; ML engineering builds models from scratch. The bottleneck shifts from training to evaluation, prompt design, context construction, and inference cost.
- **Evaluation is the hardest part of AI engineering.** The book dedicates two chapters to it (Chs 3-4) — far more than any other topic. Open-ended generation breaks classical metric pipelines; AI-as-judge and comparative evaluation are necessary but introduce their own failure modes.
- **The model's response quality depends on three optimizable aspects (outside generation settings): instructions, context, model itself.** Prompt engineering (Ch 5), context construction via RAG/agents (Ch 6), and finetuning (Ch 7) target these three respectively.
- **Start simple.** For most problems, the book starts from the simplest solution and progresses to more complex ones only as challenges rise. This applies recursively: prompt before RAG, RAG before agents, prompt before finetuning, finetuning before training-from-scratch.
- **Inference economics matter as much as model quality.** Chapter 9 frames latency, throughput, and cost as first-class engineering constraints — the book's most quantitative chapter.

## Key Quotes

> "AI engineering: the process of building applications with readily available foundation models." — book jacket

> "I'm a fan of the start-simple approach, so for many problems, I'll start from the simplest solution and then progress with more complex solutions to address rising challenges." — Preface

> "Evaluation is one of the hardest, if not the hardest, challenges of AI engineering." — Preface

> "This book isn't a tutorial. While it mentions specific tools and includes pseudocode snippets to illustrate certain concepts, it doesn't teach you how to use a tool. Instead, it offers a framework for selecting tools." — Preface

## Connections

- [[ChipHuyen]] — author (formerly Snorkel AI, [[NVIDIA]]; taught ML systems design at [[stanforduniversity|Stanford]]; founded an AI infrastructure startup, acquired)
- [[OReilly]] — publisher
- [[DesigningMachineLearningSystems]] — Huyen's prior book (2022); foundation-model-era successor
- [[AIEngineering]] — the discipline this book defines
- [[FoundationModel]] — central concept
- [[rag]] / [[Agent]] / [[FineTuning]] / [[PromptEngineering]] / [[InferenceOptimization]] / [[DatasetEngineering]] — the seven core technical pillars (Chs 5-10)
- [[Evaluation]] / [[LLMAsAJudge]] / [[ComparativeEvaluation]] — the two-chapter evaluation backbone (Chs 3-4)

## Position in the wiki corpus

This is the wiki's **first end-to-end AI-engineering textbook** — a survey-style anchor that touches almost every concept the wiki already has individual paper-level entries for ([[rag]], [[Agent]], [[lora]], [[MIPROv2]], [[chainofthought]], [[react]], [[selfconsistency]], [[Hallucination]], etc.). The per-chapter source pages cite back to the existing paper-level entries where they exist, and mint new concept/entity pages for terms the book introduces.

Where the book is denser than the wiki's prior coverage, the chapter source pages flag it; where the wiki's prior paper-level coverage is denser than the book's summary treatment, the chapter source pages link back to the paper-level pages as the authoritative entry.

## Contradictions

Flagged in individual chapter source pages where they appear. No book-level contradictions with the existing wiki corpus.

## Bibliographic detail

- **Title**: AI Engineering: Building Applications with Foundation Models
- **Author**: [[ChipHuyen|Chip Huyen]]
- **Publisher**: [[OReilly|O'Reilly Media, Inc.]]
- **Edition**: First Edition, December 2024 (Revision: 2024-12-04 First Release)
- **ISBN**: 978-1-098-16630-4
- **Copyright**: © 2025 Developer Experience Advisory LLC
- **Editorial**: Acquisitions Editor Nicole Butterfield; Development Editor Melissa Potter; Production Editor Beth Kelly
- **Source**: `raw/papers/ai-engineering-chip-huyen.pdf` (32 MB; converted to `raw/papers/ai-engineering-chip-huyen.md` via `markitdown[pdf]` — 25,135 lines / 1.1 MB)
- **Per-chapter raw splits**: `raw/papers/ai-engineering/{preface,ch01-intro,ch02-foundation-models,ch03-evaluation-methodology,ch04-evaluate-ai-systems,ch05-prompt-engineering,ch06-rag-agents,ch07-finetuning,ch08-dataset-engineering,ch09-inference-optimization,ch10-architecture-feedback}.md`
