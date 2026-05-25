---
title: "CLIP"
type: concept
tags: [multimodal, embedding, vision-language, openai]
sources: [ai-engineering-ch01-intro, ai-engineering-ch06-rag-agents, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# CLIP

**Contrastive Language-Image Pre-training** — [[openai|OpenAI's]] 2021 multimodal embedding model that produces a **joint embedding space for both images and texts**. The first model that could generalize to many image classification tasks **without requiring task-specific training** (zero-shot). Cited in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] as the foundational multimodal embedding model that paved the way for generative foundation models.

## What's special about CLIP

CLIP is trained with **[[NaturalLanguageSupervision|natural language supervision]]**: instead of manually generating labels for each image, OpenAI harvested **400 million (image, text) pairs** that co-occurred on the internet — **400× larger than [[ImageNet]]**, at zero manual labeling cost.

This dataset enabled CLIP to be the first model that:
- **Generalizes zero-shot** across many image classification tasks.
- Provides a **joint embedding** of images and texts — text-image similarity can be computed by dot product in shared embedding space.

## CLIP is NOT generative

A subtle but important point Huyen emphasizes in Ch 1:

> *"Note that CLIP isn't a generative model — it wasn't trained to generate open-ended outputs. CLIP is an embedding model, trained to produce joint embeddings of both texts and images."*

CLIP outputs vectors, not images or text. It can be **used by** generative models (as a visual encoder), but it itself is not generative.

## CLIP as the backbone of generative multimodal models

Multimodal embedding models like CLIP are **the backbones of generative multimodal models**: Flamingo, [[LLaVA15|LLaVA]], and [[gemini|Gemini]] (previously [[bard|Bard]]) all use CLIP-style visual encoders to project images into a token-like embedding space that an LLM can attend over.

## Connections

- [[openai|OpenAI]] — developer.
- [[NaturalLanguageSupervision]] — the training paradigm CLIP pioneered.
- [[SelfSupervision]] — the parent paradigm.
- [[FoundationModel]] / [[MultimodalLLM]] — downstream architectures.
- [[ImageNet]] — the supervised counterexample CLIP outperforms zero-shot.
- [[LLaVA15]] / [[gemini]] — generative multimodal models that use CLIP-style backbones.
- [[ai-engineering-ch01-intro]] — primary source for the Ch 1 framing.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

Ch 6 re-engages CLIP as the **canonical retriever backbone for [[MultimodalRAG|multimodal RAG]]**. The three-step receipt:

1. Generate CLIP embeddings for all data (text + images), store in a [[VectorDatabase|vector database]].
2. Given a query, generate its CLIP embedding.
3. Query the vector database for all images and texts whose embeddings are close to the query embedding.

The structural reason CLIP enables multimodal RAG: **shared embedding space for text and images**. A text query can retrieve image neighbors and vice versa because both modalities project into the same vector space. Without a CLIP-style joint embedding, multimodal RAG would require modality-specific retrievers and a separate cross-modal fusion step.

Worked Ch 6 example: *"Given 'What's the color of the house in the Pixar movie Up?' the retriever can fetch a picture of the house in Up to help the model answer."*

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 is the wiki's first **runnable** CLIP receipt. The chapter canonizes CLIP as the field's reference multimodal embedding model — *"the most well-known and currently most-used model"* — and walks the **training procedure** decomposed into three figures:

1. **Encode image and text separately.** *"CLIP uses a text encoder to embed text and an image encoder to embed images. ... the result is an embedding for both the image and its corresponding caption."*
2. **Compare via [[CosineSimilarity|cosine similarity]].** *"The pair of embeddings that are generated are compared through cosine similarity ... the cosine of the angle between vectors, which is calculated through the dot product of the embeddings and divided by the product of their lengths."*
3. **Update encoders to optimize the similarity** — *"maximize them for similar image/caption pairs and minimize them for dissimilar image/caption pairs"* — this is **[[ContrastiveLearning|contrastive learning]]**, walked end-to-end in [[hands-on-llm-ch10-creating-text-embedding-models|Ch 10]].

**Four named CLIP applications**: [[ZeroShotClassification|zero-shot classification]], clustering, search (text→image or image→text), and **generation** (driving [[StableDiffusion|stable diffusion]]).

### The CLIP `[CLS]` convention inversion

A wiki-novel observation: in CLIP, the `[CLS]` token represents the **image embedding**, not the text embedding (the inverse of [[bert|BERT]]'s convention). *"In CLIP, the [CLS] token is actually used to represent the image embedding."*

### Worked code via [[OpenCLIP]]

Ch 9 uses `openai/clip-vit-base-patch32` via Hugging Face `transformers`:

```python
from transformers import CLIPTokenizerFast, CLIPProcessor, CLIPModel
clip_tokenizer = CLIPTokenizerFast.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
text_embedding = model.get_text_features(...)   # torch.Size([1, 512])
image_embedding = model.get_image_features(...) # torch.Size([1, 512])
```

Both text and image embeddings live in the same **512-dim** space; images are preprocessed to **224 × 224 pixels**. The worked AI-generated puppy-in-the-snow image + caption *"a puppy playing in the snow"* normalizes-and-dot-products to similarity **0.33** — the highest in the 3×3 similarity matrix Ch 9 builds.

Ch 9 also names the easy-mode wrapper via [[SentenceTransformers|sentence-transformers]]: `SentenceTransformer("clip-ViT-B-32")`.

### CLIP's wider role in Ch 9

The chapter then **uses CLIP-style encoders** as the [[ImageEncoder|frozen image encoder]] for [[BLIP2|BLIP-2]] / [[LLaVA15|LLaVA]] / [[Idefics2|Idefics-2]] — adapter-style [[MultimodalLLM|multimodal LLMs]] that *"connect pretrained CLIP-like visual encoders with textual LLMs."* Ch 9 establishes CLIP as **both** the canonical multimodal embedding model **and** the backbone whose representations downstream adapter-LLMs bridge to language models.
