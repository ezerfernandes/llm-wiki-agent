---
title: "Agent Communication"
type: concept
tags: [agents, agentic-design-patterns, agent-characteristics, multi-agent]
sources: [agentic-design-patterns-00-frontmatter, agentic-design-patterns-ch07-multi-agent, agentic-design-patterns-ch15-a2a]
last_updated: 2026-06-07
---

# Agent Communication

**Communication** is the agent characteristic of **exchanging information with users, other systems, or other agents** operating on the same or connected "canvases." One of the defining features of an [[AgenticAI|agentic system]] in [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli), and the capability that makes [[MultiAgentCollaboration|multi-agent collaboration]] possible.

## How it works
Communication lets an agent reach beyond its own state to coordinate. In a Level-3 [[multiagentsystems|multi-agent system]], a "Project Manager" agent delegates tasks to specialist agents (Market Research, Product Design, Marketing); "the key to their success would be the seamless communication and information sharing between them, ensuring all individual efforts align to achieve the collective goal." The dedicated pattern for structured agent-to-agent messaging is [[InterAgentCommunication|Inter-Agent Communication]] (Ch 15), whose concrete realization is [[A2AProtocol|Google's A2A protocol]] — an open, HTTP(S)/[[JSONRPC|JSON-RPC 2.0]] standard built around [[AgentCard|Agent Cards]] for capability discovery.

[[agentic-design-patterns-ch07-multi-agent|Chapter 7 (Multi-Agent Collaboration)]] makes this dependency explicit: the efficacy of a multi-agent system "is not merely due to the division of labor but is **critically dependent on the mechanisms for inter-agent communication**," requiring "a standardized communication protocol and a shared ontology" so agents can exchange data, delegate sub-tasks, and keep the final output coherent. Communication channels are one of the three constituent elements of a multi-agent system (alongside roles and a task-flow protocol).

## Why it matters
Communication is the connective tissue of collaborative AI. The book identifies it as one of the present-day bottlenecks: multi-agent effectiveness "is presently constrained by the reasoning limitations of LLMs," and the ability of agents to genuinely learn from one another and improve as a cohesive unit "is still in its early stages." Robust communication standards (e.g., [[ModelContextProtocol|MCP]] for tool/context exchange) are part of building the "interstate system" that lets agents operate safely and at high velocity.

## Connections
- [[InterAgentCommunication]] — the dedicated agent-to-agent messaging pattern (Ch 15).
- [[A2AProtocol]] / [[AgentCard]] — the concrete A2A protocol and its discovery file.
- [[MultiAgentCollaboration]] / [[multiagentsystems|Multi-Agent Systems]] — what communication enables.
- [[ModelContextProtocol]] — a standardized protocol for context/tool exchange.
- [[Autonomy]] / [[Proactiveness]] / [[Reactiveness]] / [[GoalOriented]] — companion characteristics.
- [[AgenticAI]] / [[AgentComplexitySpectrum]] — context.
- [[agentic-design-patterns-00-frontmatter]] — source page.
