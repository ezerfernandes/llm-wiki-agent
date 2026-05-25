---
title: "Hands-On LLMs Ch 6 — Prompt Engineering"
type: source
tags: [book, hands-on-llm, oreilly, llm, prompt-engineering, chain-of-thought, self-consistency, tree-of-thought, in-context-learning, few-shot, output-verification, grammar-constrained-decoding, json, llama-cpp, temperature, top-p, persona, reasoning]
date: 2024-01-01
source_file: raw/books/hands-on-llm/ch06-prompt-engineering.md
book: "Hands-On Large Language Models"
book_isbn13: "9781098150969"
book_authors: ["Jay Alammar", "Maarten Grootendorst"]
book_publisher: "O'Reilly Media"
book_year: 2024
---

# Hands-On LLMs Ch 6 — Prompt Engineering

## Summary

The sixth chapter of [[JayAlammar|Jay Alammar]] and [[MaartenGrootendorst|Maarten Grootendorst]]'s *Hands-On Large Language Models* ([[OReilly|O'Reilly Media]], 2024, ISBN 978-1-098-15096-9) and **the wiki's first chapter from the book that puts the generative-LLM half of the two-bucket organizing axis in the foreground** — opens Part III on "**[[PromptEngineering|prompt engineering]], reasoning with generative models, verification, and even evaluating their output**." Ch 6 is the **pedagogical operationalization** of the generative half of Ch 1's representation-vs-generative split: where Chs 4 and 5 used [[Phi3Mini|Phi-3-mini]] alongside embedding models for classification / clustering, Ch 6 uses [[Phi3Mini|Phi-3-mini]] as the **prompt-driven text generator** and walks the design space of prompt construction, reasoning prompting, and output-format control. The chapter has four movements: (1) **using a text generation model** (model selection — proprietary vs open source; loading via `transformers.pipeline`; the [[ChatTemplate|chat-template]] underlying `messages=[{"role": "user", "content": ...}]`; controlling output via [[Temperature|temperature]] + [[Topp|top_p]] + [[Topk|top_k]]); (2) **intro to prompt engineering** (basic ingredients — instruction + data + output indicator; instruction-based prompting; specificity / [[Hallucination|hallucination]] / order tips); (3) **advanced prompt engineering** (the **seven-component prompt** — [[Persona|persona]] / [[InstructionPrompt|instruction]] / [[ContextPrompt|context]] / [[OutputFormat|format]] / [[AudiencePrompt|audience]] / [[TonePrompt|tone]] / data; [[InContextLearning|in-context learning]] via zero / one / few-shot prompting; **chain prompting** = [[PromptDecomposition|prompt decomposition]] across multiple LLM calls — name → slogan → sales pitch); (4) **reasoning with generative models** ([[System1And2|System 1 vs System 2]] thinking; **[[chainofthought|chain-of-thought]]** with both few-shot examples and the zero-shot *"Let's think step-by-step"* trigger; **[[selfconsistency|self-consistency]]** = N-CoT + majority vote; **[[TreeOfThoughts|tree-of-thought]]** as multi-path search, and a single-prompt "imagine three experts" approximation); (5) **output verification** (the four reasons — structured output / valid output / ethics / accuracy; the three control methods — examples / grammar / fine-tuning; a worked **JSON-grammar-constrained sampling** example with `llama-cpp-python` + the `GGUF` Phi-3 model). The chapter forward-references Ch 7 (memory + tool use beyond prompt chaining) and Ch 12 (fine-tuning as the third output-control lever).

Ch 6 is the **wiki's second book-chapter prompt-engineering treatment** after [[ai-engineering-ch05-prompt-engineering|Huyen's *AI Engineering* Ch 5]]. The two are **highly complementary**: Huyen Ch 5 is the **rigorous-discipline framing** (six best practices, defensive prompt engineering, [[PromptStructure|three-part anatomy]], [[PromptEngineeringTools|tools taxonomy]], hidden-cost warnings); Alammar & Grootendorst Ch 6 is the **modular-component framing** (seven Lego-block prompt parts, build-it-up-iteratively workflow). Where Huyen frames CoT under *"give the model time to think"* alongside [[SelfCritique|self-critique]] and notes four variants in a table, Alammar & Grootendorst walk through CoT both **with examples** (Wei et al. 2022) and **without examples** (zero-shot CoT via *"Let's think step-by-step"*, Kojima et al. 2022) on the same canonical *cafeteria-apples* problem the wiki has now seen in **three places** (Huyen Ch 8's CoT-training data story, [[chainofthought]] page, and now Ch 6's prompt-engineering demonstration). Where Huyen sketches [[selfconsistency]] as the majority-vote variant of [[bestofn|best-of-N]] without code, Alammar & Grootendorst frame it as the natural response to temperature/top_p stochasticity and explicitly note the *n* times slower cost. Where Huyen's [[TreeOfThoughts]] coverage was via [[2402.01817-llm-modulo|Kambhampati et al.'s critique]] (ToT as "prompt diversification on top of an external verifier"), Ch 6 frames ToT both **architecturally** (Yao et al. 2023 multi-path search) and as a **single-prompt conversation-between-experts approximation** — a different operating point.

