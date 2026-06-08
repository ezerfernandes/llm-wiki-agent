---
title: "Chapter 7 — Multi-Agent Collaboration (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, multi-agent, collaboration, topology, orchestration]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 7 of [[AntonioGulli|Antonio Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] presents the **Multi-Agent Collaboration** pattern: structuring a system as a cooperative ensemble of distinct, specialized agents rather than one monolithic agent, predicated on **task decomposition** and **inter-agent communication**. It enumerates the *forms* collaboration takes (sequential handoffs, parallel processing, debate & consensus, hierarchical structures, expert teams, critic-reviewer) and a *spectrum* of interrelationship/communication topologies (single agent, network, supervisor, supervisor-as-a-tool, hierarchical, custom). It ships runnable examples in [[crewai|CrewAI]] (a sequential research→writer crew) and [[GoogleADK|Google ADK]] (hierarchical `sub_agents`, `LoopAgent`, `SequentialAgent`, `ParallelAgent`, and `AgentTool` "agent-as-a-tool"). (Agentic Design Patterns, PDF pp 113–131.)

## Key Claims
- A monolithic agent is constrained on complex, multi-domain tasks; the Multi-Agent Collaboration pattern decomposes a high-level objective into discrete sub-problems, each assigned to the agent with the best-suited tools, data access, or reasoning capability.
- Efficacy depends not merely on division of labor but **critically on inter-agent communication** — a standardized communication protocol and a *shared ontology* so agents can exchange data, delegate sub-tasks, and coordinate to keep the final output coherent.
- The distributed architecture yields enhanced **modularity, scalability, and robustness** (single-agent failure need not crash the system) and a **synergistic** result where collective performance surpasses any single agent.
- A multi-agent system fundamentally comprises three things: (1) delineation of agent **roles & responsibilities**, (2) **communication channels**, and (3) a **task flow / interaction protocol** directing collaboration.
- Collaboration forms named: **Sequential Handoffs** (output of one agent → next, like a pipeline but across distinct agents), **Parallel Processing** (agents work simultaneously, results combined), **Debate and Consensus** (varied-perspective agents discuss to reach an informed decision), **Hierarchical Structures** (a manager delegates to workers by tool access and synthesizes results), **Expert Teams** (domain specialists — researcher/writer/editor), and **Critic-Reviewer** (one group produces, a second critically assesses for policy/security/compliance/correctness/quality/alignment, then a reviser finalizes — reduces hallucinations and errors).
- Six interrelationship/communication models form a spectrum from simplest to custom: **Single Agent**, **Network** (decentralized peer-to-peer, resilient but communication-overhead-heavy), **Supervisor** (a central coordinating hub — clear authority but a single point of failure / bottleneck), **Supervisor as a Tool** (supervisor provides resources/guidance rather than top-down command), **Hierarchical** (multi-layered supervisors over operational agents), and **Custom** (hybrid/novel designs).
- Frameworks **CrewAI** and **Google ADK** are engineered to facilitate the pattern by providing structures for specifying agents, tasks, and their interactive procedures.
- The CrewAI hands-on builds a content-creation crew: a `researcher` (role "Senior Research Analyst") and `writer` (role "Technical Content Writer"), each an `Agent` with `role`/`goal`/`backstory`, two `Task`s (the writing task takes `context=[research_task]`), assembled into a `Crew` with `process=Process.sequential` and `llm` = `gemini-2.0-flash`, executed via `kickoff()`.
- The ADK hands-on shows: (a) a **hierarchical** coordinator `LlmAgent` with `sub_agents=[greeter, task_doer]` where ADK auto-establishes parent-child relationships and delegation is driven by the coordinator's `description`/`instruction`; (b) a custom non-LLM agent (`TaskExecutor`) subclassing `BaseAgent` and overriding `_run_async_impl` to `yield Event`s; (c) a `LoopAgent` (`StatusPoller`, `max_iterations=10`) iterating `process_step` + a `ConditionChecker` that escalates (`EventActions(escalate=True)`) when session `status == "completed"`; (d) a `SequentialAgent` pipeline passing data via `output_key`/`session.state`; (e) a `ParallelAgent` (`data_gatherer`) running `weather_fetcher` and `news_fetcher` concurrently; (f) **Agent-as-a-Tool** via `agent_tool.AgentTool`, wrapping a sub-agent so a parent agent can invoke it like a function (an artist agent invents a prompt then calls an ImageGen agent through `AgentTool`).
- Rule of thumb: use the pattern when a task is too complex for one agent and decomposes into distinct sub-tasks needing specialized skills/tools, or benefits from diverse expertise, parallel processing, or a multi-stage structured workflow.

## Key Quotes
> "The efficacy of such a system is not merely due to the division of labor but is critically dependent on the mechanisms for inter-agent communication. This requires a standardized communication protocol and a shared ontology…" — on why collaboration ≠ just splitting work
> "The collaboration allows for a synergistic outcome where the collective performance of the multi-agent system surpasses the potential capabilities of any single agent within the ensemble." — the core value proposition
> "A multi-agent system … fundamentally comprises the delineation of agent roles and responsibilities, the establishment of communication channels through which agents exchange information, and the formulation of a task flow or interaction protocol that directs their collaborative endeavors." — the three constituent elements
> "The AgentTool acts as a bridge, allowing one agent to use another agent as a tool." — describing ADK's agent-as-a-tool paradigm

## Connections
- [[MultiAgentCollaboration]] — the named pattern this chapter defines (Pattern #7).
- [[multiagentsystems|Multi-Agent Systems]] — the broader system class this pattern instantiates (Gulli's Level-3 of the [[AgentComplexitySpectrum]]).
- [[AgenticDesignPatterns]] / [[AntonioGulli]] — book hub and author.
- [[AgentCommunication]] / [[InterAgentCommunication]] — the communication dependency; Ch 15 covers the dedicated agent-to-agent (A2A) pattern.
- [[AgentHandoff]] — sequential handoffs / delegation; Ch 2's coordinator→specialist routing is the entry point to this pattern.
- [[TaskDecomposition]] / [[Planning]] — decomposing the objective into sub-problems per agent.
- [[Parallelization]] — ADK `ParallelAgent`; "parallel processing" collaboration form.
- [[Reflection]] — the Critic-Reviewer form is the multi-agent generalization of reflection.
- [[crewai|CrewAI]] / [[GoogleADK|Google ADK]] / [[LangChain]] / [[langgraph|LangGraph]] — frameworks.
- [[gemini|Gemini]] / [[google|Google]] / [[GoogleCloudVertexAI|Vertex AI]] — models/platform behind the examples.
- [[ToolUse]] — Agent-as-a-Tool (`AgentTool`) reuses the tool-use abstraction for inter-agent calls.

## Contradictions
- None found. Consistent with the [[multiagentsystems]] page and the [[AgenticDesignPatterns]] hub; this chapter is the detailed treatment of the Level-3 collaboration the front matter previews.
