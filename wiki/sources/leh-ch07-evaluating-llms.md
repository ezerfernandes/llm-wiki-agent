---
title: "LLM Engineer's Handbook — Ch 7: Evaluating LLMs"
type: source
tags: [book, llm-engineering, llm-engineers-handbook, evaluation, rag, llm-as-a-judge, benchmarks]
date: 2024-10-22
source_file: raw/books/llm-engineers-handbook/ch07-evaluating-llms.md
---

## Summary
Chapter 7 of the *LLM Engineer's Handbook* (Iusztin, Labonne, Vesa, Packt 2024) surveys the landscape of LLM evaluation, distinguishing **model evaluation** (assessing a single LLM in isolation) from **system evaluation** (e.g., a [[rag]] pipeline). It contrasts traditional ML metrics (accuracy, precision, recall, F1, ROUGE) with the more subjective demands of evaluating language generation, and walks through general-purpose, domain-specific, and task-specific benchmarks (MMLU, HellaSwag, ARC-C, Winogrande, PIQA, IFEval, Chatbot Arena, AlpacaEval, MT-Bench, GAIA; plus Medical, BigCodeBench, Hallucinations, and Enterprise leaderboards). The chapter then introduces two RAG-specific frameworks — **Ragas** (LLM-assisted faithfulness / answer relevancy / context precision / context recall) and **ARES** (synthetic data + fine-tuned classifiers) — and closes with a worked example: evaluating **TwinLlama-3.1-8B** and **TwinLlama-3.1-8B-DPO** against `meta-llama/Meta-Llama-3.1-8B-Instruct` using GPT-4o-mini as a judge with a 1–3 Likert scale for **Accuracy** and **Style**.

## Key Claims
- LLM evaluation has no unified approach; benchmarks should be treated as **signals**, not single sources of truth — agreement across multiple evaluations is what raises confidence in a model's capabilities.
- Three core differences between ML and LLM evaluation: (1) ML relies on objective numerical metrics, LLMs rarely can; (2) ML depends heavily on feature engineering, LLMs handle raw text; (3) ML predictions are more directly interpretable than LLM generations.
- General-purpose evaluation falls into three phases: **during pre-training** (training/validation loss, [[Perplexity]], gradient norm), **after pre-training** (MMLU, HellaSwag, ARC-C, Winogrande, PIQA), and **after fine-tuning** ([[ifeval]], Chatbot Arena, AlpacaEval, MT-Bench, [[gaia]]).
- **MMLU** is multiple-choice across 57 subjects from elementary to professional level; **HellaSwag** tests common-sense sentence completion; **ARC-C** evaluates grade-school causal science reasoning; **Winogrande** assesses pronoun-resolution common sense; **PIQA** tests physical common sense.
- An MMLU score jump of ~10 points during fine-tuning is unrealistic and is a red flag for **dataset contamination** with the test set.
- Public benchmarks can be **gamed** via training on near-test data; human evaluators are **biased toward long, confident, well-formatted (Markdown) answers**; private test sets are less scrutinized but may carry their own biases.
- Domain-specific leaderboards (on Hugging Face): **Open Medical-LLM Leaderboard** (MedQA, PubMedQA, MedMCQA + 6 MMLU subsets), **BigCodeBench** (Complete + Instruct, scored by Pass@1 with greedy decoding, plus an Elo for Complete), **Hallucinations Leaderboard** (16 tasks across QA, reading comprehension, summarization, dialogue, fact checking), **Enterprise Scenarios Leaderboard** (FinanceBench, Legal Confidentiality, Writing Prompts, Customer Support Dialogue, Toxic Prompts, Enterprise PII; partly closed-source to deter gaming).
- Language-specific leaderboards (OpenKo-LLM, Open Portuguese LLM, Open Arabic LLM) routinely **translate general-purpose benchmarks** plus add native-language tasks; human-translated benchmarks outperform machine-translated ones.
- All evaluations should be **complex, diverse, and practical**; recommended evaluation libraries are **EleutherAI's `lm-evaluation-harness`** and **Hugging Face's `lighteval`**.
- Task-specific LLMs can often reuse **traditional ML metrics** because their outputs are structured: summarization uses **[[ROUGE]]**; classification/NER use accuracy, precision, recall, [[F1Score]].
- Multiple-choice question answering is a generic pattern for building custom benchmarks; two evaluation modes are **text generation** (model emits "A/B/C/D") and **log-likelihood / probability-based** comparison (`lm-evaluation-harness` computes probabilities of full answer text). The authors prefer text generation because it is more discriminative and closer to real usage.
- For open-ended tasks, **[[LLMAsAJudge]]** is recommended; large judge models, iterative prompt refinement, structured output (Outlines or OpenAI JSON mode), and explanation fields all improve evaluation quality.
- Judge LLM biases include preferences for assertive/verbose answers, lack of domain expertise, **inconsistency** across similar inputs, and stylistic preferences unrelated to accuracy. Mitigations: combine with other metrics, use multiple judges, design prompts that explicitly counter biases.
- **RAG evaluation** must measure three additional dimensions on top of the LLM: **retrieval accuracy**, **integration quality** (how well retrieved context is fused into generation), and **factuality/relevance** of the final output.
- **Ragas** is built on **metrics-driven development (MDD)** and uses LLM-assisted metrics: **Faithfulness** (verifiable-claims / total-claims), **Answer Relevancy** (mean cosine similarity between LLM-generated questions and the original question), **Context Precision** (rank-aware), **Context Recall** (ground-truth claim attribution to retrieved context). It can also synthetically generate test sets (Evol-Instruct-style) and conversational samples.
- **ARES** has three configurable stages: **synthetic data generation** (default `google/flan-t5-xxl`), **classifier training** (default `microsoft/deberta-v3-large` with early-stopping patience and configurable LR), and **RAG evaluation** with confidence intervals and vLLM-backed local execution.
- Ragas and ARES are **complementary**: Ragas excels at production monitoring and nuanced LLM-graded metrics; ARES gives fast, consistent classifier-based evaluation once trained.
- In the TwinLlama-3.1-8B case study, generations use **vLLM** with `temperature=0.8`, `top_p=0.95`, `min_p=0.05`, `max_tokens=4096` over 334 test prompts; judge is **GPT-4o-mini** with a JSON response_format and a system prompt enforcing analysis+score per criterion.
- Final scores (mean over the test set): TwinLlama-3.1-8B → Accuracy 2.45 / Style 2.04; TwinLlama-3.1-8B-DPO → 2.46 / 2.12; Llama-3.1-8B-Instruct → 2.62 / 1.86. DPO improves style without harming accuracy; the Meta instruct model is more accurate (10M+ post-training samples vs. 13k here) but too verbose/formal.

