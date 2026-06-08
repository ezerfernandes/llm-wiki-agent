---
title: "LangGraph"
type: entity
tags: [tool, framework, llm, agent, open-source, langchain, agentic-design-patterns]
sources: [leh-ch09-rag-inference-pipeline, agentic-design-patterns-ch01-prompt-chaining, agentic-design-patterns-ch02-routing, agentic-design-patterns-ch03-parallelization, agentic-design-patterns-ch04-reflection, agentic-design-patterns-ch05-tool-use, agentic-design-patterns-ch08-memory-management, agentic-design-patterns-ch14-rag, agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

## What it is
LangGraph is an open-source library from the [[LangChain]] team for building stateful, multi-actor LLM applications as graphs (nodes + edges) — the canonical way to express agent loops, RAG sub-graphs, and human-in-the-loop steps in the LangChain ecosystem.

## In Agentic Design Patterns — Appendix C (frameworks overview)
[[agentic-design-patterns-appendices-bg|Appendix C]] (Gulli) positions LangGraph as the layer built **on top of [[LangChain]]** for advanced agentic systems: the workflow is defined as a **graph of nodes** (functions or LCEL chains) and **edges** (conditional logic). Its main advantage is the ability to create **cycles** — loop, retry, or call tools in a flexible order until a task is complete — backed by an **explicit, persistent state object** passed between and updated by nodes. Recommended uses: multi-agent systems (a supervisor routing to workers), plan-and-execute agents, and human-in-the-loop. The appendix's runnable example builds a `StateGraph` that runs three LLM calls in parallel (joke/story/poem) and an aggregator node. Comparison: LangGraph = *Graph of Nodes / Cyclical / explicit persistent state / complex dynamic stateful agents*, vs. LangChain's linear stateless chains. Choose LangGraph "when you need your application to reason, plan, or operate in a loop."

## In LLM Engineer's Handbook
Ch. 9 ([[leh-ch09-rag-inference-pipeline]]) references LangGraph (`langgraph`) alongside [[LangChain]] when introducing `PromptTemplate` and LCEL `prompt | model` composition: the chapter uses these primitives directly while keeping the rest of the RAG pipeline framework-light, but notes LangGraph as the natural next step if richer state management or agent loops are needed.

## In Agentic Design Patterns
[[agentic-design-patterns-ch01-prompt-chaining|Ch 1]] of [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli) draws the [[LangChain]]/LangGraph division of labor explicitly: *"LangChain provides foundational abstractions for linear sequences, while LangGraph extends these capabilities to support stateful and cyclical computations, which are necessary for implementing more sophisticated agentic behaviors."* So in the book's framing, plain [[PromptChaining|prompt chaining]] is LangChain's territory; LangGraph is what you reach for once the chain needs **state and cycles** (loops, branching, retries).

## In Agentic Design Patterns Ch 2 (Routing)
[[agentic-design-patterns-ch02-routing|Ch 2 (Routing)]] singles LangGraph out for the [[Routing|routing]] pattern: *"With its state-based graph architecture, LangGraph is particularly well-suited for complex routing scenarios where decisions are contingent upon the accumulated state of the entire system."* Routing in LangGraph is expressed as **conditional edges** — the functions or model-based evaluations that *"dictate the transitions between nodes in the computational graph."* This is the explicit-graph alternative to [[GoogleADK|ADK]]'s declarative Auto-Flow delegation; the chapter's LangChain example itself uses a `RunnableBranch` over a router chain's decision, with LangGraph named as the upgrade path once routing depends on system state.

## In Agentic Design Patterns Ch 3 (Parallelization)
[[agentic-design-patterns-ch03-parallelization|Ch 3 (Parallelization)]] applies the same graph-topology lens to the [[Parallelization|parallelization]] pattern: *"Parallel workflows are defined by architecting the graph such that multiple nodes, lacking direct sequential dependencies, can be initiated from a single common node. These parallel pathways execute independently before their results can be aggregated at a subsequent convergence point in the graph."* So LangGraph expresses **parallel branches** structurally (one source node → many independent nodes → an aggregation/convergence node), the graph-native counterpart to [[LangChain]]'s `RunnableParallel` dict construct and [[GoogleADK|ADK]]'s `ParallelAgent`.

## In Agentic Design Patterns Ch 4 (Reflection)
[[agentic-design-patterns-ch04-reflection|Ch 4 (Reflection)]] casts LangGraph as the **stateful substrate for *true iterative* reflection**. The chapter notes that a single generate→critique→refine cycle can be shown with plain [[LangChain]] LCEL, but *"the implementation of a complete, iterative reflection process necessitates mechanisms for state management and cyclical execution. While these are handled natively in graph-based frameworks like LangGraph or through custom procedural code, the fundamental principle of a single reflection cycle can be demonstrated effectively using ... LCEL."* So [[Reflection|reflection]] follows the same LangChain/LangGraph division of labor as the prior patterns: LCEL for one pass, LangGraph once the loop needs **state and cycles** (the [[FeedbackLoop|feedback loop]] back from Critic to Producer).

## In Agentic Design Patterns Ch 5 (Tool Use)
[[agentic-design-patterns-ch05-tool-use|Ch 5 (Tool Use)]] names LangGraph alongside [[LangChain]] and [[GoogleADK|Google ADK]] as frameworks that *"provide robust support for defining tools and integrating them into agent workflows, often leveraging the native function calling capabilities of modern LLMs like those in the [[gemini|Gemini]] or [[openai|OpenAI]] series."* No dedicated LangGraph code example is given (the chapter's runnable tool-calling agent uses LangChain's `create_tool_calling_agent`/`AgentExecutor`); LangGraph is the stateful-graph option once [[ToolUse|tool-use]] loops need persisted state and cycles. See [[ToolUse]].

## In Agentic Design Patterns Ch 8 (Memory Management)
[[agentic-design-patterns-ch08-memory-management|Ch 8 (Memory Management)]] casts LangGraph as the stateful substrate for *both* tiers of the [[MemoryManagement|memory-management]] pattern. **[[ShortTermMemory|Short-term]]** memory is persisted by a **checkpointer** (resumable, thread-scoped). **[[LongTermMemory|Long-term]]** memory is saved as **JSON documents in a store**, *"organized under a custom namespace (like a folder) and a distinct key (like a filename)"* — `store.put(namespace, key, value)`, `store.get(namespace, key)`, and `store.search(namespace, filter=..., query=...)` (vector similarity). The chapter's `InMemoryStore(index={"embed": embed, "dims": 2})` is the testable version (production: a database-backed store). LangGraph's store is the framework's home for all three long-term memory types — [[SemanticMemory|semantic]] facts, [[EpisodicMemory|episodic]] experiences, and **[[ProceduralMemory|procedural]] rules**: the chapter's procedural-memory pseudo-code stores an agent's own instructions in a `BaseStore` and rewrites them via [[Reflection|Reflection]] (`update_instructions` / `call_model` nodes). See [[MemoryManagement]].

## In Agentic Design Patterns Ch 14 (Knowledge Retrieval / RAG)
[[agentic-design-patterns-ch14-rag|Ch 14 (RAG)]] uses LangGraph as the **orchestration layer for a full [[rag|RAG]] pipeline** — finally giving the chapter-long "LangGraph adds state/cycles" framing a concrete RAG receipt. The pipeline defines `class RAGGraphState(TypedDict)` with fields `question` / `documents` / `generation`, then a `StateGraph(RAGGraphState)` with two nodes: `retrieve_documents_node` (queries a [[Weaviate]] retriever built over [[LangChain]] `CharacterTextSplitter` chunks + `OpenAIEmbeddings`) and `generate_response_node` (runs `prompt | llm | StrOutputParser()` over [[openai|OpenAI]] `gpt-3.5-turbo`). Edges wire `set_entry_point("retrieve")`, `add_edge("retrieve", "generate")`, `add_edge("generate", END)`; `app = workflow.compile()` and queries run via `app.stream(inputs)`. This is the wiki's **first LangGraph `StateGraph` RAG receipt** — the graph-orchestrated complement to the framework-light LEH Ch 9 RAG and the LangChain `RetrievalQA` chain. See [[rag]].

## Connections
- [[rag]] / [[agentic-design-patterns-ch14-rag]] — Ch 14's two-node `StateGraph` (retrieve → generate) RAG pipeline over Weaviate + OpenAI.
- [[MemoryManagement]] / [[ShortTermMemory]] / [[LongTermMemory]] — Ch 8: checkpointer (short-term) + namespaced store (long-term).
- [[SemanticMemory]] / [[EpisodicMemory]] / [[ProceduralMemory]] — the long-term-memory types the store holds.
- [[LangChain]] — parent ecosystem.
- [[ToolUse]] / [[FunctionCalling]] — Ch 5's pattern; LangGraph supports tool definition/integration.
- [[Reflection]] — Ch 4's iterative reflection loop (LangGraph as the stateful/cyclical substrate; LCEL for a single cycle).
- [[Parallelization]] — Ch 3's parallel branches via graph topology (fan-out from a common node, converge downstream).
- [[LangSmith]] — sibling observability product from the same team.
- [[LlamaIndex]] — peer framework.
- [[Agent]] — LangGraph's primary use case.
- [[rag]] — LangGraph can orchestrate RAG sub-graphs.
- [[PromptChaining]] — linear chaining is LangChain's job; LangGraph adds state/cycles.
- [[Routing]] — Ch 2's state-contingent routing via conditional edges.
- [[CrewAI]] / [[GoogleADK]] — peer agent frameworks named in *Agentic Design Patterns*.
- [[agentic-design-patterns-ch01-prompt-chaining]] / [[agentic-design-patterns-ch02-routing]] / [[agentic-design-patterns-ch03-parallelization]] / [[agentic-design-patterns-ch04-reflection]] / [[agentic-design-patterns-ch05-tool-use]] / [[agentic-design-patterns-ch08-memory-management]] / [[agentic-design-patterns-ch14-rag]] — sources.
