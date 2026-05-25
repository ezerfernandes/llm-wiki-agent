---
title: "Multimodal RAG"
type: concept
tags: [rag, multimodal, retrieval, vision]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Multimodal RAG

**Multimodal RAG** is the [[rag|RAG]] variant in which retrieved context can be **text, image, video, audio, or any combination** — not just text. [[ChipHuyen|Huyen]] introduces it in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] as the natural extension of RAG when the generator is multimodal.

## Two retrieval strategies for images

1. **Metadata-based**: if images have titles, tags, or captions, retrieve by querying those text fields — the standard [[TermBasedRetrieval]] or [[EmbeddingBasedRetrieval]] machinery, just over text metadata.
2. **Content-based via joint embedding**: use a multimodal embedding model like [[CLIP]] to embed both texts and images into a shared space. Huyen's recipe:
   - Generate CLIP embeddings for all data (text + images), store in a [[VectorDatabase]].
   - Given a query (text or image), generate its CLIP embedding.
   - Search the vector DB for nearest neighbors across both modalities.

## The example

> *"Given 'What's the color of the house in the Pixar movie Up?' the retriever can fetch a picture of the house in Up to help the model answer."*

The query is text; the retrieved context includes an image; the multimodal generator answers by inspecting the image. This is only possible because CLIP's text and image embeddings live in the same vector space.

## Connections

- [[rag]] — the parent application.
- [[CLIP]] — the canonical multimodal embedding model.
- [[MultimodalEmbeddingSpace]] — the substrate.
- [[MultimodalLLM]] — the generator family multimodal RAG augments.
- [[EmbeddingBasedRetrieval]] — the retrieval mechanism multimodal RAG uses.
- [[VectorDatabase]] — the storage layer.
- [[ai-engineering-ch06-rag-agents]] — primary source.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 supplies the **worked code** for the CLIP half of [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]'s multimodal-RAG recipe. Where Huyen Ch 6 described the recipe (*"generate CLIP embeddings for all data, store in a vector database, search across modalities"*), Ch 9 walks the runnable encoding step — `CLIPModel.get_text_features(...)` / `CLIPModel.get_image_features(...)` producing `torch.Size([1, 512])` embeddings in the same 512-dim space — and notes that **the four named CLIP applications (zero-shot classification / clustering / search / generation) all reduce to dot-product-in-shared-space**, of which **search** is precisely the operation a multimodal-RAG retriever performs.

The connection chain is now complete in the wiki: Ch 9 produces the embedding → [[VectorDatabase|vector DB]] stores it → [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]'s multimodal-RAG retriever queries it → [[BLIP2|BLIP-2]]-style multimodal LLM (Ch 9 again) generates an answer conditioned on the retrieved image(s). Ch 9 is the **first runnable CLIP encoding step** in the wiki's multimodal-RAG stack.