## Key Quotes
> "benchmarks are not a single source of truth but should be used as signals. Once multiple evaluations provide a similar answer, you can raise your confidence level about the real capabilities of a model."

> "improving the MMLU score of a base model by 10 points during the fine-tuning phase is unlikely. This is a sign that the instruction data might be contaminated."

> "Even human evaluation is not perfect and is often biased toward long and confident answers, especially when they're nicely formatted (e.g., using Markdown)."

> "judge LLMs can exhibit biases favoring assertive or verbose responses, potentially overrating answers that sound more confident but are less accurate."

> "Ragas's strength in production monitoring and LLM-assisted metrics can be combined with ARES's highly configurable evaluation process and classifier-based assessments."

## Evaluation Methods Covered

### Pre-training-time signals
- **Training / Validation loss** (cross-entropy)
- **[[Perplexity]]** — exp of cross-entropy, lower is better
- **Gradient norm** — detects vanishing/exploding gradients

### General-purpose benchmarks (post-pretraining)
- **MMLU** — multiple-choice across 57 subjects (knowledge)
- **HellaSwag** — sentence completion (common-sense reasoning)
- **ARC-C** — grade-school causal science (reasoning)
- **Winogrande** — pronoun-resolution common sense (reasoning)
- **PIQA** — physical common sense (reasoning)

### Fine-tuned-model benchmarks
- **IFEval** — instruction following with explicit constraints
- **Chatbot Arena (LMSYS)** — human pairwise voting
- **AlpacaEval** — auto-eval correlated with Chatbot Arena
- **MT-Bench** — multi-turn conversation quality
- **GAIA** — agentic abilities (tool use, web browsing, multi-step)

### Domain-specific Hugging Face leaderboards
- **Open Medical-LLM** — MedQA / PubMedQA / MedMCQA + 6 MMLU clinical subsets
- **BigCodeBench** — Complete (docstring-based) + Instruct (NL-based), Pass@1 + Elo
- **Hallucinations Leaderboard** — 16 tasks: NQ Open, TruthfulQA, SQuADv2, TriviaQA, RACE, HaluEval Summ, XSum, CNN/DM, HaluEval Dial, FaithDial, MemoTrap, SelfCheckGPT, FEVER, TrueFalse + IFEval
- **Enterprise Scenarios** — FinanceBench, Legal Confidentiality (LegalBench), Writing Prompts, Customer Support Dialogue, Toxic Prompts, Enterprise PII

### Language-specific leaderboards
- **OpenKo-LLM** — Korean (GPQA, Winogrande, GSM8K, EQ-Bench, IFEval translated + native)
- **Open Portuguese LLM** — ENEM, BLUEX, OAB, ASSIN2, FAQUAD, HateBR, PT Hate Speech, tweetSentBR
- **Open Arabic LLM** — AlGhafa + Arabic-Culture-Value-Alignment + 12 translated (MMLU, ARC-C, HellaSwag, PIQA, etc.)

### Task-specific / classical ML metrics
- **Accuracy, Precision, Recall, [[F1Score]]** — classification, NER
- **[[ROUGE]]** — summarization
- **Multiple-choice QA** — generic custom-benchmark scaffold (text-gen vs log-likelihood modes)

### LLM-as-a-judge
- General-purpose judge prompt with Likert scale (1–4) and explanation field
- Recommended: structured output (Outlines, OpenAI JSON mode), large judge models, multiple judges, ground-truth context when available

