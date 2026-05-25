---
title: "LLM Engineer's Handbook — Ch 9: RAG Inference Pipeline"
type: source
tags: [book, llm-engineering, llm-engineers-handbook, rag, inference, retrieval, reranking, query-expansion, self-querying, vector-search]
date: 2024-10-22
source_file: raw/books/llm-engineers-handbook/ch09-rag-inference-pipeline.md
---

## Summary
Chapter 9 of *LLM Engineer's Handbook* (Iusztin, Labonne, Vesa, Packt 2024) builds the **RAG inference pipeline** of the LLM Twin: a retrieval module sitting in front of a fine-tuned LLM hosted on AWS SageMaker. It splits advanced [[rag]] into three optimization stages — **pre-retrieval** (query expansion + self-querying), **retrieval** (filtered vector search over Qdrant), and **post-retrieval** (cross-encoder reranking) — and ties them together in a single `ContextRetriever.search()` orchestrator that runs N expanded queries in parallel, deduplicates, and reranks down to top-K chunks. The chapter walks through concrete Python implementations using LangChain `PromptTemplate`, OpenAI `GPT-4o-mini`, `sentence-transformers` cross-encoders, and a `SingletonMeta` pattern, plus a final five-line `rag()` function that ingests a user query and returns the LLM answer. It closes with proposed extensions: conversation memory with summary compression, a routing classifier to prune which data category collections to query, [[BM25]]-style hybrid search, and Superlinked-based multi-index vector structures.

## Key Claims
- The RAG inference flow can be decomposed into eight steps: user query → query expansion → self-querying → filtered vector search → result aggregation → reranking → prompt construction → LLM call.
- Most of the engineering complexity in a production RAG system lives in the **retrieval module**, not the LLM call — "this is where the magic happens."
- The feature pipeline (which populates the vector DB) and the retrieval module are decoupled processes; the feature pipeline runs on a schedule for feature freshness while retrieval runs on demand per request.
- **Query expansion** (a.k.a. multi-query) uses an LLM to generate xN paraphrased variants of the user query so that the resulting embeddings cover a broader region of the embedding space, reducing the chance of missing semantically relevant but geometrically distant documents.
- **Self-querying** uses an LLM as a metadata extractor (here: extract `author_full_name` / `author_id`) so that critical filter fields are guaranteed to be present rather than relying on them being implicitly encoded in the embedding vector.
- **Filtered vector search** combines vector similarity with metadata filters (e.g., Qdrant `Filter(must=[FieldCondition(key="author_id", match=MatchValue(...))])`) to both improve accuracy and reduce the search space (latency).
- Plain vector search has two failure modes: (1) high cosine similarity for semantically related but contextually wrong documents (the "Java the language vs. Java the island" example) and (2) scalability degradation as the vector space grows.
- **Reranking** uses a neural **cross-encoder** (via `sentence-transformers.CrossEncoder`) to score (query, chunk) pairs jointly, producing more accurate relevance scores than bi-encoder cosine similarity used at retrieval time.
- Reranking compensates for three retrieval failure modes: noise in retrieved context, prompt bloat (and the lost-in-the-middle bias toward first/last tokens), and embedding misalignment with the actual question.
- The N×K → K reranking step is most powerful when combined with query expansion: aggregate N searches of K chunks, deduplicate, then rerank globally and keep the top K.
- LLMs are **biased toward the first and last pieces of context** in a long prompt — relevant content stuck in the middle is often ignored, motivating tight top-K filtering. (See [[lostinthemiddle]].)
- The `Query` domain object inherits from `VectorBaseDocument` (an Object-Vector Mapping / **OVM** abstraction analogous to ORM) so queries can be embedded and stored in Qdrant just like documents.
- An `EmbeddingDispatcher` is reused between feature pipeline and inference pipeline to guarantee the same embedding model is used at ingestion and at query time — a critical invariant for retrieval correctness.
- `CrossEncoderModelSingleton` (using a `SingletonMeta` metaclass) ensures the reranker model is loaded into memory exactly once per process — a standard pattern for expensive model objects.
- Each search per expanded query queries three Qdrant collections (articles, posts, repositories), retrieving ≤ K/3 per category, so a single search returns ≤ K chunks before aggregation.
- Search across N expanded queries is parallelized with a `concurrent.futures.ThreadPoolExecutor`, drastically cutting end-to-end latency.
- A `mock=True` flag on every `RAGStep` (QueryExpansion, SelfQuery, Reranker) lets developers bypass paid LLM API calls during testing and debugging — a reusable cost/dev-loop pattern.
- The final `rag()` function is intentionally five lines — modular composition of retrieval + prompt building + LLM call mirrors what frameworks like [[langgraph|LangChain]], LlamaIndex, and Haystack hide internally.
- Suggested future improvements: (1) conversation memory with rolling summarization, (2) a multi-class router that picks which data categories to query, (3) hybrid search merging dense vector and BM25 sparse retrieval with score normalization, (4) multi-index embeddings over multiple fields (content + platform + recency) via [[Superlinked]].
- Hybrid search merges vector + keyword scores via parallel processing → score normalization → weighted result merging; weights expose a knob for tuning semantic-vs-exact-match emphasis.
- Multi-indexing addresses cases where a single field (content) isn't enough — e.g., platform or publish date may materially shift relevance.
- The chapter explicitly defers LLM deployment to Chapter 10 (AWS SageMaker inference endpoint); `LLMInferenceSagemakerEndpoint` and `InferenceExecutor` are introduced but not detailed here.

