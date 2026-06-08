---
title: "Multi-Agent Collaboration"
type: concept
tags: [agentic-design-patterns, agents, multi-agent, collaboration, topology, orchestration, pattern]
sources: [agentic-design-patterns-ch07-multi-agent, agentic-design-patterns-ch15-a2a]
last_updated: 2026-06-07
---

# Multi-Agent Collaboration

**Multi-Agent Collaboration** is the **7th [[AgenticDesignPatterns|agentic design pattern]]** ([[AntonioGulli|Gulli]], Ch 7): structuring a system as a **cooperative ensemble of distinct, specialized agents** instead of one monolithic agent. It is predicated on **[[TaskDecomposition|task decomposition]]** — a high-level objective is broken into discrete sub-problems, each assigned to the agent possessing the tools, data access, or reasoning capability best suited to it (e.g., a Research Agent → Data Analysis Agent → Synthesis Agent for a complex research query).

This page is the **pattern** entry; the broader system class lives at [[multiagentsystems|Multi-Agent Systems]], which positions collaboration at **Level 3** of the [[AgentComplexitySpectrum]].

## Why it matters
The pattern's value is **synergy, not just division of labor**: "the collective performance of the multi-agent system surpasses the potential capabilities of any single agent within the ensemble." The distributed architecture also brings **modularity, scalability, and robustness** — the failure of one agent need not crash the whole system. A monolithic agent is constrained on complex, multi-domain tasks because it may lack the diverse specialized skills or tool access any one part requires.

Critically, efficacy "is not merely due to the division of labor but is **critically dependent on the mechanisms for inter-agent communication**" — a **standardized communication protocol** and a **shared ontology** so agents can exchange data, delegate sub-tasks, and keep the final output coherent. See [[AgentCommunication]] and the dedicated [[InterAgentCommunication|Inter-Agent Communication (A2A)]] pattern (Ch 15), whose [[A2AProtocol|A2A protocol]] is precisely the open, framework-agnostic standard that lets the [[crewai|CrewAI]] / [[langgraph|LangGraph]] / [[GoogleADK|ADK]] crews below interoperate across framework boundaries.

## The three constituent elements
A multi-agent system fundamentally comprises:
1. **Roles & responsibilities** — delineation of what each agent does ([[Persona|agent personas]] / specializations).
2. **Communication channels** — how agents exchange information.
3. **Task flow / interaction protocol** — what directs their collaborative endeavor.

## Forms of collaboration
The chapter enumerates the *behavioral* forms collaboration can take:
- **Sequential Handoffs** — one agent completes a task and passes its output to the next (like the [[Planning|Pipeline]] pattern, but explicitly across *different* agents). See [[AgentHandoff]].
- **Parallel Processing** — multiple agents work on different parts simultaneously; results are later combined. See [[Parallelization]].
- **Debate and Consensus** — agents with varied perspectives and information sources discuss to evaluate options and reach a consensus / more-informed decision.
- **Hierarchical Structures** — a manager agent dynamically delegates to worker agents based on their tool access / plugin capabilities and synthesizes their results (orchestrator-worker).
- **Expert Teams** — domain specialists (e.g., researcher, writer, editor) collaborate to produce a complex output.
- **Critic-Reviewer** — one group produces an initial output (plan, draft, answer); a second group critically assesses it for policy, security, compliance, correctness, quality, and organizational alignment; a reviser finalizes. Particularly effective for code generation, research writing, logic checking, and ethical alignment — increasing robustness and quality and reducing hallucinations/errors. This is the multi-agent generalization of [[Reflection]].

## Interrelationship & communication topologies
A spectrum of communication models, from simplest to fully custom:
1. **Single Agent** — one autonomous agent, no inter-agent communication; limited by its own scope.
2. **Network** — decentralized peer-to-peer; agents interact directly. Resilient (no single point of failure) but burdened by communication overhead and coherence challenges in large unstructured networks.
3. **Supervisor** — a dedicated supervisor agent is the central hub for communication, task allocation, and conflict resolution. Clear lines of authority, but a single point of failure / bottleneck.
4. **Supervisor as a Tool** — the supervisor provides resources, guidance, or analytical support rather than rigid top-down command, leveraging its capabilities without dictating every action.
5. **Hierarchical** — multi-layered supervisors over operational agents; structured scalability and distributed decision-making within defined boundaries.
6. **Custom** — hybrid or novel designs tailored to a problem's specific performance metrics, dynamics, or domain knowledge.

