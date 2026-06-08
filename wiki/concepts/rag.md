---
title: "RAG"
type: concept
tags: [concept, retrieval, generation, dspy]
sources: [2604.27707-agentic-memory-is-a-memo, 2408.08849-ecg-chat, dspy-custom-module, dspy-rag-tutorial, ai-engineering-ch01-intro, ai-engineering-ch06-rag-agents, ai-engineering-ch07-finetuning, hands-on-llm-ch08-semantic-search-and-rag, agentic-design-patterns-ch14-rag, agentic-design-patterns-appendix-a-prompting]
last_updated: 2026-06-07
---

# RAG

Retrieval-Augmented Generation (Lewis et al., 2021). Originally framed as augmenting parametric memory with retrieval; Xu et al. point out the field has progressively replaced parametric updates with expanded non-parametric stores, inverting the original vision.

## Canonical DSPy receipts

The wiki has two end-to-end DSPy RAG receipts at increasing complexity:

| Tutorial | Retriever | Top-k | Optimization | Benchmark | Result |
|---|---|---|---|---|---|
| [[dspy-custom-module]] | [[ColBERTv2|`dspy.ColBERTv2`]] Wikipedia 2017 abstracts | k=1 | none (worked code listing) | none (illustrative) | — |
| [[dspy-rag-tutorial]] | [[openai|OpenAI]] `text-embedding-3-small` + 28K-doc local corpus (6K-char truncation) | k=5 | [[MIPROv2|`dspy.MIPROv2`]] `auto="medium"` (~$1.50) | [[RAGQAArenaTech]] (1K QA pairs) | 42% → 55.5% → **61.1%** [[SemanticF1]] |

The [[dspy-custom-module|Custom Module tutorial]] establishes the `class RAG(dspy.Module)` shape; the [[dspy-rag-tutorial|RAG tutorial]] extends it with embedding retrieval, a measurable benchmark, and end-to-end optimization. Together they cover the simplest → measurable progression for DSPy RAG.

The [[dspy-custom-module|Custom Module tutorial]] three-stage program: `dspy.Predict(QueryGenerator)` rewrites the question into a retrieval query, `dspy.ColBERTv2(...)` fetches the top-`k=1` Wikipedia passage from the canonical public endpoint `http://20.102.90.50:2017/wiki17_abstracts`, and [[chainofthought|`dspy.ChainOfThought("question,context->answer")`]] synthesizes the final answer. The retrieval step is a **plain Python function**, not a sub-module — so [[DSPyOptimizers|optimizers]] do not see retrieval as a tunable parameter (endpoint, ranker, and `k` are fixed inputs).

```python
class RAG(dspy.Module):
    def __init__(self):
        self.query_generator = dspy.Predict(QueryGenerator)
        self.answer_generator = dspy.ChainOfThought("question,context->answer")

    def forward(self, question, **kwargs):
        query = self.query_generator(question=question).query
        context = search_wikipedia(query)[0]
        return self.answer_generator(question=question, context=context).answer
```

## Graph variant — [[GraphRAG]]

[[GraphRAG]] (Edge et al., Microsoft 2024) replaces flat chunk retrieval with **graph-structured retrieval over community-detected document subgraphs** — used by [[2408.08849-ecg-chat|ECG-Chat]] over seven cardiology textbooks to mitigate hallucination in clinical report generation. The companion module is [[DSPy]] for automated prompt tuning; together they lift [[RAGAS]] Faithfulness from 39.87 to 82.12 on ECG-ExpertQA.

## Connections
- [[ColBERTv2]] — late-interaction retriever; the [[DSPy]] ecosystem's default Wikipedia retriever via `dspy.ColBERTv2(url=...)`.
- [[dspy-custom-module]] — canonical worked DSPy RAG receipt; first wiki-corpus end-to-end RAG inside a `dspy.Module` subclass.
- [[dspy-rag-tutorial]] — extends the custom-module receipt to embedding retrieval ([[openai|OpenAI]] `text-embedding-3-small`, k=5) + [[MIPROv2|MIPROv2]] optimization on [[RAGQAArenaTech]]; 42→55.5→61.1% [[SemanticF1]].
- [[SemanticF1]] — the reference-based [[llmasjudge|LLM-as-judge]] metric most commonly used to score RAG outputs in DSPy.
- [[RAGQAArenaTech]] — the canonical small-scale RAG benchmark in the wiki.
- [[MIPROv2]] — the optimizer that lifts a single-hop CoT-based RAG by ~6 points for ~$1.50.
- [[GraphRAG]] — the knowledge-graph variant.
- [[RAGAS]] — reference-free evaluation framework for RAG systems.
- [[2408.08849-ecg-chat]] — the wiki's first clinical-specialty deployed-RAG instance.

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] in *AI Engineering* Ch 1 introduces RAG as **one of three core [[ModelAdaptation|model adaptation]] techniques** in the [[PromptBasedAdaptation|prompt-based]] family — distinct from [[FineTuning|finetuning]] in that RAG doesn't update model weights:

