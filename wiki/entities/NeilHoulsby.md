---
title: "Neil Houlsby"
type: entity
tags: [person, researcher, peft, adapter]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Neil Houlsby

ML researcher, **first author of the canonical adapter-based [[PEFT|PEFT]] paper** — Houlsby et al. (2019), *"Parameter-Efficient Transfer Learning for NLP."* Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], the paper that **established PEFT as a viable alternative to full finetuning** by showing:

- Inserting two small adapter modules per transformer block (around the attention and FFN sublayers) of a frozen [[bert|BERT]] base.
- Training only the adapters (~3% of BERT's parameters).
- Achieving performance within **0.4% of full finetuning** on [[GLUE]].

## Why this paper anchors Ch 7

The Houlsby 2019 result is what motivated the entire PEFT research line that produced [[lora|LoRA]], [[BitFit]], [[IA3]], [[PrefixTuning]], and the rest. Ch 7 includes Figure 7-8 reproducing the Houlsby et al. adapter architecture.

The paper's downside Ch 7 names: **adapters add inference latency** (extra layers in the forward pass). LoRA later solved this by parametrizing the update so it could be merged back into base weights.

## Affiliation

[[google|Google]] Research at the time of the adapter paper. Has continued work on transfer learning and Vision Transformers ([[ViT]]).

## Other notable work

- Co-author on **ViT (Vision Transformer)** (Dosovitskiy et al. 2020).
- Work on efficient transfer learning across modalities.

## Connections

- [[adapterlayers|Adapter Layers]] / [[PEFT]] — the field he founded.
- [[lora|LoRA]] — successor that addressed adapters' latency overhead.
- [[Houlsby2019AdapterModules]] — the foundational paper.
- [[bert|BERT]] — the base model in the original experiments.
- [[ai-engineering-ch07-finetuning]] — wiki source.
