---
title: "Reasoning with LM is Planning with World Model (RAP)"
type: concept
tags: [planning, agents, world-model, reasoning]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Reasoning with Language Model is Planning with World Model

**RAP** (Hao et al. 2023, *"Reasoning with Language Model is Planning with World Model"*) is the framework that argues an LLM's internal *world model* — its compressed knowledge of how actions lead to outcomes — can be **plumbed into a planning search**, enabling planning capabilities the LLM cannot exhibit when prompted to emit linear chains of actions.

## Position in the [[ai-engineering-ch06-rag-agents|Ch 6]] planning debate

Huyen records the debate between *"LLMs can plan"* and *"LLMs can't plan"* and credits Hao et al. with the most credible counter to the skeptics:

> *"The paper 'Reasoning with Language Model is Planning with World Model' (Hao et al., 2023) argues that an LLM, by containing so much information about the world, is capable of predicting the outcome of each action. This LLM can incorporate this outcome prediction to generate coherent plans."*

The thesis: planning is **search**, and search needs **outcome prediction** — *"an action takes you from one state to another, and it's necessary to know the outcome state to determine whether to take an action."* LLMs aren't bad at search; they're bad at **forward-only generation of action sequences**, which isn't search. Use the LLM as both the action proposer and the world model, and you can do real search (e.g. Monte Carlo Tree Search) on top.

## Position relative to [[2402.01817-llm-modulo|LLM-Modulo]] / [[SubbaraoKambhampati|Kambhampati]]

The two positions are contradictory on the surface:

- **[[2402.01817-llm-modulo|LLM-Modulo]] / [[SubbaraoKambhampati|Kambhampati]] / [[YannLeCun|LeCun]]**: LLMs cannot plan; need external sound critics.
- **Hao et al. RAP**: LLMs contain world models; can plan via LLM-driven search.

Huyen doesn't adjudicate — *"it's unclear whether it's because we don't know how to use LLMs the right way or because LLMs, fundamentally, can't plan."* Empirically, RAP-style approaches work on some benchmarks where chain-of-thought fails.

## Connections

- [[Planning]] — the parent concept.
- [[worldmodels|WorldModels]] — what RAP relies on.
- [[2402.01817-llm-modulo]] / [[SubbaraoKambhampati]] / [[YannLeCun]] — the skeptic position.
- [[Agent]] — the application surface.
- [[chainofthought|Chain-of-Thought]] — the linear-emission baseline RAP improves over.
- [[InferenceTimeSearch]] — the broader family of search-at-inference techniques.
- [[ai-engineering-ch06-rag-agents]] — primary source.
