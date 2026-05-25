---
title: "Context Construction"
type: concept
tags: [prompt-engineering, rag, llm, application-development]
sources: [ai-engineering-ch05-prompt-engineering, ai-engineering-ch06-rag-agents, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Context Construction

**The process of gathering the necessary context for a given query and assembling it into a prompt.** Named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the umbrella over [[rag|RAG]] retrieval, web search, and other data-access tools. The deep dive lives in Ch 6.

> "The process of gathering necessary context for a given query is called context construction. Context construction tools include data retrieval, such as in a RAG pipeline, and web search." — Ch 5

## Why it matters

Two practical reasons from Ch 5:

1. **Better answers.** *"Just as reference texts can help students do better on an exam, sufficient context can help models perform better. If you want the model to answer questions about a paper, including that paper in the context will likely improve the model's responses."*
2. **Hallucination mitigation.** *"Context can also mitigate hallucinations. If the model isn't provided with the necessary information, it'll have to rely on its internal knowledge, which might be unreliable, causing it to hallucinate."*

## Two ways to get context

Either:

- **Pre-attach** — the application code retrieves the relevant context and includes it in the prompt before sending.
- **Tool-mediated** — the model is given tools (retrieval, web search) and decides which to call.

The first is the [[rag|RAG]] pattern. The second is the [[Agent|agent]] pattern. Ch 6 of *AI Engineering* develops both.

## Restricting model knowledge to context

Ch 5 has a sidebar on the harder problem of getting the model to use **only** the supplied context (no internal knowledge):

- Clear instructions help: *"answer using only the provided context."*
- Negative examples help: provide examples of what the model shouldn't answer.
- Quote-supporting requirement: *"instruct the model to specifically quote where in the provided corpus it draws its answer from."*
- But none of these are guaranteed. Even fine-tuning on the corpus leaks pretraining knowledge.

> "The safest method is to train a model exclusively on the permitted corpus of knowledge, though this is often not feasible for most use cases. Additionally, the corpus may be too limited to train a high-quality model." — Ch 5

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[rag|RAG]] — the canonical retrieval-side implementation.
- [[Agent]] — the tool-mediated implementation.
- [[PromptEngineering]] — parent.
- [[Hallucination]] — what context construction defends against.
- [[PromptStructure]] — context is part of the "task" portion of a prompt.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

Ch 6 is the **deep dive** Ch 5 promises. [[ChipHuyen|Huyen]]'s reframe of context construction in Ch 6 is the load-bearing one:

> *"Context construction for foundation models is equivalent to feature engineering for classical ML models. They serve the same purpose: giving the model the necessary information to process an input."*

The two implementations the Ch 5 stub names are developed here:

- **Pre-attached (RAG)** — [[rag|RAG]] retrieves the relevant context and includes it in the prompt before sending. Ch 6 develops [[TermBasedRetrieval]] / [[EmbeddingBasedRetrieval]] / [[HybridSearch]], retrieval optimization ([[ChunkingStrategy]] / [[ReRanking]] / [[QueryRewriting]] / [[ContextualRetrieval]]), and multimodal/tabular extensions ([[MultimodalRAG]] / [[RAGOverTabularData]]).
- **Tool-mediated (Agent)** — the model is given tools that retrieve context on demand. Ch 6 develops [[KnowledgeAugmentation|knowledge-augmentation]] tools (text retrievers, [[WebBrowsingTool|web browsing]], SQL executors) as the agent realization of context construction.

The two are unified by Huyen's closing observation: *"The RAG pattern can be seen as a special case of agent where the retriever is a tool the model can use."*

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 positions context construction as **Step 1 of the production AI-app reference architecture** — the first component added to the bare model API. The Ch 6 *"feature engineering for foundation models"* reframe is reprised verbatim.

### The provider-support landscape

> *"Due to its central role in a system's output quality, context construction is almost universally supported by model API providers. For example, providers like OpenAI, Claude, and Gemini allow users to upload files and allow their models to use tools."* — Ch 10

But provider capabilities differ:

- **Document limits** — provider APIs cap upload counts; specialized RAG solutions are bounded only by your vector DB.
- **Retrieval configuration** — different frameworks differ in retrieval algorithm, chunk size, re-ranking.
- **Tool-use modes** — parallel function execution, long-running jobs, etc. are not uniformly supported.

### Why context construction is Step 1 of the architecture

In Huyen's additive walkthrough, context construction is the **first** component that gets added to a raw model call — *before* guardrails, before the router, before caching. The implication: an LLM app is essentially a context-construction engine wrapped around a model. Everything else (guardrails, router, cache, agent loop) is operational infrastructure around that core.
