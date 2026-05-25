---
title: "Hands-On LLMs Ch 11 — Fine-Tuning Representation Models for Classification"
type: source
tags: [book, hands-on-llm, oreilly, llm, fine-tuning, bert, classification, supervised-learning, sequence-classification, token-classification, named-entity-recognition, ner, setfit, few-shot, contrastive-learning, masked-language-modeling, continued-pretraining, domain-adaptation, layer-freezing, data-collator, trainer, huggingface]
date: 2024-01-01
source_file: raw/books/hands-on-llm/ch11-fine-tuning-representation-models.md
book: "Hands-On Large Language Models"
book_isbn13: "9781098150969"
book_authors: ["Jay Alammar", "Maarten Grootendorst"]
book_publisher: "O'Reilly Media"
book_year: 2024
---

# Hands-On LLMs Ch 11 — Fine-Tuning Representation Models for Classification

## Summary

The eleventh chapter of [[JayAlammar|Jay Alammar]] and [[MaartenGrootendorst|Maarten Grootendorst]]'s *Hands-On Large Language Models* ([[OReilly|O'Reilly Media]], 2024, ISBN 978-1-098-15096-9) and the **second chapter of Part III ("Training and Fine-Tuning Language Models")**. Where [[hands-on-llm-ch10-creating-text-embedding-models|Ch 10]] taught how to *train* embedding models with [[ContrastiveLearning|contrastive learning]], Ch 11 teaches how to **fine-tune representation models (BERT-class encoders) for classification tasks** — the runnable-code resolution of [[hands-on-llm-ch01-introduction-to-llms|Ch 1]]'s *"we forward-reference Ch 11 for fine-tuning representation models"* promise and the **task-specific deepening of [[hands-on-llm-ch04-text-classification|Ch 4]]** which had used frozen pretrained models without weight updates.

The chapter is organized around **four fine-tuning regimes** for [[bert|BERT]]-class encoders, each motivated by a different data-availability or domain-mismatch constraint:

1. **Supervised classification fine-tuning** (full fine-tuning of `bert-base-cased` on [[RottenTomatoes|rotten_tomatoes]]) — the baseline recipe: load `AutoModelForSequenceClassification`, attach a randomly-initialized classification head, train both the backbone and the head end-to-end via Hugging Face `Trainer`. **F1 = 0.85** in one epoch (~minutes), beating Ch 4's frozen task-specific model (F1 = 0.80).
2. **[[LayerFreezing|Layer freezing]]** variants on the same task — freeze everything except the classification head (F1 = **0.63**, much faster but worse), then freeze only encoder blocks 0–9 leaving blocks 10–11 + classification head trainable (F1 = **0.80**). The chapter's empirical finding: *"training only the first five encoder blocks ... is enough to almost reach the performance of training all encoder blocks"* — diminishing returns up the stack.
3. **[[SetFit|SetFit]] for few-shot classification** (Tunstall et al. 2022, arXiv:2209.11055) — when only a handful of labels per class are available, generate positive/negative sentence-pair training data from in-class / out-class selection, fine-tune a [[SentenceTransformers|SentenceTransformer]] via [[ContrastiveLearning|contrastive learning]], train a classification head (default: scikit-learn [[LogisticRegression|logistic regression]]) on the resulting embeddings. **F1 = 0.85 on 32 labeled examples** (16 per class), matching the full-data baseline.
4. **[[ContinuedPretraining|Continued pretraining]] with [[MaskedLanguageModel|masked language modeling]]** — inject a domain-adaptation stage *between* generic pretraining and task fine-tuning: load `AutoModelForMaskedLM`, run [[MLM]] on the target-domain raw text via `DataCollatorForLanguageModeling` (15% token masking; whole-word masking optionally available via `DataCollatorForWholeWordMask`), then fine-tune the adapted model on the classification task. Demonstrated qualitatively by `fill-mask` on *"What a horrible [MASK]!"*: base BERT predicts generic words (`idea`, `dream`, `day`); MLM-adapted BERT predicts movie-specific words (`movie`, `film`, `mess`, `comedy`).

