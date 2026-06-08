# Carving Unit Tests

So far, we have always generated _system input_, i.e. data that the program as a whole obtains via its input channels.  If we are interested in testing only a small set of functions, having to go through the system can be very inefficient.  This chapter introduces a technique known as _carving_, which, given a system test, automatically extracts a set of _unit tests_ that replicate the calls seen during the system test.  The key idea is to _record_ such calls such that we can _replay_ them later – as a whole or selectively.  On top, we also explore how to synthesize API grammars from carved unit tests; this means that we can _synthesize API tests without having to write a grammar at all._

**Prerequisites**

* Carving makes use of dynamic traces of function calls and variables, as introduced in the [chapter on configuration fuzzing](ConfigurationFuzzer.ipynb).
* Using grammars to test units was introduced in the [chapter on API fuzzing](APIFuzzer.ipynb).

```python
import bookutils.setup
```

```python
import APIFuzzer
```

## Synopsis
<!-- Automatically generated. Do not edit. -->

To [use the code provided in this chapter](Importing.ipynb), write

```python
>>> from fuzzingbook.Carver import <identifier>
```

and then make use of the following features.

This chapter provides means to _record and replay function calls_ during a system test.  Since individual function calls are much faster than a whole system run, such "carving" mechanisms have the potential to run tests much faster.

### Recording Calls

The `CallCarver` class records all calls occurring while it is active.  It is used in conjunction with a `with` clause:

```python
>>> with CallCarver() as carver:
>>>     y = my_sqrt(2)
>>>     y = my_sqrt(4)
```
After execution, `called_functions()` lists the names of functions encountered:

```python
>>> carver.called_functions()
['my_sqrt', '__exit__']
```
The `arguments()` method lists the arguments recorded for a function.  This is a mapping of the function name to a list of lists of arguments; each argument is a pair (parameter name, value).

```python
>>> carver.arguments('my_sqrt')
[[('x', 2)], [('x', 4)]]
```
Complex arguments are properly serialized, such that they can be easily restored.

### Synthesizing Calls

While such recorded arguments already could be turned into arguments and calls, a much nicer alternative is to create a _grammar_ for recorded calls.  This allows synthesizing arbitrary _combinations_ of arguments, and also offers a base for further customization of calls.

The `CallGrammarMiner` class turns a list of carved executions into a grammar.

```python
>>> my_sqrt_miner = CallGrammarMiner(carver)
>>> my_sqrt_grammar = my_sqrt_miner.mine_call_grammar()
>>> my_sqrt_grammar
{'<start>': ['<call>'],
 '<call>': ['<my_sqrt>'],
 '<my_sqrt-x>': ['2', '4'],
 '<my_sqrt>': ['my_sqrt(<my_sqrt-x>)']}
```
This grammar can be used to synthesize calls.

```python
>>> fuzzer = GrammarCoverageFuzzer(my_sqrt_grammar)
>>> fuzzer.fuzz()
'my_sqrt(4)'
```
These calls can be executed in isolation, effectively extracting unit tests from system tests:

```python
>>> eval(fuzzer.fuzz())
1.414213562373095
```

## System Tests vs Unit Tests

Remember the URL grammar introduced for [grammar fuzzing](Grammars.ipynb)?  With such a grammar, we can happily test a Web browser again and again, checking how it reacts to arbitrary page requests.

Let us define a very simple "web browser" that goes and downloads the content given by the URL.

```python
import urllib.parse
```

```python
def webbrowser(url):
    """Download the http/https resource given by the URL"""
    import requests  # Only import if needed

    r = requests.get(url)
    return r.text
```

