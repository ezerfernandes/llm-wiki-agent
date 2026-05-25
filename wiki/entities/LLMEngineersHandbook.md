---
title: "LLM Engineer's Handbook"
type: entity
tags: [book, publication, llm-engineering, mlops]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch02-tooling-and-installation, leh-ch03-data-engineering, leh-ch04-rag-feature-pipeline, leh-ch05-supervised-fine-tuning, leh-ch06-preference-alignment, leh-ch07-evaluating-llms, leh-ch08-inference-optimization, leh-ch09-rag-inference-pipeline, leh-ch10-inference-pipeline-deployment, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
"LLM Engineer's Handbook: Master the Art of Engineering Large Language Models from Concept to Production" is a 2024 book by [[PaulIusztin]], [[MaximeLabonne]], and [[AlexVesa]], published by [[Packt]]. It is an end-to-end, project-driven guide to building, fine-tuning, evaluating, deploying, and operating production LLM systems via a worked "LLM Twin" example.

## In LLM Engineer's Handbook
This is the book itself. The wiki currently has source pages for chapters 1 through 11 — covering [[LLMTwin]] concept and FTI architecture (Ch. 1), tooling (Ch. 2: [[Python]], [[PoetryPython]], [[ZenML]], [[CometML]], [[MongoDB]], [[Qdrant]], [[AmazonSageMaker]]), data engineering (Ch. 3: crawlers, [[ODM]], [[Selenium]]), the RAG feature pipeline (Ch. 4: chunking, embedding, [[VectorDatabase]] indices), supervised fine-tuning (Ch. 5: [[lora]]/[[QLoRA]] with [[Unsloth]]+[[TRL]]), preference alignment (Ch. 6: [[DPO]]), evaluation (Ch. 7: benchmarks + [[RAGAS]]/ARES), inference optimization (Ch. 8: quantization, [[flashattention]], parallelism), RAG inference (Ch. 9: query expansion, self-querying, cross-encoder reranking), deployment (Ch. 10: [[AmazonSageMaker]] + [[FastAPI]] microservices + autoscaling), and full MLOps/LLMOps integration (Ch. 11: CI/CD/CT, [[Opik]] tracing, drift detection).

## Connections
- [[PaulIusztin]] / [[MaximeLabonne]] / [[AlexVesa]] — co-authors.
- [[Packt]] / [[PacktPublishing]] — publisher.
- [[LLMTwin]] — running project across all chapters.
- [[MLOps]] / [[LLMOps]] — the book's organizing disciplines.
- [[FTIArchitecture]] — the architectural backbone.
