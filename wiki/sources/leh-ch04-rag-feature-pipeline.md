---
title: "LLM Engineer's Handbook — Ch 4: RAG Feature Pipeline"
type: source
tags: [book, llm-engineering, llm-engineers-handbook, rag, chunking, embeddings, vector-database, feature-pipeline, advanced-rag, qdrant, zenml]
date: 2024-10-22
source_file: raw/books/llm-engineers-handbook/ch04-rag-feature-pipeline.md
---

## Summary
Chapter 4 of the *LLM Engineer's Handbook* delivers a comprehensive theoretical and applied treatment of Retrieval-Augmented Generation (RAG), then walks through the design and implementation of LLM Twin's batch RAG feature pipeline. It covers the vanilla RAG framework (ingestion, retrieval, generation modules), the role of embeddings and vector databases (with HNSW, PQ, LSH, and random-projection indexing algorithms), and a full taxonomy of *advanced RAG* optimizations grouped into pre-retrieval (data indexing + query optimization), retrieval (better embeddings + DB filter/search), and post-retrieval (prompt compression + re-ranking with a cross-encoder) stages. The applied half builds an end-to-end ZenML batch pipeline that pulls raw articles, posts, and code repos from MongoDB, cleans/chunks/embeds them with Sentence Transformers, and loads them into a Qdrant vector DB using a custom Object-Vector Mapping (OVM) layer plus Dispatcher + Factory + Strategy + Singleton design patterns. It also introduces Change Data Capture (CDC) as the production-grade alternative to the naive periodic-pull sync between data warehouse and feature store.

