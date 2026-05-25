---
title: "BERT"
type: concept
tags: [concept, model, transformer, pretraining]
sources: [1810.04805-bert, d2l-nlp-pretraining, d2l-nlp-applications, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch04-text-classification, hands-on-llm-ch09-multimodal-llms, hands-on-llm-ch10-creating-text-embedding-models, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# BERT

**Bidirectional Encoder Representations from Transformers** (Devlin et al., 2018) — a Transformer encoder pre-trained on BooksCorpus + English Wikipedia with two unsupervised objectives, [[MaskedLanguageModel]] and [[NextSentencePrediction]], then fine-tuned end-to-end with a single extra output layer for downstream tasks. Two sizes: BERT_BASE (110M) and BERT_LARGE (340M).

Introduced in [[1810.04805-bert]]. Along with [[1706.03762-attention-is-all-you-need]], one of the two papers that define the modern pre-train-then-finetune NLP paradigm. Subsequent decoder-style LLMs (GPT-family) generalize BERT's recipe by replacing the encoder + MLM with a causal decoder + next-token prediction. [[1910.10683-t5]] generalizes BERT in a different direction: keeping the bidirectional encoder but adding a decoder, replacing [[maskedlanguagemodel]] with [[spancorruption]] (shorter targets, faster training), and unifying *all* downstream tasks via the [[texttotextframework]] rather than per-task heads.

## Key facts
- Multi-layer bidirectional Transformer **encoder** — unlike GPT (left-only decoder) and ELMo (shallow concat of independent L-R / R-L LSTMs), every layer of BERT jointly conditions on left and right context.
- Input representation = token + segment + positional embeddings, summed; `[CLS]` at position 0 serves as the aggregate sequence vector; `[SEP]` separates segment A from segment B.
- Same pre-trained weights transfer to sentence-pair classification, single-sentence classification, span prediction (SQuAD), and sequence tagging (NER) — only the output head changes.
- [[d2l-nlp-applications]] §`finetuning-bert` operationalizes this template into four worked categories — single-text classification ([[SentimentAnalysis]] / [[CoLA]]), text-pair classification ([[NaturalLanguageInference|NLI]] on [[SNLI]]), text-pair regression ([[SemanticTextualSimilarity|STS-B]]), text tagging (POS), and span prediction ([[QuestionAnswering]] on [[SQuAD]]). See [[FineTuningBert]].

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

[[JayAlammar|Alammar]] and [[MaartenGrootendorst|Grootendorst]] position BERT in Ch 1 as **the canonical [[RepresentationModel|representation model]]** — the encoder-only template that, paired with [[GPT|GPT]] (the decoder-only [[GenerativeModel|generative model]] template), defines the central architectural split in the modern LLM tree.

> "In 2018, a new architecture called Bidirectional Encoder Representations from Transformers (BERT) was introduced that could be leveraged for a wide variety of tasks and would serve as the foundation of Language AI for years to come. BERT is an encoder-only architecture that focuses on representing language." — Ch 1

Ch 1 emphasizes:

- **BERT-base has 12 encoders** (per Figure 1-21 caption).
- The **`[CLS]` token** at position 0 serves as the sequence-level representation; *"often, we use this `[CLS]` token as the input embedding for fine-tuning the model on specific tasks, like classification."*
- BERT's training procedure is **[[maskedlanguagemodel|masked language modeling]]** — mask a fraction of input tokens; predict them from surrounding context. *"This prediction task is difficult but allows BERT to create more accurate (intermediate) representations of the input."*
- The book's permissive LLM definition includes BERT — *"the term LLM is not only reserved for generative models (decoder-only) but also representation models (encoder-only)."*

Ch 1 also flags BERT's role as a **[[TransferLearning|transfer-learning]] vehicle**: pretrain on the entirety of Wikipedia for language modeling, then fine-tune for downstream tasks like text classification. *"A huge benefit of pretrained models is that most of the training is already done for us. Fine-tuning on specific tasks is generally less compute-intensive and requires less data."*

And as a **feature-extraction machine**: *"BERT models generate embeddings at almost every step in their architecture. This also makes BERT models feature extraction machines without the need to fine-tune them on a specific task."*

The chapter forward-references BERT-like models throughout the book — Ch 4 (classification), Ch 5 (clustering), Ch 8 (semantic search), Ch 11 (fine-tuning representation models).

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]] (tokenizer details)

Ch 2 surveys BERT's tokenizer in both its **uncased** and **cased** variants as the canonical [[WordPiece]] example:

| Variant | Year | Vocabulary | Notable behavior |
|---|---|---|---|
| BERT-base **uncased** | 2018 | 30,522 | Lowercases all input; drops newlines; `[UNK]` for emoji/Chinese; `##` for continuation pieces |
| BERT-base **cased** | 2018 | 28,996 | Preserves case (`CAPITALIZATION` → 8 tokens: `CA ##PI ##TA ##L ##I ##Z ##AT ##ION`) |

**Five [[SpecialToken|special tokens]]** Ch 2 enumerates:
- `[UNK]` ([[UnkToken|unknown]])
- `[SEP]` ([[SepToken|separator]] — for sentence pairs, e.g. cross-encoder reranking)
- `[PAD]` ([[PadToken|padding]])
- `[CLS]` ([[ClsToken|classification]] / aggregate-sequence token)
- `[MASK]` ([[MaskToken|masking]] for MLM pretraining)

