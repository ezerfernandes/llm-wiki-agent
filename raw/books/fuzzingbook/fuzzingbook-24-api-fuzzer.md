# Fuzzing APIs

So far, we have always generated _system input_, i.e. data that the program as a whole obtains via its input channels.  However, we can also generate inputs that go directly into individual functions, gaining flexibility and speed in the process.  In this chapter, we explore the use of grammars to synthesize code for function calls, which allows you to generate _program code that very efficiently invokes functions directly._

```python
from bookutils import YouTubeVideo
YouTubeVideo('CC1VvOGkzm8')
```

**Prerequisites**

* You have to know how grammar fuzzing work, e.g. from the [chapter on grammars](Grammars.ipynb).
* We make use of _generator functions_, as discussed in the [chapter on fuzzing with generators](GeneratorGrammarFuzzer.ipynb).
* We make use of probabilities, as discussed in the [chapter on fuzzing with probabilities](ProbabilisticGrammarFuzzer.ipynb).

## Synopsis
<!-- Automatically generated. Do not edit. -->

To [use the code provided in this chapter](Importing.ipynb), write

```python
>>> from fuzzingbook.APIFuzzer import <identifier>
```

and then make use of the following features.

This chapter provides *grammar constructors* that are useful for generating _function calls_.

The grammars are [probabilistic](ProbabilisticGrammarFuzzer.ipynb) and make use of [generators](GeneratorGrammarFuzzer.ipynb), so use `ProbabilisticGeneratorGrammarFuzzer` as a producer.

```python
>>> from GeneratorGrammarFuzzer import ProbabilisticGeneratorGrammarFuzzer
```
`INT_GRAMMAR`, `FLOAT_GRAMMAR`, `ASCII_STRING_GRAMMAR` produce integers, floats, and strings, respectively:

```python
>>> fuzzer = ProbabilisticGeneratorGrammarFuzzer(INT_GRAMMAR)
>>> [fuzzer.fuzz() for i in range(10)]
['-51', '9', '0', '0', '0', '0', '32', '0', '0', '0']
>>> fuzzer = ProbabilisticGeneratorGrammarFuzzer(FLOAT_GRAMMAR)
>>> [fuzzer.fuzz() for i in range(10)]
['0e0',
 '-9.43e34',
 '-7.3282e0',
 '-9.5e-9',
 '0',
 '-30.840386e-5',
 '3',
 '-4.1e0',
 '-9.7',
 '413']
>>> fuzzer = ProbabilisticGeneratorGrammarFuzzer(ASCII_STRING_GRAMMAR)
>>> [fuzzer.fuzz() for i in range(10)]
['"#vYV*t@I%KNTT[q~}&-v+[zAzj[X-z|RzC$(g$Br]1tC\':5<F-"',
 '""',
 '"^S/"',
 '"y)QDs_9"',
 '")dY~?WYqMh,bwn3\\"A!02Pk`gx"',
 '"01n|(dd$-d.sx\\"83\\"h/]qx)d9LPNdrk$}$4t3zhC.%3VY@AZZ0wCs2 N"',
 '"D\\6\\xgw#TQ}$\'3"',
 '"LaM{"',
 '"\\"ux\'1H!=%;2T$.=l"',
 '"=vkiV~w.Ypt,?JwcEr}Moc>!5<U+DdYAup\\"N 0V?h3x~jFN3"']
```
`int_grammar_with_range(start, end)` produces an integer grammar with values `N` such that `start <= N <= end`:

```python
>>> int_grammar = int_grammar_with_range(100, 200)
>>> fuzzer = ProbabilisticGeneratorGrammarFuzzer(int_grammar)
>>> [fuzzer.fuzz() for i in range(10)]
['154', '149', '185', '117', '182', '154', '131', '194', '147', '192']
```
`float_grammar_with_range(start, end)` produces a floating-number grammar with values `N` such that `start <= N <= end`.

```python
>>> float_grammar = float_grammar_with_range(100, 200)
>>> fuzzer = ProbabilisticGeneratorGrammarFuzzer(float_grammar)
>>> [fuzzer.fuzz() for i in range(10)]
['121.8092479227325',
 '187.18037169119634',
 '127.9576486784452',
 '125.47768739781723',
 '151.8091820472274',
 '117.864410860742',
 '187.50918008379483',
 '119.29335112884749',
 '149.2637029583114',
 '126.61818995939146']
