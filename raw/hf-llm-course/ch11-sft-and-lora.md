# HuggingFace LLM Course — Chapter 11: Fine-tune Large Language Models using SFT and LoRA
Source: https://huggingface.co/learn/llm-course/chapter11/
Sections: 1,2,3,4,5,6
---

## Section 1: Introduction

# Supervised Fine-Tuning

In [Chapter 2 Section 2](/course/chapter2/2), we saw that generative language models can be fine-tuned on specific tasks like summarization and question answering. However, nowadays it is far more common to fine-tune language models on a broad range of tasks simultaneously; a method known as supervised fine-tuning (SFT). This process helps models become more versatile and capable of handling diverse use cases. Most LLMs that people interact with on platforms like ChatGPT have undergone SFT to make them more helpful and aligned with human preferences. We will separate this chapter into four sections:

### 1️⃣ Chat Templates

Chat templates structure interactions between users and AI models, ensuring consistent and contextually appropriate responses. They include components like system prompts and role-based messages.

### 2️⃣ Supervised Fine-Tuning

Supervised Fine-Tuning (SFT) is a critical process for adapting pre-trained language models to specific tasks. It involves training the model on a task-specific dataset with labeled examples. For a detailed guide on SFT, including key steps and best practices, see [the supervised fine-tuning section of the TRL documentation](https://huggingface.co/docs/trl/en/sft_trainer).

### 3️⃣ Low Rank Adaptation (LoRA)

Low Rank Adaptation (LoRA) is a technique for fine-tuning language models by adding low-rank matrices to the model's layers. This allows for efficient fine-tuning while preserving the model's pre-trained knowledge. One of the key benefits of LoRA is the significant memory savings it offers, making it possible to fine-tune large models on hardware with limited resources.

### 4️⃣ Evaluation

Evaluation is a crucial step in the fine-tuning process. It allows us to measure the performance of the model on a task-specific dataset.

> [!TIP]
> ⚠️ In order to benefit from all features available with the Model Hub and 🤗 Transformers, we recommend creating an account.

### References

- [Transformers documentation on chat templates](https://huggingface.co/docs/transformers/main/en/chat_templating)
- [Script for Supervised Fine-Tuning in TRL](https://github.com/huggingface/trl/blob/main/trl/scripts/sft.py)
- [`SFTTrainer` in TRL](https://huggingface.co/docs/trl/main/en/sft_trainer)
- [Direct Preference Optimization Paper](https://arxiv.org/abs/2305.18290)
- [Supervised Fine-Tuning with TRL](https://huggingface.co/docs/trl/sft_trainer)
- [How to fine-tune Google Gemma with ChatML and Hugging Face TRL](https://github.com/huggingface/alignment-handbook)
- [Fine-tuning LLM to Generate Persian Product Catalogs in JSON Format](https://huggingface.co/learn/cookbook/en/fine_tuning_llm_to_generate_persian_product_catalogs_in_json_format)

---

## Section 2: Chat Templates

# Chat Templates

### Introduction

Chat templates are essential for structuring interactions between language models and users. Whether you're building a simple chatbot or a complex AI agent, understanding how to properly format your conversations is crucial for getting the best results from your model. In this guide, we'll explore what chat templates are, why they matter, and how to use them effectively.

> [!TIP]
> Chat templates are crucial for:
> - Maintaining consistent conversation structure
> - Ensuring proper role identification
> - Managing context across multiple turns
> - Supporting advanced features like tool use

### Model Types and Templates

#### Base Models vs Instruct Models
A base model is trained on raw text data to predict the next token, while an instruct model is fine-tuned specifically to follow instructions and engage in conversations. For example, [`SmolLM2-135M`](https://huggingface.co/HuggingFaceTB/SmolLM2-135M) is a base model, while [`SmolLM2-135M-Instruct`](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct) is its instruction-tuned variant.

Instruction tuned models are trained to follow a specific conversational structure, making them more suitable for chatbot applications. Moreover, instruct models can handle complex interactions, including tool use, multimodal inputs, and function calling.

To make a base model behave like an instruct model, we need to format our prompts in a consistent way that the model can understand. This is where chat templates come in. ChatML is one such template format that structures conversations with clear role indicators (system, user, assistant). Here's a guide on [ChatML](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct/blob/e2c3f7557efbdec707ae3a336371d169783f1da1/tokenizer_config.json#L146).

> [!WARNING]
> When using an instruct model, always verify you're using the correct chat template format. Using the wrong template can result in poor model performance or unexpected behavior. The easiest way to ensure this is to check the model tokenizer configuration on the Hub. For example, the `SmolLM2-135M-Instruct` model uses this configuration.

#### Common Template Formats

Before diving into specific implementations, it's important to understand how different models expect their conversations to be formatted. Let's explore some common template formats using a simple example conversation:

We'll use the following conversation structure for all examples:

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi! How can I help you today?"},
    {"role": "user", "content": "What's the weather?"},
]
```

This is the ChatML template used in models like SmolLM2 and Qwen 2:

```sh
system
You are a helpful assistant.
user
Hello!
assistant
Hi! How can I help you today?
user
What's the weather?assistant
```

This is using the `mistral` template format:

```sh
[INST] You are a helpful assistant. [/INST]
Hi! How can I help you today?
[INST] Hello! [/INST]
```

Key differences between these formats include:
1. **System Message Handling**:
   - Llama 2 wraps system messages in `>` tags
   - Llama 3 uses `` tags with `` endings
   - Mistral includes system message in the first instruction
   - Qwen uses explicit `system` role with `` tags
   - ChatGPT uses `SYSTEM:` prefix

2. **Message Boundaries**:
   - Llama 2 uses `[INST]` and `[/INST]` tags
   - Llama 3 uses role-specific tags (``, ``, ``) with `` endings
   - Mistral uses `[INST]` and `[/INST]` with `` and ``
   - Qwen uses role-specific start/end tokens

3. **Special Tokens**:
   - Llama 2 uses `` and `` for conversation boundaries
   - Llama 3 uses `` to end each message
   - Mistral uses `` and `` for turn boundaries
   - Qwen uses role-specific start/end tokens

Understanding these differences is key to working with various models. Let's look at how the transformers library helps us handle these variations automatically:

```python
from transformers import AutoTokenizer

# These will use different templates automatically
mistral_tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
qwen_tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-7B-Chat")
smol_tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-135M-Instruct")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"},
]

# Each will format according to its model's template
mistral_chat = mistral_tokenizer.apply_chat_template(messages, tokenize=False)
qwen_chat = qwen_tokenizer.apply_chat_template(messages, tokenize=False)
smol_chat = smol_tokenizer.apply_chat_template(messages, tokenize=False)
```

Click to see template examples

Qwen 2 and SmolLM2 ChatML template:

```sh
system
You are a helpful assistant.
user
Hello!
assistant
Hi! How can I help you today?
user
What's the weather?assistant
```

Mistral template:

```sh
[INST] You are a helpful assistant. [/INST]
Hi! How can I help you today?
[INST] Hello! [/INST]
```

#### Advanced Features
Chat templates can handle more complex scenarios beyond just conversational interactions, including:

1. **Tool Use**: When models need to interact with external tools or APIs
2. **Multimodal Inputs**: For handling images, audio, or other media types
3. **Function Calling**: For structured function execution
4. **Multi-turn Context**: For maintaining conversation history

> [!TIP]
> When implementing advanced features:
> - Test thoroughly with your specific model. Vision and tool use template are particularly diverse.
> - Monitor token usage carefully between each feature and model.
> - Document the expected format for each feature

For multimodal conversations, chat templates can include image references or base64-encoded images:

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful vision assistant that can analyze images.",
    },
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {"type": "image", "image_url": "https://example.com/image.jpg"},
        ],
    },
]
```

Here's an example of a chat template with tool use:

```python
messages = [
    {
        "role": "system",
        "content": "You are an AI assistant that can use tools. Available tools: calculator, weather_api",
    },
    {"role": "user", "content": "What's 123 * 456 and is it raining in Paris?"},
    {
        "role": "assistant",
        "content": "Let me help you with that.",
        "tool_calls": [
            {
                "tool": "calculator",
                "parameters": {"operation": "multiply", "x": 123, "y": 456},
            },
            {"tool": "weather_api", "parameters": {"city": "Paris", "country": "France"}},
        ],
    },
    {"role": "tool", "tool_name": "calculator", "content": "56088"},
    {
        "role": "tool",
        "tool_name": "weather_api",
        "content": "{'condition': 'rain', 'temperature': 15}",
    },
]
```

### Best Practices

#### General Guidelines
When working with chat templates, follow these key practices:

1. **Consistent Formatting**: Always use the same template format throughout your application
2. **Clear Role Definition**: Clearly specify roles (system, user, assistant, tool) for each message
3. **Context Management**: Be mindful of token limits when maintaining conversation history
4. **Error Handling**: Include proper error handling for tool calls and multimodal inputs
5. **Validation**: Validate message structure before sending to the model

> [!WARNING]
> Common pitfalls to avoid:
> - Mixing different template formats in the same application
> - Exceeding token limits with long conversation histories
> - Not properly escaping special characters in messages
> - Forgetting to validate input message structure
> - Ignoring model-specific template requirements

### Hands-on Exercise

Let's practice implementing chat templates with a real-world example.

> [!TIP]
> Follow these steps to convert the `HuggingFaceTB/smoltalk` dataset into chatml format:
>
> 1. Load the dataset:
> ```python
> from datasets import load_dataset
>
> dataset = load_dataset("HuggingFaceTB/smoltalk")
> ```
>
> 2. Create a processing function:
> ```python
> def convert_to_chatml(example):
>     return {
>         "messages": [
>             {"role": "user", "content": example["input"]},
>             {"role": "assistant", "content": example["output"]},
>         ]
>     }
> ```
>
> 3. Apply the chat template using your chosen model's tokenizer
>
> Remember to validate your output format matches your target model's requirements!

### Additional Resources

- [Hugging Face Chat Templating Guide](https://huggingface.co/docs/transformers/main/en/chat_templating)
- [Transformers Documentation](https://huggingface.co/docs/transformers)
- [Chat Templates Examples Repository](https://github.com/chujiezheng/chat_templates)

---

## Section 3: Fine-Tuning with SFTTrainer

# Supervised Fine-Tuning

Supervised Fine-Tuning (SFT) is a process primarily used to adapt pre-trained language models to follow instructions, engage in dialogue, and use specific output formats. While pre-trained models have impressive general capabilities, SFT helps transform them into assistant-like models that can better understand and respond to user prompts. This is typically done by training on datasets of human-written conversations and instructions.

This page provides a step-by-step guide to fine-tuning the [`deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B) model using the [`SFTTrainer`](https://huggingface.co/docs/trl/en/sft_trainer). By following these steps, you can adapt the model to perform specific tasks more effectively.

### When to Use SFT

Before diving into implementation, it's important to understand when SFT is the right choice for your project. As a first step, you should consider whether using an existing instruction-tuned model with well-crafted prompts would suffice for your use case. SFT involves significant computational resources and engineering effort, so it should only be pursued when prompting existing models proves insufficient.

> [!TIP]
> Consider SFT only if you:
> - Need additional performance beyond what prompting can achieve
> - Have a specific use case where the cost of using a large general-purpose model outweighs the cost of fine-tuning a smaller model
> - Require specialized output formats or domain-specific knowledge that existing models struggle with

If you determine that SFT is necessary, the decision to proceed depends on two primary factors:

#### Template Control
SFT allows precise control over the model's output structure. This is particularly valuable when you need the model to:
1. Generate responses in a specific chat template format
2. Follow strict output schemas
3. Maintain consistent styling across responses

#### Domain Adaptation
When working in specialized domains, SFT helps align the model with domain-specific requirements by:
1. Teaching domain terminology and concepts
2. Enforcing professional standards
3. Handling technical queries appropriately
4. Following industry-specific guidelines

> [!TIP]
> Before starting SFT, evaluate whether your use case requires:
> - Precise output formatting
> - Domain-specific knowledge
> - Consistent response patterns
> - Adherence to specific guidelines
>
> This evaluation will help determine if SFT is the right approach for your needs.

### Dataset Preparation

The supervised fine-tuning process requires a task-specific dataset structured with input-output pairs. Each pair should consist of:
1. An input prompt
2. The expected model response
3. Any additional context or metadata

The quality of your training data is crucial for successful fine-tuning. Let's look at how to prepare and validate your dataset:

### Training Configuration

The success of your fine-tuning depends heavily on choosing the right training parameters. Let's explore each important parameter and how to configure them effectively:

The SFTTrainer configuration requires consideration of several parameters that control the training process. Let's explore each parameter and their purpose:

1. **Training Duration Parameters**:
   - `num_train_epochs`: Controls total training duration
   - `max_steps`: Alternative to epochs, sets maximum number of training steps
   - More epochs allow better learning but risk overfitting

2. **Batch Size Parameters**:
   - `per_device_train_batch_size`: Determines memory usage and training stability
   - `gradient_accumulation_steps`: Enables larger effective batch sizes
   - Larger batches provide more stable gradients but require more memory

3. **Learning Rate Parameters**:
   - `learning_rate`: Controls size of weight updates
   - `warmup_ratio`: Portion of training used for learning rate warmup
   - Too high can cause instability, too low results in slow learning

4. **Monitoring Parameters**:
   - `logging_steps`: Frequency of metric logging
   - `eval_steps`: How often to evaluate on validation data
   - `save_steps`: Frequency of model checkpoint saves

> [!TIP]
> Start with conservative values and adjust based on monitoring:
> - Begin with 1-3 epochs
> - Use smaller batch sizes initially
> - Monitor validation metrics closely
> - Adjust learning rate if training is unstable

### Implementation with TRL

Now that we understand the key components, let's implement the training with proper validation and monitoring. We will use the `SFTTrainer` class from the Transformers Reinforcement Learning (TRL) library, which is built on top of the `transformers` library. Here's a complete example using the TRL library:

```python
from datasets import load_dataset
from trl import SFTConfig, SFTTrainer
import torch

# Set device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load dataset
dataset = load_dataset("HuggingFaceTB/smoltalk", "all")

# Configure model and tokenizer
model_name = "HuggingFaceTB/SmolLM2-135M"
model = AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path=model_name).to(
    device
)
tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path=model_name)
# Setup chat template
model, tokenizer = setup_chat_format(model=model, tokenizer=tokenizer)

# Configure trainer
training_args = SFTConfig(
    output_dir="./sft_output",
    max_steps=1000,
    per_device_train_batch_size=4,
    learning_rate=5e-5,
    logging_steps=10,
    save_steps=100,
    eval_strategy="steps",
    eval_steps=50,
)

# Initialize trainer
trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    processing_class=tokenizer,
)

# Start training
trainer.train()
```

> [!TIP]
> When using a dataset with a "messages" field (like the example above), the SFTTrainer automatically applies the model's chat template, which it retrieves from the hub. This means you don't need any additional configuration to handle chat-style conversations - the trainer will format the messages according to the model's expected template format.

### Packing the Dataset

The SFTTrainer supports example packing to optimize training efficiency. This feature allows multiple short examples to be packed into the same input sequence, maximizing GPU utilization during training. To enable packing, simply set `packing=True` in the SFTConfig constructor. When using packed datasets with `max_steps`, be aware that you may train for more epochs than expected depending on your packing configuration. You can customize how examples are combined using a formatting function - particularly useful when working with datasets that have multiple fields like question-answer pairs. For evaluation datasets, you can disable packing by setting `eval_packing=False` in the SFTConfig. Here's a basic example of customizing the packing configuration:

```python
# Configure packing
training_args = SFTConfig(packing=True)

trainer = SFTTrainer(model=model, train_dataset=dataset, args=training_args)

trainer.train()
```

When packing the dataset with multiple fields, you can define a custom formatting function to combine the fields into a single input sequence. This function should take a list of examples and return a dictionary with the packed input sequence. Here's an example of a custom formatting function:

```python
def formatting_func(example):
    text = f"### Question: {example['question']}\n ### Answer: {example['answer']}"
    return text

training_args = SFTConfig(packing=True)
trainer = SFTTrainer(
    "facebook/opt-350m",
    train_dataset=dataset,
    args=training_args,
    formatting_func=formatting_func,
)
```

### Monitoring Training Progress

Effective monitoring is crucial for successful fine-tuning. Let's explore what to watch for during training:

#### Understanding Loss Patterns

Training loss typically follows three distinct phases:
1. Initial Sharp Drop: Rapid adaptation to new data distribution
2. Gradual Stabilization: Learning rate slows as model fine-tunes
3. Convergence: Loss values stabilize, indicating training completion

#### Metrics to Monitor

Effective monitoring involves tracking quantitative metrics, and evaluating qualitative metrics. Available metrics are:

- Training loss
- Validation loss
- Learning rate progression
- Gradient norms

> [!WARNING]
> Watch for these warning signs during training:
> 1. Validation loss increasing while training loss decreases (overfitting)
> 2. No significant improvement in loss values (underfitting)
> 3. Extremely low loss values (potential memorization)
> 4. Inconsistent output formatting (template learning issues)

#### The Path to Convergence

As training progresses, the loss curve should gradually stabilize. The key indicator of healthy training is a small gap between training and validation loss, suggesting
the model is learning generalizable patterns rather than memorizing specific examples. The absolute loss values will vary depending on your task and dataset.

#### Monitoring Training Progress

The graph above shows a typical training progression. Notice how both training and validation loss decrease sharply at first, then gradually level off. This pattern indicates the model is learning effectively while maintaining generalization ability.

#### Warning Signs to Watch For

Several patterns in the loss curves can indicate potential issues. Below we illustrate common warning signs and solutions that we can consider.

If the validation loss decreases at a significantly slower rate than training loss, your model is likely overfitting to the training data. Consider:
- Reducing the training steps
- Increasing the dataset size
- Validating dataset quality and diversity

If the loss doesn't show significant improvement, the model might be:
- Learning too slowly (try increasing the learning rate)
- Struggling with the task (check data quality and task complexity)
- Hitting architecture limitations (consider a different model)

Extremely low loss values could suggest memorization rather than learning. This is particularly concerning if:
- The model performs poorly on new, similar examples
- The outputs lack diversity
- The responses are too similar to training examples

> [!WARNING]
> Monitor both the loss values and the model's actual outputs during training. Sometimes the loss can look good while the model develops unwanted behaviors. Regular qualitative evaluation of the model's responses helps catch issues that metrics alone might miss.

We should note that the interpretation of the loss values we outline here is aimed on the most common case, and in fact, loss values can behave on various ways depending on the model, the dataset, the training parameters, etc. If you interested in exploring more about outlined patterns, you should check out this blog post by the people at [Fast AI](https://www.fast.ai/posts/2023-09-04-learning-jumps/).

### Evaluation after SFT

In section [11.4](/en/chapter11/4) we will learn how to evaluate the model using benchmark datasets. For now, we will focus on the qualitative evaluation of the model.

After completing SFT, consider these follow-up actions:

1. Evaluate the model thoroughly on held-out test data
2. Validate template adherence across various inputs
3. Test domain-specific knowledge retention
4. Monitor real-world performance metrics

> [!TIP]
> Document your training process, including:
> - Dataset characteristics
> - Training parameters
> - Performance metrics
> - Known limitations
> This documentation will be valuable for future model iterations.

### Quiz

#### 1. What parameters control the training duration in SFT?

#### 2. Which pattern in the loss curves indicates potential overfitting?

#### 3. What is gradient_accumulation_steps used for?

#### 4. What should you monitor during SFT training?

#### 5. What indicates healthy convergence during training?

### Additional Resources

- [TRL Documentation](https://huggingface.co/docs/trl)
- [SFT Examples Repository](https://github.com/huggingface/trl/blob/main/trl/scripts/sft.py)
- [Fine-tuning Best Practices](https://huggingface.co/docs/transformers/training)

---

## Section 4: LoRA (Low-Rank Adaptation)

# LoRA (Low-Rank Adaptation)

Fine-tuning large language models is a resource intensive process. LoRA is a technique that allows us to fine-tune large language models with a small number of parameters. It works by adding and optimizing smaller matrices to the attention weights, typically reducing trainable parameters by about 90%.

### Understanding LoRA

LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique that freezes the pre-trained model weights and injects trainable rank decomposition matrices into the model's layers. Instead of training all model parameters during fine-tuning, LoRA decomposes the weight updates into smaller matrices through low-rank decomposition, significantly reducing the number of trainable parameters while maintaining model performance. For example, when applied to GPT-3 175B, LoRA reduced trainable parameters by 10,000x and GPU memory requirements by 3x compared to full fine-tuning. You can read more about LoRA in the [LoRA paper](https://arxiv.org/pdf/2106.09685).

LoRA works by adding pairs of rank decomposition matrices to transformer layers, typically focusing on attention weights. During inference, these adapter weights can be merged with the base model, resulting in no additional latency overhead. LoRA is particularly useful for adapting large language models to specific tasks or domains while keeping resource requirements manageable.

### Key advantages of LoRA

1. **Memory Efficiency**:
   - Only adapter parameters are stored in GPU memory
   - Base model weights remain frozen and can be loaded in lower precision
   - Enables fine-tuning of large models on consumer GPUs

2. **Training Features**:
   - Native PEFT/LoRA integration with minimal setup
   - Support for QLoRA (Quantized LoRA) for even better memory efficiency

3. **Adapter Management**:
   - Adapter weight saving during checkpoints
   - Features to merge adapters back into base model

### Loading LoRA Adapters with PEFT

[PEFT](https://github.com/huggingface/peft) is a library that provides a unified interface for loading and managing PEFT methods, including LoRA. It allows you to easily load and switch between different PEFT methods, making it easier to experiment with different fine-tuning techniques.

Adapters can be loaded onto a pretrained model with `load_adapter()`, which is useful for trying out different adapters whose weights aren't merged. Set the active adapter weights with the `set_adapter()` function. To return the base model, you could use unload() to unload all of the LoRA modules. This makes it easy to switch between different task-specific weights.

```python
from peft import PeftModel, PeftConfig

config = PeftConfig.from_pretrained("ybelkada/opt-350m-lora")
model = AutoModelForCausalLM.from_pretrained(config.base_model_name_or_path)
lora_model = PeftModel.from_pretrained(model, "ybelkada/opt-350m-lora")
```

![lora_load_adapter](https://github.com/huggingface/smol-course/raw/main/3_parameter_efficient_finetuning/images/lora_adapter.png)

### Fine-tune LLM using `trl` and the `SFTTrainer` with LoRA

The [SFTTrainer](https://huggingface.co/docs/trl/sft_trainer) from `trl` provides integration with LoRA adapters through the [PEFT](https://huggingface.co/docs/peft/en/index) library. This means that we can fine-tune a model in the same way as we did with SFT, but use LoRA to reduce the number of parameters we need to train.

We'll use the `LoRAConfig` class from PEFT in our example. The setup requires just a few configuration steps:

1. Define the LoRA configuration (rank, alpha, dropout)
2. Create the SFTTrainer with PEFT config
3. Train and save the adapter weights

### LoRA Configuration

Let's walk through the LoRA configuration and key parameters.

| Parameter | Description |
|-----------|-------------|
| `r` (rank) | Dimension of the low-rank matrices used for weight updates. Typically between 4-32. Lower values provide more compression but potentially less expressiveness. |
| `lora_alpha` | Scaling factor for LoRA layers, usually set to 2x the rank value. Higher values result in stronger adaptation effects. |
| `lora_dropout` | Dropout probability for LoRA layers, typically 0.05-0.1. Higher values help prevent overfitting during training. |
| `bias` | Controls training of bias terms. Options are "none", "all", or "lora_only". "none" is most common for memory efficiency. |
| `target_modules` | Specifies which model modules to apply LoRA to. Can be "all-linear" or specific modules like "q_proj,v_proj". More modules enable greater adaptability but increase memory usage. |

> [!TIP]
> When implementing PEFT methods, start with small rank values (4-8) for LoRA and monitor training loss. Use validation sets to prevent overfitting and compare results with full fine-tuning baselines when possible. The effectiveness of different methods can vary by task, so experimentation is key.

### Using TRL with PEFT

PEFT methods can be combined with TRL for fine-tuning to reduce memory requirements. We can pass the  `LoraConfig` to the model when loading it.

```python
from peft import LoraConfig

# TODO: Configure LoRA parameters
# r: rank dimension for LoRA update matrices (smaller = more compression)
rank_dimension = 6
# lora_alpha: scaling factor for LoRA layers (higher = stronger adaptation)
lora_alpha = 8
# lora_dropout: dropout probability for LoRA layers (helps prevent overfitting)
lora_dropout = 0.05

peft_config = LoraConfig(
    r=rank_dimension,  # Rank dimension - typically between 4-32
    lora_alpha=lora_alpha,  # LoRA scaling factor - typically 2x rank
    lora_dropout=lora_dropout,  # Dropout probability for LoRA layers
    bias="none",  # Bias type for LoRA. the corresponding biases will be updated during training.
    target_modules="all-linear",  # Which modules to apply LoRA to
    task_type="CAUSAL_LM",  # Task type for model architecture
)
```

Above, we used `device_map="auto"` to automatically assign the model to the correct device. You can also manually assign the model to a specific device using `device_map={"": device_index}`.

We will also need to define the `SFTTrainer` with the LoRA configuration.

```python
# Create SFTTrainer with LoRA configuration
trainer = SFTTrainer(
    model=model,
    args=args,
    train_dataset=dataset["train"],
    peft_config=peft_config,  # LoRA configuration
    max_seq_length=max_seq_length,  # Maximum sequence length
    processing_class=tokenizer,
)
```

> [!TIP]
> ✏️ **Try it out!** Build on your fine-tuned model from the previous section, but fine-tune it with LoRA. Use the `HuggingFaceTB/smoltalk` dataset to fine-tune a `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B` model, using the LoRA configuration we defined above.

### Merging LoRA Adapters

After training with LoRA, you might want to merge the adapter weights back into the base model for easier deployment. This creates a single model with the combined weights, eliminating the need to load adapters separately during inference.

The merging process requires attention to memory management and precision. Since you'll need to load both the base model and adapter weights simultaneously, ensure sufficient GPU/CPU memory is available. Using `device_map="auto"` in `transformers` will find the correct device for the model based on your hardware.

Maintain consistent precision (e.g., float16) throughout the process, matching the precision used during training and saving the merged model in the same format for deployment.

### Merging Implementation

After training a LoRA adapter, you can merge the adapter weights back into the base model. Here's how to do it:

```python
import torch
from transformers import AutoModelForCausalLM
from peft import PeftModel

# 1. Load the base model
base_model = AutoModelForCausalLM.from_pretrained(
    "base_model_name", torch_dtype=torch.float16, device_map="auto"
)

# 2. Load the PEFT model with adapter
peft_model = PeftModel.from_pretrained(
    base_model, "path/to/adapter", torch_dtype=torch.float16
)

# 3. Merge adapter weights with base model
merged_model = peft_model.merge_and_unload()
```

If you encounter size discrepancies in the saved model, ensure you're also saving the tokenizer:

```python
# Save both model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("base_model_name")
merged_model.save_pretrained("path/to/save/merged_model")
tokenizer.save_pretrained("path/to/save/merged_model")
```

> [!TIP]
> ✏️ **Try it out!** Merge the adapter weights back into the base model. Use the `HuggingFaceTB/smoltalk` dataset to fine-tune a `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B` model, using the LoRA configuration we defined above.

### Resources

- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/pdf/2106.09685)
- [PEFT Documentation](https://huggingface.co/docs/peft)
- [Hugging Face blog post on PEFT](https://huggingface.co/blog/peft)

---

## Section 5: Evaluation

# Evaluation

With a finetuned model through either SFT or LoRA SFT, we should evaluate it on standard benchmarks. As machine learning engineers you should maintain a suite of relevant evaluations for your targeted domain of interest. In this page, we will look at some of the most common benchmarks and how to use them to evaluate your model. We'll also look at how to create custom benchmarks for your specific use case.

### Automatic Benchmarks

Automatic benchmarks serve as standardized tools for evaluating language models across different tasks and capabilities. While they provide a useful starting point for understanding model performance, it's important to recognize that they represent only one piece of a comprehensive evaluation strategy.

### Understanding Automatic Benchmarks

Automatic benchmarks typically consist of curated datasets with predefined tasks and evaluation metrics. These benchmarks aim to assess various aspects of model capability, from basic language understanding to complex reasoning. The key advantage of using automatic benchmarks is their standardization - they allow for consistent comparison across different models and provide reproducible results.

However, it's crucial to understand that benchmark performance doesn't always translate directly to real-world effectiveness. A model that excels at academic benchmarks may still struggle with specific domain applications or practical use cases.

### General Knowledge Benchmarks

[MMLU](https://huggingface.co/datasets/cais/mmlu) (Massive Multitask Language Understanding) tests knowledge across 57 subjects, from science to humanities. While comprehensive, it may not reflect the depth of expertise needed for specific domains. TruthfulQA evaluates a model's tendency to reproduce common misconceptions, though it can't capture all forms of misinformation.

### Reasoning Benchmarks

[BBH](https://huggingface.co/datasets/lukaemon/bbh) (Big Bench Hard) and [GSM8K](https://huggingface.co/datasets/openai/gsm8k) focus on complex reasoning tasks. BBH tests logical thinking and planning, while GSM8K specifically targets mathematical problem-solving. These benchmarks help assess analytical capabilities but may not capture the nuanced reasoning required in real-world scenarios.

### Language Understanding

[HELM](https://github.com/stanford-crfm/helm) provides a holistic evaluation framework. Benchmarks like HELM offer insights into language processing capabilities on aspects like commonsense, world knowledge, and reasoning. But may not fully represent the complexity of natural conversation or domain-specific terminology.

### Domain-Specific Benchmarks

Let's look at a few benchmarks that focus on specific domains like math, coding, and chat.

The [MATH benchmark](https://huggingface.co/papers/2103.03874) is another important evaluation tool for mathematical reasoning. It consists of 12,500 problems from mathematics competitions, covering algebra, geometry, number theory, counting, probability, and more. What makes MATH particularly challenging is that it requires multi-step reasoning, formal mathematical notation understanding, and the ability to generate step-by-step solutions. Unlike simpler arithmetic tasks, MATH problems often demand sophisticated problem-solving strategies and mathematical concept applications.

The [HumanEval Benchmark](https://github.com/openai/human-eval) is a coding-focused evaluation dataset consisting of 164 programming problems. The benchmark tests a model's ability to generate functionally correct Python code that solves the given programming tasks. What makes HumanEval particularly valuable is that it evaluates both code generation capabilities and functional correctness through actual test case execution, rather than just superficial similarity to reference solutions. The problems range from basic string manipulation to more complex algorithms and data structures.

[Alpaca Eval](https://tatsu-lab.github.io/alpaca_eval/) is an automated evaluation framework designed to assess the quality of instruction-following language models. It uses GPT-4 as a judge to evaluate model outputs across various dimensions including helpfulness, honesty, and harmlessness. The framework includes a dataset of 805 carefully curated prompts and can evaluate responses against multiple reference models like Claude, GPT-4, and others. What makes Alpaca Eval particularly useful is its ability to provide consistent, scalable evaluations without requiring human annotators, while still capturing nuanced aspects of model performance that traditional metrics might miss.

### Alternative Evaluation Approaches

Many organizations have developed alternative evaluation methods to address the limitations of standard benchmarks:

#### LLM-as-Judge

Using one language model to evaluate another's outputs has become increasingly popular. This approach can provide more nuanced feedback than traditional metrics, though it comes with its own biases and limitations.

#### Evaluation Arenas

Evaluation arenas like [Chatbot Arena](https://lmarena.ai/) offer a unique approach to LLM assessment through crowdsourced feedback. In these platforms, users engage in anonymous "battles" between two LLMs, asking questions and voting on which model provides better responses. This approach captures real-world usage patterns and preferences through diverse, challenging questions, with studies showing strong agreement between crowd-sourced votes and expert evaluations. While powerful, these platforms have limitations including potential user base bias, skewed prompt distributions, and a primary focus on helpfulness rather than safety considerations.

#### Custom Benchmark Suites

Organizations often develop internal benchmark suites tailored to their specific needs and use cases. These might include domain-specific knowledge tests or evaluation scenarios that mirror actual deployment conditions.

### Custom Evaluation

While standard benchmarks provide a useful baseline, they shouldn't be your only evaluation method. Here's how to develop a more comprehensive approach:

1. Start with relevant standard benchmarks to establish a baseline and enable comparison with other models.

2. Identify the specific requirements and challenges of your use case. What tasks will your model actually perform? What kinds of errors would be most problematic?

3. Develop custom evaluation datasets that reflect your actual use case. This might include:
   - Real user queries from your domain
   - Common edge cases you've encountered
   - Examples of particularly challenging scenarios

4. Consider implementing a multi-layered evaluation strategy:
   - Automated metrics for quick feedback
   - Human evaluation for nuanced understanding
   - Domain expert review for specialized applications
   - A/B testing in controlled environments

### Implementing Custom Evaluations

In this section, we will implement evaluation for our finetuned model. We can use [`lighteval`](https://github.com/huggingface/lighteval) to evaluate our finetuned model on standard benchmarks, which contains a wide range of tasks built into the library. We just need to define the tasks we want to evaluate and the parameters for the evaluation.

LightEval tasks are defined using a specific format:

```
{suite}|{task}|{num_few_shot}|{auto_reduce}
```

| Parameter | Description |
|-----------|-------------|
| `suite` | The benchmark suite (e.g., 'mmlu', 'truthfulqa') |
| `task` | Specific task within the suite (e.g., 'abstract_algebra') |
| `num_few_shot` | Number of examples to include in prompt (0 for zero-shot) |
| `auto_reduce` | Whether to automatically reduce few-shot examples if prompt is too long (0 or 1) |

Example: `"mmlu|abstract_algebra|0|0"` evaluates on MMLU's abstract algebra task with zero-shot inference.

### Example Evaluation Pipeline

Let's set up an evaluation pipeline for our finetuned model. We will evaluate the model on  set of sub tasks that relate to the domain of medicine.

Here's a complete example of evaluating on automatic benchmarks relevant to one specific domain using Lighteval with the VLLM backend:

```bash
lighteval accelerate \
    "pretrained=your-model-name" \
    "mmlu|anatomy|0|0" \
    "mmlu|high_school_biology|0|0" \
    "mmlu|high_school_chemistry|0|0" \
    "mmlu|professional_medicine|0|0" \
    --max_samples 40 \
    --batch_size 1 \
    --output_path "./results" \
    --save_generations true
```

Results are displayed in a tabular format showing:

```
|                  Task                  |Version|Metric|Value |   |Stderr|
|----------------------------------------|------:|------|-----:|---|-----:|
|all                                     |       |acc   |0.3333|±  |0.1169|
|leaderboard:mmlu:_average:5             |       |acc   |0.3400|±  |0.1121|
|leaderboard:mmlu:anatomy:5              |      0|acc   |0.4500|±  |0.1141|
|leaderboard:mmlu:high_school_biology:5  |      0|acc   |0.1500|±  |0.0819|
```

Lighteval also include a python API for more detailed evaluation tasks, which is useful for manipulating the results in a more flexible way. Check out the [Lighteval documentation](https://huggingface.co/docs/lighteval/using-the-python-api) for more information.

> [!TIP]
> ✏️ **Try it out!** Evaluate your finetuned model on a specific task in lighteval.

### End-of-chapter quiz

#### 1. What are the main advantages of using automatic benchmarks for model evaluation?

#### 2. Which benchmark specifically tests knowledge across 57 different subjects?

#### 3. What is LLM-as-Judge?

#### 4. What should be included in a comprehensive evaluation strategy?

#### 5. What is a limitation of automatic benchmarks?

#### 6. What is the purpose of creating custom evaluation datasets?

---

## Section 6: Conclusion

# Conclusion

In this chapter, we explored the essential components of fine-tuning language models:

1. **Chat Templates** provide structure to model interactions, ensuring consistent and appropriate responses through standardized formatting.

2. **Supervised Fine-Tuning (SFT)** allows adaptation of pre-trained models to specific tasks while maintaining their foundational knowledge.

3. **LoRA** offers an efficient approach to fine-tuning by reducing trainable parameters while preserving model performance.

4. **Evaluation** helps measure and validate the effectiveness of fine-tuning through various metrics and benchmarks.

These techniques, when combined, enable the creation of specialized language models that can excel at specific tasks while remaining computationally efficient. Whether you're building a customer service bot or a domain-specific assistant, understanding these concepts is crucial for successful model adaptation.
