---
title: "Context Engineering"
type: concept
tags: [agents, agentic-design-patterns, context, prompt-engineering]
sources: [agentic-design-patterns-00-frontmatter, agentic-design-patterns-ch01-prompt-chaining, agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
---

# Context Engineering

**Context engineering** is the strategic discipline of **selecting, packaging, and managing the most relevant information for each step** of an agent's operation. Defined in [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli) as a core enabling skill of a Level-2 [[AgentComplexitySpectrum|strategic problem-solving]] agent: "To achieve maximum accuracy from an AI, it must be given a short, focused, and powerful context."

## How it works
Because a model's attention is limited, context engineering curates it to prevent cognitive overload. Worked examples from the book:
- **Routing between tools**: to find a coffee shop between two locations, the agent first uses a mapping tool, then engineers that output into a short focused context (e.g., just a list of street names) before feeding it to a local search tool — keeping the second step efficient and accurate.
- **Travel assistant**: engineers context from a verbose flight-confirmation email, selecting only key details (flight numbers, dates, locations) to package for subsequent calendar and weather-API calls.
- **Software engineering**: given a bug report, the agent reads the report and codebase, then engineers these large sources into a potent, focused context to write, test, and submit a correct patch.

## Why it matters
Context engineering is broader than [[PromptEngineering|prompt engineering]] — it manages *all* available sources of information, not just the prompt string. It is the lever for accuracy in tool-using and multi-step agents, and a substrate for self-improvement: an agent that refines its own context-engineering process (asking how a prompt could be improved) creates an automated feedback loop that increases accuracy and efficiency over time. In the book's "metamorphic" future hypothesis, automatic prompt/context engineering is the "Instructional Modification" level at which a multi-agent system continuously tunes the guidance given to each agent.

## Ch 1 definition (Gulli): the informational-environment framing
[[agentic-design-patterns-ch01-prompt-chaining|Chapter 1]] gives a complementary, more formal definition: *"Context Engineering ... is the systematic discipline of designing, constructing, and delivering a complete informational environment to an AI model prior to token generation. This methodology asserts that the quality of a model's output is less dependent on the model's architecture itself and more on the richness of the context provided."* It is framed as a **significant evolution from traditional [[PromptEngineering|prompt engineering]]**, which optimizes only the phrasing of the immediate query.

Ch 1's Fig. 1 draws Context Engineering as the encompassing set, with five overlapping sub-domains inside it:
- **[[PromptEngineering|Prompt Engineering]]** — the immediate-query phrasing (the [[SystemPrompt|system prompt]] that defines operational parameters, e.g., *"You are a technical writer; your tone must be formal and precise."*).
- **[[RAG]]** — retrieved documents fetched from a knowledge base.
- **[[StateManagement|State / History]]** — interaction history.
- **[[MemoryManagement|Memory]]** — persisted memory.
- **[[StructuredOutputs|Structured Outputs]]** — machine-readable outputs (links Context Engineering to the [[ContextHandoff|structured hand-offs]] in prompt chains).

The chapter stresses that context combines **explicit data** (tool outputs, retrieved docs) with **critical implicit data** (user identity, interaction history, environmental state), and that *"even advanced models underperform when provided with a limited or poorly constructed view of the operational environment."*

### Automating context quality: Vertex AI prompt optimizer
Ch 1 notes that specialized tuning systems can automate context improvement at scale — citing **[[GoogleCloudVertexAI|Google's Vertex AI]] prompt optimizer**, which systematically evaluates responses against sample inputs and predefined metrics to refine prompts/system-instructions across models *"without requiring extensive manual rewriting,"* implementing the **feedback loops** required for sophisticated Context Engineering.

## Appendix A's "Contextual Engineering" layers
[[agentic-design-patterns-appendix-a-prompting|Appendix A]] restates context engineering as **dynamically providing background information crucial for tasks and conversations**, contrasting it with *static* [[SystemPrompt|system prompts]]: *"the quality of a model's output depends more on the richness of the provided context than on the model's architecture."* It enumerates the **layers** of context:
- **System prompts** — foundational operational parameters (*"You are a technical writer; your tone must be formal and precise"*).
- **External data** — **retrieved documents** (a knowledge base / [[rag|RAG]]) and **tool outputs** (results from an external API, e.g. a calendar query).
- **Implicit data** — user identity, interaction history, environmental state; incorporating it raises **privacy and governance** concerns, especially in enterprise, healthcare, and finance.

The "engineering" aspect is building robust pipelines to **fetch and transform** this data at runtime and establishing **feedback loops** (e.g. the [[GoogleCloudVertexAI|Vertex AI Prompt Optimizer]]) to continually improve context quality — the discipline that transforms stateless chatbots into situationally-aware systems.

## Connections
- [[PromptEngineering]] — the narrower, prompt-string-focused discipline context engineering subsumes.
- [[agentic-design-patterns-appendix-a-prompting]] — Appendix A's "Contextual Engineering" section (layers + governance).
- [[agentic-design-patterns-ch01-prompt-chaining]] — Ch 1's "informational environment" definition + Fig. 1 Venn diagram.
- [[StructuredOutputs]] / [[ContextHandoff]] — a Fig. 1 sub-domain; structured outputs as engineered context.
- [[RAG]] / [[MemoryManagement]] / [[StateManagement]] / [[SystemPrompt]] — the other Fig. 1 sub-domains.
- [[GoogleCloudVertexAI]] — Vertex AI prompt optimizer for automated context-quality feedback loops.
- [[AgentComplexitySpectrum]] — context engineering is a Level-2 enabling skill.
- [[Planning]] / [[ToolUse]] / [[RAG]] — the multi-step operations context engineering optimizes.
- [[LearningAndAdaptation]] — self-refinement of context-engineering processes.
- [[AgenticAI]] — the systems that apply it.
- [[agentic-design-patterns-00-frontmatter]] — source page.