```
All such values can be immediately used for testing function calls:

```python
>>> from math import sqrt
>>> fuzzer = ProbabilisticGeneratorGrammarFuzzer(int_grammar)
>>> call = "sqrt(" + fuzzer.fuzz() + ")"
>>> call
'sqrt(143)'
>>> eval(call)
11.958260743101398
```
These grammars can also be composed to form more complex grammars. `list_grammar(object_grammar)` returns a grammar that produces lists of objects as defined by `object_grammar`.

```python
>>> int_list_grammar = list_grammar(int_grammar)
>>> fuzzer = ProbabilisticGeneratorGrammarFuzzer(int_list_grammar)
>>> [fuzzer.fuzz() for i in range(5)]
['[118, 111, 188, 137, 129]',
 '[170, 172]',
 '[171, 161, 117, 191, 175, 183, 164]',
 '[189]',
 '[129, 110, 178]']
>>> some_list = eval(fuzzer.fuzz())
>>> some_list
[172, 120, 106, 192, 124, 191, 161, 100, 117]
>>> len(some_list)
9
```
In a similar vein, we can construct arbitrary further data types for testing individual functions programmatically.

## Fuzzing a Function

Let us start with our first problem: How do we fuzz a given function?  For an interpreted language like Python, this is pretty straight-forward.  All we need to do is to generate _calls_ to the function(s) we want to test.  This is something we can easily do with a grammar.

As an example, consider the `urlparse()` function from the Python library.  `urlparse()` takes a URL and decomposes it into its individual components.

```python
import bookutils.setup
```

```python
from urllib.parse import urlparse
```

```python
urlparse('https://www.fuzzingbook.com/html/APIFuzzer.html')
```

You see how the individual elements of the URL – the _scheme_ (`"http"`), the _network location_ (`"www.fuzzingbook.com"`), or the path (`"//html/APIFuzzer.html"`) are all properly identified.  Other elements (like `params`, `query`, or `fragment`) are empty, because they were not part of our input.

To test `urlparse()`, we'd want to feed it a large set of different URLs.  We can obtain these from the URL grammar we had defined in the ["Grammars"](Grammars.ipynb) chapter.

```python
from Grammars import URL_GRAMMAR, is_valid_grammar, START_SYMBOL
from Grammars import opts, extend_grammar, Grammar
from GrammarFuzzer import GrammarFuzzer
```

```python
url_fuzzer = GrammarFuzzer(URL_GRAMMAR)
```

```python
for i in range(10):
    url = url_fuzzer.fuzz()
    print(urlparse(url))
```

This way, we can easily test any Python function – by setting up a scaffold that runs it.  How would we proceed, though, if we wanted to have a test that can be re-run again and again, without having to generate new calls every time?

## Synthesizing Code

The "scaffolding" method, as sketched above, has an important downside: It couples test generation and test execution into a single unit, disallowing running both at different times, or for different languages.  To decouple the two, we take another approach: Rather than generating inputs and immediately feeding this input into a function, we _synthesize code_ instead that invokes functions with a given input.

For instance, if we generate the string

```python
call = "urlparse('http://www.cispa.de/')"
```

we can execute this string as a whole (and thus run the test) at any time:

```python
eval(call)
```

To systematically generate such calls, we can again use a grammar:

```python
URLPARSE_GRAMMAR: Grammar = {
    "<call>":
        ['urlparse("<url>")']
}

# Import definitions from URL_GRAMMAR
URLPARSE_GRAMMAR.update(URL_GRAMMAR)
URLPARSE_GRAMMAR["<start>"] = ["<call>"]

