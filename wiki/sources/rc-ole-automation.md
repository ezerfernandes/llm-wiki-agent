---
title: "OLE automation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, inter-process-communication, windows]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/OLE_automation
---

## Summary
OLE Automation is a Windows inter-process communication mechanism built on top of the Component Object Model (COM). This task asks the programmer to build an automation server that exposes objects whose methods can be invoked by a client running in a separate process. The key challenge is that the client only holds a proxy object, and arguments and return values must be marshalled across the process boundary as COM variants, requiring conversion to and from the language's native value types.

## Task Requirements
- Implement an automation server that exposes objects with callable methods.
- Implement a client running in a separate process that obtains a proxy object for the server's objects.
- Have the client call methods on the proxy object.
- Correctly convert variant types to and from the host language's native value types in both directions.

## Language Coverage
8 languages implement this task — a small set, since OLE/COM is a Windows-specific technology with limited cross-platform relevance. Representative implementations include Python, Go, Julia, Phix, FreeBASIC, AutoHotkey, M2000 Interpreter, and Wren.

## Connections
- [[ComponentObjectModel]] — the COM substrate OLE Automation is layered on
- [[InterProcessCommunication]] — the broader problem class this task exemplifies
- [[VariantType]] — the tagged union used to marshal values across the boundary
- [[ProxyPattern]] — the client-side proxy object standing in for the remote server object
- [[Marshalling]] — serializing arguments and results between processes

## Contradictions
- None — reference task page.
