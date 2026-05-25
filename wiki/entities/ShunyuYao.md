---
title: "Shunyu Yao"
type: entity
tags: [researcher, llm, agent, react, reasoning]
sources: [hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# Shunyu Yao

**Shunyu Yao** is a researcher in LLM agents and reasoning. **First author** of two of the most consequential papers in the LLM-agent literature:

1. **[[react|ReAct]] — *"ReAct: Synergizing Reasoning and Acting in Language Models"*** (Yao et al. 2022, arXiv:2210.03629). The framework that interleaves **reasoning** (free-form thought) with **acting** (tool calls), each action's observation feeding back into the next reasoning step. The structural ancestor of every *"the LM thinks, calls a tool, observes, thinks again"* agent loop in the modern field.

2. **[[TreeOfThoughts|Tree of Thoughts]] — *"Tree of Thoughts: Deliberate Problem Solving with Large Language Models"*** (Yao et al. 2023, arXiv:2305.10601). The reasoning-pattern that extends [[chainofthought|chain-of-thought]] from a single linear path to a **branching tree** with explicit step-level evaluation and pruning.

Together these two papers anchor the wiki's **agent-and-reasoning** vocabulary.

## In Hands-On LLMs Ch 7

[[hands-on-llm-ch07-advanced-text-generation|Ch 7]] cites Yao et al. (2022) as the **driving force of many agent-based systems**:

> *"The driving force of many agent-based systems is the use of a framework called Reasoning and Acting (ReAct). ReAct merges these two concepts and allows reasoning to affect acting and actions to affect reasoning."* — Ch 7

The chapter's [[LangChainAgent|`create_react_agent` + `AgentExecutor`]] worked example is the wiki's **first runnable [[LangChain]]-native ReAct receipt**, operationalizing Yao et al. 2022 in production-shaped Python code.

## In other parts of the wiki

- [[react|ReAct]] — the concept page anchored to Yao et al. 2022.
- [[TreeOfThoughts]] — the concept page anchored to Yao et al. 2023.
- [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]] — covers tree-of-thought via the **single-prompt three-experts-roleplay approximation** (Hulbert 2023) as well as Yao et al. 2023's architectural form.

## Connections

- [[react|ReAct]] — Yao et al. 2022.
- [[TreeOfThoughts]] — Yao et al. 2023.
- [[chainofthought]] — the reasoning-pattern ReAct and ToT both extend.
- [[Agent]] / [[AgenticAI]] / [[LangChainAgent]] — the agent vocabulary ReAct underwrites.
- [[hands-on-llm-ch07-advanced-text-generation]] — Ch 7 cites Yao 2022 directly.
- [[hands-on-llm-ch06-prompt-engineering]] — Ch 6 cites Yao 2023 for ToT.

## From Hands-On LLMs Ch 7

Yao's ReAct framework is the **structural backbone** of Ch 7's Agents section. The chapter does not survey Yao's other work; ReAct is cited as a single-paper foundation for everything the chapter says about agents.