assert is_valid_grammar(URLPARSE_GRAMMAR)
```

This grammar creates calls in the form `urlparse(<url>)`, where `<url>` comes from the "imported" URL grammar.  The idea is to create many of these calls and to feed them into the Python interpreter.

```python
URLPARSE_GRAMMAR
```

We can now use this grammar for fuzzing and synthesizing calls to `urlparse)`:

```python
urlparse_fuzzer = GrammarFuzzer(URLPARSE_GRAMMAR)
urlparse_fuzzer.fuzz()
```

Just as above, we can immediately execute these calls.  To better see what is happening, we define a small helper function:

```python
# Call function_name(arg[0], arg[1], ...) as a string
def do_call(call_string):
    print(call_string)
    result = eval(call_string)
    print("\t= " + repr(result))
    return result
```

```python
call = urlparse_fuzzer.fuzz()
do_call(call)
```

If `urlparse()` were a C function, for instance, we could embed its call into some (also generated) C function:

```python
URLPARSE_C_GRAMMAR: Grammar = {
    "<cfile>": ["<cheader><cfunction>"],
    "<cheader>": ['#include "urlparse.h"\n\n'],
    "<cfunction>": ["void test() {\n<calls>}\n"],
    "<calls>": ["<call>", "<calls><call>"],
    "<call>": ['    urlparse("<url>");\n']
}
```

```python
URLPARSE_C_GRAMMAR.update(URL_GRAMMAR)
```

```python
URLPARSE_C_GRAMMAR["<start>"] = ["<cfile>"]
```

```python
assert is_valid_grammar(URLPARSE_C_GRAMMAR)
```

```python
urlparse_fuzzer = GrammarFuzzer(URLPARSE_C_GRAMMAR)
print(urlparse_fuzzer.fuzz())
```

## Synthesizing Oracles

In our `urlparse()` example, both the Python as well as the C variant only check for _generic_ errors in `urlparse()`; that is, they only detect fatal errors and exceptions.  For a full test, we need to set up a specific *oracle* as well that checks whether the result is valid.

Our plan is to check whether specific parts of the URL reappear in the result – that is, if the scheme is `http:`, then the `ParseResult` returned should also contain a `http:` scheme.  As discussed in the [chapter on fuzzing with generators](GeneratorGrammarFuzzer.ipynb), equalities of strings such as `http:` across two symbols cannot be expressed in a context-free grammar.  We can, however, use a _generator function_ (also introduced in the [chapter on fuzzing with generators](GeneratorGrammarFuzzer.ipynb)) to automatically enforce such equalities.

Here is an example.  Invoking `geturl()` on a `urlparse()` result should return the URL as originally passed to `urlparse()`.

```python
from GeneratorGrammarFuzzer import GeneratorGrammarFuzzer, ProbabilisticGeneratorGrammarFuzzer
```

```python
URLPARSE_ORACLE_GRAMMAR: Grammar = extend_grammar(URLPARSE_GRAMMAR,
{
     "<call>": [("assert urlparse('<url>').geturl() == '<url>'",
                 opts(post=lambda url_1, url_2: [None, url_1]))]
})
```

```python
urlparse_oracle_fuzzer = GeneratorGrammarFuzzer(URLPARSE_ORACLE_GRAMMAR)
test = urlparse_oracle_fuzzer.fuzz()
print(test)
```

```python
exec(test)
```

In a similar way, we can also check individual components of the result:

```python
URLPARSE_ORACLE_GRAMMAR: Grammar = extend_grammar(URLPARSE_GRAMMAR,
{
     "<call>": [("result = urlparse('<scheme>://<host><path>?<params>')\n"
                 # + "print(result)\n"
                 + "assert result.scheme == '<scheme>'\n"
                 + "assert result.netloc == '<host>'\n"
                 + "assert result.path == '<path>'\n"
                 + "assert result.query == '<params>'",
                 opts(post=lambda scheme_1, authority_1, path_1, params_1,
                      scheme_2, authority_2, path_2, params_2:
                      [None, None, None, None,
                       scheme_1, authority_1, path_1, params_1]))]
})

