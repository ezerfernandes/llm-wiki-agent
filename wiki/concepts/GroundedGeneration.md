---
title: "Grounded Generation"
type: concept
tags: [rag, generation, retrieval, llm, citations, hallucination-mitigation]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Grounded Generation

**Grounded generation** is the generation step of [[rag|RAG]] — the LLM is prompted with the user's question **and** the retrieved relevant documents, and asked to answer using that context. Ch 8 of *Hands-On LLMs* introduces the name:

> *"This generation step is called grounded generation because the retrieved relevant information we provide the LLM establishes a certain context that grounds the LLM in the domain we're interested in."* — Ch 8

The pedagogical contrast is with **ungrounded generation** — the bare-LLM completion that produces [[Hallucination|hallucinations]] when the model lacks the necessary knowledge. The retrieved context is the **non-parametric memory** that fills the knowledge gap.

## The structural extension from search to RAG

Ch 8 develops the search → RAG transition as **adding an LLM at the end of the search pipeline**:

> *"We do that by adding an LLM to the end of the search pipeline. We present the question and the top retrieved documents to the LLM, and ask it to answer the question given the context provided by the search results."*

The pipeline becomes: **retrieve → augment prompt with retrieved docs → generate**. Grounded generation is the **third stage** — the LLM call that produces the user-visible answer.

## Worked example: Cohere `co.chat` with `documents=`

Ch 8's managed-RAG receipt produces **automatic span-level [[CitationGeneration|citations]]**:

```python
query = "income generated"
results = search(query)  # dense retrieval
docs_dict = [{'text': text} for text in results['texts']]
response = co.chat(
    message=query,
    documents=docs_dict
)
print(response.text)
# → "The film generated a worldwide gross of over $677 million, or $773 million with subsequent re-releases."

# Citations are returned automatically:
# citations=[ChatCitation(start=21, end=36, text='worldwide gross', document_ids=['doc_0']), ...]
```

The `documents=` parameter is the API-level signal that the LLM should **ground on these documents only** and **emit citations linking spans of the output back to source documents**. See [[CohereChat]] for the full primitive.

## Worked example: local RAG via LangChain

Ch 8's local replication uses a [[PromptTemplate|prompt template]] with explicit `{context}` injection:

```
<|user|>
Relevant information:
{context}

Provide a concise answer the following question using the relevant information provided above:
{question}<|end|>
<|assistant|>
```

Wired via `RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=db.as_retriever(), chain_type_kwargs={"prompt": prompt})`. The `chain_type='stuff'` parameter is LangChain's name for *"stuff all retrieved docs into a single prompt"* — the simplest of LangChain's retrieval-QA chain types.

The local path **loses span-level citations** — *"we will lose the ability to do span citations and the smaller local model isn't going to work as well as the larger managed model, but it's useful to demonstrate the flow."*

## What grounded generation buys

Per Ch 8: RAG systems *"can be seen as an improvement to generation systems because they reduce their hallucinations and improve their factuality. They also enable use cases of 'chat with my data' that consumers and companies can use to ground an LLM on internal company data, or a specific data source of interest (e.g., chatting with a book)."*

The three structural benefits:

1. **Hallucination mitigation** — retrieved docs anchor the LLM's claims.
2. **Up-to-date answers** — non-parametric memory can be refreshed without retraining.
3. **Private-data use cases** — *"chat with my data"* without leaking weights or context-window contents into a managed model's training set.

## Connections

- [[rag]] — the parent technique family.
- [[GenerativeSearch]] — search engines that end with grounded generation; Ch 8's named examples are [[Perplexity]], Microsoft Bing AI, [[gemini|Gemini]].
- [[CitationGeneration]] — the span-level citation primitive that makes grounded generation verifiable.
- [[Faithfulness]] / [[AnswerRelevance]] — the [[RAGAS|Ragas]] metrics that measure grounded-generation quality.
- [[CitationRecall]] / [[CitationPrecision]] — the [[NelsonFLiu|Liu et al. 2023]] axes that measure citation correctness.
- [[Hallucination]] — the failure mode grounded generation mitigates.
- [[PromptTemplate]] — the substrate for the RAG prompt (`{context}` + `{question}`).
- [[CohereChat]] — the worked managed-API primitive.
- [[LangChain]] — the local-RAG framework (`RetrievalQA.from_chain_type(chain_type='stuff', ...)`).
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
