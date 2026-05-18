# Learning DSPy: An Overview

Source: https://dspy.ai/learn/

DSPy provides a small, learnable API for building AI systems through an iterative development process. The framework organizes this journey into **three distinct stages** — programming, evaluation, and optimization — and the documentation advises following them in that order.

## The Three-Stage Model

### 1) DSPy Programming

> "defining your task, its constraints, exploring a few examples, and using that to inform your initial pipeline design"

The Programming stage is where the developer specifies *what* the system should do (signatures over inputs and outputs), composes the modules that implement that behavior (predictors, chain-of-thought, ReAct, RAG, etc.), wires the language model(s) and any external tools they need, and assembles a runnable pipeline. The output of this stage is an initial DSPy program that produces *some* answers — not necessarily good ones.

### 2) DSPy Evaluation

Once the pipeline is functioning, developers:

> "collect an initial development set, define your DSPy metric, and use these to iterate on your system more systematically"

The Evaluation stage is where the developer gathers a development set (input examples, possibly with gold outputs or rubric-style judgement criteria), declares a metric that converts a (prediction, example) pair into a numerical score, and runs that metric over the dev set to characterize the program's current behavior. This stage is what turns vibes-driven iteration into a measurable feedback loop.

### 3) DSPy Optimization

> "use DSPy optimizers to tune the prompts or weights in your program"

The Optimization stage is where DSPy compilers / optimizers ingest the program from stage 1 and the metric+data from stage 2, and search over prompts, demonstrations, and/or model weights to improve the metric. The output is an optimized program that scores better on the dev metric than the hand-written baseline.

## Learning Recommendation

The page is emphatic that the stages have a strict precedence:

> "it's unproductive to launch optimization runs using a poorly designed program or a bad metric"

In other words: **don't optimize what you cannot evaluate, and don't evaluate what you have not yet programmed clearly.** The recommended path is Programming → Evaluation → Optimization, with the developer free to iterate within and between stages as understanding of the task grows.

## Content Organization

The Learn section of dspy.ai covers thirteen pages, organized under the three stages:

**Programming** (seven pages):
- Programming Overview
- Language Models
- Signatures
- Modules
- Adapters
- Tools
- MCP

**Evaluation** (three pages):
- Evaluation Overview
- Data Handling
- Metrics

**Optimization** (two pages):
- Optimization Overview
- Optimizers

(Plus this top-level *Learn* index page itself.)

This structure reflects the recommended progression for developing AI systems effectively within the DSPy framework. The three sections map onto the three stages of the model, and each section's "Overview" page is the entry point for that stage.

## Key Terms Introduced (Forward References)

- **Signatures** — DSPy's declarative input-output specification (covered in its own page)
- **Modules** — composable DSPy program building blocks (covered in its own page)
- **Adapters** — translation layer between signatures and underlying LM APIs
- **Tools** — external function/API integration mechanism
- **MCP** — Model Context Protocol integration
- **Metrics** — scoring functions over (prediction, example) pairs
- **Optimizers** — the prompt/weight tuners that DSPy compiles programs through

Each of the above is the title of a separate Learn-section page.
