---
title: "Chapter 1 — Prompt Chaining (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, prompt-chaining, pipeline-pattern, sequential-decomposition, structured-output, context-engineering]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 1 of [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] establishes **[[PromptChaining|prompt chaining]]** (also called the **Pipeline pattern**) as the foundational agentic design pattern: a divide-and-conquer strategy that decomposes a complex task into a sequence of smaller sub-problems, where each LLM call's output is fed as input to the next. The chapter argues this [[SequentialDecomposition|sequential decomposition]] beats a single monolithic prompt on reliability, and shows that the data passed between steps should use a structured format (JSON/XML) — what the chapter calls the [[ContextHandoff|role of structured output]]. It closes with a [[LangChain]]/[[LangGraph]] LCEL hands-on example and a section on [[ContextEngineering|Context Engineering]]. (Agentic Design Patterns, PDF pp 23–35.)

## Key Claims
- Prompt chaining ("Pipeline pattern") applies a **divide-and-conquer** strategy: break the original problem into a sequence of smaller sub-problems, each addressed by a dedicated prompt, with each output fed as input to the next.
- A single complex prompt for a multifaceted task is unreliable; the chapter names the failure modes: **instruction neglect**, **contextual drift**, **error propagation**, **context-window pressure**, and **hallucination from cognitive load**.
- **Sequential decomposition** improves reliability and control by making each step simpler and less ambiguous, reducing the model's cognitive load; each step can be assigned a distinct role (e.g., "Market Analyst," "Trade Analyst," "Expert Documentation Writer").
- **The role of structured output**: chain reliability depends on the integrity of data passed between steps; specifying a structured format (JSON or XML) for inter-step hand-offs is crucial because ambiguous/poorly formatted output causes the next prompt to fail.
- Prompt chaining enables integration of **external tools, APIs, and databases** between steps, and supports inserting **deterministic logic / conditional branching** between model calls (managed by an underlying execution framework).
- Frameworks like [[LangChain]]/[[LangGraph]], [[CrewAI|Crew AI]], and the [[GoogleADK|Google Agent Development Kit (ADK)]] provide structured environments to define, manage, and execute these multi-step sequences; LangChain handles linear sequences while LangGraph extends to **stateful, cyclical** computations.
- **[[ContextEngineering|Context Engineering]]** is the systematic discipline of building the complete informational environment (system prompt, retrieved docs/[[RAG]], tool outputs, [[StateManagement|state/history]], [[MemoryManagement|memory]], [[StructuredOutputs|structured outputs]]) delivered to a model before generation — an evolution beyond prompt engineering. Output quality depends more on context richness than model architecture.
- **Rule of thumb**: use prompt chaining when a task is too complex for a single prompt, involves multiple distinct processing stages, requires tool interaction between steps, or when building agents that need multi-step reasoning and state.

## Key Quotes
> "Prompt chaining, sometimes referred to as Pipeline pattern, represents a powerful paradigm for handling intricate tasks when leveraging large language models (LLMs). Rather than expecting an LLM to solve a complex problem in a single, monolithic step, prompt chaining advocates for a divide-and-conquer strategy." — Pattern Overview, p 23

> "The output of one step acting as the input for the next is crucial. This passing of information establishes a dependency chain, hence the name, where the context and results of previous operations guide the subsequent processing." — p 23

> "The reliability of a prompt chain is highly dependent on the integrity of the data passed between steps. If the output of one prompt is ambiguous or poorly formatted, the subsequent prompt may fail due to faulty input. To mitigate this, specifying a structured output format, such as JSON or XML, is crucial." — The Role of Structured Output, p 24

> "Context Engineering ... is the systematic discipline of designing, constructing, and delivering a complete informational environment to an AI model prior to token generation. This methodology asserts that the quality of a model's output is less dependent on the model's architecture itself and more on the richness of the context provided." — Context Engineering and Prompt Engineering, p 31

## Connections
- [[PromptChaining]] — the chapter's named pattern (primary concept; augmented with this book's framing).
- [[AgenticDesignPatterns]] — book hub; this is Chapter 1 of the 21 patterns.
- [[AntonioGulli]] — author.
- [[SequentialDecomposition]] — the divide-and-conquer mechanic the chapter formalizes.
- [[ContextHandoff]] — the structured-output passing between chain steps.
- [[ContextEngineering]] — the chapter's closing discipline (Fig. 1 Venn diagram).
- [[StructuredOutputs]] — JSON/XML inter-step formatting.
- [[LangChain]] / [[LangGraph]] — frameworks in the hands-on LCEL example.
- [[CrewAI]] / [[GoogleADK]] — additional named frameworks.
- [[GoogleCloudVertexAI]] — Vertex AI prompt optimizer cited for automated context-engineering feedback loops.
- [[PromptEngineering]] — the narrower discipline Context Engineering subsumes.
- [[Routing]] / [[Parallelization]] / [[ToolUse]] — adjacent patterns the chapter forward-references (e.g., parallel data gathering + chained synthesis).

## Contradictions
- vs [[PromptChaining]]'s existing *Hands-On LLMs* Ch 6/7 framing — none; complementary. Gulli adds the explicit "Pipeline pattern" alias, the single-prompt failure-mode taxonomy, the role-assignment idea, and the structured-output hand-off requirement, which reinforce rather than contradict the prior sources. None found.