The chapter introduces **two new things the wiki did not previously cover**: (1) **the seven-component modular prompt** — [[Persona|persona]] + [[InstructionPrompt|instruction]] + [[ContextPrompt|context]] + [[OutputFormat|format]] + [[AudiencePrompt|audience]] + [[TonePrompt|tone]] + data — as an *iterable design surface* where each component can be independently added/removed/reordered to see its effect (Huyen Ch 5's three-part anatomy is *task description / examples / task*; Ch 6's seven-part is a finer decomposition that is **constructively additive** rather than structural); (2) **grammar-constrained decoding in worked code** via `llama-cpp-python` with `response_format={"type": "json_object"}` on a [[GGUF]]-quantized [[Phi3Mini]] — the wiki's first runnable demonstration of [[ConstrainedSampling|constrained sampling]] producing valid JSON, where the [[ConstrainedSampling|existing page]] (from [[ai-engineering-ch02-foundation-models|Huyen Ch 2]]) was conceptual-only. The chapter also makes the **System 1 / System 2 framing explicit** as the **pedagogical motivation for CoT / self-consistency / ToT** — *"if we could give a generative model the ability to mimic a form of self-reflection, we would essentially be emulating the system 2 way of thinking, which tends to produce more thoughtful responses than system 1 thinking"* — adding a Kahneman citation alongside the [[System1And2|existing System1And2 page]]'s coverage from [[2402.01817-llm-modulo]]. Note this is a **constructive use of System 2** (use CoT / ToT to *simulate* System 2 reasoning to improve outputs) which sits in **soft tension** with Kambhampati et al.'s critique on [[System1And2]] that *"a system that takes constant time to produce the next token cannot possibly be doing principled reasoning on its own"* — Ch 6 takes the LLM-resemble-reasoning position and operationalizes it; [[2402.01817-llm-modulo]] critiques it. The two positions are documented side-by-side on [[System1And2]].

## Key Claims

- **Model selection starts with proprietary vs open source.** *"Although proprietary models are generally more performant, we focus in this book more on open source models as they offer more flexibility and are free to use."* The book recommends **starting with a small foundation model** — [[Phi3Mini|Phi-3-mini]] (3.8B params, MIT-licensed, fits in under 8 GB VRAM) — because *"scaling up to larger models tends to be a nicer experience than scaling down."*
- **The `transformers.pipeline` wrapper hides chat-template processing.** Under the hood, `pipe.tokenizer.apply_chat_template(messages, tokenize=False)` converts `messages=[{"role": "user", "content": "..."}]` into the model-specific [[ChatTemplate|chat template]]. For [[Phi3Mini|Phi-3]]:
  ```
  <s><|user|>
  Create a funny joke about chickens.<|end|>
  <|assistant|>
  ```
  The special tokens `<|user|>`, `<|assistant|>`, `<|end|>` were introduced during training; `<|end|>` is also the stopping signal.
- **`do_sample=False` makes the output deterministic** — [[GreedyDecoding|greedy decoding]], always picking the highest-probability next token. To use [[Temperature|temperature]] and [[Topp|top_p]] you must set `do_sample=True`.
- **[[Temperature|Temperature]] controls randomness / creativity.** *"A higher value allows less probable words to be generated."* T=0 → deterministic; T≈0.2 → predictable; T≈0.8 → diverse. Ch 6 frames temperature operationally — *"every time you rerun this piece of code, the output will change"* — without the [[Softmax|softmax]]-rescaling math [[ai-engineering-ch02-foundation-models|Huyen Ch 2]] gives.
- **[[Topp|top_p (nucleus sampling)]] controls which subset of tokens the LLM can consider** by summing probabilities in descending order until reaching `p`. *"If we set top_p to 0.1, it will consider tokens until it reaches that value. If we set top_p to 1, it will consider all tokens."* [[Topk|top_k]] is the fixed-count alternative — *"if you change its value to 100, the LLM will only consider the top 100 most probable tokens."*
- **Temperature + top_p map to use-case quadrants** (Table 6-1):
  | Use case | Temperature | top_p | Description |
  |---|---|---|---|
  | Brainstorming | High | High | Highly diverse, creative, unexpected. |
  | Email generation | Low | Low | Predictable, focused, conservative. |
  | Creative writing | High | Low | Creative but coherent. |
  | Translation | Low | High | Coherent + linguistic variety. |
- **Prompt engineering is iterative; there is no perfect prompt.** *"Prompt engineering is more than designing effective prompts. It can be used as a tool to evaluate the output of a model as well as to design safeguards and safety mitigation methods. This is an iterative process of prompt optimization and requires experimentation. There is not and unlikely will ever be a perfect prompt design."*
- **The basic prompt has two ingredients** — **instruction + data**. Adding an **output indicator** (e.g., prefixing input with `Text:` and appending `Sentiment:` so the model emits *"negative"* or *"positive"* rather than continuing the sentence) extends this to three.
- **Instruction-based prompting has three tips**:
  1. **Specificity** — *"Accurately describe what you want to achieve. Instead of asking the LLM to 'Write a description for a product' ask it to 'Write a description for a product in less than two sentences and use a formal tone.'"* The most important of the three.
  2. **Hallucination mitigation** — *"To reduce its impact, we can ask the LLM to only generate an answer if it knows the answer. If it does not know the answer, it can respond with 'I don't know.'"*
  3. **Order (primacy / recency effects)** — *"Either begin or end your prompt with the instruction. Especially with long prompts, information in the middle is often forgotten."* — citing [[lostinthemiddle|Liu et al. 2023]] *"Lost in the middle"*.