The chapter then pivots from document-level to **token-level classification** for **[[NamedEntityRecognition|named-entity recognition]] (NER)** on [[CoNLL2003|CoNLL-2003]] — a structurally distinct fine-tuning task where the model predicts a label *per token* rather than per document. Key mechanical differences vs document classification: use `AutoModelForTokenClassification` instead of `AutoModelForSequenceClassification`; use `DataCollatorForTokenClassification` instead of `DataCollatorWithPadding`; align word-level labels with subword tokens via a custom `align_labels` function (first subtoken of a word inherits the word's label with `B-` prefix; subsequent subtokens get the `I-` continuation prefix; `[CLS]` / `[SEP]` / padding get `-100` to be ignored in the loss); use [[seqeval|`seqeval`]] for token-level F1 evaluation. The **[[BIOTagging|BIO (Beginning / Inside / Outside) tagging scheme]]** is introduced here as the standard for marking entity-span boundaries.

The four regimes together form a **decision tree for representation-model fine-tuning**:

| Constraint | Regime | Recipe |
|---|---|---|
| Have plenty of labeled data | Full supervised fine-tuning | `AutoModelForSequenceClassification` + `Trainer` |
| Have plenty of labeled data but limited compute | Layer freezing | Same as above with `param.requires_grad = False` on early blocks |
| Have only a few labels per class | SetFit | Contrastive sentence-pair fine-tuning + classification head |
| Have a domain mismatch (medical / legal / specialized) | Continued pretraining + fine-tuning | `AutoModelForMaskedLM` + MLM stage, then fine-tune |
| Need per-token (not per-document) classification | Token classification | `AutoModelForTokenClassification` + BIO tagging + `seqeval` |

The chapter closes by forward-referencing Ch 12 for **fine-tuning generative models** (instruction fine-tuning + preference alignment via [[rlhf|RLHF]] / [[DPO]]) — the parallel chapter for the generative-model branch.

## Key Claims

### The supervised-classification baseline

- **Fine-tuning beats frozen pretrained models when data is sufficient.** *"If we have sufficient data, fine-tuning tends to lead to some of the best-performing models possible."* Ch 4's frozen task-specific [[TwitterRoBERTa]] hit F1 = 0.80 on Rotten Tomatoes; Ch 11's one-epoch fine-tuned `bert-base-cased` hits **F1 = 0.85** — *"It only costs us a couple of minutes to train."*
- **The architecture: pretrained backbone + classification head, trained jointly.** *"Compared to the embedding model approach, we will fine-tune both the representation model and the classification head as a single architecture. ... In practice, this means that the pretrained BERT model and the classification head are updated jointly. Instead of independent processes, they learn from one another and allow for more accurate representations."*
- **Backward pass starts at the classification head and propagates through BERT.** *"A backward pass will start at the classification head and go through BERT."* Standard joint-training mechanics.

### The Hugging Face `Trainer` API

- **`Trainer` encapsulates the training loop and lets you focus on hyperparameters.** Ch 11 uses `transformers.TrainingArguments` to declare hyperparameters and `transformers.Trainer` to execute the loop:

  ```python
  training_args = TrainingArguments(
     "model",
     learning_rate=2e-5,
     per_device_train_batch_size=16,
     per_device_eval_batch_size=16,
     num_train_epochs=1,
     weight_decay=0.01,
     save_strategy="epoch",
     report_to="none"
  )

  trainer = Trainer(
     model=model,
     args=training_args,
     train_dataset=tokenized_train,
     eval_dataset=tokenized_test,
     tokenizer=tokenizer,
     data_collator=data_collator,
     compute_metrics=compute_metrics,
  )
  trainer.train()
  ```

- **The chapter's default hyperparameters** for BERT fine-tuning on Rotten Tomatoes: `learning_rate=2e-5`, `batch_size=16`, `num_epochs=1`, `weight_decay=0.01`. (For the MLM continued-pretraining run: same `lr` and `batch_size`, but `num_epochs=10`.)
- **`DataCollator` builds batches and may also apply data augmentation.** *"A DataCollator is a class that helps us build batches of data but also allows us to apply data augmentation."* The three variants used in the chapter: [[DataCollatorWithPadding]] (pad to longest in batch — for classification), [[DataCollatorForLanguageModeling]] (random token masking — for MLM), [[DataCollatorForTokenClassification]] (token-aligned padding — for NER).
- **`compute_metrics` lets you track any metric during training.** Ch 11's classification example computes F1 via `evaluate`/`load_metric("f1")`:

  ```python
  def compute_metrics(eval_pred):
      logits, labels = eval_pred
      predictions = np.argmax(logits, axis=-1)
      load_f1 = load_metric("f1")
      f1 = load_f1.compute(predictions=predictions, references=labels)["f1"]
      return {"f1": f1}
  ```

  *"This is especially helpful during training as it allows for detecting overfitting behavior."*

### Layer freezing

- **You can freeze layers selectively to trade quality for speed.** *"We could choose to only freeze certain layers to speed up computing but still allow the main model to learn from the classification task."*
- **Standard idiom**: iterate over `model.named_parameters()` and set `param.requires_grad = False` on what you want frozen.
- **General rule**: *"Generally, we want frozen layers to be followed by trainable layers."* Don't sandwich frozen layers between trainable layers.
- **`bert-base-cased`'s structure**: 12 encoder blocks (indices 0–11) of `attention.self.{query,key,value}` + `attention.output` + `intermediate.dense` + `output.dense` + 2× LayerNorm, on top of an embedding stack (`word_embeddings` + `position_embeddings` + `token_type_embeddings` + LayerNorm), followed by a `pooler` and a `classifier`. Encoder block 11's parameters start at index 165 across `named_parameters()` — Ch 11's code freezes indices `< 165` to keep only block 11 + classifier trainable.
- **Empirical F1 ladder on Rotten Tomatoes (1 epoch)**: all-trainable = **0.85**; freeze-everything-but-head = **0.63**; freeze-blocks-0–9 (train 10–11 + head) = **0.80**.
- **Diminishing returns up the stack.** *"Training only the first five encoder blocks (red vertical line) is enough to almost reach the performance of training all encoder blocks."* (Figure 11-7.)
- **Compute / quality trade-off scales with epochs.** *"When you are training for multiple epochs, the difference (in training time and resources) between freezing and not freezing often becomes larger."*

### SetFit (few-shot classification)

- **SetFit fine-tunes a SentenceTransformer with contrastive learning when labels are scarce.** *"To perform few-shot text classification, we use an efficient framework called SetFit. It is built on top of the architecture of sentence-transformers to generate high-quality textual representations that are updated during training. Only a few labeled examples are needed for this framework to be competitive with fine-tuning a BERT-like model on a large, labeled dataset."* Reference: Lewis Tunstall et al. *"Efficient few-shot learning without prompts,"* arXiv:2209.11055 (2022).
- **Three-step algorithm**:
  1. **Sampling training data** — *"Based on in-class and out-class selection of labeled data it generates positive (similar) and negative (dissimilar) pairs of sentences."* Same-class pairs become positives, cross-class pairs become negatives.
  2. **Fine-tuning embeddings** — *"Fine-tuning a pretrained embedding model based on the previously generated training data,"* via [[ContrastiveLearning|contrastive learning]] on the generated pairs.
  3. **Training a classifier** — *"Create a classification head on top of the embedding model and train it using the previously generated training data."* Default: scikit-learn logistic regression.
- **Pair-generation math.** *"When we have 16 sentences about sports, we can create 16 * (16 – 1) / 2 = 120 pairs that we label as positive pairs."* Combinatorial expansion is what makes few-shot viable — 32 labeled sentences → 1,280 generated pairs (20 pair-combinations × 32 samples × 2 [positive + negative]).
- **The worked recipe**:

  ```python
  from setfit import sample_dataset, SetFitModel
  from setfit import TrainingArguments as SetFitTrainingArguments
  from setfit import Trainer as SetFitTrainer

  sampled_train_data = sample_dataset(tomatoes["train"], num_samples=16)
  model = SetFitModel.from_pretrained("sentence-transformers/all-mpnet-base-v2")

  args = SetFitTrainingArguments(num_epochs=3, num_iterations=20)
  args.eval_strategy = args.evaluation_strategy

  trainer = SetFitTrainer(
      model=model, args=args,
      train_dataset=sampled_train_data,
      eval_dataset=test_data, metric="f1"
  )
  trainer.train()
  trainer.evaluate()  # {'f1': 0.8363988383349468}
  ```

- **32 labels → F1 = 0.85.** *"With only 32 labeled documents, we get an F1 score of 0.85. ... in Chapter 2, we got the same performance but instead trained a logistic regression model on the embeddings of the full data. Thus, this pipeline demonstrates the potential of taking the time to label just a few instances."*
- **Differentiable head as alternative.** Default head is logistic regression; for a differentiable head:

  ```python
  model = SetFitModel.from_pretrained(
      "sentence-transformers/all-mpnet-base-v2",
      use_differentiable_head=True,
      head_params={"out_features": num_classes},
  )
  ```

- **SetFit also supports zero-shot.** *"SetFit generates synthetic examples from the label names to resemble the classification task and then trains a SetFit model on them. For example, if the target labels are 'happy' and 'sad,' then synthetic data could be 'The example is happy' and 'This example is sad.'"*

### Continued pretraining with masked language modeling

- **The three-stage pipeline.** *"Instead of adopting this two-step approach [pretrain + fine-tune], we can squeeze another step between them, namely continue pretraining an already pretrained BERT model."* The lineage example: general BERT → BioBERT (continued pretraining on medical text) → fine-tuned BioBERT for medication classification.
- **Continued pretraining helps when domain vocabulary diverges.** *"The pretrained model is often trained on very general data, like Wikipedia pages, and might not be tuned to your domain-specific words. ... This will update the subword representations to be more tuned toward words it would not have seen before."*
- **Continuing pretraining improves downstream classification.** *"Continuing pretraining on a pretrained BERT model has been shown to improve the performance of models in classification tasks and is a worthwhile addition to the fine-tuning pipeline."* Reference: Chi Sun et al. *"How to fine-tune BERT for text classification?"* CCL 2019.
- **The MLM recipe**:

  ```python
  from transformers import AutoModelForMaskedLM, DataCollatorForLanguageModeling

  model = AutoModelForMaskedLM.from_pretrained("bert-base-cased")
  tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

  data_collator = DataCollatorForLanguageModeling(
      tokenizer=tokenizer,
      mlm=True,
      mlm_probability=0.15
  )

  # Remove the labels — MLM is self-supervised
  tokenized_train = tokenized_train.remove_columns("label")
  ```

  Train for ~10 epochs, save the model to a directory (`model.save_pretrained("mlm")`), then load it with `AutoModelForSequenceClassification.from_pretrained("mlm", num_labels=2)` for the downstream classification fine-tune.

- **Token masking vs whole-word masking.** *"With token masking, we randomly mask 15% of the tokens in a sentence. It might happen that part of a word will be masked. To enable masking of the entire word, we could apply whole-word masking."* Trade-off: *"Generally, predicting whole words tends to be more complicated than tokens, which makes the model perform better as it needs to learn more accurate and precise representations during training. However, it tends to take a bit more time to converge."* Use `DataCollatorForWholeWordMask` to switch.
- **15% masking probability.** *"We set the probability that a token is masked in a given sentence to 15% (`mlm_probability`)."* The same 15% inherited from BERT's original masked-LM recipe.
- **Qualitative demonstration via `fill-mask`.** Prompt `"What a horrible [MASK]!"`:

  | Model | Top predictions |
  |---|---|
  | Base `bert-base-cased` | idea, dream, thing, day, thought |
  | MLM-continued-on-rotten-tomatoes | movie, film, mess, comedy, story |

  *"A horrible movie, film, mess, etc. clearly shows us that the model is more biased toward the data that we fed it compared to the pretrained model."*

- **Save the tokenizer before training, save the model after.** *"The tokenizer is not updated during training so there is no need to save it after training. We will, however, save our model after we continue pretraining."*

### Named-entity recognition (token classification)

- **NER classifies individual tokens, not documents.** *"Instead of classifying entire documents, this procedure allows for the classification of individual tokens and/or words, including people and locations. This is especially helpful for de-identification and anonymization tasks when there is sensitive data."*
- **Tokens, not words.** *"Our word-level classification task does not entail classifying entire words, but rather the tokens that collectively constitute those words."* Subword tokenization splits words like `homer → home + ##r` or `Maarten → Ma + ##arte + ##n`, and the model labels each subtoken.
- **CoNLL-2003 is the canonical NER benchmark.** *"The English version of the CoNLL-2003 dataset, which contains several different types of named entities (person, organization, location, miscellaneous, and no entity) and has roughly 14,000 training samples."* Reference: Erik F. Sang & Fien De Meulder. *"Introduction to the CoNLL-2003 shared task,"* arXiv:cs/0306050 (2003).
- **Related NER datasets** mentioned in passing: [[WNUT17|`wnut_17`]] (emerging and rare entities), `tner/mit_movie_trivia` (actor, plot, soundtrack), `tner/mit_restaurant` (amenity, dish, cuisine). Reference: Jingjing Liu et al. *"Asgard: A portable architecture for multilingual dialogue systems,"* ICASSP 2013.
- **The BIO-tagging label scheme.** Nine labels in CoNLL-2003:

  ```python
  label2id = {
      "O": 0, "B-PER": 1, "I-PER": 2, "B-ORG": 3, "I-ORG": 4,
      "B-LOC": 5, "I-LOC": 6, "B-MISC": 7, "I-MISC": 8
  }
  ```

  Entity classes: **PER** (person), **ORG** (organization), **LOC** (location), **MISC** (miscellaneous). Prefixes: **B-** (beginning of phrase), **I-** (inside / continuation), **O** (outside any entity).
  *"If two tokens that follow each other are part of the same phrase, then the start of that phrase is indicated with B, which is followed by an I to show that they belong to each other and are not independent entities."* Example: *"Dean Palmer"* → `B-PER B-PER` would mean two separate people; `B-PER I-PER` correctly marks it as one person.
- **Label alignment is the new step.** *"This creates a bit of a problem for us since we have labeled data at the word level but not at the token level. This can be resolved by aligning the labels with their subtoken counterparts during tokenization."* For `Maarten → Ma + ##arte + ##n`, the alignment rule is: first subtoken `Ma` keeps `B-PER`; subsequent subtokens `##arte` and `##n` get `I-PER`.
- **Special tokens get `-100`.** `[CLS]`, `[SEP]`, and padding tokens get label `-100` to be **ignored by the loss function** (PyTorch's `CrossEntropyLoss` default `ignore_index=-100`). Original sentence labels `[1, 2, 0, 0, 0, 0, 0, 0, 3, 0]` become `[-100, 1, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, -100]` after alignment.
- **The alignment function**:

  ```python
  def align_labels(examples):
      token_ids = tokenizer(
          examples["tokens"],
          truncation=True,
          is_split_into_words=True
      )
      labels = examples["ner_tags"]

      updated_labels = []
      for index, label in enumerate(labels):
          word_ids = token_ids.word_ids(batch_index=index)
          previous_word_idx = None
          label_ids = []
          for word_idx in word_ids:
              if word_idx != previous_word_idx:
                  # First subtoken of a new word — inherit the word's label
                  previous_word_idx = word_idx
                  updated_label = -100 if word_idx is None else label[word_idx]
                  label_ids.append(updated_label)
              elif word_idx is None:
                  # Special token — ignore
                  label_ids.append(-100)
              else:
                  # Continuation subtoken — convert B-XXX → I-XXX
                  updated_label = label[word_idx]
                  if updated_label % 2 == 1:
                      updated_label += 1
                  label_ids.append(updated_label)
          updated_labels.append(label_ids)
      token_ids["labels"] = updated_labels
      return token_ids
  ```

  The `if updated_label % 2 == 1: updated_label += 1` step exploits the label2id ordering — `B-*` labels are odd, `I-*` labels are even and one higher — to convert beginning labels to inside labels on continuation subtokens.

- **Use `AutoModelForTokenClassification`, not `AutoModelForSequenceClassification`.** *"Now that we have loaded our model, the rest of the steps are similar to previous training procedures in this chapter."* The structural change is the head architecture: per-token classification head over the encoder's per-position hidden states, not a pooled-CLS-over-sequence head.
- **Use `DataCollatorForTokenClassification`.** *"Instead of `DataCollatorWithPadding`, we need a collator that works with classification on a token level."*
- **Use [[seqeval|`seqeval`]] for token-level metrics.** *"We now have multiple predictions per document, namely per token. We will make use of the evaluate package by Hugging Face to create a `compute_metrics` function that allows us to evaluate performance on a token level."* `seqeval` knows about BIO-tag span semantics, so its F1 is span-level (correct only if both start and end of a span are predicted correctly).
- **Inference via `pipeline("token-classification")`.** On the sentence *"My name is Maarten."*, the model correctly identifies `Ma + ##arte + ##n` as `B-PER + I-PER + I-PER` with scores ≈ 0.99.

## Key Quotes

> *"If we have sufficient data, fine-tuning tends to lead to some of the best-performing models possible. ... we will go through several methods and applications for fine-tuning BERT models."* — Ch 11 opener.

> *"Compared to the embedding model approach, we will fine-tune both the representation model and the classification head as a single architecture."* — describing the **task-specific architecture** that differentiates Ch 11 from [[hands-on-llm-ch04-text-classification|Ch 4]]'s frozen approach.

> *"A backward pass will start at the classification head and go through BERT."* — joint-training mechanics.

> *"Generally, we want frozen layers to be followed by trainable layers."* — the layer-freezing design rule.

> *"Training only the first five encoder blocks ... is enough to almost reach the performance of training all encoder blocks."* — the empirical finding that motivates partial fine-tuning.

> *"Only a few labeled examples are needed for [SetFit] to be competitive with fine-tuning a BERT-like model on a large, labeled dataset."* — the headline SetFit claim.

> *"When we have 16 sentences about sports, we can create 16 * (16 – 1) / 2 = 120 pairs that we label as positive pairs."* — SetFit's combinatorial data expansion.

> *"With only 32 labeled documents, we get an F1 score of 0.85."* — the SetFit result.

> *"It is like going from a general BERT model to a BioBERT model specialized for the medical domain, to a fine-tuned BioBERT model to classify medication."* — the canonical example of the three-stage continued-pretraining pipeline.

> *"This will update the subword representations to be more tuned toward words it would not have seen before."* — what continued MLM pretraining accomplishes.

> *"Generally, predicting whole words tends to be more complicated than tokens, which makes the model perform better as it needs to learn more accurate and precise representations during training. However, it tends to take a bit more time to converge."* — the token-masking vs whole-word-masking trade-off.

> *"Our word-level classification task does not entail classifying entire words, but rather the tokens that collectively constitute those words."* — the structural change from document- to token-classification.

> *"If two tokens that follow each other are part of the same phrase, then the start of that phrase is indicated with B, which is followed by an I to show that they belong to each other and are not independent entities."* — the BIO-tagging convention.

> *"Whenever an entity is split into tokens, the first token should have B (for beginning) and the following should be I (for inner)."* — the subtoken-alignment rule.

## Connections

### Source-internal cross-chapter

- [[hands-on-llm-ch01-introduction-to-llms]] — Ch 1's *"we forward-reference Ch 11 for fine-tuning representation models"* promise. Ch 1's two-flavors-of-fine-tuning taxonomy (task vs instruction) puts representation-model fine-tuning on the **task** side; Ch 11 walks that side.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2 introduced [[ClsToken|`[CLS]`]] / `[SEP]` and WordPiece subword tokenization; Ch 11 relies on both for the NER alignment story (`homer → home + ##r`).
- [[hands-on-llm-ch03-looking-inside-llms]] — Ch 3's tour of BERT's 12 encoder blocks is the structural prerequisite for Ch 11's layer-freezing experiments.
- [[hands-on-llm-ch04-text-classification]] — Ch 4 used frozen pretrained representation models on the same `rotten_tomatoes` dataset (F1 = 0.80 with `TwitterRoBERTa`); Ch 11 fine-tunes the same dataset (F1 = 0.85) showing the lift fine-tuning provides.
- [[hands-on-llm-ch09-multimodal-llms]] — Ch 9 covered frozen encoders bridged by trainable adapters (BLIP-2 Q-Former, LLaVA MLP); Ch 11 covers the opposite — trainable encoders for classification with optional layer freezing.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — Ch 10 introduced [[ContrastiveLearning|contrastive learning]] for sentence-transformers and explicitly forward-referenced Ch 11 for the [[MaskedLanguageModel|MLM]]-on-pretrained-BERT half of the [[DomainAdaptation|domain-adaptation]] recipe. Ch 10's [[SentenceTransformers]] / `all-mpnet-base-v2` / contrastive-learning machinery is the substrate SetFit builds on in Ch 11.
- **Ch 12** (forward reference) — fine-tuning **generative** models with instruction fine-tuning and preference alignment ([[rlhf|RLHF]] / [[DPO]]). Ch 11's representation-model fine-tuning is the encoder-side sibling.

### Wiki-level

- [[bert]] / [[FineTuningBert]] — Ch 11 is the **runnable-code instance** of the FineTuningBert recipe (single-text classification + token-level tagging templates).
- [[FineTuning]] / [[FullFinetuning]] / [[PartialFinetuning]] — Ch 11 walks **full fine-tuning** (regime 1) and **partial fine-tuning via layer freezing** (regime 2) as runnable code.
- [[ContinuedPretraining]] — Ch 11 provides the **encoder-side MLM** recipe for continued pretraining, complementing the next-token-prediction recipe sketched in [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]].
- [[DomainAdaptation]] / [[AdaptivePretraining]] — Ch 11 implements the **MLM half** of [[hands-on-llm-ch10-creating-text-embedding-models|Ch 10]]'s domain-adaptation recipe matrix.
- [[MaskedLanguageModel|MLM]] — Ch 11 uses MLM not as a *creation* objective (Ch 1 framing) but as a **continued-pretraining** objective (Ch 11 framing).
- [[SetFit]] — primary source for the wiki's SetFit page.
- [[NamedEntityRecognition]] / [[TokenClassification]] / [[BIOTagging]] — Ch 11 is the wiki's first end-to-end NER runnable recipe.
- [[CoNLL2003]] — Ch 11 is the wiki's first canonical worked use.
- [[F1Score]] — Ch 11 reuses Ch 4's F1 reporting convention.
- [[ContrastiveLearning]] — Ch 11's SetFit pipeline uses Ch 10's contrastive-learning machinery for the sentence-pair fine-tuning step.
- [[RottenTomatoes]] / [[BERT|`bert-base-cased`]] / [[HuggingFace|Hugging Face `transformers`]] / [[Trainer]] / [[SentenceTransformers]] / [[AllMPNetBaseV2]] — the chapter's stack.
- [[LewisTunstall]] — first author of the SetFit paper; cited in Ch 11.
- [[OReilly]] / [[HandsOnLLM]] / [[JayAlammar]] / [[MaartenGrootendorst]] — book metadata.

## Contradictions

- **No hard contradictions with prior wiki sources.** Ch 11's claims are consistent with:
  - [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]'s coverage of [[PartialFinetuning|partial fine-tuning]] (Houlsby et al. 2019, *"BERT-large needs ~25% of params updated to match full FT on GLUE"*) — Ch 11 provides a runnable demonstration with a smaller fraction (just block 11 + head) showing the same shape of result (0.80 vs 0.85 in one epoch).
  - [[ContinuedPretraining]]'s framing as *"self-supervised finetuning on cheap task-related raw text before expensive supervised finetuning"* — Ch 11 implements exactly this.
  - [[d2l-nlp-applications]] / [[FineTuningBert]]'s coverage of the *"pretrained encoder + task head, joint update"* template — Ch 11 is the Hugging Face `Trainer` instantiation of this template.
  - [[hands-on-llm-ch10-creating-text-embedding-models|Ch 10]]'s [[DomainAdaptation]] recipe — Ch 11 walks the MLM half of that matrix as promised.

- **Soft note**: Ch 11 trains the MLM-continued model for **10 epochs** vs the sequence-classification fine-tune at **1 epoch**. This reflects the difference in difficulty (MLM is harder per-step because only 15% of positions contribute gradient) and is consistent with the wiki's [[MaskedLanguageModel]] page noting that *"MLM converges marginally slower than left-to-right LM."* The Ch 11 prose says *"We train for 20 epochs"* mid-paragraph but the code says `num_train_epochs=10` — likely a residual edit artifact in the source text. The wiki records both numbers.

- **Soft note on terminology**: *"BERT" is the cover-term* — Ch 11's code uses `bert-base-cased` specifically (Wikipedia + BookCorpus pretraining); other BERT variants (`bert-base-uncased`, `bert-large-cased`, RoBERTa, DistilBERT) work identically with the same `AutoModelForSequenceClassification` / `AutoModelForTokenClassification` / `AutoModelForMaskedLM` pattern.

- **Soft note on the misprint**: Ch 11's footnote 3 cites *"How to fine-tune GERT for text classification?"* — this is a typo in the source; the actual paper title is *"How to Fine-Tune BERT for Text Classification?"* (Sun et al., CCL 2019). The wiki records the corrected citation.
