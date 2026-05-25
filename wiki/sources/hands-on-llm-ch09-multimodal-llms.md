---
title: "Hands-On LLMs Ch 9 — Multimodal Large Language Models"
type: source
tags: [book, hands-on-llm, oreilly, llm, multimodal, vision-language, vision-transformer, vit, patch-embedding, clip, opencli, opencli, multimodal-embedding, contrastive-learning, blip-2, q-former, llava, idefics, soft-visual-prompt, image-captioning, visual-question-answering, zero-shot-classification]
date: 2024-01-01
source_file: raw/books/hands-on-llm/ch09-multimodal-llms.md
book: "Hands-On Large Language Models"
book_isbn13: "9781098150969"
book_authors: ["Jay Alammar", "Maarten Grootendorst"]
book_publisher: "O'Reilly Media"
book_year: 2024
---

# Hands-On LLMs Ch 9 — Multimodal Large Language Models

## Summary

The ninth chapter of [[JayAlammar|Jay Alammar]] and [[MaartenGrootendorst|Maarten Grootendorst]]'s *Hands-On Large Language Models* ([[OReilly|O'Reilly Media]], 2024, ISBN 978-1-098-15096-9) and the book's **vision-language chapter** — the only chapter that extends the wiki's existing text-only LLM coverage to **multimodal models that accept images** (and, by extension, audio / video / sensors — though Ch 9 only walks images). The chapter is organized around three architecturally distinct moves, each walked intuition → mechanism → runnable code: **(1) [[VisionTransformer|Vision Transformer (ViT)]]** — adapting the Transformer encoder to images by tokenizing the image into [[PatchEmbedding|patches]] and treating patch embeddings the same way as text token embeddings; **(2) [[CLIP|Contrastive Language-Image Pre-training (CLIP)]]** — a multimodal *embedding* model that projects images and texts into the **same vector space** via [[ContrastiveLearning|contrastive learning]] on (image, caption) pairs, demonstrated via [[OpenCLIP]] (`openai/clip-vit-base-patch32`) on an AI-generated puppy-in-the-snow image; **(3) [[BLIP2|BLIP-2]]** — a multimodal *generative* model that bridges a frozen [[VisionTransformer|ViT]] and a frozen LLM via the trainable **[[QFormer|Querying Transformer (Q-Former)]]**, demonstrated on a supercar image for both [[ImageCaptioning|image captioning]] and [[VisualQuestionAnswering|chat-based visual question answering]].

