---
title: "Port (Oz)"
type: concept
tags: [programming-languages, concurrency, oz, message-passing]
sources: [vol1000-oz-programming-model]
last_updated: 2026-05-22
---

# Port

In the [[OPM|Oz Programming Model]]: a **procedure connected to a stream** — the canonical message-queue abstraction for agent-style communication. *"A port is a concurrent data structure since it allows several concurrent computations to write consistently on a single stream."* Cited in [[vol1000-oz-programming-model|Smolka 1995]] Section 9, building on Janson, Montelius & Haridi 1993 (*"Ports for objects"*).

## Stream

A **stream** is a variable $S$ incrementally constrained to a list by telling a constraint for each element:

$$S = X_1 \mid S_1, \quad S_1 = X_2 \mid S_2, \quad S_2 = X_3 \mid S_3, \ \ldots$$

Only the port's procedure writes on the stream.

## Construction

```oz
proc {NewPort Stream Port}
  local Cell in
    {NewCell Stream Cell}
    proc {Port Message}
      local Old New in
        {Exchange Cell Old New}  Old=Message|New
      end
    end
  end
end
```

The port holds the current tail of its stream in a **private [[Cell|cell]]** (lexical scoping ensures no other agent sees it). Each `{Port Message}` application atomically advances the tail by one element.

## Synchronizing ports

A variant `NewSyncPort` returns a *binary* procedure `{Port Message Continuation}` that tells `Continuation = Port` only after `Message` has been put on the stream. This enables **strict ordering** — two messages $A$ then $B$ written via

```oz
local Continuation Dummy in
  {Port A Continuation} {Continuation B Dummy}
end
```

are guaranteed to appear in that order on the stream, even with concurrent senders.

## In this wiki

First message-queue abstraction anchored in the wiki that is **derived from primitives** (logic variables + cells + first-class procedures) rather than primitive itself. Contrasts with [[MPI]] [[MessagePassing|message-passing]] (channel-style, send/recv primitives) and POSIX [[Pipe|pipes]] (kernel-mediated byte streams).
