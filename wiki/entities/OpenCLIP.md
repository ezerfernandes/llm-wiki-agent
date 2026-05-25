---
title: "OpenCLIP"
type: entity
tags: [model, library, multimodal, embedding, vision-language, open-source, clip]
sources: [hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# OpenCLIP

The **open-source variant of [[CLIP]]** — [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]'s named runnable wrapper for the [[CLIP]] training recipe. *"For our next example, we are going to be using models from the open source variant of CLIP, namely OpenCLIP. Using OpenCLIP, or any CLIP model, boils down to two things: processing the textual and image inputs before passing them to the main model."*

## Worked code recipe (Ch 9)

Loaded via Hugging Face `transformers` against the canonical `openai/clip-vit-base-patch32` checkpoint:

```python
from transformers import CLIPTokenizerFast, CLIPProcessor, CLIPModel
model_id = "openai/clip-vit-base-patch32"
clip_tokenizer = CLIPTokenizerFast.from_pretrained(model_id)
clip_processor = CLIPProcessor.from_pretrained(model_id)
model = CLIPModel.from_pretrained(model_id)
```

Three components:

1. **`CLIPTokenizerFast`** — tokenizes text; wraps with `<|startoftext|>` / `<|endoftext|>`.
2. **`CLIPProcessor`** — preprocesses images (resizes to 224 × 224).
3. **`CLIPModel`** — produces `get_text_features(...)` and `get_image_features(...)`; both return `torch.Size([1, 512])` embeddings in a **shared 512-dim vector space**.

## Worked similarity computation (Ch 9)

```python
text_embedding /= text_embedding.norm(dim=-1, keepdim=True)
image_embedding /= image_embedding.norm(dim=-1, keepdim=True)
score = np.dot(text_embedding, image_embedding.T)
# array([[0.33149648]], dtype=float32)
```

The AI-generated puppy-in-the-snow image paired with the caption *"a puppy playing in the snow"* scores **0.33** — high in CLIP's distribution, even though it looks numerically low.

## Easy-mode wrapper via [[SentenceTransformers|sentence-transformers]]

*"sentence-transformers implements a few CLIP-based models that make it much easier to create embeddings. It only takes a few lines of code:"*

```python
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer("clip-ViT-B-32")
image_embeddings = model.encode(images)
text_embeddings = model.encode(captions)
sim_matrix = util.cos_sim(image_embeddings, text_embeddings)
```

## Connections

- [[hands-on-llm-ch09-multimodal-llms]] — primary source.
- [[CLIP]] — the model OpenCLIP is the open-source counterpart of.
- [[openai]] — author of the original [[CLIP]] training recipe and the `openai/clip-vit-base-patch32` checkpoint name.
- [[HuggingFace]] — host of the worked checkpoint; provides the `CLIPModel` / `CLIPTokenizerFast` / `CLIPProcessor` classes.
- [[SentenceTransformers]] — easy-mode wrapper named in Ch 9.
- [[VisionTransformer]] — the image encoder backbone (`clip-vit-base-patch32`).
- [[ContrastiveLearning]] — the training paradigm.
- [[MultimodalEmbeddingSpace]] — the shared text-image vector space OpenCLIP produces.
