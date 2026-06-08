---
title: "FTP (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, file-transfer]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/FTP
---

## Summary
This Rosetta Code task asks the programmer to interact with a remote server using the File Transfer Protocol (FTP). The implementation must connect to the server, change the working directory, list the directory contents, and download a file in binary transfer mode. Where supported, passive mode should be used so the client initiates the data connection (important for clients behind firewalls or NAT).

## Task Requirements
- Connect to an FTP server.
- Change to a target directory on the server.
- List the contents of that directory.
- Download a file using binary (not ASCII) transfer mode.
- Use passive mode if the client/library supports it.

## Language Coverage
36 languages implement this task, showing broad support across systems and scripting languages — many simply wrap an existing FTP library or shell client. Representative implementations include C, C++, Go, Rust, Python, Perl, Ruby, Java, Haskell, and Tcl.

## Connections
- [[FileTransferProtocol]] — the network protocol the task exercises
- [[NetworkProgramming]] — establishing and managing client/server connections
- [[PassiveMode]] — the data-connection mode requested for firewall/NAT traversal
- [[BinaryFileTransfer]] — downloading without text/line-ending translation

## Contradictions
- None — reference task page.
