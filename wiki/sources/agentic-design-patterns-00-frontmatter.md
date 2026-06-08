---
title: "Agentic Design Patterns — Foreword, Preface & What Makes a System an Agent"
type: source
tags: [agentic-design-patterns, agents, autonomy, agent-levels, future-of-agents]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
The front matter of Antonio Gulli's *Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems* (Google) frames the book's thesis: the raw power of LLMs must be harnessed through reusable **design patterns** to build robust, scalable, reliable agents — the "car" we build around the LLM "engine." It introduces the defining characteristics of agentic systems (autonomy, proactiveness, reactiveness, goal-orientation, tool use, memory, communication), a five-step agentic loop, a four-level spectrum of agent complexity (Level 0–3), and five hypotheses about the future of agents. The book promises 21 dedicated chapters of patterns plus appendices, with runnable code on three frameworks: LangChain/LangGraph, CrewAI, and Google ADK. (Agentic Design Patterns, PDF pp 7–22; internal printed pp i–iv of Preface and 1–9 of the "What makes an AI system an Agent?" section.)

## Key Claims
- An agentic system is "a computational entity designed to perceive its environment, make informed decisions based on those perceptions and a set of predefined or learned goals, and execute actions to achieve those goals autonomously" — exhibiting flexibility and initiative beyond rigid step-by-step software.
- Agentic systems are characterized by **autonomy** (acting without constant oversight), **proactiveness** (initiating goal-directed actions), **reactiveness** (responding to environmental change), **goal-orientation**, **tool use** (reaching beyond the model via APIs/databases/services), **memory** (retaining information across interactions), and **communication** (with users, systems, or other agents).
- Design patterns are "battle-tested templates or blueprints," not rigid rules; just as software design patterns gave engineering a common language and reusable solutions, agentic patterns do the same for agent development.
- The book extracts **21 key design patterns**; each chapter contains a Pattern Overview, Practical Applications & Use Cases, a Hands-On Code Example, Key Takeaways, and References.
- An AI agent follows a five-step loop: **Get the Mission → Scan the Scene → Think It Through → Take Action → Learn and Get Better** (Fig. 1).
- The AI paradigm evolved from LLM workflows → RAG → individual tool-using AI agents → collaborative Agentic AI (Fig. 2). Agent complexity spans four levels: **Level 0** (core reasoning engine, no tools/memory), **Level 1** (connected problem-solver using external tools/RAG), **Level 2** (strategic problem-solver doing planning + prompt/context engineering + self-improvement), **Level 3** (collaborative multi-agent systems).
- **Context engineering** — strategically selecting, packaging, and managing the most relevant information for each step — is the discipline that maximizes accuracy by curating the model's limited attention.
- Five hypotheses about the future of agents (Fig. 4): generalist agents (and the complementary SLM "Lego" composition path), deep personalization & proactive goal discovery, embodiment & physical-world interaction, an agent-driven economy, and goal-driven metamorphic multi-agent systems that rewrite their own topology.
- Market framing: by end of 2024 AI-agent startups raised >$2B; market valued at $5.2B, projected ~$200B by 2034; 96% of enterprises increasing AI-agent use.

## Key Quotes
> "If the last eighteen months were about the engine — the breathtaking, almost vertical ascent of Large Language Models (LLMs) — the next era will be about the car we build around it." — Marco Argenti (CIO, Goldman Sachs), A Thought Leader's Perspective

> "Just as architectural patterns guide the construction of a building, or design patterns structure software, agentic design patterns provide reusable solutions for the recurring problems you'll face when bringing intelligent agents to life on your chosen canvas." — Preface

> "An AI agent is a system designed to perceive its environment and take actions to achieve a specific goal. It's an evolution from a standard Large Language Model (LLM), enhanced with the abilities to plan, use tools, and interact with its surroundings." — What makes an AI system an Agent?

> "Messy systems plus agents are a recipe for disaster. An AI trained on 'garbage' data doesn't just produce garbage-out; it produces plausible, confident garbage that can poison an entire process." — Marco Argenti

## Connections
- [[AgenticDesignPatterns]] — the book hub this front matter introduces (entity).
- [[AgenticDesignPattern]] — the meta-concept of reusable agent design patterns the book formalizes.
- [[AntonioGulli]] — author; [[google|Google]] — publisher/affiliation; Foreword by Saurabh Tiwary (VP & GM, Cloud AI @ Google); Thought-Leader perspective by Marco Argenti (CIO, Goldman Sachs).
- [[AgenticAI]] — the system class defined here; [[multiagentsystems|Multi-Agent Systems]] — the Level-3 collaborative paradigm.
- [[Autonomy]], [[Proactiveness]], [[Reactiveness]], [[GoalOriented]], [[ToolUse]], [[AgentCommunication]] — the defining characteristics.
- [[ContextEngineering]] — the Level-2 enabling discipline; [[AgentComplexitySpectrum]] — the Level 0–3 model.
- [[ModelContextProtocol|MCP]], [[RetrievalAugmentedGeneration|RAG]], [[Planning]], [[PromptChaining]] — patterns referenced.
- [[LangChain]], [[LangGraph]], [[CrewAI]], [[GoogleADK]] — the frameworks used for code examples.
- [[ReactiveOrProactive]] — Huyen's reactive/proactive product axis, conceptually parallel to Gulli's reactiveness/proactiveness characteristics.

## Contradictions
- vs [[AgenticAI]] on terminology: this wiki's primary [[AgenticAI]] page anchors to Liao et al.'s formal DAG-of-mappings definition $\Psi = (\mathcal{G}, \mathcal{F}, \Lambda)$; Gulli uses "agentic AI" in the practitioner sense (autonomous tool-using, goal-driven systems). These are compatible framings at different altitudes, not a conflict — Gulli's practitioner Level-3 collaborative systems are an informal instance of the DAG formalism.
- Otherwise None found.
