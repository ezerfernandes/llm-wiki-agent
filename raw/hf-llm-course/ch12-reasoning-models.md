# HuggingFace LLM Course — Chapter 12: Build Reasoning Models like DeepSeek R1
Source: https://huggingface.co/learn/llm-course/chapter12/
Sections: 1,2,3,3b,4,5,6
---

## Section 1: Introduction

# Open R1 for Students

Welcome to an exciting journey into the world of open-source AI with reinforcement learning! This chapter is designed to help students understand reinforcement learning and its role in LLMs.

We will also explore [Open R1](https://github.com/huggingface/open-r1), a groundbreaking community project that's making advanced AI accessible to everyone. Specifically, this course is to help students and learners to use and contribute to [Open R1](https://github.com/huggingface/open-r1).

## What You'll Learn

In this chapter, we'll break down complex concepts into easy-to-understand pieces and show you how you can be part of this exciting project to make LLMs reason on complex problems.

LLMs have shown excellent performance on many generative tasks. However, up until recently they have struggled on complex problems that require reasoning. For example, they struggle to deal with puzzles or math problems that require multiple steps of reasoning.

Open R1 is a project that aims to make LLMs reason on complex problems. It does this by using reinforcement learning to encourage LLMs to 'think' and reason.

In simple terms, the model is trained to generate thoughts as well as outputs, and to structure these thoughts and outputs so that they can be handled separately by the user.

Let's take a look at an example. As we gave ourself the task of solving the following problem, we might think like this:

```sh
Problem: "I have 3 apples and 2 oranges. How many pieces of fruit do I have in total?"

Thought: "I need to add the number of apples and oranges to get the total number of pieces of fruit."

Answer: "5"
```

We can then structure this thought and answer so that they can be handled separately by the user. For reasoning tasks, LLMs can be trained to generate thoughts and answers in the following format:

```sh
I need to add the number of apples and oranges to get the total number of pieces of fruit.
5
```

As a user, we can then extract the thought and answer from the model's output and use them to solve the problem.

## Why This Matters for Students

As a student, understanding Open R1 and the role of reinforcement learning in LLMs is valuable because:
- It shows you how cutting-edge AI is developed
- It gives you hands-on opportunities to learn and contribute
- It helps you understand where AI technology is heading
- It opens doors to future career opportunities in AI

## Chapter Overview

This chapter is divided into four sections, each focusing on a different aspect of Open R1:

### 1. Introduction to Reinforcement Learning and its Role in LLMs
- What is RL?
- How is RL used in LLMs?
- What is DeepSeek R1?
- What are the key innovations of DeepSeek R1?

### 2. Understanding the DeepSeek R1 Paper
- Key innovations and breakthroughs
- The training process and architecture
- Results and their significance

### 3. Implementing GRPO in TRL
- How to use the Transformer Reinforcement Learning (TRL) library
- Setting up GRPO training

### 4. Practical use case to align a model
- How to train a model using GRPO in TRL
- Share your model on the Hugging Face Hub

## Prerequisites

- Solid understanding of Python programming
- Familiarity with machine learning concepts
- Interest in AI and language models

---

## Section 2: Reinforcement Learning on LLMs

# Introduction to Reinforcement Learning and its Role in LLMs

## What is Reinforcement Learning (RL)?

Imagine you're training a dog. You want to teach it to sit. You might say "Sit!" and then, if the dog sits, you give it a treat and praise. Over time, the dog learns to associate sitting with the positive reward. In reinforcement learning, we refer to this feedback as a **reward**.

Instead of a dog, we have a **language model** (in reinforcement learning, we call it an **agent**), and instead of you, we have the **environment** that gives feedback.

### Agent
The learner. In the context of LLMs, the LLM itself becomes the agent.

### Environment
The world the agent lives in and interacts with. For an LLM, the environment could be the users it interacts with, or a simulated scenario.

### Action
The choices the agent can make. For an LLM, actions could be generating words in a sentence, choosing which answer to give to a question, or deciding how to respond.

### Reward
Feedback the environment gives to the agent. Positive rewards say "good job"; negative rewards (penalties) say "that wasn't quite right".

### Policy
The agent's strategy for choosing actions. In RL, the policy is what we're really trying to learn and improve.

## The RL Process: Trial and Error

| Step | Process | Description |
|------|---------|-------------|
| 1. Observation | The agent observes the environment | Takes in information about its current state |
| 2. Action | Takes an action based on its current policy | Decides what to do next |
| 3. Feedback | The environment gives a reward | Feedback on how good or bad the action was |
| 4. Learning | Updates its policy based on the reward | Reinforce high-reward actions, avoid low-reward |
| 5. Iteration | Repeat | Continuously improve decision-making |

## Role of RL in Large Language Models (LLMs)

We want LLMs to be:
* **Helpful:** Provide useful and relevant information.
* **Harmless:** Avoid generating toxic, biased, or harmful content.
* **Aligned with Human Preferences:** Respond in ways that humans find natural, helpful, and engaging.

Pre-training (next-word prediction) and supervised fine-tuning can be less effective at producing helpful, harmless, and aligned responses. RL fills the gap.

## Reinforcement Learning from Human Feedback (RLHF)

1. **Get Human Preferences:** Ask humans to compare different LLM responses.
2. **Train a Reward Model:** Train a separate model to predict what humans prefer.
3. **Fine-tune the LLM with RL:** The reward model scores responses; the LLM is trained to maximize that score.

Benefits:
| Benefit | Description |
|---------|-------------|
| Improved Control | More control over the kind of text LLMs generate |
| Enhanced Alignment with Human Values | Learn from human judgments instead of hand-coded rules |
| Mitigating Undesirable Behaviors | Penalize toxic language, misinformation, biases |

RLHF has been used to train GPT-4, Gemini, and DeepSeek R1.

## Why GRPO (Group Relative Policy Optimization)?

Other RLHF techniques:
- **Proximal Policy Optimization (PPO):** One of the first highly effective techniques for RLHF. Policy gradient method using a separate reward model.
- **Direct Preference Optimization (DPO):** Simpler — eliminates the need for a separate reward model by framing the problem as a classification task between chosen and rejected responses.

Unlike DPO and PPO, GRPO **groups similar samples together** and compares them as a group. The group-based approach provides more stable gradients and better convergence.

GRPO does not use preference data like DPO; it compares groups of similar samples using a reward signal from a model or function. GRPO can work with any function that evaluates response quality — a length function, a math solver, a factual-correctness function, etc.

---

## Section 3: The Aha Moment in the DeepSeek R1 Paper

# Understanding the DeepSeek R1 Paper

DeepSeek R1 represents a significant advancement in language model training, particularly in developing reasoning capabilities through reinforcement learning. The paper introduces a new RL algorithm called **Group Relative Policy Optimization (GRPO)**.

The initial goal of the paper was to explore whether **pure reinforcement learning could develop reasoning capabilities without supervised fine-tuning**.

## The Breakthrough 'Aha' Moment

One of the most remarkable discoveries in R1-Zero's training was the emergence of a phenomenon known as the "Aha Moment":

1. **Initial Attempt:** The model makes an initial attempt at solving a problem
2. **Recognition:** It recognizes potential errors or inconsistencies
3. **Self-Correction:** It adjusts its approach based on this recognition
4. **Explanation:** It can explain why the new approach is better

Puzzle analogy:
- First try: "This piece should go here based on the color"
- Recognition: "But wait, the shape doesn't quite fit"
- Correction: "Ah, it actually belongs over there"
- Explanation: "Because both the color and shape pattern match in this position"

This ability emerged naturally from RL training, without being explicitly programmed, demonstrating learning rather than mere memorization of a process from the training data.

## The Training Process

The final process results in two models:
- **DeepSeek-R1-Zero:** A model trained purely using reinforcement learning.
- **DeepSeek-R1:** A model that builds on the foundation of DeepSeek-R1-Zero and adds supervised fine-tuning.

| Feature | DeepSeek-R1-Zero | DeepSeek-R1 |
|---------|------------------|--------------|
| Training Approach | Pure RL | Multi-phase (SFT + RL) |
| Fine-tuning | None | Supervised fine-tuning |
| Reasoning Capability | Emergent | Enhanced |
| AIME Performance | 71.0% | 79.8% |
| Key Characteristics | Strong reasoning but readability issues | Better language consistency and readability |

Four phases:

### 1. Cold Start Phase (Quality Foundation)
Small dataset of high-quality samples from R1-Zero used to fine-tune the V3-Base model. Establishes strong baseline readability and response quality.

### 2. Reasoning RL Phase (Capability Building)
Focuses on core reasoning across mathematics, coding, science, and logic. **Rule-based reinforcement learning**, with rewards directly tied to solution correctness. All tasks are 'verifiable' — we can check the answer (e.g., a math solver). Eliminates the need for a separate reward model.

### 3. Rejection Sampling Phase (Quality Control)
Model generates samples filtered through quality control. DeepSeek-V3 serves as the quality judge. Filtered data is used for supervised fine-tuning.

### 4. Diverse RL Phase (Broad Alignment)
For deterministic tasks, rule-based rewards; for subjective tasks, LLM feedback. Hybrid reward approach for human-preference alignment.

## The Algorithm: Group Relative Policy Optimization (GRPO)

GRPO's novelty lies in its capacity to "directly optimize for preference rectification," contrasting with PPO.

### Group Formation: Creating Multiple Solutions
The model creates multiple attempts at solving the same problem (usually 4, 8, or 16 different attempts). All attempts are kept together as a group.

### Preference Learning: Understanding What Makes a Good Solution
GRPO can use any function or model to evaluate quality — length function, math solver, etc.

The evaluation looks at:
- Is the final answer correct?
- Did the solution follow proper formatting (like using the right XML tags)?
- Does the reasoning match the answer provided?

**Group relative advantage estimation:**

```
Advantage = (reward - mean(group_rewards)) / std(group_rewards)
```

This normalization is like grading on a curve.

### Optimization: Learning from Experience
1. Encourages more solutions like the successful ones
2. Includes a **KL divergence penalty** that prevents the model from changing too drastically

GRPO's key innovations:
> - Learning directly from any function or model, eliminating the reliance on a separate reward model.
> - Group-based learning, which is more stable and efficient than traditional methods like pairwise comparisons.

### GRPO Algorithm in Pseudocode

```
Input:
- initial_policy: Starting model to be trained
- reward_function: Function that evaluates outputs
- training_prompts: Set of training examples
- group_size: Number of outputs per prompt (typically 4-16)

Algorithm GRPO:
1. For each training iteration:
   a. Set reference_policy = initial_policy (snapshot current policy)
   b. For each prompt in batch:
      i. Generate group_size different outputs using initial_policy
      ii. Compute rewards for each output using reward_function
      iii. Normalize rewards within group:
           normalized_advantage = (reward - mean(rewards)) / std(rewards)
      iv. Update policy by maximizing the clipped ratio:
          min(prob_ratio * normalized_advantage,
              clip(prob_ratio, 1-epsilon, 1+epsilon) * normalized_advantage)
          - kl_weight * KL(initial_policy || reference_policy)

          where prob_ratio is current_prob / reference_prob

Output: Optimized policy model
```

## Results and Impact

| Domain | Key Results |
|--------|-------------|
| Mathematics | 79.8% on AIME 2024 / 97.3% on MATH-500 |
| Coding | Codeforces Rating: 2029 / LiveCodeBench: 65.9% |
| General Knowledge | MMLU: 90.8% / GPQA Diamond: 71.5% |
| Language Tasks | AlpacaEval 2.0: 87.6% win rate / FRAMES: 82.5% |

API pricing $0.14 per million input tokens; distillation across 1.5B to 70B parameters. 7B model achieves 55.5% on AIME 2024; 70B distilled approaches o1-mini on MATH-500 (94.5%).

## Limitations and Challenges of GRPO

- **Generation Cost**: Generating 4-16 completions per prompt increases compute.
- **Batch Size Constraints**: Processing groups together limits effective batch sizes.
- **Reward Function Design**: Poorly designed rewards lead to unintended behaviors.
- **Group Size Tradeoffs**: Balance diversity vs computational cost.
- **KL Divergence Tuning**: Too high — model won't learn; too low — model diverges too far.

---

## Section 3b: Advanced Understanding of GRPO in DeepSeekMath

# Advanced Understanding of Group Relative Policy Optimization (GRPO) in DeepSeekMath

> Authored by Shirin Yamani.

GRPO directly evaluates model-generated responses by comparing them within groups, instead of training a separate value model (Critic). This leads to significant reduction in computational cost.

GRPO can be applied to any verifiable task.

## The GRPO Algorithm

### Step 1: Group Sampling

For each question `q`, the model generates `G` outputs (group size) from the trained policy: `{o_1, o_2, …, o_G} ~ π_θ_old`, `G = 8`.

Example: `q: Calculate 2 + 2 × 6`, `G = 8`:
`{o_1: 14 (correct), o_2: 16 (wrong), o_3: 10 (wrong), …, o_8: 14 (correct)}`

### Step 2: Advantage Calculation

Assign reward score `r_i` (e.g., 1 correct / 0 wrong), then:

```
A_i = (r_i - mean({r_1, ..., r_G})) / std({r_1, ..., r_G})
```

Example: 4 of 8 correct → mean = 0.5, std = 0.53. Correct → A = 0.94. Wrong → A = -0.94.

Interpretation: A_i > 0 means `o_i` is better than average within its group; A_i < 0 means worse.

### Step 3: Policy Update (Objective Function)

Three components:

#### 1. Probability Ratio
```
ratio = π_θ(o_i|q) / π_θ_old(o_i|q)
```
- ratio > 1: new model assigns higher probability than old
- ratio < 1: new model assigns lower probability than old

#### 2. Clip Function
```
clip(ratio, 1 - ε, 1 + ε)
```
Limits the ratio to `[1-ε, 1+ε]` to avoid drastic updates.

Example with ε = 0.2:
- Case 1: ratio = 0.9 / 0.5 = 1.8 → clipped to 1.2
- Case 2: ratio = 0.2 / 0.5 = 0.4 → clipped to 0.8

#### 3. KL Divergence

```
β * D_KL(π_θ || π_ref)
```

`π_ref` is the pre-update model output (`per_token_logps`); `π_θ` is the new model output (`new_per_token_logps`). Minimizing KL divergence prevents the model from deviating too far from its original behavior.

```
D_KL(P || Q) = Σ P(x) log(P(x) / Q(x))
```

Role of β:
- **Higher β:** More constraint, slower adaptation
- **Lower β:** More freedom, risk of instability / reward hacking
- **DeepSeekMath paper:** β = 0.04

## Worked Example

`Q: Calculate 2 + 2 × 6`

### Step 1: Group Sampling
G = 8, 4 correct (14, reward = 1), 4 wrong (reward = 0).

### Step 2: Advantage Calculation
mean = 0.5, std = 0.53. Correct A = 0.94, Wrong A = -0.94.

### Step 3: Policy Update
Old probability for correct `o_1` = 0.5; new = 0.7.
Ratio = 0.7/0.5 = 1.4 → clip to 1.2 (ε = 0.2).

## Implementation Example (PyTorch)

### 1. Loading the Model and Generating Responses

```python
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "Qwen/Qwen2-Math-1.5B"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model.eval()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Input prompt
prompt = "Solve y = 2x + 1 for x = 2, y = "  # Correct answer: 5
inputs = tokenizer(prompt, return_tensors="pt", padding=True)
input_ids = inputs["input_ids"].to(device)
attention_mask = inputs["attention_mask"].to(device)

# Step 1: Generate 8 responses (B = 2 groups, G = 4 responses per group)
batch_size, num_generations = 2, 4
outputs = model.generate(
    input_ids=input_ids,
    attention_mask=attention_mask,
    max_new_tokens=1,
    num_return_sequences=batch_size * num_generations,
    do_sample=True,
    top_k=10,
    temperature=0.7,
    pad_token_id=tokenizer.eos_token_id,
    return_dict_in_generate=True,
    output_scores=True,
)
```

Sample output:
```
Output 1: 5.0
Output 2: 6.0
Output 3: 7.0
Output 4: 5.0
Output 5: 10.0
Output 6: 2.0
Output 7: 5.0
Output 8: 5.0
```

### 2. Calculating Rewards

```python
# Per-response rewards
reward_1 = [1, 0, 0, 1]
reward_2 = [0, 0, 1, 1]

# Shape: (B * G,) = (8,)
rewards = torch.tensor([1, 0, 0, 1, 0, 0, 1, 1], dtype=torch.float32)
num_generations = 4

# Group rewards: Shape (B, G) = (2, 4)
rewards_grouped = rewards.view(-1, num_generations)

# Mean per group: Shape (B,) = (2,)
mean_grouped_rewards = rewards_grouped.mean(dim=1)
std_grouped_rewards = rewards_grouped.std(dim=1)

# Broadcast to match rewards
mean_grouped_rewards = mean_grouped_rewards.repeat_interleave(num_generations, dim=0)
std_grouped_rewards = std_grouped_rewards.repeat_interleave(num_generations, dim=0)

# Advantages
advantages = (rewards - mean_grouped_rewards) / (std_grouped_rewards + 1e-8)
advantages = advantages.unsqueeze(1)  # (B*G, 1)
```

Output:
```
Advantages: tensor([ 0.8659, -0.8660, -0.8660,  0.8659, -0.8660, -0.8660,  0.8659,  0.8659])
```

### 3. Updating the Policy

```python
# Probability ratio
ratio = torch.exp(new_per_token_logps - per_token_logps)

# Clipping
eps = self.cliprange  # e.g. 0.2
pg_losses1 = -advantages * ratio
pg_losses2 = -advantages * torch.clamp(ratio, 1.0 - eps, 1.0 + eps)
pg_loss_max = torch.max(pg_losses1, pg_losses2)

# Combine with KL penalty
per_token_loss = pg_loss_max + self.beta * per_token_kl

# per_token_kl
per_token_kl = F.kl_div(
    F.log_softmax(new_per_token_logps, dim=-1),
    F.softmax(per_token_logps, dim=-1),
    reduction="none",
).sum(dim=-1, keepdim=True)
```

Full implementation: TRL GRPOTrainer at `huggingface/trl/blob/main/trl/trainer/grpo_trainer.py`.

## References
1. RLHF Book by Nathan Lambert
2. DeepSeek-V3 Technical Report (arXiv 2412.19437)
3. DeepSeekMath (arXiv 2402.03300)

---

## Section 4: Implementing GRPO in TRL

# Implementing GRPO in TRL

Core concepts of GRPO embodied in TRL's `GRPOTrainer`:
- **Group Formation**: Multiple completions for each prompt.
- **Preference Learning**: Reward function compares groups of completions.
- **Training Configuration**: `GRPOConfig` controls the training process.

To implement GRPO:
- Define a dataset of prompts.
- Define a reward function `(completions) -> rewards`.
- Configure with `GRPOConfig`.
- Train using `GRPOTrainer`.

### Minimal Example

```python
from trl import GRPOTrainer, GRPOConfig
from datasets import load_dataset

# 1. Load your dataset
dataset = load_dataset("your_dataset", split="train")

# 2. Define a simple reward function
def reward_func(completions, **kwargs):
    """Example: Reward longer completions"""
    return [float(len(completion)) for completion in completions]

# 3. Configure training
training_args = GRPOConfig(
    output_dir="output",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=2,
    logging_steps=10,
)

# 4. Initialize and train
trainer = GRPOTrainer(
    model="your_model",  # e.g. "Qwen/Qwen2-0.5B-Instruct"
    args=training_args,
    train_dataset=dataset,
    reward_funcs=reward_func,
)
trainer.train()
```

## Key Components

### 1. Dataset Format
Prompts that the model will respond to. GRPOTrainer generates multiple completions per prompt and compares them with the reward function.

### 2. Reward Function

```python
def reward_length(completions, **kwargs):
    return [float(len(completion)) for completion in completions]

import re
def reward_format(completions, **kwargs):
    pattern = r"^.*?.*?$"
    return [1.0 if re.match(pattern, c) else 0.0 for c in completions]
```

### 3. Training Configuration

```python
training_args = GRPOConfig(
    output_dir="output",
    num_train_epochs=3,
    num_generation=4,  # Group size
    per_device_train_batch_size=4,
    gradient_accumulation_steps=2,
    learning_rate=1e-5,
    logging_steps=10,
    use_vllm=True,  # Speed up generation
)
```

`num_generation` defines the group size:
- Too small (2-3): Not enough diversity
- Recommended (4-16): Good balance
- Larger: Better learning, more compute

## Tips for Success
1. **Memory Management**: Adjust `per_device_train_batch_size` and `gradient_accumulation_steps`.
2. **Speed**: Enable `use_vllm=True`.
3. **Monitoring**: `reward`, `reward_std`, `kl`.

## Reward Function Design

### 1. Length-Based Rewards
```python
def reward_len(completions, **kwargs):
    ideal_length = 20
    return [-abs(ideal_length - len(completion)) for completion in completions]
```

### 2. Rule-Based Rewards for Verifiable Tasks
```python
def problem_reward(completions, answers, **kwargs):
    """Reward function for math problems with verifiable answers"""
    rewards = []
    for completion, correct_answer in zip(completions, answers):
        try:
            answer = extract_final_answer(completion)
            reward = 1.0 if answer == correct_answer else 0.0
            rewards.append(reward)
        except:
            rewards.append(0.0)
    return rewards
```

### 3. Format-Based Rewards
```python
def format_reward(completions, **kwargs):
    """Reward completions that follow the desired format"""
    pattern = r"(.*?)\s*(.*?)"
    rewards = []
    for completion in completions:
        match = re.search(pattern, completion, re.DOTALL)
        if match:
            think_content = match.group(1).strip()
            answer_content = match.group(2).strip()
            if len(think_content) > 20 and len(answer_content) > 0:
                rewards.append(1.0)
            else:
                rewards.append(0.5)
        else:
            rewards.append(0.0)
    return rewards
```

---

## Section 5: Practical Exercise to Fine-tune a model with GRPO

# Practical Exercise: Fine-tune a model with GRPO

> Exercise written by LLM fine-tuning expert [@mlabonne](https://huggingface.co/mlabonne).

## Install dependencies

```bash
!pip install -qqq datasets==3.2.0 transformers==4.47.1 trl==0.14.0 peft==0.14.0 accelerate==1.2.1 bitsandbytes==0.45.2 wandb==0.19.7 --progress-bar off
!pip install -qqq flash-attn --no-build-isolation --progress-bar off
```

```python
import torch
from datasets import load_dataset
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import GRPOConfig, GRPOTrainer
```

## Weights & Biases

```python
import wandb
wandb.login()
```

## Load the dataset

Dataset: `mlabonne/smoltldr` — short stories.

```python
dataset = load_dataset("mlabonne/smoltldr")
print(dataset)
```

## Load model

`SmolLM2-135M` — small 135M parameter model.

```python
model_id = "HuggingFaceTB/SmolLM-135M-Instruct"
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
    attn_implementation="flash_attention_2",
)
tokenizer = AutoTokenizer.from_pretrained(model_id)
```

## Load LoRA

```python
lora_config = LoraConfig(
    task_type="CAUSAL_LM",
    r=16,
    lora_alpha=32,
    target_modules="all-linear",
)
model = get_peft_model(model, lora_config)
print(model.print_trainable_parameters())
```

```
Total trainable parameters: 135M
```

## Reward function — target 50 tokens

```python
ideal_length = 50
def reward_len(completions, **kwargs):
    return [-abs(ideal_length - len(completion)) for completion in completions]
```

## Training arguments

```python
training_args = GRPOConfig(
    output_dir="GRPO",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    gradient_accumulation_steps=2,
    max_prompt_length=512,
    max_completion_length=96,
    num_generations=8,
    optim="adamw_8bit",
    num_train_epochs=1,
    bf16=True,
    report_to=["wandb"],
    remove_unused_columns=False,
    logging_steps=1,
)
```

## Train

```python
trainer = GRPOTrainer(
    model=model,
    reward_funcs=[reward_len],
    args=training_args,
    train_dataset=dataset["train"],
)
wandb.init(project="GRPO")
trainer.train()
```

Training takes ~1 hour on a single A10G GPU.

## Interpret training results

Reward moves closer to 0 as the model learns the target length. Loss starts at zero and increases — **this is expected**: the loss in GRPO is proportional to the KL divergence from the original policy. As training progresses, the model diverges more from its initial policy as it adapts to the reward.

## Save and publish

```python
merged_model = trainer.model.merge_and_unload()
merged_model.push_to_hub(
    "SmolGRPO-135M", private=False, tags=["GRPO", "Reasoning-Course"]
)
```

## Generate text

```python
prompt = """
# A long document about the Cat
The cat (Felis catus)... [truncated for brevity]
"""

messages = [{"role": "user", "content": prompt}]

from transformers import pipeline
generator = pipeline("text-generation", model="SmolGRPO-135M")

generate_kwargs = {
    "max_new_tokens": 256,
    "do_sample": True,
    "temperature": 0.5,
    "min_p": 0.1,
}

generated_text = generator(messages, generate_kwargs=generate_kwargs)
print(generated_text)
```

---

## Section 6: Practical Exercise with Unsloth

# Practical Exercise: GRPO with Unsloth

Unsloth accelerates LLM fine-tuning, training models faster with less compute. Unsloth plugs into TRL.

## Install dependencies

```bash
pip install unsloth vllm
pip install --upgrade pillow
```

## Setting up Unsloth

```python
from unsloth import FastLanguageModel
import torch

max_seq_length = 1024
lora_rank = 32

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="google/gemma-3-1b-it",
    max_seq_length=max_seq_length,
    load_in_4bit=True,
    fast_inference=True,  # Enable vLLM fast inference
    max_lora_rank=lora_rank,
    gpu_memory_utilization=0.6,
)

model = FastLanguageModel.get_peft_model(
    model,
    r=lora_rank,
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ],
    lora_alpha=lora_rank,
    use_gradient_checkpointing="unsloth",
    random_state=3407,
)
```

4-bit quantization + LoRA.

## Data Preparation — GSM8K

```python
SYSTEM_PROMPT = """
Respond in the following format:

<reasoning>
...
</reasoning>
<answer>
...
</answer>
"""

XML_COT_FORMAT = """\
<reasoning>
{reasoning}
</reasoning>
<answer>
{answer}
</answer>
"""
```

```python
import re
from datasets import load_dataset, Dataset

def extract_xml_answer(text: str) -> str:
    answer = text.split("<answer>")[-1]
    answer = answer.split("</answer>")[0]
    return answer.strip()

def extract_hash_answer(text: str) -> str | None:
    if "####" not in text:
        return None
    return text.split("####")[1].strip()

def get_gsm8k_questions(split="train") -> Dataset:
    data = load_dataset("openai/gsm8k", "main")[split]
    data = data.map(
        lambda x: {
            "prompt": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": x["question"]},
            ],
            "answer": extract_hash_answer(x["answer"]),
        }
    )
    return data

dataset = get_gsm8k_questions()
```

## Defining Reward Functions

```python
def correctness_reward_func(prompts, completions, answer, **kwargs) -> list[float]:
    responses = [completion[0]["content"] for completion in completions]
    q = prompts[0][-1]["content"]
    extracted_responses = [extract_xml_answer(r) for r in responses]
    return [2.0 if r == a else 0.0 for r, a in zip(extracted_responses, answer)]

def int_reward_func(completions, **kwargs) -> list[float]:
    responses = [completion[0]["content"] for completion in completions]
    extracted_responses = [extract_xml_answer(r) for r in responses]
    return [0.5 if r.isdigit() else 0.0 for r in extracted_responses]

def strict_format_reward_func(completions, **kwargs) -> list[float]:
    pattern = r"^<reasoning>\n.*?\n</reasoning>\n<answer>\n.*?\n</answer>\n$"
    responses = [completion[0]["content"] for completion in completions]
    matches = [re.match(pattern, r) for r in responses]
    return [0.5 if match else 0.0 for match in matches]

def soft_format_reward_func(completions, **kwargs) -> list[float]:
    pattern = r"<reasoning>.*?</reasoning>\s*<answer>.*?</answer>"
    responses = [completion[0]["content"] for completion in completions]
    matches = [re.match(pattern, r) for r in responses]
    return [0.5 if match else 0.0 for match in matches]

def count_xml(text) -> float:
    count = 0.0
    if text.count("<reasoning>\n") == 1:
        count += 0.125
    if text.count("\n</reasoning>\n") == 1:
        count += 0.125
    if text.count("\n<answer>\n") == 1:
        count += 0.125
        count -= len(text.split("\n</answer>\n")[-1]) * 0.001
    if text.count("\n</answer>") == 1:
        count += 0.125
        count -= (len(text.split("\n</answer>")[-1]) - 1) * 0.001
    return count

def xmlcount_reward_func(completions, **kwargs) -> list[float]:
    contents = [completion[0]["content"] for completion in completions]
    return [count_xml(c) for c in contents]
```

| Reward Function | Purpose |
|-----------------|---------|
| `correctness_reward_func` | Rewards correct answer |
| `int_reward_func` | Rewards numeric answer |
| `strict_format_reward_func` and `soft_format_reward_func` | Reward format compliance |
| `xmlcount_reward_func` | Rewards proper XML tag usage |

## Training with GRPO

```python
from trl import GRPOConfig, GRPOTrainer

max_prompt_length = 256

training_args = GRPOConfig(
    learning_rate=5e-6,
    adam_beta1=0.9,
    adam_beta2=0.99,
    weight_decay=0.1,
    warmup_ratio=0.1,
    lr_scheduler_type="cosine",
    optim="paged_adamw_8bit",
    logging_steps=1,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=1,
    num_generations=6,
    max_prompt_length=max_prompt_length,
    max_completion_length=max_seq_length - max_prompt_length,
    max_steps=250,
    save_steps=250,
    max_grad_norm=0.1,
    report_to="none",
    output_dir="outputs",
)

trainer = GRPOTrainer(
    model=model,
    processing_class=tokenizer,
    reward_funcs=[
        xmlcount_reward_func,
        soft_format_reward_func,
        strict_format_reward_func,
        int_reward_func,
        correctness_reward_func,
    ],
    args=training_args,
    train_dataset=dataset,
)

trainer.train()
```

> Training may take some time. You might not see rewards increase immediately — it can take 150-200 steps before improvements appear.

## Testing the Model

```python
model.save_lora("grpo_saved_lora")
```

```python
from vllm import SamplingParams

text = tokenizer.apply_chat_template(
    [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Calculate pi."},
    ],
    tokenize=False,
    add_generation_prompt=True,
)

sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=1024)
output = (
    model.fast_generate(
        text,
        sampling_params=sampling_params,
        lora_request=model.load_lora("grpo_saved_lora"),
    )[0]
    .outputs[0]
    .text
)
print(output)
```

## Saving the Model

```python
# Merge to 16-bit
model.save_pretrained_merged("model", tokenizer, save_method="merged_16bit")

# Push to Hub
model.push_to_hub_merged(
    "your-username/model-name", tokenizer, save_method="merged_16bit", token="your-token"
)

# GGUF for llama.cpp
model.push_to_hub_gguf(
    "your-username/model-name",
    tokenizer,
    quantization_method=["q4_k_m", "q8_0", "q5_k_m"],
    token="your-token",
)
```
