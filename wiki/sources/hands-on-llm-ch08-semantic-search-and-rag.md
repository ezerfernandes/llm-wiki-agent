---
title: "Hands-On LLMs Ch 8 — Semantic Search and Retrieval-Augmented Generation"
type: source
tags: [book, hands-on-llm, oreilly, llm, semantic-search, rag, dense-retrieval, reranking, cross-encoder, bm25, faiss, vector-database, chunking, query-rewriting, multi-hop, agentic-rag, grounded-generation, llm-as-judge, evaluation, map, ndcg]
date: 2024-01-01
source_file: raw/books/hands-on-llm/ch08-semantic-search-and-rag.md
book: "Hands-On Large Language Models"
book_isbn13: "9781098150969"
book_authors: ["Jay Alammar", "Maarten Grootendorst"]
book_publisher: "O'Reilly Media"
book_year: 2024
---

# Hands-On LLMs Ch 8 — Semantic Search and Retrieval-Augmented Generation

## Summary

The eighth chapter of [[JayAlammar|Jay Alammar]] and [[MaartenGrootendorst|Maarten Grootendorst]]'s *Hands-On Large Language Models* ([[OReilly|O'Reilly Media]], 2024, ISBN 978-1-098-15096-9) and **the book's headline [[rag|RAG]] chapter** — picks up the retrieval thread [[hands-on-llm-ch07-advanced-text-generation|Ch 7]] explicitly deferred (*"retrieval will be discussed in the next chapter"*) and resolves it via the **three-category taxonomy** the chapter organizes itself around: **[[DenseRetrieval|dense retrieval]]** (embed query + documents, find nearest neighbors), **[[ReRanking|reranking]]** (rescore an existing shortlist with a stronger model), and **[[rag|RAG]]** (text generation grounded on retrieved documents — with citations). Each category is walked from intuition → runnable code → caveats → evaluation, with the canonical worked example being **a 15-sentence Wikipedia article on the film *Interstellar*** searched via [[Cohere]]'s `co.embed(input_type="search_document")` → [[FAISS|`faiss.IndexFlatL2`]] → `co.embed(input_type="search_query")` → `co.rerank(top_n=3)` → `co.chat(documents=...)` (managed-LLM RAG) and then replicated locally with [[Phi3Mini|Phi-3]] + [[BGESmallEnV15|`BAAI/bge-small-en-v1.5`]] + [[FAISS]] + [[LangChain|`langchain.RetrievalQA`]]. The chapter ends with a section on **advanced RAG** (query rewriting, multi-query RAG, multi-hop RAG, query routing, agentic RAG) and a section on **RAG evaluation** (four-axis verifiability + [[RAGAS|Ragas]] LLM-as-a-judge automation).

