---
title: "Principle of Least Privilege"
type: concept
tags: [security, agents, agentic-design-patterns, least-privilege, sandboxing, defense, authorization]
sources: [agentic-design-patterns-ch18-guardrails]
last_updated: 2026-06-07
---

# Principle of Least Privilege

The **Principle of Least Privilege (PoLP)** is the security discipline of granting any component — here, an AI agent — the **absolute minimum set of permissions, tools, and data access required to perform its task**, and nothing more. It is a classic software/operating-systems principle ("a subject should be given only the privileges it needs to complete its task") transposed onto agentic systems, where it becomes a core **guardrail** ([[Guardrail|safety pattern]]) and a precondition for trustworthy autonomy.

## Why it matters in agentic systems
As agents gain autonomy and the ability to call [[ToolUse|tools]], invoke APIs, read files, and act on external systems, an over-permissioned agent is a large attack surface and a large liability. [[AntonioGulli|Gulli's]] [[AgenticDesignPatterns|*Agentic Design Patterns*]] ([[agentic-design-patterns-ch18-guardrails|Ch 18, Guardrails/Safety Patterns]]) names PoLP as one of the core principles of "Engineering Reliable Agents":

> "An agent should be granted the absolute minimum set of permissions required to perform its task. An agent designed to summarize public news articles should only have access to a news API, not the ability to read private files or interact with other company systems. This drastically limits the 'blast radius' of potential errors or malicious exploits." — Ch 18

The key concept is **blast radius**: if an agent is compromised (e.g. via a [[Jailbreak|jailbreak]] or [[IndirectPromptInjection|indirect prompt injection]]) or simply malfunctions, least privilege bounds the damage to what that minimal permission set allows. A summarizer that can only read a news API cannot exfiltrate private files or mutate other systems no matter what an adversary convinces it to attempt.

## How it is enforced
- **Tool-use restrictions** — expose only the specific tools an agent needs (a guardrail stage in [[Guardrail|Ch 18's]] taxonomy); restrict or filter the available tool set (cf. [[GoogleADK|ADK]]'s `tool_filter`).
- **Tool-argument validation / sandboxing** — validate calls before execution. Ch 18's ADK example wires a `before_tool_callback` (`validate_tool_params`) that compares a tool's `user_id_param` against the session-state `session_user_id` and **blocks the call** on mismatch — least privilege enforced at the call boundary. See [[ToolUse]].
- **Isolated execution environments** — run agent-generated code in sandboxes ([[LocalSandbox]], [[CodeInterpreter]]) so it cannot touch the host.
- **Network boundaries** — restrict agent activity within secure perimeters (the chapter cites Google Cloud **VPC Service Controls** in the [[GoogleCloudVertexAI|Vertex AI]] example).
- **Scoped credentials / identity** — establish agent and user identity and authorization, and secure API keys so an agent holds only the scopes it needs.

## Connections
- [[Guardrail]] — least privilege is the security/tool-restriction layer of the guardrails safety pattern.
- [[agentic-design-patterns-ch18-guardrails]] — the source chapter ("Engineering Reliable Agents").
- [[ToolUse]] / [[FunctionCalling]] — tool-use restrictions and argument validation are the agentic expression of PoLP.
- [[GoogleADK]] — the `before_tool_callback` (`validate_tool_params`) example; `tool_filter` scoping.
- [[LocalSandbox]] / [[CodeInterpreter]] — isolated code execution that bounds privilege.
- [[Jailbreak]] / [[IndirectPromptInjection]] / [[promptinjection|Prompt Injection]] — the compromise vectors whose blast radius PoLP limits.
- [[HumanInTheLoop]] — high-privilege actions are gated behind human approval rather than granted to the agent.
- [[GoogleCloudVertexAI]] — VPC Service Controls as a network-boundary realization.
- [[AgenticDesignPatterns]] / [[AntonioGulli]] — the book and author.
