---
title: "Flan-T5"
type: entity
tags: [model, llm, encoder-decoder, instruction-tuned, google]
sources: [hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Flan-T5

[[google|Google's]] instruction-tuned variant of the [[t5|T5]] encoder-decoder family — *"Scaling Instruction-Finetuned Language Models"* (Chung et al., 2022). Combines the [[t5|T5]] architecture and pretraining recipe with **instruction-tuning across 1,800+ tasks** drawn from the FLAN, P3, SuperNaturalInstructions, and Chain-of-Thought collections.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 includes Flan-T5 in the comparative tokenizer tour.

**Tokenization details:**
- **Method**: [[SentencePiece]] (which itself supports both [[BPE]] and the **unigram language model** described in Kudo's *"Subword regularization"*).
- **Vocabulary size**: 32,100.
- **[[SpecialToken|Special tokens]]**:
  - `<unk>` — unknown token.
  - `<pad>` — padding token.
  - `</s>` — end-of-sequence (visible at the end of the chapter's tokenized output).

**Tokenizer behavior observed in Ch 2**:
- **No newline or whitespace tokens** — *"this would make it challenging for the model to work with code."* Flan-T5 is not a code-domain model.
- **`<unk>` blindness** — both the 🎵 emoji and Chinese characters are replaced by `<unk>` tokens. *"making the model completely blind to them."* Unlike [[GPT2|GPT-2]] (byte-fallback BPE), Flan-T5's vocabulary doesn't recover the original Unicode bytes.

## Connections

- [[t5|T5]] — the base model family Flan-T5 is fine-tuned from.
- [[google]] — the publishing organization.
- [[SentencePiece]] — the tokenization method.
- [[HandsOnLLM]] / [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2 surveys Flan-T5's tokenizer.
- Instruction tuning — the training procedure Flan-T5 epitomizes at scale (existing wiki forward-reference convention).
- [[HuggingFace]] — model hub host.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 uses **`google/flan-t5-small`** as the chapter's **open-source [[GenerativeClassification|generative-classification]] demo**:

```python
pipe = pipeline("text2text-generation",
                model="google/flan-t5-small", device="cuda:0")

prompt = "Is the following sentence positive or negative? "
data = data.map(lambda example: {"t5": prompt + example["text"]})

# Output "negative" or "positive" — parse back to 0 / 1
for output in pipe(KeyDataset(data["test"], "t5")):
    text = output[0]["generated_text"]
    y_pred.append(0 if text == "negative" else 1)
```

**Result on [[RottenTomatoes|Rotten Tomatoes]]**: F1 = **0.84** weighted average — *"an amazing first look into the capabilities of generative models."* All five sizes (`small`/`base`/`large`/`xl`/`xxl`) are available; the chapter uses `small` for speed.

The chapter sketches Flan-T5's training as a **two-stage** recipe:
1. **Span-corruption MLM pretraining** ([[t5|T5]]'s objective — mask token *spans*, not individual tokens).
2. **Multi-task instruction-tuning across 1,800+ tasks** (per Chung et al. *"Scaling instruction-finetuned language models"*, 2022). Each task is cast as sequence-to-sequence and trained simultaneously, *"that more closely follow instructions as we know them from GPT models."*

Flan-T5 is the chapter's example of an **encoder-decoder** generative model — visible architecturally (Ch 4 names *"12 decoders and 12 encoders stacked together"* per the T5 paper) and operationally via Hugging Face's `text2text-generation` task type (vs `text-generation` for decoder-only models like Phi-3 / Llama / GPT).

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 uses **`google/flan-t5-small`** as a **local LLM topic-labeling backend** for [[BERTopic]]'s [[GenerativeTopicLabeling|generative representation model]]. The chapter feeds topic keywords + 4 most-representative documents into a `text2text-generation` pipeline with the prompt template:

```
I have a topic that contains the following documents:
[DOCUMENTS]

The topic is described by the following keywords: '[KEYWORDS]'.

Based on the documents and keywords, what is this topic about?
```

Flan-T5's outputs are **mixed quality** — strong on some topics (*"Speech-to-description,"* *"Summarization"*) but prone to overgeneric labels on others (*"Science/Tech"* for medical NLP). The chapter contrasts this with [[ChatGPT|GPT-3.5-turbo]] via the OpenAI API, which produces more descriptive labels (*"Advancements in Aspect-Based Sentiment Analysis"*) at the cost of API key + tokens.

Flan-T5 is thus Ch 5's open-source / local-inference baseline for LLM-based topic labeling — a useful capability ceiling demonstration for the GPU-poor reader.
