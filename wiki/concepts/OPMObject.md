---
title: "OPMObject (Oz Object)"
type: concept
tags: [programming-languages, concurrency, oz, object-oriented]
sources: [vol1000-oz-programming-model]
last_updated: 2026-05-22
---

# OPMObject — Oz Object

In the [[OPM|Oz Programming Model]]: an object is a procedure `{Object Message}` applied to messages, where a message is a pair `MethodName|Argument`. *"Objects are a modular programming abstraction for concurrent data structures with state."*

## Specification

An object's functionality is given by a procedure

$$\text{Serve}: \text{State} \times \text{Message} \times \text{Self} \to \text{NewState}$$

where **Self** *"is a reference to the object invoking Serve making it possible to have a self reference within Serve and still share Serve between several objects."*

## Constructor

```oz
proc {NewObject Serve Init Object}
  local Cell in
    {NewCell Init Cell}
    proc {Object Message}
      local State NewState in
        {Exchange Cell State NewState}
        {Serve State Message Object NewState}
      end
    end
  end
end
```

Object state lives in a **private [[Cell|cell]]**; lexical scoping makes it inaccessible outside `Object`. The `Exchange` provides atomic read-modify-write — *"OPM ensures mutual exclusion for concurrent exchange tasks for the same cell."*

## Classes, inheritance, methods

> *"It is straightforward to express classes defining serve procedures in a modular fashion by means of named methods. Methods are modeled as procedures similar to serve procedures. Objects can then be obtained as instances of classes. The states of objects are modeled as finite mappings from attributes to variables, where attributes are modeled as [[Name|names]]. ... One can also provide for **inheritance** ... All this is a matter of straightforward higher-order programming. Exploiting the power of lexical scoping and names, it is straightforward to express **private attributes** and methods."*

A concrete OO system is given in *"Object-oriented concurrent constraint programming in Oz"* (Henz, Smolka & Würtz 1995, MIT Press *Principles and Practice of Constraint Programming*) and *"An Oz Primer"* (Smolka 1995).

## Object vs Agent

Under distribution:

| | Where the message is served |
|---|---|
| [[Agent]] | Site where the agent was created (stationary) |
| **OPMObject** | Site where the object is **applied** (mobile) |

> *"We can see agents as active objects. An object can easily be turned into an agent by interfacing it through a port."*

## In this wiki

The wiki's first **concurrent object-oriented programming** anchor — Smolka 1995 explicitly notes that *"no comprehensive formal model existed until now"* for concurrent OO programming, and OPM is the first to subsume it as a facet of a unified model. Distinct from modern OO models ([[Java]] / [[CPP|C++]] / [[Python|Python]] classes) which are inherently sequential or rely on external threading. Page slug uses `OPMObject` to avoid colliding with the unrelated [[ObjectDetection]] / [[ObjectFile]] concept pages from the [[DiveIntoSystems]] corpus.
