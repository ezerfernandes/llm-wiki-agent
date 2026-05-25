---
title: "LLMOps"
type: concept
tags: [llmops, mlops, llm-engineering, monitoring, cicd]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch10-inference-pipeline-deployment, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## Definition
**LLMOps** is the operational discipline of building, deploying, and maintaining systems that use Large Language Models in production. It inherits the six core principles of [[MLOps]] (automation, versioning, experiment tracking, testing, monitoring, reproducibility) and adds LLM-specific concerns: prompt monitoring with full traces, input/output guardrails, human-feedback loops ([[rlhf]] / [[DirectPreferenceOptimization|DPO]]), per-token latency metrics, and the recognition that most teams fine-tune rather than train foundation models from scratch.

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] enumerates LLMOps requirements up front — dataset and model versioning, lineage, reusability, experiment tracking, CT/CI/CD, prompt and system monitoring — and treats them as first-class architectural inputs rather than afterthoughts. [[leh-ch11-mlops-and-llmops]] is the chapter-length deep dive: the authors define the explicit hierarchy **DevOps → MLOps → LLMOps**, arguing each layer adds first-class citizens (DevOps owns code; MLOps adds data + model; LLMOps adds prompts). The chapter quantifies why LLMOps matters operationally — the ~$100M cost of training GPT-4 means almost no team trains foundation models, so LLMOps work concentrates on fine-tuning, prompt engineering, and [[rag|RAG]]. [[leh-ch10-inference-pipeline-deployment]] grounds the discussion in deployment specifics: [[Autoscaling]], [[MicroservicesArchitecture]], [[InferenceComponent|inference components]], and [[TargetTrackingScaling]] policies are all LLMOps-side concerns.

## Key details
- LLMOps adds five distinct latency metrics (TTFT, TBT, TPS, TPOT, total) because LLMs stream tokens — a coarse "request time" metric is misleading.
- LLMOps-specific risks: [[promptinjection|prompt injection]], [[Jailbreak|jailbreak]], sensitive-data exfiltration, toxic output, hallucinated answers — addressed by input/output [[Guardrail|guardrails]] ([[GuardrailsAI]], [[NeMoGuardrails]], Galileo Protect, OpenAI Moderation).
- [[PromptMonitoring]] (e.g., via [[Opik]], [[Langfuse]], [[WeightsAndBiases]]) logs the full trace — user input, prompt template, input variables, retrieved context, generated answer, tokens, latency — because chained prompts cannot be debugged from coarse logs.
- LLMOps inherits [[ContinuousTraining]] from MLOps but the most common "retraining" is a fine-tune of an existing foundation model, not a from-scratch run.
- LLMOps practitioners typically need to manage a [[FeatureStore]], [[ModelRegistry]], experiment tracker, and orchestrator simultaneously — most platforms unify several of these.

## Connections
- [[MLOps]] — the parent discipline LLMOps extends.
- [[CICD]] / [[ContinuousTraining]] — automation pillars LLMOps inherits.
- [[PromptMonitoring]] — the distinctive LLMOps practice.
- [[Guardrail]] — input/output safety mechanisms specific to LLM serving.
- [[rlhf]] / [[DirectPreferenceOptimization]] — the algorithms behind human-feedback loops.
- [[FTIArchitecture]] — the architectural backbone that makes LLMOps tractable.
- [[Hallucination]] — primary risk LLMOps must surface and mitigate.
- [[CometML]] / [[Opik]] / [[Langfuse]] / [[MLflow]] — vendor stack.
- [[ChipHuyen]] — author of an LLMOps-platform essay heavily cited in the chapter.