Choosing a topology is a critical design decision driven by task complexity, agent count, desired autonomy, robustness needs, and acceptable communication overhead.

## Framework realizations
- **[[crewai|CrewAI]]** — the chapter's content-creation crew: a `researcher` ("Senior Research Analyst") and a `writer` ("Technical Content Writer"), each an `Agent(role, goal, backstory)`; two `Task`s where the writing task takes `context=[research_task]`; assembled into a `Crew(agents, tasks, process=Process.sequential, llm=ChatGoogleGenerativeAI("gemini-2.0-flash"))` and run via `kickoff()`. A sequential-handoff crew.
- **[[GoogleADK|Google ADK]]** — multiple coordination paradigms:
  - **Hierarchical** — a coordinator `LlmAgent` with `sub_agents=[greeter, task_doer]`; ADK auto-establishes parent-child relationships (`assert greeter.parent_agent == coordinator`) and delegation is driven by the coordinator's `description`/`instruction`.
  - **Custom non-LLM agent** — `TaskExecutor(BaseAgent)` overriding `_run_async_impl` to `yield Event(...)`.
  - **Iterative / loop** — `LoopAgent("StatusPoller", max_iterations=10, sub_agents=[process_step, ConditionChecker()])`; the `ConditionChecker` escalates (`EventActions(escalate=True)`) to stop the loop when session `status == "completed"`.
  - **Sequential** — `SequentialAgent("MyPipeline", sub_agents=[step1, step2])`, passing data through `output_key`/`session.state["data"]`.
  - **Parallel** — `ParallelAgent("data_gatherer", sub_agents=[weather_fetcher, news_fetcher])` running sub-agents concurrently and gathering results in shared state.
  - **Agent-as-a-Tool** — `agent_tool.AgentTool(agent=image_generator_agent, ...)` wraps a sub-agent so a parent (`artist_agent`) can call it like a [[ToolUse|tool]]; "the AgentTool acts as a bridge, allowing one agent to use another agent as a tool."
- **[[LangChain]] / [[langgraph|LangGraph]]** — named peer frameworks for orchestrating such workflows.

## When to use it (rule of thumb)
Use when a task is too complex for a single agent and decomposes into distinct sub-tasks needing specialized skills/tools — ideal for problems benefiting from diverse expertise, parallel processing, or a structured multi-stage workflow (complex research & analysis, software development, creative content generation, financial analysis, customer-support escalation, supply-chain optimization, network analysis & remediation).

## Connections
- [[multiagentsystems|Multi-Agent Systems]] — the broader concept/system class (this page is the *pattern*).
- [[AgenticDesignPatterns]] / [[AntonioGulli]] — book hub and author.
- [[AgentComplexitySpectrum]] — Multi-agent collaboration is Level 3.
- [[AgentCommunication]] / [[InterAgentCommunication]] / [[A2AProtocol]] — the communication dependency (A2A pattern + protocol, Ch 15).
- [[AgentHandoff]] / [[TaskDecomposition]] / [[Planning]] — handoff/decomposition mechanics.
- [[Parallelization]] — the parallel-processing form (ADK `ParallelAgent`).
- [[Reflection]] — the Critic-Reviewer form generalizes reflection across agents.
- [[ToolUse]] — Agent-as-a-Tool reuses the tool abstraction for inter-agent calls.
- [[crewai|CrewAI]] / [[GoogleADK|Google ADK]] / [[LangChain]] / [[langgraph|LangGraph]] — frameworks.
- [[Persona]] — agent roles/personas.
- [[agentic-design-patterns-ch07-multi-agent]] — source.