Ch 8 is **the wiki's third chapter-length RAG treatment** after [[ai-engineering-ch06-rag-agents|Huyen's *AI Engineering* Ch 6]] (the design-discipline framing — retrieval-as-feature-engineering, the term-vs-embedding division, four production retrieval-optimization tactics) and [[leh-ch04-rag-feature-pipeline|*LLM Engineer's Handbook* Ch 4]] (the ZenML-based batch RAG feature pipeline). Where Huyen Ch 6 is the **engineering-discipline** chapter and LEH Ch 4 is the **production-pipeline-recipe** chapter, *Hands-On LLMs* Ch 8 is the **pedagogical-introduction-with-runnable-code** chapter — the smallest-credible worked example that puts dense retrieval, BM25, reranking, and grounded generation on the same 15-sentence corpus so the reader can run all four side by side and watch them produce visibly different answers to the same query (*"how precise was the science"*).

The chapter opens with a structural observation: **the first industrial-scale adoption of LLMs was not chat — it was search.** Within months of the 2018 BERT paper, Google announced *"one of the biggest leaps forward in the history of Search"* and Microsoft Bing announced *"the largest quality improvements to our Bing customers in the past year."* The ability these models add is named — **[[SemanticSearch|semantic search]]** — *"searching by meaning, and not simply keyword matching."* On a parallel track, the fast adoption of generative LLMs produced **[[Hallucination|hallucinations]]** at scale; the leading industry mitigation was [[rag|RAG]] (Lewis et al. 2020, *"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"*, NeurIPS 33: 9459–9474). Ch 8's pedagogical move is to treat both halves — search-by-meaning and grounded-generation — as the same architectural family at different stages of completion: retrieval-then-rerank-then-generate.

Six things the chapter introduces at runnable-code granularity that the wiki did not previously cover: (1) **the dense-vs-sparse retrieval comparison on the same query** — the *"how precise was the science"* query returns the correct answer (*"It has also received praise from many astronomers for its scientific accuracy and portrayal of theoretical astrophysics"*) via dense retrieval but the wrong answer via [[BM25]] (which picks *"Interstellar is a 2014 epic science fiction film..."* because of the word *"science"* overlap); (2) **the [[CrossEncoder|cross-encoder]] reranking primitive** via Cohere's `co.rerank` endpoint with the **MIRACL benchmark efficacy claim** *"a reranker can boost performance from 36.5 to 62.8, measured as nDCG@10"*; (3) **[[FAISS]] used as the in-memory search index** for embedding nearest-neighbor search (`faiss.IndexFlatL2(dim)` + `index.add(embeds)` + `index.search(query_embed, k)`); (4) **the [[ChunkingStrategy|chunking-strategy design space]]** as a load-bearing dense-retrieval decision (one-vector-per-document vs multiple-vectors-per-document; sentence vs paragraph vs overlapping); (5) **the [[GroundedGeneration|grounded-generation citation primitive]]** via Cohere's `co.chat(message=query, documents=docs_dict)` returning **explicit span-level citations** (`ChatCitation(start=21, end=36, text='worldwide gross', document_ids=['doc_0'])`); (6) **the [[RAGEvaluation|RAG-evaluation four-axis taxonomy]]** — **fluency / perceived utility / citation recall / citation precision** — per Liu, Zhang & Liang 2023 *"Evaluating verifiability in generative search engines"* (arXiv:2304.09848), with the [[RAGAS|Ragas]] LLM-as-a-judge library as the automated counterpart.

The chapter forward-references **Ch 10** (training and fine-tuning embedding models — Ch 8's deferred coverage of *"language models need to be trained on question-answer pairs to become better at retrieval"*) and the broader literature via **Lin, Nogueira & Yates 2021** (*"Pretrained transformers for text ranking: BERT and beyond"*) as the canonical reference for LLM-for-search developments through 2021. Forward references also point at **[[ChipHuyen|Chip Huyen]] / [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]** indirectly via shared vocabulary (the four-axis RAG-evaluation framing matches Huyen's [[ContextPrecision]] / [[ContextRecall]] axes).

## Key Claims

- **The three-category taxonomy is the chapter's organizing axis.** *"There's a lot of research on how to best use language models for search. Three broad categories of these models are dense retrieval, reranking, and RAG."* Each category is treated as architecturally distinct rather than as a single pipeline — they are **composable** (the chapter's worked RAG example is dense-retrieval → reranking → grounded generation) but not **dependent** (you can run dense retrieval without reranking, or reranking without RAG).
- **The first industrial-scale LLM adoption was search.** *"Search was one of the first language model applications to see broad industry adoption. Months after the release of the seminal 'BERT: Pre-training of deep bidirectional transformers for language understanding' (2018) paper, Google announced it was using it to power Google Search and that it represented 'one of the biggest leaps forward in the history of Search.' Not to be outdone, Microsoft Bing also stated that 'Starting from April of this year, we used large transformer models to deliver the largest quality improvements to our Bing customers in the past year.'"*
- **The capability is named: [[SemanticSearch|semantic search]]** — *"the ability they add is called semantic search, which enables searching by meaning, and not simply keyword matching."*
- **The hallucination problem motivates RAG.** *"the fast adoption of text generation models led many users to ask the models questions and expect factual answers. And while the models were able to answer fluently and confidently, their answers were not always correct or up-to-date. This problem grew to be known as model 'hallucinations,' and one of the leading ways to reduce it is to build systems that can retrieve relevant information and provide it to the LLM to aid it in generating more factual answers."*
- **Generative search is a subset of RAG.** *"Generative search is a subset of a broader type of category of systems better called RAG systems. These are text generation systems that incorporate search capabilities to reduce hallucinations, increase factuality, and/or ground the generation model on a specific dataset."*

### Dense retrieval

- **[[DenseRetrieval|Dense retrieval]] turns search into nearest-neighbor lookup over embeddings.** *"Dense retrieval systems rely on the concept of embeddings ... and turn the search problem into retrieving the nearest neighbors of the search query (after both the query and the documents are converted into embeddings)."*
- **The two-question caveat:** (1) the system designer must decide whether to **apply a similarity threshold** to filter irrelevant results; (2) **a query and its best result are not always semantically similar** — *"This is why language models need to be trained on question-answer pairs to become better at retrieval. This process is explained in more detail in Chapter 10."* (Forward reference to Ch 10's embedding-model fine-tuning chapter.)
- **The worked example is the Wikipedia *Interstellar* article — 15 sentences.** Each sentence becomes a chunk via `text.split('.')` (light processing). Embedded via Cohere with `input_type="search_document"` for documents and `input_type="search_query"` for queries — the dual-input-type signal that distinguishes document indexing from query embedding. Output shape: `(15, 4096)` — 15 vectors of dimension 4,096.
- **Index built with [[FAISS|`faiss.IndexFlatL2`]]** (L2 distance, flat / exhaustive index):
  ```python
  import faiss
  dim = embeds.shape[1]
  index = faiss.IndexFlatL2(dim)
  index.add(np.float32(embeds))
  ```
- **The signature dense-retrieval result on the *Interstellar* query:** `query = "how precise was the science"` returns *"It has also received praise from many astronomers for its scientific accuracy and portrayal of theoretical astrophysics"* as the top hit (distance 10757.379883) — **the correct answer with no keyword overlap with the query.** *"Notice that this wouldn't have been possible if we were only doing keyword search because the top result did not include the same keywords in the query."*
- **[[BM25]] runs on the same corpus for direct comparison** via `rank_bm25.BM25Okapi`. The tokenizer lowercases, strips punctuation, and removes [[StopWord|stop words]] (`sklearn.feature_extraction._stop_words.ENGLISH_STOP_WORDS`). **On the same query, BM25 picks the wrong answer:** *"Interstellar is a 2014 epic science fiction film co-written, directed, and produced by Christopher Nolan"* (BM25 score 1.789) — *"the first result does not really answer the question despite it sharing the word 'science' with the query."* This is the chapter's canonical motivating contrast for **why semantic search matters when keyword search exists**.
- **Three caveats of dense retrieval Ch 8 names explicitly:**
  1. **Out-of-distribution queries still get results** — *"if the texts don't contain the answer? We still get results and their distances."* Worked failure case: query *"What is the mass of the moon?"* against the *Interstellar* corpus returns the film's worldwide-gross sentence as the nearest neighbor. The mitigation: a **similarity threshold** ([[SimilarityThreshold]]) or surface the best info and let the user decide; logging clicks improves future versions.
  2. **Exact-phrase matching is a [[BM25]] strength, not a dense-retrieval strength** — *"another caveat of dense retrieval is when a user wants to find an exact match for a specific phrase. That's a case that's perfect for keyword matching. That's one reason why **hybrid search**, which includes both semantic search and keyword search, is advised instead of relying solely on dense retrieval."* (Establishes [[HybridSearch|hybrid search]] as the default production answer.)
  3. **Domain transfer is hard** — *"dense retrieval systems also find it challenging to work properly in domains other than the ones that they were trained on. So, for example, if you train a retrieval model on internet and Wikipedia data, and then deploy it on legal texts (without having enough legal data as part of the training set), the model will not work as well in that legal domain."*
- **[[Chunking|Chunking long texts]] is forced by Transformer context limits.** *"One limitation of Transformer language models is that they are limited in context sizes, meaning we cannot feed them very long texts that go above the number of words or tokens that the model supports. So how do we embed long texts?"*
- **The chunking design space is two-bucket:**
  - **One vector per document** — either embed only a representative slice (title / opening paragraph), or embed chunks and average. The slice option *"may work better for documents where the beginning captures the main points"* (Wikipedia-style); the averaging option *"results in a highly compressed vector that loses a lot of the information."*
  - **Multiple vectors per document** — *"this approach is better because it has full coverage of the text and because the vectors tend to capture individual concepts inside the text."* Sub-strategies:
    - One sentence per chunk — too granular, vectors don't capture enough context.
    - One paragraph per chunk — good if paragraphs are short, else *"every 3–8 sentences is a chunk."*
    - **Add document title to each chunk** to inject context.
    - **Overlapping chunks** — *"adding some of the text before and after them to the chunk. This way, the chunks can overlap so they include some surrounding text that also appears in adjacent chunks."*
  - *"Expect more chunking strategies to arise as the field develops — some of which may even use LLMs to dynamically split a text into meaningful chunks."*
- **Nearest-neighbor search vs vector databases.** Naive `numpy` distance computation works *"if you have thousands or tens of thousands of vectors in your archive."* Beyond that:
  - **[[ApproximateNearestNeighbor|Approximate-nearest-neighbor]] libraries** — [[Annoy]] (Spotify), [[FAISS]] (Meta) — *"allow you to retrieve results from massive indexes in milliseconds and some of them can improve their performance by utilizing GPUs and scaling to clusters of machines to serve very large indices."*
  - **[[VectorDatabase|Vector databases]]** — [[Weaviate]], [[Pinecone]] — *"A vector database allows you to add or delete vectors without having to rebuild the index. They also provide ways to filter your search or customize it in ways beyond merely vector distances."* (This is the **library-vs-database** distinction Huyen Ch 6 codifies.)
- **Fine-tuning embedding models for dense retrieval.** *"The process for this fine-tuning is to get training data composed of queries and relevant results."* Worked example with the *"Interstellar premiered on October 26, 2014, in Los Angeles"* sentence: two **positive queries** (*"Interstellar release date"* / *"When did Interstellar premier"*) and one **negative query** (*"Interstellar cast"*). *"The fine-tuning step works to make the relevant queries closer to the document and at the same time make irrelevant queries farther from the document."* Deferred to Ch 10 for the full treatment.

### Reranking

- **[[ReRanking|Reranking]] is the lightest-touch way to add LLMs to an existing search system.** *"For those organizations, an easier way to incorporate language models is as a final step inside their search pipeline. This step is tasked with changing the order of the search results based on relevance to the search query. This one step can vastly improve search results and it's in fact what Microsoft Bing added to achieve the improvements to search results using BERT-like models."*
- **The worked reranking example uses Cohere's `co.rerank` endpoint** — *"a simple way to start using a first reranker. We simply pass it the query and texts and get the results back. We don't need to train or tune it."*
  ```python
  results = co.rerank(query=query, documents=texts, top_n=3, return_documents=True)
  for idx, result in enumerate(results.results):
      print(idx, result.relevance_score, result.document.text)
  ```
- **On *"how precise was the science"* over the 15 *Interstellar* sentences,** the reranker assigns relevance score **0.1698** to the correct *"praise from astronomers for scientific accuracy"* sentence and ≤ 0.07 to all others — *"much more confident about the first result."*
- **The two-stage search pipeline pattern.** *"In this basic example, we passed our reranker all 15 of our documents. More often, however, our index would have thousands or millions of entries, and we need to shortlist, say one hundred or one thousand results and then present those to the reranker."* This is the canonical **first-stage retrieval → second-stage reranking** pattern. *"The first-stage retriever can be keyword search, dense retrieval, or better yet — hybrid search that uses both of them."*
- **Headline efficacy claim:** *"On a multilingual benchmark like [[MIRACL]], a reranker can boost performance from 36.5 to 62.8, measured as [[NDCG|nDCG@10]] (more on evaluation later in this chapter)."* — almost a **2× lift** from adding a reranker on top of [[BM25]].
- **The keyword + rerank pipeline worked example.** *"Let's tweak our keyword search function so it retrieves a list of the top 10 results using keyword search, then use rerank to choose the top 3 results from those 10"* — `bm25.get_scores(...)` → top-10 → `co.rerank(query, docs, top_n=3)`. On *"how precise was the science"* the reranker **elevates the correct sentence to position 1** even though BM25 had ranked it at position 2.
- **The open-source path is `sentence-transformers`.** *"If you want to locally set up retrieval and reranking on your own machine, then you can use the Sentence Transformers library."* The library's *"Retrieve & Re-Rank"* documentation section has the canonical instructions.
- **How reranking models work — the [[CrossEncoder|cross-encoder]] mechanism.** *"One popular way of building LLM search rerankers is to present the query and each result to an LLM working as a cross-encoder. This means that a query and possible result are presented to the model at the same time allowing the model to view both these texts before it assigns a relevance score."*
- **All documents processed simultaneously as a batch, but each scored independently.** *"All of the documents are processed simultaneously as a batch yet each document is evaluated against the query independently. The scores then determine the new order of the results."*
- **The method has a name — [[MonoBERT|monoBERT]]** — *"This method is described in more detail in a paper titled 'Multi-stage document ranking with BERT' and is sometimes referred to as monoBERT."*
- **Reranking is fundamentally a classification problem.** *"This formulation of search as relevance scoring basically boils down to being a classification problem. Given those inputs, the model outputs a score from 0–1 where 0 is irrelevant and 1 is highly relevant."* (Connects to Ch 4's classification framing.)
- **Canonical reference for LLM-for-search developments through 2021:** Lin, Nogueira & Yates, *"Pretrained transformers for text ranking: BERT and beyond."*

### Retrieval evaluation

- **Retrieval evaluation requires three components:** *"a text archive, a set of queries, and relevance judgments indicating which documents are relevant for each query."* The relevance-judgments-as-ground-truth requirement is the **annotation bottleneck** of IR evaluation.
- **The chapter focuses on [[MAP|mean average precision]] (MAP)** as its worked example metric. Pedagogical walkthrough:
  - **Precision at position k** = (number of relevant results at position k) / k.
  - **Average precision** for one query = the average of precisions at each position where a relevant document appears. Only relevant-document positions contribute; non-relevant positions are skipped.
  - If the only relevant result is at position 1, AP = 1.0. If it is at position 3 (with two irrelevant results above), AP is penalized.
  - **MAP = mean of average precisions across all queries** in the test suite. *"You may be wondering why the same operation is called 'mean' and 'average.' It's likely an aesthetic choice because MAP sounds better than average average precision."*
- **Beyond MAP, the chapter names [[NDCG|normalized discounted cumulative gain (nDCG)]]** as the more nuanced alternative: *"the relevance of documents is not binary (relevant versus not relevant) and one document can be labeled as more relevant than another in the test suite and scoring mechanism."*
- **Recommended deeper reading:** *"the 'Evaluation in Information Retrieval' chapter of Introduction to Information Retrieval (Cambridge University Press) by Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze."*

### RAG

- **RAG was popularized as the leading hallucination-mitigation technique.** *"The mass adoption of LLMs quickly led to people asking them questions and expecting factual answers. While the models can answer some questions correctly, they also confidently answer lots of questions incorrectly. The leading method the industry turned to remedy this behavior is RAG, described in the paper 'Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks' (2020)."*
- **Canonical citation:** Patrick Lewis et al., *"Retrieval-augmented generation for knowledge-intensive NLP tasks."* Advances in Neural Information Processing Systems 33 (2020): 9459–9474.
- **What RAG adds beyond plain generation:** *"RAG systems incorporate search capabilities in addition to generation capabilities. They can be seen as an improvement to generation systems because they reduce their hallucinations and improve their factuality. They also enable use cases of 'chat with my data' that consumers and companies can use to ground an LLM on internal company data, or a specific data source of interest (e.g., chatting with a book)."*
- **Search-engine-with-RAG examples Ch 8 names:** [[Perplexity]], Microsoft Bing AI, Google [[gemini|Gemini]].
- **The structural extension from search to RAG** is one component: *"We do that by adding an LLM to the end of the search pipeline. We present the question and the top retrieved documents to the LLM, and ask it to answer the question given the context provided by the search results."*
- **[[GroundedGeneration|Grounded generation]] is the chapter's name for the generation step.** *"This generation step is called grounded generation because the retrieved relevant information we provide the LLM establishes a certain context that grounds the LLM in the domain we're interested in."*
- **The Cohere RAG worked example** — uses `co.chat(message=query, documents=docs_dict)`:
  ```python
  query = "income generated"
  results = search(query)  # dense retrieval
  docs_dict = [{'text': text} for text in results['texts']]
  response = co.chat(message=query, documents=docs_dict)
  print(response.text)
  # → "The film generated a worldwide gross of over $677 million, or $773 million with subsequent re-releases."
  ```
- **Span-level citations are returned automatically:**
  ```python
  citations=[
    ChatCitation(start=21, end=36, text='worldwide gross', document_ids=['doc_0']),
    ChatCitation(start=40, end=57, text='over $677 million', document_ids=['doc_0']),
    ChatCitation(start=62, end=103, text='$773 million with subsequent re-releases.', document_ids=['doc_0'])
  ]
  ```
  This is the **wiki's first runnable demonstration of span-level [[CitationGeneration|citation generation]]** in a RAG response.
- **The local-models RAG worked example** — replicates the flow with [[Phi3Mini|Phi-3]] + [[BGESmallEnV15|`BAAI/bge-small-en-v1.5`]] (*"high on the [[MTEB|MTEB]] leaderboard for embedding models and relatively small"*) + [[FAISS]] + [[LangChain]]:
  ```python
  from langchain import LlamaCpp
  llm = LlamaCpp(model_path="Phi-3-mini-4k-instruct-fp16.gguf", n_gpu_layers=-1, max_tokens=500, n_ctx=2048, seed=42, verbose=False)
  from langchain.embeddings.huggingface import HuggingFaceEmbeddings
  embedding_model = HuggingFaceEmbeddings(model_name='thenlper/gte-small')
  from langchain.vectorstores import FAISS
  db = FAISS.from_texts(texts, embedding_model)
  ```
  (The actual model loaded by the chapter's code snippet is [[GTESmall|`thenlper/gte-small`]] despite the surrounding text discussing `BAAI/bge-small-en-v1.5` — a transcription inconsistency in the source.) *"We will lose the ability to do span citations and the smaller local model isn't going to work as well as the larger managed model, but it's useful to demonstrate the flow."*
- **The [[PromptTemplate|RAG prompt template]] is the central place where retrieved documents enter the LLM:**
  ```
  <|user|>
  Relevant information:
  {context}

  Provide a concise answer the following question using the relevant information provided above:
  {question}<|end|>
  <|assistant|>
  ```
  Wired together via `RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=db.as_retriever(), chain_type_kwargs={"prompt": prompt})`.
- **The `chain_type='stuff'` parameter** is LangChain's name for *"stuff all the retrieved docs into a single prompt"* — the simplest of LangChain's retrieval-QA chain types.

### Advanced RAG techniques

- **[[QueryRewriting|Query rewriting]]** — *"if a question is too verbose, or to refer to context in previous messages in the conversation."* Worked example: the rambling student-essay question *"We have an essay due tomorrow. We have to write about some animal. I love penguins. I could write about them. But I could also write about dolphins. Are they animals? Maybe. Let's do dolphins. Where do they live for example?"* should be rewritten into the focused query *"Where do dolphins live"* before retrieval. *"Cohere's API, for example, has a dedicated query-rewriting mode for `co.chat`."*
- **[[MultiQueryRAG|Multi-query RAG]]** — *"extend the query rewriting to be able to search multiple queries if more than one is needed to answer a specific question."* Worked example: *"Compare the financial results of Nvidia in 2020 vs. 2023"* → **Query 1**: *"Nvidia 2020 financial results"* + **Query 2**: *"Nvidia 2023 financial results"*. *"An additional small improvement here is to also give the query rewriter the option to determine if no search is required and if it can directly generate a confident answer without searching."*
- **[[MultiHopRAG|Multi-hop RAG]]** — *"a more advanced question may require a series of sequential queries."* Worked example: *"Who are the largest car manufacturers in 2023? Do they each make EVs or not?"* → **Step 1**: search for *"largest car manufacturers 2023"* → **Step 2** (with Toyota / Volkswagen / Hyundai as the answer): three follow-up queries, one per manufacturer. The sequential structure distinguishes multi-hop from multi-query.
- **[[QueryRouting|Query routing]]** — *"give the model the ability to search multiple data sources."* Example: HR questions → Notion (HR information system); customer questions → Salesforce (CRM). The router is itself an LLM call that decides the data source.
- **[[AgenticRAG|Agentic RAG]]** — *"the list of previous enhancements slowly delegates more and more responsibility to the LLM to solve more and more complex problems. This relies on the LLM's capability to gauge the required information needs as well as its ability to utilize multiple data sources. This new nature of the LLM starts to become closer and closer to an agent that acts on the world. The data sources can also now be abstracted into tools."* Connection: read-Notion → write-Notion symmetry.
- **Capability ceiling caveat:** *"Not all LLMs will have the RAG capabilities mentioned here. At the time of writing, likely only the largest managed models may be able to attempt this behavior. Thankfully, Cohere's Command R+ excels at these tasks and is available as an open-weights model as well."* (Same agent-capability-cliff caveat as [[hands-on-llm-ch07-advanced-text-generation|Ch 7's]] *"Phi-3-mini is not sufficient"* observation for ReAct agents.)

### RAG evaluation

- **The reference paper is Liu, Zhang & Liang 2023** — *"Evaluating verifiability in generative search engines"* (arXiv:2304.09848). *"A good paper to read on this topic is 'Evaluating verifiability in generative search engines' (2023), which runs human evaluations on different generative search systems."*
- **The four-axis taxonomy** (the chapter's central evaluation contribution):
  - **[[Fluency]]** — *"Whether the generated text is fluent and cohesive."*
  - **[[PerceivedUtility]]** — *"Whether the generated answer is helpful and informative."*
  - **[[CitationRecall]]** — *"The proportion of generated statements about the external world that are fully supported by their citations."*
  - **[[CitationPrecision]]** — *"The proportion of generated citations that support their associated statements."*
- **Human evaluation is preferred but expensive.** *"While human evaluation is always preferred, there are approaches that attempt to automate these evaluations by having a capable LLM act as a judge (called LLM-as-a-judge) and score the different generations along the different axes."*
- **[[RAGAS|Ragas]] is the canonical [[llmasjudge|LLM-as-a-judge]] automation library** — *"Ragas is a software library that does exactly this."* Adds two further metrics beyond the four-axis taxonomy:
  - **[[Faithfulness]]** — *"Whether the answer is consistent with the provided context."*
  - **[[AnswerRelevance]]** — *"How relevant the answer is to the question."*
  - *"The Ragas documentation site provides more details about the formulas to actually calculate these metrics."*

### Summary

- **The chapter's three-bullet summary:**
  1. *"**Dense retrieval**, which relies on the similarity of text embeddings."*
  2. *"**Rerankers**, systems (like monoBERT) that look at a query and candidate results and score the relevance of each document to that query."*
  3. *"**RAG**, where search systems have a generative LLM at the end of the pipeline to formulate an answer based on retrieved documents while citing sources."*
- **Evaluation summary:** *"Mean average precision allows us to score search systems ... Evaluating RAG systems requires multiple axes, however, like faithfulness, fluency, and others that can be evaluated by humans or by [[llmasjudge|LLM-as-a-judge]]."*

## Key Quotes

> "Search was one of the first language model applications to see broad industry adoption. Months after the release of the seminal 'BERT: Pre-training of deep bidirectional transformers for language understanding' (2018) paper, Google announced it was using it to power Google Search and that it represented 'one of the biggest leaps forward in the history of Search.'" — Ch 8, opening

> "The ability they add is called semantic search, which enables searching by meaning, and not simply keyword matching." — Ch 8, on semantic search

> "Generative search is a subset of a broader type of category of systems better called RAG systems. These are text generation systems that incorporate search capabilities to reduce hallucinations, increase factuality, and/or ground the generation model on a specific dataset." — Ch 8, on RAG

> "Notice that this wouldn't have been possible if we were only doing keyword search because the top result did not include the same keywords in the query." — Ch 8, after the *"how precise was the science"* worked example

> "That's one reason why hybrid search, which includes both semantic search and keyword search, is advised instead of relying solely on dense retrieval." — Ch 8, on the BM25 / dense complement

> "On a multilingual benchmark like MIRACL, a reranker can boost performance from 36.5 to 62.8, measured as nDCG@10 (more on evaluation later in this chapter)." — Ch 8, the reranker-efficacy claim

> "This formulation of search as relevance scoring basically boils down to being a classification problem. Given those inputs, the model outputs a score from 0–1 where 0 is irrelevant and 1 is highly relevant." — Ch 8, on reranker training as classification

> "You may be wondering why the same operation is called 'mean' and 'average.' It's likely an aesthetic choice because MAP sounds better than average average precision." — Ch 8, on MAP naming

> "This generation step is called grounded generation because the retrieved relevant information we provide the LLM establishes a certain context that grounds the LLM in the domain we're interested in." — Ch 8, on grounded generation

> "Not all LLMs will have the RAG capabilities mentioned here. At the time of writing, likely only the largest managed models may be able to attempt this behavior." — Ch 8, on the agentic-RAG capability ceiling

> "While human evaluation is always preferred, there are approaches that attempt to automate these evaluations by having a capable LLM act as a judge (called LLM-as-a-judge) and score the different generations along the different axes. Ragas is a software library that does exactly this." — Ch 8, on RAG-evaluation automation

## Connections

### People
- [[JayAlammar]] — co-author. Director and Engineering Fellow at [[Cohere]] — connection load-bearing because Ch 8 uses Cohere's `co.embed` / `co.rerank` / `co.chat` endpoints as the canonical managed-API path through the chapter's worked examples.
- [[MaartenGrootendorst]] — co-author.

### Companies
- [[OReilly|O'Reilly Media]] — publisher.
- [[Cohere]] — managed-API provider for the chapter's worked examples (embed + rerank + chat-with-documents).
- [[meta|Meta]] — Patrick Lewis et al.'s **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks** (2020) was published while Lewis was at Facebook AI Research; [[FAISS]] is Meta's vector-search library.
- [[google|Google]] — historical anchor: the **Google Search adopts BERT** (2018) story that opens the chapter; also [[gemini|Gemini]] is cited as a generative-search example.
- [[microsoft|Microsoft]] — historical anchor: **Bing adopts transformers** (2019) for ranking; Bing AI is cited as a generative-search example; [[Phi3Mini|Phi-3-mini]] is the local-model anchor.
- [[Perplexity]] — cited as a generative-search example alongside Bing AI and Gemini.

### Books / Papers
- [[HandsOnLLM]] — the book.
- *"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"* (Lewis et al. 2020, NeurIPS 33: 9459–9474) — the foundational RAG paper.
- *"Multi-stage document ranking with BERT"* — the [[MonoBERT|monoBERT]] cross-encoder reranking paper.
- *"Pretrained transformers for text ranking: BERT and beyond"* (Lin, Nogueira & Yates 2021) — Ch 8's recommended deeper reading on LLM-for-search.
- *"Evaluating verifiability in generative search engines"* (Liu, Zhang & Liang 2023, arXiv:2304.09848) — the four-axis [[RAGEvaluation|RAG-evaluation]] taxonomy.
- *"BERT: Pre-training of deep bidirectional transformers for language understanding"* (2018) — historical anchor for the Google Search and Bing adoption stories.
- *Introduction to Information Retrieval* (Manning, Raghavan & Schütze, Cambridge University Press) — the chapter's recommended deeper reading for IR evaluation metrics.

### Existing wiki concepts extended
- [[rag]] — the chapter's headline concept; this is the wiki's **third book-chapter treatment of RAG** alongside [[ai-engineering-ch06-rag-agents|Huyen Ch 6]] and [[leh-ch04-rag-feature-pipeline|LEH Ch 4]]; Ch 8 is the **pedagogical-introduction-with-runnable-code** treatment to their **engineering-discipline** and **production-pipeline-recipe** counterparts.
- [[SemanticSearch]] — Ch 8 codifies semantic search as *"searching by meaning, and not simply keyword matching"* and frames it as the 2018-BERT-Google-Search adoption story.
- [[EmbeddingBasedRetrieval]] — Ch 8's name for this is **dense retrieval**; the worked Cohere `co.embed(input_type="search_document" / "search_query")` example is the runnable demonstration.
- [[TermBasedRetrieval]] — Ch 8's name for this is **keyword search** / **lexical search**; the worked `rank_bm25.BM25Okapi` example is the runnable demonstration.
- [[BM25]] — Ch 8 runs `BM25Okapi` on the *Interstellar* corpus and shows it picks the wrong answer to *"how precise was the science"* due to surface-keyword bias.
- [[HybridSearch]] — Ch 8's structural answer to dense-retrieval's exact-phrase weakness.
- [[FAISS]] — Ch 8's worked search-index primitive (`faiss.IndexFlatL2` for exhaustive search; ANN families named for scale).
- [[Annoy]] — Ch 8 names this as the **tree-based ANN library** alternative to FAISS.
- [[ApproximateNearestNeighbor]] — Ch 8 names this as the family of algorithms needed for *"millions of vectors"*.
- [[VectorDatabase]] — Ch 8 distinguishes vector DBs from ANN libraries (CRUD + metadata filtering + no-rebuild-on-update).
- [[Chunking]] — Ch 8's design space (sentence / paragraph / overlapping / LLM-driven) is the chapter's load-bearing dense-retrieval decision.
- [[ChunkingStrategy]] — Ch 8 adds the **one-vector-per-document vs multiple-vectors-per-document** axis to the existing wiki coverage.
- [[CrossEncoder]] — Ch 8's structural mechanism for rerankers; *"the query and possible result are presented to the model at the same time"*.
- [[ReRanking]] — Ch 8 is the chapter that **dedicates a section to reranking as a search-pipeline component**; the worked `co.rerank` example, the keyword-then-rerank pipeline, the MIRACL 36.5 → 62.8 efficacy claim, and the [[MonoBERT|monoBERT]] mechanism all live here.
- [[QueryRewriting]] — Ch 8's *"penguins / dolphins essay question → 'Where do dolphins live'"* worked rewrite.
- [[MAP]] — Ch 8 walks the precision-at-k → AP → MAP construction step-by-step.
- [[NDCG]] — Ch 8 names this as the **graded-relevance alternative to MAP** and as the metric MIRACL is reported under.
- [[Hallucination]] — Ch 8 frames hallucination as the **structural motivation for RAG** (industry mass adoption + factual-answer expectation gap → Lewis et al. 2020).
- [[llmasjudge]] — Ch 8 names [[RAGAS|Ragas]] as the canonical LLM-as-a-judge automation library for RAG evaluation.
- [[RAGAS]] — Ch 8 adds the *Faithfulness* + *Answer Relevance* metrics to the existing seven-metric ECG-Chat treatment.
- [[Cohere]] — Ch 8 is the chapter that uses Cohere's `co.embed` / `co.rerank` / `co.chat` as the **managed-API path through the entire chapter**; promotes the existing Cohere entity-page coverage from *"first-class embedding-API alternative"* (Ch 4) to *"first-class managed-RAG-API alternative."*
- [[LangChain]] — Ch 8's local-RAG path uses `langchain.LlamaCpp` + `langchain.embeddings.huggingface.HuggingFaceEmbeddings` + `langchain.vectorstores.FAISS` + `langchain.chains.RetrievalQA` — the **wiki's first runnable `RetrievalQA.from_chain_type(chain_type='stuff', ...)` receipt**, complementing [[hands-on-llm-ch07-advanced-text-generation|Ch 7's]] Chains / Memory / Agents trio with a fourth LangChain integration (Retrieval).
- [[Phi3Mini]] — the local-RAG generation model.
- [[FineTuning]] — Ch 8's *"queries-and-relevant-results"* fine-tuning recipe for embedding models (forward reference to Ch 10).
- [[MTEB]] — Ch 8 names *"the [[MTEB]] leaderboard for embedding models"* as the selection rubric for the local-RAG embedding model.
- [[Embedding]] / [[SentenceEmbedding]] / [[TextEmbedding]] — the substrate.
- [[CosineSimilarity]] — the standard distance for embedding retrieval (Ch 8 uses L2 in its worked FAISS example but the choice is corpus-dependent).
- [[Lewis2020RAG|Lewis et al. 2020]] (NeurIPS 33: 9459–9474) — the canonical RAG paper.

### New concept pages minted
- [[DenseRetrieval]] — Ch 8's name for embedding-based search; aliases / overlaps with [[EmbeddingBasedRetrieval]].
- [[SparseRetrieval]] — Ch 8's term for [[TermBasedRetrieval]] / lexical / [[BM25]]-style retrieval.
- [[GroundedGeneration]] — the generation step of RAG, anchored on retrieved-context grounding.
- [[GenerativeSearch]] — Ch 8's term for search systems with a generative LLM at the end (subset of RAG); examples [[Perplexity]] / Bing AI / [[gemini|Gemini]].
- [[CitationGeneration]] — span-level citations in RAG outputs (`ChatCitation(start=..., end=..., document_ids=[...])`); Ch 8's worked Cohere `co.chat` example produces these automatically.
- [[CitationRecall]] — *"the proportion of generated statements about the external world that are fully supported by their citations"* (Liu et al. 2023 axis 3).
- [[CitationPrecision]] — *"the proportion of generated citations that support their associated statements"* (Liu et al. 2023 axis 4).
- [[Faithfulness]] — Ragas metric: *"whether the answer is consistent with the provided context"* (named in Ch 8 alongside Answer Relevance).
- [[AnswerRelevance]] — Ragas metric: *"how relevant the answer is to the question."*
- [[Fluency]] — Liu et al. 2023 axis 1 of RAG evaluation.
- [[PerceivedUtility]] — Liu et al. 2023 axis 2 of RAG evaluation.
- [[RAGEvaluation]] — the multi-axis evaluation surface for RAG systems (four-axis Liu et al. 2023 + Ragas Faithfulness + Answer Relevance).
- [[MultiQueryRAG]] — Ch 8's name for the *"more than one query needed to answer a specific question"* pattern (Nvidia 2020 vs 2023).
- [[MultiHopRAG]] — Ch 8's name for the *"sequential queries, each consuming the previous"* pattern (largest car manufacturers → per-manufacturer EV check).
- [[QueryRouting]] — the multi-data-source extension of query rewriting; HR → Notion, customer → Salesforce.
- [[AgenticRAG]] — the agent-end of the Advanced-RAG-techniques continuum, where the LLM coordinates query rewriting + multi-query + multi-hop + routing + tool use.
- [[MonoBERT]] — Nogueira & Lin's BERT-as-cross-encoder reranking model; Ch 8's named reference architecture for *"multi-stage document ranking with BERT."*
- [[SimilarityThreshold]] — the dense-retrieval mitigation for out-of-distribution queries returning nearest-but-irrelevant results.
- [[AveragePrecision]] — Ch 8's per-query precision-at-k average; the building block of [[MAP]].
- [[PrecisionAtK]] — Ch 8's *"number of relevant results at position k, divided by k"* primitive.
- [[RelevanceJudgment]] — Ch 8's name for the human-annotation ground truth in retrieval evaluation.
- [[InformationRetrieval]] — the parent IR field Ch 8 inherits its evaluation vocabulary from.
- [[StopWord]] — Ch 8's BM25 tokenizer removes `sklearn.feature_extraction._stop_words.ENGLISH_STOP_WORDS`.
- [[Lewis2020RAG]] — source-stub for the foundational RAG paper.

### New entity pages minted
- [[MIRACL]] — multilingual retrieval benchmark; Ch 8's source for the *"36.5 → 62.8 nDCG@10"* reranker-efficacy claim.
- [[BGESmallEnV15]] — [[BAAI|BAAI]]'s `BAAI/bge-small-en-v1.5` embedding model (Ch 8's named local-RAG embedding model — *"at the time of writing, it is high on the MTEB leaderboard for embedding models and relatively small"*).
- [[BAAI]] — Beijing Academy of Artificial Intelligence; producer of the BGE embedding-model family.
- [[CohereRerank]] — the Cohere `co.rerank` managed-API endpoint; the chapter's named reranker.
- [[CohereChat]] — the Cohere `co.chat` managed-API endpoint with `documents=...` for grounded generation + automatic citations.
- [[CohereEmbed]] — the Cohere `co.embed` managed-API endpoint with `input_type="search_document" / "search_query"` for dense retrieval.
- [[PatrickLewis]] — first author of *"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"* (NeurIPS 2020).
- [[NelsonFLiu]] — first author of *"Evaluating verifiability in generative search engines"* (arXiv:2304.09848).
- [[PercyLiang]] — last author of the verifiability paper.

## Contradictions and consistency notes

No direct contradictions. Soft consistency notes flagged:

- **[[rag|RAG]] framing harmony with [[ai-engineering-ch06-rag-agents|Huyen Ch 6]].** Huyen frames RAG as *"context construction for foundation models is equivalent to feature engineering for classical ML models"* and decomposes it into **retriever + generator**; Ch 8 takes the same retriever-then-generator decomposition and adds the **three-category retrieval taxonomy** (dense / rerank / RAG) as a finer architectural axis. The two are complementary granularities — Huyen's retriever-vs-generator is the **2-stage view**, Ch 8's dense-vs-rerank-vs-RAG is the **3-mode view**. Documented on [[rag]].

- **[[TermBasedRetrieval]] vs [[SparseRetrieval]] vocabulary.** Huyen Ch 6 deliberately uses *"term-based vs embedding-based"* and rejects *"sparse vs dense"* because [[SPLADE]] produces sparse embeddings whose operations look dense. Ch 8 uses the **dense / sparse** terminology informally (the worked example is *"dense retrieval"* vs *"keyword search using BM25"*) — but never calls BM25 "sparse retrieval" explicitly. The two vocabularies are reconciled: Ch 8's *"keyword search"* = Huyen's *"term-based retrieval"*; Ch 8's *"dense retrieval"* = Huyen's *"embedding-based retrieval"*. The wiki keeps both vocabularies — [[SparseRetrieval]] is created as an alias and back-link.

- **[[VectorDatabase]] vs [[FAISS|FAISS-as-library]].** Ch 8 distinguishes *"ANN libraries like Annoy or FAISS"* from *"vector databases like Weaviate or Pinecone"* on the **CRUD-and-no-rebuild** axis. Same distinction Huyen Ch 6 makes (*"FAISS is the library, not a database"*) and that LEH Ch 4 makes (*"vector DBs vs vector indices"*). Three sources, same framing.

- **[[ReRanking]] efficacy claim** *"36.5 → 62.8 nDCG@10"* on [[MIRACL]] is consistent with Huyen Ch 6's framing of reranking as one of the four production retrieval-optimization tactics; the Ch 8 number is new to the wiki and goes on [[MIRACL]] + [[ReRanking]] as the **canonical reranker-lift benchmark**.

- **[[CrossEncoder]] vs bi-encoder mechanism.** Ch 8's *"the query and possible result are presented to the model at the same time"* description matches the existing LEH-sourced [[CrossEncoder]] page's *"transformer model that scores a (query, document) pair jointly"* — the Ch 8 contribution is naming **[[MonoBERT|monoBERT]]** as the specific reference architecture (Nogueira & Lin), which the existing page did not have.

- **[[QueryRewriting]] LM-driven path** consistent with [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]; Ch 8 adds the **multi-query** ([[MultiQueryRAG]]) and **multi-hop** ([[MultiHopRAG]]) extensions that Huyen Ch 6 does not name as distinct patterns.

- **[[Chunking|Chunking]] design space** consistent with [[ai-engineering-ch06-rag-agents|Huyen Ch 6]] (*"I left my wife a note"* / *"a note"* failure case) and [[leh-ch04-rag-feature-pipeline|LEH Ch 4]] (`RecursiveCharacterTextSplitter` + `SentenceTransformersTokenTextSplitter`); Ch 8's contribution is the **one-vector-per-document vs multiple-vectors-per-document** top-level axis that the other two sources don't make explicit. The unified design space is recorded on [[Chunking]] / [[ChunkingStrategy]].

- **[[MAP]] / [[NDCG]] / [[MRR]] coverage** consistent with [[ai-engineering-ch06-rag-agents|Huyen Ch 6]] (Huyen names all three in a single passage; Ch 8 develops [[MAP]] step-by-step and names [[NDCG]] as the graded-relevance alternative). [[MRR]] is not developed in Ch 8 but the existing wiki page already covers it.

- **[[llmasjudge|LLM-as-a-judge]] for RAG evaluation** consistent with Ragas's reference-free evaluation framing in [[2408.08849-ecg-chat|ECG-Chat]] (where Ragas runs Faithfulness / Answer Relevancy / Context Recall / Context Precision / Context Utilization / Context Entity Recall / Summarization Score); Ch 8 names only the **two simplest** Ragas metrics (Faithfulness + Answer Relevance) plus the Liu et al. 2023 four-axis taxonomy that pre-dates Ragas. The full eight-metric union is on [[RAGAS]].

- **[[CitationGeneration|Citation generation]]** in Cohere's `co.chat` is the wiki's first runnable example; consistent with Liu et al. 2023's four-axis framing where citation recall + citation precision are two of four axes. No prior wiki source covered the **automatic span-level citation** primitive at runnable-code granularity.

- **[[AgenticRAG|Agentic RAG]]** capability-ceiling caveat (*"likely only the largest managed models may be able to attempt this behavior"*) is consistent with [[hands-on-llm-ch07-advanced-text-generation|Ch 7's]] agent-capability-cliff observation (*"Phi-3-mini is not sufficient to run these examples"*) and with [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]'s [[CompoundErrorAccumulation|compound-error-accumulation]] warning. The capability ceiling is a recurring theme across the book and across the wiki.

- **Transcription inconsistency in the local-RAG embedding model.** The chapter's surrounding text discusses *"the [[BGESmallEnV15|BAAI/bge-small-en-v1.5]] model"* but the code snippet loads *"thenlper/gte-small"* ([[GTESmall]]). The wiki records both models — [[BGESmallEnV15]] as the named-in-text model, [[GTESmall]] as the actually-loaded model. This is a documentation bug in the source, not a wiki contradiction.

## Position in the wiki

**Third book-chapter RAG treatment in the wiki**, after [[ai-engineering-ch06-rag-agents|Huyen *AI Engineering* Ch 6]] (the engineering-discipline chapter) and [[leh-ch04-rag-feature-pipeline|LEH Ch 4]] (the production-pipeline-recipe chapter). Ch 8 is the **pedagogical-introduction-with-runnable-code** treatment — the chapter that **puts dense retrieval, BM25, reranking, and grounded generation on the same 15-sentence corpus** so they can be run side-by-side. First wiki coverage of:

- The **three-category retrieval taxonomy** (dense / rerank / RAG) as Ch 8's organizing axis.
- **[[MonoBERT|monoBERT]]** as the reference cross-encoder reranking architecture.
- **The [[MIRACL]] reranker-lift benchmark** (36.5 → 62.8 nDCG@10).
- **[[CitationGeneration|Span-level citation generation]]** in a RAG response (via Cohere `co.chat`).
- **Multi-query / multi-hop / query-routing / agentic-RAG** as a continuum of advanced-RAG techniques.
- **The Liu et al. 2023 four-axis RAG-evaluation taxonomy** (Fluency / Perceived Utility / Citation Recall / Citation Precision).
- **The `BAAI/bge-small-en-v1.5` embedding model** ([[BGESmallEnV15]]) and the [[BAAI]] org.
- **Span-level citation API** via Cohere's `co.chat(documents=...)`.
- **The two-question dense-retrieval caveat** (threshold + query-document-asymmetric semantic distance).
- **The `RetrievalQA.from_chain_type(chain_type='stuff', ...)` LangChain primitive**.
- **The reranker-as-classification framing** (Ch 4 → Ch 8 continuity).

Complements rather than replaces [[ai-engineering-ch06-rag-agents|Huyen Ch 6]] / [[leh-ch04-rag-feature-pipeline|LEH Ch 4]] / [[dspy-rag-tutorial|DSPy RAG tutorial]] — the four sources now form a **four-source RAG curriculum** in the wiki: Ch 8 (intuition + runnable code on a 15-sentence corpus) → Huyen Ch 6 (engineering discipline + production-retrieval tactics) → LEH Ch 4 (ZenML batch feature pipeline + chunking-strategy-per-data-type) → DSPy RAG tutorial (`MIPROv2` optimization on RAGQAArenaTech).
