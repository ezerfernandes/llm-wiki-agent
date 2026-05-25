---
title: "Git LFS"
type: entity
tags: [tool, version-control, data-versioning, open-source]
sources: [leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
Git Large File Storage (Git LFS) is an open-source Git extension that replaces large files in a repository with text pointers, while the actual binary contents are stored on a remote LFS server. It is used to keep model weights, datasets, or media out of Git's pack files.

## In LLM Engineer's Handbook
Ch. 11 ([[leh-ch11-mlops-and-llmops]]) lists Git LFS alongside [[DVC]] as the canonical code-adjacent options for versioning datasets — useful when you want dataset history to track with Git history rather than living in a separate artifact system.

## Connections
- [[DVC]] — peer data-versioning tool.
- [[GitHub]] / [[GitLab]] — hosts that support Git LFS.
- [[Versioning]] — MLOps principle.
- [[MLOps]] — discipline.
