---
title: "Agentic Design Patterns (book)"
type: entity
tags: [book, agents, agentic-design-patterns, google]
sources: [agentic-design-patterns-00-frontmatter, agentic-design-patterns-ch06-planning, agentic-design-patterns-ch12-exception-handling, agentic-design-patterns-ch14-rag, agentic-design-patterns-ch17-reasoning, agentic-design-patterns-ch18-guardrails, agentic-design-patterns-ch19-evaluation, agentic-design-patterns-appendix-a-prompting, agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# Agentic Design Patterns (book)

***Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems*** is a 2025 practitioner book by [[AntonioGulli|Antonio Gulli]] ([[google|Google]]). It is the **book hub** for this wiki's ingest of the work. The book's thesis: the power of LLMs (the "engine") must be harnessed through structured, reusable **design patterns** (the "car built around the engine") to produce robust, scalable, and reliable intelligent agents. Just as software design patterns gave engineering a shared vocabulary and reusable solutions, **agentic design patterns** provide proven, reusable solutions to recurring problems in agent design — see the meta-concept [[AgenticDesignPattern]].

## Framing and metaphor
- The book uses the metaphor of a **"canvas"** — the underlying infrastructure and frameworks (state, communication, tool access, control flow) on which agents are built.
- **Foreword** by Saurabh Tiwary (VP & General Manager, Cloud AI @ Google), tying the patterns to Google's [[GoogleCloudVertexAI|Vertex AI]] platform.
- **A Thought Leader's Perspective: Power and Responsibility** by Marco Argenti (CIO, Goldman Sachs), arguing the next AI era is "about the car we build around" the LLM engine, and stressing clean data, well-defined APIs, and trust.
- Each of the 21 chapters contains: **Pattern Overview**, **Practical Applications & Use Cases**, a **Hands-On Code Example**, **Key Takeaways**, and **References**. Appendices cover advanced prompting, real-world principles, and agentic frameworks.

## Appendices & Conclusion
- **Appendix A** — Advanced prompting ([[agentic-design-patterns-appendix-a-prompting]]).
- **Appendices B, C, D, E, G + Conclusion** — consolidated in [[agentic-design-patterns-appendices-bg]]: Appendix B ([[ComputerUse|computer use]]/[[guiagents|GUI agents]], real-world interaction, [[VibeCoding|vibe coding]]); Appendix C (frameworks overview — [[LangChain]], [[langgraph|LangGraph]], [[GoogleADK|ADK]], [[crewai|CrewAI]], [[autogen|AutoGen]], [[LlamaIndex]], [[Haystack]], [[SemanticKernel|Semantic Kernel]], [[awsstrands|Strands]], MetaGPT, SuperAGI); Appendix D ([[Agentspace|Google AgentSpace]]); Appendix E (CLI agents — [[claudecode|Claude Code]], [[GeminiCLI|Gemini CLI]], [[Aider]], [[copilotcli|GitHub Copilot CLI]], [[terminalbench|Terminal-Bench]]); Appendix G (the [[CodingAgent|Coding Agent]] team pattern); and the book **Conclusion** (capstone synthesis of all 21 patterns — see [[AgenticDesignPattern]]'s four foundational categories). *Note: Appendix F "Under the Hood" is absent from the PDF.*

## Frameworks used for code examples
- [[LangChain]] + its stateful extension [[LangGraph]] — chaining models/components into complex sequences and graphs.
- [[CrewAI]] — structured orchestration of multiple agents, roles, and tasks (collaborative systems).
- [[GoogleADK|Google Agent Developer Kit (ADK)]] — building, evaluating, and deploying agents, integrated with Google's AI infrastructure.

## The 21 patterns
1. [[PromptChaining]]
2. [[Routing]]
3. [[Parallelization]]
4. [[Reflection]]
5. [[ToolUse]]
6. [[Planning]]
7. [[MultiAgentCollaboration]]
8. [[MemoryManagement]]
9. [[LearningAndAdaptation]]
10. [[ModelContextProtocol]]
11. [[GoalSettingAndMonitoring]]
12. [[ExceptionHandlingAndRecovery]]
13. [[HumanInTheLoop]]
14. [[RAG]]
15. [[InterAgentCommunication]]
16. [[ResourceAwareOptimization]]
17. [[ReasoningTechniques]]
18. [[Guardrail|Guardrails]] (Guardrails / Safety Patterns)
19. [[EvaluationAndMonitoring]]
20. [[Prioritization]]
21. [[ExplorationAndDiscovery]]

## Connections
- [[AntonioGulli]] — author.
- [[google|Google]] — author affiliation and publisher context.
- [[AgenticDesignPattern]] — the meta-concept of reusable agent design patterns (distinct from this book entity).
- [[AgenticAI]] — the system class the book teaches how to build.
- [[AgentComplexitySpectrum]] — the Level 0–3 model introduced in the front matter.
- [[agentic-design-patterns-00-frontmatter]] — source page for the front matter unit.
- [[agentic-design-patterns-ch06-planning]] — Chapter 6 (Planning) source page; exemplified by [[DeepResearch|Deep Research]].
- [[agentic-design-patterns-ch12-exception-handling]] — Chapter 12 (Exception Handling and Recovery) source page.
- [[ExceptionHandlingAndRecovery]] — the 12th pattern; making agents fault-tolerant via detect → handle → recover.
- [[agentic-design-patterns-ch17-reasoning]] — Chapter 17 (Reasoning Techniques) source page.
- [[ReasoningTechniques]] — the 17th pattern; advanced reasoning methodologies (CoT, ToT, ReAct, self-correction, CoD/GoD, MASS, Deep Research) unified by spending compute at inference.
- [[agentic-design-patterns-ch18-guardrails]] — Chapter 18 (Guardrails / Safety Patterns) source page.
- [[Guardrail]] — the 18th pattern; multi-layered safety guardrails (input/output validation, content moderation, jailbreak defense, tool sandboxing, human oversight). NB: the basename `[[Guardrails]]` is the Guardrails AI library entity; the safety pattern lives at [[Guardrail]] / [[PrincipleOfLeastPrivilege]].
- [[agentic-design-patterns-ch19-evaluation]] — Chapter 19 (Evaluation and Monitoring) source page.
- [[EvaluationAndMonitoring]] — the 19th pattern; continuous external measurement of agent effectiveness/efficiency/compliance ([[AgentTrajectoryEvaluation|trajectory eval]], [[LLMAsAJudge]], drift/A-B/latency monitoring, the [[AIContract|contractor]] evolution, [[GoogleADK|ADK]] eval tooling).