## Key Quotes
> "At the retrieval step (and not when calling the LLM), you write most of the RAG inference code. This step is where you have to wrangle your data to ensure that you retrieve the most relevant data points from the vector DB."

> "Using an LLM to generate multiple queries based on your initial question, you create various perspectives that capture different facets of your query. These expanded queries, when embedded, target other areas of the embedding space that are still relevant to your original question."

> "By embedding the query prompt alone, you can never be sure that the tags are sufficiently represented in the embedding vector or have enough signal when computing the distance against other vectors."

> "Language models are usually biased toward the context's first and last pieces. So, if you add a large amount of context, there's a big chance it will miss the essence."

> "As we modularized all the RAG steps into independent classes, we reduced the high-level rag() function to five lines of code (encapsulating all the complexities of the system) similar to what we see in tools such as LangChain, LlamaIndex, or Haystack."

> "The world of LLMs and RAG is experimental, similar to any other AI domain. Thus, when building real-world products, it's important to quickly build an end-to-end solution that works but is not necessarily the best. Then, you can reiterate with various experiments until you completely optimize it for your use case."

## RAG Inference Components

### Retrieval client — `ContextRetriever`
- Orchestrator that wires together `SelfQuery`, `QueryExpansion`, `Reranker`, and the per-category Qdrant search.
- Entry point: `search(query: str, k=3, expand_to_n_queries=3) -> list[EmbeddedChunk]`.
- Concurrency: `concurrent.futures.ThreadPoolExecutor` over the N expanded queries.
- Post-processing: flatten → `list(set(...))` deduplication → rerank → top-K.

### Query optimizer — `QueryExpansion`
- Inherits from `RAGStep` (with `mock` flag).
- Uses `ChatOpenAI(model=settings.OPENAI_MODEL_ID, temperature=0)` (default: `GPT-4o-mini`).
- Prompts the LLM via `QueryExpansionTemplate` to emit `expand_to_n - 1` paraphrased variants separated by a sentinel `#next-question#`.
- Returns `[original_query] + [Query.replace_content(variant) for variant in variants]`.

### Metadata extractor — `SelfQuery`
- Few-shot prompted via `SelfQueryTemplate` to return either the user's name/ID or the literal token `none`.
- On success, splits full name → `first_name`, `last_name`, then `UserDocument.get_or_create(...)` to resolve to a UUID.
- Mutates the `Query` object to set `author_id` and `author_full_name`, which then propagate into the Qdrant filter at search time.

### Filtered vector search — per-category Qdrant searches
- Uses `EmbeddingDispatcher.dispatch(query)` (same dispatcher as ingestion in [[rag]] feature pipeline) → `EmbeddedQuery`.
- For each of three data categories (`EmbeddedPostChunk`, `EmbeddedArticleChunk`, `EmbeddedRepositoryChunk`) calls `.search(query_vector, limit=k//3, query_filter=...)`.
- Filter built as `Filter(must=[FieldCondition(key="author_id", match=MatchValue(value=str(author_id)))])` if author was extracted; else `None`.

### Reranker — `Reranker` + `CrossEncoderModelSingleton`
- Reranker calls the singleton with `(query.content, chunk.content)` tuples → scores, sorts descending, keeps top-K.
- `CrossEncoderModelSingleton(metaclass=SingletonMeta)` wraps `sentence_transformers.cross_encoder.CrossEncoder` on `settings.RAG_MODEL_DEVICE`, `model.eval()` mode.
- The wrapper exists so a future swap (e.g., a hosted reranker API) only requires a new class with the same `__call__(pairs) -> list[float]` interface.

### Prompt builder + response generator — `rag()` + `call_llm_service()`
- Prompt template:
  ```
  You are a content creator. Write what the user asked you to while using the
  provided context as the primary source of information for the content.
  User query: {query}
  Context: {context}
  ```
- `EmbeddedChunk.to_context(documents)` flattens retrieved chunks into the `{context}` slot.
- `call_llm_service(query, context)` instantiates `LLMInferenceSagemakerEndpoint(...)` and runs `InferenceExecutor(llm, query, context).execute()` — actual SageMaker plumbing deferred to Chapter 10.

## Code & Concrete Examples

**RAGStep base interface** (`base.py`):
```python
class RAGStep(ABC):
    def __init__(self, mock: bool = False) -> None:
        self._mock = mock
    @abstractmethod
    def generate(self, query: Query, *args, **kwargs) -> Any: ...

class PromptTemplateFactory(ABC, BaseModel):
    @abstractmethod
    def create_template(self) -> PromptTemplate: ...
```