# Get rid of unused symbols
del URLPARSE_ORACLE_GRAMMAR["<url>"]
del URLPARSE_ORACLE_GRAMMAR["<query>"]
del URLPARSE_ORACLE_GRAMMAR["<authority>"]
del URLPARSE_ORACLE_GRAMMAR["<userinfo>"]
del URLPARSE_ORACLE_GRAMMAR["<port>"]
```

```python
urlparse_oracle_fuzzer = GeneratorGrammarFuzzer(URLPARSE_ORACLE_GRAMMAR)
test = urlparse_oracle_fuzzer.fuzz()
print(test)
```

```python
exec(test)
```

The use of generator functions may feel a bit cumbersome.  Indeed, if we uniquely stick to Python, we could also create a _unit test_ that directly invokes the fuzzer to generate individual parts:

```python
def fuzzed_url_element(symbol):
    return GrammarFuzzer(URLPARSE_GRAMMAR, start_symbol=symbol).fuzz()
```

```python
scheme = fuzzed_url_element("<scheme>")
authority = fuzzed_url_element("<authority>")
path = fuzzed_url_element("<path>")
query = fuzzed_url_element("<params>")
url = "%s://%s%s?%s" % (scheme, authority, path, query)
result = urlparse(url)
# print(result)
assert result.geturl() == url
assert result.scheme == scheme
assert result.path == path
assert result.query == query
```

Using such a unit test makes it easier to express oracles.  However, we lose the ability to systematically cover individual URL elements and alternatives as with [`GrammarCoverageFuzzer`](GrammarCoverageFuzzer.ipynb) as well as the ability to guide generation towards specific elements as with [`ProbabilisticGrammarFuzzer`](ProbabilisticGrammarFuzzer.ipynb).  Furthermore, a grammar allows us to generate tests for arbitrary programming languages and APIs.

## Synthesizing Data

For `urlparse()`, we have used a very specific grammar for creating a very specific argument.  Many functions take basic data types as (some) arguments, though; we therefore define grammars that generate precisely those arguments.  Even better, we can define functions that _generate_ grammars tailored towards our specific needs, returning values in a particular range, for instance.

### Integers

We introduce a simple grammar to produce integers.

```python
from Grammars import convert_ebnf_grammar, crange
```

```python
from ProbabilisticGrammarFuzzer import ProbabilisticGrammarFuzzer
```

```python
INT_EBNF_GRAMMAR: Grammar = {
    "<start>": ["<int>"],
    "<int>": ["<_int>"],
    "<_int>": ["(-)?<leaddigit><digit>*", "0"],
    "<leaddigit>": crange('1', '9'),
    "<digit>": crange('0', '9')
}

assert is_valid_grammar(INT_EBNF_GRAMMAR)
```

```python
INT_GRAMMAR = convert_ebnf_grammar(INT_EBNF_GRAMMAR)
INT_GRAMMAR
```

```python
int_fuzzer = GrammarFuzzer(INT_GRAMMAR)
print([int_fuzzer.fuzz() for i in range(10)])
```

If we need integers in a specific range, we can add a generator function that does right that:

```python
from Grammars import set_opts
```

```python
import random
```

```python
def int_grammar_with_range(start, end):
    int_grammar = extend_grammar(INT_GRAMMAR)
    set_opts(int_grammar, "<int>", "<_int>",
        opts(pre=lambda: random.randint(start, end)))
    return int_grammar
```

```python
int_fuzzer = GeneratorGrammarFuzzer(int_grammar_with_range(900, 1000))
[int_fuzzer.fuzz() for i in range(10)]
```

### Floats

The grammar for floating-point values closely resembles the integer grammar.

```python
FLOAT_EBNF_GRAMMAR: Grammar = {
    "<start>": ["<float>"],
    "<float>": [("<_float>", opts(prob=0.9)), "inf", "NaN"],
    "<_float>": ["<int>(.<digit>+)?<exp>?"],
    "<exp>": ["e<int>"]
}
FLOAT_EBNF_GRAMMAR.update(INT_EBNF_GRAMMAR)
FLOAT_EBNF_GRAMMAR["<start>"] = ["<float>"]

