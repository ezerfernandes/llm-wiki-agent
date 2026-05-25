---
title: "Multimodal Embedding Space"
type: concept
tags: [embeddings, multimodal, nlp]
sources: [ai-engineering-ch03-evaluation-methodology, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Multimodal Embedding Space

A **joint [[Embedding|embedding]] space** in which data from different modalities — text, images, audio, 3D point clouds — are projected into the same vector space, so that the embedding of an image and the embedding of a caption describing that image are close. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "A joint embedding space that can represent data of different modalities is a multimodal embedding space. In a text–image joint embedding space, the embedding of an image of a man fishing should be closer to the embedding of the text 'a fisherman' than the embedding of the text 'fashion show'."

## Three named models (Ch 3)

| Model | Modalities | Year |
|---|---|---|
| [[CLIP]] | text + image | 2021 |
| [[ULIP]] | text + image + 3D point clouds | 2022 |
| [[ImageBind]] | 6 modalities (text, image, audio, depth, thermal, IMU) | 2023 |

## CLIP architecture (Ch 3 description)

CLIP is trained on (image, text) pairs where the text is the caption or comment associated with the image. A text encoder produces a text embedding; an image encoder produces an image embedding; both are projected into the joint space. The training objective: get the embedding of an image close to the embedding of its corresponding text.

## What it enables

- **Text-based image search** — embed the query text, retrieve the nearest images.
- **Image-based text retrieval** — embed the image, retrieve the nearest captions/labels.
- **Cross-modal classification** (zero-shot ImageNet via CLIP).
- **Cross-modal evaluation** — judge image-text alignment without per-modality reference data.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[Embedding]] — parent concept.
- [[CLIP]] / [[ULIP]] / [[ImageBind]] — the three named multimodal-embedding models.
- [[SemanticSimilarity]] — the metric this space enables for cross-modal data.
- [[CosineSimilarity]] — the standard score function.
- [[NaturalLanguageSupervision]] — how CLIP was trained.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 is the wiki's **first runnable concretization** of this concept — where the [[ai-engineering-ch03-evaluation-methodology|Huyen Ch 3]] treatment was discipline-level framing, Ch 9 walks the code that produces a shared space and queries it:

```python
from transformers import CLIPModel, CLIPTokenizerFast, CLIPProcessor
model_id = "openai/clip-vit-base-patch32"
clip_tokenizer = CLIPTokenizerFast.from_pretrained(model_id)
clip_processor = CLIPProcessor.from_pretrained(model_id)
model = CLIPModel.from_pretrained(model_id)
# Both branches produce torch.Size([1, 512]) embeddings in the same 512-dim space.
```

Ch 9 names **four applications** of multimodal embedding spaces operationalized by [[CLIP]]:

1. **[[ZeroShotClassification|Zero-shot classification]]** — compare an image's embedding to the embeddings of class descriptions (`"a photo of a <label>"`); pick the highest cosine similarity.
2. **Clustering** — cluster both images and keywords; keywords closest to a cluster's centroid serve as captions.
3. **Search** — text → images or image → texts across billions of items (the [[MultimodalRAG|multimodal-RAG]] backbone).
4. **Generation** — drive image generation as in [[StableDiffusion|Stable Diffusion]] (Rombach et al. 2022).

Ch 9 also operationalizes the **0.33 puppy-snow similarity score** as the demonstration of what *"high"* looks like in CLIP's distribution — even though the absolute number sounds low. *"This similarity score is difficult to interpret because we have no reference point to compare it to."* Reading similarity matrices comparatively rather than absolutely is the practical discipline this concept requires.
