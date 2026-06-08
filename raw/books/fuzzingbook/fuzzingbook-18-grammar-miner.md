# Mining Input Grammars

So far, the grammars we have seen have been mostly specified manually – that is, you (or the person knowing the input format) had to design and write a grammar in the first place.  While the grammars we have seen so far have been rather simple, creating a grammar for complex inputs can involve quite some effort.  In this chapter, we therefore introduce techniques that _automatically mine grammars from programs_ – by executing the programs and observing how they process which parts of the input.  In conjunction with a grammar fuzzer, this allows us to
1. take a program,
2. extract its input grammar, and
3. fuzz it with high efficiency and effectiveness, using the concepts in this book.

```python
from bookutils import YouTubeVideo
YouTubeVideo("ddM1oL2LYDI")
```

**Prerequisites**

* You should have read the [chapter on grammars](Grammars.ipynb).
* The [chapter on configuration fuzzing](ConfigurationFuzzer.ipynb) introduces grammar mining for configuration options, as well as observing variables and values during execution.
* We use the tracer from the [chapter on coverage](Coverage.ipynb).
* The concept of parsing from the [chapter on parsers](Parser.ipynb) is also useful.

## Synopsis
<!-- Automatically generated. Do not edit. -->

To [use the code provided in this chapter](Importing.ipynb), write

```python
>>> from fuzzingbook.GrammarMiner import <identifier>
```

and then make use of the following features.

This chapter provides a number of classes to mine input grammars from existing programs.  The function `recover_grammar()` could be the easiest to use.  It takes a function and a set of inputs, and returns a grammar that describes its input language.

We apply `recover_grammar()` on a `url_parse()` function that takes and decomposes URLs:

```python
>>> url_parse('https://www.fuzzingbook.org/')
>>> URLS
['http://user:pass@www.google.com:80/?q=path#ref',
 'https://www.cispa.saarland:80/',
 'http://www.fuzzingbook.org/#News']
```
We extract the input grammar for `url_parse()` using `recover_grammar()`:

```python
>>> grammar = recover_grammar(url_parse, URLS, files=['urllib/parse.py'])
>>> grammar
{'<start>': ['<urlsplit@437:url>'],
 '<urlsplit@437:url>': ['<urlparse@394:scheme>:<_splitnetloc@411:url>'],
 '<urlparse@394:scheme>': ['https', 'http'],
 '<_splitnetloc@411:url>': ['//<urlparse@394:netloc><urlsplit@481:url>',
  '//<urlparse@394:netloc>/'],
 '<urlparse@394:netloc>': ['www.cispa.saarland:80',
  'user:pass@www.google.com:80',
  'www.fuzzingbook.org'],
 '<urlsplit@481:url>': ['<urlsplit@486:url>#<urlparse@394:fragment>',
  '/#<urlparse@394:fragment>'],
 '<urlsplit@486:url>': ['/?<urlparse@394:query>'],
 '<urlparse@394:query>': ['q=path'],
 '<urlparse@394:fragment>': ['News', 'ref']}
```
The names of nonterminals are a bit technical; but the grammar nicely represents the structure of the input; for instance, the different schemes (`"http"`, `"https"`) are all identified:

```python
>>> syntax_diagram(grammar)
start

```
![](PICS/GrammarMiner-synopsis-1.svg)
```
urlsplit@437:url

```
![](PICS/GrammarMiner-synopsis-2.svg)
```
urlparse@394:scheme

```
![](PICS/GrammarMiner-synopsis-3.svg)
```
_splitnetloc@411:url

```
![](PICS/GrammarMiner-synopsis-4.svg)
```
urlparse@394:netloc

```
![](PICS/GrammarMiner-synopsis-5.svg)
```
urlsplit@481:url

```
![](PICS/GrammarMiner-synopsis-6.svg)
```
urlsplit@486:url

```
![](PICS/GrammarMiner-synopsis-7.svg)
```
urlparse@394:query

```
![](PICS/GrammarMiner-synopsis-8.svg)
```
urlparse@394:fragment

```
![](PICS/GrammarMiner-synopsis-9.svg)

The grammar can be immediately used for fuzzing, producing arbitrary combinations of input elements, which are all syntactically valid.

```python
>>> from GrammarCoverageFuzzer import GrammarCoverageFuzzer
>>> fuzzer = GrammarCoverageFuzzer(grammar)
>>> [fuzzer.fuzz() for i in range(5)]
['https://www.cispa.saarland:80/',
 'http://www.fuzzingbook.org/#ref',
 'https://user:pass@www.google.com:80/?q=path#News',
 'http://user:pass@www.google.com:80/#ref',
 'https://www.fuzzingbook.org/#News']
```
Being able to automatically extract a grammar and to use this grammar for fuzzing makes for very effective test generation with a minimum of manual work.

## A Grammar Challenge

Consider the `process_inventory()` method from the [chapter on parsers](Parser.ipynb):

```python
import bookutils.setup
```

```python
from typing import List, Tuple, Callable, Any
from collections.abc import Iterable
```

```python
from Parser import process_inventory, process_vehicle, process_car, process_van, lr_graph  # minor dependency
```

It takes inputs of the following form.

```python
INVENTORY = """\
1997,van,Ford,E350
2000,car,Mercury,Cougar
1999,car,Chevy,Venture\
"""
```

```python
print(process_inventory(INVENTORY))
```

