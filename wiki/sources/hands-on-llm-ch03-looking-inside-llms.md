---
title: "Hands-On LLMs Ch 3 — Looking Inside Large Language Models"
type: source
tags: [book, hands-on-llm, oreilly, llm, transformer, attention, kv-cache, rope, gqa, mqa, flashattention]
date: 2024-01-01
source_file: raw/books/hands-on-llm/ch03-looking-inside-llms.md
book: "Hands-On Large Language Models"
book_isbn13: "9781098150969"
book_authors: ["Jay Alammar", "Maarten Grootendorst"]
book_publisher: "O'Reilly Media"
book_year: 2024
---

# Hands-On LLMs Ch 3 — Looking Inside Large Language Models

## Summary

The third chapter of [[JayAlammar|Jay Alammar]] and [[MaartenGrootendorst|Maarten Grootendorst]]'s *Hands-On Large Language Models* ([[OReilly|O'Reilly Media]], 2024, ISBN 978-1-098-15096-9) is the book's **internals deep-dive on the [[transformer|Transformer]] LLM** — *"the main intuitions of how Transformer language models work"* with text-generation models in particular as the focus. It opens with the **autoregressive token-by-token generation loop** (one [[forwardpass|forward pass]] per output token; each generated token appended to the prompt for the next pass) and breaks the model into three components: the **[[Tokenizer|tokenizer]]**, a **stack of [[transformer|Transformer blocks]]**, and the **[[LMHead|language modeling head]]** that turns the final hidden state into a probability distribution over the vocabulary. A worked example loads `microsoft/Phi-3-mini-4k-instruct` ([[Phi3Mini|Phi-3-mini]]) — 32,064-token vocabulary, 3,072-dim embeddings, **32 `Phi3DecoderLayer` blocks**, each containing a `Phi3Attention` (with `qkv_proj`, `o_proj`, and `Phi3RotaryEmbedding`) and a `Phi3MLP` (`gate_up_proj` → `SiLU` → `down_proj`) wrapped in `Phi3RMSNorm` pre-normalization — then prints `Paris` as the most-probable next token for *"The capital of France is"* by running input through `model.model` and then `model.lm_head`.

The chapter then introduces **parallel token-stream processing**: each input token *"flows through its own computation path"* with limited cross-stream interaction in attention steps; the count of these streams is the **[[ContextLength|context length]]**. Only the **last stream's output** is fed to the LM head for next-token prediction, but every earlier stream's intermediate computations are needed because the attention layers consume them. The **[[KVCache|keys-and-values cache]]** falls out naturally: by caching K and V from previous tokens, decoding step $t+1$ only computes one new stream — Hugging Face Transformers enables this by default (`use_cache=True`); the chapter measures a **4.5 s vs 21.8 s** speedup on a Colab T4 generating 100 tokens with [[Phi3Mini|Phi-3-mini]].

