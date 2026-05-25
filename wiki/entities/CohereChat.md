---
title: "Cohere Chat"
type: entity
tags: [api, endpoint, cohere, rag, grounded-generation, citations]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Cohere Chat

The `co.chat` endpoint of the [[Cohere]] managed API — a chat-completion endpoint with **first-class [[rag|RAG]] support** via a `documents` parameter and **automatic span-level [[CitationGeneration|citations]]** in the response. Ch 8 of *Hands-On LLMs* uses it as the chapter's **managed-RAG primitive**.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

The signature minimal-API receipt:

```python
query = "income generated"
results = search(query)  # dense retrieval over Interstellar Wikipedia
docs_dict = [{'text': text} for text in results['texts']]
response = co.chat(
    message=query,
    documents=docs_dict
)
print(response.text)
# → "The film generated a worldwide gross of over $677 million, or $773 million with subsequent re-releases."
```

The response carries **span-level citations** automatically:

```python
citations=[
    ChatCitation(start=21, end=36, text='worldwide gross', document_ids=['doc_0']),
    ChatCitation(start=40, end=57, text='over $677 million', document_ids=['doc_0']),
    ChatCitation(start=62, end=103, text='$773 million with subsequent re-releases.', document_ids=['doc_0']),
]
documents=[{'id': 'doc_0', 'text': '...'}]
```

This is the **wiki's first runnable demonstration of span-level [[CitationGeneration|citation generation]]** in a RAG response. The `start` / `end` byte offsets into `response.text` plus the `document_ids` back-pointer make each citation **mechanically verifiable** — exactly the property [[NelsonFLiu|Liu]] / Zhang / [[PercyLiang|Liang]] 2023's [[CitationRecall|citation recall]] + [[CitationPrecision|citation precision]] axes measure.

## Position in Cohere's managed-RAG stack

Ch 8 walks the **full Cohere managed-RAG path** as three endpoints in sequence:

| Step | Endpoint | Role |
|---|---|---|
| Embed query + documents | [[CohereEmbed|`co.embed`]] | Dense retrieval substrate |
| Rescore top-k candidates | [[CohereRerank|`co.rerank`]] | Cross-encoder reranking |
| Generate grounded answer + citations | **`co.chat`** | Grounded generation + auto-citation |

This is the canonical three-endpoint managed-RAG receipt — minimal-API equivalent of the LangChain `RetrievalQA` + Phi-3 local-RAG path that Ch 8 also demonstrates (the local path loses the `documents=` citation primitive).

## Connections

- [[Cohere]] — parent API provider.
- [[CohereEmbed]] / [[CohereRerank]] — sibling endpoints in the same managed-RAG stack.
- [[rag]] / [[GroundedGeneration]] — the technique family.
- [[CitationGeneration]] — the span-citation primitive `co.chat` produces.
- [[CitationRecall]] / [[CitationPrecision]] — the [[NelsonFLiu|Liu et al. 2023]] axes the citation primitive supports.
- [[QueryRewriting]] — Cohere's API also has a dedicated query-rewriting mode for `co.chat`.
- [[CommandR]] — Cohere's flagship managed LLM family `co.chat` defaults to.
- [[LangChain]] — the local alternative path Ch 8 also demonstrates.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