We found from the [chapter on parsers](Parser.ipynb) that coarse grammars do not work well for fuzzing when the input format includes details expressed only in code. That is, even though we have the formal specification of CSV files ([RFC 4180](https://tools.ietf.org/html/rfc4180)), the inventory system includes further rules as to what is expected at each index of the CSV file. The solution of simply recombining existing inputs, while practical, is incomplete. In particular, it relies on a formal input specification being available in the first place. However, we have no assurance that the program obeys the input specification given.

One of the ways out of this predicament is to interrogate the program under test as to what its input specification is. That is, if the program under test is written in a style such that specific methods are responsible for handling specific parts of the input, one can recover the parse tree by observing the process of parsing. Further, one can recover a reasonable approximation of the grammar by abstraction from multiple input trees.

 _We start with the assumption (1) that the program is written in such a fashion that specific methods are responsible for parsing specific fragments of the program -- This includes almost all ad hoc parsers._

The idea is as follows:

* Hook into the Python execution and observe the fragments of input string as they are produced and named in different methods.
* Stitch the input fragments together in a tree structure to retrieve the **Parse Tree**.
* Abstract common elements from multiple parse trees to produce the **Context Free Grammar** of the input.

## A Simple Grammar Miner

Say we want to obtain the input grammar for the function `process_vehicle()`. We first collect the sample inputs for this function.

```python
VEHICLES = INVENTORY.split('\n')
```

The set of methods responsible for processing inventory are the following.

```python
INVENTORY_METHODS = {
    'process_inventory',
    'process_vehicle',
    'process_van',
    'process_car'}
```

We have seen from the chapter on [configuration fuzzing](ConfigurationFuzzer.ipynb) that one can hook into the Python runtime to observe the arguments to a function and any local variables created. We have also seen that one can obtain the context of execution by inspecting the `frame` argument. Here is a simple tracer that can return the local variables and other contextual information in a traced function. We reuse the `Coverage` tracing class.

### Tracer

```python
from Coverage import Coverage
```

```python
import inspect
```

```python
class Tracer(Coverage):
    def traceit(self, frame, event, arg):
        method_name = inspect.getframeinfo(frame).function
        if method_name not in INVENTORY_METHODS:
            return
        file_name = inspect.getframeinfo(frame).filename

        param_names = inspect.getargvalues(frame).args
        lineno = inspect.getframeinfo(frame).lineno
        local_vars = inspect.getargvalues(frame).locals
        print(event, file_name, lineno, method_name, param_names, local_vars)
        return self.traceit
```

We run the code under trace context.

```python
with Tracer() as tracer:
    process_vehicle(VEHICLES[0])
```

The main thing that we want out of tracing is a list of assignments of input fragments to different variables. We can use the tracing facility `settrace()` to get that as we showed above.

However, the `settrace()` function hooks into the Python debugging facility. When it is in operation, no debugger can hook into the program. That is, if there is a problem with our grammar miner, we will not be able to attach a debugger to it to understand what is happening. This is not ideal. Hence, we limit the tracer to the simplest implementation possible, and implement the core of grammar mining in later stages.

The `traceit()` function relies on information from the `frame` variable which exposes Python internals. We define a `context` class that encapsulates the information that we need from the `frame`.

### Context

The `Context` class provides easy access to the information such as the current module, and parameter names.

```python
class Context:
    def __init__(self, frame, track_caller=True):
        self.method = inspect.getframeinfo(frame).function
        self.parameter_names = inspect.getargvalues(frame).args
        self.file_name = inspect.getframeinfo(frame).filename
        self.line_no = inspect.getframeinfo(frame).lineno

    def _t(self):
        return (self.file_name, self.line_no, self.method,
                ','.join(self.parameter_names))

    def __repr__(self):
        return "%s:%d:%s(%s)" % self._t()
```

Here we add a few convenience methods that operate on the `frame` to `Context`.

```python
class Context(Context):
    def extract_vars(self, frame):
        return inspect.getargvalues(frame).locals

    def parameters(self, all_vars):
        return {k: v for k, v in all_vars.items() if k in self.parameter_names}

    def qualified(self, all_vars):
        return {"%s:%s" % (self.method, k): v for k, v in all_vars.items()}
```

We hook printing the context to our `traceit()` to see it in action. First we define a `log_event()` for displaying events.

```python
def log_event(event, var):
    print({'call': '->', 'return': '<-'}.get(event, '  '), var)
```

And use the `log_event()` in the `traceit()` function.

```python
class Tracer(Tracer):
    def traceit(self, frame, event, arg):
        log_event(event, Context(frame))
        return self.traceit
```

Running `process_vehicle()` under trace prints the contexts encountered.

```python
with Tracer() as tracer:
    process_vehicle(VEHICLES[0])
```

The trace produced by executing any function can get overwhelmingly large. Hence, we need to restrict our attention to specific modules. Further, we also restrict our attention exclusively to `str` variables since these variables are more likely to contain input fragments. (We will show how to deal with complex objects later in exercises.)

The `Context` class we developed earlier is used to decide which modules to monitor, and which variables to trace.

We store the current *input string* so that it can be used to determine if any particular string fragments came from the current input string. Any optional arguments are processed separately.

```python
class Tracer(Tracer):
    def __init__(self, my_input, **kwargs):
        self.options(kwargs)
        self.my_input, self.trace = my_input, []
```

We use an optional argument `files` to indicate the specific source files we are interested in, and `methods` to indicate which specific methods are of interest. Further, we also use `log` to specify whether verbose logging should be enabled during trace. We use the `log_event()` method we defined earlier for logging.

The options processing is as below.

```python
class Tracer(Tracer):
    def options(self, kwargs):
        self.files = kwargs.get('files', [])
        self.methods = kwargs.get('methods', [])
        self.log = log_event if kwargs.get('log') else lambda _evt, _var: None
```

The `files` and `methods` are checked to determine, if a particular event should be traced or not

```python
class Tracer(Tracer):
    def tracing_context(self, cxt, event, arg):
        fres = not self.files or any(
            cxt.file_name.endswith(f) for f in self.files)
        mres = not self.methods or any(cxt.method == m for m in self.methods)
        return fres and mres
```

Similar to the context of events, we also want to restrict our attention to specific variables. For now, we want to focus only on strings. (See the Exercises at the end of the chapter on how to extend it to other kinds of objects).

```python
class Tracer(Tracer):
    def tracing_var(self, k, v):
        return isinstance(v, str)
```

We modify the `traceit()` to call an `on_event()` function with the context information only on the specific events we are interested in.

```python
class Tracer(Tracer):
    def on_event(self, event, arg, cxt, my_vars):
        self.trace.append((event, arg, cxt, my_vars))

    def create_context(self, frame):
        return Context(frame)

    def traceit(self, frame, event, arg):
        cxt = self.create_context(frame)
        if not self.tracing_context(cxt, event, arg):
            return self.traceit
        self.log(event, cxt)

        my_vars = {
            k: v
            for k, v in cxt.extract_vars(frame).items()
            if self.tracing_var(k, v)
        }
        self.on_event(event, arg, cxt, my_vars)
        return self.traceit
```

The `Tracer` class can now focus on specific kinds of events on specific files. Further, it provides a first level filter for variables that we find interesting. For example, we want to focus specifically on variables from `process_*` methods that contain input fragments. Here is how our updated `Tracer` can be used.

```python
with Tracer(VEHICLES[0], methods=INVENTORY_METHODS, log=True) as tracer:
    process_vehicle(VEHICLES[0])
```

The execution produced the following trace.

```python
for t in tracer.trace:
    print(t[0], t[2].method, dict(t[3]))
```

Since we are saving the input already in `Tracer`, it is redundant to specify it separately again as an argument.

```python
with Tracer(VEHICLES[0], methods=INVENTORY_METHODS, log=True) as tracer:
    process_vehicle(tracer.my_input)
```

### DefineTracker

We define a `DefineTracker` class that processes the trace from the `Tracer`. The idea is to store different variable definitions which are input fragments.

The tracker identifies string fragments that are part of the input string, and stores them in a dictionary `my_assignments`. It saves the trace, and the corresponding input for processing. Finally, it calls `process()` to process the `trace` it was given. We will start with a simple tracker that relies on certain assumptions, and later see how these assumptions can be relaxed.

```python
class DefineTracker:
    def __init__(self, my_input, trace, **kwargs):
        self.options(kwargs)
        self.my_input = my_input
        self.trace = trace
        self.my_assignments = {}
        self.process()
```

One of the problems of using substring search is that short string sequences tend to be included in other string sequences even though they may not have come from the original string. That is, say the input fragment is `v`, it could have equally come from either `van` or `chevy`. We rely on being able to predict the exact place in the input where a given fragment occurred. Hence, we define a constant `FRAGMENT_LEN` such that we ignore strings up to that length. We also incorporate a logging facility as before.

```python
FRAGMENT_LEN = 3
```

```python
class DefineTracker(DefineTracker):
    def options(self, kwargs):
        self.log = log_event if kwargs.get('log') else lambda _evt, _var: None
        self.fragment_len = kwargs.get('fragment_len', FRAGMENT_LEN)
```

Our tracer simply records the variable values as they occur. We next need to check if the variables contain values from the **input string**. Common ways to do this is to rely on symbolic execution or at least dynamic tainting, which are powerful, but also complex. However, one can obtain a reasonable approximation by simply relying on substring search. That is, we consider any value produced that is a substring of the original input string to have come from the original input.

We define an `is_input_fragment()` method that relies on string inclusion to detect if the string came from the input.

```python
class DefineTracker(DefineTracker):
    def is_input_fragment(self, var, value):
        return len(value) >= self.fragment_len and value in self.my_input
```

We can use `is_input_fragment()` to select only a subset of variables defined, as implemented below in `fragments()`.

```python
class DefineTracker(DefineTracker):
    def fragments(self, variables):
        return {k: v for k, v in variables.items(
        ) if self.is_input_fragment(k, v)}
```

The tracker processes each event, and at each event, it updates the dictionary `my_assignments` with the current local variables that contain strings that are part of the input. Note that there is a choice here with respect to what happens during reassignment. We can either discard all the reassignments, or keep only the last assignment. Here, we choose the latter. If you want the former behavior, check whether the value exists in `my_assignments` before storing a fragment.

```python
class DefineTracker(DefineTracker):
    def track_event(self, event, arg, cxt, my_vars):
        self.log(event, (cxt.method, my_vars))
        self.my_assignments.update(self.fragments(my_vars))

    def process(self):
        for event, arg, cxt, my_vars in self.trace:
            self.track_event(event, arg, cxt, my_vars)
```

Using the tracker, we can obtain the input fragments. For example, say we are only interested in strings that are at least `5` characters long.

```python
tracker = DefineTracker(tracer.my_input, tracer.trace, fragment_len=5)
for k, v in tracker.my_assignments.items():
    print(k, '=', repr(v))
```

Or strings that are `2` characters long (the default).

```python
tracker = DefineTracker(tracer.my_input, tracer.trace)
for k, v in tracker.my_assignments.items():
    print(k, '=', repr(v))
```

```python
class DefineTracker(DefineTracker):
    def assignments(self):
        return self.my_assignments.items()
```

### Assembling a Derivation Tree

```python
from Grammars import START_SYMBOL, syntax_diagram, \
    is_nonterminal, Grammar
```

```python
from GrammarFuzzer import GrammarFuzzer, display_tree, \
    DerivationTree
```

The input fragments from the `DefineTracker` only tell half the story. The fragments may be created at different stages of parsing. Hence, we need to assemble the fragments to a  derivation tree of the input. The basic idea is as follows:

Our input from the previous step was:

```python
"1997,van,Ford,E350"
```

We start a derivation tree, and associate it with the start symbol in the grammar.

```python
derivation_tree: DerivationTree = (START_SYMBOL, [("1997,van,Ford,E350", [])])
```

```python
display_tree(derivation_tree)
```

The next input was:
```python
vehicle = "1997,van,Ford,E350"
```
Since vehicle covers the `<start>` node's value completely, we replace the value with the vehicle node.

```python
derivation_tree: DerivationTree = (START_SYMBOL,
                                   [('<vehicle>', [("1997,van,Ford,E350", [])],
                                                   [])])
```

```python
display_tree(derivation_tree)
```

The next input was:
```python
year = '1997'
```
Traversing the derivation tree from `<start>`, we see that it replaces a portion of the `<vehicle>` node's value. Hence we split the `<vehicle>` node's value to two children, where one corresponds to the value `"1997"` and the other to `",van,Ford,E350"`, and replace the first one with the node `<year>`.

```python
derivation_tree: DerivationTree = (START_SYMBOL,
                                   [('<vehicle>', [('<year>', [('1997', [])]),
                                                   (",van,Ford,E350", [])], [])])
```

```python
display_tree(derivation_tree)
```

We perform similar operations for
```python
company = 'Ford'
```

```python
derivation_tree: DerivationTree = (START_SYMBOL,
                                   [('<vehicle>', [('<year>', [('1997', [])]),
                                                   (",van,", []),
                                                   ('<company>', [('Ford', [])]),
                                                   (",E350", [])], [])])
```

```python
display_tree(derivation_tree)
```

Similarly for
```python
kind = 'van'
```
and
```python
model = 'E350'
```

```python
derivation_tree: DerivationTree = (START_SYMBOL,
                                   [('<vehicle>', [('<year>', [('1997', [])]),
                                                   (",", []),
                                                   ("<kind>", [('van', [])]),
                                                   (",", []),
                                                   ('<company>', [('Ford', [])]),
                                                   (",", []),
                                                   ("<model>", [('E350', [])])
                                                   ], [])])
```

```python
display_tree(derivation_tree)
```

We now develop the complete algorithm with the above described steps.
The derivation tree `TreeMiner` is initialized with the input string, and the variable assignments, and it converts the assignments to the corresponding derivation tree.

```python
class TreeMiner:
    def __init__(self, my_input, my_assignments, **kwargs):
        self.options(kwargs)
        self.my_input = my_input
        self.my_assignments = my_assignments
        self.tree = self.get_derivation_tree()

    def options(self, kwargs):
        self.log = log_call if kwargs.get('log') else lambda _i, _v: None

    def get_derivation_tree(self):
        return (START_SYMBOL, [])
```

The `log_call()` is as follows.

```python
def log_call(indent, var):
    print('\t' * indent, var)
```

The basic idea is as follows:
* **For now, we assume that the value assigned to a variable is stable. That is, it is never reassigned. In particular, there are no recursive calls, or multiple calls to the same function from different parts.** (We will show how to overcome this limitation later).
* For each pair _var_, _value_ found in `my_assignments`:
    1. We search for occurrences of _value_ `val` in the derivation tree recursively.
    2. If an occurrence was found as a value `V1` of a node `P1`, we partition the value of the node `P1` into three parts, with the central part matching the _value_ `val`, and the first and last part, the corresponding prefix and suffix in `V1`.
    3. Reconstitute the node `P1` with three children, where prefix and suffix mentioned earlier are string values, and the matching value `val` is replaced by a node `var` with a single value `val`.

First, we define a wrapper to generate a nonterminal from a variable name.

```python
def to_nonterminal(var):
    return "<" + var.lower() + ">"
```

The `string_part_of_value()` method checks whether the given `part` value was part of the whole.

```python
class TreeMiner(TreeMiner):
    def string_part_of_value(self, part, value):
        return (part in value)
```

The `partition_by_part()` splits the `value` by the given part if it matches, and returns a list containing the first part, the part that was replaced, and the last part. This is a format that can be used as a part of the list of children.

```python
class TreeMiner(TreeMiner):
    def partition(self, part, value):
        return value.partition(part)
```

```python
class TreeMiner(TreeMiner):
    def partition_by_part(self, pair, value):
        k, part = pair
        prefix_k_suffix = [
                    (k, [[part, []]]) if i == 1 else (e, [])
                    for i, e in enumerate(self.partition(part, value))
                    if e]
        return prefix_k_suffix
```

The `insert_into_tree()` method accepts a given tree `tree` and a `(k,v)` pair.  It recursively checks whether the given pair can be applied. If the pair can be applied, it applies the pair and returns `True`.

```python
class TreeMiner(TreeMiner):
    def insert_into_tree(self, my_tree, pair):
        var, values = my_tree
        k, v = pair
        self.log(1, "- Node: %s\t\t? (%s:%s)" % (var, k, repr(v)))
        applied = False
        for i, value_ in enumerate(values):
            value, arr = value_
            self.log(2, "-> [%d] %s" % (i, repr(value)))
            if is_nonterminal(value):
                applied = self.insert_into_tree(value_, pair)
                if applied:
                    break
            elif self.string_part_of_value(v, value):
                prefix_k_suffix = self.partition_by_part(pair, value)
                del values[i]
                for j, rep in enumerate(prefix_k_suffix):
                    values.insert(j + i, rep)
                applied = True

                self.log(2, " > %s" % (repr([i[0] for i in prefix_k_suffix])))
                break
            else:
                continue
        return applied
```

Here is how `insert_into_tree()` is used.

```python
tree: DerivationTree = (START_SYMBOL, [("1997,van,Ford,E350", [])])
m = TreeMiner('', {}, log=True)
```

First, we have our input string as the only node.

```python
display_tree(tree)
```

Inserting the `<vehicle>` node.

```python
v = m.insert_into_tree(tree, ('<vehicle>', "1997,van,Ford,E350"))
```

```python
display_tree(tree)
```

Inserting `<model>` node.

```python
v = m.insert_into_tree(tree, ('<model>', 'E350'))
```

```python
display_tree((tree))
```

Inserting `<company>`.

```python
v = m.insert_into_tree(tree, ('<company>', 'Ford'))
```

```python
display_tree(tree)
```

Inserting `<kind>`.

```python
v = m.insert_into_tree(tree, ('<kind>', 'van'))
```

```python
display_tree(tree)
```

Inserting `<year>`.

```python
v = m.insert_into_tree(tree, ('<year>', '1997'))
```

```python
display_tree(tree)
```

To make life simple, we define a wrapper function `nt_var()` that will convert a token to its corresponding nonterminal symbol.

```python
class TreeMiner(TreeMiner):
    def nt_var(self, var):
        return var if is_nonterminal(var) else to_nonterminal(var)
```

Now, we need to apply a new definition to an entire grammar.

```python
class TreeMiner(TreeMiner):
    def apply_new_definition(self, tree, var, value):
        nt_var = self.nt_var(var)
        return self.insert_into_tree(tree, (nt_var, value))
```

This algorithm is implemented as `get_derivation_tree()`.

```python
class TreeMiner(TreeMiner):
    def get_derivation_tree(self):
        tree = (START_SYMBOL, [(self.my_input, [])])

        for var, value in self.my_assignments:
            self.log(0, "%s=%s" % (var, repr(value)))
            self.apply_new_definition(tree, var, value)
        return tree
```

The `TreeMiner` is used as follows:

```python
with Tracer(VEHICLES[0]) as tracer:
    process_vehicle(tracer.my_input)
assignments = DefineTracker(tracer.my_input, tracer.trace).assignments()
dt = TreeMiner(tracer.my_input, assignments, log=True)
dt.tree
```

The obtained derivation tree is as below.

```python
display_tree(TreeMiner(tracer.my_input, assignments).tree)
```

Combining all the pieces:

```python
trees = []
for vehicle in VEHICLES:
    print(vehicle)
    with Tracer(vehicle) as tracer:
        process_vehicle(tracer.my_input)
    assignments = DefineTracker(tracer.my_input, tracer.trace).assignments()
    trees.append((tracer.my_input, assignments))
    for var, val in assignments:
        print(var + " = " + repr(val))
    print()
```

The corresponding derivation trees are below.

```python
csv_dt = []
for inputstr, assignments in trees:
    print(inputstr)
    dt = TreeMiner(inputstr, assignments)
    csv_dt.append(dt)
    display_tree(dt.tree)
```

### Recovering Grammars from Derivation Trees

We define a class `Miner` that can combine multiple derivation trees to produce the grammar. The initial grammar is empty.

```python
class GrammarMiner:
    def __init__(self):
        self.grammar = {}
```

The `tree_to_grammar()` method converts our derivation tree to a grammar by picking one node at a time, and adding it to the grammar. The node name becomes the key, and any list of children it has becomes another alternative for that key.

```python
class GrammarMiner(GrammarMiner):
    def tree_to_grammar(self, tree):
        node, children = tree
        one_alt = [ck for ck, gc in children]
        hsh = {node: [one_alt] if one_alt else []}
        for child in children:
            if not is_nonterminal(child[0]):
                continue
            chsh = self.tree_to_grammar(child)
            for k in chsh:
                if k not in hsh:
                    hsh[k] = chsh[k]
                else:
                    hsh[k].extend(chsh[k])
        return hsh
```

```python
gm = GrammarMiner()
gm.tree_to_grammar(csv_dt[0].tree)
```

The grammar being generated here is `canonical`. We define a function `readable()` that takes in a canonical grammar and returns it in a readable form.

```python
def readable(grammar):
    def readable_rule(rule):
        return ''.join(rule)

    return {k: list(set(readable_rule(a) for a in grammar[k]))
            for k in grammar}
```

```python
syntax_diagram(readable(gm.tree_to_grammar(csv_dt[0].tree)))
```

The `add_tree()` method gets a combined list of non-terminals from current grammar, and the tree to be added to the grammar, and updates the definitions of each non-terminal.

```python
import itertools
```

```python
class GrammarMiner(GrammarMiner):
    def add_tree(self, t):
        t_grammar = self.tree_to_grammar(t.tree)
        self.grammar = {
            key: self.grammar.get(key, []) + t_grammar.get(key, [])
            for key in itertools.chain(self.grammar.keys(), t_grammar.keys())
        }
```

The `add_tree()` is used as follows:

```python
inventory_grammar_miner = GrammarMiner()
for dt in csv_dt:
    inventory_grammar_miner.add_tree(dt)
```

```python
syntax_diagram(readable(inventory_grammar_miner.grammar))
```

Given execution traces from various inputs, one can define `update_grammar()` to obtain the complete grammar from the traces.

```python
class GrammarMiner(GrammarMiner):
    def update_grammar(self, inputstr, trace):
        at = self.create_tracker(inputstr, trace)
        dt = self.create_tree_miner(inputstr, at.assignments())
        self.add_tree(dt)
        return self.grammar

    def create_tracker(self, *args):
        return DefineTracker(*args)

    def create_tree_miner(self, *args):
        return TreeMiner(*args)
```

The complete grammar recovery is implemented in `recover_grammar()`.

```python
def recover_grammar(fn: Callable, inputs: Iterable[str],
                    **kwargs: Any) -> Grammar:
    miner = GrammarMiner()

    for inputstr in inputs:
        with Tracer(inputstr, **kwargs) as tracer:
            fn(tracer.my_input)
        miner.update_grammar(tracer.my_input, tracer.trace)

    return readable(miner.grammar)
```

Note that the grammar could have been retrieved directly from the tracker, without the intermediate derivation tree stage. However, going through the derivation tree allows one to inspect the inputs being fragmented and verify that it happens correctly.

#### Example 1. Recovering the Inventory Grammar

```python
inventory_grammar = recover_grammar(process_vehicle, VEHICLES)
```

```python
inventory_grammar
```

#### Example 2. Recovering URL Grammar

Our algorithm is robust enough to recover grammar from real world programs. For example, the `urlparse` function in the Python `urlib` module accepts the following sample URLs.

```python
URLS = [
    'http://user:pass@www.google.com:80/?q=path#ref',
    'https://www.cispa.saarland:80/',
    'http://www.fuzzingbook.org/#News',
]
```

The urllib caches its intermediate results for faster access. Hence, we need to disable it using `clear_cache()` after every invocation.

```python
from urllib.parse import urlparse, clear_cache  # type: ignore
```

We use the sample URLs to recover grammar as follows. The `urlparse` function tends to cache its previous parsing results. Hence, we define a new method `url_parse()` that clears the cache before each call.

```python
def url_parse(url):
    clear_cache()
    urlparse(url)
```

```python
trees = []
for url in URLS:
    print(url)
    with Tracer(url) as tracer:
        url_parse(tracer.my_input)
    assignments = DefineTracker(tracer.my_input, tracer.trace).assignments()
    trees.append((tracer.my_input, assignments))
    for var, val in assignments:
        print(var + " = " + repr(val))
    print()

url_dt = []
for inputstr, assignments in trees:
    print(inputstr)
    dt = TreeMiner(inputstr, assignments)
    url_dt.append(dt)
    display_tree(dt.tree)
```

Let us use `url_parse()` to recover the grammar:

```python
url_grammar = recover_grammar(url_parse, URLS, files=['urllib/parse.py'])
```

```python
syntax_diagram(url_grammar)
```

The recovered grammar describes the URL format reasonably well.

### Fuzzing

We can now use our recovered grammar for fuzzing as follows.

First, the inventory grammar.

```python
f = GrammarFuzzer(inventory_grammar)
for _ in range(10):
    print(f.fuzz())
```

Next, the URL grammar.

```python
f = GrammarFuzzer(url_grammar)
for _ in range(10):
    print(f.fuzz())
```

What this means is that we can now take a program and a few samples, extract its grammar, and then use this very grammar for fuzzing.  Now that's quite an opportunity!

### Problems with the Simple Miner

One of the problems with our simple grammar miner is the assumption that the values assigned to variables are stable. Unfortunately, that may not hold true in all cases. For example, here is a URL with a slightly different format.

```python
URLS_X = URLS + ['ftp://freebsd.org/releases/5.8']
```

The grammar generated from this set of samples is not as nice as what we got earlier

```python
url_grammar = recover_grammar(url_parse, URLS_X, files=['urllib/parse.py'])
```

```python
syntax_diagram(url_grammar)
```

Clearly, something has gone wrong.

To investigate why the `url` definition has gone wrong, let us inspect the trace for the URL.

```python
clear_cache()
with Tracer(URLS_X[0]) as tracer:
    urlparse(tracer.my_input)
for i, t in enumerate(tracer.trace):
    if t[0] in {'call', 'line'} and 'parse.py' in str(t[2]) and t[3]:
        print(i, t[2]._t()[1], t[3:])
```

Notice how the value of `url` changes as the parsing progresses? This violates our assumption that the value assigned to a variable is stable. We next look at how this limitation can be removed.

## Grammar Miner with Reassignment

One way to uniquely identify different variables is to annotate them with *line numbers* both when they are defined and also when their value changes. Consider the code fragment below

### Tracking variable assignment locations

```python
def C(cp_1):
    c_2 = cp_1 + '@2'
    c_3 = c_2 + '@3'
    return c_3
```

```python
def B(bp_7):
    b_8 = bp_7 + '@8'
    return C(b_8)
```

```python
def A(ap_12):
    a_13 = ap_12 + '@13'
    a_14 = B(a_13) + '@14'
    a_14 = a_14 + '@15'
    a_13 = a_14 + '@16'
    a_14 = B(a_13) + '@17'
    a_14 = B(a_13) + '@18'
```

Notice how all variables are either named corresponding to either where they are defined, or the value is annotated to indicate that it was changed.

Let us run this under the trace.

```python
with Tracer('____') as tracer:
    A(tracer.my_input)

for t in tracer.trace:
    print(t[0], "%d:%s" % (t[2].line_no, t[2].method), t[3])
```

Each variable was referenced first as follows:

* `cp_1` -- *call* `1:C`
* `c_2` -- *line* `3:C` (but the previous event was *line* `2:C`)
* `c_3` -- *line* `4:C` (but the previous event was *line* `3:C`)
* `bp_7` -- *call* `7:B`
* `b_8` -- *line* `9:B` (but the previous event was *line* `8:B`)
* `ap_12` -- *call* `12:A`
* `a_13` -- *line* `14:A` (but the previous event was *line* `13:A`)
* `a_14` -- *line* `15:A` (the previous event was *return* `9:B`. However, the previous event in `A()` was *line* `14:A`)
* reassign `a_14` at *15* -- *line* `16:A` (the previous event was *line* `15:A`)
* reassign `a_13` at *16* -- *line* `17:A` (the previous event was *line* `16:A`)
* reassign `a_14` at *17* -- *return* `17:A` (the previous event in `A()` was *line* `17:A`)
* reassign `a_14` at *18* -- *return* `18:A` (the previous event in `A()` was *line* `18:A`)

So, our observations are that, if it is a call, the current location is the right one for any new variables being defined. On the other hand, if the variable being referenced for the first time (or reassigned a new value), then the  right location to consider is the previous location *in the same method invocation*. Next, let us see how we can incorporate this information into variable naming.

Next, we need a way to track the individual method calls as they are being made. For this we define the class `CallStack`. Each method invocation gets a separate identifier, and when the method call is over, the identifier is reset.

### CallStack

```python
class CallStack:
    def __init__(self, **kwargs):
        self.options(kwargs)
        self.method_id = (START_SYMBOL, 0)
        self.method_register = 0
        self.mstack = [self.method_id]

    def enter(self, method):
        self.method_register += 1
        self.method_id = (method, self.method_register)
        self.log('call', "%s%s" % (self.indent(), str(self)))
        self.mstack.append(self.method_id)

    def leave(self):
        self.mstack.pop()
        self.log('return', "%s%s" % (self.indent(), str(self)))
        self.method_id = self.mstack[-1]
```

A few extra functions to make life simpler.

```python
class CallStack(CallStack):
    def options(self, kwargs):
        self.log = log_event if kwargs.get('log') else lambda _evt, _var: None

    def indent(self):
        return len(self.mstack) * "\t"

    def at(self, n):
        return self.mstack[n]

    def __len__(self):
        return len(mstack) - 1

    def __str__(self):
        return "%s:%d" % self.method_id

    def __repr__(self):
        return repr(self.method_id)
```

We also define a convenience method to display a given stack.

```python
def display_stack(istack):
    def stack_to_tree(stack):
        current, *rest = stack
        if not rest:
            return (repr(current), [])
        return (repr(current), [stack_to_tree(rest)])
    display_tree(stack_to_tree(istack.mstack), graph_attr=lr_graph)
```

Here is how we can use the `CallStack`.

```python
cs = CallStack()
display_stack(cs)
cs
```

```python
cs.enter('hello')
display_stack(cs)
cs
```

```python
cs.enter('world')
display_stack(cs)
cs
```

```python
cs.leave()
display_stack(cs)
cs
```

```python
cs.enter('world')
display_stack(cs)
cs
```

```python
cs.leave()
display_stack(cs)
cs
```

In order to account for variable reassignments, we need to have a more intelligent data structure than a dictionary for storing variables. We first define a simple interface `Vars`. It acts as a container for variables, and is instantiated at `my_assignments`.

### Vars

The `Vars` stores references to variables as they occur during parsing in its internal dictionary `defs`. We initialize the dictionary with the original string.

```python
class Vars:
    def __init__(self, original):
        self.defs = {}
        self.my_input = original
```

The dictionary needs two methods: `update()` that takes a set of key-value pairs to update itself, and `_set_kv()` that updates a particular key-value pair.

```python
class Vars(Vars):
    def _set_kv(self, k, v):
        self.defs[k] = v

    def __setitem__(self, k, v):
        self._set_kv(k, v)

    def update(self, v):
        for k, v in v.items():
            self._set_kv(k, v)
```

The `Vars` is a proxy for the internal dictionary. For example, here is how one can use it.

```python
v = Vars('')
v.defs
```

```python
v['x'] = 'X'
v.defs
```

```python
v.update({'x': 'x', 'y': 'y'})
v.defs
```

### AssignmentVars

We now extend the simple `Vars` to account for variable reassignments. For this, we define `AssignmentVars`.

The idea for detecting reassignments and renaming variables is as follows: We keep track of the previous reassignments to particular variables using `accessed_seq_var`. It contains the last rename of any particular variable as its corresponding value. The `new_vars` contains a list of all new variables that were added on this iteration.

```python
class AssignmentVars(Vars):
    def __init__(self, original):
        super().__init__(original)
        self.accessed_seq_var = {}
        self.var_def_lines = {}
        self.current_event = None
        self.new_vars = set()
        self.method_init()
```

The `method_init()` method takes care of keeping track of method invocations using records saved in the `call_stack`. `event_locations` is for keeping track of the locations accessed *within this method*. This is used for line number tracking of variable definitions.

```python
class AssignmentVars(AssignmentVars):
    def method_init(self):
        self.call_stack = CallStack()
        self.event_locations = {self.call_stack.method_id: []}
```

The `update()` is now modified to track the changed line numbers if any, using `var_location_register()`. We reinitialize the `new_vars` after use for the next event.

```python
class AssignmentVars(AssignmentVars):
    def update(self, v):
        for k, v in v.items():
            self._set_kv(k, v)
        self.var_location_register(self.new_vars)
        self.new_vars = set()
```

The variable name now incorporates an index of how many reassignments it has gone through, effectively making each reassignment a unique variable.

```python
class AssignmentVars(AssignmentVars):
    def var_name(self, var):
        return (var, self.accessed_seq_var[var])
```

While storing variables, we need to first check whether it was previously known. If it is not, we need to initialize the rename count. This is accomplished by `var_access`.

```python
class AssignmentVars(AssignmentVars):
    def var_access(self, var):
        if var not in self.accessed_seq_var:
            self.accessed_seq_var[var] = 0
        return self.var_name(var)
```

During a variable reassignment, we update the `accessed_seq_var` to reflect the new count.

```python
class AssignmentVars(AssignmentVars):
    def var_assign(self, var):
        self.accessed_seq_var[var] += 1
        self.new_vars.add(self.var_name(var))
        return self.var_name(var)
```

These methods can be used as follows

```python
sav = AssignmentVars('')
sav.defs
```

```python
sav.var_access('v1')
```

```python
sav.var_assign('v1')
```

Assigning to it again increments the counter.

```python
sav.var_assign('v1')
```

The core of the logic is in `_set_kv()`. When a variable is being assigned, we get the sequenced variable name `s_var`. If the sequenced variable name was previously unknown in `defs`, then we have no further concerns. We add the sequenced variable to `defs`.

If the variable is previously known, then it is an indication of a possible reassignment. In this case, we look at the value the variable is holding. We check if the value changed. If it has not, then it is not.

If the value has changed, it is a reassignment. We first increment the variable usage sequence using `var_assign`, retrieve the new name, update the new name in `defs`.

```python
class AssignmentVars(AssignmentVars):
    def _set_kv(self, var, val):
        s_var = self.var_access(var)
        if s_var in self.defs and self.defs[s_var] == val:
            return
        self.defs[self.var_assign(var)] = val
```

Here is how it can be used. Assigning a variable the first time initializes its counter.

```python
sav = AssignmentVars('')
sav['x'] = 'X'
sav.defs
```

If the variable is assigned again with the same value, it is probably not a reassignment.

```python
sav['x'] = 'X'
sav.defs
```

However, if the value changed, it is a reassignment.

```python
sav['x'] = 'Y'
sav.defs
```

There is a subtlety here. It is possible for a child method to be called from the middle of a parent method, and for both to use the same variable name with different values. In this case, when the child returns, parent will have the old variable with old value in context. With our implementation, we consider this as a reassignment. However, this is OK because adding a new reassignment is harmless, but missing one is not. Further, we will discuss later how this can be avoided.

We also define bookkeeping codes for `register_event()` `method_enter()` and `method_exit()` which are the methods responsible for keeping track of the method stack. The basic idea is that, each `method_enter()` represents a new method invocation. Hence, it merits a new method id, which is generated from the `method_register`, and saved in the `method_id`. Since this is a new method, the method stack is extended by one element with this id. In the case of `method_exit()`, we pop the method stack, and reset the current `method_id` to what was below the current one.

```python
class AssignmentVars(AssignmentVars):
    def method_enter(self, cxt, my_vars):
        self.current_event = 'call'
        self.call_stack.enter(cxt.method)
        self.event_locations[self.call_stack.method_id] = []
        self.register_event(cxt)
        self.update(my_vars)

    def method_exit(self, cxt, my_vars):
        self.current_event = 'return'
        self.register_event(cxt)
        self.update(my_vars)
        self.call_stack.leave()

    def method_statement(self, cxt, my_vars):
        self.current_event = 'line'
        self.register_event(cxt)
        self.update(my_vars)
```

For each of the method events, we also register the event using `register_event()` which keeps track of the line numbers that were referenced in *this* method.

```python
class AssignmentVars(AssignmentVars):
    def register_event(self, cxt):
        self.event_locations[self.call_stack.method_id].append(cxt.line_no)
```

The `var_location_register()` keeps the locations of newly added variables. The definition location of variables in a `call` is the *current*  location. However, for a `line`, it would be the previous event in the current method.

```python
class AssignmentVars(AssignmentVars):
    def var_location_register(self, my_vars):
        def loc(mid):
            if self.current_event == 'call':
                return self.event_locations[mid][-1]
            elif self.current_event == 'line':
                return self.event_locations[mid][-2]
            elif self.current_event == 'return':
                return self.event_locations[mid][-2]
            else:
                assert False

        my_loc = loc(self.call_stack.method_id)
        for var in my_vars:
            self.var_def_lines[var] = my_loc
```

We define `defined_vars()` which returns the names of variables annotated with the line numbers as below.

```python
class AssignmentVars(AssignmentVars):
    def defined_vars(self, formatted=True):
        def fmt(k):
            v = (k[0], self.var_def_lines[k])
            return "%s@%s" % v if formatted else v

        return [(fmt(k), v) for k, v in self.defs.items()]
```

Similar to `defined_vars()` we define `seq_vars()` which annotates different variables with the number of times they were used.

```python
class AssignmentVars(AssignmentVars):
    def seq_vars(self, formatted=True):
        def fmt(k):
            v = (k[0], self.var_def_lines[k], k[1])
            return "%s@%s:%s" % v if formatted else v

        return {fmt(k): v for k, v in self.defs.items()}
```

### AssignmentTracker

The `AssignmentTracker` keeps the assignment definitions using the `AssignmentVars` we defined previously.

```python
class AssignmentTracker(DefineTracker):
    def __init__(self, my_input, trace, **kwargs):
        self.options(kwargs)
        self.my_input = my_input

        self.my_assignments = self.create_assignments(my_input)

        self.trace = trace
        self.process()

    def create_assignments(self, *args):
        return AssignmentVars(*args)
```

To fine-tune the process, we define an optional parameter called `track_return`. During tracing a method return, Python produces a virtual variable that contains the result of the returned value. If the `track_return` is set, we capture this value as a variable.

* `track_return` -- if true, add a *virtual variable* to the Vars representing the return value

```python
class AssignmentTracker(AssignmentTracker):
    def options(self, kwargs):
        self.track_return = kwargs.get('track_return', False)
        super().options(kwargs)
```

There can be different kinds of events during a trace, which includes `call` when a function is entered, `return` when the function returns, `exception` when an exception is thrown and `line` when a statement is executed.

The previous `Tracker` was too simplistic in that it did not distinguish between the different events. We rectify that and define `on_call()`, `on_return()`, and `on_line()` respectively, which get called on their corresponding events.

Note that `on_line()` is called also for `on_return()`. The reason is, that Python invokes the trace function *before* the corresponding line is executed. Hence, effectively, the `on_return()` is called with the binding produced by the execution of the previous statement in the environment. Our processing in effect is done on values that were bound by the previous statement. Hence, calling `on_line()` here is appropriate as it provides the event handler a chance to work on the previous binding.

```python
class AssignmentTracker(AssignmentTracker):
    def on_call(self, arg, cxt, my_vars):
        my_vars = cxt.parameters(my_vars)
        self.my_assignments.method_enter(cxt, self.fragments(my_vars))

    def on_line(self, arg, cxt, my_vars):
        self.my_assignments.method_statement(cxt, self.fragments(my_vars))

    def on_return(self, arg, cxt, my_vars):
        self.on_line(arg, cxt, my_vars)
        my_vars = {'<-%s' % cxt.method: arg} if self.track_return else {}
        self.my_assignments.method_exit(cxt, my_vars)

    def on_exception(self, arg, cxt, my_vara):
        return

    def track_event(self, event, arg, cxt, my_vars):
        self.current_event = event
        dispatch = {
            'call': self.on_call,
            'return': self.on_return,
            'line': self.on_line,
            'exception': self.on_exception
        }
        dispatch[event](arg, cxt, my_vars)
```

We can now use `AssignmentTracker` to track the different variables. To verify that our variable line number inference works, we recover definitions from the functions `A()`, `B()` and `C()` (with data annotations removed so that the input fragments are correctly identified).

```python
def C(cp_1):  # type: ignore
    c_2 = cp_1
    c_3 = c_2
    return c_3
```

```python
def B(bp_7):  # type: ignore
    b_8 = bp_7
    return C(b_8)
```

```python
def A(ap_12):  # type: ignore
    a_13 = ap_12
    a_14 = B(a_13)
    a_14 = a_14
    a_13 = a_14
    a_14 = B(a_13)
    a_14 = B(a_14)[3:]
```

Running `A()` with sufficient input.

```python
with Tracer('---xxx') as tracer:
    A(tracer.my_input)
tracker = AssignmentTracker(tracer.my_input, tracer.trace, log=True)
for k, v in tracker.my_assignments.seq_vars().items():
    print(k, '=', repr(v))
print()
for k, v in tracker.my_assignments.defined_vars(formatted=True):
    print(k, '=', repr(v))
```

As can be seen, the line numbers are now correctly identified for each variable.

 Let us try retrieving the assignments for a real world example.

```python
traces = []
for inputstr in URLS_X:
    clear_cache()
    with Tracer(inputstr, files=['urllib/parse.py']) as tracer:
        urlparse(tracer.my_input)
    traces.append((tracer.my_input, tracer.trace))

    tracker = AssignmentTracker(tracer.my_input, tracer.trace, log=True)
    for k, v in tracker.my_assignments.defined_vars():
        print(k, '=', repr(v))
    print()
```

The line numbers of variables can be verified from the source code of [urllib/parse.py](https://github.com/python/cpython/blob/3.6/Lib/urllib/parse.py).

### Recovering a Derivation Tree

Does handling variable reassignments help with our URL examples? We look at these next.

```python
class TreeMiner(TreeMiner):
    def get_derivation_tree(self):
        tree = (START_SYMBOL, [(self.my_input, [])])
        for var, value in self.my_assignments:
            self.log(0, "%s=%s" % (var, repr(value)))
            self.apply_new_definition(tree, var, value)
        return tree
```

#### Example 1: Recovering URL Derivation Tree

First we obtain the derivation tree of the URL 1

##### URL 1 derivation tree

```python
clear_cache()
with Tracer(URLS_X[0], files=['urllib/parse.py']) as tracer:
    urlparse(tracer.my_input)
sm = AssignmentTracker(tracer.my_input, tracer.trace)
dt = TreeMiner(tracer.my_input, sm.my_assignments.defined_vars())
display_tree(dt.tree)
```

Next, we obtain the derivation tree of URL 4

##### URL 4 derivation tree

```python
clear_cache()
with Tracer(URLS_X[-1], files=['urllib/parse.py']) as tracer:
    urlparse(tracer.my_input)
sm = AssignmentTracker(tracer.my_input, tracer.trace)
dt = TreeMiner(tracer.my_input, sm.my_assignments.defined_vars())
display_tree(dt.tree)
```

The derivation trees seem to belong to the same grammar. Hence, we obtain the grammar for the complete set. First, we update the `recover_grammar()` to use `AssignTracker`.

### Recover Grammar

```python
class GrammarMiner(GrammarMiner):
    def update_grammar(self, inputstr, trace):
        at = self.create_tracker(inputstr, trace)
        dt = self.create_tree_miner(inputstr, at.my_assignments.defined_vars())
        self.add_tree(dt)
        return self.grammar

    def create_tracker(self, *args):
        return AssignmentTracker(*args)

    def create_tree_miner(self, *args):
        return TreeMiner(*args)
```

Next, we use the modified `recover_grammar()` on derivation trees obtained from URLs.

```python
url_grammar = recover_grammar(url_parse, URLS_X, files=['urllib/parse.py'])
```

The recovered grammar is below.

```python
syntax_diagram(url_grammar)
```

Let us fuzz a little to see if the produced values are sane.

```python
f = GrammarFuzzer(url_grammar)
for _ in range(10):
    print(f.fuzz())
```

Our modifications do seem to help. Next, we check whether we can still retrieve the grammar for inventory.

#### Example 2: Recovering Inventory Grammar

```python
inventory_grammar = recover_grammar(process_vehicle, VEHICLES)
```

```python
syntax_diagram(inventory_grammar)
```

Using fuzzing to produce values from the grammar.

```python
f = GrammarFuzzer(inventory_grammar)
for _ in range(10):
    print(f.fuzz())
```

### Problems with the Grammar Miner with Reassignment

One of the problems with our grammar miner is that it doesn't yet account for the current context. That is, when replacing, a variable can replace tokens that it does not have access to (and hence, it is not a fragment of). Consider this example.

```python
with Tracer(INVENTORY) as tracer:
    process_inventory(tracer.my_input)
sm = AssignmentTracker(tracer.my_input, tracer.trace)
dt = TreeMiner(tracer.my_input, sm.my_assignments.defined_vars())
display_tree(dt.tree, graph_attr=lr_graph)
```

As can be seen, the derivation tree obtained is not quite what we expected. The issue is easily seen if we enable logging in the `TreeMiner`.

```python
dt = TreeMiner(tracer.my_input, sm.my_assignments.defined_vars(), log=True)
```

Look at the last statement. We have a value `1999,car,` where only the `year` got replaced. We no longer have a `'car'` variable to continue the replacement here. This happens because the `'car'` value in `'1999,car,Chevy,Venture'` is not treated as a new value because the value `'car'` had occurred for `'vehicle'` variable in the exact same location for a *different* method call (for `'2000,car,Mercury,Cougar'`).

## A Grammar Miner with Scope

We need to incorporate inspection of the variables in the current context. We already have a stack of method calls so that we can obtain the current method at any point. We need to do the same for variables.

For that, we extend the `CallStack` to a new class `InputStack` which holds the method invoked as well as the parameters observed. It is essentially the record of activation of the method. We start with the original input at the base of the stack, and for each new method-call, we push the parameters of that call into the stack as a new record.

### Input Stack

```python
class InputStack(CallStack):
    def __init__(self, i, fragment_len=FRAGMENT_LEN):
        self.inputs = [{START_SYMBOL: i}]
        self.fragment_len = fragment_len
        super().__init__()
```

In order to check if a particular variable be saved, we define `in_current_record()` which checks only the variables in the current scope for inclusion (rather than the original input string).

```python
class InputStack(InputStack):
    def in_current_record(self, val):
        return any(val in var for var in self.inputs[-1].values())
```

```python
my_istack = InputStack('hello my world')
```

```python
my_istack.in_current_record('hello')
```

```python
my_istack.in_current_record('bye')
```

```python
my_istack.inputs.append({'greeting': 'hello', 'location': 'world'})
```

```python
my_istack.in_current_record('hello')
```

```python
my_istack.in_current_record('my')
```

We define the method `ignored()` that returns true if either the variable is not a string, or the variable length is less than the defined `fragment_len`.

```python
class InputStack(InputStack):
    def ignored(self, val):
        return not (isinstance(val, str) and len(val) >= self.fragment_len)
```

```python
my_istack = InputStack('hello world')
my_istack.ignored(1)
```

```python
my_istack.ignored('a')
```

```python
my_istack.ignored('help')
```

We can now define the `in_scope()` method that checks whether the variable needs to be ignored, and if it is not to be ignored, whether the variable value is present in the current scope.

```python
class InputStack(InputStack):
    def in_scope(self, k, val):
        if self.ignored(val):
            return False
        return self.in_current_record(val)
```

Finally, we update `enter()` that pushes relevant variables in the current context to the stack.

```python
class InputStack(InputStack):
    def enter(self, method, inputs):
        my_inputs = {k: v for k, v in inputs.items() if self.in_scope(k, v)}
        self.inputs.append(my_inputs)
        super().enter(method)
```

When a method returns, we also need a corresponding `leave()` to pop out the inputs and unwind the stack.

```python
class InputStack(InputStack):
    def leave(self):
        self.inputs.pop()
        super().leave()
```

### ScopedVars

We need to update our `AssignmentVars` to include information about which scope the variable was defined in. We start by updating `method_init()`.

```python
class ScopedVars(AssignmentVars):
    def method_init(self):
        self.call_stack = self.create_call_stack(self.my_input)
        self.event_locations = {self.call_stack.method_id: []}

    def create_call_stack(self, i):
        return InputStack(i)
```

Similarly, the `method_enter()` now initializes the `accessed_seq_var` for the current method call.

```python
class ScopedVars(ScopedVars):
    def method_enter(self, cxt, my_vars):
        self.current_event = 'call'
        self.call_stack.enter(cxt.method, my_vars)
        self.accessed_seq_var[self.call_stack.method_id] = {}
        self.event_locations[self.call_stack.method_id] = []
        self.register_event(cxt)
        self.update(my_vars)
```

The `update()` method now saves the context in which the value is defined. In the case of a parameter to a function, the context should be the context in which the function was called. On the other hand, a value defined during a statement execution would have the current context.

Further, we annotate on value rather than key because we do not want to duplicate variables when parameters are in context in the next line. They will have same value, but different context because they are present in a statement execution.

```python
class ScopedVars(ScopedVars):
    def update(self, v):
        if self.current_event == 'call':
            context = -2
        elif self.current_event == 'line':
            context = -1
        else:
            context = -1
        for k, v in v.items():
            self._set_kv(k, (v, self.call_stack.at(context)))
        self.var_location_register(self.new_vars)
        self.new_vars = set()
```

We also need to save the current method invocation to determine which variables are in scope. This information is now incorporated in the variable name as `accessed_seq_var[method_id][var]`.

```python
class ScopedVars(ScopedVars):
    def var_name(self, var):
        return (var, self.call_stack.method_id,
                self.accessed_seq_var[self.call_stack.method_id][var])
```

As before, `var_access` simply initializes the corresponding counter, this time in the context of `method_id`.

```python
class ScopedVars(ScopedVars):
    def var_access(self, var):
        if var not in self.accessed_seq_var[self.call_stack.method_id]:
            self.accessed_seq_var[self.call_stack.method_id][var] = 0
        return self.var_name(var)
```

During a variable reassignment, we update the `accessed_seq_var` to reflect the new count.

```python
class ScopedVars(ScopedVars):
    def var_assign(self, var):
        self.accessed_seq_var[self.call_stack.method_id][var] += 1
        self.new_vars.add(self.var_name(var))
        return self.var_name(var)
```

We now update `defined_vars()` to account for the new information.

```python
class ScopedVars(ScopedVars):
    def defined_vars(self, formatted=True):
        def fmt(k):
            method, i = k[1]
            v = (method, i, k[0], self.var_def_lines[k])
            return "%s[%d]:%s@%s" % v if formatted else v

        return [(fmt(k), v) for k, v in self.defs.items()]
```

Updating `seq_vars()` to account for new information.

```python
class ScopedVars(ScopedVars):
    def seq_vars(self, formatted=True):
        def fmt(k):
            method, i = k[1]
            v = (method, i, k[0], self.var_def_lines[k], k[2])
            return "%s[%d]:%s@%s:%s" % v if formatted else v

        return {fmt(k): v for k, v in self.defs.items()}
```

### Scope Tracker

With the `InputStack` and `Vars` defined, we can now define the `ScopeTracker`. The `ScopeTracker` only saves variables if the value is present in the current scope.

```python
class ScopeTracker(AssignmentTracker):
    def __init__(self, my_input, trace, **kwargs):
        self.current_event = None
        super().__init__(my_input, trace, **kwargs)

    def create_assignments(self, *args):
        return ScopedVars(*args)
```

We define a wrapper for checking whether a variable is present in the scope.

```python
class ScopeTracker(ScopeTracker):
    def is_input_fragment(self, var, value):
        return self.my_assignments.call_stack.in_scope(var, value)
```

We can use the `ScopeTracker` as follows.

```python
vehicle_traces = []
with Tracer(INVENTORY) as tracer:
    process_inventory(tracer.my_input)
sm = ScopeTracker(tracer.my_input, tracer.trace)
vehicle_traces.append((tracer.my_input, sm))
for k, v in sm.my_assignments.seq_vars().items():
    print(k, '=', repr(v))
```

### Recovering a Derivation Tree

The main difference in `apply_new_definition()` is that we add a second condition that checks for scope. In particular, variables are only allowed to replace portions of string fragments that were in scope.
The variable scope is indicated by `scope`. However, merely accounting for scope is not sufficient. For example, consider the fragment below.

```python
def my_fn(stringval):
    partA, partB = stringval.split('/')
    return partA, partB

svalue = ...
v1, v2 = my_fn(svalue)
```

Here, `v1` and `v2` get their values from a previous function call. Not from their current context. That is, we have to provide an exception for cases where an internal child method call may have generated a large fragment as we showed above. To account for that, we define `mseq()` that retrieves the method call sequence. In the above case, the `mseq()` of the internal child method call would be larger than the current `mseq()`. If so, we allow the replacement to proceed.

```python
class ScopeTreeMiner(TreeMiner):
    def mseq(self, key):
        method, seq, var, lno = key
        return seq
```

The `nt_var()` method needs to take the tuple and generate a non-terminal symbol out of it. We skip the method sequence because it is not relevant for the grammar.

```python
class ScopeTreeMiner(ScopeTreeMiner):
    def nt_var(self, key):
        method, seq, var, lno = key
        return to_nonterminal("%s@%d:%s" % (method, lno, var))
```

We now redefine the `apply_new_definition()` to account for context and scope. In particular, a variable is allowed to replace a part of a value only if the variable is in *scope* -- that is, it's scope (method sequence number of either its calling context in case it is a parameter or the current context in case it is a statement) is same as that of the value's method sequence number. An exception is made when the value's method sequence number is greater than the variable's method sequence number. In that case, the value may have come from an internal call. We allow the replacement to proceed in that case.

```python
class ScopeTreeMiner(ScopeTreeMiner):
    def partition(self, part, value):
        return value.partition(part)
    def partition_by_part(self, pair, value):
        (nt_var, nt_seq), (v, v_scope) = pair
        prefix_k_suffix = [
                    (nt_var, [(v, [], nt_seq)]) if i == 1 else (e, [])
                    for i, e in enumerate(self.partition(v, value))
                    if e]
        return prefix_k_suffix

    def insert_into_tree(self, my_tree, pair):
        var, values, my_scope = my_tree
        (nt_var, nt_seq), (v, v_scope) = pair
        applied = False
        for i, value_ in enumerate(values):
            key, arr, scope = value_
            self.log(2, "-> [%d] %s" % (i, repr(value_)))
            if is_nonterminal(key):
                applied = self.insert_into_tree(value_, pair)
                if applied:
                    break
            else:
                if v_scope != scope:
                    if nt_seq > scope:
                        continue
                if not v or not self.string_part_of_value(v, key):
                    continue
                prefix_k_suffix = [(k, children, scope) for k, children
                                   in self.partition_by_part(pair, key)]
                del values[i]
                for j, rep in enumerate(prefix_k_suffix):
                    values.insert(j + i, rep)

                applied = True
                self.log(2, " > %s" % (repr([i[0] for i in prefix_k_suffix])))
                break
        return applied
```

The `apply_new_definition()` is now modified to carry additional contextual information `mseq`.

```python
class ScopeTreeMiner(ScopeTreeMiner):
    def apply_new_definition(self, tree, var, value_):
        nt_var = self.nt_var(var)
        seq = self.mseq(var)
        val, (smethod, mseq) = value_
        return self.insert_into_tree(tree, ((nt_var, seq), (val, mseq)))
```

We also modify `get_derivation_tree()` so that the initial node carries the context.

```python
class ScopeTreeMiner(ScopeTreeMiner):
    def get_derivation_tree(self):
        tree = (START_SYMBOL, [(self.my_input, [], 0)], 0)
        for var, value in self.my_assignments:
            self.log(0, "%s=%s" % (var, repr(value)))
            self.apply_new_definition(tree, var, value)
        return tree
```

#### Example 1: Recovering URL Parse Tree

We verify that our URL parse tree recovery still works as expected.

```python
url_dts = []
for inputstr in URLS_X:
    clear_cache()
    with Tracer(inputstr, files=['urllib/parse.py']) as tracer:
        urlparse(tracer.my_input)
    sm = ScopeTracker(tracer.my_input, tracer.trace)
    for k, v in sm.my_assignments.defined_vars(formatted=False):
        print(k, '=', repr(v))
    dt = ScopeTreeMiner(
        tracer.my_input,
        sm.my_assignments.defined_vars(
            formatted=False))
    display_tree(dt.tree, graph_attr=lr_graph)
    url_dts.append(dt)
```

#### Example 2: Recovering Inventory Parse Tree

Next, we look at recovering the parse tree from `process_inventory()` which failed last time.

```python
with Tracer(INVENTORY) as tracer:
    process_inventory(tracer.my_input)

sm = ScopeTracker(tracer.my_input, tracer.trace)
for k, v in sm.my_assignments.defined_vars():
    print(k, '=', repr(v))
inventory_dt = ScopeTreeMiner(
    tracer.my_input,
    sm.my_assignments.defined_vars(
        formatted=False))
display_tree(inventory_dt.tree, graph_attr=lr_graph)
```

The recovered parse tree seems reasonable.

One of the things that one might notice from our Example (2) is that the three subtrees -- `vehicle[2:1]`, `vehicle[4:1]` and `vehicle[6:1]` are quite alike. We will examine how this can be exploited to generate a grammar directly, next.

### Grammar Mining

The `tree_to_grammar()` is now redefined as follows, to account for the extra scope in nodes.

```python
class ScopedGrammarMiner(GrammarMiner):
    def tree_to_grammar(self, tree):
        key, children, scope = tree
        one_alt = [ckey for ckey, gchildren, cscope in children if ckey != key]
        hsh = {key: [one_alt] if one_alt else []}
        for child in children:
            (ckey, _gc, _cscope) = child
            if not is_nonterminal(ckey):
                continue
            chsh = self.tree_to_grammar(child)
            for k in chsh:
                if k not in hsh:
                    hsh[k] = chsh[k]
                else:
                    hsh[k].extend(chsh[k])
        return hsh
```

The grammar is in canonical form, which needs to be massaged to display. First, the recovered grammar for inventory.

```python
si = ScopedGrammarMiner()
si.add_tree(inventory_dt)
syntax_diagram(readable(si.grammar))
```

The recovered grammar for URLs.

```python
su = ScopedGrammarMiner()
for t in url_dts:
    su.add_tree(t)
syntax_diagram(readable(su.grammar))
```

One might notice that the grammar is not entirely human-readable, with a number of single token definitions.

Hence, the last piece of the puzzle is the cleanup method `clean_grammar()`, which cleans up such definitions. The idea is to look for single token definitions such that a key is defined exactly by another key (single alternative, single token, nonterminal).

```python
class ScopedGrammarMiner(ScopedGrammarMiner):
    def get_replacements(self, grammar):
        replacements = {}
        for k in grammar:
            if k == START_SYMBOL:
                continue
            alts = grammar[k]
            if len(set([str(i) for i in alts])) != 1:
                continue
            rule = alts[0]
            if len(rule) != 1:
                continue
            tok = rule[0]
            if not is_nonterminal(tok):
                continue
            replacements[k] = tok
        return replacements
```

Once we have such a list, iteratively replace the original key where ever it is used with the token we found earlier. Repeat until none is left.

```python
class ScopedGrammarMiner(ScopedGrammarMiner):
    def clean_grammar(self):
        replacements = self.get_replacements(self.grammar)

        while True:
            changed = set()
            for k in self.grammar:
                if k in replacements:
                    continue
                new_alts = []
                for alt in self.grammar[k]:
                    new_alt = []
                    for t in alt:
                        if t in replacements:
                            new_alt.append(replacements[t])
                            changed.add(t)
                        else:
                            new_alt.append(t)
                    new_alts.append(new_alt)
                self.grammar[k] = new_alts
            if not changed:
                break
            for k in changed:
                self.grammar.pop(k, None)
        return readable(self.grammar)
```

The `clean_grammar()` is used as follows:

```python
si = ScopedGrammarMiner()
si.add_tree(inventory_dt)
syntax_diagram(readable(si.clean_grammar()))
```

We update the `update_grammar()` to use the right tracker and miner.

```python
class ScopedGrammarMiner(ScopedGrammarMiner):
    def update_grammar(self, inputstr, trace):
        at = self.create_tracker(inputstr, trace)
        dt = self.create_tree_miner(
            inputstr, at.my_assignments.defined_vars(
                formatted=False))
        self.add_tree(dt)
        return self.grammar

    def create_tracker(self, *args):
        return ScopeTracker(*args)

    def create_tree_miner(self, *args):
        return ScopeTreeMiner(*args)
```

The `recover_grammar()` uses the right miner, and returns a cleaned grammar.

```python
def recover_grammar(fn, inputs, **kwargs):  # type: ignore
    miner = ScopedGrammarMiner()
    for inputstr in inputs:
        with Tracer(inputstr, **kwargs) as tracer:
            fn(tracer.my_input)
        miner.update_grammar(tracer.my_input, tracer.trace)
    return readable(miner.clean_grammar())
```

```python
url_grammar = recover_grammar(url_parse, URLS_X, files=['urllib/parse.py'])
```

```python
syntax_diagram(url_grammar)
```

```python
f = GrammarFuzzer(url_grammar)
for _ in range(10):
    print(f.fuzz())
```

```python
inventory_grammar = recover_grammar(process_inventory, [INVENTORY])
```

```python
syntax_diagram(inventory_grammar)
```

```python
f = GrammarFuzzer(inventory_grammar)
for _ in range(10):
    print(f.fuzz())
```

We see how tracking scope helps us to extract an even more precise grammar.

Notice that we use *String* inclusion testing as a way of determining whether a particular string fragment came from the original input string. While this may seem rather error-prone compared to dynamic tainting, we note that numerous tracing tools such as `dtrace()` and `ptrace()` allow one to obtain the information we seek from execution of binaries directly in different platforms. However, methods for obtaining dynamic taints almost always involve instrumenting the binaries before they can be used. Hence, this method of string inclusion can be more generally applied than dynamic tainting approaches. Further, dynamic taints are often lost due to implicit transmission, or at the boundary between *Python* and *C* code. String inclusion has not such problems. Hence, our approach can often obtain better results than relying on dynamic tainting.

## Synopsis

This chapter provides a number of classes to mine input grammars from existing programs.  The function `recover_grammar()` could be the easiest to use.  It takes a function and a set of inputs, and returns a grammar that describes its input language.

We apply `recover_grammar()` on a `url_parse()` function that takes and decomposes URLs:

```python
url_parse('https://www.fuzzingbook.org/')
```

```python
URLS
```

We extract the input grammar for `url_parse()` using `recover_grammar()`:

```python
grammar = recover_grammar(url_parse, URLS, files=['urllib/parse.py'])
grammar
```

The names of nonterminals are a bit technical; but the grammar nicely represents the structure of the input; for instance, the different schemes (`"http"`, `"https"`) are all identified:

```python
syntax_diagram(grammar)
```

The grammar can be immediately used for fuzzing, producing arbitrary combinations of input elements, which are all syntactically valid.

```python
from GrammarCoverageFuzzer import GrammarCoverageFuzzer
```

```python
fuzzer = GrammarCoverageFuzzer(grammar)
[fuzzer.fuzz() for i in range(5)]
```

Being able to automatically extract a grammar and to use this grammar for fuzzing makes for very effective test generation with a minimum of manual work.

## Lessons Learned

* Given a set of sample inputs for a program, we can learn an input grammar by examining variable values during execution if the program relies on handwritten parsers.
* Simple string inclusion checks are sufficient to obtain reasonably accurate grammars from real world programs.
* The resulting grammars can be directly used for fuzzing, and can have a multiplier effect on any samples you have.

## Next Steps

* Learn how to use [information flow](InformationFlow.ipynb) to further improve mapping inputs to states.

## Background

Recovering the language from a _set of samples_ (i.e., not taking into account a possible program that might process them) is a well researched topic.  The excellent reference by Higuera \cite{higuera2010grammatical} covers all the classical approaches. The current state of the art in black box grammar mining is described by Clark \cite{clark2013learning}.

Learning an input language from a _program_, with or without samples, is yet an emerging topic, despite its potential for fuzzing.  The pioneering work in this area was done by Lin et al. \cite{Lin2008} who invented a way to retrieve the parse trees from top down and bottom up parsers. The approach described in this chapter is based directly on the AUTOGRAM work of Hoschele et al. \cite{Hoschele2017}.

## Exercises

### Exercise 1: Flattening complex objects

Our grammar miners only check for string fragments. However, programs may often pass containers or custom objects containing input fragments. For example, consider the plausible modification for our inventory processor, where we use a custom object `Vehicle` to carry fragments.

```python
class Vehicle:
    def __init__(self, vehicle: str):
        year, kind, company, model, *_ = vehicle.split(',')
        self.year, self.kind, self.company, self.model = year, kind, company, model
```

```python
def process_inventory_with_obj(inventory: str) -> str:
    res = []
    for vehicle in inventory.split('\n'):
        ret = process_vehicle(vehicle)
        res.extend(ret)

    return '\n'.join(res)
```

```python
def process_vehicle_with_obj(vehicle: str) -> List[str]:
    v = Vehicle(vehicle)
    if v.kind == 'van':
        return process_van_with_obj(v)

    elif v.kind == 'car':
        return process_car_with_obj(v)

    else:
        raise Exception('Invalid entry')
```

```python
def process_van_with_obj(vehicle: Vehicle) -> List[str]:
    res = [
        "We have a %s %s van from %s vintage." % (vehicle.company,
                                                  vehicle.model, vehicle.year)
    ]
    iyear = int(vehicle.year)
    if iyear > 2010:
        res.append("It is a recent model!")
    else:
        res.append("It is an old but reliable model!")
    return res
```

```python
def process_car_with_obj(vehicle: Vehicle) -> List[str]:
    res = [
        "We have a %s %s car from %s vintage." % (vehicle.company,
                                                  vehicle.model, vehicle.year)
    ]
    iyear = int(vehicle.year)
    if iyear > 2016:
        res.append("It is a recent model!")
    else:
        res.append("It is an old but reliable model!")
    return res
```

We recover the grammar as before.

```python
vehicle_grammar = recover_grammar(
    process_inventory_with_obj,
    [INVENTORY],
    methods=INVENTORY_METHODS)
```

The new vehicle grammar is missing in details, especially as to the different models and company for a van and car.

```python
syntax_diagram(vehicle_grammar)
```

The problem is that, we are looking specifically for string objects that contain fragments of the input string during tracing. Can you modify our grammar miner to correctly account for the complex objects too?

**Solution.**

The problem can be understood if we execute the tracer under verbose logging.

```python
with Tracer(INVENTORY, methods=INVENTORY_METHODS, log=True) as tracer:
    process_inventory(tracer.my_input)
print()
print('Traced values:')
for t in tracer.trace:
    print(t)
```

You can see that we lose track of string fragments as soon as they are incorporated into the `Vehicle` object. The way out is to trace these variables separately.

For that, we develop the `flatten()` method that given any custom complex object and its key, returns a list of flattened (_key_, _value_) pairs that correspond to the object passed in.

The `MAX_DEPTH` parameter controls the maximum flattening limit.

```python
MAX_DEPTH = 10
```

```python
def set_flatten_depth(depth):
    global MAX_DEPTH
    MAX_DEPTH = depth
```

```python
def flatten(key, val, depth=MAX_DEPTH):
    tv = type(val)
    if depth <= 0:
        return [(key, val)]
    if isinstance(val, (int, float, complex, str, bytes, bytearray)):
        return [(key, val)]
    elif isinstance(val, (set, frozenset, list, tuple, range)):
        values = [(i, e) for i, elt in enumerate(val) for e in flatten(i, elt, depth-1)]
        return [("%s.%d" % (key, i), v) for i, v in values]
    elif isinstance(val, dict):
        values = [e for k, elt in val.items() for e in flatten(k, elt, depth-1)]
        return [("%s.%s" % (key, k), v) for k, v in values]
    elif isinstance(val, str):
        return [(key, val)]
    elif hasattr(val, '__dict__'):
        values = [e for k, elt in val.__dict__.items()
                  for e in flatten(k, elt, depth-1)]
        return [("%s.%s" % (key, k), v) for k, v in values]
    else:
        return [(key, val)]
```

Next, we hook the `flatten()` into the `Context` class so that the parameters we obtain are flattened.

```python
class Context(Context):
    def extract_vars(self, frame):
        vals = inspect.getargvalues(frame).locals
        return {k1: v1 for k, v in vals.items() for k1, v1 in flatten(k, v)}

    def parameters(self, all_vars):
        def check_param(k):
            return any(k.startswith(p) for p in self.parameter_names)
        return {k: v for k, v in all_vars.items() if check_param(k)}

    def qualified(self, all_vars):
        return {"%s:%s" % (self.method, k): v for k, v in all_vars.items()}
```

With this change, we have the following trace output.

```python
with Tracer(INVENTORY, methods=INVENTORY_METHODS, log=True) as tracer:
    process_inventory(tracer.my_input)
print()
print('Traced values:')
for t in tracer.trace:
    print(t)
```

Our change seems to have worked. Let us derive the grammar.

```python
vehicle_grammar = recover_grammar(
    process_inventory,
    [INVENTORY],
    methods=INVENTORY_METHODS)
```

```python
syntax_diagram(vehicle_grammar)
```

The recovered grammar contains all the details that we were able to recover before.

### Exercise 2: Incorporating Taints from InformationFlow

We have been using *string inclusion* to check whether a particular fragment came from the input string. This is unsatisfactory as it required us to compromise on the size of the strings tracked, which was limited to those greater than `FRAGMENT_LEN`. Further, it is possible that a single method could process a string where a fragment repeats, but is part of different tokens. For example, an embedded comma in the CSV file would cause our parser to fail. One way to avoid this is to rely on *dynamic taints*, and check for taint inclusion rather than string inclusion.

The chapter on [information flow](InformationFlow.ipynb) details how to incorporate dynamic taints. Can you update our grammar miner based on scope to use *dynamic taints* instead?

**Solution.**

First, we import `ostr` to track the origins of string fragments.

```python
from InformationFlow import ostr
```

Next, we define `is_fragment()` to verify that a fragment is from a given input string.

```python
def is_fragment(fragment, original):
    assert isinstance(original, ostr)
    if not isinstance(fragment, ostr):
        return False
    return set(fragment.origin) <= set(original.origin)
```

Now, all that remains is to hook the tainted fragment check to our grammar miner. This is accomplished by modifying `in_current_record()` and `ignored()` methods in the `InputStack`.

```python
class TaintedInputStack(InputStack):
    def in_current_record(self, val):
        return any(is_fragment(val, var) for var in self.inputs[-1].values())
```

```python
class TaintedInputStack(TaintedInputStack):
    def ignored(self, val):
        return not isinstance(val, ostr)
```

We then hook in the `TaintedInputStack` to the grammar mining infrastructure.

```python
class TaintedScopedVars(ScopedVars):
    def create_call_stack(self, i):
        return TaintedInputStack(i)
```

```python
class TaintedScopeTracker(ScopeTracker):
    def create_assignments(self, *args):
        return TaintedScopedVars(*args)
```

```python
class TaintedScopeTreeMiner(ScopeTreeMiner):
    def string_part_of_value(self, part, value):
        return is_fragment(part, value)

    def partition(self, part, value):
        begin = value.origin.index(part.origin[0])
        end = value.origin.index(part.origin[-1])+1
        return value[:begin], value[begin:end], value[end:]
```

<!-- **Advanced.** The *dynamic taint* approach is limited in that it can not observe implicit flows. For example, consider the fragment below.

```python
if my_fragment == 'begin':
    return 'begin'
```

In this case, we lose track of the string `begin` that is returned even though it is dependent on the value of `my_fragment`. For such cases, a better (but costly) alternative is to rely on concolic execution and capture the constraints as it relates to input characters on each variable.

The chapter on [concolic fuzzing](ConcolicFuzzer.ipynb) details how to incorporate concolic symbolic execution to program execution. Can you update our grammar miner to use *concolic execution* to track taints instead?
-->

```python
class TaintedScopedGrammarMiner(ScopedGrammarMiner):
    def create_tracker(self, *args):
        return TaintedScopeTracker(*args)

    def create_tree_miner(self, *args):
        return TaintedScopeTreeMiner(*args)
```

Finally, we define `recover_grammar_with_taints()` to recover the grammar.

```python
def recover_grammar_with_taints(fn, inputs, **kwargs):
    miner = TaintedScopedGrammarMiner()
    for inputstr in inputs:
        with Tracer(ostr(inputstr), **kwargs) as tracer:
            fn(tracer.my_input)
        miner.update_grammar(tracer.my_input, tracer.trace)
    return readable(miner.clean_grammar())
```

Here is how one can use it.

```python
inventory_grammar = recover_grammar_with_taints(
    process_inventory, [INVENTORY],
    methods=[
        'process_inventory', 'process_vehicle', 'process_car', 'process_van'
    ])
```

```python
syntax_diagram(inventory_grammar)
```

```python
url_grammar = recover_grammar_with_taints(
    url_parse, URLS_X + ['ftp://user4:pass1@host4/?key4=value3'],
    methods=['urlsplit', 'urlparse', '_splitnetloc'])
```