assert is_valid_grammar(FLOAT_EBNF_GRAMMAR)
```

```python
FLOAT_GRAMMAR = convert_ebnf_grammar(FLOAT_EBNF_GRAMMAR)
FLOAT_GRAMMAR
```

```python
float_fuzzer = ProbabilisticGrammarFuzzer(FLOAT_GRAMMAR)
print([float_fuzzer.fuzz() for i in range(10)])
```

```python
def float_grammar_with_range(start, end):
    float_grammar = extend_grammar(FLOAT_GRAMMAR)
    set_opts(float_grammar, "<float>", "<_float>", opts(
        pre=lambda: start + random.random() * (end - start)))
    return float_grammar
```

```python
float_fuzzer = ProbabilisticGeneratorGrammarFuzzer(
    float_grammar_with_range(900.0, 900.9))
[float_fuzzer.fuzz() for i in range(10)]
```

### Strings

Finally, we introduce a grammar for producing strings.

```python
ASCII_STRING_EBNF_GRAMMAR: Grammar = {
    "<start>": ["<ascii-string>"],
    "<ascii-string>": ['"<ascii-chars>"'],
    "<ascii-chars>": [
        ("", opts(prob=0.05)),
        "<ascii-chars><ascii-char>"
    ],
    "<ascii-char>": crange(" ", "!") + [r'\"'] + crange("#", "~")
}

assert is_valid_grammar(ASCII_STRING_EBNF_GRAMMAR)
```

```python
ASCII_STRING_GRAMMAR = convert_ebnf_grammar(ASCII_STRING_EBNF_GRAMMAR)
```

```python
string_fuzzer = ProbabilisticGrammarFuzzer(ASCII_STRING_GRAMMAR)
print([string_fuzzer.fuzz() for i in range(10)])
```

## Synthesizing Composite Data

From basic data, as discussed above, we can also produce _composite data_ in data structures such as sets or lists.  We illustrate such generation on lists.

### Lists

```python
LIST_EBNF_GRAMMAR: Grammar = {
    "<start>": ["<list>"],
    "<list>": [
        ("[]", opts(prob=0.05)),
        "[<list-objects>]"
    ],
    "<list-objects>": [
        ("<list-object>", opts(prob=0.2)),
        "<list-object>, <list-objects>"
    ],
    "<list-object>": ["0"],
}

assert is_valid_grammar(LIST_EBNF_GRAMMAR)
```

```python
LIST_GRAMMAR = convert_ebnf_grammar(LIST_EBNF_GRAMMAR)
```

Our list generator takes a grammar that produces objects; it then instantiates a list grammar with the objects from these grammars.

```python
def list_grammar(object_grammar, list_object_symbol=None):
    obj_list_grammar = extend_grammar(LIST_GRAMMAR)
    if list_object_symbol is None:
        # Default: Use the first expansion of <start> as list symbol
        list_object_symbol = object_grammar[START_SYMBOL][0]

    obj_list_grammar.update(object_grammar)
    obj_list_grammar[START_SYMBOL] = ["<list>"]
    obj_list_grammar["<list-object>"] = [list_object_symbol]

    assert is_valid_grammar(obj_list_grammar)

    return obj_list_grammar
```

```python
int_list_fuzzer = ProbabilisticGrammarFuzzer(list_grammar(INT_GRAMMAR))
[int_list_fuzzer.fuzz() for i in range(10)]
```

```python
string_list_fuzzer = ProbabilisticGrammarFuzzer(
    list_grammar(ASCII_STRING_GRAMMAR))
[string_list_fuzzer.fuzz() for i in range(10)]
```

```python
float_list_fuzzer = ProbabilisticGeneratorGrammarFuzzer(list_grammar(
    float_grammar_with_range(900.0, 900.9)))