> *"You can connect the model to a database of customer reviews that the model can leverage to generate better descriptions. Using a database to supplement the instructions is called retrieval-augmented generation (RAG)."* — Ch 1, worked product-description example

Ch 1's framing is intentionally lightweight — RAG is just *"supplementing instructions with a database"* — because Chapter 6 of the book is the deep dive (RAG + Agents). The Ch 1 contribution is positional: RAG sits between [[PromptEngineering|prompt engineering]] (no external data) and [[FineTuning|finetuning]] (weights modified) on the adaptation-complexity spectrum.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

Ch 6 is *AI Engineering*'s **RAG deep dive**. Huyen's central reframe: RAG is the foundation-model-era analogue of **feature engineering** — *"context construction for foundation models is equivalent to feature engineering for classical ML models."* The RAG system decomposes into a **retriever** (with [[TermBasedRetrieval|term-based]] / [[EmbeddingBasedRetrieval|embedding-based]] / [[HybridSearch|hybrid]] variants) and a **generator**.

**Why long context doesn't kill RAG** — two reasons Huyen names: (1) application data grows faster than any fixed context limit ([[ParkinsonsContextLaw|Parkinson's Law for context]]); (2) long contexts have efficiency penalties — *"the longer the context, the more likely the model is to focus on the wrong part of the context."* [[anthropic|Anthropic]]'s 2024 *"under 200K tokens, just use the full context"* recommendation is quoted approvingly as the lower-bound threshold below which RAG is unnecessary.

**Production retrieval optimization** — four tactics: [[ChunkingStrategy]], [[ReRanking]], [[QueryRewriting]], [[ContextualRetrieval]] ([[anthropic|Anthropic]] 2024 LM-generated chunk context).

**Retrieval evaluation** — Ch 6 names [[ContextPrecision]] / [[ContextRecall]] as the two-axis basic metrics, [[NDCG]] / [[MAP]] / [[MRR]] when ranking matters, [[MTEB]] for embeddings, and [[BEIRBenchmark|BEIR]] for retrieval-system benchmarking.

**RAG beyond text** — [[MultimodalRAG]] (via [[CLIP]]-style joint embeddings) and [[RAGOverTabularData]] (via [[TextToSQL]] + SQL execution).

**Position relative to agents** — Ch 6 ends with Huyen's load-bearing observation that *"the RAG pattern can be seen as a special case of agent where the retriever is a tool the model can use."* This is the structural reason RAG and agents share a chapter.

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

Ch 7's most quoted line — and the **canonical decision rule for choosing between RAG and finetuning**:

> "Finetuning is for form, and RAG is for facts."

Specifically:
- [[InformationBasedFailure|Information-based failures]] (factually wrong / outdated outputs, missing private knowledge) → use **RAG**.
- [[BehaviorBasedFailure|Behavior-based failures]] (wrong format, wrong style, domain-specific syntax) → use **[[FineTuning|finetuning]]**.

### Empirical evidence: [[Ovadia2024FineTuningOrRetrieval|Ovadia et al. (2024)]]

Ch 7 leans heavily on this paper for the RAG-wins-on-current-events claim. Their finding across Mistral-7B, Llama-2-7B, Orca-2-7B on a current-events QA benchmark:

| Setup | Mistral-7B | Llama-2-7B | Orca-2-7B |
|---|---|---|---|
| Base | 0.481 | 0.353 | 0.456 |
| Base + RAG | **0.875** | 0.585 | **0.876** |
| Finetuned alone | 0.504 / 0.392 | 0.219 / 0.588 | 0.511 / 0.566 |
| Finetuned + RAG | 0.810 / 0.830 | 0.326 / 0.520 | 0.820 / 0.826 |

The base + RAG row is the winner across all three models — **finetuning often hurts when added on top of RAG** for information-heavy tasks.

### When to combine

Ch 7's recommended order: **start with RAG, then add finetuning if behavior-based failures remain**. RAG is typically easier (no training-data curation, no model hosting). Even within RAG, start with [[BM25]] before jumping to vector databases.

### The 43% / 57% caveat

> "In the same experiment, Ovadia et al. (2024) showed that incorporating RAG on top of a finetuned model can boost its performance on the MMLU benchmark 43% of the time. ... using RAG with finetuned models doesn't improve the performance 57% of the time, compared to using RAG alone."

This is the chapter's clearest signal that **finetuning isn't free** — it has a measurable downside risk even when combined with RAG.

## From [[agentic-design-patterns-ch14-rag|Agentic Design Patterns (Gulli) Ch 14]]