## Key Claims
- RAG composes three independent modules: an **ingestion pipeline** (extract/clean/chunk/embed/load to vector DB), a **retrieval pipeline** (embed query, ANN-search vector DB), and a **generation pipeline** (assemble prompt template + retrieved context + user query, call LLM).
- RAG solves two fundamental LLM limitations: hallucinations (it forces the model to answer "solely based on the introduced context" as a single source of truth) and stale/private knowledge (avoids constant fine-tuning costs).
- The query embedding and indexed embeddings MUST be produced by the same model and preprocessing pipeline, or the inference is corrupted — the same principle as the training-serving skew in classic ML.
- Cosine distance (1 minus cosine similarity) is the most popular vector distance for RAG, but Euclidean/Manhattan/dot-product are alternatives; the right choice depends on data and embedding model.
- Embeddings (typically 64–2048 dimensional) outperform one-hot encoding (curse of dimensionality) and feature hashing (collisions, lost semantics) because they condense information into a dense vector while preserving semantic similarity.
- Embeddings can be produced by Word2Vec/GloVe (classical), encoder-only transformers like BERT/RoBERTa (modern), CNNs (images via ResNet-style backbones), or cross-modal models like CLIP (text+image into a shared space); audio is typically embedded via spectrogram-then-image-model.
- Sentence Transformers (and Hugging Face's MTEB leaderboard) are the practical entry points for picking and swapping text-embedding models; `all-MiniLM-L6-v2` and `all-mpnet-base-v2` are the working defaults in the chapter.
- Instructor-style embedding models (e.g., `hkunlp/instructor-base`/`-xl`) let you steer the embedding with a natural-language instruction prefix — a cheaper alternative to fine-tuning the embedder for a domain.
- Vector DBs differ from standalone vector indices (FAISS) by adding CRUD, metadata filtering, scalability, real-time updates, backups, and access control — making them production-grade.
- The four canonical ANN index algorithms covered are HNSW (multi-layer navigable small-world graph), random projection, Product Quantization (PQ, sub-vector quantization), and Locality-Sensitive Hashing (LSH); HNSW is the de-facto default.
- Advanced RAG optimizes at three stages: **pre-retrieval** (data indexing + query optimization), **retrieval** (better embeddings + filter/hybrid search), **post-retrieval** (prompt compression + re-ranking).
- Pre-retrieval data-indexing techniques include sliding-window chunking (overlap to preserve boundary context), enhancing data granularity (cleaning), metadata tagging, multi-indexing, and the *small-to-big* strategy (embed small chunks, store wider context as metadata for the prompt).
- Pre-retrieval query-optimization techniques include query routing (LLM- or embedding-based if/else over natural language), query rewriting (paraphrase, synonym substitution, sub-queries), HyDE (LLM-generated hypothetical answer embedded alongside the query), query expansion, and self-query (LLM extracts structured filters from the unstructured query).
- Retrieval-stage optimizations: fine-tune the embedding model on domain data OR use instructor models; on the DB side use *hybrid search* (vector + keyword, blended via an alpha weight) or *filtered vector search* (vector search constrained by metadata filters pre/post search).
- Post-retrieval optimizations: *prompt compression* (strip redundancy) and *re-ranking* with a cross-encoder (e.g., `cross-encoder/ms-marco-MiniLM-L-4-v2`) that scores (query, chunk) pairs jointly — too expensive for first-stage retrieval, perfect for refining the top-N from a bi-encoder.
- LLM Twin's feature pipeline is a **batch** design (not streaming) because data volume is small (thousands of records), simplicity wins, and a few minutes of staleness is acceptable; the author explicitly recommends starting batch and migrating to streaming only when warranted.
- The five canonical RAG feature-pipeline steps: data extraction → cleaning → chunking → embedding → loading; ZenML orchestrates them with `@pipeline`/`@step` decorators and tracks outputs as versioned artifacts.
- The pipeline stores two snapshots in the feature store: cleaned documents (for fine-tuning) and chunked+embedded documents (for RAG retrieval) — both in Qdrant, leveraging Qdrant's metadata index as a NoSQL store for the cleaned-only collection (no vector index).
- **Change Data Capture (CDC)** is the production-grade syncing strategy between data warehouse and feature store; three patterns: timestamp-based, trigger-based, and log-based (log-based is most popular: low overhead, captures deletes, vendor-specific log format is the main drawback); push vs pull are the two delivery models.
- The chapter implements a custom **Object-Vector Mapping (OVM)** layer (`VectorBaseDocument`) analogous to ORM — it sits on top of Qdrant, exposes `bulk_insert`, `bulk_find`, `search`, `from_record`, `to_point`, infers collection names from a `Config` inner class, and uses Pydantic + Generics for type safety.
- The domain model factors RAG entities along two axes — **data state** (cleaned, chunked, embedded) × **data category** (posts, articles, repositories) — yielding nine concrete Pydantic classes inheriting from abstract base classes (`CleanedDocument`, `Chunk`, `EmbeddedChunk`).
- The processing layer uses the **Dispatcher + Abstract Factory + Strategy** patterns: `CleaningDispatcher`/`ChunkingDispatcher`/`EmbeddingDispatcher` route to handler classes via a factory keyed on `DataCategory`, isolating per-category logic and respecting DRY.
- Article chunking uses a regex sentence splitter (avoids splitting on abbreviations like "e.g." or "Dr.") and groups sentences into chunks bounded by `min_length`/`max_length`; chunk IDs are MD5 hashes of chunk content, enabling automatic deduplication.
- Generic chunking (`chunk_text`) is a two-stage process: LangChain's `RecursiveCharacterTextSplitter` (paragraph-aware splitting at chunk_size=500) followed by `SentenceTransformersTokenTextSplitter` (enforces the embedding model's max input length with chunk_overlap=50).
- Embedding handlers batch chunks for GPU throughput (10x+ speedup via parallel inference), and the `EmbeddingModelSingleton` ensures the SentenceTransformer model is loaded once into memory using the Singleton pattern.
- Threading is used for I/O-bound parallelism (MongoDB fetch across articles/posts/repos collections) because Python's GIL doesn't block I/O; multiprocessing is reserved for CPU/memory-bound work where each process has its own GIL.

## Key Quotes
> "RAG enhances the accuracy and reliability of generative AI models with information fetched from external sources. It is a technique complementary to the internal knowledge of the LLMs." — defining RAG

> "By introducing RAG, we enforce the LLM to always answer solely based on the introduced context. The LLM will act as the reasoning engine, while the additional information added through RAG will act as the single source of truth for the generated answer." — RAG as a hallucination control

> "It is essential to preprocess the user input in the same way you processed the raw documents in the RAG ingestion pipeline. This means you must clean, chunk (if necessary), and embed the user's input using the same functions, models, and hyperparameters." — invoking the training-serving skew analogy for RAG

> "While standalone vector indices like FAISS are effective for similarity search, they lack vector DBs' comprehensive data management capabilities. Vector DBs support CRUD operations, metadata filtering, scalability, real-time updates, backups, ecosystem integration, and robust data security, making them more suited for production environments than standalone indices." — distinguishing vector DBs from vector indices

> "Query routing is identical to an if/else statement but much more versatile as it works directly with natural language." — intuition for LLM-based routing

