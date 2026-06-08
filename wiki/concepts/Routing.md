---
title: "Routing"
type: concept
tags: [agentic-design-patterns, agents, routing, control-flow, conditional-logic, intent-classification]
sources: [agentic-design-patterns-ch02-routing]
last_updated: 2026-06-07
---

# Routing

**Routing** is the agentic design pattern that introduces **conditional logic** into an agent's operational framework: instead of following a fixed execution path, the agent **dynamically evaluates criteria and selects** from a set of possible subsequent actions — specialized functions, tools, or sub-processes. It is the **conditional counterpart to [[PromptChaining|prompt chaining]]**: where chaining executes a deterministic, linear sequence, routing arbitrates between multiple potential branches based on contingent factors (environment state, user input, the outcome of a preceding operation).

Routing is **pattern #2** of the 21 patterns in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]]. Its canonical figure (Fig. 1) shows an LLM acting as a **Router** between a user-facing prompt and a fan-out of specialized agents/outputs.

> *"This capacity for dynamic decision-making, which governs the flow of control to different specialized functions, tools, or sub-processes, is achieved through a mechanism known as routing."* — Ch 2, Routing Pattern Overview

## Why it matters in agentic systems

A purely sequential workflow is **rigid and non-adaptive** — it cannot choose the right tool or sub-process for a specific task. Routing is what lets a system "triage": first analyze an incoming query to determine its **intent or nature**, then direct the flow of control to the most appropriate destination. This transforms an agent *"from a static executor of pre-defined sequences into a dynamic system that can make decisions about the most effective method for accomplishing a task under changing conditions."*

The chapter's worked motivation is a **customer-inquiry agent**: classify the query → route "check order status" to an order-database tool chain, "product information" to a catalog search, "technical support" to a troubleshooting chain or human escalation, and an unclear intent to a clarification sub-agent.

## Where routing happens in the agent cycle

Routing mechanisms can be applied at **multiple junctures**:
- **At the outset** — to classify a primary task (the most common position; cf. the canonical *"Routing → retrieval → generation → scoring"* pipeline order on [[ModelRouter]]).
- **At intermediate points** within a processing chain — to determine the next action.
- **Inside a subroutine** — to select the most appropriate tool from a given set.

## The four implementation mechanisms (Ch 2)

The chapter enumerates four distinct ways the evaluation-and-dispatch mechanism can be built:

| Mechanism | How the decision is made | Trade-offs |
|---|---|---|
| **LLM-based routing** | Prompt the LLM to analyze the input and emit a route identifier (e.g., output only one of `'Order Status'`, `'Product Info'`, `'Technical Support'`, `'Other'`). | Most flexible; handles nuance; costs an LLM inference per decision. |
| **Embedding-based (semantic) routing** | Convert the query into a [[Embedding|vector embedding]], compare against embeddings representing each route/capability, route to the **most [[SemanticSimilarity|similar]]** one. Decision is on *meaning*, not keywords. | Good for semantic intent; depends on embedding quality. Connects to [[RAG]] (Ch 14). |
| **Rule-based routing** | Predefined rules / logic — if-else, switch-cases, keyword/pattern matching on structured input. | Faster and more deterministic than LLM routing, but less flexible for nuanced or novel inputs. |
| **ML model-based routing** | A discriminative model (e.g., a classifier) **fine-tuned on a small labeled corpus** to perform the routing task; the routing logic lives in the model's learned **weights**, not a runtime prompt. | Distinct from LLM-based routing — no generative model at inference. LLMs may pre-generate synthetic training data, but aren't in the real-time decision. Akin to embedding methods but supervised. |

These map onto the existing wiki pages: LLM-based routing is the [[ModelRouter]] / [[IntentClassifier]] story; embedding/semantic routing is structurally [[QueryRouting]] over capability vectors; ML-model routing is the [[Classification|classifier]]-as-router; and the theoretical sample-efficiency of routing to specialists is formalized in [[RoutingBasedAgenticAI]].

## Practical applications

