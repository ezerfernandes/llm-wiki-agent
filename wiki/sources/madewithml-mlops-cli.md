---
title: "Made With ML — Command-Line Interface (CLI)"
type: source
tags: [mlops, made-with-ml, cli, developer-experience]
date: 2026-05-15
source_file: raw/madewithml/mlops-cli.md
---

## Summary
Made With ML lesson on exposing ML workloads as CLI commands so users can run them without knowing the underlying Python. Compares three approaches — importing functions, using `if __name__ == "__main__"` with hard-coded args, and `argparse` — then standardizes on [[Typer]] for richer commands, typed inputs with `Annotated`, help strings via `typer.Option`, and automatic `--help` output.

## Key Claims
- A good CLI hides the code: users invoke `python madewithml/train.py --experiment-name llm ...` without importing anything or knowing the function signature.
- The `if __name__ == "__main__"` plus hard-coded args approach is too rigid — only one workload per script and no runtime input.
- `argparse` is acceptable for single-workload scripts (e.g. `serve.py` with one `serve.run()` call) but does not scale to multiple commands in one module.
- [[Typer]] lets you decorate multiple functions with `@app.command()`, making one script expose many subcommands.
- `Annotated[str, typer.Option(help="...")]` carries both typing information and help text, so `--help` is self-documenting and IDEs see the types.
- All input arguments should be made optional in the function signature so users must pass them explicitly via CLI flags — this prevents silent default-driven misconfiguration.
- The README should hold canonical CLI invocations for every workload (train, tune, evaluate, inference, serve).

## Key Quotes
> "We make all of our input arguments optional so that we can explicitly define them in our CLI commands." — on enforcing explicit configuration via CLI

## Connections
- [[MadeWithML]] — source course
- [[GokuMohandas]] — author
- [[Anyscale]] — publisher
- [[Typer]] — CLI library
- [[Argparse]] — alternative stdlib option
- [[PythonLanguage]] — host language
- [[Ray]] — runtime initialized in CLI entrypoint
- [[CLI]] — primary concept
- [[DeveloperExperience]] — motivation
- [[MLOps]] — discipline
- [[WorkloadFunction]] — what each CLI command wraps

## Contradictions
- None identified.
