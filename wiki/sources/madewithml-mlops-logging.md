---
title: "Made With ML — Logging for ML Systems"
type: source
tags: [mlops, made-with-ml, logging, observability]
date: 2026-05-15
source_file: raw/madewithml/mlops-logging.md
---

## Summary
Made With ML lesson on application logging for ML systems. Introduces the three building blocks (Logger, Handler, Formatter), the five severity levels (DEBUG → CRITICAL), and shows how to configure Python's `logging` module via a dict-config with `minimal` and `detailed` formatters, a stdout console handler, and rotating file handlers for `info.log` and `error.log`. Closes with placement guidance: log inside high-level workflows, not inside small modular functions.

## Key Claims
- Logging beats `print` because it routes messages to specific destinations with custom formatting and shared interfaces — a precondition for [[Observability]] in production.
- Three primitives suffice for most projects: Logger emits, Handler routes, Formatter styles.
- Severity levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) gate which messages reach which handler; the logger's level acts as a floor.
- Rotating file handlers (e.g. 1 MB cap, 10 backups) prevent unbounded log growth without losing recent history.
- A dict-based config is preferred over scripted handler-by-handler setup or `.ini` files for readability and version-control diff-ability.
- `rich.logging.RichHandler` upgrades console output with color and tracebacks without changing the rest of the config.
- Placement heuristic: log inside `main.py` / `train.py` orchestration scripts, not inside small data/eval helpers — if you feel the urge to log inside a helper, the helper is probably too large.
- For production, ship logs to cloud blob storage (S3, GCS) or stand up an Elastic stack (ELK) rather than relying on local files.

## Key Quotes
> "A best practice is to not clutter our modular functions with log statements. Instead we should log messages outside of small functions and inside larger workflows." — on where logging belongs in the call graph

## Connections
- [[MadeWithML]] — source course
- [[GokuMohandas]] — author
- [[Anyscale]] — publisher
- [[PythonLogging]] — the stdlib module
- [[Logging]] — primary concept
- [[Observability]] — broader umbrella
- [[RichLibrary]] — `RichHandler` for console
- [[ElasticStack]] — production log pipeline (ELK)
- [[AmazonS3]] — log archival target
- [[GoogleCloudStorage]] — log archival target
- [[MLOps]] — discipline
- [[RotatingFileHandler]] — log-rotation pattern
- [[StructuredLogging]] — implicit goal of formatters

## Contradictions
- None identified.