[[AntonioGulli|Gulli's]] [[AgenticDesignPatterns|*Agentic Design Patterns*]] makes RAG the **14th of 21 agentic design patterns** — the agent-centric framing rather than the engineering deep-dive. Its load-bearing sentence: RAG *"transforms the LLM from a closed-book reasoner into an open-book one,"* and for agents specifically *"allows them to ground their actions and responses in real-time, verifiable data … transforming agents from simple conversationalists into effective, data-driven tools capable of executing meaningful work."*

The chapter's mechanics are a concise, beginner-pitched walk consistent with [[ai-engineering-ch06-rag-agents|Huyen Ch 6]] and [[hands-on-llm-ch08-semantic-search-and-rag|Hands-On LLMs Ch 8]]: query → **[[SemanticSearch|semantic search]]** (not keyword match) over an external base → pull relevant **[[Chunking|chunks]]** → **augment** the prompt → send to LLM. Foundations: [[Embedding|embeddings]] (the "cat (2,3) / kitten (2.1,3.1) / car (8,1)" toy example), text vs [[SemanticSimilarity|semantic similarity/distance]], chunking, [[VectorDatabase|vector databases]], and retrieval via vector search / [[BM25]] / [[HybridSearch|hybrid]]. It names the vendor landscape ([[Pinecone]], [[Weaviate]], [[ChromaDB|Chroma]], [[Milvus]], [[Qdrant]]; [[RedisVectorSearch|Redis]], [[Elasticsearch]], [[PostgreSQL|pgvector]]), the ANN index [[HNSW]], and the core libraries [[FAISS]] (Meta AI) and [[ScaNN]] (Google Research). RAG's *"vital advantage"* is **[[CitationGeneration|citations]]** that pinpoint exact sources; its benefits include [[Hallucination|hallucination]] reduction via [[GroundedGeneration|grounding]]; its challenges are cross-chunk/cross-document fragmentation, contradictory-source synthesis, pre-processing burden + periodic reconciliation, and added latency/cost/token usage.

**Two advanced variants the chapter introduces:**

- **[[GraphRAG]]** — retrieval over a **[[KnowledgeGraph|knowledge graph]]** (nodes/edges) instead of a flat vector DB, navigating explicit entity relationships to synthesize answers fragmented across documents. Gulli's distinctive use cases: complex financial analysis, connecting companies to market events, and gene–disease relationship discovery. *"It excels where deep, interconnected insights are more critical than the speed and simplicity of standard RAG."*
- **[[AgenticRAG]]** — a reasoning agent as **critical gatekeeper and refiner** of knowledge (vs Naive RAG's fixed query-vectors→chunks→model pipeline; Agentic RAG *"picks tools to call"*). Four scenarios: (1) reflection & source validation (discard the stale 2020 blog post for the authoritative 2025 policy doc); (2) reconcile knowledge conflicts (€65K finalized report over €50K initial proposal); (3) multi-step reasoning (decompose a feature+pricing comparison into sub-queries); (4) identify knowledge gaps and fire an external [[ToolUse|tool]] (live web-search API for fresh info).

**Hands-on (three examples):** [[GoogleADK|Google ADK]] with the `google_search` grounding tool; ADK's `VertexAiRagMemoryService` over a [[GoogleCloudVertexAI|Vertex AI]] **RAG Corpus** (`SIMILARITY_TOP_K=5`, `VECTOR_DISTANCE_THRESHOLD=0.7`) — the [[MemoryManagement|long-term-memory]] tie-in; and a full [[LangChain]]/[[langgraph|LangGraph]] pipeline (`CharacterTextSplitter` chunking → [[openai|OpenAI]] `OpenAIEmbeddings` → [[Weaviate]] vectorstore → a two-node `StateGraph`: `retrieve_documents_node` → `generate_response_node`, `gpt-3.5-turbo` generator). Gulli grounds the chapter in [[Lewis2020RAG|Lewis et al. 2020]] (arxiv 2005.11401) — the same foundational citation the wiki's other RAG sources use.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 is **the wiki's third book-chapter RAG treatment** — the pedagogical-introduction-with-runnable-code complement to [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]'s engineering-discipline framing and [[leh-ch04-rag-feature-pipeline|LEH Ch 4]]'s production-pipeline framing.

**The three-category retrieval taxonomy** that organizes Ch 8: **[[DenseRetrieval|dense retrieval]]** (embed query + documents, find nearest neighbors), **[[ReRanking|reranking]]** (rescore an existing shortlist with a stronger model), and **RAG** (text generation grounded on retrieved documents — with citations). Each is **architecturally distinct but composable** — you can run dense retrieval without reranking, reranking without RAG, or chain all three.

**The historical anchor**: *"The leading method the industry turned to remedy this behavior is RAG, described in the paper 'Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks' (2020)."* The canonical citation Ch 8 uses is **[[PatrickLewis|Patrick Lewis]] et al. 2020**, NeurIPS 33: 9459–9474 (see [[Lewis2020RAG]]).

**The RAG-vs-generative-search distinction**: *"Generative search is a subset of a broader type of category of systems better called RAG systems."* Generative search is the **product category** (chat-style search engines: [[Perplexity]], Microsoft Bing AI, [[gemini|Gemini]]); RAG is the **technique family**. All generative search is RAG; not all RAG is generative search.

### Canonical Cohere-API receipt (managed RAG)

Ch 8's worked managed-RAG pipeline on the 15-sentence *Interstellar* corpus:

```python
# 1. Dense retrieval
embeds = co.embed(texts=texts, input_type="search_document").embeddings  # (15, 4096)
index = faiss.IndexFlatL2(embeds.shape[1])
index.add(np.float32(embeds))
query_embed = co.embed(texts=[query], input_type="search_query").embeddings[0]
distances, ids = index.search(np.float32([query_embed]), k=3)

# 2. (Optional) Rerank
results = co.rerank(query=query, documents=candidates, top_n=3)

# 3. Grounded generation with automatic span citations
response = co.chat(message=query, documents=[{'text': t} for t in top_texts])
# response.citations = [ChatCitation(start=21, end=36, text='worldwide gross', document_ids=['doc_0']), ...]
```

This is the **wiki's first runnable demonstration of span-level [[CitationGeneration|citation generation]]** as a RAG primitive — `co.chat(documents=...)` returns `ChatCitation` objects with byte offsets into the response text + back-pointers to source document IDs.

### Canonical local receipt (LangChain RAG)

Ch 8's local-RAG path:

```python
from langchain import LlamaCpp, PromptTemplate
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

llm = LlamaCpp(model_path="Phi-3-mini-4k-instruct-fp16.gguf", n_gpu_layers=-1, ...)
embedding_model = HuggingFaceEmbeddings(model_name='thenlper/gte-small')  # or BAAI/bge-small-en-v1.5
db = FAISS.from_texts(texts, embedding_model)
rag = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=db.as_retriever(), chain_type_kwargs={"prompt": prompt})
rag.invoke('Income generated')
```

The **wiki's first runnable `RetrievalQA.from_chain_type(chain_type='stuff', ...)` receipt**. The `chain_type='stuff'` parameter is LangChain's name for *"stuff all retrieved docs into a single prompt"* — the simplest of LangChain's retrieval-QA chain types. The local path **loses citation generation** — *"we will lose the ability to do span citations and the smaller local model isn't going to work as well as the larger managed model, but it's useful to demonstrate the flow."*

### Advanced RAG continuum

Ch 8 names a **delegation-increasing continuum** of Advanced-RAG techniques:

| Technique | Concept page | Pattern |
|---|---|---|
| Query rewriting | [[QueryRewriting]] | Penguins/dolphins essay → *"Where do dolphins live"* |
| **Multi-query RAG** | [[MultiQueryRAG]] | Nvidia 2020 vs 2023 → two parallel queries |
| **Multi-hop RAG** | [[MultiHopRAG]] | Largest car manufacturers 2023 → Toyota/VW/Hyundai → three EV-followups |
| **Query routing** | [[QueryRouting]] | HR → Notion, customer → Salesforce |
| **Agentic RAG** | [[AgenticRAG]] | LLM-as-agent with read+write tool symmetry |

**Capability-ceiling caveat**: *"Not all LLMs will have the RAG capabilities mentioned here. At the time of writing, likely only the largest managed models may be able to attempt this behavior. Thankfully, Cohere's Command R+ excels at these tasks and is available as an open-weights model as well."* — same agent-capability-cliff observation as [[hands-on-llm-ch07-advanced-text-generation|Ch 7's]] *"Phi-3-mini is not sufficient"* for ReAct, and consistent with [[ai-engineering-ch06-rag-agents|Huyen Ch 6's]] [[CompoundErrorAccumulation|compound-error-accumulation]] warning.

### RAG evaluation

Ch 8 names the [[NelsonFLiu|Liu]] / Zhang / [[PercyLiang|Liang]] 2023 *"Evaluating verifiability in generative search engines"* four-axis taxonomy: [[Fluency]] / [[PerceivedUtility|Perceived Utility]] / [[CitationRecall|Citation Recall]] / [[CitationPrecision|Citation Precision]]. Plus [[RAGAS|Ragas]] as the [[llmasjudge|LLM-as-a-judge]] automation framework (adding [[Faithfulness]] + [[AnswerRelevance|Answer Relevance]]). See [[RAGEvaluation]] for the full multi-axis surface.