Ch 9 is **the wiki's first runnable end-to-end vision-language pipeline** ([[Salesforce|Salesforce]]'s `Salesforce/blip2-opt-2.7b` loaded via `transformers.Blip2ForConditionalGeneration` + `AutoProcessor`). Where prior wiki coverage of multimodality was either **discipline-level framing** ([[ai-engineering-ch03-evaluation-methodology|Huyen Ch 3]] on [[MultimodalEmbeddingSpace|multimodal embedding spaces]] + [[ImageBind]] + [[ULIP]]), **architectural pattern recognition** ([[2408.08849-ecg-chat|ECG-Chat]] / [[MultimodalLLM]] codifying the [[LLaVA15|LLaVA]] adapter-on-frozen-encoder pattern), or **native-multimodality contrast** ([[nativemultimodality|Gemini's]] from-the-start joint pretraining), Ch 9 is the **pedagogical bridge** — the chapter that runs both a CLIP-style embedding model and a BLIP-2 generative model with concrete shapes (`torch.Size([1, 512])` text/image embeddings; `224 × 224` preprocessed pixel tensor; `0.33` puppy/caption similarity) on a consumer-GPU notebook. The chapter's central mechanical observation is that **the moment the patch embeddings are passed to the encoder, they are treated as if they were textual tokens** — *"from that point forward, there is no difference in how a text or image trains."* This sameness-after-tokenization is the structural reason the Transformer generalizes from language to vision and what makes adapter-style multimodal LLMs (BLIP-2 / LLaVA / Idefics 2) work.

The chapter forward-references **Chapter 10** (training and fine-tuning embedding models — Ch 9's deferred *"as we will see in Chapter 10, to make sure the representations are as accurate as possible, negative examples ... should also be included in the training process"*) and closes Part II of the book before opening **Part III** on training and fine-tuning. The book treats Ch 9 as the **multimodal capstone** of Part II — after walking text classification (Ch 4), clustering / topic modeling (Ch 5), prompt engineering (Ch 6), advanced text generation (Ch 7), and semantic search / RAG (Ch 8), the same Transformer machinery is finally extended out of language into vision.

Six things the chapter introduces at runnable-code granularity that the wiki did not previously cover: **(1)** the [[VisionTransformer|ViT]] *"tokenization-by-patching"* construction made explicit as the structural analog to text tokenization (image → 16×16 patches → linear projection → patch embeddings → encoder); **(2)** the [[CLIP]] training algorithm walked in three figures (encode image + text → compute pairwise cosine similarity → optimize similarity to maximize-paired / minimize-unpaired); **(3)** the [[OpenCLIP]] worked-code recipe via `transformers.CLIPModel` / `CLIPTokenizerFast` / `CLIPProcessor` on `openai/clip-vit-base-patch32` with the concrete observation that **CLIP uses `[CLS]` to represent the image embedding, not the text embedding** — *"In CLIP, the [CLS] token is actually used to represent the image embedding"* (the inverse of BERT's convention); **(4)** the [[BLIP2|BLIP-2]] architecture decomposed into **two training stages** ([[QFormer|Q-Former]] representation learning + LLM soft-prompting) with the **three Q-Former objectives** ([[ImageTextContrastive|image-text contrastive]] / [[ImageTextMatching|image-text matching]] / [[ImageGroundedTextGeneration|image-grounded text generation]]) — **the wiki's first concrete architectural recipe for an adapter-on-frozen-encoder multimodal LLM**; **(5)** the [[SoftVisualPrompt|soft visual prompt]] mechanism — *"these embeddings serve as soft visual prompts that condition the LLM on the visual representations that were extracted by the Q-Former"* — the wiki's first runnable instance of soft-prompting where the soft prompt is **derived from a non-text encoder**; **(6)** [[VisualQuestionAnswering|visual question answering]] as **chat-based prompting around an image** — using `prompt = "Question: ... Answer:"` and feeding it together with `image` through the same `Blip2Processor` + `model.generate` call to perform multimodal chat (worked example: supercar image + *"What would it cost me to drive that car?"* → *"$1,000,000"*).

## Key Claims

- **Multimodality is the union of modalities a model can handle.** *"A model that is able to handle text and images (each of which is called a modality) is said to be multimodal ... It's possible for a model to accept a modality as input yet not be able to generate in that modality."* (The asymmetry between input-modality and output-modality is established up front — most adapter-style multimodal LLMs accept images but only emit text.)
- **Why multimodality matters for LLMs.** *"In practice, language does not solely live in a vacuum. As an example, your body language, facial expressions, intonation, etc. are all methods of communication that enhance the spoken word. The same thing applies to LLMs; if we can enable them to reason about multimodal information, their capabilities might increase and we become able to deploy them to solve new kinds of problems."*

### Vision Transformer (ViT)

- **ViT is the Transformer encoder applied to images.** *"The method they came up with is called the Vision Transformer (ViT), which has been shown to do tremendously well on image recognition tasks compared to the previously default convolutional neural networks (CNNs)."* Cited as **Dosovitskiy et al. 2020** *"An image is worth 16x16 words: Transformers for image recognition at scale"* (arXiv:2010.11929).
- **ViT relies on the encoder, not the decoder.** *"ViT relies on an important component of the Transformer architecture, namely the encoder. ... the encoder is responsible for converting textual input into numerical representations before being passed to the decoder."* ViT is encoder-only.
- **The bottleneck is the image-tokenization step.** *"Since an image does not consist of words this tokenization process cannot be used for visual data. Instead, the authors of ViT came up with a method for tokenizing images into 'words,' which allowed them to use the original encoder structure."*
- **Patches are the image-tokens.** *"Instead of splitting up text into tokens, it converts the original image into patches of images. In other words, it cuts the image into a number of pieces horizontally and vertically."*
- **Patches → linear embeddings.** *"Unlike tokens, we cannot just assign each patch with an ID since these patches will rarely be found in other images, unlike the vocabulary of a text. Instead, the patches are linearly embedded to create numerical representations, namely embeddings."*
- **16×16 is the canonical patch size.** *"For illustrative purposes, the images in the examples were patched into 3 × 3 patches but the original implementation used 16 × 16 patches. After all, the paper is called 'An Image is Worth 16x16 Words.'"*
- **The structural punchline that justifies multimodal-by-adapter:** *"What is so interesting about this approach is that the moment the embeddings are passed to the encoder, they are treated as if they were textual tokens. From that point forward, there is no difference in how a text or image trains."*
- **ViT is used to make language models multimodal.** *"Due to these similarities, the ViT is often used to make all kinds of language models multimodal. One of the most straightforward ways to use it is during the training of embedding models."* (The bridge between Ch 9's first section (ViT) and second section ([[CLIP]]).)

### Multimodal Embedding Models — [[CLIP]]

- **Multimodal embedding models project multiple modalities into a shared vector space.** *"Multimodal embedding models can create embeddings for multiple modalities in the same vector space ... Despite having coming from different modalities, embeddings with similar meaning will be close to each other in vector space."*
- **The application is cross-modal retrieval.** *"For instance, using such a multimodal embedding model, we can find images based on input text. What images would we find if we search for images similar to 'pictures of a puppy'? Vice versa would also be possible. Which documents are best related to this question?"* — **text-to-image retrieval** and **image-to-text retrieval** are framed as the same dot-product-in-shared-space operation.
- **[[CLIP]] is the current canonical multimodal embedding model.** *"There are a number of multimodal embedding models, but the most well-known and currently most-used model is Contrastive Language-Image Pre-training (CLIP)."* Cited as **Radford et al. 2021** *"Learning transferable visual models from natural language supervision"* (ICML 2021, PMLR).
- **Four CLIP applications named:** **[[ZeroShotClassification|zero-shot classification]]** (compare an image's embedding to embeddings of class descriptions); **clustering** (cluster both images and keywords; the keywords-per-cluster fall out as captions); **search** (text → images or image → texts across billions of items); **generation** (drive image generation as in [[StableDiffusion|stable diffusion]] — citing Rombach et al. 2022).
- **CLIP's training procedure decomposed into three steps:**
  1. **Encode image and text separately.** *"CLIP uses a text encoder to embed text and an image encoder to embed images. ... the result is an embedding for both the image and its corresponding caption."*
  2. **Compare via [[CosineSimilarity|cosine similarity]].** *"The pair of embeddings that are generated are compared through cosine similarity ... the cosine of the angle between vectors, which is calculated through the dot product of the embeddings and divided by the product of their lengths."*
  3. **Update encoders to optimize the similarity.** *"During training, we optimize for the similarity between the embeddings and want to maximize them for similar image/caption pairs and minimize them for dissimilar image/caption pairs."* — this paradigm is named **[[ContrastiveLearning|contrastive learning]]** with the forward-reference *"we will go in depth into its inner workings in Chapter 10 where we will create our own embedding model."*
- **Why contrastive learning needs negatives.** *"Eventually, we expect the embedding of an image of a cat would be similar to the embedding of the phrase 'a picture of a cat.' As we will see in Chapter 10, to make sure the representations are as accurate as possible, negative examples of images and captions that are not related should also be included in the training process. Modeling similarity is not only knowing what makes things similar to one another, but also what makes them different and dissimilar."*

### [[OpenCLIP]] — the worked code example

- **The worked example uses [[OpenCLIP]] via `transformers`.** Three Hugging Face classes loaded for `openai/clip-vit-base-patch32`:
  - **`CLIPTokenizerFast`** — tokenizes text.
  - **`CLIPProcessor`** — preprocesses and resizes images.
  - **`CLIPModel`** — converts both into embeddings.
- **CLIP's text tokenization is wrapped with `<|startoftext|>` / `<|endoftext|>`.** Worked example: `caption = "a puppy playing in the snow"` → `['<|startoftext|>', 'a</w>', 'puppy</w>', 'playing</w>', 'in</w>', 'the</w>', 'snow</w>', '<|endoftext|>']`. The chapter notes: *"the [CLS] token is missing. In CLIP, the [CLS] token is actually used to represent the image embedding."* (This is the inverse of [[bert|BERT]]'s convention where `[CLS]` is the text-side aggregator.)
- **Image preprocessing resizes the input to 224 × 224 pixels.** The worked input (an AI-generated puppy in the snow) was 512 × 512; the preprocessor reduces it to `torch.Size([1, 3, 224, 224])`. *"all the original different shapes of the image will be processed into squares. So be careful inputting very wide or tall images as they might get distorted."*
- **Both text and image embeddings live in the same 512-dim space.** `text_embedding.shape == image_embedding.shape == torch.Size([1, 512])`. *"This is important as it allows us to compare their embeddings and see if they are similar."*
- **Similarity score = normalized dot product.** After L2-normalizing both embeddings, the dot product gives `0.33` similarity between the puppy image and *"a puppy playing in the snow."* The chapter notes 0.33 is hard to interpret in isolation but on a 3×3 similarity matrix of three images and three captions, it is the highest in the row — so **0.33 is high for CLIP's distribution**, not low in absolute terms.
- **The [[SentenceTransformers|sentence-transformers]] CLIP wrapper exists** — `SentenceTransformer("clip-ViT-B-32")` lets you call `.encode(images)` and `.encode(captions)` and `util.cos_sim(...)` in *"only ... a few lines of code."*

### Making Text Generation Models Multimodal — [[BLIP2|BLIP-2]]

- **Text generation models are limited to the modality they were trained on.** *"Models like Llama 2 and ChatGPT excel at reasoning about textual information and responding with natural language. They are, however, limited to the modality they were trained in, namely text."*
- **The goal is to add visual reasoning to text generation.** Worked motivating examples: *"we could give it an image of a pizza and ask it what ingredients it contains. You could show it a picture of the Eiffel Tower and ask when it was built or where it is located."*
- **[[BLIP2|BLIP-2]] is the chapter's worked multimodal text-generation model.** *"One such method is called BLIP-2: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation 2."* Cited as **Li et al. 2023** *"BLIP-2: Bootstrapping language-image pretraining with frozen image encoders and large language models"* (ICML 2023, PMLR).
- **Why bridge instead of train from scratch.** *"Creating a multimodal language model from scratch requires significant computing power and data. We would have to use billions of images, text, and image-text pairs to create such a model. ... Instead of building the architecture from scratch, BLIP-2 bridges the vision-language gap by building a bridge, named the Querying Transformer (Q-Former), that connects a pretrained image encoder and a pretrained LLM."*
- **Only the bridge is trained.** *"By leveraging pretrained models, BLIP-2 only needs to train the bridge without needing to train the image encoder and LLM from scratch."* — the [[VisionTransformer|ViT]] and the LLM are both **frozen**; only the [[QFormer|Q-Former]] (and the projection layer feeding the LLM) is trainable.
- **The [[QFormer|Q-Former]] is a two-module transformer that mimics both sides:**
  - **An Image Transformer** that interacts with the frozen [[VisionTransformer|ViT]] for feature extraction.
  - **A Text Transformer** that interacts with the LLM.
  - The two modules **share their attention layers** — this is the structural device that lets the Q-Former learn a representation that is simultaneously image-shaped and text-shaped.
- **[[QFormer|Q-Former]] training stage 1 — joint representation learning on three contrastive-like tasks:**
  1. **[[ImageTextContrastive|Image-text contrastive learning]]** — align (image, text) pairs to maximize their mutual information.
  2. **[[ImageTextMatching|Image-text matching]]** — a binary classification task: *"predict whether an image and text pair is positive (matched) or negative (unmatched)."*
  3. **[[ImageGroundedTextGeneration|Image-grounded text generation]]** — *"trains the model to generate text based on information extracted from the input image."*
  - *"These three objectives are jointly optimized to improve the visual representations that are extracted from the frozen ViT. In a way, we are trying to inject textual information into the embeddings of the frozen ViT so that we can use them in the LLM."*
- **[[QFormer|Q-Former]] training stage 2 — soft visual prompts.** *"The learnable embeddings derived from step 1 now contain visual information in the same dimensional space as the corresponding textual information. The learnable embeddings are then passed to the LLM. In a way, these embeddings serve as soft visual prompts that condition the LLM on the visual representations that were extracted by the Q-Former."*
- **A linear projection layer is inserted between the Q-Former and the LLM.** *"There is also a fully connected linear layer in between them to make sure that the learnable embeddings have the same shape as the LLM expects."* (This is the same architectural slot LLaVA-style adapters fill with their 2-layer MLP projector — see [[MultimodalLLM]].)
- **Putting it together — the [[SoftVisualPrompt|soft visual prompt]] equivalence.** *"As a result, the LLM will be given information about the image in a similar manner to the context you would provide an LLM when prompting."* The Q-Former-mediated visual features arrive at the LLM in the same role as a textual prompt would — soft, continuous, and conditioning.
- **BLIP-2 is one of several adapter-style multimodal LLMs.** *"Since BLIP-2, many other visual LLMs have been released that have similar processes, like LLaVA, a framework for making textual LLMs multimodal or Idefics 2, an efficient visual LLM based on the Mistral 7B LLM."* — cites **Liu et al. 2024** *"Visual instruction tuning"* (NeurIPS 36, the [[LLaVA15|LLaVA]] paper) and **Laurençon et al. 2024** *"What matters when building vision-language models?"* (arXiv:2405.02246, the [[Idefics2]] paper).
- **The common architectural goal.** *"Both visual LLMs, although having different architectures, connect pretrained CLIP-like visual encoders with textual LLMs. The goal of these architectures is to project visual features from the input images to language embeddings such that they can be used as the input for an LLM. Similar to the Q-Former, they attempt to bridge the gap between images and text."*

### BLIP-2 worked-code receipt

- **Loading the [[BLIP2|BLIP-2]] model.** The chapter uses [[Salesforce]]'s `Salesforce/blip2-opt-2.7b` checkpoint via `transformers.Blip2ForConditionalGeneration` + `transformers.AutoProcessor`, loaded in `torch.float16` and moved to GPU when available.
- **Inspecting the wrapped sub-models.** *"Using `model.vision_model` and `model.language_model`, we can see which ViT and generative model are used, respectively, in the BLIP-2 model we loaded."*
- **The processor is the multimodal analog of the tokenizer.** *"The processor can be compared to the tokenizer of language models. It converts unstructured input, such as images and text, to representations that the model generally expects."* — `Blip2Processor` is a single object that handles both image preprocessing and text tokenization.
- **Image preprocessing also resizes to 224 × 224.** The chapter loads a 520 × 492 supercar image; `blip_processor(image, return_tensors="pt")` produces `torch.Size([1, 3, 224, 224])`. *"all the original different shapes of the image will be processed into squares. So be careful inputting very wide or tall images as they might get distorted."*
- **The text tokenizer is a `GPT2TokenizerFast`** (since the LLM backbone is OPT-2.7b, which uses the GPT-2-style BPE tokenizer family). Inspection of `blip_processor.tokenizer` reveals `vocab_size=50265`, BOS/EOS/UNK = `</s>`, PAD = `<pad>`. Worked tokenization of *"Her vocalization was remarkably melodic"* → `['</s>', 'Her', 'Ġvocal', 'ization', 'Ġwas', 'Ġremarkably', 'Ġmel', 'odic']`.
- **The Ġ-symbol-as-space convention.** *"This is actually supposed to be a space. However, an internal function takes characters in certain code points and moves them up by 256 to make them printable. As a result, the space (code point 32) becomes Ġ (code point 288)."* — Ch 9 codifies the BPE-byte-level-space convention.

### Use Case 1: [[ImageCaptioning|Image Captioning]]

- **Image captioning is the simplest [[BLIP2|BLIP-2]] use case.** *"The most straightforward usage of a model like BLIP-2 is to create captions of images that you have in your data. You might be a store that wants to create descriptions of its clothing or perhaps you are a photographer that does not have the time to manually label the 1,000+ pictures of a wedding."*
- **The pipeline matches the standard generation loop, with images replacing text input.** *"An image is converted to pixel values that the model can read. These pixel values are passed to BLIP-2 to be converted into soft visual prompts that the LLM can use to decide on a proper caption."*
- **Worked example.** A supercar image → `inputs = blip_processor(image, return_tensors="pt")` → `generated_ids = model.generate(**inputs, max_new_tokens=20)` → `blip_processor.batch_decode(generated_ids, skip_special_tokens=True)` → **`"an orange supercar driving on the road at sunset"`** — *"This seems like a perfect description for this image!"*
- **The Rorschach test as a fun stress-test.** The chapter ends the captioning use case with a Rorschach inkblot image (from Wikipedia) → caption **`"a black and white ink drawing of a bat"`**. *"I can definitely see how the model would caption this image using such a description. Since this is a Rorschach test, what do you think it says about the model?"* (A light-touch flag of the **training-data-distribution-as-model-personality** observation.)
- **Domain-specific images may fail.** *"Domain-specific images, like pictures of specific cartoon characters or imaginary creations, may fail as the model was trained on largely public data."* (The Ch 9 analog of [[hands-on-llm-ch08-semantic-search-and-rag|Ch 8's]] dense-retrieval-domain-transfer caveat — multimodal models inherit the same out-of-distribution failure mode.)

### Use Case 2: [[VisualQuestionAnswering|Visual Question Answering]] / Multimodal Chat

- **VQA extends captioning by giving the model an explicit question alongside the image.** *"Instead of following this linear structure, we can try to present both modalities simultaneously by performing what is called visual question answering. In this particular use case, we give the model an image along with a question about that specific image for it to answer. The model needs to process both the image as well as the question at once."*
- **The interface trick: prompt the BLIP-2 processor with both `image` and `text`.** Without a prompt the model captions; with a prompt it answers. Worked example: supercar image + `prompt = "Question: Write down what you see in this picture. Answer:"` → **`"A sports car driving on the road at sunset"`** (essentially a caption — the question was a paraphrase of captioning).
- **Multi-turn chat is implemented by concatenating prior Q/A into the prompt.** *"To do so, we can give the model our previous conversation, including its answer to our question. We then ask it a follow-up question."* Worked second turn — `prompt = "Question: Write down what you see in this picture. Answer: A sports car driving on the road at sunset. Question: What would it cost me to drive that car? Answer:"` → **`"$1,000,000"`** — *"highly specific! This shows more chat-like behavior from BLIP-2, which allows for some interesting conversations."*
- **The chapter ends with an `ipywidgets`-based interactive chatbot** over a single fixed image — `Question: ... Answer: ...` template, a running `memory` list of `(question, answer)` tuples, and a `widgets.Text()` event handler that re-renders BLIP-2's response. *"Using this chat-based approach, we essentially created a chatbot that can reason about images!"*

## Key Quotes

> *"A model that is able to handle text and images (each of which is called a modality) is said to be multimodal ... It's possible for a model to accept a modality as input yet not be able to generate in that modality."* — Ch 9's opening definition; the input-output asymmetry that justifies the adapter pattern.

> *"What is so interesting about this approach is that the moment the embeddings are passed to the encoder, they are treated as if they were textual tokens. From that point forward, there is no difference in how a text or image trains."* — The structural punchline of [[VisionTransformer|ViT]].

> *"There are a number of multimodal embedding models, but the most well-known and currently most-used model is Contrastive Language-Image Pre-training (CLIP)."* — Ch 9's canonization of [[CLIP]] as the field's reference multimodal embedding model.

> *"In CLIP, the [CLS] token is actually used to represent the image embedding."* — A wiki-novel observation: CLIP inverts BERT's `[CLS]` convention so that the special token marks the image side rather than the text side.

> *"Instead of building the architecture from scratch, BLIP-2 bridges the vision-language gap by building a bridge, named the Querying Transformer (Q-Former), that connects a pretrained image encoder and a pretrained LLM."* — The compute-efficiency thesis behind adapter-style multimodal LLMs.

> *"These embeddings serve as soft visual prompts that condition the LLM on the visual representations that were extracted by the Q-Former."* — The [[SoftVisualPrompt|soft-visual-prompt]] equivalence; multimodal input arrives at the LLM in the same architectural role as a soft text prompt.

> *"Both visual LLMs, although having different architectures, connect pretrained CLIP-like visual encoders with textual LLMs. The goal of these architectures is to project visual features from the input images to language embeddings such that they can be used as the input for an LLM."* — Ch 9's generalization from [[BLIP2|BLIP-2]] to the broader [[LLaVA15|LLaVA]] / [[Idefics2|Idefics-2]] family.

## Connections

### Entities
- [[JayAlammar]] / [[MaartenGrootendorst]] — co-authors.
- [[OReilly]] — publisher.
- [[HandsOnLLM]] — book this chapter belongs to.
- [[OpenCLIP]] — the open-source CLIP variant used in the worked code.
- [[openai]] — original [[CLIP]] author lab.
- [[Salesforce]] — author of the [[BLIP2|BLIP-2]] model checkpoint (`Salesforce/blip2-opt-2.7b`).
- [[meta]] — author of OPT-2.7b, the LLM backbone inside the BLIP-2 checkpoint used.
- [[Idefics2]] — Hugging Face's [[Mistral|Mistral-7B]]-based adapter-style multimodal LLM cited as a contemporary of [[BLIP2|BLIP-2]] and [[LLaVA15|LLaVA]].
- [[HuggingFace]] — `transformers` (`CLIPModel` / `CLIPTokenizerFast` / `CLIPProcessor` / `Blip2ForConditionalGeneration` / `AutoProcessor`); host of the worked checkpoints.
- [[SentenceTransformers]] — Ch 9's named easy-mode wrapper for CLIP (`SentenceTransformer("clip-ViT-B-32")`).
- [[StableDiffusion]] — named in Ch 9 as the canonical downstream use of multimodal embeddings for **generation** (citing Rombach et al. 2022).
- [[GPT2]] — Ch 9 reveals the BLIP-2 OPT-2.7b backbone uses `GPT2TokenizerFast` (GPT-2-family BPE tokenizer); the Ġ-as-space convention is codified.

### Concepts
- [[VisionTransformer]] — Dosovitskiy et al. 2020; Ch 9's vision-encoder backbone.
- [[PatchEmbedding]] — the *"tokenization-by-patching"* primitive ViT introduces.
- [[CLIP]] — Radford et al. 2021; Ch 9's worked multimodal-embedding model.
- [[ContrastiveLearning]] — the training paradigm behind CLIP.
- [[CosineSimilarity]] — the metric that quantifies image-text alignment.
- [[NaturalLanguageSupervision]] — the supervision paradigm CLIP pioneered (used by Huyen Ch 1; reaffirmed in Ch 9).
- [[MultimodalEmbeddingSpace]] — the shared vector space CLIP / [[ULIP]] / [[ImageBind]] produce.
- [[ZeroShotClassification]] — one of the four named CLIP applications (compare image embedding to class-description embeddings).
- [[BLIP2]] — Li et al. 2023; Ch 9's worked multimodal text-generation model.
- [[QFormer]] — the Querying Transformer bridge inside [[BLIP2|BLIP-2]].
- [[ImageTextContrastive]] / [[ImageTextMatching]] / [[ImageGroundedTextGeneration]] — the three Q-Former stage-1 objectives.
- [[SoftVisualPrompt]] — the soft-prompt mechanism by which Q-Former outputs condition the LLM.
- [[MultimodalLLM]] — the pattern category [[BLIP2|BLIP-2]] / [[LLaVA15|LLaVA]] / [[Idefics2|Idefics-2]] instantiate.
- [[ImageCaptioning]] — Ch 9 Use Case 1.
- [[VisualQuestionAnswering]] — Ch 9 Use Case 2.
- [[ImageEncoder]] — the role the frozen [[VisionTransformer|ViT]] plays in [[BLIP2|BLIP-2]].
- [[FoundationModel]] — the broader category that includes both CLIP-style and BLIP-2-style multimodal models.

### Prior wiki sources Ch 9 connects to
- [[ai-engineering-ch03-evaluation-methodology]] — Huyen's [[MultimodalEmbeddingSpace]] framing names CLIP / ULIP / ImageBind as the three reference multimodal embedding models. Ch 9 walks the **first** of those at runnable-code granularity.
- [[ai-engineering-ch06-rag-agents]] — Huyen's [[MultimodalRAG|multimodal RAG]] receipt uses CLIP as the retriever backbone; Ch 9 supplies the worked code for the CLIP half of that recipe.
- [[2408.08849-ecg-chat]] — first wiki record of an adapter-style multimodal LLM; cites [[LLaVA15|LLaVA-v1.5]] as the architectural precedent. Ch 9 supplies the **pedagogical origin** ([[BLIP2|BLIP-2]] = the canonical first adapter-style multimodal LLM that LLaVA simplified).
- [[2312.11805-gemini]] — [[nativemultimodality|native multimodality]] is the architectural alternative to Ch 9's adapter-on-frozen-encoder pattern.
- [[hands-on-llm-ch01-introduction-to-llms]] — Ch 9 extends the book's text-only LLM curriculum into vision; the [[transformer|Transformer]] machinery is the same.
- [[hands-on-llm-ch03-looking-inside-llms]] — the Transformer block Ch 9 reuses as the [[VisionTransformer|ViT]] encoder.
- [[hands-on-llm-ch10-creating-text-embedding-models]] *(forward-referenced)* — Ch 10 walks contrastive learning end-to-end; Ch 9 explicitly forward-references it for the negatives / loss-form treatment.

## Contradictions

- **None direct.** Ch 9's content is consistent with the prior wiki's multimodal coverage. Soft consistency notes:
  - **CLIP's `[CLS]` token convention.** Ch 9's statement *"In CLIP, the [CLS] token is actually used to represent the image embedding"* is the **inverse of [[bert|BERT]]'s convention** (where `[CLS]` is the text-side aggregator) — flagged on [[ClsToken]] as a CLIP-specific override, not a contradiction.
  - **Adapter vs native multimodality.** Ch 9's BLIP-2 / LLaVA / Idefics-2 pattern is the **adapter-on-frozen-encoder** family. [[nativemultimodality|Gemini's]] native-multimodality stance argues this family caps cross-modal reasoning at the projector bottleneck. Both stances coexist on [[MultimodalLLM]] as architecturally distinct regimes for the same problem; Ch 9 does not claim adapter-style is universally superior — it claims it is **compute-feasible** (*"easily feasible"*) where native multimodality is not.
  - **ViT vs CNN.** Ch 9 frames ViT as *"shown to do tremendously well on image recognition tasks compared to the previously default convolutional neural networks (CNNs)."* This is consistent with the existing [[VisionTransformer]] page's *"scalability trumps inductive biases"* thesis from Dosovitskiy et al.; the small-data caveat ([[VisionTransformer]] notes ViT *does not* beat ResNet on ImageNet-1k without 300M-image pretraining) is not contradicted by Ch 9, just not mentioned.
  - **Image preprocessing distortion warning.** Ch 9's *"all the original different shapes of the image will be processed into squares. So be careful inputting very wide or tall images as they might get distorted"* is consistent with the wiki's general embedding-input-preprocessing-as-load-bearing-step framing; no prior source contradicted it.
  - **The Ġ-as-space BPE convention.** Ch 9 codifies the BPE byte-level encoder's space-marking trick (space code-point 32 → Ġ code-point 288). Consistent with [[BPE]] and [[ByteLevelTokenization]]; this is the wiki's first explicit narration of the code-point-shift mechanism.