> "The intuition behind [small-to-big] is that if we use the whole text for computing the embedding, we might introduce too much noise, or the text could contain multiple topics, which results in a poor overall semantic representation of the embedding."

> "In practice, on the retrieval side, you usually start with filtered vector search or hybrid search, as they are fairly quick to implement. This approach gives you the flexibility to adjust your strategy based on performance. If the results are not as expected, you can always fine-tune your embedding model." — practical retrieval ordering

> "We can't apply this [cross-encoder re-ranking] model at the initial retrieval step because it is costly. That is why a popular strategy is to retrieve the data using a similarity distance between the embeddings and refine the retrieved information using a re-ranking model."

> "A popular strategy is to start with a batch architecture, as it's faster and easier to implement. After the product is in place, you gradually move to a streaming design to reduce costs and improve the user experience." — batch-first feature-pipeline doctrine

> "Change data capture (CDC) is a strategy that allows you to optimally keep two or more data storage types in sync without computing and I/O overhead. It captures any CRUD operation done on the source DB and replicates it on a target DB."

> "Using threads to parallelize I/O-bounded calls is good practice in Python, as they are not locked by the Python Global Interpreter Lock (GIL). In contrast, adding each call to a different process would add too much overhead, as a process takes longer to spin off than a thread."

## Architecture & Components

**Vanilla RAG architecture** (Figure 4.1) — three loosely-coupled pipelines:
- **Ingestion pipeline**: data extraction module → cleaning layer → chunking module → embedding component → loading module. Populates the vector DB with `(embedding, metadata)` records.
- **Retrieval pipeline**: embeds user input with the same model used at ingest, queries the vector DB via ANN (approximate nearest neighbor) using a distance metric, returns top-K chunks.
- **Generation pipeline**: assembles `system_template + prompt_template.format(context=retrieved, user_question=q)`, calls the LLM. Prompt templates are versioned via Git, a DB, or tools like LangFuse.

**Vector DB workflow**:
1. Index vectors using HNSW / random projection / PQ / LSH.
2. Query by similarity (cosine, Euclidean, dot product).
3. Post-process results (refine, metadata filtering pre/post search).
4. Production-grade DB operations: sharding/replication, monitoring, access control, backups.

