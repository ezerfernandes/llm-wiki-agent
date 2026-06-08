---
title: "Chat server (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, concurrency]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Chat_server
---

## Summary
This task asks the programmer to build a minimal text-based chat server that clients can reach over a raw TCP connection using `telnet`. After connecting, a user signs on with a nickname and any message they type is broadcast to all other connected clients. The key challenge is handling multiple simultaneous connections and fanning out each message to every participant, which forces a concurrency or event-loop design rather than a simple request/response loop.

## Task Requirements
- Run a server that accepts client connections via `telnet`.
- Let each client sign on with a chosen nickname.
- Broadcast every message typed by a user to all other connected users.
- Emit notification messages when members arrive (join) and depart (disconnect).

## Language Coverage
32 languages implement this task, spanning systems languages, functional languages, and scripting languages with strong networking or actor support. Representative implementations include C, Go, Rust, Erlang, Haskell, Java, Python, Ruby, Common Lisp, and Perl.

## Connections
- [[SocketProgramming]] — built on TCP server sockets accepting telnet clients
- [[Concurrency]] — must service many connected clients at once
- [[PublishSubscribe]] — broadcasting each message to all subscribers
- [[EventLoop]] — common non-blocking design for multiplexing connections
- [[ActorModel]] — used by Erlang/Go-style implementations to isolate per-client state

## Contradictions
- None — reference task page.