Let us apply this on [fuzzingbook.org](https://www.fuzzingbook.org/) and measure the time, using the [Timer class](Timer.ipynb):

```python
from Timer import Timer
```

```python
with Timer() as webbrowser_timer:
    fuzzingbook_contents = webbrowser(
        "http://www.fuzzingbook.org/html/Fuzzer.html")

print("Downloaded %d bytes in %.2f seconds" %
      (len(fuzzingbook_contents), webbrowser_timer.elapsed_time()))
```

```python
fuzzingbook_contents[:100]
```

A full web browser, of course, would also render the HTML content.  We can achieve this using these commands (but we don't, as we do not want to replicate the entire Web page here):

```python
from IPython.display import HTML, display
HTML(fuzzingbook_contents)
```

Having to start a whole browser (or having it render a Web page) again and again means lots of overhead, though – in particular if we want to test only a subset of its functionality.  In particular, after a change in the code, we would prefer to test only the subset of functions that is affected by the change, rather than running the well-tested functions again and again.

Let us assume we change the function that takes care of parsing the given URL and decomposing it into the individual elements – the scheme ("http"), the network location (`"www.fuzzingbook.com"`), or the path (`"/html/Fuzzer.html"`).  This function is named `urlparse()`:

```python
from urllib.parse import urlparse
```

```python
urlparse('https://www.fuzzingbook.com/html/Carver.html')
```

You see how the individual elements of the URL – the _scheme_ (`"http"`), the _network location_ (`"www.fuzzingbook.com"`), or the path (`"//html/Carver.html"`) are all properly identified.  Other elements (like `params`, `query`, or `fragment`) are empty, because they were not part of our input.

The interesting thing is that executing only `urlparse()` is orders of magnitude faster than running all of `webbrowser()`.  Let us measure the factor:

```python
runs = 1000
with Timer() as urlparse_timer:
    for i in range(runs):
        urlparse('https://www.fuzzingbook.com/html/Carver.html')

avg_urlparse_time = urlparse_timer.elapsed_time() / 1000
avg_urlparse_time
```

Compare this to the time required by the web browser

```python
webbrowser_timer.elapsed_time()
```

The difference in time is huge:

```python
webbrowser_timer.elapsed_time() / avg_urlparse_time
```

Hence, in the time it takes to run `webbrowser()` once, we can have _tens of thousands_ of executions of `urlparse()` – and this does not even take into account the time it takes the browser to render the downloaded HTML, to run the included scripts, and whatever else happens when a Web page is loaded.  Hence, strategies that allow us to test at the _unit_ level are very promising as they can save lots of overhead.

## Carving Unit Tests

Testing methods and functions at the unit level requires a very good understanding of the individual units to be tested as well as their interplay with other units.  Setting up an appropriate infrastructure and writing unit tests by hand thus is demanding, yet rewarding.  There is, however, an interesting alternative to writing unit tests by hand.  The technique of _carving_ automatically _converts system tests into unit tests_ by means of recording and replaying function calls:

1. During a system test (given or generated), we _record_ all calls into a function, including all arguments and other variables the function reads.
2. From these, we synthesize a self-contained _unit test_ that reconstructs the function call with all arguments.
3. This unit test can be executed (replayed) at any time with high efficiency.

In the remainder of this chapter, let us explore these steps.

## Recording Calls

Our first challenge is to record function calls together with their arguments.  (In the interest of simplicity, we restrict ourselves to arguments, ignoring any global variables or other non-arguments that are read by the function.)  To record calls and arguments, we use the mechanism [we introduced for coverage](Coverage.ipynb): By setting up a tracer function, we track all calls into individual functions, also saving their arguments.  Just like `Coverage` objects, we want to use `Carver` objects to be able to be used in conjunction with the `with` statement, such that we can trace a particular code block:

```python
with Carver() as carver:
    function_to_be_traced()
c = carver.calls()
```

The initial definition supports this construct:

\todo{Get tracker from [dynamic invariants](DynamicInvariants.ipynb)}

```python
import sys
```

```python
class Carver:
    def __init__(self, log=False):
        self._log = log
        self.reset()

    def reset(self):
        self._calls = {}

    # Start of `with` block
    def __enter__(self):
        self.original_trace_function = sys.gettrace()
        sys.settrace(self.traceit)
        return self

    # End of `with` block
    def __exit__(self, exc_type, exc_value, tb):
        sys.settrace(self.original_trace_function)
```

The actual work takes place in the `traceit()` method, which records all calls in the `_calls` attribute.  First, we define two helper functions:

```python
import inspect
```

```python
def get_qualified_name(code):
    """Return the fully qualified name of the current function"""
    name = code.co_name
    module = inspect.getmodule(code)
    if module is not None:
        name = module.__name__ + "." + name
    return name
```

```python
def get_arguments(frame):
    """Return call arguments in the given frame"""
    # When called, all arguments are local variables
    local_variables = frame.f_locals.copy()
    arguments = [(var, frame.f_locals[var])
                 for var in local_variables]
    arguments.reverse()  # Want same order as call
    return arguments
```

```python
class CallCarver(Carver):
    def add_call(self, function_name, arguments):
        """Add given call to list of calls"""
        if function_name not in self._calls:
            self._calls[function_name] = []
        self._calls[function_name].append(arguments)

    # Tracking function: Record all calls and all args
    def traceit(self, frame, event, arg):
        if event != "call":
            return None

        code = frame.f_code
        function_name = code.co_name
        qualified_name = get_qualified_name(code)
        arguments = get_arguments(frame)

        self.add_call(function_name, arguments)
        if qualified_name != function_name:
            self.add_call(qualified_name, arguments)

        if self._log:
            print(simple_call_string(function_name, arguments))

        return None
```

Finally, we need some convenience functions to access the calls:

```python
class CallCarver(CallCarver):
    def calls(self):
        """Return a dictionary of all calls traced."""
        return self._calls

    def arguments(self, function_name):
        """Return a list of all arguments of the given function
        as (VAR, VALUE) pairs.
        Raises an exception if the function was not traced."""
        return self._calls[function_name]

    def called_functions(self, qualified=False):
        """Return all functions called."""
        if qualified:
            return [function_name for function_name in self._calls.keys()
                    if function_name.find('.') >= 0]
        else:
            return [function_name for function_name in self._calls.keys()
                    if function_name.find('.') < 0]
```

### Recording my_sqrt()

Let's try out our new `Carver` class – first on a very simple function:

```python
from Intro_Testing import my_sqrt
```

```python
with CallCarver() as sqrt_carver:
    my_sqrt(2)
    my_sqrt(4)
```

We can retrieve all calls seen...

```python
sqrt_carver.calls()
```

```python
sqrt_carver.called_functions()
```

... as well as the arguments of a particular function:

```python
sqrt_carver.arguments("my_sqrt")
```

We define a convenience function for nicer printing of these lists:

```python
def simple_call_string(function_name, argument_list):
    """Return function_name(arg[0], arg[1], ...) as a string"""
    return function_name + "(" + \
        ", ".join([var + "=" + repr(value)
                   for (var, value) in argument_list]) + ")"
```

```python
for function_name in sqrt_carver.called_functions():
    for argument_list in sqrt_carver.arguments(function_name):
        print(simple_call_string(function_name, argument_list))
```

This is a syntax we can directly use to invoke `my_sqrt()` again:

```python
eval("my_sqrt(x=2)")
```

### Carving urlparse()

What happens if we apply this to `webbrowser()`?

```python
with CallCarver() as webbrowser_carver:
    webbrowser("https://www.fuzzingbook.org")
```

We see that retrieving a URL from the Web requires quite some functionality:

```python
function_list = webbrowser_carver.called_functions(qualified=True)
len(function_list)
```

```python
print(function_list[:50])
```

Among several other functions, we also have a call to `urlparse()`:

```python
urlparse_argument_list = webbrowser_carver.arguments("urllib.parse.urlparse")
urlparse_argument_list
```

Again, we can convert this into a well-formatted call:

```python
urlparse_call = simple_call_string("urlparse", urlparse_argument_list[0])
urlparse_call
```

Again, we can re-execute this call:

```python
eval(urlparse_call)
```

We now have successfully carved the call to `urlparse()` out of the `webbrowser()` execution.

## Replaying Calls

Replaying calls in their entirety and in all generality is tricky, as there are several challenges to be addressed.  These include:

1. We need to be able to _access_ individual functions.  If we access a function by name, the name must be in scope.  If the name is not visible (for instance, because it is a name internal to the module), we must make it visible.

2. Any _resources_ accessed outside of arguments must be recorded and reconstructed for replay as well.  This can be difficult if variables refer to external resources such as files or network resources.

3. _Complex objects_ must be reconstructed as well.

These constraints make carving hard or even impossible if the function to be tested interacts heavily with its environment.  To illustrate these issues, consider the `email.parser.parse()` method that is invoked in `webbrowser()`:

```python
email_parse_argument_list = webbrowser_carver.arguments("email.parser.parse")
```

Calls to this method look like this:

```python
email_parse_call = simple_call_string(
    "email.parser.Parser.parse",
    email_parse_argument_list[0])
email_parse_call
```

We see that `email.parser.Parser.parse()` is part of a `email.parser.Parser` object (`self`) and it gets a `StringIO` object (`fp`).  Both are non-primitive values.  How could we possibly reconstruct them?

### Serializing Objects

The answer to the problem of complex objects lies in creating a _persistent_ representation that can be _reconstructed_ at later points in time.  This process is known as _serialization_; in Python, it is also known as _pickling_.  The `pickle` module provides means to create a serialized representation of an object.  Let us apply this on the `email.parser.Parser` object we just found:

```python
import pickle
```

```python
email_parse_argument_list
```

```python
parser_object = email_parse_argument_list[0][2][1]
parser_object
```

```python
pickled = pickle.dumps(parser_object)
pickled
```

From this string representing the serialized `email.parser.Parser` object, we can recreate the Parser object at any time:

```python
unpickled_parser_object = pickle.loads(pickled)
unpickled_parser_object
```

The serialization mechanism allows us to produce a representation for all objects passed as parameters (assuming they can be pickled, that is).  We can now extend the `simple_call_string()` function such that it automatically pickles objects.  Additionally, we set it up such that if the first parameter is named `self` (i.e., it is a class method), we make it a method of the `self` object.

```python
def call_value(value):
    value_as_string = repr(value)
    if value_as_string.find('<') >= 0:
        # Complex object
        value_as_string = "pickle.loads(" + repr(pickle.dumps(value)) + ")"
    return value_as_string
```

```python
def call_string(function_name, argument_list):
    """Return function_name(arg[0], arg[1], ...) as a string, pickling complex objects"""
    if len(argument_list) > 0:
        (first_var, first_value) = argument_list[0]
        if first_var == "self":
            # Make this a method call
            method_name = function_name.split(".")[-1]
            function_name = call_value(first_value) + "." + method_name
            argument_list = argument_list[1:]

    return function_name + "(" + \
        ", ".join([var + "=" + call_value(value)
                   for (var, value) in argument_list]) + ")"
```

Let us apply the extended `call_string()` method to create a call for `email.parser.parse()`, including pickled objects:

```python
call = call_string("email.parser.Parser.parse", email_parse_argument_list[0])
print(call)
```

With this call involving the pickled object, we can now re-run the original call and obtain a valid result:

```python
import email
```

```python
eval(call)
```

### All Calls

So far, we have seen only one call of `webbrowser()`.  How many of the calls within `webbrowser()` can we actually carve and replay?  Let us try this out and compute the numbers.

```python
import traceback
```

```python
import enum
import socket
```

```python
all_functions = set(webbrowser_carver.called_functions(qualified=True))
call_success = set()
run_success = set()
```

```python
exceptions_seen = set()

for function_name in webbrowser_carver.called_functions(qualified=True):
    for argument_list in webbrowser_carver.arguments(function_name):
        try:
            call = call_string(function_name, argument_list)
            call_success.add(function_name)

            result = eval(call)
            run_success.add(function_name)

        except Exception as exc:
            exceptions_seen.add(repr(exc))
            # print("->", call, file=sys.stderr)
            # traceback.print_exc()
            # print("", file=sys.stderr)
            continue
```

```python
print("%d/%d calls (%.2f%%) successfully created and %d/%d calls (%.2f%%) successfully ran" % (
    len(call_success), len(all_functions), len(
        call_success) * 100 / len(all_functions),
    len(run_success), len(all_functions), len(run_success) * 100 / len(all_functions)))
```

About a quarter of the calls succeed.  Let us take a look into some of the error messages we get:

```python
for i in range(10):
    print(list(exceptions_seen)[i])
```

We see that:

* **A large majority of calls could be converted into call strings.**  If this is not the case, this is mostly due to having non-serialized objects being passed.
* **About a quarter of the calls could be executed.**  The error messages for the failing runs are varied; the most frequent being that some internal name is invoked that is not in scope.

Our carving mechanism should be taken with a grain of salt: We still do not cover the situation where external variables and values (such as global variables) are being accessed, and the serialization mechanism cannot recreate external resources.  Still, if the function of interest falls among those that _can_ be carved and replayed, we can very effectively re-run its calls with their original arguments.

## Mining API Grammars from Carved Calls

So far, we have used carved calls to replay exactly the same invocations as originally encountered.  However, we can also _mutate_ carved calls to effectively fuzz APIs with previously recorded arguments.

The general idea is as follows:

1. First, we record all calls of a specific function from a given execution of the program.
2. Second, we create a grammar that incorporates all these calls, with separate rules for each argument and alternatives for each value found; this allows us to produce calls that arbitrarily _recombine_ these arguments.

Let us explore these steps in the following sections.

### From Calls to Grammars

Let us start with an example.  The `power(x, y)` function returns $x^y$; it is but a wrapper around the equivalent `math.pow()` function.  (Since `power()` is defined in Python, we can trace it – in contrast to `math.pow()`, which is implemented in C.)

```python
import math
```

```python
def power(x, y):
    return math.pow(x, y)
```

Let us invoke `power()` while recording its arguments:

```python
with CallCarver() as power_carver:
    z = power(1, 2)
    z = power(3, 4)
```

```python
power_carver.arguments("power")
```

From this list of recorded arguments, we could now create a grammar for the `power()` call, with `x` and `y` expanding into the values seen:

```python
from Grammars import START_SYMBOL, is_valid_grammar, new_symbol
from Grammars import extend_grammar, Grammar
```

```python
POWER_GRAMMAR: Grammar = {
    "<start>": ["power(<x>, <y>)"],
    "<x>": ["1", "3"],
    "<y>": ["2", "4"]
}

assert is_valid_grammar(POWER_GRAMMAR)
```

When fuzzing with this grammar, we then get arbitrary combinations of `x` and `y`; aiming for coverage will ensure that all values are actually tested at least once:

```python
from GrammarCoverageFuzzer import GrammarCoverageFuzzer
```

```python
power_fuzzer = GrammarCoverageFuzzer(POWER_GRAMMAR)
[power_fuzzer.fuzz() for i in range(5)]
```

What we need is a method to automatically convert the arguments as seen in `power_carver` to the grammar as seen in `POWER_GRAMMAR`.  This is what we define in the next section.

### A Grammar Miner for Calls

We introduce a class `CallGrammarMiner`, which, given a `Carver`, automatically produces a grammar from the calls seen.  To initialize, we pass the carver object:

```python
class CallGrammarMiner:
    def __init__(self, carver, log=False):
        self.carver = carver
        self.log = log
```

#### Initial Grammar

The initial grammar produces a single call.  The possible `<call>` expansions are to be constructed later:

```python
import copy
```

```python
class CallGrammarMiner(CallGrammarMiner):
    CALL_SYMBOL = "<call>"

    def initial_grammar(self):
        return extend_grammar(
            {START_SYMBOL: [self.CALL_SYMBOL],
                self.CALL_SYMBOL: []
             })
```

```python
m = CallGrammarMiner(power_carver)
initial_grammar = m.initial_grammar()
initial_grammar
```

#### A Grammar from Arguments

Let us start by creating a grammar from a list of arguments.  The method `mine_arguments_grammar()` creates a grammar for the arguments seen during carving, such as these:

```python
arguments = power_carver.arguments("power")
arguments
```

The `mine_arguments_grammar()` method iterates through the variables seen and creates a mapping `variables` of variable names to a set of values seen (as strings, going through `call_value()`).  In a second step, it then creates a grammar with a rule for each variable name, expanding into the values seen.

```python
class CallGrammarMiner(CallGrammarMiner):
    def var_symbol(self, function_name, var, grammar):
        return new_symbol(grammar, "<" + function_name + "-" + var + ">")

    def mine_arguments_grammar(self, function_name, arguments, grammar):
        var_grammar = {}

        variables = {}
        for argument_list in arguments:
            for (var, value) in argument_list:
                value_string = call_value(value)
                if self.log:
                    print(var, "=", value_string)

                if value_string.find("<") >= 0:
                    var_grammar["<langle>"] = ["<"]
                    value_string = value_string.replace("<", "<langle>")

                if var not in variables:
                    variables[var] = set()
                variables[var].add(value_string)

        var_symbols = []
        for var in variables:
            var_symbol = self.var_symbol(function_name, var, grammar)
            var_symbols.append(var_symbol)
            var_grammar[var_symbol] = list(variables[var])

        return var_grammar, var_symbols
```

```python
m = CallGrammarMiner(power_carver)
var_grammar, var_symbols = m.mine_arguments_grammar(
    "power", arguments, initial_grammar)
```

```python
var_grammar
```

The additional return value `var_symbols` is a list of argument symbols in the call:

```python
var_symbols
```

#### A Grammar from Calls

To get the grammar for a single function (`mine_function_grammar()`), we add a call to the function:

```python
class CallGrammarMiner(CallGrammarMiner):
    def function_symbol(self, function_name, grammar):
        return new_symbol(grammar, "<" + function_name + ">")

    def mine_function_grammar(self, function_name, grammar):
        arguments = self.carver.arguments(function_name)

        if self.log:
            print(function_name, arguments)

        var_grammar, var_symbols = self.mine_arguments_grammar(
            function_name, arguments, grammar)

        function_grammar = var_grammar
        function_symbol = self.function_symbol(function_name, grammar)

        if len(var_symbols) > 0 and var_symbols[0].find("-self") >= 0:
            # Method call
            function_grammar[function_symbol] = [
                var_symbols[0] + "." + function_name + "(" + ", ".join(var_symbols[1:]) + ")"]
        else:
            function_grammar[function_symbol] = [
                function_name + "(" + ", ".join(var_symbols) + ")"]

        if self.log:
            print(function_symbol, "::=", function_grammar[function_symbol])

        return function_grammar, function_symbol
```

```python
m = CallGrammarMiner(power_carver)
function_grammar, function_symbol = m.mine_function_grammar(
    "power", initial_grammar)
function_grammar
```

The additionally returned `function_symbol` holds the name of the function call just added:

```python
function_symbol
```

#### A Grammar from all Calls

Let us now repeat the above for all function calls seen during carving.  To this end, we simply iterate over all function calls seen:

```python
power_carver.called_functions()
```

```python
class CallGrammarMiner(CallGrammarMiner):
    def mine_call_grammar(self, function_list=None, qualified=False):
        grammar = self.initial_grammar()
        fn_list = function_list
        if function_list is None:
            fn_list = self.carver.called_functions(qualified=qualified)

        for function_name in fn_list:
            if function_list is None and (function_name.startswith("_") or function_name.startswith("<")):
                continue  # Internal function

            # Ignore errors with mined functions
            try:
                function_grammar, function_symbol = self.mine_function_grammar(
                    function_name, grammar)
            except:
                if function_list is not None:
                    raise

            if function_symbol not in grammar[self.CALL_SYMBOL]:
                grammar[self.CALL_SYMBOL].append(function_symbol)
            grammar.update(function_grammar)

        assert is_valid_grammar(grammar)
        return grammar
```

The method `mine_call_grammar()` is the one that clients can and should use – first for mining...

```python
m = CallGrammarMiner(power_carver)
power_grammar = m.mine_call_grammar()
power_grammar
```

...and then for fuzzing:

```python
power_fuzzer = GrammarCoverageFuzzer(power_grammar)
[power_fuzzer.fuzz() for i in range(5)]
```

With this, we have successfully extracted a grammar from a recorded execution; in contrast to "simple" carving, our grammar allows us to _recombine_ arguments and thus to fuzz at the API level.

## Fuzzing Web Functions

Let us now apply our grammar miner on a larger API – the `urlparse()` function we already encountered during carving.

```python
with CallCarver() as webbrowser_carver:
    webbrowser("https://www.fuzzingbook.org")
```

We can mine a grammar from the calls encountered:

```python
m = CallGrammarMiner(webbrowser_carver)
webbrowser_grammar = m.mine_call_grammar()
```

This is a rather large grammar:

```python
call_list = webbrowser_grammar['<call>']
len(call_list)
```

```python
print(call_list[:20])
```

Here's the rule for the `urlparse()` function:

```python
webbrowser_grammar["<urlparse>"]
```

Here are the arguments.

```python
webbrowser_grammar["<urlparse-url>"]
```

If we now apply a fuzzer on these rules, we systematically cover all variations of arguments seen, including, of course, combinations not seen during carving.  Again, we are fuzzing at the API level here.

```python
urlparse_fuzzer = GrammarCoverageFuzzer(
    webbrowser_grammar, start_symbol="<urlparse>")
for i in range(5):
    print(urlparse_fuzzer.fuzz())
```

Just as seen with carving, running tests at the API level is orders of magnitude faster than executing system tests.  Hence, this calls for means to fuzz at the method level:

```python
from urllib.parse import urlsplit
```

```python
from Timer import Timer
```

```python
with Timer() as urlsplit_timer:
    urlsplit('http://www.fuzzingbook.org/', 'http', True)
urlsplit_timer.elapsed_time()
```

```python
with Timer() as webbrowser_timer:
    webbrowser("http://www.fuzzingbook.org")
webbrowser_timer.elapsed_time()
```

```python
webbrowser_timer.elapsed_time() / urlsplit_timer.elapsed_time()
```

But then again, the caveats encountered during carving apply, notably the requirement to recreate the original function environment.  If we also alter or recombine arguments, we get the additional risk of _violating an implicit precondition_ – that is, invoking a function with arguments the function was never designed for.  Such _false alarms_, resulting from incorrect invocations rather than incorrect implementations, must then be identified (typically manually) and wed out (for instance, by altering or constraining the grammar).  The huge speed gains at the API level, however, may well justify this additional investment.

## Synopsis

This chapter provides means to _record and replay function calls_ during a system test.  Since individual function calls are much faster than a whole system run, such "carving" mechanisms have the potential to run tests much faster.

### Recording Calls

The `CallCarver` class records all calls occurring while it is active.  It is used in conjunction with a `with` clause:

```python
with CallCarver() as carver:
    y = my_sqrt(2)
    y = my_sqrt(4)
```

After execution, `called_functions()` lists the names of functions encountered:

```python
carver.called_functions()
```

The `arguments()` method lists the arguments recorded for a function.  This is a mapping of the function name to a list of lists of arguments; each argument is a pair (parameter name, value).

```python
carver.arguments('my_sqrt')
```

Complex arguments are properly serialized, such that they can be easily restored.

### Synthesizing Calls

While such recorded arguments already could be turned into arguments and calls, a much nicer alternative is to create a _grammar_ for recorded calls.  This allows synthesizing arbitrary _combinations_ of arguments, and also offers a base for further customization of calls.

The `CallGrammarMiner` class turns a list of carved executions into a grammar.

```python
my_sqrt_miner = CallGrammarMiner(carver)
my_sqrt_grammar = my_sqrt_miner.mine_call_grammar()
my_sqrt_grammar
```

This grammar can be used to synthesize calls.

```python
fuzzer = GrammarCoverageFuzzer(my_sqrt_grammar)
fuzzer.fuzz()
```

These calls can be executed in isolation, effectively extracting unit tests from system tests:

```python
eval(fuzzer.fuzz())
```

## Lessons Learned

* _Carving_ allows for effective replay of function calls recorded during a system test.
* A function call can be _orders of magnitude faster_ than a system invocation.
* _Serialization_ allows creating persistent representations of complex objects.
* Functions that heavily interact with their environment and/or access external resources are difficult to carve.
* From carved calls, one can produce API grammars that arbitrarily combine carved arguments.

## Next Steps

In the next chapter, we will discuss [how to reduce failure-inducing inputs](Reducer.ipynb).

## Background

Carving was invented by Elbaum et al. \cite{Elbaum2006} and originally implemented for Java.  In this chapter, we follow several of their design choices (including recording and serializing method arguments only).

The combination of carving and fuzzing at the API level is described in \cite{Kampmann2018}.

## Exercises

### Exercise 1: Carving for Regression Testing

So far, during carving, we only have looked into reproducing _calls_, but not into actually checking the _results_ of these calls.  This is important for _regression testing_ – i.e. checking whether a change to code does not impede existing functionality.  We can build this by recording not only _calls_, but also _return values_ – and then later compare whether the same calls result in the same values.  This may not work on all occasions; values that depend on time, randomness, or other external factors may be different.  Still, for functionality that abstracts from these details, checking that nothing has changed is an important part of testing.

Our aim is to design a class `ResultCarver` that extends `CallCarver` by recording both calls and return values.

In a first step, create a `traceit()` method that also tracks return values by extending the `traceit()` method.  The `traceit()` event type is `"return"` and the `arg` parameter is the returned value.  Here is a prototype that only prints out the returned values:

```python
class ResultCarver(CallCarver):
    def traceit(self, frame, event, arg):
        if event == "return":
            if self._log:
                print("Result:", arg)

        super().traceit(frame, event, arg)
        # Need to return traceit function such that it is invoked for return
        # events
        return self.traceit
```

```python
with ResultCarver(log=True) as result_carver:
    my_sqrt(2)
```

#### Part 1: Store function results

Extend the above code such that results are _stored_ in a way that associates them with the currently returning function (or method).  To this end, you need to keep track of the _current stack of called functions_.

**Solution.** Here's a solution, building on the above:

```python
class ResultCarver(CallCarver):
    def reset(self):
        super().reset()
        self._call_stack = []
        self._results = {}

    def add_result(self, function_name, arguments, result):
        key = simple_call_string(function_name, arguments)
        self._results[key] = result

    def traceit(self, frame, event, arg):
        if event == "call":
            code = frame.f_code
            function_name = code.co_name
            qualified_name = get_qualified_name(code)
            self._call_stack.append(
                (function_name, qualified_name, get_arguments(frame)))

        if event == "return":
            result = arg
            (function_name, qualified_name, arguments) = self._call_stack.pop()
            self.add_result(function_name, arguments, result)
            if function_name != qualified_name:
                self.add_result(qualified_name, arguments, result)
            if self._log:
                print(
                    simple_call_string(
                        function_name,
                        arguments),
                    "=",
                    result)

        # Keep on processing current calls
        super().traceit(frame, event, arg)

        # Need to return traceit function such that it is invoked for return
        # events
        return self.traceit
```

```python
with ResultCarver(log=True) as result_carver:
    my_sqrt(2)
result_carver._results
```

#### Part 2: Access results

  Give it a method `result()` that returns the value recorded for that particular function name and result:

```python
class ResultCarver(CallCarver):
    def result(self, function_name, argument):
        """Returns the result recorded for function_name(argument"""
```

**Solution.** This is mostly done in the code for part 1:

```python
class ResultCarver(ResultCarver):
    def result(self, function_name, argument):
        key = simple_call_string(function_name, arguments)
        return self._results[key]
```

#### Part 3: Produce assertions

For the functions called during `webbrowser()` execution, create a set of _assertions_ that check whether the result returned is still the same.  Test this for `urllib.parse.urlparse()`.

**Solution.** Not too hard now:

```python
# ignore
import sys
```

```python
if sys.version_info >= (3, 11):  # Requires Python 3.11 or later
    with ResultCarver() as webbrowser_result_carver:
        webbrowser("https://www.cispa.de")
```

```python
if sys.version_info >= (3, 11):
    for function_name in ["urllib.parse.urlparse"]:
        for arguments in webbrowser_result_carver.arguments(function_name):
            try:
                call = call_string(function_name, arguments)
                result = webbrowser_result_carver.result(function_name, arguments)
                print("assert", call, "==", call_value(result))
            except Exception:
                continue
```

We can run these assertions:

```python
from urllib.parse import SplitResult, ParseResult, urlparse, urlsplit
```

```python
if sys.version_info >= (3, 11):
    assert urlparse(
        url='http://www.cispa.de',
        scheme='',
        allow_fragments=True) == ParseResult(
            scheme='http',
            netloc='www.cispa.de',
            path='',
            params='',
            query='',
        fragment='')
    assert urlsplit(
        url='http://www.cispa.de',
        scheme='',
        allow_fragments=True) == SplitResult(
            scheme='http',
            netloc='www.cispa.de',
            path='',
            query='',
        fragment='')
```

We can now add these carved tests to a _regression test suite_ which would be run after every change to ensure that the functionality of `urlparse()` and `urlsplit()` is not changed.

### Exercise 2: Abstracting Arguments

When mining an API grammar from executions, set up an abstraction scheme to widen the range of arguments to be used during testing.  If the values for an argument, all conform to some type `T`. abstract it into `<T>`.  For instance, if calls to `foo(1)`, `foo(2)`, `foo(3)` have been seen, the grammar should abstract its calls into `foo(<int>)`, with `<int>` being appropriately defined.

Do this for a number of common types: integers, positive numbers, floating-point numbers, host names, URLs, mail addresses, and more.

**Solution.** Left to the reader.