The chapter notes: *"Both BERT tokenizers wrap the input within a starting `[CLS]` token and a closing `[SEP]` token."* This input-format convention is inherited by every BERT-family encoder (and the [[deberta|DeBERTa]] worked example in Ch 2's contextualized-embedding section uses the same `[CLS] ... [SEP]` wrap).

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 frames the **BERT family** as the canonical [[TaskSpecificModel|task-specific representation-model]] substrate for text classification, listing six baselines worth trying off the [[HuggingFace|Hugging Face]] Hub:

- BERT base (uncased)
- [[RoBERTa]] base
- [[DistilBERT]] base (uncased)
- [[DeBERTa]] base
- bert-tiny
- [[ALBERT]] base v2

> "BERT, a well-known encoder-only architecture, is a popular choice for creating task-specific and embedding models. While generative models, like the GPT family, are incredible models, encoder-only models similarly excel in task-specific use cases and tend to be significantly smaller in size." — Ch 4

The chapter's task-specific demo uses [[TwitterRoBERTa|`cardiffnlp/twitter-roberta-base-sentiment-latest`]] — a BERT-family RoBERTa fine-tuned on tweets for 3-class sentiment. The embedding-model demo uses [[AllMPNetBaseV2|`all-mpnet-base-v2`]], built on Microsoft's MPNet (another BERT-family encoder). Both are kept **frozen** at inference time — the alternative to fine-tuning (Ch 11's subject).

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 records the wiki's first **CLIP-vs-BERT `[CLS]` convention contrast**: where BERT's `[CLS]` token is the **text-side aggregator** (the universal sequence-level handle BERT was designed around), [[CLIP]] **inverts this convention** — *"in CLIP, the [CLS] token is actually used to represent the image embedding, not the text embedding."* This is not a contradiction with BERT's convention; it is a CLIP-specific override that the wiki now flags on [[ClsToken]]. BERT's convention remains canonical inside the text-only Transformer family; CLIP repurposes the special token to the image branch because in CLIP's vision-language setting the `[CLS]` aggregator role has migrated to the [[VisionTransformer|ViT]] side.

## From [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 uses **`bert-base-uncased` as the train-from-scratch base** for the chapter's loss-function ladder. Every from-scratch run in Ch 10 starts with `SentenceTransformer('bert-base-uncased')` — softmax loss → 0.59, cosine loss → 0.72, MNR loss → 0.80, [[AugmentedSBERT]] → 0.71, [[TSDAE]] → 0.70 STS-B Pearson cosine. The chapter notes `microsoft/mpnet-base` is an equally-valid alternative as a sentence-embedding starting point.

Ch 10 also codifies the **structural reason BERT is insufficient for sentence embeddings without additional training**: per the Sentence-BERT paper (Reimers & Gurevych 2019) cited in Ch 10, *"a solution to this overhead is to generate embeddings from a BERT model by averaging its output layer or using the [CLS] token. This, however, has shown to be worse than simply averaging word vectors, like GloVe."* In other words, **pretrained BERT's `[CLS]` and mean-pooled outputs are NOT good sentence embeddings out of the box** — contrastive fine-tuning ([[SBERTArchitecture|SBERT]]) is required to make BERT's embeddings useful for sentence similarity.

The Ch 10 use of [[CrossEncoder|cross-encoders]] in [[AugmentedSBERT]] also leans on `bert-base-uncased`: *"we train our cross-encoder ... `CrossEncoder('bert-base-uncased', num_labels=2)`"*. Same base model, different architectural use — joint encoding for cross-encoder, siamese encoding for bi-encoder.

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 is the wiki's **canonical runnable fine-tuning chapter for BERT** — `bert-base-cased` on the same Rotten Tomatoes / CoNLL-2003 datasets across four fine-tuning regimes. The chapter dissects BERT's architecture at the `model.named_parameters()` level for the [[LayerFreezing|layer-freezing]] experiments:

```
bert.embeddings.word_embeddings.weight
bert.embeddings.position_embeddings.weight
bert.embeddings.token_type_embeddings.weight
bert.embeddings.LayerNorm.weight / .bias
bert.encoder.layer.0.attention.self.query.weight / .bias
...
bert.encoder.layer.11.output.LayerNorm.weight / .bias
bert.pooler.dense.weight / .bias
classifier.weight / .bias
```

12 encoder blocks (indices 0–11), each with `attention.self.{query,key,value}` + `attention.output` + `intermediate.dense` + `output.dense` + 2× LayerNorm. On top: a `pooler` (the pooled-`[CLS]` dense layer) and the task-specific `classifier` head.

**Encoder block 11 starts at parameter index 165** in `named_parameters()` — Ch 11's freezing code uses `if index < 165: param.requires_grad = False` to keep only block 11 + pooler + classifier trainable.

Ch 11's four uses of BERT:

| `bert-base-cased` model class | Use case | Ch 11 regime |
|---|---|---|
| `AutoModelForSequenceClassification` | Document classification | Regimes 1, 2 (full FT & layer-frozen FT) |
| `AutoModelForMaskedLM` | [[ContinuedPretraining|Continued pretraining]] via MLM | Regime 4 |
| `AutoModelForTokenClassification` | NER on CoNLL-2003 | Regime 5 |
| (via [[SentenceTransformers]] / [[AllMPNetBaseV2]]) | Embedding model for [[SetFit]] | Regime 3 |

Ch 11 is the **runnable demonstration of the four-template `FineTuningBert` recipe** — single-text classification (regimes 1/2), token-level tagging (regime 5), and now (new for the wiki) **continued-pretraining as a self-supervised pre-stage** (regime 4) and **few-shot via contrastive sentence-pair fine-tuning of a SentenceTransformer wrapper** (regime 3, SetFit).
