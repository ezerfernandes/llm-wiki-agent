# HuggingFace LLM Course — Chapter 1: Transformer models
Source: https://huggingface.co/learn/llm-course/chapter1/
Sections: 1,2,3,4,5,6,8,9,10
---

## Section 1: Introduction

# Introduction[[introduction]]

## Welcome to the 🤗 Course![[welcome-to-the-course]]

This course will teach you about large language models (LLMs) and natural language processing (NLP) using libraries from the [Hugging Face](https://huggingface.co/) ecosystem — [🤗 Transformers](https://github.com/huggingface/transformers), [🤗 Datasets](https://github.com/huggingface/datasets), [🤗 Tokenizers](https://github.com/huggingface/tokenizers), and [🤗 Accelerate](https://github.com/huggingface/accelerate) — as well as the [Hugging Face Hub](https://huggingface.co/models).

We'll also cover libraries outside the Hugging Face ecosystem. These are amazing contributions to the AI community and incredibly useful tools.

It's completely free and without ads.

## Understanding NLP and LLMs[[understanding-nlp-and-llms]]

While this course was originally focused on NLP (Natural Language Processing), it has evolved to emphasize Large Language Models (LLMs), which represent the latest advancement in the field.

**What's the difference?**
- **NLP (Natural Language Processing)** is the broader field focused on enabling computers to understand, interpret, and generate human language. NLP encompasses many techniques and tasks such as sentiment analysis, named entity recognition, and machine translation.
- **LLMs (Large Language Models)** are a powerful subset of NLP models characterized by their massive size, extensive training data, and ability to perform a wide range of language tasks with minimal task-specific training. Models like the Llama, GPT, or Claude series are examples of LLMs that have revolutionized what's possible in NLP.

Throughout this course, you'll learn about both traditional NLP concepts and cutting-edge LLM techniques, as understanding the foundations of NLP is crucial for working effectively with LLMs.

## What to expect?[[what-to-expect]]

Here is a brief overview of the course:

- Chapters 1 to 4 provide an introduction to the main concepts of the 🤗 Transformers library. By the end of this part of the course, you will be familiar with how Transformer models work and will know how to use a model from the [Hugging Face Hub](https://huggingface.co/models), fine-tune it on a dataset, and share your results on the Hub!
- Chapters 5 to 8 teach the basics of 🤗 Datasets and 🤗 Tokenizers before diving into classic NLP tasks and LLM techniques. By the end of this part, you will be able to tackle the most common language processing challenges by yourself.
- Chapter 9 goes beyond NLP to cover how to build and share demos of your models on the 🤗 Hub. By the end of this part, you will be ready to showcase your 🤗 Transformers application to the world!
- Chapters 10 to 12 dive into advanced LLM topics like fine-tuning, curating high-quality datasets, and building reasoning models.

This course:

* Requires a good knowledge of Python
* Is better taken after an introductory deep learning course, such as [fast.ai's](https://www.fast.ai/) [Practical Deep Learning for Coders](https://course.fast.ai/) or one of the programs developed by [DeepLearning.AI](https://www.deeplearning.ai/)
* Does not expect prior [PyTorch](https://pytorch.org/) or [TensorFlow](https://www.tensorflow.org/) knowledge, though some familiarity with either of those will help

## Who are we?[[who-are-we]]

About the authors:

- **Abubakar Abid** — completed his PhD at Stanford in applied machine learning. Founded Gradio (acquired by Hugging Face); now ML team lead at HF.
- **Ben Burtenshaw** — ML Engineer at Hugging Face. PhD in NLP at University of Antwerp.
- **Matthew Carrigan** — ML Engineer at Hugging Face based in Dublin.
- **Lysandre Debut** — ML Engineer at Hugging Face, has worked on Transformers since early development.
- **Sylvain Gugger** — Research Engineer at HF, core maintainer of Transformers, co-author of *Deep Learning for Coders with fastai and PyTorch*.
- **Dawood Khan** — ML Engineer at HF, co-founder of Gradio.
- **Merve Noyan** — developer advocate at Hugging Face.
- **Lucile Saulnier** — ML engineer at HF, involved in BigScience and collaborative training.
- **Lewis Tunstall** — ML engineer at HF, co-author of O'Reilly *Natural Language Processing with Transformers*.
- **Leandro von Werra** — ML engineer in HF open-source team, co-author of O'Reilly *Natural Language Processing with Transformers*.

## Let's go 🚀

In this chapter, you will learn:

* How to use the `pipeline()` function to solve NLP tasks such as text generation and classification
* About the Transformer architecture
* How to distinguish between encoder, decoder, and encoder-decoder architectures and use cases

---

## Section 2: Natural Language Processing and Large Language Models

# Natural Language Processing and Large Language Models[[natural-language-processing-and-large-language-models]]

Before jumping into Transformer models, let's do a quick overview of what natural language processing is, how large language models have transformed the field, and why we care about it.

## What is NLP?[[what-is-nlp]]

NLP is a field of linguistics and machine learning focused on understanding everything related to human language. The aim of NLP tasks is not only to understand single words individually, but to be able to understand the context of those words.

The following is a list of common NLP tasks, with some examples of each:

- **Classifying whole sentences**: Getting the sentiment of a review, detecting if an email is spam, determining if a sentence is grammatically correct or whether two sentences are logically related or not
- **Classifying each word in a sentence**: Identifying the grammatical components of a sentence (noun, verb, adjective), or the named entities (person, location, organization)
- **Generating text content**: Completing a prompt with auto-generated text, filling in the blanks in a text with masked words
- **Extracting an answer from a text**: Given a question and a context, extracting the answer to the question based on the information provided in the context
- **Generating a new sentence from an input text**: Translating a text into another language, summarizing a text

NLP isn't limited to written text though. It also tackles complex challenges in speech recognition and computer vision, such as generating a transcript of an audio sample or a description of an image.

## The Rise of Large Language Models (LLMs)[[rise-of-llms]]

In recent years, the field of NLP has been revolutionized by Large Language Models (LLMs). These models, which include architectures like GPT (Generative Pre-trained Transformer) and [Llama](https://huggingface.co/meta-llama), have transformed what's possible in language processing.

> A large language model (LLM) is an AI model trained on massive amounts of text data that can understand and generate human-like text, recognize patterns in language, and perform a wide variety of language tasks without task-specific training. They represent a significant advancement in the field of natural language processing (NLP).

LLMs are characterized by:
- **Scale**: They contain millions, billions, or even hundreds of billions of parameters
- **General capabilities**: They can perform multiple tasks without task-specific training
- **In-context learning**: They can learn from examples provided in the prompt
- **Emergent abilities**: As these models grow in size, they demonstrate capabilities that weren't explicitly programmed or anticipated

The advent of LLMs has shifted the paradigm from building specialized models for specific NLP tasks to using a single, large model that can be prompted or fine-tuned to address a wide range of language tasks. This has made sophisticated language processing more accessible while also introducing new challenges in areas like efficiency, ethics, and deployment.

However, LLMs also have important limitations:
- **Hallucinations**: They can generate incorrect information confidently
- **Lack of true understanding**: They lack true understanding of the world and operate purely on statistical patterns
- **Bias**: They may reproduce biases present in their training data or inputs.
- **Context windows**: They have limited context windows (though this is improving)
- **Computational resources**: They require significant computational resources

## Why is language processing challenging?[[why-is-it-challenging]]

Computers don't process information in the same way as humans. For example, when we read the sentence "I am hungry," we can easily understand its meaning. Similarly, given two sentences such as "I am hungry" and "I am sad," we're able to easily determine how similar they are. For machine learning (ML) models, such tasks are more difficult. The text needs to be processed in a way that enables the model to learn from it. And because language is complex, we need to think carefully about how this processing must be done. There has been a lot of research done on how to represent text, and we will look at some methods in the next chapter.

Even with the advances in LLMs, many fundamental challenges remain. These include understanding ambiguity, cultural context, sarcasm, and humor. LLMs address these challenges through massive training on diverse datasets, but still often fall short of human-level understanding in many complex scenarios.

---

## Section 3: Transformers, what can they do?

# Transformers, what can they do?[[transformers-what-can-they-do]]

In this section, we will look at what Transformer models can do and use our first tool from the 🤗 Transformers library: the `pipeline()` function.

## Transformers are everywhere![[transformers-are-everywhere]]

Transformer models are used to solve all kinds of tasks across different modalities, including natural language processing (NLP), computer vision, audio processing, and more.

The [🤗 Transformers library](https://github.com/huggingface/transformers) provides the functionality to create and use those shared models. The [Model Hub](https://huggingface.co/models) contains millions of pretrained models that anyone can download and use. You can also upload your own models to the Hub!

## Working with pipelines[[working-with-pipelines]]

The most basic object in the 🤗 Transformers library is the `pipeline()` function. It connects a model with its necessary preprocessing and postprocessing steps, allowing us to directly input any text and get an intelligible answer:

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
classifier("I've been waiting for a HuggingFace course my whole life.")
```

```python out
[{'label': 'POSITIVE', 'score': 0.9598047137260437}]
```

We can even pass several sentences!

```python
classifier(
    ["I've been waiting for a HuggingFace course my whole life.", "I hate this so much!"]
)
```

```python out
[{'label': 'POSITIVE', 'score': 0.9598047137260437},
 {'label': 'NEGATIVE', 'score': 0.9994558095932007}]
```

By default, this pipeline selects a particular pretrained model that has been fine-tuned for sentiment analysis in English. The model is downloaded and cached when you create the `classifier` object.

There are three main steps involved when you pass some text to a pipeline:

1. The text is preprocessed into a format the model can understand.
2. The preprocessed inputs are passed to the model.
3. The predictions of the model are post-processed, so you can make sense of them.

## Available pipelines for different modalities

### Text pipelines

- `text-generation`: Generate text from a prompt
- `text-classification`: Classify text into predefined categories
- `summarization`: Create a shorter version of a text while preserving key information
- `translation`: Translate text from one language to another
- `zero-shot-classification`: Classify text without prior training on specific labels
- `feature-extraction`: Extract vector representations of text

### Image pipelines

- `image-to-text`: Generate text descriptions of images
- `image-classification`: Identify objects in an image
- `object-detection`: Locate and identify objects in images

### Audio pipelines

- `automatic-speech-recognition`: Convert speech to text
- `audio-classification`: Classify audio into categories
- `text-to-speech`: Convert text to spoken audio

### Multimodal pipelines

- `image-text-to-text`: Respond to an image based on a text prompt

## Zero-shot classification[[zero-shot-classification]]

```python
from transformers import pipeline

classifier = pipeline("zero-shot-classification")
classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)
```

```python out
{'sequence': 'This is a course about the Transformers library',
 'labels': ['education', 'business', 'politics'],
 'scores': [0.8445963859558105, 0.111976258456707, 0.043427448719739914]}
```

This pipeline is called _zero-shot_ because you don't need to fine-tune the model on your data to use it.

## Text generation[[text-generation]]

```python
from transformers import pipeline

generator = pipeline("text-generation")
generator("In this course, we will teach you how to")
```

You can control how many different sequences are generated with `num_return_sequences` and total length with `max_length`.

## Using any model from the Hub in a pipeline[[using-any-model-from-the-hub-in-a-pipeline]]

```python
from transformers import pipeline

generator = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-360M")
generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2,
)
```

### Inference Providers[[inference-providers]]

All the models can be tested directly through your browser using the Inference Providers, available on the Hugging Face website. Inference Providers is also available as a paid product.

## Mask filling[[mask-filling]]

```python
from transformers import pipeline

unmasker = pipeline("fill-mask")
unmasker("This course will teach you all about <mask> models.", top_k=2)
```

```python out
[{'sequence': 'This course will teach you all about mathematical models.',
  'score': 0.19619831442832947,
  'token': 30412,
  'token_str': ' mathematical'},
 {'sequence': 'This course will teach you all about computational models.',
  'score': 0.04052725434303284,
  'token': 38163,
  'token_str': ' computational'}]
```

The `top_k` argument controls how many possibilities are displayed. Note that the model fills in the special `<mask>` word (the *mask token*); other mask-filling models may have different mask tokens.

## Named entity recognition[[named-entity-recognition]]

```python
from transformers import pipeline

ner = pipeline("ner", grouped_entities=True)
ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")
```

```python out
[{'entity_group': 'PER', 'score': 0.99816, 'word': 'Sylvain', 'start': 11, 'end': 18},
 {'entity_group': 'ORG', 'score': 0.97960, 'word': 'Hugging Face', 'start': 33, 'end': 45},
 {'entity_group': 'LOC', 'score': 0.99321, 'word': 'Brooklyn', 'start': 49, 'end': 57}
]
```

We pass `grouped_entities=True` to regroup parts of the sentence corresponding to the same entity. The preprocessing even splits some words into smaller parts (`Sylvain` → `S`, `##yl`, `##va`, `##in`); the pipeline regroups them in post-processing.

## Question answering[[question-answering]]

```python
from transformers import pipeline

question_answerer = pipeline("question-answering")
question_answerer(
    question="Where do I work?",
    context="My name is Sylvain and I work at Hugging Face in Brooklyn",
)
```

```python out
{'score': 0.6385916471481323, 'start': 33, 'end': 45, 'answer': 'Hugging Face'}
```

This pipeline works by extracting information from the provided context; it does not generate the answer.

## Summarization[[summarization]]

```python
from transformers import pipeline

summarizer = pipeline("summarization")
summarizer("""...long article text...""")
```

You can specify `max_length` or `min_length` for the result.

## Translation[[translation]]

```python
from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
translator("Ce cours est produit par Hugging Face.")
```

```python out
[{'translation_text': 'This course is produced by Hugging Face.'}]
```

## Image and audio pipelines

### Image classification

```python
from transformers import pipeline

image_classifier = pipeline(
    task="image-classification", model="google/vit-base-patch16-224"
)
result = image_classifier(
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg"
)
```

### Automatic speech recognition

```python
from transformers import pipeline

transcriber = pipeline(
    task="automatic-speech-recognition", model="openai/whisper-large-v3"
)
result = transcriber(
    "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac"
)
```

## Combining data from multiple sources

Transformer models can combine and process data from multiple sources — searching across databases, consolidating information from different formats (text, images, audio), and creating a unified view of related information.

## Conclusion

The pipelines shown here are mostly for demonstrative purposes. They were programmed for specific tasks and cannot perform variations of them. In the next chapter, you'll learn what's inside a `pipeline()` function and how to customize its behavior.

---

## Section 4: How do Transformers work?

# How do Transformers work?[[how-do-transformers-work]]

In this section, we will take a look at the architecture of Transformer models and dive deeper into the concepts of attention, encoder-decoder architecture, and more.

## A bit of Transformer history[[a-bit-of-transformer-history]]

Here are some reference points in the (short) history of Transformer models:

The [Transformer architecture](https://arxiv.org/abs/1706.03762) was introduced in June 2017. The focus of the original research was on translation tasks. This was followed by the introduction of several influential models, including:

- **June 2018**: [GPT](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf), the first pretrained Transformer model, used for fine-tuning on various NLP tasks and obtained state-of-the-art results
- **October 2018**: [BERT](https://arxiv.org/abs/1810.04805), another large pretrained model, this one designed to produce better summaries of sentences
- **February 2019**: [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), an improved (and bigger) version of GPT that was not immediately publicly released due to ethical concerns
- **October 2019**: [T5](https://huggingface.co/papers/1910.10683), a multi-task focused implementation of the sequence-to-sequence Transformer architecture.
- **May 2020**: [GPT-3](https://huggingface.co/papers/2005.14165), an even bigger version of GPT-2 that is able to perform well on a variety of tasks without the need for fine-tuning (called _zero-shot learning_)
- **January 2022**: [InstructGPT](https://huggingface.co/papers/2203.02155), a version of GPT-3 that was trained to follow instructions better.
- **January 2023**: [Llama](https://huggingface.co/papers/2302.13971), a large language model that is able to generate text in a variety of languages.
- **March 2023**: [Mistral](https://huggingface.co/papers/2310.06825), a 7-billion-parameter language model that outperforms Llama 2 13B across all evaluated benchmarks, leveraging grouped-query attention for faster inference and sliding window attention to handle sequences of arbitrary length.
- **May 2024**: [Gemma 2](https://huggingface.co/papers/2408.00118), a family of lightweight, state-of-the-art open models ranging from 2B to 27B parameters that incorporate interleaved local-global attentions and group-query attention, with smaller models trained using knowledge distillation to deliver performance competitive with models 2-3 times larger.
- **November 2024**: [SmolLM2](https://huggingface.co/papers/2502.02737), a state-of-the-art small language model (135 million to 1.7 billion parameters) that achieves impressive performance despite its compact size, and unlocking new possibilities for mobile and edge devices.

Broadly, they can be grouped into three categories:

- GPT-like (also called _auto-regressive_ Transformer models)
- BERT-like (also called _auto-encoding_ Transformer models)
- T5-like (also called _sequence-to-sequence_ Transformer models)

## Transformers are language models[[transformers-are-language-models]]

All the Transformer models mentioned above (GPT, BERT, T5, etc.) have been trained as *language models*. This means they have been trained on large amounts of raw text in a self-supervised fashion.

Self-supervised learning is a type of training in which the objective is automatically computed from the inputs of the model. That means that humans are not needed to label the data!

This type of model develops a statistical understanding of the language it has been trained on, but it's less useful for specific practical tasks. Because of this, the general pretrained model then goes through a process called *transfer learning* or *fine-tuning*. During this process, the model is fine-tuned in a supervised way -- that is, using human-annotated labels -- on a given task.

An example of a task is predicting the next word in a sentence having read the *n* previous words. This is called *causal language modeling* because the output depends on the past and present inputs, but not the future ones.

Another example is *masked language modeling*, in which the model predicts a masked word in the sentence.

## Transformers are big models[[transformers-are-big-models]]

Apart from a few outliers (like DistilBERT), the general strategy to achieve better performance is by increasing the models' sizes as well as the amount of data they are pretrained on.

Unfortunately, training a model, especially a large one, requires a large amount of data. This becomes very costly in terms of time and compute resources. It even translates to environmental impact.

This is why sharing language models is paramount: sharing the trained weights and building on top of already trained weights reduces the overall compute cost and carbon footprint of the community.

You can evaluate the carbon footprint of your models' training through several tools. For example [ML CO2 Impact](https://mlco2.github.io/impact/) or [Code Carbon](https://codecarbon.io/) which is integrated in 🤗 Transformers.

## Transfer Learning[[transfer-learning]]

*Pretraining* is the act of training a model from scratch: the weights are randomly initialized, and the training starts without any prior knowledge. This pretraining is usually done on very large amounts of data.

*Fine-tuning*, on the other hand, is the training done **after** a model has been pretrained. To perform fine-tuning, you first acquire a pretrained language model, then perform additional training with a dataset specific to your task. Reasons:

* The pretrained model was already trained on a dataset that has some similarities with the fine-tuning dataset. The fine-tuning process is thus able to take advantage of knowledge acquired by the initial model during pretraining.
* Since the pretrained model was already trained on lots of data, the fine-tuning requires way less data to get decent results.
* For the same reason, the amount of time and resources needed to get good results are much lower.

Fine-tuning a model therefore has lower time, data, financial, and environmental costs. The knowledge the pretrained model has acquired is "transferred," hence the term *transfer learning*.

## General Transformer architecture[[general-transformer-architecture]]

The model is primarily composed of two blocks:

* **Encoder (left)**: The encoder receives an input and builds a representation of it (its features). This means that the model is optimized to acquire understanding from the input.
* **Decoder (right)**: The decoder uses the encoder's representation (features) along with other inputs to generate a target sequence. This means that the model is optimized for generating outputs.

Each of these parts can be used independently, depending on the task:

* **Encoder-only models**: Good for tasks that require understanding of the input, such as sentence classification and named entity recognition.
* **Decoder-only models**: Good for generative tasks such as text generation.
* **Encoder-decoder models** or **sequence-to-sequence models**: Good for generative tasks that require an input, such as translation or summarization.

## Attention layers[[attention-layers]]

A key feature of Transformer models is that they are built with special layers called *attention layers*. In fact, the title of the paper introducing the Transformer architecture was ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762)! For now, all you need to know is that this layer will tell the model to pay specific attention to certain words in the sentence you passed it (and more or less ignore the others) when dealing with the representation of each word.

To put this into context: when translating "You like this course" from English to French, the model needs to attend to "You" to properly conjugate "like". When translating "this", it must attend to "course" because "this" translates differently depending on whether the associated noun is masculine or feminine.

## The original architecture[[the-original-architecture]]

The Transformer architecture was originally designed for translation. During training, the encoder receives inputs (sentences) in a certain language, while the decoder receives the same sentences in the desired target language. In the encoder, the attention layers can use all the words in a sentence. The decoder works sequentially and can only pay attention to the words it has already translated.

To speed things up during training, the decoder is fed the whole target, but it is not allowed to use future words. For instance, when predicting the fourth word, the attention layer will only have access to the words in positions 1 to 3.

The first attention layer in a decoder block pays attention to all (past) inputs to the decoder, but the second attention layer uses the output of the encoder. The *attention mask* can also be used in the encoder/decoder to prevent the model from paying attention to some special words — for instance, the special padding word used to make all the inputs the same length when batching together sentences.

## Architectures vs. checkpoints[[architecture-vs-checkpoints]]

* **Architecture**: This is the skeleton of the model — the definition of each layer and each operation that happens within the model.
* **Checkpoints**: These are the weights that will be loaded in a given architecture.
* **Model**: This is an umbrella term that isn't as precise as "architecture" or "checkpoint": it can mean both.

For example, BERT is an architecture while `bert-base-cased`, a set of weights trained by the Google team for the first release of BERT, is a checkpoint.

---

## Section 5: How 🤗 Transformers solve tasks

# How 🤗 Transformers solve tasks

This page looks at how models solve common tasks. We'll cover:

- [Wav2Vec2](https://huggingface.co/docs/transformers/model_doc/wav2vec2) for audio classification and automatic speech recognition (ASR)
- [Vision Transformer (ViT)](https://huggingface.co/docs/transformers/model_doc/vit) and [ConvNeXT](https://huggingface.co/docs/transformers/model_doc/convnext) for image classification
- [DETR](https://huggingface.co/docs/transformers/model_doc/detr) for object detection
- [Mask2Former](https://huggingface.co/docs/transformers/model_doc/mask2former) for image segmentation
- [GLPN](https://huggingface.co/docs/transformers/model_doc/glpn) for depth estimation
- [BERT](https://huggingface.co/docs/transformers/model_doc/bert) for NLP tasks like text classification, token classification and question answering that use an encoder
- [GPT2](https://huggingface.co/docs/transformers/model_doc/gpt2) for NLP tasks like text generation that use a decoder
- [BART](https://huggingface.co/docs/transformers/model_doc/bart) for NLP tasks like summarization and translation that use an encoder-decoder

## Transformer models for language

The Transformer was initially designed for machine translation, and since then, it has become the default architecture for solving all AI tasks.

### How language models work

Two main approaches for training a transformer model:

1. **Masked language modeling (MLM)**: Used by encoder models like BERT, this approach randomly masks some tokens in the input and trains the model to predict the original tokens based on the surrounding context. This allows the model to learn bidirectional context (looking at words both before and after the masked word).

2. **Causal language modeling (CLM)**: Used by decoder models like GPT, this approach predicts the next token based on all previous tokens in the sequence. The model can only use context from the left (previous tokens) to predict the next token.

### Types of language models

1. **Encoder-only models** (like BERT): Use a bidirectional approach. Best for tasks that require deep understanding of text: classification, NER, question answering.
2. **Decoder-only models** (like GPT, Llama): Process text from left to right. Good at text generation.
3. **Encoder-decoder models** (like T5, BART): Combine both — encoder understands input, decoder generates output. Best for seq-to-seq tasks like translation, summarization, generative QA.

### Text generation

[GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2) is a decoder-only model pretrained on a large amount of text.

1. GPT-2 uses [byte pair encoding (BPE)](https://huggingface.co/docs/transformers/tokenizer_summary#bytepair-encoding-bpe) to tokenize words and generate a token embedding. Positional encodings are added to the token embeddings. Input embeddings pass through multiple decoder blocks to output a final hidden state. Within each decoder block, GPT-2 uses a *masked self-attention* layer — it can't attend to future tokens, only to tokens on the left.

2. The output from the decoder is passed to a language modeling head, which performs a linear transformation to convert hidden states into logits. The label is the next token in the sequence (shifted right by one). The cross-entropy loss is calculated between the shifted logits and the labels.

GPT-2's pretraining objective is based entirely on [causal language modeling](https://huggingface.co/docs/transformers/glossary#causal-language-modeling).

### Text classification

[BERT](https://huggingface.co/docs/transformers/model_doc/bert) is an encoder-only model and is the first model to effectively implement deep bidirectionality.

1. BERT uses [WordPiece](https://huggingface.co/docs/transformers/tokenizer_summary#wordpiece) tokenization. A special `[SEP]` token separates sentences in a pair. A special `[CLS]` token is added to the beginning of every sequence — its final output is used as input to the classification head. BERT also adds a segment embedding to denote whether a token belongs to the first or second sentence.

2. BERT is pretrained with two objectives: masked language modeling and next-sentence prediction. In MLM, some percentage of the input tokens are randomly masked, and the model predicts them. The second pretraining objective is next-sentence prediction — the model must predict whether sentence B follows sentence A.

3. The input embeddings are passed through multiple encoder layers to output some final hidden states.

To use the pretrained model for text classification, add a sequence classification head on top of the base BERT model.

### Token classification

To use BERT for token classification tasks like NER, add a token classification head on top of the base BERT model. The token classification head is a linear layer that converts final hidden states into logits.

### Question answering

To use BERT for question answering, add a span classification head on top of the base BERT model. This linear layer accepts the final hidden states and performs a linear transformation to compute the `span` start and end logits corresponding to the answer.

### Summarization

Encoder-decoder models like [BART](https://huggingface.co/docs/transformers/model_doc/bart) and [T5](model_doc/t5) are designed for sequence-to-sequence tasks.

1. BART's encoder architecture is very similar to BERT and accepts a token and positional embedding of the text. BART is pretrained by corrupting the input and then reconstructing it with the decoder. BART can apply any type of corruption — *text infilling* works best: a number of text spans are replaced with a **single** `[mask]` token. The model has to predict the masked tokens and the number of missing tokens.

2. The encoder's output is passed to the decoder, which must predict the masked tokens and any uncorrupted tokens from the encoder's output. The decoder output is passed to a language modeling head; cross-entropy loss is computed.

### Translation

BART adapts to translation by adding a separate randomly initialized encoder to map a source language to an input that can be decoded into the target language. This new encoder's embeddings are passed to the pretrained encoder instead of the original word embeddings. BART has since been followed up by a multilingual version, mBART.

## Modalities beyond text

### Speech and audio

[Whisper](https://huggingface.co/docs/transformers/main/en/model_doc/whisper) is an encoder-decoder (sequence-to-sequence) transformer pretrained on 680,000 hours of labeled audio data. This enables zero-shot performance on audio tasks in English and many other languages.

1. An **encoder** processes the input audio. The raw audio is first converted into a log-Mel spectrogram. This spectrogram is then passed through a Transformer encoder network.
2. A **decoder** takes the encoded audio representation and autoregressively predicts the corresponding text tokens. Special tokens steer the model towards specific tasks like transcription, translation, or language identification.

### Automatic speech recognition

```python
from transformers import pipeline

transcriber = pipeline(
    task="automatic-speech-recognition", model="openai/whisper-base.en"
)
transcriber("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac")
# Output: {'text': ' I have a dream that one day this nation will rise up and live out the true meaning of its creed.'}
```

### Computer vision

Two approaches:
1. Split an image into a sequence of patches and process them in parallel with a Transformer.
2. Use a modern CNN, like [ConvNeXT](https://huggingface.co/docs/transformers/model_doc/convnext), which relies on convolutional layers but adopts modern network designs.

### Image classification

[ViT](https://huggingface.co/docs/transformers/model_doc/vit) replaces convolutions entirely with a pure Transformer architecture.

1. An image is split into square non-overlapping patches; each gets turned into a *patch embedding* via a conv 2D layer. A 224x224 image can be split into 196 16x16 patches.
2. A *learnable embedding* — special `[CLS]` token — is added to the beginning of the patch embeddings (like BERT). Its final hidden state feeds the classification head.
3. *Position embeddings* (learnable) are added because the model doesn't know how the patches are ordered.
4. The output (specifically the `[CLS]` output) is passed to a multilayer perceptron head (MLP). ViT's pretraining objective is classification.

---

## Section 6: Transformer Architectures

# Transformer Architectures[[transformer-architectures]]

Three main architectural variants of Transformer models: encoder-only, decoder-only, encoder-decoder.

## Encoder models[[encoder-models]]

Encoder models use only the encoder of a Transformer model. At each stage, the attention layers can access all the words in the initial sentence. These models are often characterized as having "bi-directional" attention, and are often called *auto-encoding models*.

The pretraining of these models usually revolves around somehow corrupting a given sentence (for instance, by masking random words in it) and tasking the model with finding or reconstructing the initial sentence.

Encoder models are best suited for tasks requiring an understanding of the full sentence, such as sentence classification, named entity recognition (and more generally word classification), and extractive question answering.

Representatives:
- [BERT](https://huggingface.co/docs/transformers/model_doc/bert)
- [DistilBERT](https://huggingface.co/docs/transformers/model_doc/distilbert)
- [ModernBERT](https://huggingface.co/docs/transformers/en/model_doc/modernbert)

## Decoder models[[decoder-models]]

Decoder models use only the decoder of a Transformer model. At each stage, for a given word the attention layers can only access the words positioned before it. These models are often called *auto-regressive models*.

The pretraining of decoder models usually revolves around predicting the next word in the sentence.

These models are best suited for tasks involving text generation.

Representatives:
- [Hugging Face SmolLM Series](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct)
- [Meta's Llama Series](https://huggingface.co/docs/transformers/en/model_doc/llama4)
- [Google's Gemma Series](https://huggingface.co/docs/transformers/main/en/model_doc/gemma3)
- [DeepSeek's V3](https://huggingface.co/deepseek-ai/DeepSeek-V3)

### Modern Large Language Models (LLMs)

Most modern Large Language Models (LLMs) use the decoder-only architecture. Modern LLMs are typically trained in two phases:
1. **Pretraining**: The model learns to predict the next token on vast amounts of text data
2. **Instruction tuning**: The model is fine-tuned to follow instructions and generate helpful responses

#### Key capabilities of modern LLMs

| Capability | Description | Example |
|------------|-------------|---------|
| Text generation | Creating coherent and contextually relevant text | Writing essays, stories, or emails |
| Summarization | Condensing long documents into shorter versions | Creating executive summaries of reports |
| Translation | Converting text between languages | Translating English to Spanish |
| Question answering | Providing answers to factual questions | "What is the capital of France?" |
| Code generation | Writing or completing code snippets | Creating a function based on a description |
| Reasoning | Working through problems step by step | Solving math problems or logical puzzles |
| Few-shot learning | Learning from a few examples in the prompt | Classifying text after seeing just 2-3 examples |

## Sequence-to-sequence models[[sequence-to-sequence-models]]

Encoder-decoder models (also called *sequence-to-sequence models*) use both parts of the Transformer architecture. At each stage, the attention layers of the encoder can access all the words in the initial sentence, whereas the attention layers of the decoder can only access the words positioned before a given word in the input.

The pretraining of T5 consists of replacing random spans of text with a single mask special token; the task is then to predict the text the mask token replaces.

Sequence-to-sequence models are best suited for tasks revolving around generating new sentences depending on a given input, such as summarization, translation, or generative question answering.

### Practical applications

| Application | Description | Example Model |
|-------------|-------------|---------------|
| Machine translation | Converting text between languages | Marian, T5 |
| Text summarization | Creating concise summaries of longer texts | BART, T5 |
| Data-to-text generation | Converting structured data into natural language | T5 |
| Grammar correction | Fixing grammatical errors in text | T5 |
| Question answering | Generating answers based on context | BART, T5 |

Representatives:
- [BART](https://huggingface.co/docs/transformers/model_doc/bart)
- [mBART](https://huggingface.co/docs/transformers/model_doc/mbart)
- [Marian](https://huggingface.co/docs/transformers/model_doc/marian)
- [T5](https://huggingface.co/docs/transformers/model_doc/t5)

## Choosing the right architecture[[choosing-the-right-architecture]]

| Task | Suggested Architecture | Examples |
|------|------------------------|----------|
| Text classification (sentiment, topic) | Encoder | BERT, RoBERTa |
| Text generation (creative writing) | Decoder | GPT, LLaMA |
| Translation | Encoder-Decoder | T5, BART |
| Summarization | Encoder-Decoder | BART, T5 |
| Named entity recognition | Encoder | BERT, RoBERTa |
| Question answering (extractive) | Encoder | BERT, RoBERTa |
| Question answering (generative) | Encoder-Decoder or Decoder | T5, GPT |
| Conversational AI | Decoder | GPT, LLaMA |

## Attention mechanisms[[attention-mechanisms]]

Most transformer models use full attention — the attention matrix is square. It can be a big computational bottleneck for long texts (O(n²) complexity). Longformer and Reformer use a sparse version of the attention matrix.

### LSH attention

[Reformer](https://huggingface.co/docs/transformers/model_doc/reformer) uses LSH attention. In softmax(QK^t), only the biggest elements of QK^t give useful contributions. For each query q in Q, we can consider only the keys k in K that are close to q. A hash function determines closeness. Several hash functions are used in practice (n_rounds parameter) and averaged together.

### Local attention

[Longformer](https://huggingface.co/docs/transformers/model_doc/longformer) uses local attention: often, the local context (e.g., what are the two tokens to the left and right?) is enough. By stacking attention layers with a small window, the last layer has a receptive field of more than just the tokens in the window. Some preselected input tokens are also given global attention.

### Axial positional encodings

[Reformer](https://huggingface.co/docs/transformers/model_doc/reformer) uses axial positional encodings: factorize the positional encoding matrix E (size l × d) into two smaller matrices E1 (l₁ × d₁) and E2 (l₂ × d₂), such that l₁ × l₂ = l and d₁ + d₂ = d. The embedding for time step j is obtained by concatenating the embeddings for j % l₁ in E1 and j // l₁ in E2.

---

## Section 8: Inference with LLMs

# Deep dive into Text Generation Inference with LLMs[[inference-with-llms]]

So far, we've explored the transformer architecture in relation to a range of discrete tasks. However, LLMs are most used for text generation.

## Understanding the Basics

Inference is the process of using a trained LLM to generate human-like text from a given input prompt. Language models use their knowledge from training to formulate responses one word at a time. The model leverages learned probabilities from billions of parameters to predict and generate the next token in a sequence. This sequential generation is what allows LLMs to produce coherent and contextually relevant text.

## The Role of Attention

The attention mechanism is what gives LLMs their ability to understand context and generate coherent responses. When predicting the next word, not every word in a sentence carries equal weight — for example, in *"The capital of France is ..."*, the words "France" and "capital" are crucial.

> In short, the attention mechanism is the key to LLMs being able to generate text that is both coherent and context-aware. It sets modern LLMs apart from previous generations of language models.

### Context Length and Attention Span

The context length refers to the maximum number of tokens that the LLM can process at once. Think of it as the size of the model's working memory.

Limited by several practical factors:
- The model's architecture and size
- Available computational resources
- The complexity of the input and desired output

### The Art of Prompting

When we pass information to LLMs, we structure our input in a way that guides the generation of the LLM toward the desired output. This is called _prompting_. Since the model's primary task is to predict the next token by analyzing the importance of each input token, the wording of your input sequence becomes crucial.

## The Two-Phase Inference Process

The process can be broken down into two main phases: **prefill** and **decode**.

### The Prefill Phase

Three key steps:
1. **Tokenization**: Converting the input text into tokens
2. **Embedding Conversion**: Transforming these tokens into numerical representations that capture their meaning
3. **Initial Processing**: Running these embeddings through the model's neural networks to create a rich understanding of the context

This phase is computationally intensive because it needs to process all input tokens at once.

### The Decode Phase

The model generates one token at a time in what we call an autoregressive process. Steps per new token:
1. **Attention Computation**: Looking back at all previous tokens to understand context
2. **Probability Calculation**: Determining the likelihood of each possible next token
3. **Token Selection**: Choosing the next token based on these probabilities
4. **Continuation Check**: Deciding whether to continue or stop generation

This phase is memory-intensive because the model needs to keep track of all previously generated tokens and their relationships.

## Sampling Strategies

### Understanding Token Selection: From Probabilities to Token Choices

1. **Raw Logits**: The model's initial gut feelings about each possible next word
2. **Temperature Control**: Like a creativity dial — higher settings (>1.0) make choices more random and creative, lower settings (<1.0) make choices more deterministic
3. **Top-p (Nucleus) Sampling**: Considers smallest set of tokens whose cumulative probability exceeds threshold p
4. **Top-k Filtering**: Limits choices to k most likely next tokens

### Managing Repetition: Keeping Output Fresh

- **Presence Penalty**: Fixed penalty to any token that has appeared before
- **Frequency Penalty**: Increasing penalty based on how often a token has been used

### Controlling Generation Length

- **Token Limits**: max/min token counts
- **Stop Sequences**: Specific patterns that signal end of generation
- **EOS Detection**: Recognizing when the model naturally wants to end its response

### Beam Search: Looking Ahead for Better Coherence

Beam search keeps track of multiple possible sequences (typically 5–10) at once, exploring different paths simultaneously. At each step it computes probabilities for each beam, selects the most promising combinations, continues expanding, and finally chooses the sequence with the highest overall probability. This often produces more coherent and grammatically correct text but requires more compute.

## Practical Challenges and Optimization

### Key Performance Metrics

1. **Time to First Token (TTFT)**: How quickly can you get the first response? Affected by the prefill phase.
2. **Time Per Output Token (TPOT)**: How fast can you generate subsequent tokens?
3. **Throughput**: How many requests can you handle simultaneously?
4. **VRAM Usage**: How much GPU memory do you need?

### The Context Length Challenge

- **Memory Usage**: Grows quadratically with context length
- **Processing Speed**: Decreases linearly with longer contexts
- **Resource Allocation**: Requires careful balancing of VRAM usage

Recent models like [Qwen2.5-1M](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-1M) offer impressive 1M token context windows, but this comes at the cost of significantly slower inference times.

### The KV Cache Optimization

One of the most powerful optimizations is KV (Key-Value) caching — storing and reusing intermediate calculations. This optimization:
- Reduces repeated calculations
- Improves generation speed
- Makes long-context generation practical

The trade-off is additional memory usage.

## Conclusion

We've covered: the fundamental role of attention and context, the two-phase inference process, various sampling strategies for controlling generation, and practical challenges and optimizations.

---

## Section 9: Bias and limitations

# Bias and limitations[[bias-and-limitations]]

If your intent is to use a pretrained model or a fine-tuned version in production, please be aware that these models come with limitations. The biggest is that, to enable pretraining on large amounts of data, researchers often scrape all the content they can find, taking the best as well as the worst of what is available on the internet.

Example with the `fill-mask` pipeline and BERT:

```python
from transformers import pipeline

unmasker = pipeline("fill-mask", model="bert-base-uncased")
result = unmasker("This man works as a [MASK].")
print([r["token_str"] for r in result])

result = unmasker("This woman works as a [MASK].")
print([r["token_str"] for r in result])
```

```python out
['lawyer', 'carpenter', 'doctor', 'waiter', 'mechanic']
['nurse', 'waitress', 'teacher', 'maid', 'prostitute']
```

When asked to fill in the missing word, the model gives only one gender-free answer (waiter/waitress). The others are occupations usually associated with one specific gender — and "prostitute" ended up in the top 5 possibilities the model associates with "woman" and "work." This happens even though BERT is trained on apparently neutral data (English Wikipedia and BookCorpus).

When you use these tools, you need to keep in the back of your mind that the original model could very easily generate sexist, racist, or homophobic content. **Fine-tuning the model on your data won't make this intrinsic bias disappear.**

---

## Section 10: Summary

# Summary[[summary]]

In this chapter, you've been introduced to the fundamentals of Transformer models, Large Language Models (LLMs), and how they're revolutionizing AI and beyond.

## Key concepts covered

### Natural Language Processing and LLMs

- NLP encompasses a wide range of tasks from classification to generation
- LLMs are powerful models trained on massive amounts of text data
- These models can perform multiple tasks within a single architecture
- Despite their capabilities, LLMs have limitations including hallucinations and bias

### Transformer capabilities

The `pipeline()` function from 🤗 Transformers makes it easy to use pre-trained models for various tasks:
- Text classification, token classification, and question answering
- Text generation and summarization
- Translation and other sequence-to-sequence tasks
- Speech recognition and image classification

### Transformer architecture

- The importance of the attention mechanism
- How transfer learning enables models to adapt to specific tasks
- The three main architectural variants: encoder-only, decoder-only, and encoder-decoder

### Model architectures and their applications

| Model           | Examples                                   | Tasks                                                                            |
|-----------------|--------------------------------------------|----------------------------------------------------------------------------------|
| Encoder-only    | BERT, DistilBERT, ModernBERT               | Sentence classification, named entity recognition, extractive question answering |
| Decoder-only    | GPT, LLaMA, Gemma, SmolLM                  | Text generation, conversational AI, creative writing                             |
| Encoder-decoder | BART, T5, Marian, mBART                    | Summarization, translation, generative question answering                        |

### Modern LLM developments

- How LLMs have grown in size and capability over time
- The concept of scaling laws and how they guide model development
- Specialized attention mechanisms that help models process longer sequences
- The two-phase training approach of pretraining and instruction tuning

### Practical applications

- Using the Hugging Face Hub to find and use pre-trained models
- Leveraging the Inference API to test models directly in your browser
- Understanding which models are best suited for specific tasks

## Looking ahead

In the next chapters, you'll learn how to:

- Use the Transformers library to load and fine-tune models
- Process different types of data for model input
- Adapt pre-trained models to your specific tasks
- Deploy models for practical applications