**LLM Twin RAG feature pipeline architecture** (Figure 4.9) — batch design:
- Source: MongoDB data warehouse (populated by Chapter 3's ETL crawlers of Medium/Substack/GitHub).
- Orchestrator: ZenML (`@pipeline feature_engineering`, with each phase a `@step`).
- Five steps: `query_data_warehouse` → `clean_documents` → (parallel: `load_to_vector_db(cleaned)`) and (`chunk_and_embed` → `load_to_vector_db(embedded)`).
- Sink: Qdrant vector DB serving as the **logical feature store**, alongside ZenML versioned artifacts for offline training.
- Two snapshots stored: cleaned (no vector index, NoSQL-style usage of Qdrant metadata) and chunked+embedded (with vector index).
- Configuration: Pydantic `Settings` class with `.env` overrides; YAML configs injected at runtime via `feature_engineering.with_options(config_path=...)`.

**Domain entity hierarchy** (Figure 4.16) — two-axis taxonomy:
- State axis: `CleanedDocument` / `Chunk` / `EmbeddedChunk` (abstract base classes).
- Category axis: `Post*` / `Article*` / `Repository*`.
- Nine concrete combinations (e.g., `CleanedArticleDocument`, `ArticleChunk`, `EmbeddedArticleChunk`).
- All inherit `VectorBaseDocument` (the custom OVM).

**Object-Vector Mapping (OVM)** — `VectorBaseDocument(BaseModel, Generic[T], ABC)`:
- Translates Pydantic instances ↔ Qdrant `PointStruct` via `to_point()` / `from_record()`.
- Exposes class methods: `bulk_insert`, `_bulk_insert`, `bulk_find`, `_bulk_find`, `search`, `_search`, `get_collection_name`, `create_collection`.
- Collection name + data category + `use_vector_index` flag come from each subclass's inner `Config` class.
- Failure pattern: public method wraps private method, catches `UnexpectedResponse`, attempts collection creation, retries once.

**Dispatcher layer** — applies Abstract Factory + Strategy patterns:
- `CleaningDispatcher` / `ChunkingDispatcher` / `EmbeddingDispatcher` each call a corresponding `HandlerFactory.create_handler(data_category)`.
- Returns a concrete `Handler` implementing `clean()` / `chunk()` / `embed_batch()`.

**Handler classes** (9 total):
- `PostCleaningHandler`, `ArticleCleaningHandler`, `RepositoryCleaningHandler` (return `Cleaned*Document`).
- `PostChunkingHandler`, `ArticleChunkingHandler`, `RepositoryChunkingHandler` (return `list[*Chunk]`).
- `PostEmbeddingHandler`, `ArticleEmbeddingHandler`, `RepositoryEmbeddingHandler` (return `list[Embedded*Chunk]`).

**EmbeddingModelSingleton** — wraps `SentenceTransformer`, ensures one in-memory model instance, exposes `model_id`, `embedding_size` (computed via a one-shot dummy forward pass + `@cached_property`), `max_input_length`, `tokenizer`, and a callable `__call__(text)` interface returning numpy arrays or Python lists.

## RAG Techniques Covered

**Pre-retrieval — data indexing**:
- **Sliding window chunking**: overlap between chunks preserves boundary context (legal/scientific/medical documents).
- **Enhancing data granularity**: clean irrelevant details, verify factual accuracy, update outdated content.
- **Metadata tagging**: dates, URLs, external IDs, chapter markers used for filtered search.
- **Optimizing index structures**: vary chunk sizes, multi-indexing strategies.
- **Small-to-big**: embed a small, high-purity span, store a wider window as metadata for prompt construction — decouples retrieval signal from generation context.

**Pre-retrieval — query optimization**:
- **Query routing**: LLM- or embedding-based natural-language if/else for selecting data sources, prompt templates, or skipping retrieval entirely.
- **Query rewriting**: paraphrase, synonym substitution, sub-query decomposition.
- **HyDE (Hypothetical Document Embeddings)**: LLM drafts a fake answer, both query and fake answer get embedded.
- **Query expansion**: enrich with related terms/synonyms (e.g., "disease" → "illness", "ailment").
- **Self-query**: LLM extracts structured filters (entities, events, relationships) from an unstructured query and applies them to the metadata index to shrink the vector search space.

**Retrieval**:
- **Embedding model fine-tuning**: adapt pretrained embedder to domain jargon.
- **Instructor models**: prefix-instruction-guided embeddings as a fine-tuning alternative.
- **Hybrid search**: blend vector and keyword search with an alpha weight; two parallel searches, normalized and unified.
- **Filtered vector search**: metadata filtering applied pre/post vector search using Qdrant's metadata index.

**Post-retrieval**:
- **Prompt compression**: remove noise before sending to LLM (context window economy).
- **Re-ranking** (Figure 4.7, 4.8): cross-encoder scores `(query, chunk)` jointly; results sorted and top-N kept. Bi-encoder for first-pass speed, cross-encoder for second-pass accuracy.

## Code & Concrete Examples

**Cosine similarity with Sentence Transformers**:
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode([
    "The dog sits outside waiting for a treat.",
    "I am going swimming.",
    "The dog is swimming."
])  # shape (3, 384)
similarities = model.similarity(embeddings, embeddings)
```

**Cross-modal embedding with CLIP** (`clip-ViT-B-32`): a single model embeds both an image and natural-language captions into the same 512-dim space; cosine similarity quantifies image↔text alignment.

**Instructor model**: `INSTRUCTOR("hkunlp/instructor-base")` with input `[instruction, sentence]` produces (1, 768)-dim instruction-conditioned embeddings.

**ZenML pipeline skeleton**:
```python
@pipeline
def feature_engineering(author_full_names: list[str]) -> None:
    raw_documents = fe_steps.query_data_warehouse(author_full_names)
    cleaned_documents = fe_steps.clean_documents(raw_documents)
    last_step_1 = fe_steps.load_to_vector_db(cleaned_documents)
    embedded_documents = fe_steps.chunk_and_embed(cleaned_documents)
    last_step_2 = fe_steps.load_to_vector_db(embedded_documents)
```

**Settings defaults**:
- `TEXT_EMBEDDING_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"`
- `RERANKING_CROSS_ENCODER_MODEL_ID = "cross-encoder/ms-marco-MiniLM-L-4-v2"`
- `RAG_MODEL_DEVICE = "cpu"`
- `QDRANT_DATABASE_HOST/PORT = "localhost"/6333`
- Article chunking metadata: `min_length=1000`, `max_length=1000` (override of the base default `chunk_size=500, chunk_overlap=50`).
- Pipeline observed values: 76 raw documents → 2,373 chunks (3 authors).

**Article chunking regex**: `re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s", text)` — splits on sentence-ending punctuation while preserving abbreviations like "e.g." or "Dr.".

**Two-stage `chunk_text`**:
1. LangChain `RecursiveCharacterTextSplitter(separators=["\n\n"], chunk_size=500, chunk_overlap=0)` for paragraph-aware splitting.
2. LangChain `SentenceTransformersTokenTextSplitter(chunk_overlap=50, tokens_per_chunk=model.max_input_length, model_name=model.model_id)` to enforce the embedding model's token limit.

**Thread-pool fan-out for I/O-bound MongoDB queries**: `ThreadPoolExecutor()` submits article/post/repository fetches concurrently; total time = max(latencies) rather than sum.

## Connections
- [[rag]] — this chapter is a comprehensive RAG primer; expand the page with vanilla-vs-advanced taxonomy.
- [[GraphRAG]] — sibling RAG variant, not covered here.
- [[Hallucination]] — RAG is presented as the primary mitigation lever.
- [[ContextualEmbedding]] — embeddings as the substrate of RAG retrieval.
- [[CosineSimilarity]] — primary distance metric for ANN retrieval discussed at length.
- [[Word2Vec]], [[GloVe]] — cited as classical text embedding precursors.
- [[bert]] — encoder-only transformer family used to produce modern text embeddings.
- [[CNN]], [[ResNet]] — used as image embedders.
- [[encoderdecoder]] / [[transformer]] — architectural backbone for embedding models.
- [[OneHotEncoding]] — explicit foil for embeddings (curse of dimensionality).
- [[CurseOfDimensionality]] — invoked to motivate dense embeddings over one-hot.
- [[Tokenization]] / [[Tokenizer]] — required at retrieval/inference to satisfy embedding-model input format.
- [[TrainingServingSkew]] — same-preprocessing principle applied to RAG.
- [[FeatureStore]], [[FeatureEngineering]] — Qdrant + ZenML artifacts form LLM Twin's logical feature store.
- [[DataWarehouse]], [[DataLake]], [[ETL]], [[ELT]] — MongoDB warehouse is the upstream source; CDC discussion bridges these.
- [[MLOps]] — orchestration, prompt-template versioning, continuous training framing.
- [[GlobalInterpreterLock]] — directly cited to justify threads-for-IO / processes-for-CPU policy.
- [[Singleton]] — pattern used for `EmbeddingModelSingleton`.
- [[Hadoop]] / NoSQL DB families — vector DBs compared with traditional scalar DBs.
- [[HuggingFace]] — host of Sentence Transformers and the MTEB leaderboard.
- [[NetflixPrize]] (collaborative filtering lineage) — embeddings pre-LLM use case.
- [[anthropic]]-class LLMs / [[openai]] GPT-4o — referenced as the LLM consuming the augmented prompt.

New entity/concept candidates worth creating (see report): Qdrant, ZenML, LangChain, Sentence Transformers, MongoDB, Apache Kafka (existing entity), Redpanda, Apache Flink (existing entity), Bytewax, RabbitMQ, MTEB, Pinecone, Confluent, LangFuse, Unstructured, CLIP, UMAP, t-SNE, Instructor (model family), HNSW, ProductQuantization, LocalitySensitiveHashing, RandomProjection, ApproximateNearestNeighbor, FAISS, HypotheticalDocumentEmbeddings (HyDE), QueryRouting, QueryRewriting, QueryExpansion, SelfQuery, SlidingWindowChunking, SmallToBigRetrieval, HybridSearch, FilteredVectorSearch, CrossEncoder, BiEncoder, ReRanking, PromptCompression, ChangeDataCapture, BatchPipeline, StreamingPipeline, FeaturePipeline, ObjectVectorMapping (OVM), AbstractFactoryPattern, StrategyPattern, DispatcherPattern, DomainDrivenDesign, Pydantic, VanillaRAG, AdvancedRAG, LLMTwin, Spectrogram, OneHotEncoding (exists), FeatureHashing, PromptTemplate, ContinuousTraining, EmbeddingModel, ChunkingStrategy, RecursiveCharacterTextSplitter.

## Contradictions
- None observed. The chapter aligns with the existing [[rag]] wiki page (which currently sketches the same ingest/retrieve/generate triad) and the [[Hallucination]] mitigation framing. It deepens rather than contradicts those notes. The training-serving-skew analogy reinforces the existing [[TrainingServingSkew]] stub.
