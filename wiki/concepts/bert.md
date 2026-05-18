---
title: "BERT"
type: concept
tags: [concept, model, transformer, pretraining]
sources: [1810.04805-bert, d2l-nlp-pretraining, d2l-nlp-applications]
last_updated: 2026-05-16
---

# BERT

**Bidirectional Encoder Representations from Transformers** (Devlin et al., 2018) — a Transformer encoder pre-trained on BooksCorpus + English Wikipedia with two unsupervised objectives, [[MaskedLanguageModel]] and [[NextSentencePrediction]], then fine-tuned end-to-end with a single extra output layer for downstream tasks. Two sizes: BERT_BASE (110M) and BERT_LARGE (340M).

Introduced in [[1810.04805-bert]]. Along with [[1706.03762-attention-is-all-you-need]], one of the two papers that define the modern pre-train-then-finetune NLP paradigm. Subsequent decoder-style LLMs (GPT-family) generalize BERT's recipe by replacing the encoder + MLM with a causal decoder + next-token prediction. [[1910.10683-t5]] generalizes BERT in a different direction: keeping the bidirectional encoder but adding a decoder, replacing [[maskedlanguagemodel]] with [[spancorruption]] (shorter targets, faster training), and unifying *all* downstream tasks via the [[texttotextframework]] rather than per-task heads.

## Key facts
- Multi-layer bidirectional Transformer **encoder** — unlike GPT (left-only decoder) and ELMo (shallow concat of independent L-R / R-L LSTMs), every layer of BERT jointly conditions on left and right context.
- Input representation = token + segment + positional embeddings, summed; `[CLS]` at position 0 serves as the aggregate sequence vector; `[SEP]` separates segment A from segment B.
- Same pre-trained weights transfer to sentence-pair classification, single-sentence classification, span prediction (SQuAD), and sequence tagging (NER) — only the output head changes.
- [[d2l-nlp-applications]] §`finetuning-bert` operationalizes this template into four worked categories — single-text classification ([[SentimentAnalysis]] / [[CoLA]]), text-pair classification ([[NaturalLanguageInference|NLI]] on [[SNLI]]), text-pair regression ([[SemanticTextualSimilarity|STS-B]]), text tagging (POS), and span prediction ([[QuestionAnswering]] on [[SQuAD]]). See [[FineTuningBert]].