Inside each [[transformer|Transformer block]] sit two sublayers: the **[[FeedForwardNetwork|feedforward network (MLP)]]** — *"the source of [the model's] information"*, the locus of memorization and interpolation (the chapter's *"The Shawshank ___"* → `Redemption` example) — and the **[[selfattention|self-attention]]** layer that incorporates contextual information (*"The dog chased the squirrel because it ___"*: attention determines whether *"it"* refers to *the dog* or *the squirrel*). The chapter walks attention in two steps — (1) **relevance scoring** by multiplying the current position's query vector with the keys matrix and applying [[Softmax|softmax]] to get attention weights, then (2) **combining information** by weighted sum over value vectors — and emphasizes that **three projection matrices (Q, K, V)** are the learned parameters that turn input vectors into queries / keys / values. **[[multiheadattention|Multi-head attention]]** duplicates this calculation in parallel; each head has its own Q/K/V projections and the results are combined.

The chapter's final section is a tour of **recent improvements** to the original 2017 Transformer architecture that show up in 2024-era models like [[Llama|Llama 2]] / [[Llama|Llama 3]]: (1) **efficient-attention variants** — [[LocalAttention|local / sparse attention]] (used by [[GPT3|GPT-3]] which interleaves full and sparse blocks), **[[SlidingWindowAttention|sliding-window attention]]** (Longformer), **[[multiqueryattention|multi-query attention]] (MQA)** which shares one K/V projection across all heads, and **[[GroupedQueryAttention|grouped-query attention]] (GQA)** which interpolates between MQA and full multi-head by sharing K/V projections within groups of heads (used by Llama 2 and 3); (2) **[[FlashAttention|FlashAttention]]** as a popular GPU-IO-aware implementation that optimizes movement between SRAM and HBM (FlashAttention + FlashAttention-2); (3) **Transformer block tweaks** — **pre-normalization** ([[PreNorm|pre-norm]]) over post-norm, **[[RMSNorm|RMSNorm]]** instead of LayerNorm, and **[[SwiGLU|SwiGLU]]** instead of ReLU; (4) **[[RoPE|rotary positional embeddings (RoPE)]]** — applied at the attention step (mixed into queries and keys just before relevance scoring) rather than added once at the start of the forward pass; encodes both absolute and relative position via vector rotation; (5) **[[SequencePacking|sequence packing]]** as the training-time efficiency technique that motivates the move from absolute to relative-aware positional encodings (multiple short documents share one context window, so absolute position 50 may be the *first* token of a new document); (6) brief notes on the broader Transformer-tweaks survey ("A Survey of Transformers") and the architecture's spread into **computer vision**, **robotics** (RT-X), and **time series**.

## Key Claims

- **Transformer LLMs generate one token at a time**, with each forward pass producing a probability distribution over the vocabulary; the loop appends the chosen token to the prompt and runs again. *"Transformer LLMs generate one token at a time, not the entire text at once."*
- **Three top-level components**: tokenizer (vocabulary → token IDs) → stack of Transformer blocks (the bulk of processing) → **[[LMHead|LM head]]** (a single linear layer mapping the final hidden state to a vocabulary-sized vector of logits). *"The lm_head ... is a simple neural network layer itself. It is one of multiple possible 'heads' to attach to a stack of Transformer blocks."* Other heads include **sequence classification** and **token classification** heads.
- **Phi-3-mini structural read-out**: 32,064-token vocabulary; 3,072-dim embeddings; **32 decoder layers**; per-block components are `qkv_proj` (3072→9216 — fuses Q, K, V projections; the 3× factor reflects the three matrices), `o_proj` (3072→3072 output projection), `Phi3RotaryEmbedding`, `Phi3MLP` (`gate_up_proj`: 3072→16384, `down_proj`: 8192→3072, `SiLU` activation — gated structure consistent with [[SwiGLU|SwiGLU]] / GLU variants), and `Phi3RMSNorm` for both `input_layernorm` and `post_attention_layernorm`. The `lm_head` is `Linear(3072 → 32064)`.
- **The first generated token for *"The capital of France is"* is `Paris`**, recovered by computing `lm_head_output[0, -1].argmax(-1)` over the [1, 6, 32064] logit tensor and decoding the resulting token ID.
- **[[DecodingStrategy|Decoding strategy]] terminology**: choosing the token to emit from the predicted probability distribution is called the **decoding strategy**. *"Choosing the highest scoring token every time is called [[GreedyDecoding|greedy decoding]]. It's what happens if you set the temperature parameter to zero in an LLM."* Adding randomness ([[Sampling|sampling]] from the distribution) usually produces better outputs than greedy decoding for most use cases.
- **Parallel token-stream processing**: *"Each token is processed through its own stream of computation (with some interaction between them in attention steps)."* The count of streams equals the **[[ContextLength|context length]]**; a 4K-context model has 4K streams. Each stream begins with an input vector (token embedding + positional information) and ends with an output vector of the same **model dimension** (3,072 for Phi-3-mini).
- **Only the last stream's output is consumed by the LM head**, but every earlier stream's intermediate outputs are required because the attention sub-layers in each block consume them.
- **[[KVCache|KV cache]] = the central inference-time optimization**: cache K and V projections from previous tokens so step $t+1$ only computes one new stream. *"This is one reason why LLM APIs stream the output tokens as the model generates them instead of waiting for the entire generation to be completed."* **Empirical measurement**: 100-token generation with [[Phi3Mini|Phi-3-mini]] on a Colab T4 takes **4.5 s with `use_cache=True`** vs **21.8 s with `use_cache=False`** — a ~5× speedup. `use_cache` defaults to `True` in Hugging Face Transformers.
- **A Transformer block has two sublayers**: (1) the **[[selfattention|attention layer]]** *"mainly concerned with incorporating relevant information from other input tokens and positions"*; (2) the **[[FeedForwardNetwork|feedforward layer (MLP)]]** *"houses the majority of the model's processing capacity"*. Modern blocks have between 6 (original Transformer) and 100+ (large LLMs) Transformer blocks.
- **The feedforward network is the model's memory and interpolation engine**. *"The feedforward neural network (collectively in all the model layers) is the source of [factual] information ... it learned and stored the information (and behaviors) that make it succeed at this task."* The chapter's *"The Shawshank ___"* → `Redemption` example (referring to the 1994 film) illustrates this. Memorization is *one ingredient*; the same machinery interpolates between data points to generalize to unseen inputs.
- **Raw language models vs chat models**. Raw LMs (like [[GPT3|GPT-3]]) are *"difficult for people to properly utilize"* — they predict next tokens but don't follow instructions. **Instruction-tuning + human-preference fine-tuning** is what turns raw LMs into chat LLMs like [[GPT4|GPT-4]] that respond conversationally to *"The Shawshank"* with a film description rather than the word `Redemption`.
- **Attention's two-step computation** (per attention head, per current position): (1) **relevance scoring** — multiply the current position's **query vector** by the **keys matrix** (all previous tokens' keys); pass through [[Softmax|softmax]] to get a probability distribution that sums to 1 over previous tokens; (2) **combining information** — multiply each previous token's **value vector** by its score, then sum the weighted value vectors to produce the output of attention at this position.
- **Three projection matrices** are the learned attention parameters: the **[[QueryProjection|query projection matrix]]**, **[[KeyProjection|key projection matrix]]**, and **[[ValueProjection|value projection matrix]]**. They project layer inputs into queries / keys / values matrices. The bottom row of each matrix corresponds to the current position; rows above it correspond to previous positions.
- **[[multiheadattention|Multi-head attention]] = attention duplicated and executed in parallel**. *"To give the Transformer more extensive attention capability, the attention mechanism is duplicated and executed multiple times in parallel."* Each parallel pass is an **attention head**; each head has its own Q/K/V projections; *"increases the model's capacity to model complex patterns in the input sequence that require paying attention to different patterns at once."*
- **Decoder Transformer attention is causal**. *"This figure also shows the autoregressive nature of decoder Transformer blocks ... they can only pay attention to previous tokens. Contrast this to [[bert|BERT]], which can pay attention to both sides (hence the B in BERT stands for bidirectional)."*
- **[[LocalAttention|Local / sparse attention]] limits the context each token can attend to**, improving efficiency for long sequences. Citations: *"Generating long sequences with sparse transformers"* (Child et al., for [[GPT3|GPT-3]]'s sparse blocks) and *"Longformer: The long-document transformer"* (Beltagy et al., sliding-window). **[[GPT3|GPT-3]] interweaves full-attention and sparse-attention Transformer blocks** — blocks 1 and 3 are full attention, blocks 2 and 4 are sparse — because *"the quality of the generation would vastly degrade if the model could only see a small number of previous tokens"* if used everywhere.
- **[[multiqueryattention|Multi-query attention (MQA)]]** (citation: *"Fast transformer decoding: One write-head is all you need"*, Shazeer 2019) shares K and V matrices across all attention heads; only the Q matrices remain per-head. Reduces matrix size and improves inference scalability of large models.
- **[[GroupedQueryAttention|Grouped-query attention (GQA)]]** (citation: *"GQA: Training generalized multi-query transformer models from multi-head checkpoints"*, Ainslie et al.) is the interpolation: K and V are shared **within groups of attention heads** instead of across all heads, sacrificing some MQA efficiency for quality. **Used by [[Llama|Llama 2]] and [[Llama|Llama 3]]**. *"As model sizes grow, however, this optimization [MQA] can be too punishing and we can afford to use a little more memory to improve the quality of the models. This is where grouped-query attention comes in."*
- **[[FlashAttention|FlashAttention]]** *"speeds up the attention calculation by optimizing what values are loaded and moved between a GPU's shared memory (SRAM) and high bandwidth memory (HBM)."* Citations: Dao et al. *"FlashAttention: Fast and memory-efficient exact attention with IO-awareness"* and Dao 2023 *"FlashAttention-2: Faster attention with better parallelism and work partitioning"*.
- **Modern Transformer block tweaks**: (i) **pre-normalization** (normalization before attention and FFN, *"reported to reduce the required training time"*, citation: *"On layer normalization in the Transformer architecture"*); (ii) **[[RMSNorm|RMSNorm]]** instead of LayerNorm (*"simpler and more efficient"*, citation: *"Root mean square layer normalization"*); (iii) **[[SwiGLU|SwiGLU]]** instead of ReLU (citation: *"GLU Variants Improve Transformer"* by Shazeer).
- **[[RoPE|Rotary positional embeddings]]** (citation: Su et al. *"RoFormer: Enhanced Transformer with rotary position embedding"*). *"Instead of the static, absolute embeddings that are added in the beginning of the forward pass, rotary embeddings are a method to encode positional information in a way that captures absolute and relative token position information."* Mechanism: rotates vectors in their embedding space; **applied at the attention step** (mixed into queries and keys *"just before we multiply them for relevance scoring"*), not at the start of the forward pass.
- **The motivation for relative-aware positional embeddings is [[SequencePacking|sequence packing]] during training**. *"A lot of documents in the training set are much shorter than that context. It would be inefficient to allocate the entire, say, 4K context to a short 10-word sentence. So during model training, documents are packed together into each context."* Absolute positional embeddings break here: telling the model that the first token of Document 50 (packed at position 50) is at position 50 misleads it into assuming previous context exists. Citation: *"Efficient sequence packing without cross-contamination"*, and Graphcore's *"Introducing packed BERT for 2X training speed-up"*.
- **The original [[1706.03762-attention-is-all-you-need|Transformer]] paper used absolute positional embeddings**, either static (geometric / sinusoidal) or learned. *"Some challenges arise from such methods when we scale up models, which requires us to find ways to improve their efficiency."*
- **Transformer architecture research extends beyond LLMs** — citations to *"Transformers in vision: A survey"* and *"A survey on vision transformer"* (computer vision), *"Open X-Embodiment: Robotic learning datasets and RT-X models"* (robotics), and *"Transformers in time series: A survey"* (time series).

## Key Quotes

> "Transformer LLMs generate one token at a time, not the entire text at once." — Ch 3

> "After each token generation, we tweak the input prompt for the next generation step by appending the output token to the end of the input prompt." — Ch 3

> "There's a specific word used in machine learning to describe models that consume their earlier predictions to make later predictions ... They're called autoregressive models. That is why you'll hear text generation LLMs being called autoregressive models. This is often used to differentiate text generation models from text representation models like BERT, which are not autoregressive." — Ch 3

> "The tokenizer is followed by the neural network: a stack of Transformer blocks that do all of the processing. That stack is then followed by the LM head, which translates the output of the stack into probability scores for what the most likely next token is." — Ch 3

> "The lm_head is a simple neural network layer itself. It is one of multiple possible 'heads' to attach to a stack of Transformer blocks to build different kinds of systems. Other kinds of Transformer heads include sequence classification heads and token classification heads." — Ch 3

> "The method of choosing a single token from the probability distribution is called the decoding strategy. ... Choosing the highest scoring token every time is called greedy decoding. It's what happens if you set the temperature parameter to zero in an LLM." — Ch 3

> "Each of the token streams starts with an input vector (the embedding vector and some positional information; we'll discuss positional embeddings later in the chapter). At the end of the stream, another vector emerges as the result of the model's processing." — Ch 3

> "For text generation, only the output result of the last stream is used to predict the next token. That output vector is the only input into the LM head as it calculates the probabilities of the next token." — Ch 3

> "If we give the model the ability to cache the results of the previous calculation (especially some of the specific vectors in the attention mechanism), we no longer need to repeat the calculations of the previous streams. ... This is an optimization technique called the keys and values (kv) cache and it provides a significant speedup of the generation process." — Ch 3

> "The attention layer is mainly concerned with incorporating relevant information from other input tokens and positions. The feedforward layer houses the majority of the model's processing capacity." — Ch 3

> "The feedforward neural network (collectively in all the model layers) is the source of this information. ... When the model was successfully trained to model a massive text archive (which included many mentions of 'The Shawshank Redemption'), it learned and stored the information (and behaviors) that make it succeed at this task." — Ch 3

> "For an LLM to be successfully trained, it needs to memorize a lot of information. But it is not simply a large database. Memorization is only one ingredient in the recipe of impressive text generation. The model is able to use this same machinery to interpolate between data points and more complex patterns to be able to generalize." — Ch 3

> "Context is vital in order to properly model language. Simple memorization and interpolation based on the previous token can only take us so far. ... Attention is a mechanism that helps the model incorporate context as it's processing a specific token." — Ch 3

> "Attention starts by multiplying the inputs by the projection matrices to create three new matrices. These are called the queries, keys, and values matrices. These matrices contain the information of the input tokens projected to three different spaces that help carry out the two steps of attention: (1) Relevance scoring (2) Combining information." — Ch 3

> "The relevance scoring step of attention is conducted by multiplying the query vector of the current position with the keys matrix. This produces a score stating how relevant each previous token is. Passing that by a softmax operation normalizes these scores so they sum up to 1." — Ch 3

> "To give the Transformer more extensive attention capability, the attention mechanism is duplicated and executed multiple times in parallel. Each of these parallel applications of attention is conducted into an attention head. This increases the model's capacity to model complex patterns in the input sequence that require paying attention to different patterns at once." — Ch 3

> "The way that multi-query attention optimizes this is to share the keys and values matrices between all the heads. So the only unique matrices for each head would be the queries matrices." — Ch 3 (on MQA)

> "As model sizes grow, however, this optimization [MQA] can be too punishing and we can afford to use a little more memory to improve the quality of the models. This is where grouped-query attention comes in. Instead of cutting the number of keys and values matrices to one of each, it allows us to use more (but less than the number of heads)." — Ch 3 (on GQA)

> "Flash Attention is a popular method and implementation that provides significant speedups for both training and inference of Transformer LLMs on GPUs. It speeds up the attention calculation by optimizing what values are loaded and moved between a GPU's shared memory (SRAM) and high bandwidth memory (HBM)." — Ch 3

> "Instead of the static, absolute embeddings that are added in the beginning of the forward pass, rotary embeddings are a method to encode positional information in a way that captures absolute and relative token position information. It is based on the idea of rotating vectors in their embeddings space. In the forward pass, they are added in the attention step." — Ch 3 (on RoPE)

> "During the attention process, the positional information is mixed in specifically to the queries and keys matrices just before we multiply them for relevance scoring." — Ch 3

> "Packing is the process of efficiently organizing short training documents into the context. It includes grouping multiple documents in a single context while minimizing the padding at the end of the context." — Ch 3

## Concepts Introduced or Engaged

- [[transformer|Transformer]] — *engaged*, the chapter's primary subject; the architecture from the inside.
- [[selfattention|Self-attention]] — *engaged*, the chapter walks the mechanism end-to-end.
- [[multiheadattention|Multi-Head Attention]] — *engaged*, the chapter's parallel-heads formulation.
- [[scaleddotproductattention|Scaled Dot-Product Attention]] — *engaged via the two-step framing* (relevance scoring + combining information; the softmax over scores is the same operation).
- [[QueryProjection]] / [[KeyProjection]] / [[ValueProjection]] — *new*, the three learned projection matrices.
- [[multiqueryattention|Multi-Query Attention (MQA)]] — *engaged*, K/V matrices shared across all heads.
- [[GroupedQueryAttention|Grouped-Query Attention (GQA)]] — *new*, K/V shared within groups of heads; used by Llama 2 / 3.
- [[FlashAttention|FlashAttention]] / [[FlashAttention2]] — *engaged*, the IO-aware GPU kernel for attention.
- [[LocalAttention|Local / sparse attention]] — *new*, restricted-context attention used by GPT-3 every other block.
- [[SlidingWindowAttention|Sliding-window attention]] — *new*, Longformer's variant.
- [[KVCache|KV cache]] — *engaged*, the chapter's centerpiece inference optimization.
- [[ContextLength|Context length]] — *engaged*, framed here as "the number of token-processing streams".
- [[forwardpass|Forward pass]] — *engaged*, the unit of token generation.
- [[LMHead|Language modeling head]] — *new*, the final linear layer mapping hidden state to vocab-sized logits.
- [[DecodingStrategy|Decoding strategy]] — *new*, the umbrella term for picking a token from the probability distribution.
- [[GreedyDecoding|Greedy decoding]] — *engaged*, the highest-probability-token strategy (temperature = 0).
- [[Sampling|Sampling]] — *engaged*, the alternative to greedy decoding.
- [[Softmax|Softmax]] — *engaged*, the operation normalizing attention scores to sum to 1.
- [[FeedForwardNetwork|Feedforward network (MLP)]] — *engaged*, the per-block memorization-and-interpolation sublayer.
- [[ResidualConnection|Residual connection]] — *engaged*, the bypass around each sublayer.
- [[LayerNormalization|Layer normalization]] — *engaged*, the original-Transformer normalization the chapter contrasts with RMSNorm.
- [[PreNorm|Pre-normalization]] — *engaged*, the chapter's choice over post-norm for modern LLMs.
- [[RMSNorm|RMSNorm]] — *new*, the simpler-and-more-efficient normalization replacing LayerNorm.
- [[SwiGLU|SwiGLU]] — *new*, the GLU-variant activation replacing ReLU in modern LLMs.
- [[SiLU|SiLU]] — *new*, the activation used by Phi-3's MLP (consistent with the SwiGLU-style gated structure).
- [[ReLU|ReLU]] — *engaged*, the original Transformer activation the chapter compares against.
- [[RoPE|Rotary positional embeddings (RoPE)]] — *new*, the relative-aware positional encoding applied at the attention step.
- [[positionalencoding|Positional encoding]] — *engaged*, the umbrella concept the chapter contrasts absolute vs RoPE.
- [[AutoregressiveLanguageModel|Autoregressive language model]] — *engaged*, the chapter's framing of LM generation.
- [[SequencePacking|Sequence packing]] — *new*, the training-time efficiency technique motivating relative-aware positional encodings.
- [[TokenStream|Token stream]] — *new*, the per-position computation track through the model.
- [[ModelDimension|Model dimension]] — *new*, the shared input/output vector size for each token stream.
- [[AttentionHead|Attention head]] — *new*, one parallel attention computation; multi-head attention is many of these in parallel.
- [[InstructionTuning|Instruction tuning]] — *engaged*, the post-pretraining step that turns raw LMs into chat models.
- [[VisionTransformer|Vision Transformer]] — *engaged via passing reference*, the chapter cites two Transformer-in-vision surveys.

## Entities Introduced or Engaged

- [[JayAlammar]] / [[MaartenGrootendorst]] — *engaged*, co-authors.
- [[HandsOnLLM]] — *engaged*, the book.
- [[Phi3Mini]] — *engaged*, the worked model (`microsoft/Phi-3-mini-4k-instruct`) whose internals the chapter dissects.
- [[microsoft|Microsoft]] — *engaged*, Phi-3 provider.
- [[HuggingFace|Hugging Face]] — *engaged*, source of the `transformers` package whose `use_cache` parameter the chapter demonstrates.
- [[Llama|Llama 2]] / [[Llama|Llama 3]] — *engaged*, the canonical 2024-era models using GQA + RoPE + SwiGLU + RMSNorm + pre-norm.
- [[GPT3|GPT-3]] — *engaged*, named as the model that interleaves full and sparse attention blocks.
- [[GPT4|GPT-4]] — *engaged*, named as the chat-tuned counterexample to raw LMs.
- [[bert|BERT]] — *engaged*, the bidirectional contrast to causal decoder-only LMs.
- [[GoogleColab|Google Colab]] — *engaged*, the runtime environment for the KV-cache speedup measurement (T4 GPU).
- [[TriDao|Tri Dao]] — *engaged via passing reference*, FlashAttention author.
- [[NoamShazeer|Noam Shazeer]] — *new*, author of *"Fast transformer decoding: One write-head is all you need"* (MQA, 2019) and *"GLU Variants Improve Transformer"* (SwiGLU); both papers cited here.

## Connections

- [[hands-on-llm-ch01-introduction-to-llms]] / [[hands-on-llm-ch02-tokens-and-embeddings]] — predecessor chapters; this chapter is the deep-dive on what Ch 1 forward-referenced as *"multi-head attention, positional embeddings, and layer normalization"*.
- [[1706.03762-attention-is-all-you-need]] — the original Transformer paper this chapter walks the modern descendants of.
- [[Phi3Mini]] — the worked model.
- [[transformer]] — the architecture this chapter dissects.
- [[selfattention]] / [[multiheadattention]] / [[scaleddotproductattention]] / [[KVCache]] / [[FlashAttention]] — the existing wiki concept pages this chapter most extensively engages.
- [[multiqueryattention]] / [[GroupedQueryAttention]] / [[LocalAttention]] / [[SlidingWindowAttention]] / [[RoPE]] / [[RMSNorm]] / [[SwiGLU]] / [[SiLU]] / [[LMHead]] / [[SequencePacking]] / [[TokenStream]] / [[ModelDimension]] / [[AttentionHead]] / [[QueryProjection]] / [[KeyProjection]] / [[ValueProjection]] / [[DecodingStrategy]] — new pages this chapter mints.
- [[GreedyDecoding]] / [[ContextLength]] / [[ResidualConnection]] / [[LayerNormalization]] / [[PreNorm]] / [[positionalencoding]] / [[FeedForwardNetwork]] / [[Softmax]] / [[AutoregressiveLanguageModel]] / [[InstructionTuning]] / [[Attention]] / [[forwardpass]] / [[Sampling]] / [[bert]] — pages this chapter engages.

## Contradictions

None directly conflicting with existing wiki content. **Soft consistency notes worth flagging**:

- **RoPE timing of injection.** This chapter states RoPE is *"applied in the attention step, not at the start of the forward pass"* and is *"mixed in specifically to the queries and keys matrices just before we multiply them for relevance scoring"*. This is consistent with the original RoFormer paper (Su et al. 2021) and with [[positionalencoding|the existing PositionalEncoding page]]'s passing note that *"many later models use ... rotary position embeddings (RoPE)"*. No contradiction; the chapter adds the **per-layer-Q/K-injection** mechanism the existing page omits.
- **GQA / MQA framing.** The existing [[multiqueryattention|MQA]] page cites [[2312.11805-gemini|Gemini 1.0]] as a deployment context and notes *"Modern models also use Grouped-Query Attention (GQA) — an interpolation between full multi-head and MQA"*. This chapter's framing is fully consistent and adds the Llama 2 / Llama 3 deployment anchor plus the *"as model sizes grow ... MQA can be too punishing"* motivation.
- **FlashAttention scope.** The existing [[FlashAttention|FlashAttention]] page (sourced from [[2205.14135-flashattention]]) carries the full IO-complexity treatment (Θ(N²d²M⁻¹) HBM accesses, tiling + recomputation). Ch 3 states the chapter-level intuition (*"optimizing what values are loaded and moved between SRAM and HBM"*). No contradiction; the chapter is the pedagogical pointer to the deeper page.
- **KV cache framing.** The existing [[KVCache|KVCache]] page (sourced from [[leh-ch08-inference-optimization|LEH Ch 8]]) gives the memory formula (`tokens * layers * heads * head_dim * 2 bytes`) and distinguishes dynamic vs [[StaticKVCache|static KV cache]]. Ch 3 is consistent and adds the **5× wall-clock speedup measurement** on Phi-3-mini / T4 / 100 tokens.
- **Causal vs bidirectional attention.** Ch 3's framing — *"decoder Transformer blocks ... can only pay attention to previous tokens. Contrast this to BERT, which can pay attention to both sides"* — is consistent with [[selfattention|self-attention page]]'s masked-decoder-attention treatment and with [[hands-on-llm-ch01-introduction-to-llms|Ch 1]]'s same contrast.
- **The "feedforward stores facts" claim.** Ch 3 states *"the feedforward neural network ... is the source of this information ... it learned and stored the information"*. The existing [[FeedForwardNetwork|FFN page]] (sourced from [[1706.03762-attention-is-all-you-need]] / [[d2l-attention-and-transformers]]) describes the FFN structurally without making this memorization claim. The two are complementary, not contradictory — Ch 3's claim is consistent with the wider mechanistic-interpretability literature (Geva et al. *"Transformer Feed-Forward Layers Are Key-Value Memories"*, 2020) but is not itself cited here.

## Position in the wiki

This is the **third chapter from *Hands-On Large Language Models*** ingested (after [[hands-on-llm-ch01-introduction-to-llms|Ch 1]] and [[hands-on-llm-ch02-tokens-and-embeddings|Ch 2]]) and the **wiki's canonical pedagogical walkthrough of the autoregressive-decoder Transformer LLM from the inside**. It complements rather than replaces the wiki's existing Transformer coverage:

- Where [[1706.03762-attention-is-all-you-need|the original *Attention Is All You Need* page]] is the **formal architectural paper**, and [[ai-engineering-ch02-foundation-models|Huyen's AI Engineering Ch 2]] is the **practitioner inference-time framing** (prefill vs decode, sampling, latency), *Hands-On LLMs* Ch 3 is the **intuition-first walkthrough with a runnable model dissection**. The 32-decoder-layer / 3,072-dim / `qkv_proj` / `Phi3RotaryEmbedding` / `Phi3RMSNorm` / `SiLU` / `gate_up_proj` printout for `microsoft/Phi-3-mini-4k-instruct` is the chapter's headline pedagogical move — showing what the layer-by-layer config actually looks like in modern code.
- **First wiki coverage of the 2024-era Transformer block recipe** as a coherent bundle: pre-norm + RMSNorm + SwiGLU + GQA + RoPE. The wiki had each component covered separately (the modern [[transformer|Transformer page]] notes RoPE in passing; [[multiqueryattention|MQA]] mentions GQA; etc.), but Ch 3 is the first source that puts the whole 2024 block recipe together as the canonical update to the 2017 design.
- **First explicit wiki page for [[KVCache|KV cache]]** as the central inference-time optimization with a **concrete speedup measurement** on a small model and consumer GPU. The existing [[KVCache|KVCache page]] (from [[leh-ch08-inference-optimization|LEH Ch 8]]) carries the memory formula but not the wall-clock measurement on a specific model/hardware.
- **First wiki coverage of [[SequencePacking|sequence packing]]** as the motivation for relative-aware positional encodings.
- **First wiki coverage of [[LMHead|the LM head]] as a named distinct component** — the existing [[transformer|Transformer page]] folds it into "embeddings are shared with the pre-softmax linear transformation", but Ch 3 makes the LM head a first-class architectural component swappable with sequence/token classification heads.

Subsequent chapters (Ch 4: text classification, Ch 5: clustering + topic modeling, Chs 6+: prompt engineering, RAG, multimodal, embedding/fine-tuning) build on the architectural foundation this chapter lays. Ch 3 is the **last theory-first chapter** before the book pivots to applications (Part II).
