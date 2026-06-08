---
title: "Google AgentSpace"
type: entity
tags: [product, google, platform, agents, enterprise, no-code, agentic-design-patterns]
sources: [agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# Google AgentSpace

**AgentSpace** is a [[google|Google]] platform for building an **"agent-driven enterprise"** — integrating AI into daily workflows. Per [[agentic-design-patterns-appendices-bg|*Agentic Design Patterns* Appendix D]] (Gulli), it provides unified AI **search across an organization's entire digital footprint** (documents, emails, databases), powered by [[gemini|Gemini]], and lets users build and deploy specialized AI **agents** — largely through an online, no-code interface. (At the time of writing it appears in the Google Cloud Console as "Agentspace (Preview)".)

## What it does
- **Enterprise knowledge graph** — maps relationships between people, documents, and data so the AI can deliver context-aware, personalized results.
- **Specialized agents** — not mere chatbots; they reason, plan, and execute multi-step actions (e.g. research a topic, compile a cited report, generate an audio summary).
- **Agent Designer** — a no-code interface for creating custom agents without deep technical expertise.
- **Multi-agent collaboration** — agents communicate via the open **Agent2Agent (A2A) Protocol** ([[InterAgentCommunication]]).
- **Security** — role-based access controls and data encryption for sensitive enterprise information.

## How you build an agent (Appendix D UI walkthrough)
1. Access via **AI Applications** in the **Google Cloud Console**; choose the "Agentspace (Preview)" app type (vs. "Custom search (general)").
2. **Connect data services** — Google sources (Calendar, Gmail) and third-party sources (Workday, Jira, Outlook, ServiceNow).
3. **Choose a prompt** from Google's pre-made **prompt gallery** (Analyze Data, Book Time Off, Chat with Documents, Create Jira Ticket, Deep Research, Draft Email, Explain Technical Documentation, Find Information, Generate Code, Generate Image, Generate Marketing Copy, etc.) — or create a custom prompt (name, display name, title, description, prompt type "User query", activation behavior, icon, enabled toggle).
4. **Configure advanced features** — datastores for your own data, Google Cloud Knowledge Graph or a private Knowledge Graph, a web interface to expose your agent, and analytics for usage monitoring.
5. **Chat** via the AgentSpace UI ("Search your data and ask questions").

## Connections
- [[agentic-design-patterns-appendices-bg]] — source (Appendix D).
- [[google]] — vendor.
- [[gemini]] — underlying model.
- [[GoogleCloudVertexAI]] — Google's broader AI platform.
- [[InterAgentCommunication]] — the A2A protocol AgentSpace uses for multi-agent collaboration.
- [[GoogleADK]] — Google's code-first agent framework (AgentSpace is the no-code/online counterpart).
- Hands-on lab: "Build a Gen AI Agent with Agentspace" on Google Cloud Skills Boost.
