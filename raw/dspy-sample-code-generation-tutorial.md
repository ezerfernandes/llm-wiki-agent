# Automated Code Generation from Documentation with DSPy

Source: https://dspy.ai/tutorials/sample_code_generation/
Fetched: 2026-05-24

## Overview

Tutorial teaches building a documentation-powered code generation system using DSPy that can "automatically fetch documentation from URLs and generate working code examples for any library."

## What You'll Build

A system capable of:
- Fetching and parsing documentation from multiple URLs
- Extracting API patterns, methods, and usage examples
- Generating working code for specific use cases
- Providing explanations and best practices
- Working with any library's documentation

## Setup

Install required dependencies:

```bash
pip install dspy requests beautifulsoup4 html2text
```

## Step 1: Documentation Fetching and Processing

The tutorial provides a `DocumentationFetcher` class that:
- Fetches content from URLs with retry logic
- Uses BeautifulSoup to parse HTML
- Converts HTML to markdown for better LLM processing
- Removes scripts, styles, navigation, and footer elements

Key initialization includes setting User-Agent headers and configuring html2text converter.

The `fetch_url()` method implements retry logic (default 3 attempts) with delays between requests. Returns a dictionary containing URL, title, markdown content, and success status.

Two signature classes are defined:

- `LibraryAnalyzer`: Analyzes documentation to extract core concepts, patterns, methods, installation info, and examples.
- `CodeGenerator`: Generates code examples for specific use cases with explanations, best practices, and required imports.

The `DocumentationLearningAgent` class combines these components, using `ChainOfThought` modules for reasoning.

## Step 2: Learning from Documentation URLs

The `learn_library_from_urls()` function demonstrates learning about FastAPI and Streamlit:

```python
fastapi_urls = [
    "https://fastapi.tiangolo.com/",
    "https://fastapi.tiangolo.com/tutorial/first-steps/",
    "https://fastapi.tiangolo.com/tutorial/path-params/",
    "https://fastapi.tiangolo.com/tutorial/query-params/"
]
```

The learning process:
1. Fetches all documentation URLs
2. Combines successful fetches into a single content block
3. Analyzes the combined documentation
4. Returns library analysis with core concepts, patterns, methods, and installation details

## Step 3: Generating Code Examples

The `generate_examples_for_library()` function creates three generic use cases:

- "Basic Setup and Hello World"
- "Common Operations"
- "Advanced Usage"

For each use case it:
1. Formats library information for the code generator
2. Calls the `generate_example()` method
3. Displays the generated code, imports, explanation, and best practices
4. Stores results in a structured format

## Step 4: Interactive Library Learning Function

The `learn_any_library()` function provides a programmatic interface that:
- Takes library name, documentation URLs, and optional use cases
- Learns from documentation
- Generates examples for each use case
- Returns a dictionary with library info and all examples

The `interactive_learning_session()` function creates an interactive CLI experience.

Users can:
- Enter any library name
- Provide multiple documentation URLs
- Define custom use cases (or use defaults)
- View generated examples
- Save results to JSON files
- Learn multiple libraries in one session

The session provides a complete workflow with prompts for library selection, URL input, use case customization, example viewing, and results saving.

## Example Output

When running the interactive system with FastAPI:

Learning Phase Output:
- Status indicators show URL fetching progress
- Summary displays successful fetches and identified concepts
- "Core Concepts: ['FastAPI app', 'path operations', 'dependencies', 'request/response models']"
- Installation instructions extracted from documentation

Code Generation Example:

The tutorial shows a generated authentication example including:
- JWT token verification with HTTPBearer security
- Login endpoint returning JWT tokens
- Protected route requiring authentication
- Proper error handling with HTTP exceptions

Generated code includes:

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import uvicorn
```

Output includes:
- Complete working code
- Required imports and dependencies
- Step-by-step explanations
- Best practices list (secret key management, password hashing, token expiration, error handling)

## Next Steps

Suggested enhancements:
- GitHub integration for README files and repositories
- Video tutorial processing for documentation
- Community example aggregation from forums
- Version comparison tracking API changes
- Automatic unit test generation
- Documentation page crawling for active learning

## Key Features Demonstrated

1. **Robust Fetching**: Handles network errors with retry logic and delays respecting server resources
2. **Content Processing**: Removes unnecessary elements and converts to markdown for optimal LLM comprehension
3. **Multi-Stage Analysis**: Separates documentation understanding from code generation for better results
4. **Interactive Interface**: Allows users to customize learning experiences with custom use cases
5. **Flexible Output**: Supports viewing examples interactively and saving results to files

The system demonstrates how DSPy enables "rapid technology adoption and exploration" by automating documentation analysis and practical code generation.