**Query domain entity** (OVM):
```python
class Query(VectorBaseDocument):
    content: str
    author_id: UUID4 | None = None
    author_full_name: str | None = None
    metadata: dict = Field(default_factory=dict)
    class Config:
        category = DataCategory.QUERIES
```

**Query expansion call** — produces N variants from a single user question, used to widen embedding-space coverage. Example output for "Write an article about the best types of advanced RAG methods":
- "What are the most effective advanced RAG methods, and how can they be applied?"
- "Can you provide an overview of the top advanced retrieval-augmented generation techniques?"

**Self-query call** — extracts `author_id`, `author_full_name` from "I am Paul Iusztin. Write an article about…".

**Qdrant filtered search**:
```python
records = qdrant_connection.search(
    collection_name="articles",
    query_vector=query_embedding,
    limit=3,
    with_payload=True,
    query_filter=Filter(must=[
        FieldCondition(key="author_id", match=MatchValue(value=str("1234")))
    ]),
)
```

**Reranker generate()** — cross-encoder scoring pattern:
```python
query_doc_tuples = [(query.content, chunk.content) for chunk in chunks]
scores = self._model(query_doc_tuples)
scored = sorted(zip(scores, chunks), key=lambda x: x[0], reverse=True)
return [chunk for _, chunk in scored[:keep_top_k]]
```

**The five-line `rag()` function**:
```python
def rag(query: str) -> str:
    retriever = ContextRetriever(mock=False)
    documents = retriever.search(query, k=3)
    context = EmbeddedChunk.to_context(documents)
    answer = call_llm_service(query, context)
    return answer
```

**Superlinked multi-index example** (future-improvement section):
```python
articles_space_content = TextSimilaritySpace(
    text=chunk(article.content, chunk_size=500, chunk_overlap=50),
    model=settings.EMBEDDING_MODEL_ID,
)
articles_space_platform = CategoricalSimilaritySpace(
    category_input=article.platform,
    categories=["medium", "substack", "wordpress"],
    negative_filter=-5.0,
)
article_index = Index([articles_space_content, articles_space_platform],
                      fields=[article.author_id])
```

## Connections
- [[rag]] — Chapter 9 is the canonical advanced-RAG inference reference; defines pre/retrieval/post-retrieval taxonomy used elsewhere.
- [[RAGChatbot]] — chapter explicitly frames LLM Twin as a chatbot and discusses conversation memory extension.
- [[GraphRAG]] — alternative advanced-RAG variant, not used here but adjacent in design space.
- [[RAGAS]] — evaluation framework adjacent to but not used in this chapter.
- [[AmazonSageMaker]] — target deployment surface for the LLM endpoint (`LLMInferenceSagemakerEndpoint`).
- [[Singleton]] — the design pattern used by `CrossEncoderModelSingleton` via `SingletonMeta`.
- [[CosineSimilarity]] — baseline retrieval scoring that reranking is meant to refine.
- [[BM25]]-style keyword retrieval — referenced as the sparse half of proposed hybrid search.
- [[lostinthemiddle]] — explains the first/last-bias claim that motivates aggressive top-K filtering.
- [[Tokenizer]] / [[Tokenization]] — chunk-level retrieval depends on the chunking strategy from Ch 4.
- [[PromptOptimization]] — query expansion and self-querying are LLM-as-prompt-generator patterns adjacent to prompt optimization.
- [[chainofthought]] / few-shot prompting — `SelfQueryTemplate` uses few-shot examples to anchor extraction format.
- [[Agent]] — `RAGStep` + `ContextRetriever` is a lightweight non-agentic pipeline; routing improvement nudges toward agentic behavior.
- [[ConversationHistory]] — the proposed memory improvement directly relates.
- [[FastAPI]] — Chapter 10 will wrap this as a FastAPI business layer.
- [[langgraph]] / LangChain — `PromptTemplate` and `prompt | model` LCEL composition is used directly.
- [[Qdrant]] (entity, may not exist) — concrete vector DB used.
- [[openai]] — `GPT-4o-mini` via `ChatOpenAI` underlies both query expansion and self-querying.
- [[HuggingFace]] — `sentence-transformers` cross-encoder model is from HuggingFace.
- [[Superlinked]] — explicitly proposed for multi-index improvement; not in current pipeline.
- [[LlamaIndex]] / Haystack — namechecked as comparable frameworks.
- [[PaulIusztin]] / [[MaximeLabonne]] / [[AlexVesa]] — co-authors of the book.
- [[Packt]] — publisher.
- [[LLMEngineersHandbook]] — parent book entity.

## Contradictions
- None directly with existing wiki content. The chapter's claim that "LLMs are biased toward first and last context tokens" is consistent with [[lostinthemiddle]]. The architecture pattern (retrieve → rerank → augment → generate) is consistent with the canonical RAG description in [[rag]].
- Mild tension: this chapter argues against heavy LangChain reliance ("we avoid being heavily reliant on LangChain… as we want to implement everything ourselves to understand the engineering behind the scenes") while still using `PromptTemplate` and `prompt | model` LCEL composition — a pragmatic middle position rather than a contradiction.
