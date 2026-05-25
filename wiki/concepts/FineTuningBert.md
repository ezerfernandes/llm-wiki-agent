---
title: "Fine-Tuning BERT"
type: concept
tags: [training, nlp, bert, transfer-learning, fine-tuning]
sources: [d2l-nlp-applications, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Fine-Tuning BERT

The recipe — formalized in [[d2l-nlp-applications]] §`finetuning-bert` — for adapting a pretrained [[BERT]] encoder to downstream NLP applications **with minimal architecture changes**: an extra fully-connected head (or two), trained from scratch, while all BERT parameters are also updated end-to-end. The applied-NLP companion to the [[FineTuning|computer-vision fine-tuning recipe]] from [[d2l-computer-vision]].

## Four application templates

| Task type | Input | Head | Examples |
|---|---|---|---|
| **Single-text classification** | `[CLS] text [SEP]` | MLP on [[ClsToken|`[CLS]`]] hidden state | [[SentimentAnalysis|Sentiment]] ([[IMDb]]), grammaticality ([[CoLA]]) |
| **Text-pair classification** | `[CLS] A [SEP] B [SEP]` with segment ids | MLP on `[CLS]` | [[NaturalLanguageInference|NLI]] ([[SNLI]]) |
| **Text-pair regression** | `[CLS] A [SEP] B [SEP]` | Linear regressor on `[CLS]` + MSE loss | [[SemanticTextualSimilarity|STS-B]] |
| **Token-level tagging** | `[CLS] text [SEP]` | Same FC head applied per-token | Part-of-speech tagging, NER |
| **Question answering ([[SQuAD]] v1.1)** | `[CLS] Q [SEP] P [SEP]` | Two independent linear heads on each passage token → start-score $s_i$, end-score $e_i$; predict $\arg\max_{i \le j} s_i + e_j$ | Reading comprehension |

## Training protocol

- **Output-layer parameters** (`net.output`) — random init, **learn from scratch**.
- **Hidden-layer parameters** (`net.hidden` / encoder) — **fine-tune** end-to-end.
- **Stale parameters** — the `MaskLM` and `NextSentencePred` MLPs used only for pretraining loss are *not* updated; their gradients are explicitly allowed to be stale (`ignore_stale_grad=True`).
- **Learning rate**: $1{\times}10^{-4}$ in D2L's worked SNLI example, Adam optimizer, ~5 epochs.
- **Sequence packing for pairs**: `SNLIBERTDataset` joint-truncates to $|p| + |h| \le \text{max\_len} - 3$ (reserving slots for `<CLS>` + 2× `<SEP>`).

## Trade-off

> "BERT requires minimal architecture changes for a wide range of natural language processing applications. However, this benefit comes at the cost of fine-tuning a huge number of BERT parameters for the downstream applications. When space or time is limited, those crafted models based on MLPs, CNNs, RNNs, and attention are more feasible." — [[d2l-nlp-applications]]

For the SNLI worked example, D2L provides a "bert.small" variant (256 hidden / 512 FFN / 2 heads / 2 blocks) so the demo fits on educational hardware; "bert.base" is also available for production-quality results.

## Connections

- [[BERT]] / [[FineTuning]] — base concepts.
- [[ClsToken]] / [[MaskedLanguageModel]] / [[NextSentencePrediction]] / [[WordPiece]] — BERT machinery.
- [[NaturalLanguageInference]] / [[SentimentAnalysis]] / [[QuestionAnswering]] / [[SemanticTextualSimilarity]] — downstream tasks.
- [[SNLI]] / [[IMDb]] / [[SQuAD]] / [[CoLA]] — canonical datasets.
- [[d2l-nlp-applications]] §`finetuning-bert` / §`natural-language-inference-bert` — D2L's canonical worked examples.

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 is the **Hugging Face `Trainer` runnable instantiation** of this template, walking **four regimes** on the same `bert-base-cased` backbone:

| Ch 11 regime | Implementation | Result on Rotten Tomatoes |
|---|---|---|
| Full supervised FT | `AutoModelForSequenceClassification` + [[Trainer]] + [[DataCollatorWithPadding]] | F1 = **0.85** |
| [[LayerFreezing]] (head only) | Above + `param.requires_grad = False` on backbone | F1 = **0.63** |
| [[LayerFreezing]] (blocks 10–11 + head) | Above + `param.requires_grad = False` for index `< 165` | F1 = **0.80** |
| [[SetFit]] (few-shot) | [[ContrastiveLearning|Contrastive]] [[SentenceTransformers|SentenceTransformer]] FT + classifier head | F1 = **0.85** on 32 labels |
| [[ContinuedPretraining]] + FT | [[MaskedLanguageModel|MLM]] adaptation via `AutoModelForMaskedLM` + [[DataCollatorForLanguageModeling]], then the supervised FT row | qualitative shift via [[FillMaskPipeline\|`fill-mask`]] |
| [[NamedEntityRecognition]] (token-level) | `AutoModelForTokenClassification` + [[DataCollatorForTokenClassification]] + [[BIOTagging]] + [[LabelAlignment]] + [[seqeval]] | (the *"token-level tagging"* row of the D2L template above, instantiated end-to-end) |

Ch 11's empirical contribution to the FineTuningBert page: full FT (all params trainable) reaches F1 = 0.85 in **one epoch** with `lr=2e-5`, `batch_size=16`, `weight_decay=0.01` — matching the D2L hyperparameter intuition (BERT fine-tuning works at `~1e-4` to `~2e-5` LRs for a few epochs). Layer-freezing experiments quantify the previously-loose claim that *"upper layers matter more"* — freezing blocks 0–9 leaves block 11 + head as the only trainable parameters and still reaches F1 = 0.80 in one epoch.

> *"Compared to the embedding model approach, we will fine-tune both the representation model and the classification head as a single architecture."* — Ch 11. This is the **task-specific architecture** that differentiates Ch 11 from [[hands-on-llm-ch04-text-classification|Ch 4]]'s frozen approach.

The chapter completes the D2L template's *"token-level tagging"* row with a runnable [[NamedEntityRecognition|NER]] pipeline on [[CoNLL2003|CoNLL-2003]] — using `AutoModelForTokenClassification` + the [[BIOTagging|BIO]] / [[LabelAlignment|subtoken-alignment]] machinery + [[seqeval|span-aware F1]].
