---
title: "Role Prompting"
type: concept
tags: [prompt-engineering, prompting, agentic-design-patterns, llm, roleplaying]
sources: [agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
---

# Role Prompting

**Role prompting** assigns a specific **character, persona, or identity to the language model** — instructing it to adopt the knowledge, tone, and communication style associated with that role. Examples: *"Act as a travel guide"*, *"You are an expert data analyst"*. Defining a role provides a framework for the tone, style, and focused expertise of the output, and the desired style within the role can be further specified (e.g. *"a humorous and inspirational style"*). Surveyed in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] [[agentic-design-patterns-appendix-a-prompting|Appendix A]] under "Structuring Prompts."

> *Appendix A example:* "Act as a seasoned travel blogger. Write a short, engaging paragraph about the best hidden gem in Rome."

## Where it lives in the prompt

Role prompting is often used in conjunction with [[SystemPrompt|system prompting]] or [[ContextPrompt|contextual prompting]] — the role assignment most naturally sits in the system prompt, where it shapes the model's behavior throughout the session. It is the prompt-engineering operationalization of giving the model a [[Persona|persona]].

## Role Prompting vs. the Persona Pattern

Appendix A draws a sharp distinction that is easy to conflate:

| Technique | Whose persona is described | Effect |
|---|---|---|
| **Role prompting** | the **model** (*"You are an expert data analyst"*) | shapes the model's expertise, tone, and perspective |
| **Persona Pattern** | the **user / target audience** (*"The audience is a high-school student with no prior knowledge…"*) | shapes language complexity, depth, and the kind of information provided |

Both tailor the response, but role prompting controls the *speaker* while the persona pattern controls the *listener*. See [[Persona]] for the wiki's deeper treatment of model-persona prompting (Huyen Ch 5 / Hands-On LLMs Ch 6).

## Why it matters in agentic systems

In multi-step and multi-agent workflows, role prompting is how a single LLM is specialized per step — e.g. chaining a *"Market Analyst" → "Trade Analyst" → "Expert Documentation Writer"* sequence (see [[PromptChaining]]). It enhances the quality and relevance of each step's output by activating the most appropriate slice of the model's knowledge.

## Connections
- [[agentic-design-patterns-appendix-a-prompting]] — source (Appendix A).
- [[Persona]] — the wiki's deeper model-persona page; role prompting is its prompt-structuring framing.
- [[SystemPrompt]] / [[ContextPrompt]] — where role assignments are placed.
- [[Roleplaying]] / [[RoleLLM]] — related role-based prompting concepts in the wiki.
- [[PromptChaining]] — per-step role assignment in multi-step pipelines.
- [[PromptEngineering]] — parent discipline.
- [[AgenticDesignPatterns]] / [[AntonioGulli]] — book hub and author.