[float_list_fuzzer.fuzz() for i in range(10)]
```

Generators for dictionaries, sets, etc. can be defined in a similar fashion.  By plugging together grammar generators, we can produce data structures with arbitrary elements.

## Synopsis

This chapter provides *grammar constructors* that are useful for generating _function calls_.

The grammars are [probabilistic](ProbabilisticGrammarFuzzer.ipynb) and make use of [generators](GeneratorGrammarFuzzer.ipynb), so use `ProbabilisticGeneratorGrammarFuzzer` as a producer.

```python
from GeneratorGrammarFuzzer import ProbabilisticGeneratorGrammarFuzzer
```

`INT_GRAMMAR`, `FLOAT_GRAMMAR`, `ASCII_STRING_GRAMMAR` produce integers, floats, and strings, respectively:

```python
fuzzer = ProbabilisticGeneratorGrammarFuzzer(INT_GRAMMAR)
[fuzzer.fuzz() for i in range(10)]
```

```python
fuzzer = ProbabilisticGeneratorGrammarFuzzer(FLOAT_GRAMMAR)
[fuzzer.fuzz() for i in range(10)]
```

```python
fuzzer = ProbabilisticGeneratorGrammarFuzzer(ASCII_STRING_GRAMMAR)
[fuzzer.fuzz() for i in range(10)]
```

`int_grammar_with_range(start, end)` produces an integer grammar with values `N` such that `start <= N <= end`:

```python
int_grammar = int_grammar_with_range(100, 200)
fuzzer = ProbabilisticGeneratorGrammarFuzzer(int_grammar)
[fuzzer.fuzz() for i in range(10)]
```

`float_grammar_with_range(start, end)` produces a floating-number grammar with values `N` such that `start <= N <= end`.

```python
float_grammar = float_grammar_with_range(100, 200)
fuzzer = ProbabilisticGeneratorGrammarFuzzer(float_grammar)
[fuzzer.fuzz() for i in range(10)]
```

All such values can be immediately used for testing function calls:

```python
from math import sqrt
```

```python
fuzzer = ProbabilisticGeneratorGrammarFuzzer(int_grammar)
call = "sqrt(" + fuzzer.fuzz() + ")"
call
```

```python
eval(call)
```

These grammars can also be composed to form more complex grammars. `list_grammar(object_grammar)` returns a grammar that produces lists of objects as defined by `object_grammar`.

```python
int_list_grammar = list_grammar(int_grammar)
fuzzer = ProbabilisticGeneratorGrammarFuzzer(int_list_grammar)
[fuzzer.fuzz() for i in range(5)]
```

```python
some_list = eval(fuzzer.fuzz())
```

```python
some_list
```

```python
len(some_list)
```

In a similar vein, we can construct arbitrary further data types for testing individual functions programmatically.

## Lessons Learned

* To fuzz individual functions, one can easily set up grammars that produce function calls.
* Fuzzing at the API level can be much faster than fuzzing at the system level, but brings the risk of false alarms by violating implicit preconditions.

## Next Steps

This chapter was all about manually writing test and controlling which data gets generated.  [In the next chapter](Carver.ipynb), we will introduce a much higher level of automation:

* _Carving_ automatically records function calls and arguments from program executions.
* We can turn these into _grammars_, allowing to test these functions with various combinations of recorded values.

With these techniques, we automatically obtain grammars that already invoke functions in application contexts, making our work of specifying them much easier.

## Background

The idea of using generator functions to generate input structures was first explored in QuickCheck \cite{Claessen2000}.   A very nice implementation for Python is the [hypothesis package](https://hypothesis.readthedocs.io/en/latest/) which allows writing and combining data structure generators for testing APIs.

## Exercises

The exercises for this chapter combine the above techniques with fuzzing techniques introduced earlier.

### Exercise 1: Deep Arguments

In the example generating oracles for `urlparse()`, important elements such as `authority` or `port` are not checked.  Enrich `URLPARSE_ORACLE_GRAMMAR` with post-expansion functions that store the generated elements in a symbol table, such that they can be accessed when generating the assertions.

**Solution.** Left to the reader.

### Exercise 2: Covering Argument Combinations

In the chapter on [configuration testing](ConfigurationFuzzer.ipynb), we also discussed _combinatorial testing_ – that is, systematic coverage of _sets_ of configuration elements.  Implement a scheme that by changing the grammar, allows all _pairs_ of argument values to be covered.

**Solution.** Left to the reader.

### Exercise 3: Mutating Arguments

To widen the range of arguments to be used during testing, apply the _mutation schemes_ introduced in [mutation fuzzing](MutationFuzzer.ipynb) – for instance, flip individual bytes or delete characters from strings.  Apply this either during grammar inference or as a separate step when invoking functions.

**Solution.** Left to the reader.