### RAG-specific frameworks
- **[[RAGAS]]** — Faithfulness, Answer Relevancy, Context Precision, Context Recall; Evol-Instruct synthetic test-set generation
- **ARES** — synthetic data → classifier training (`microsoft/deberta-v3-large`) → evaluation with confidence intervals; vLLM-friendly

### Evaluation libraries
- **`lm-evaluation-harness`** (EleutherAI) — `github.com/EleutherAI/lm-evaluation-harness`
- **`lighteval`** (Hugging Face) — `github.com/huggingface/lighteval`

## Code & Concrete Examples

### Text-generation answer pipeline (vLLM)
```python
from vllm import LLM, SamplingParams
from datasets import load_dataset

def generate_answers(model_id, dataset_name):
    dataset = load_dataset(dataset_name, split="test")
    def format(sample):
        return ("Below is an instruction that describes a task. "
                "Write a response that appropriately completes the request.\n\n"
                "### Instruction:\n{}\n\n### Response:\n").format(sample["instruction"])
    dataset = dataset.map(lambda s: {"prompt": format(s)})
    llm = LLM(model=model_id, max_model_len=4096)
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95, min_p=0.05, max_tokens=4096)
    outputs = llm.generate(dataset["prompt"], sampling_params)
    answers = [o.outputs[0].text for o in outputs]
    dataset = dataset.add_column("answers", answers)
    dataset.push_to_hub(f"mlabonne/{model_id.split('/')[-1]}-results")
    return dataset
```

### GPT-4o-mini judge with Accuracy/Style scales (1–3 Likert)
- System prompt: *"You are a helpful assistant who evaluates answers based on accuracy and style. Provide your response in JSON format with a short analysis and score for each criterion."*
- `response_format={"type": "json_object"}`, `temperature=0.8`, `max_tokens=1000`
- Batched evaluation via `ThreadPoolExecutor` for parallelism
- Output JSON shape:
  ```json
  {"accuracy": {"analysis": "...", "score": 0},
   "style":    {"analysis": "...", "score": 0}}
  ```
- Style scale specifically penalizes formal/academic language and rewards "simple but technical" blog/social-media style

### General-purpose judge prompt template (Table 7.2)
```
You are an evaluator who assesses the quality of an answer to an instruction.
Use a scale of 1 to 4:
  1. Not relevant
  2. Relevant but not helpful
  3. Relevant and helpful but could be more detailed
  4. Relevant, helpful, and detailed

##Evaluation##
Explanation: ...
Total rating: ...
```

### TwinLlama final mean scores
```
TwinLlama-3.1-8B          Accuracy 2.45  Style 2.04
TwinLlama-3.1-8B-DPO      Accuracy 2.46  Style 2.12
Llama-3.1-8B-Instruct     Accuracy 2.62  Style 1.86
```

## Connections
- [[rag]] — system that this chapter teaches how to evaluate end-to-end
- [[RAGAS]] — one of the two RAG eval frameworks covered in depth
- [[LLMAsAJudge]] / [[llmasjudge]] — central technique for open-ended evaluation
- [[mmlu]] — flagship knowledge benchmark, used as the running example for contamination
- [[ifeval]] — instruction-following benchmark recommended for instruct-model selection
- [[gaia]] — agentic-skills benchmark cited for tool-using models
- [[GSM8K]] — reused (translated) in OpenKo-LLM
- [[Perplexity]] — pre-training-time signal listed alongside loss and gradient norm
- [[CrossEntropy]] / [[CrossEntropyLoss]] — basis of training-loss and perplexity metrics
- [[ROUGE]] — recommended summarization metric
- [[F1Score]] / [[PrecisionRecall]] — classical metrics for classification/NER tasks
- [[Hallucination]] — addressed by the Hallucinations Leaderboard and faithfulness metric
- [[Benchmarking]] / [[ModelEvaluation]] — broader concept pages
- [[FineTuning]] / [[BootstrapFinetune]] / [[LLMFineTuning]] — what this chapter's evaluations measure the success of
- [[meta]] — publisher of `meta-llama/Meta-Llama-3.1-8B-Instruct` baseline
- [[openai]] — provider of GPT-4o-mini judge model
- [[HuggingFace]] — hosts most of the leaderboards, datasets, and the `lighteval` library
- [[google]] — publisher of `google/flan-t5-xxl` (ARES default generator)
- [[microsoft]] — publisher of `microsoft/deberta-v3-large` (ARES default classifier)
- [[Llama3_8BInstruct]] — explicit baseline used in the TwinLlama comparison
- [[GraphRAG]] / [[RAGChatbot]] / [[RAGQAArenaTech]] — adjacent RAG concepts in the wiki

## Contradictions
- No direct contradictions with existing wiki pages. The chapter's preference for **text-generation MMLU evaluation** over log-likelihood evaluation is a methodological stance — other sources in the wiki (e.g., `lm-evaluation-harness`-aligned discussions) may default to log-likelihood; flag this as a methodological tension rather than a factual contradiction.
- The chapter's recommendation to use **judge LLMs** despite their known biases nuances any wiki page that frames LLM-as-judge as unreliable.
