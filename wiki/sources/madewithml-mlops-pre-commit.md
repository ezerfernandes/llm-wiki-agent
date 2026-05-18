---
title: "Made With ML — Pre-commit Hooks"
type: source
tags: [mlops, made-with-ml, pre-commit, git, automation]
date: 2026-05-15
source_file: raw/madewithml/mlops-pre-commit.md
---

## Summary
Made With ML lesson on the [[PreCommit]] framework for running git hooks before each commit. Covers installation (`pre-commit install` + `pre-commit autoupdate`), config via `.pre-commit-config.yaml`, and three hook flavors: built-in (`check-yaml`, `check-merge-conflict`, `detect-aws-credentials`, `check-added-large-files`), custom third-party (Black's published hook), and local hooks that shell out to Makefile targets. Shows commit-time pass/fail output, manual hook execution with `pre-commit run`, the `--no-verify` skip (discouraged), and version bumping via `autoupdate`.

## Key Claims
- Pre-commit hooks shift quality checks left to the moment of commit, so style/lint/test failures never reach the remote.
- The config file `.pre-commit-config.yaml` declares hook repos, pinned revisions, and IDs; pinning revs keeps commits reproducible.
- Three hook sources cover most needs: built-in (file hygiene, secret detection), third-party packaged (Black, isort), and local-repo hooks invoking Makefile targets.
- `check-added-large-files` with `--maxkb=1000` prevents accidental commits of model artifacts or datasets.
- `detect-aws-credentials` and similar secret-scan hooks are essential to avoid pushing credentials.
- Failed hooks abort the commit; auto-fixers (Black, isort) typically rewrite files, so the user must `git add` and re-commit.
- Skipping hooks via `git commit --no-verify` is technically possible but explicitly discouraged — "no commit deserves to be force pushed no matter how 'small' your change was."
- `pre-commit run --all-files` lets you retroactively apply hooks to existing code; `pre-commit autoupdate` bumps pinned revs.

## Key Quotes
> "It is highly not recommended to skip running any of the pre-commit hooks because they are there for a reason." — on `--no-verify` discipline

## Connections
- [[MadeWithML]] — source course
- [[GokuMohandas]] — author
- [[Anyscale]] — publisher
- [[PreCommit]] — primary framework
- [[Git]] — host VCS
- [[GitHooks]] — underlying mechanism
- [[Black]] — example custom hook
- [[isort]] — example custom hook
- [[Makefile]] — referenced via local hooks
- [[CICD]] — natural successor for remote enforcement
- [[GitHubActions]] — server-side parallel
- [[SecretsScanning]] — `detect-aws-credentials` hook
- [[MLOps]] — discipline

## Contradictions
- None identified.