- **Human-computer interaction** — virtual assistants and AI tutors interpret user intent, then invoke a retrieval tool, escalate to a human, or pick the next curriculum module based on performance.
- **Document / data processing pipelines** — incoming emails, support tickets, or API payloads are analyzed by content/metadata/format and dispatched to the right workflow (sales-lead ingestion, JSON-vs-CSV transformation, urgent-issue escalation). Routing here acts as a **classification-and-distribution function**.
- **Multi-tool / multi-agent systems** — routing acts as a **high-level dispatcher**: a research system routes tasks among search/summarize/analyze agents; an AI coding assistant routes by programming language and intent (debug / explain / translate) to the correct specialized tool.

## Frameworks (Ch 2 hands-on)

The chapter demonstrates two architectural approaches to the same pattern:

- **[[LangChain]] + [[LangGraph]]** — the LangChain example uses a `coordinator_router_chain` (`ChatPromptTemplate | llm | StrOutputParser`) that classifies a request into `'booker' / 'info' / 'unclear'`, then a **`RunnableBranch`** routes the original request to the matching handler. [[LangGraph]]'s state-based graph architecture is highlighted as *"particularly well-suited for complex routing scenarios where decisions are contingent upon the accumulated state of the entire system"* — routing maps to **conditional edges / transitions between nodes** in the computational graph.
- **[[GoogleADK|Google ADK]]** — defines a `Coordinator` agent with `sub_agents=[booking_agent, info_agent]`; the presence of `sub_agents` enables LLM-driven **Auto-Flow** delegation. Routing in the ADK paradigm is implemented by defining a discrete set of **tools/capabilities**, with the framework's internal logic matching user intent to the correct handler. See [[ToolUse]].
- [[CrewAI]] is also named (alongside LangChain/LangGraph and ADK) as a framework providing explicit constructs for this conditional logic.

Both examples implement an [[AgentHandoff|agent delegation / handoff]] pattern — a central coordinator delegating to specialized sub-agents based on intent.

## Relation to adjacent patterns

- **[[PromptChaining]]** — routing is the **conditional/branching counterpart** to sequential chaining; Gulli's Ch 1 already forward-references routing as the pattern that adds conditional branching between model calls. A complex agent typically *combines* both: chained synthesis with routed branch selection.
- **[[Parallelization]]** (Ch 3) — fans out independent work concurrently; routing fans out *one* path conditionally.
- **[[AgentHandoff]]** / **[[MultiAgentCollaboration]]** — routing to sub-agents is the entry point to multi-agent delegation; the chapter's code is *"a basic delegation pattern often seen in multi-agent architectures."*

## At a glance (Ch 2)

- **What** — agentic systems face diverse inputs a single linear process can't handle; without a mechanism to choose the right tool/sub-process, the system stays rigid.
- **Why** — routing adds conditional logic so the agent analyzes the query, then dynamically directs control to the best tool/function/sub-agent. The decision can be LLM-prompted, rule-based, or embedding-based.
- **Rule of thumb** — use routing when an agent must decide between multiple distinct workflows, tools, or sub-agents based on input or current state; essential for **triage/classification** (e.g., a support bot distinguishing sales, technical support, and account questions).

## Connections

- [[agentic-design-patterns-ch02-routing]] — primary source (Gulli Ch 2).
- [[AgenticDesignPatterns]] — book hub; routing is pattern #2.
- [[AntonioGulli]] — author.
- [[PromptChaining]] — the sequential pattern routing complements with conditional branching.
- [[Parallelization]] — sibling control-flow pattern (concurrent fan-out).
- [[AgentHandoff]] — delegation to specialized sub-agents, the chapter's code pattern.
- [[ModelRouter]] / [[IntentClassifier]] — the production-architecture instantiations of LLM-based routing.
- [[QueryRouting]] — embedding/source-selection routing in RAG.
- [[Classification]] — the ML-model-based routing mechanism.
- [[RoutingBasedAgenticAI]] — the theory of routing-to-specialists (sample-efficiency bounds).
- [[Embedding]] / [[SemanticSimilarity]] — embedding-based routing primitives.
- [[LangChain]] / [[LangGraph]] / [[GoogleADK]] / [[CrewAI]] — frameworks providing routing constructs.
- [[Agent]] / [[AgenticAI]] / [[ToolUse]] — the broader agent context routing operates within.