- **The seven-component modular prompt** (the chapter's central contribution to prompt-engineering vocabulary):
  | Component | What it specifies |
  |---|---|
  | **[[Persona|Persona]]** | The role the LLM should take — *"You are an expert in astrophysics"*. |
  | **[[InstructionPrompt|Instruction]]** | The task itself — make it as specific as possible. |
  | **[[ContextPrompt|Context]]** | Why the instruction exists / additional background. |
  | **[[OutputFormat|Format]]** | What format the LLM should output — *"Without it, the LLM will come up with a format itself, which is troublesome in automated systems."* |
  | **[[AudiencePrompt|Audience]]** | Who the output is for — *"For education purposes, it is often helpful to use ELI5 ('Explain it like I'm 5')."* |
  | **[[TonePrompt|Tone]]** | Voice / register — *"If you are writing a formal email to your boss, you might not want to use an informal tone of voice."* |
  | **Data** | The actual content of the task. |
- **Prompts are modular Lego blocks; iterate by adding/removing/reordering components.** *"The changes are not limited to simply introducing or removing components. Their order, as we saw before with the recency and primacy effects, can affect the quality of the LLM's output."* The chapter shows code that concatenates seven component strings into a paper-summary prompt: `query = persona + instruction + context + data_format + audience + tone + data`.
- **Creative components are encouraged**, including **emotional stimuli** like *"This is very important for my career."* (citing Li et al. 2023 *"EmotionPrompt"*).
- **[[InContextLearning|In-context learning]] is the *"why describe the task when you can show it"* move.** Three sub-cases by example count: **[[ZeroShotLearning|zero-shot]]** (no examples), **one-shot** (one example), **[[FewShotLearning|few-shot]]** (two or more examples). The book uses Brown et al. 2020 (the [[GPT3|GPT-3]] paper) as the citation. Worked example: defining the made-up word *Gigamuru* with a usage sentence, then asking the model to use the made-up word *screeg* in a sentence — the model produces *"During the intense duel, the knight skillfully screeged his opponent's shield, forcing him to defend himself."*
- **One-/few-shot prompting demands the [[ChatTemplate|chat-template]] role distinction.** Without alternating `{"role": "user", ...}` and `{"role": "assistant", ...}` messages, the model would think it is *"talking to itself."* The book illustrates this with the explicit Phi-3 template output that the `apply_chat_template` call produces.
- **Chain prompting (= [[PromptDecomposition|prompt decomposition]] across LLM calls) breaks complex problems into sequential prompts**, each consuming the previous output. Worked example: chatbot product → first generate `name + slogan` ("MindMeld Messenger / Unleashing Intelligent Conversations, One Response at a Time") → then generate the sales pitch from name+slogan. *"A major benefit is that we can give each call different parameters"* (e.g., short max-tokens for name, longer for pitch).
- **Chain-prompting use cases enumerated**: **response validation** (LLM double-checks previous outputs), **parallel prompts** (run multiple in parallel, merge), **writing stories** (summary → characters → story beats → dialogue). The chapter explicitly frames this as a stepping stone toward Ch 7's broader chaining (memory + tool use).
- **Reasoning with generative models is framed via [[System1And2|Kahneman's System 1 vs System 2]].** *"Generative models automatically generate tokens without any self-reflective behavior"* — that is, System 1 behavior. *"If we could give a generative model the ability to mimic a form of self-reflection, we would essentially be emulating the system 2 way of thinking, which tends to produce more thoughtful responses."* The chapter is careful with the word *"resemble"* — *"these models, at the time of writing, are generally considered to demonstrate this behavior through memorization of training data and pattern matching."*
- **[[chainofthought|Chain-of-thought]] (CoT) has the model think step-by-step before answering** (Wei et al. 2022). The chapter walks the canonical few-shot example: a tennis-ball-counting reasoning example followed by *"The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?"* — the model produces the reasoning chain `23 - 20 = 3 apples left. Then they bought 6 more apples, so they now have 3 + 6 = 9 apples. The answer is 9.`
- **Zero-shot CoT** uses the trigger phrase *"Let's think step-by-step"* — Kojima et al. 2022 *"Large language models are zero-shot reasoners."* The chapter demonstrates the same cafeteria-apples problem reaching the same answer via zero-shot CoT. *"Alternatives exist like 'Take a deep breath and think step-by-step' and 'Let's work through this problem step-by-step.'"* (citing Yang et al. 2023 *"Large language models as optimizers"*).
- **The compute justification for CoT**: *"Adding this reasoning step allows the model to distribute more compute over the reasoning process. Instead of calculating the entire solution based on a few tokens, each additional token in this reasoning process allows the LLM to stabilize its output."*
- **[[selfconsistency|Self-consistency]]** (Wang et al. 2022) — *"asks the generative model the same prompt multiple times and takes the majority result as the final answer."* *"Each answer can be affected by different temperature and top_p values to increase the diversity of sampling."* Combines naturally with CoT — *"we use the answer for the voting procedure"* while keeping the reasoning chains. **Cost**: *"becomes n times slower where n is the number of output samples."*
- **[[TreeOfThoughts|Tree-of-thought]]** (Yao et al. 2023) — *"the generative model is prompted to explore different solutions to the problem at hand. It then votes for the best solution and continues to the next step."* The full architecture requires *"many calls to the generative models, which slows the application significantly."*
- **Single-prompt tree-of-thought approximation** — *"Instead of calling the generative model multiple times, we ask the model to mimic that behavior by emulating a conversation between multiple experts."* The chapter provides the canonical zero-shot ToT prompt:
  > *"Imagine three different experts are answering this question. All experts will write down 1 step of their thinking, then share it with the group. Then all experts will go on to the next step, etc. If any expert realizes they're wrong at any point then they leave. The question is '...' Make sure to discuss the results."*
  
  Applied to the cafeteria-apples question, the model produces a back-and-forth "discussion between experts" reaching the answer 9.
- **Output verification has four motivations**: (1) **structured output** (JSON / YAML / etc.); (2) **valid output** (constrained vocabulary, e.g., only `positive` / `negative` / `neutral`); (3) **ethics** (no PII, profanity, bias); (4) **accuracy** (factual, coherent, no [[Hallucination|hallucination]]).
- **Output control has three methods** (Ch 6's framing):
  1. **Examples** — few-shot demonstrations of the expected output format.
  2. **Grammar** — constrain the token selection process.
  3. **Fine-tuning** — train the model on data with the expected output (deferred to Ch 12).
- **Few-shot output examples improve structural compliance.** The chapter contrasts a zero-shot RPG character-profile prompt (the model produces verbose, truncated JSON with attributes the user did not want) against a one-shot prompt providing the exact JSON template:
  ```json
  {
    "description": "A SHORT DESCRIPTION",
    "name": "THE CHARACTER'S NAME",
    "armor": "ONE PIECE OF ARMOR",
    "weapon": "ONE OR MORE WEAPONS"
  }
  ```
  The model output then conforms exactly: `Lysandra Shadowstep / Leather Cloak of the Night / Dagger of Whispers, Throwing Knives`. *"It is still up to the model whether it will adhere to your suggested format or not. Some models are better than others at following instructions."*
- **Grammar / constrained sampling is the next intensity level.** *"Packages have been rapidly developed to constrain and validate the output of generative models, like [[Guidance]], [[Guardrails]], and [[LMQL]]."* They work in two ways: (a) use an LLM to validate the prior LLM's output against rules; (b) **constrain token selection at sampling time** — for sentiment classification with three labels, mask logits so only the three label-token IDs can be sampled. *"This is still affected by parameters such as top_p and temperature."*
- **Worked grammar example with `llama-cpp-python` + GGUF Phi-3**:
  ```python
  from llama_cpp.llama import Llama
  llm = Llama.from_pretrained(
      repo_id="microsoft/Phi-3-mini-4k-instruct-gguf",
      filename="*fp16.gguf",
      n_gpu_layers=-1,
      n_ctx=2048,
      verbose=False
  )
  output = llm.create_chat_completion(
      messages=[{"role": "user", "content": "Create a warrior for an RPG in JSON format."}],
      response_format={"type": "json_object"},
      temperature=0,
  )['choices'][0]['message']["content"]
  json.loads(output)  # works — output is valid JSON
  ```
  The `response_format={"type": "json_object"}` parameter applies a JSON grammar under the hood. The generated character is `Eldrin Stormbringer / Warrior / level 10 / strength 18 / Ironclad Armor / Steel Greatsword`. *"This allows us to more confidently use generative models in applications where we expect the output to adhere to certain formats."*
- **The GGUF + llama-cpp-python recipe is a new toolchain in the book.** Chs 1–5 used `transformers.AutoModelForCausalLM`; Ch 6 introduces [[llamacpp|llama.cpp]] as the **runtime for quantized models** *"used to efficiently load and use compressed models (through quantization; see Chapter 12)"*. The same Phi-3-mini model is reloaded in GGUF form via `Llama.from_pretrained(repo_id="microsoft/Phi-3-mini-4k-instruct-gguf", filename="*fp16.gguf", n_gpu_layers=-1, n_ctx=2048, verbose=False)`. **VRAM cleanup recipe** is also given: `del model, tokenizer, pipe; gc.collect(); torch.cuda.empty_cache()`.
- **Chapter forward references**: Ch 7 (memory + tool use, chaining beyond LLMs), Ch 12 (fine-tuning as the third output-control lever).

## Key Quotes

> "Through prompt engineering, we can design these prompts in a way that enhances the quality of the generated text." — Ch 6 opening

> "Choosing a text generation model starts with choosing between proprietary models or open source models. Although proprietary models are generally more performant, we focus in this book more on open source models as they offer more flexibility and are free to use." — Ch 6 on model selection

> "A higher temperature (e.g., 0.8) generally results in a more diverse output while a lower temperature (e.g., 0.2) creates a more deterministic output." — Ch 6 on temperature

> "These parameters allow the user to have a sliding scale between being creative (high temperature and top_p) and being predictable (lower temperature and top_p)." — Ch 6 on sampling

> "An essential part of working with text-generative LLMs is prompt engineering. By carefully designing our prompts we can guide the LLM to generate desired responses. Whether the prompts are questions, statements, or instructions, the main goal of prompt engineering is to elicit a useful response from the model." — Ch 6 on prompt-engineering scope

> "Prompt engineering is more than designing effective prompts. It can be used as a tool to evaluate the output of a model as well as to design safeguards and safety mitigation methods. This is an iterative process of prompt optimization and requires experimentation. There is not and unlikely will ever be a perfect prompt design." — Ch 6 on iteration

> "An LLM is a prediction machine. Based on a certain input, the prompt, it tries to predict the words that might follow it." — Ch 6 on the basic prompt-as-prefix framing

> "Accurately describe what you want to achieve. Instead of asking the LLM to 'Write a description for a product' ask it to 'Write a description for a product in less than two sentences and use a formal tone.'" — Ch 6 on specificity

> "LLMs may generate incorrect information confidently, which is referred to as hallucination. To reduce its impact, we can ask the LLM to only generate an answer if it knows the answer. If it does not know the answer, it can respond with 'I don't know.'" — Ch 6 on hallucination tip

> "Either begin or end your prompt with the instruction. Especially with long prompts, information in the middle is often forgotten. LLMs tend to focus on information either at the beginning of a prompt (primacy effect) or the end of a prompt (recency effect)." — Ch 6 on order

> "Persona / Instruction / Context / Format / Audience / Tone / Data" — Ch 6's seven prompt components

> "This complex prompt demonstrates the modular nature of prompting. We can add and remove components freely and judge their effect on the output... In other words, experimentation is vital when finding the best prompt for your use case. With prompting, we essentially have ourselves in an iterative cycle of experimentation." — Ch 6 on the Lego-block model

> "Instead of describing the task, why do we not just show the task? We can provide the LLM with examples of exactly the thing that we want to achieve. This is often referred to as in-context learning, where we provide the model with correct examples." — Ch 6 on ICL

> "An example is worth a thousand words." — Ch 6 paraphrasing the original few-shot paper

> "Instead of breaking the problem within a prompt, we can do so between prompts. Essentially, we take the output of one prompt and use it as input for the next, thereby creating a continuous chain of interactions that solves our problem." — Ch 6 on chain prompting

> "System 1 thinking represents an automatic, intuitive, and near-instantaneous process. It shares similarities with generative models that automatically generate tokens without any self-reflective behavior. In contrast, system 2 thinking is a conscious, slow, and logical process, akin to brainstorming and self-reflection. If we could give a generative model the ability to mimic a form of self-reflection, we would essentially be emulating the system 2 way of thinking, which tends to produce more thoughtful responses than system 1 thinking." — Ch 6 on System 1 / System 2

> "Chain-of-thought aims to have the generative model 'think' first rather than answering the question directly without any reasoning." — Ch 6 defining CoT

> "Adding this reasoning step allows the model to distribute more compute over the reasoning process. Instead of calculating the entire solution based on a few tokens, each additional token in this reasoning process allows the LLM to stabilize its output." — Ch 6 on the compute justification for CoT

> "Alternatives exist like 'Take a deep breath and think step-by-step' and 'Let's work through this problem step-by-step.'" — Ch 6 on zero-shot CoT triggers

> "This method asks the generative model the same prompt multiple times and takes the majority result as the final answer... it does require a single question to be asked multiple times. As a result, although the method can improve performance, it becomes n times slower where n is the number of output samples." — Ch 6 on self-consistency

> "When sampling tokens, we can define a number of grammars or rules that the LLM should adhere to when choosing its next token. For instance, if we ask the model to either return 'positive,' 'negative,' or 'neutral' when performing sentiment classification, it might still return something else. By constraining the sampling process, we can have the LLM only output what we are interested in. Note that this is still affected by parameters such as top_p and temperature." — Ch 6 on grammar-constrained decoding

> "The output is properly formatted as JSON. This allows us to more confidently use generative models in applications where we expect the output to adhere to certain formats." — Ch 6 closing on JSON grammar with llama-cpp-python

## Notable code recipes

### The standard `transformers.pipeline` loader (carried from Ch 1)
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct",
    device_map="cuda", torch_dtype="auto", trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
pipe = pipeline(
    "text-generation", model=model, tokenizer=tokenizer,
    return_full_text=False, max_new_tokens=500, do_sample=False,
)
```

### The seven-component prompt
```python
persona = "You are an expert in Large Language models. You excel at breaking down complex papers into digestible summaries.\n"
instruction = "Summarize the key findings of the paper provided.\n"
context = "Your summary should extract the most crucial points that can help researchers quickly understand the most vital information of the paper.\n"
data_format = "Create a bullet-point summary that outlines the method. Follow this up with a concise paragraph that encapsulates the main results.\n"
audience = "The summary is designed for busy researchers that quickly need to grasp the newest trends in Large Language Models.\n"
tone = "The tone should be professional and clear.\n"
text = "MY TEXT TO SUMMARIZE"
data = f"Text to summarize: {text}"
query = persona + instruction + context + data_format + audience + tone + data
```

### One-shot prompt for the made-up word *screeg*
```python
one_shot_prompt = [
    {"role": "user", "content": "A 'Gigamuru' is a type of Japanese musical instrument. An example of a sentence that uses the word Gigamuru is:"},
    {"role": "assistant", "content": "I have a Gigamuru that my uncle gave me as a gift. I love to play it at home."},
    {"role": "user", "content": "To 'screeg' something is to swing a sword at it. An example of a sentence that uses the word screeg is:"}
]
```

### Zero-shot CoT
```python
zeroshot_cot_prompt = [
    {"role": "user", "content": "The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have? Let's think step-by-step."}
]
```

### Single-prompt tree-of-thought (three-experts roleplay)
```python
zeroshot_tot_prompt = [
    {"role": "user", "content": "Imagine three different experts are answering this question. All experts will write down 1 step of their thinking, then share it with the group. Then all experts will go on to the next step, etc. If any expert realizes they're wrong at any point then they leave. The question is '...'  Make sure to discuss the results."}
]
```

### JSON grammar with llama-cpp-python + GGUF Phi-3
```python
from llama_cpp.llama import Llama
llm = Llama.from_pretrained(
    repo_id="microsoft/Phi-3-mini-4k-instruct-gguf",
    filename="*fp16.gguf",
    n_gpu_layers=-1, n_ctx=2048, verbose=False
)
output = llm.create_chat_completion(
    messages=[{"role": "user", "content": "Create a warrior for an RPG in JSON format."}],
    response_format={"type": "json_object"},
    temperature=0,
)['choices'][0]['message']["content"]
import json; json.loads(output)  # validates
```

## Stack engaged

- **[[Phi3Mini|Phi-3-mini]]** — *carried forward*, the recurring worked model. Used in both `transformers` form (`microsoft/Phi-3-mini-4k-instruct`) and [[GGUF]] form (`microsoft/Phi-3-mini-4k-instruct-gguf`, `*fp16.gguf`).
- **[[HuggingFace]] `transformers`** — *engaged*, `AutoModelForCausalLM`, `AutoTokenizer`, `pipeline("text-generation")`, `pipe.tokenizer.apply_chat_template`.
- **[[llamacpp|llama-cpp-python]]** — *new in worked code*, `from llama_cpp.llama import Llama; Llama.from_pretrained(repo_id=..., filename=..., n_gpu_layers=-1, n_ctx=2048)` + `create_chat_completion(..., response_format={"type": "json_object"})`. The runtime for the GGUF quantized model.
- **[[GGUF]]** — *engaged*, the quantized-model file format `llama.cpp` expects.
- **PyTorch** — *engaged*, `torch.cuda.empty_cache()` for VRAM cleanup.
- **Python `json`** — *engaged*, `json.loads(output)` to validate the constrained-decoding output.
- **[[Guidance]] / [[Guardrails]] / [[LMQL]]** — *named, not used in code*, as the canonical Python packages for grammar-constrained output and post-hoc output validation.
- **[[Outlines]]** — *implicitly siblings* of Guidance / LMQL, though Ch 6 names Guidance / Guardrails / LMQL specifically. The wiki's existing [[PromptEngineeringTools]] taxonomy reconciles this.

## Connections

- [[hands-on-llm-ch01-introduction-to-llms]] — Ch 1 introduced [[Phi3Mini|Phi-3-mini]] and the `transformers.pipeline` worked example; Ch 6 returns to it as the substrate for prompt-engineering experiments.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2 introduced the `<|user|>` / `<|assistant|>` / `<|end|>` special tokens; Ch 6 explains how they assemble into the chat template that `apply_chat_template` produces.
- [[hands-on-llm-ch03-looking-inside-llms]] — Ch 3 introduced [[GreedyDecoding|greedy decoding]] vs [[Sampling|sampling]] via `do_sample`; Ch 6 elaborates with [[Temperature]] / [[Topp]] / [[Topk]].
- [[hands-on-llm-ch04-text-classification]] — Ch 4 used `temperature=0` for the [[ChatGPT|GPT-3.5-turbo]] generative-classifier and `text2text-generation` for [[FLANT5|Flan-T5]]; Ch 6 deepens the *why* of `temperature=0` and frames classification prompts as a special case of instruction-based prompting.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5's `[DOCUMENTS]` / `[KEYWORDS]` topic-labeling template is the chapter's first complex prompt template; Ch 6 generalizes it to the seven-component framework.
- [[hands-on-llm-ch07-advanced-text-generation]] — Ch 7 forward reference: *"In the next chapter, we will automate this process and go beyond chaining LLMs. We will chain other pieces of technology together, like memory, tool use, and more!"*
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — Ch 12 forward reference: fine-tuning as the **third method** of output control after examples and grammar.
- [[ai-engineering-ch05-prompt-engineering]] — Huyen's prompt-engineering chapter; the **other book-chapter treatment** in the wiki. Strongly complementary — Huyen frames the discipline, Alammar & Grootendorst frame the modular component-design.
- [[ai-engineering-ch02-foundation-models]] — Huyen's source page for [[Temperature]], [[Topp]], [[Topk]], [[ConstrainedSampling]]; Ch 6 takes the operational rather than mechanistic angle on the same parameters.
- [[ai-engineering-ch08-dataset-engineering]] — Huyen's source page for [[chainofthought|CoT]] training data; Ch 6 takes the prompting-side; together they triangulate the CoT pattern.
- [[2402.01817-llm-modulo]] — Kambhampati et al.'s critique of [[TreeOfThoughts|tree-of-thought]] / [[chainofthought|CoT]] as "prompt diversification, not true reasoning"; Ch 6 takes the operational position (use CoT / ToT to *resemble* System 2). The two positions documented side-by-side on [[System1And2]].
- [[PromptEngineering]] — concept page substantially extended by this ingest with the seven-component vocabulary and the iterative-Lego-block framing.
- [[chainofthought]] / [[selfconsistency]] / [[TreeOfThoughts]] — three reasoning-prompting concept pages substantially extended by this ingest with the Wei 2022 / Wang 2022 / Yao 2023 + Kojima 2022 zero-shot-CoT detail.
- [[Persona]] — concept page extended with Ch 6's astrophysics-expert example and the seven-component framing.
- [[PromptDecomposition]] — concept page extended with Ch 6's "chain prompting" naming convention and the name-slogan-pitch worked example.
- [[InContextLearning]] / [[FewShotLearning]] / [[ZeroShotLearning]] — three pages extended with Ch 6's *Gigamuru / screeg* worked example.
- [[ConstrainedSampling]] — concept page substantially extended with the worked `llama-cpp-python` JSON-grammar example (the wiki's first runnable demonstration; previously conceptual-only from Huyen Ch 2).
- [[System1And2]] — concept page extended with the Kahneman citation for the constructive CoT-resembles-System-2 framing, sitting alongside [[2402.01817-llm-modulo]]'s critique.
- [[Hallucination]] — page extended with Ch 6's "ask the model to say 'I don't know'" mitigation.
- [[lostinthemiddle]] — stub extended with Ch 6's primacy/recency tip and the citation to Liu et al. 2023.
- [[Temperature]] / [[Topp]] / [[Topk]] — pages extended with Ch 6's use-case quadrant table.
- [[ChatTemplate]] — page extended with Ch 6's explicit Phi-3 `<s><|user|>...<|end|><|assistant|>` worked output.
- [[Guidance]] / [[Outlines]] / [[LMQL]] — entity pages extended with Ch 6's naming of these tools alongside [[Guardrails]] for grammar-constrained decoding.
- [[Phi3Mini]] / [[HandsOnLLM]] / [[JayAlammar]] / [[MaartenGrootendorst]] / [[OReilly]] / [[HuggingFace]] / [[llamacpp]] / [[microsoft]] — entity pages updated.
- New entity page: **[[Guardrails]]** — Shreya Rajpal's grammar-constrained output library; the third name in the Guidance / Guardrails / LMQL triad Ch 6 cites.

## Contradictions

No direct contradictions with existing wiki content. **Soft consistency notes worth flagging**:

- **[[System1And2]] dual stance**: Ch 6 frames CoT / self-consistency / tree-of-thought as **constructive operationalizations** of System 2 thinking — *"emulating the system 2 way of thinking, which tends to produce more thoughtful responses"*. The existing [[System1And2]] page anchors [[2402.01817-llm-modulo|Kambhampati et al.'s critique]]: *"Even from a pure engineering perspective, a system that takes constant time to produce the next token cannot possibly be doing principled reasoning on its own"* — and frames CoT / ToT / [[Reflexion|Reflexion]] as *"critiqued as System-1 priming variations, not true System 2."* These positions are **not contradictions** but reflect a **live methodological tension**: Ch 6 (and the LLM-engineering line generally) takes the position that the resemblance is useful and improves outputs; Kambhampati et al. take the position that without an external verifier the resemblance is empty. Both positions are now documented on [[System1And2]]; the [[TreeOfThoughts]] page is the most direct intersection point.
- **[[selfconsistency]] cost framing**: Huyen Ch 2's existing framing positions self-consistency as *"the majority-vote variant of [[bestofn|best-of-N]] within the test-time compute family"* — useful for tasks with exact-answer ground truth. Ch 6's framing — *"becomes n times slower where n is the number of output samples"* — is consistent but uses a different framing axis (latency/cost) rather than test-time-compute taxonomy. Both extend [[selfconsistency]] without conflict.
- **[[TreeOfThoughts]] two-mode framing**: Ch 6 introduces a **single-prompt three-experts-roleplay approximation** of ToT — *"we ask the model to mimic that behavior by emulating a conversation between multiple experts"* — distinct from the multi-call architecture in Yao et al. 2023. This is **complementary** to the existing [[TreeOfThoughts]] critique and adds a useful operating point.
- **[[PromptEngineering|Prompt-engineering anatomy]]**: Huyen Ch 5 names a **three-part anatomy** (task description / examples / task); Ch 6 names a **seven-component modular framework** (persona / instruction / context / format / audience / tone / data). These are **complementary granularities**, not contradictions — the seven components map cleanly to subdivisions of the Huyen three-part anatomy (persona + instruction + context + format + audience + tone all sub-divide "task description"; examples are still examples; data is the task). Both framings documented on [[PromptEngineering]].
- **[[chainofthought]] variant catalog**: Huyen Ch 5 names four CoT variants (zero-shot CoT, zero-shot CoT with rationale, zero-shot CoT with explicit steps, one-shot CoT). Ch 6 names two (few-shot CoT with example reasoning, zero-shot CoT via *"Let's think step-by-step"*) and an alternative-trigger family (*"Take a deep breath"*, *"Let's work through this"*). The catalogs are **consistent** — Ch 6's two variants subsume Huyen's four if one notes that *"Let's think step-by-step"* is the canonical zero-shot CoT trigger and the alternative triggers are equivalent operating points.
- **[[ConstrainedSampling]] toolchain set**: Huyen Ch 2 names *"guidance, outlines, instructor, llama.cpp"* as constrained-sampling tools. Ch 6 names *"[[Guidance]], [[Guardrails]], and [[LMQL]]"*. These overlap on Guidance and llama.cpp (Ch 6 uses llama.cpp as the runtime); each book adds a different tool that the other omits ([[Outlines]] / [[Instructor]] on Huyen's side, [[Guardrails]] / [[LMQL]] on Alammar & Grootendorst's). Both are valid; the [[PromptEngineeringTools]] taxonomy already enumerates the broader landscape.
- **[[Temperature]] mechanistic vs operational framing**: Huyen Ch 2 gives the [[Softmax|softmax]]-rescaling math (*"logits divided by temperature"*); Ch 6 gives the operational characterization (*"a temperature of 0 generates the same response every time because it always chooses the most likely word"*). Consistent; complementary.

## Position in the wiki

This is the **sixth chapter from *Hands-On Large Language Models*** ingested (after Chs 1–5) and the **wiki's first chapter from the book whose subject matter is squarely prompt engineering**. It complements rather than replaces the wiki's existing prompt-engineering coverage:

- The existing [[PromptEngineering]] page (from [[ai-engineering-ch01-intro|Huyen Ch 1]] / [[ai-engineering-ch05-prompt-engineering|Huyen Ch 5]]) framed prompt engineering as a discipline with six best practices, defensive-prompt-engineering safety surface, and a [[PromptStructure|three-part anatomy]]. Ch 6 adds the **seven-component modular vocabulary** and the **iterative Lego-block workflow**.
- The existing [[chainofthought|CoT]] page (from [[ai-engineering-ch05-prompt-engineering|Huyen Ch 5]] / [[ai-engineering-ch08-dataset-engineering|Huyen Ch 8]] / DSPy corpus) named the four Huyen CoT variants and traced CoT training-data implications. Ch 6 adds the **canonical cafeteria-apples worked example with both few-shot and zero-shot triggers** and the **compute-justification framing** *"each additional token in this reasoning process allows the LLM to stabilize its output."*
- The existing [[selfconsistency]] page (from [[2605.08083-autotts|AutoTTS]] / [[2025-bionlp-archehr-qa-neural|ArchEHR-QA]] / [[ai-engineering-ch02-foundation-models|Huyen Ch 2]]) framed self-consistency as the canonical [[parallelreasoning|parallel reasoning]] / [[bestofn|best-of-N]] baseline in the [[testtimescaling|TTS]] literature. Ch 6 adds the **practitioner-facing cost framing** (*"n times slower"*) and the natural pairing with [[chainofthought|CoT]] (vote over CoT-style reasoning chains' final answers).
- The existing [[TreeOfThoughts]] page (from [[2402.01817-llm-modulo]]) framed ToT primarily through the Kambhampati critique. Ch 6 adds the **practitioner-facing pedagogical framing** and the **single-prompt three-experts-roleplay approximation** that converts the multi-call ToT into a one-prompt operating point.
- The existing [[ConstrainedSampling]] page (from [[ai-engineering-ch02-foundation-models|Huyen Ch 2]]) was conceptual-only. Ch 6 adds the **wiki's first runnable demonstration** via `llama-cpp-python` + GGUF Phi-3 + `response_format={"type": "json_object"}`.
- The existing [[Persona]] page (from Huyen Ch 5) framed persona as one of six best practices with the first-grade-teacher example. Ch 6 adds the **astrophysics-expert example** and slots persona as one of seven equal-status modular components.
- The existing [[PromptDecomposition]] page (from Huyen Ch 5) framed decomposition via the GoDaddy customer-support case study and the intent-classification → response-generation worked example. Ch 6 adds the **"chain prompting" naming convention** and the **name-slogan-pitch product worked example**, plus the three sub-use-cases (**response validation**, **parallel prompts**, **writing stories**).

**Position-in-the-book**: Ch 6 is **Part III Chapter 1** — the start of the **generation-focused** half of the book. Chs 1–3 are the LLM-fundamentals foundation; Chs 4–5 are Part II applications using both representation and generative models; Chs 6–9 are Part III using generative models. Ch 6 is the **prompt-engineering opener** and forward-references **Ch 7** (advanced text generation — memory and tool use beyond chaining LLMs) and **Ch 12** (fine-tuning generation models — the third output-control lever).

**New things minted by this chapter** (concepts): **[[InstructionPrompt]]**, **[[ContextPrompt]]**, **[[OutputFormat]]**, **[[AudiencePrompt]]**, **[[TonePrompt]]**, **[[OutputVerification]]**, **[[GrammarConstrainedDecoding]]**, **[[PromptChaining]]**, **[[OneShotPrompting]]**, **[[PrimacyEffect]]**, **[[ZeroShotCoT]]** (concept stub pages). Plus the **[[EmotionPrompt]]** stub for Li et al. 2023. **Entity**: **[[Guardrails]]** (Shreya Rajpal's grammar-constrained output library — the third name in Ch 6's Guidance/Guardrails/LMQL triad). **Update in place**: [[PromptEngineering]], [[chainofthought]], [[selfconsistency]], [[TreeOfThoughts]], [[Persona]], [[InContextLearning]], [[FewShotLearning]], [[ZeroShotLearning]], [[ConstrainedSampling]], [[Temperature]], [[Topp]], [[Topk]], [[Hallucination]], [[lostinthemiddle]], [[ChatTemplate]], [[PromptDecomposition]], [[System1And2]], [[Phi3Mini]], [[HandsOnLLM]], [[JayAlammar]], [[MaartenGrootendorst]], [[OReilly]], [[HuggingFace]], [[llamacpp]], [[Guidance]], [[Outlines]], [[microsoft]].
