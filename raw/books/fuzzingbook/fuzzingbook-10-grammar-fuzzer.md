# Efficient Grammar Fuzzing

In the [chapter on grammars](Grammars.ipynb), we have seen how to use _grammars_ for very effective and efficient testing.  In this chapter, we refine the previous _string-based_ algorithm into a _tree-based_ algorithm, which is much faster and allows for much more control over the production of fuzz inputs.

The algorithm in this chapter serves as a foundation for several more techniques; this chapter thus is a "hub" in the book.

```python
from bookutils import YouTubeVideo
YouTubeVideo('Ohl8TLcLl3A')
```

**Prerequisites**

* You should know how grammar-based fuzzing works, e.g. from the [chapter on grammars](Grammars.ipynb).

## Synopsis
<!-- Automatically generated. Do not edit. -->

To [use the code provided in this chapter](Importing.ipynb), write

```python
>>> from fuzzingbook.GrammarFuzzer import <identifier>
```

and then make use of the following features.


### Efficient Grammar Fuzzing

This chapter introduces `GrammarFuzzer`, an efficient grammar fuzzer that takes a grammar to produce syntactically valid input strings.  Here's a typical usage:

```python
>>> from Grammars import US_PHONE_GRAMMAR
>>> phone_fuzzer = GrammarFuzzer(US_PHONE_GRAMMAR)
>>> phone_fuzzer.fuzz()
'(236)844-1154'
```
The `GrammarFuzzer` constructor takes a number of keyword arguments to control its behavior.  `start_symbol`, for instance, allows setting the symbol that expansion starts with (instead of `<start>`):

```python
>>> area_fuzzer = GrammarFuzzer(US_PHONE_GRAMMAR, start_symbol='<area>')
>>> area_fuzzer.fuzz()
'996'
```
Here's how to parameterize the `GrammarFuzzer` constructor:

```python
Produce strings from `grammar`, starting with `start_symbol`.
If `min_nonterminals` or `max_nonterminals` is given, use them as limits 
for the number of nonterminals produced.  
If `disp` is set, display the intermediate derivation trees.
If `log` is set, show intermediate steps as text on standard output.

```
![](PICS/GrammarFuzzer-synopsis-1.svg)

### Derivation Trees

Internally, `GrammarFuzzer` makes use of [derivation trees](#Derivation-Trees), which it expands step by step.  After producing a string, the tree produced can be accessed in the `derivation_tree` attribute.

```python
>>> display_tree(phone_fuzzer.derivation_tree)
```
![](PICS/GrammarFuzzer-synopsis-2.svg)

In the internal representation of a derivation tree, a _node_ is a pair (`symbol`, `children`).  For nonterminals, `symbol` is the symbol that is being expanded, and `children` is a list of further nodes.  For terminals, `symbol` is the terminal string, and `children` is empty.

```python
>>> phone_fuzzer.derivation_tree
('<start>',
 [('<phone-number>',
   [('(', []),
    ('<area>',
     [('<lead-digit>', [('2', [])]),
      ('<digit>', [('3', [])]),
      ('<digit>', [('6', [])])]),
    (')', []),
    ('<exchange>',
     [('<lead-digit>', [('8', [])]),
      ('<digit>', [('4', [])]),
      ('<digit>', [('4', [])])]),
    ('-', []),
    ('<line>',
     [('<digit>', [('1', [])]),
      ('<digit>', [('1', [])]),
      ('<digit>', [('5', [])]),
      ('<digit>', [('4', [])])])])])
```
The chapter contains various helpers to work with derivation trees, including visualization tools – notably, `display_tree()`, above.



## An Insufficient Algorithm

In the [previous chapter](Grammars.ipynb), we have introduced the `simple_grammar_fuzzer()` function which takes a grammar and automatically produces a syntactically valid string from it.  However, `simple_grammar_fuzzer()` is just what its name suggests – simple.  To illustrate the problem, let us get back to the `expr_grammar` we created from `EXPR_GRAMMAR_BNF` in the [chapter on grammars](Grammars.ipynb):

```python
import bookutils.setup
```

```python
from bookutils import quiz
```

```python
from typing import Tuple, List, Optional, Any, Union, Set, Callable, Dict
```

```python
from bookutils import unicode_escape
```

```python
from Grammars import EXPR_EBNF_GRAMMAR, convert_ebnf_grammar, Grammar, Expansion
from Grammars import simple_grammar_fuzzer, is_valid_grammar, exp_string
```

```python
expr_grammar = convert_ebnf_grammar(EXPR_EBNF_GRAMMAR)
expr_grammar
```

`expr_grammar` has an interesting property.  If we feed it into `simple_grammar_fuzzer()`, the function gets stuck:

```python
from ExpectError import ExpectTimeout
```

```python
with ExpectTimeout(1):
    simple_grammar_fuzzer(grammar=expr_grammar, max_nonterminals=3)
```

Why is that so?  Have a look at the grammar; remember what you know about `simple_grammar_fuzzer()`; and run `simple_grammar_fuzzer()` with `log=true` argument to see the expansions.

```python
quiz("Why does `simple_grammar_fuzzer()` hang?",
     [
         "It produces an infinite number of additions",
         "It produces an infinite number of digits",
         "It produces an infinite number of parentheses",
         "It produces an infinite number of signs",
     ], '(3 * 3 * 3) ** (3 / (3 * 3))')
```

Indeed! The problem is in this rule:

```python
expr_grammar['<factor>']
```

Here, any choice except for `(expr)` increases the number of symbols, even if only temporary.  Since we place a hard limit on the number of symbols to expand, the only choice left for expanding `<factor>` is `(<expr>)`, which leads to an _infinite addition of parentheses._

The problem of potentially infinite expansion is only one of the problems with `simple_grammar_fuzzer()`.  More problems include:

1. *It is inefficient*.  With each iteration, this fuzzer would go search the string produced so far for symbols to expand.  This becomes inefficient as the production string grows.

2. *It is hard to control.*  Even while limiting the number of symbols, it is still possible to obtain very long strings – and even infinitely long ones, as discussed above.

Let us illustrate both problems by plotting the time required for strings of different lengths.

```python
from Grammars import simple_grammar_fuzzer
```

```python
from Grammars import START_SYMBOL, EXPR_GRAMMAR, URL_GRAMMAR, CGI_GRAMMAR
```

```python
from Grammars import RE_NONTERMINAL, nonterminals, is_nonterminal
```

```python
from Timer import Timer
```

```python
trials = 50
xs = []
ys = []
for i in range(trials):
    with Timer() as t:
        s = simple_grammar_fuzzer(EXPR_GRAMMAR, max_nonterminals=15)
    xs.append(len(s))
    ys.append(t.elapsed_time())
    print(i, end=" ")
print()
```

```python
average_time = sum(ys) / trials
print("Average time:", average_time)
```

```python
%matplotlib inline

import matplotlib.pyplot as plt
plt.scatter(xs, ys)
plt.title('Time required for generating an output');
```

We see that (1) the time needed to generate an output increases quadratically with the length of that output, and that (2) a large portion of the produced outputs are tens of thousands of characters long.

To address these problems, we need a _smarter algorithm_ – one that is more efficient, that gets us better control over expansions, and that is able to foresee in `expr_grammar` that the `(expr)` alternative yields a potentially infinite expansion, in contrast to the other two.

## Derivation Trees

To both obtain a more efficient algorithm _and_ exercise better control over expansions, we will use a special representation for the strings that our grammar produces.  The general idea is to use a *tree* structure that will be subsequently expanded – a so-called *derivation tree*.  This representation allows us to always keep track of our expansion status – answering questions such as which elements have been expanded into which others, and which symbols still need to be expanded.  Furthermore, adding new elements to a tree is far more efficient than replacing strings again and again.

Like other trees used in programming, a derivation tree (also known as *parse tree* or *concrete syntax tree*) consists of *nodes* which have other nodes (called *child nodes*) as their *children*.  The tree starts with one node that has no parent; this is called the *root node*; a node without children is called a *leaf*.

The grammar expansion process with derivation trees is illustrated in the following steps, using the arithmetic grammar [from
the chapter on grammars](Grammars.ipynb).  We start with a single node as root of the tree, representing the *start symbol* – in our case `<start>`.

```python
# ignore
from graphviz import Digraph
```

```python
# ignore
tree = Digraph("root")
tree.attr('node', shape='plain')
tree.node(r"\<start\>")
```

```python
# ignore
tree
```

To expand the tree, we traverse it, searching for a nonterminal symbol $S$ without children.  $S$ thus is a symbol that still has to be expanded.  We then chose an expansion for $S$ from the grammar.  Then, we add the expansion as a new child of $S$.  For our start symbol `<start>`, the only expansion is `<expr>`, so we add it as a child.

```python
# ignore
tree.edge(r"\<start\>", r"\<expr\>")
```

```python
# ignore
tree
```

To construct the produced string from a derivation tree, we traverse the tree in order and collect the symbols at the leaves of the tree.  In the case above, we obtain the string `"<expr>"`.

To further expand the tree, we choose another symbol to expand, and add its expansion as new children.  This would get us the `<expr>` symbol, which gets expanded into `<expr> + <term>`, adding three children.

```python
# ignore
tree.edge(r"\<expr\>", r"\<expr\> ")
tree.edge(r"\<expr\>", r"+")
tree.edge(r"\<expr\>", r"\<term\>")
```

```python
# ignore
tree
```

We repeat the expansion until there are no symbols left to expand:

```python
# ignore
tree.edge(r"\<expr\> ", r"\<term\> ")
tree.edge(r"\<term\> ", r"\<factor\> ")
tree.edge(r"\<factor\> ", r"\<integer\> ")
tree.edge(r"\<integer\> ", r"\<digit\> ")
tree.edge(r"\<digit\> ", r"2 ")

tree.edge(r"\<term\>", r"\<factor\>")
tree.edge(r"\<factor\>", r"\<integer\>")
tree.edge(r"\<integer\>", r"\<digit\>")
tree.edge(r"\<digit\>", r"2")
```

```python
# ignore
tree
```

We now have a representation for the string `2 + 2`.  In contrast to the string alone, though, the derivation tree records _the entire structure_ (and production history, or _derivation_ history) of the produced string.  It also allows for simple comparison and manipulation – say, replacing one subtree (substructure) against another.

## Representing Derivation Trees

To represent a derivation tree in Python, we use the following format.  A node is a pair

```python
(SYMBOL_NAME, CHILDREN)
```

where `SYMBOL_NAME` is a string representing the node (i.e. `"<start>"` or `"+"`) and `CHILDREN` is a list of children nodes.

`CHILDREN` can take some special values:

1. `None` as a placeholder for future expansion.  This means that the node is a *nonterminal symbol* that should be expanded further.
2. `[]` (i.e., the empty list) to indicate _no_ children.  This means that the node is a *terminal symbol* that can no longer be expanded.

The type `DerivationTree` captures this very structure. (`Any` should actually read `DerivationTree`, but the Python static type checker cannot handle recursive types well.)

```python
DerivationTree = Tuple[str, Optional[List[Any]]]
```

Let us take a very simple derivation tree, representing the intermediate step `<expr> + <term>`, above.

```python
derivation_tree: DerivationTree = ("<start>",
                   [("<expr>",
                     [("<expr>", None),
                      (" + ", []),
                         ("<term>", None)]
                     )])
```

To better understand the structure of this tree, let us introduce a function `display_tree()` that visualizes this tree.

#### Excursion: Implementing `display_tree()`

We use the `dot` drawing program from the `graphviz` package algorithmically, traversing the above structure.  (Unless you're deeply interested in tree visualization, you can directly skip to the example below.)

```python
from graphviz import Digraph
```

```python
from IPython.display import display
```

```python
import re
import string
```

```python
def dot_escape(s: str, show_ascii=None) -> str:
    """Return s in a form suitable for dot.
    If `show_ascii` is True or length of `s` is 1, also append ascii value."""
    escaped_s = ''
    if show_ascii is None:
        show_ascii = (len(s) == 1)  # Default: Single chars only

    if show_ascii and s == '\n':
        return '\\\\n (10)'

    s = s.replace('\n', '\\n')
    for c in s:
        if re.match('[,<>\\\\"]', c):
            escaped_s += '\\' + c
        elif c in string.printable and 31 < ord(c) < 127:
            escaped_s += c
        else:
            escaped_s += '\\\\x' + format(ord(c), '02x')

        if show_ascii:
            escaped_s += f' ({ord(c)})'

    return escaped_s
```

```python
assert dot_escape("hello") == "hello"
```

```python
assert dot_escape("<hello>, world") == "\\<hello\\>\\, world"
```

```python
assert dot_escape("\\n") == "\\\\n"
```

```python
assert dot_escape("\n", show_ascii=False) == "\\\\n"
```

```python
assert dot_escape("\n", show_ascii=True) == "\\\\n (10)"
```

```python
assert dot_escape("\n", show_ascii=True) == "\\\\n (10)"
```

```python
assert dot_escape('\x01', show_ascii=False) == "\\\\x01"
```

```python
assert dot_escape('\x01') == "\\\\x01 (1)"
```

While we are interested at present in visualizing a `derivation_tree`, it is in our interest to generalize the visualization procedure. In particular, it would be helpful if our method `display_tree()` can display *any* tree    like data structure. To enable this, we define a helper method `extract_node()` that extract the current symbol and  children from a given data structure. The default implementation simply extracts the symbol, children, and           annotation from any `derivation_tree` node.

```python
def extract_node(node, id):
    symbol, children, *annotation = node
    return symbol, children, ''.join(str(a) for a in annotation)
```

While visualizing a tree, it is often useful to display certain nodes differently. For example, it is sometimes useful to distinguish between non-processed nodes and processed nodes. We define a helper procedure `default_node_attr()` that provides the basic display, which can be customized by the user.

```python
def default_node_attr(dot, nid, symbol, ann):
    dot.node(repr(nid), dot_escape(symbol))
```

Similar to nodes, the edges may also require modifications. We define `default_edge_attr()` as a helper        procedure that can be customized by the user.

```python
def default_edge_attr(dot, start_node, stop_node):
    dot.edge(repr(start_node), repr(stop_node))
```

While visualizing a tree, one may sometimes wish to change the appearance of the tree. For example, it is      sometimes easier to view the tree if it was laid out left to right rather than top to bottom. We define another      helper procedure `default_graph_attr()` for that.

```python
def default_graph_attr(dot):
    dot.attr('node', shape='plain')
```

Finally, we define a method `display_tree()` that accepts these four functions `extract_node()`,               `default_edge_attr()`, `default_node_attr()` and `default_graph_attr()` and uses them to display the tree.

```python
def display_tree(derivation_tree: DerivationTree,
                 log: bool = False,
                 extract_node: Callable = extract_node,
                 node_attr: Callable = default_node_attr,
                 edge_attr: Callable = default_edge_attr,
                 graph_attr: Callable = default_graph_attr) -> Any:

    # If we import display_tree, we also have to import its functions
    from graphviz import Digraph

    counter = 0

    def traverse_tree(dot, tree, id=0):
        (symbol, children, annotation) = extract_node(tree, id)
        node_attr(dot, id, symbol, annotation)

        if children:
            for child in children:
                nonlocal counter
                counter += 1
                child_id = counter
                edge_attr(dot, id, child_id)
                traverse_tree(dot, child, child_id)

    dot = Digraph(comment="Derivation Tree")
    graph_attr(dot)
    traverse_tree(dot, derivation_tree)
    if log:
        print(dot)
    return dot
```

#### End of Excursion

This is what our tree visualizes into:

```python
display_tree(derivation_tree)
```

```python
quiz("And which of these is the internal representation of `derivation_tree`?",
    [
        "`('<start>', [('<expr>', (['<expr> + <term>']))])`",
        "`('<start>', [('<expr>', (['<expr>', ' + ', <term>']))])`",
        "`" + repr(derivation_tree) + "`",
        "`(" + repr(derivation_tree) + ", None)`"
    ], len("eleven") - len("one"))
```

You can check it out yourself:

```python
derivation_tree
```

Within this book, we also occasionally use a function `display_annotated_tree()` which allows adding annotations to individual nodes.

#### Excursion: Source code and example for `display_annotated_tree()`

`display_annotated_tree()` displays an annotated tree structure, and lays out the graph left to right.

```python
def display_annotated_tree(tree: DerivationTree,
                           a_nodes: Dict[int, str],
                           a_edges: Dict[Tuple[int, int], str],
                           log: bool = False):
    def graph_attr(dot):
        dot.attr('node', shape='plain')
        dot.graph_attr['rankdir'] = 'LR'

    def annotate_node(dot, nid, symbol, ann):
        if nid in a_nodes:
            dot.node(repr(nid), 
                     "%s (%s)" % (dot_escape(unicode_escape(symbol)),
                                  a_nodes[nid]))
        else:
            dot.node(repr(nid), dot_escape(unicode_escape(symbol)))

    def annotate_edge(dot, start_node, stop_node):
        if (start_node, stop_node) in a_edges:
            dot.edge(repr(start_node), repr(stop_node),
                     a_edges[(start_node, stop_node)])
        else:
            dot.edge(repr(start_node), repr(stop_node))

    return display_tree(tree, log=log,
                        node_attr=annotate_node,
                        edge_attr=annotate_edge,
                        graph_attr=graph_attr)
```

```python
display_annotated_tree(derivation_tree, {3: 'plus'}, {(1, 3): 'op'}, log=False)
```

#### End of Excursion

If we want to see all the leaf nodes in a tree as a string, the following `all_terminals()` function comes in handy:

```python
def all_terminals(tree: DerivationTree) -> str:
    (symbol, children) = tree
    if children is None:
        # This is a nonterminal symbol not expanded yet
        return symbol

    if len(children) == 0:
        # This is a terminal symbol
        return symbol

    # This is an expanded symbol:
    # Concatenate all terminal symbols from all children
    return ''.join([all_terminals(c) for c in children])
```

```python
all_terminals(derivation_tree)
```

The alternative `tree_to_string()` function also converts the tree to a string; however, it replaces nonterminal symbols by empty strings.

```python
def tree_to_string(tree: DerivationTree) -> str:
    symbol, children, *_ = tree
    if children:
        return ''.join(tree_to_string(c) for c in children)
    else:
        return '' if is_nonterminal(symbol) else symbol
```

```python
tree_to_string(derivation_tree)
```

## Expanding a Node

Let us now develop an algorithm that takes a tree with non-expanded symbols (say, `derivation_tree`, above), and expands all these symbols one after the other.  As with earlier fuzzers, we create a special subclass of `Fuzzer` – in this case, `GrammarFuzzer`.  A `GrammarFuzzer` gets a grammar and a start symbol; the other parameters will be used later to further control creation and to support debugging.

```python
from Fuzzer import Fuzzer
```

```python
class GrammarFuzzer(Fuzzer):
    """Produce strings from grammars efficiently, using derivation trees."""

    def __init__(self,
                 grammar: Grammar,
                 start_symbol: str = START_SYMBOL,
                 min_nonterminals: int = 0,
                 max_nonterminals: int = 10,
                 disp: bool = False,
                 log: Union[bool, int] = False) -> None:
        """Produce strings from `grammar`, starting with `start_symbol`.
        If `min_nonterminals` or `max_nonterminals` is given, use them as limits 
        for the number of nonterminals produced.  
        If `disp` is set, display the intermediate derivation trees.
        If `log` is set, show intermediate steps as text on standard output."""

        self.grammar = grammar
        self.start_symbol = start_symbol
        self.min_nonterminals = min_nonterminals
        self.max_nonterminals = max_nonterminals
        self.disp = disp
        self.log = log
        self.check_grammar()  # Invokes is_valid_grammar()
```

To add further methods to `GrammarFuzzer`, we use the hack already introduced for [the `MutationFuzzer` class](MutationFuzzer.ipynb).  The construct

```python
class GrammarFuzzer(GrammarFuzzer):
    def new_method(self, args):
        pass
```

allows us to add a new method `new_method()` to the `GrammarFuzzer` class. (Actually, we get a new `GrammarFuzzer` class that extends the old one, but for all our purposes, this does not matter.)

#### Excursion: `check_grammar()` implementation

We can use the above hack to define the helper method `check_grammar()`, which checks the given grammar for consistency:

```python
class GrammarFuzzer(GrammarFuzzer):
    def check_grammar(self) -> None:
        """Check the grammar passed"""
        assert self.start_symbol in self.grammar
        assert is_valid_grammar(
            self.grammar,
            start_symbol=self.start_symbol,
            supported_opts=self.supported_opts())

    def supported_opts(self) -> Set[str]:
        """Set of supported options. To be overloaded in subclasses."""
        return set()  # We don't support specific options
```

#### End of Excursion

Let us now define a helper method `init_tree()` that constructs a tree with just the start symbol:

```python
class GrammarFuzzer(GrammarFuzzer):
    def init_tree(self) -> DerivationTree:
        return (self.start_symbol, None)
```

```python
f = GrammarFuzzer(EXPR_GRAMMAR)
display_tree(f.init_tree())
```

This is the tree we want to expand.

### Picking a Children Alternative to be Expanded

One of the central methods in `GrammarFuzzer` is `choose_node_expansion()`. This method gets a node (say, the `<start>` node) and a list of possible lists of children to be expanded (one for every possible expansion from the grammar), chooses one of them, and returns its index in the possible children list.

By overloading this method (notably in later chapters), we can implement different strategies – for now, it simply randomly picks one of the given lists of children (which in turn are lists of derivation trees).

```python
class GrammarFuzzer(GrammarFuzzer):
    def choose_node_expansion(self, node: DerivationTree,
                              children_alternatives: List[List[DerivationTree]]) -> int:
        """Return index of expansion in `children_alternatives` to be selected.
           'children_alternatives`: a list of possible children for `node`.
           Defaults to random. To be overloaded in subclasses."""
        return random.randrange(0, len(children_alternatives))
```

### Getting a List of Possible Expansions

To actually obtain the list of possible children, we will need a helper function `expansion_to_children()` that takes an expansion string and decomposes it into a list of derivation trees – one for each symbol (terminal or nonterminal) in the string.

#### Excursion: Implementing `expansion_to_children()`

The function `expansion_to_children()` uses the `re.split()` method to split an expansion string into a list of children nodes:

```python
def expansion_to_children(expansion: Expansion) -> List[DerivationTree]:
    # print("Converting " + repr(expansion))
    # strings contains all substrings -- both terminals and nonterminals such
    # that ''.join(strings) == expansion

    expansion = exp_string(expansion)
    assert isinstance(expansion, str)

    if expansion == "":  # Special case: epsilon expansion
        return [("", [])]

    strings = re.split(RE_NONTERMINAL, expansion)
    return [(s, None) if is_nonterminal(s) else (s, [])
            for s in strings if len(s) > 0]
```

#### End of Excursion

```python
expansion_to_children("<term> + <expr>")
```

The case of an *epsilon expansion*, i.e. expanding into an empty string as in `<symbol> ::=` needs special treatment:

```python
expansion_to_children("")
```

Just like `nonterminals()` in the [chapter on Grammars](Grammars.ipynb), we provide for future extensions, allowing the expansion to be a tuple with extra data (which will be ignored).

```python
expansion_to_children(("+<term>", {"extra_data": 1234}))
```

We realize this helper as a method in `GrammarFuzzer` such that it can be overloaded by subclasses:

```python
class GrammarFuzzer(GrammarFuzzer):
    def expansion_to_children(self, expansion: Expansion) -> List[DerivationTree]:
        return expansion_to_children(expansion)
```

### Putting Things Together

With this, we can now take

1. some non-expanded node in the tree, 
2. choose a random expansion, and
3. return the new tree.

This is what the method `expand_node_randomly()` does.

#### Excursion: `expand_node_randomly()` implementation

The function `expand_node_randomly()` uses a helper function `choose_node_expansion()` to randomly pick an index from an array of possible children.  (`choose_node_expansion()` can be overloaded in subclasses.)

```python
import random
```

```python
class GrammarFuzzer(GrammarFuzzer):
    def expand_node_randomly(self, node: DerivationTree) -> DerivationTree:
        """Choose a random expansion for `node` and return it"""
        (symbol, children) = node
        assert children is None

        if self.log:
            print("Expanding", all_terminals(node), "randomly")

        # Fetch the possible expansions from grammar...
        expansions = self.grammar[symbol]
        children_alternatives: List[List[DerivationTree]] = [
            self.expansion_to_children(expansion) for expansion in expansions
        ]

        # ... and select a random expansion
        index = self.choose_node_expansion(node, children_alternatives)
        chosen_children = children_alternatives[index]

        # Process children (for subclasses)
        chosen_children = self.process_chosen_children(chosen_children,
                                                       expansions[index])

        # Return with new children
        return (symbol, chosen_children)
```

The generic `expand_node()` method can later be used to select different expansion strategies; as of now, it only uses `expand_node_randomly()`.

```python
class GrammarFuzzer(GrammarFuzzer):
    def expand_node(self, node: DerivationTree) -> DerivationTree:
        return self.expand_node_randomly(node)
```

The helper function `process_chosen_children()` does nothing; it can be overloaded by subclasses to process the children once chosen.

```python
class GrammarFuzzer(GrammarFuzzer):
    def process_chosen_children(self,
                                chosen_children: List[DerivationTree],
                                expansion: Expansion) -> List[DerivationTree]:
        """Process children after selection.  By default, does nothing."""
        return chosen_children
```

#### End of Excursion

This is how `expand_node_randomly()` works:

```python
f = GrammarFuzzer(EXPR_GRAMMAR, log=True)

print("Before expand_node_randomly():")
expr_tree = ("<integer>", None)
display_tree(expr_tree)
```

```python
print("After expand_node_randomly():")
expr_tree = f.expand_node_randomly(expr_tree)
display_tree(expr_tree)
```

```python
# docassert
assert expr_tree[1][0][0] == '<digit>'
```

```python
quiz("What tree do we get if we expand the `<digit>` subtree?",
     [
         "We get another `<digit>` as new child of `<digit>`",
         "We get some digit as child of `<digit>`",
         "We get another `<digit>` as second child of `<integer>`",
         "The entire tree becomes a single node with a digit"
     ], 'len("2") + len("2")')
```

We can surely put this to the test, right? Here we go:

```python
digit_subtree = expr_tree[1][0]  # type: ignore
display_tree(digit_subtree)
```

```python
print("After expanding the <digit> subtree:")
digit_subtree = f.expand_node_randomly(digit_subtree)
display_tree(digit_subtree)
```

We see that `<digit>` gets expanded again according to the grammar rules – namely, into a single digit.

```python
quiz("Is the original `expr_tree` affected by this change?",
     [
         "No, it is unchanged",
         "Yes, it has also gained a new child"
     ], "1 ** (1 - 1)")
```

Although we have changed one of the subtrees, the original `expr_tree` is unaffected:

```python
display_tree(expr_tree)
```

That is because `expand_node_randomly()` returns a new (expanded) tree and does not change the tree passed as argument.

## Expanding a Tree

Let us now apply our functions for expanding a single node to some node in the tree.  To this end, we first need to _search the tree for non-expanded nodes_.  `possible_expansions()` counts how many unexpanded symbols there are in a tree:

```python
class GrammarFuzzer(GrammarFuzzer):
    def possible_expansions(self, node: DerivationTree) -> int:
        (symbol, children) = node
        if children is None:
            return 1

        return sum(self.possible_expansions(c) for c in children)
```

```python
f = GrammarFuzzer(EXPR_GRAMMAR)
print(f.possible_expansions(derivation_tree))
```

The method `any_possible_expansions()` returns True if the tree has any non-expanded nodes.

```python
class GrammarFuzzer(GrammarFuzzer):
    def any_possible_expansions(self, node: DerivationTree) -> bool:
        (symbol, children) = node
        if children is None:
            return True

        return any(self.any_possible_expansions(c) for c in children)
```

```python
f = GrammarFuzzer(EXPR_GRAMMAR)
f.any_possible_expansions(derivation_tree)
```

Here comes `expand_tree_once()`, the core method of our tree expansion algorithm.  It first checks whether it is currently being applied on a nonterminal symbol without expansion; if so, it invokes `expand_node()` on it, as discussed above.  

If the node is already expanded (i.e. has children), it checks the subset of children which still have non-expanded symbols, randomly selects one of them, and applies itself recursively on that child.

#### Excursion: `expand_tree_once()` implementation

The `expand_tree_once()` method replaces the child _in place_, meaning that it actually mutates the tree being passed as an argument rather than returning a new tree.  This in-place mutation is what makes this function particularly efficient.  Again, we use a helper method (`choose_tree_expansion()`) to return the chosen index from a list of children that can be expanded.

```python
class GrammarFuzzer(GrammarFuzzer):
    def choose_tree_expansion(self,
                              tree: DerivationTree,
                              children: List[DerivationTree]) -> int:
        """Return index of subtree in `children` to be selected for expansion.
           Defaults to random."""
        return random.randrange(0, len(children))

    def expand_tree_once(self, tree: DerivationTree) -> DerivationTree:
        """Choose an unexpanded symbol in tree; expand it.
           Can be overloaded in subclasses."""
        (symbol, children) = tree
        if children is None:
            # Expand this node
            return self.expand_node(tree)

        # Find all children with possible expansions
        expandable_children = [
            c for c in children if self.any_possible_expansions(c)]

        # `index_map` translates an index in `expandable_children`
        # back into the original index in `children`
        index_map = [i for (i, c) in enumerate(children)
                     if c in expandable_children]

        # Select a random child
        child_to_be_expanded = \
            self.choose_tree_expansion(tree, expandable_children)

        # Expand in place
        children[index_map[child_to_be_expanded]] = \
            self.expand_tree_once(expandable_children[child_to_be_expanded])

        return tree
```

#### End of Excursion

Let us illustrate how `expand_tree_once()` works. We start with our derivation tree from above...

```python
derivation_tree = ("<start>",
                   [("<expr>",
                     [("<expr>", None),
                      (" + ", []),
                         ("<term>", None)]
                     )])
display_tree(derivation_tree)
```

... and now expand it twice:

```python
f = GrammarFuzzer(EXPR_GRAMMAR, log=True)
derivation_tree = f.expand_tree_once(derivation_tree)
display_tree(derivation_tree)
```

```python
derivation_tree = f.expand_tree_once(derivation_tree)
display_tree(derivation_tree)
```

We see that with each step, one more symbol is expanded.  Now all it takes is to apply this again and again, expanding the tree further and further.

## Closing the Expansion

With `expand_tree_once()`, we can keep on expanding the tree – but how do we actually stop?  The key idea here, introduced by Luke in \cite{Luke2000}, is that after inflating the derivation tree to some maximum size, we _only want to apply expansions that increase the size of the tree by a minimum_.  For `<factor>`, for instance, we would prefer an expansion into `<integer>`, as this will not introduce further recursion (and potential size inflation); for `<integer>`, likewise, an expansion into `<digit>` is preferred, as it will less increase tree size than `<digit><integer>`.

To identify the _cost_ of expanding a symbol, we introduce two functions that mutually rely on each other:

* `symbol_cost()` returns the minimum cost of all expansions of a symbol, using `expansion_cost()` to compute the cost for each expansion.
* `expansion_cost()` returns the sum of all expansions in `expansions`. If a nonterminal is encountered again during traversal, the cost of the expansion is $\infty$, indicating (potentially infinite) recursion.

### Excursion: Implementing Cost Functions

```python
class GrammarFuzzer(GrammarFuzzer):
    def symbol_cost(self, symbol: str, seen: Set[str] = set()) \
            -> Union[int, float]:
        expansions = self.grammar[symbol]
        return min(self.expansion_cost(e, seen | {symbol}) for e in expansions)

    def expansion_cost(self, expansion: Expansion,
                       seen: Set[str] = set()) -> Union[int, float]:
        symbols = nonterminals(expansion)
        if len(symbols) == 0:
            return 1  # no symbol

        if any(s in seen for s in symbols):
            return float('inf')

        # the value of a expansion is the sum of all expandable variables
        # inside + 1
        return sum(self.symbol_cost(s, seen) for s in symbols) + 1
```

### End of Excursion

Here are two examples: The minimum cost of expanding a digit is 1, since we have to choose from one of its expansions.

```python
f = GrammarFuzzer(EXPR_GRAMMAR)
assert f.symbol_cost("<digit>") == 1
```

The minimum cost of expanding `<expr>`, though, is five, as this is the minimum number of expansions required.  (`<expr>` $\rightarrow$ `<term>` $\rightarrow$ `<factor>` $\rightarrow$ `<integer>` $\rightarrow$ `<digit>` $\rightarrow$ 1)

```python
assert f.symbol_cost("<expr>") == 5
```

We define `expand_node_by_cost(self, node, choose)`, a variant of `expand_node()` that takes the above cost into account.  It determines the minimum cost `cost` across all children and then chooses a child from the list using the `choose` function, which by default is the minimum cost.  If multiple children all have the same minimum cost, it chooses randomly between these.

#### Excursion: `expand_node_by_cost()` implementation

```python
class GrammarFuzzer(GrammarFuzzer):
    def expand_node_by_cost(self, node: DerivationTree, 
                            choose: Callable = min) -> DerivationTree:
        (symbol, children) = node
        assert children is None

        # Fetch the possible expansions from grammar...
        expansions = self.grammar[symbol]

        children_alternatives_with_cost = [(self.expansion_to_children(expansion),
                                            self.expansion_cost(expansion, {symbol}),
                                            expansion)
                                           for expansion in expansions]

        costs = [cost for (child, cost, expansion)
                 in children_alternatives_with_cost]
        chosen_cost = choose(costs)
        children_with_chosen_cost = [child for (child, child_cost, _) 
                                     in children_alternatives_with_cost
                                     if child_cost == chosen_cost]
        expansion_with_chosen_cost = [expansion for (_, child_cost, expansion)
                                      in children_alternatives_with_cost
                                      if child_cost == chosen_cost]

        index = self.choose_node_expansion(node, children_with_chosen_cost)

        chosen_children = children_with_chosen_cost[index]
        chosen_expansion = expansion_with_chosen_cost[index]
        chosen_children = self.process_chosen_children(
            chosen_children, chosen_expansion)

        # Return with a new list
        return (symbol, chosen_children)
```

#### End of Excursion

The shortcut `expand_node_min_cost()` passes `min()` as the `choose` function, which makes it expand nodes at minimum cost.

```python
class GrammarFuzzer(GrammarFuzzer):
    def expand_node_min_cost(self, node: DerivationTree) -> DerivationTree:
        if self.log:
            print("Expanding", all_terminals(node), "at minimum cost")

        return self.expand_node_by_cost(node, min)
```

We can now apply this function to close the expansion of our derivation tree, using `expand_tree_once()` with the above `expand_node_min_cost()` as expansion function.

```python
class GrammarFuzzer(GrammarFuzzer):
    def expand_node(self, node: DerivationTree) -> DerivationTree:
        return self.expand_node_min_cost(node)
```

```python
f = GrammarFuzzer(EXPR_GRAMMAR, log=True)
display_tree(derivation_tree)
```

```python
# docassert
assert f.any_possible_expansions(derivation_tree)
```

```python
if f.any_possible_expansions(derivation_tree):
    derivation_tree = f.expand_tree_once(derivation_tree)
display_tree(derivation_tree)
```

```python
# docassert
assert f.any_possible_expansions(derivation_tree)
```

```python
if f.any_possible_expansions(derivation_tree):
    derivation_tree = f.expand_tree_once(derivation_tree)
display_tree(derivation_tree)
```

```python
# docassert
assert f.any_possible_expansions(derivation_tree)
```

```python
if f.any_possible_expansions(derivation_tree):
    derivation_tree = f.expand_tree_once(derivation_tree)
display_tree(derivation_tree)
```

We keep on expanding until all nonterminals are expanded.

```python
while f.any_possible_expansions(derivation_tree):
    derivation_tree = f.expand_tree_once(derivation_tree)    
```

Here is the final tree:

```python
display_tree(derivation_tree)
```

We see that in each step, `expand_node_min_cost()` chooses an expansion that does not increase the number of symbols, eventually closing all open expansions.

## Node Inflation

Especially at the beginning of an expansion, we may be interested in getting _as many nodes as possible_ – that is, we'd like to prefer expansions that give us _more_ nonterminals to expand.  This is actually the exact opposite of what `expand_node_min_cost()` gives us, and we can implement a method `expand_node_max_cost()` that will always choose among the nodes with the _highest_ cost:

```python
class GrammarFuzzer(GrammarFuzzer):
    def expand_node_max_cost(self, node: DerivationTree) -> DerivationTree:
        if self.log:
            print("Expanding", all_terminals(node), "at maximum cost")

        return self.expand_node_by_cost(node, max)
```

To illustrate `expand_node_max_cost()`, we can again redefine `expand_node()` to use it, and then use `expand_tree_once()` to show a few expansion steps:

```python
class GrammarFuzzer(GrammarFuzzer):
    def expand_node(self, node: DerivationTree) -> DerivationTree:
        return self.expand_node_max_cost(node)
```

```python
derivation_tree = ("<start>",
                   [("<expr>",
                     [("<expr>", None),
                      (" + ", []),
                         ("<term>", None)]
                     )])
```

```python
f = GrammarFuzzer(EXPR_GRAMMAR, log=True)
display_tree(derivation_tree)
```

```python
# docassert
assert f.any_possible_expansions(derivation_tree)
```

```python
if f.any_possible_expansions(derivation_tree):
    derivation_tree = f.expand_tree_once(derivation_tree)
display_tree(derivation_tree)
```

```python
# docassert
assert f.any_possible_expansions(derivation_tree)
```

```python
if f.any_possible_expansions(derivation_tree):
    derivation_tree = f.expand_tree_once(derivation_tree)
display_tree(derivation_tree)
```

```python
# docassert
assert f.any_possible_expansions(derivation_tree)
```

```python
if f.any_possible_expansions(derivation_tree):
    derivation_tree = f.expand_tree_once(derivation_tree)
display_tree(derivation_tree)
```

We see that with each step, the number of nonterminals increases.  Obviously, we have to put a limit on this number.

## Three Expansion Phases

We can now put all three phases together in a single function `expand_tree()` which will work as follows:

1. **Max cost expansion.** Expand the tree using expansions with maximum cost until we have at least `min_nonterminals` nonterminals.  This phase can be easily skipped by setting `min_nonterminals` to zero.
2. **Random expansion.**  Keep on expanding the tree randomly until we reach `max_nonterminals` nonterminals.
3. **Min cost expansion.** Close the expansion with minimum cost.

We implement these three phases by having `expand_node` reference the expansion method to apply.  This is controlled by setting `expand_node` (the method reference) to first `expand_node_max_cost` (i.e., calling `expand_node()` invokes `expand_node_max_cost()`), then `expand_node_randomly`, and finally `expand_node_min_cost`.  In the first two phases, we also set a maximum limit of `min_nonterminals` and `max_nonterminals`, respectively.

#### Excursion: Implementation of three-phase `expand_tree()`

```python
class GrammarFuzzer(GrammarFuzzer):
    def log_tree(self, tree: DerivationTree) -> None:
        """Output a tree if self.log is set; if self.display is also set, show the tree structure"""
        if self.log:
            print("Tree:", all_terminals(tree))
            if self.disp:
                display(display_tree(tree))
            # print(self.possible_expansions(tree), "possible expansion(s) left")

    def expand_tree_with_strategy(self, tree: DerivationTree,
                                  expand_node_method: Callable,
                                  limit: Optional[int] = None):
        """Expand tree using `expand_node_method` as node expansion function
        until the number of possible expansions reaches `limit`."""
        self.expand_node = expand_node_method  # type: ignore
        while ((limit is None
                or self.possible_expansions(tree) < limit)
               and self.any_possible_expansions(tree)):
            tree = self.expand_tree_once(tree)
            self.log_tree(tree)
        return tree

    def expand_tree(self, tree: DerivationTree) -> DerivationTree:
        """Expand `tree` in a three-phase strategy until all expansions are complete."""
        self.log_tree(tree)
        tree = self.expand_tree_with_strategy(
            tree, self.expand_node_max_cost, self.min_nonterminals)
        tree = self.expand_tree_with_strategy(
            tree, self.expand_node_randomly, self.max_nonterminals)
        tree = self.expand_tree_with_strategy(
            tree, self.expand_node_min_cost)

        assert self.possible_expansions(tree) == 0

        return tree
```

#### End of Excursion

Let us try this out on our example. We start with a half-expanded derivation tree:

```python
initial_derivation_tree: DerivationTree = ("<start>",
                   [("<expr>",
                     [("<expr>", None),
                      (" + ", []),
                         ("<term>", None)]
                     )])
```

```python
display_tree(initial_derivation_tree)
```

We now apply our expansion strategy on this tree.  We see that initially, nodes are expanded at maximum cost, then randomly, and then closing the expansion at minimum cost.

```python
f = GrammarFuzzer(
    EXPR_GRAMMAR,
    min_nonterminals=3,
    max_nonterminals=5,
    log=True)
derivation_tree = f.expand_tree(initial_derivation_tree)
```

This is the final derivation tree:

```python
display_tree(derivation_tree)
```

And this is the resulting string:

```python
all_terminals(derivation_tree)
```

## Putting it all Together

Based on this, we can now define a function `fuzz()` that – like `simple_grammar_fuzzer()` – simply takes a grammar and produces a string from it.  It thus no longer exposes the complexity of derivation trees.

```python
class GrammarFuzzer(GrammarFuzzer):
    def fuzz_tree(self) -> DerivationTree:
        """Produce a derivation tree from the grammar."""
        tree = self.init_tree()
        # print(tree)

        # Expand all nonterminals
        tree = self.expand_tree(tree)
        if self.log:
            print(repr(all_terminals(tree)))
        if self.disp:
            display(display_tree(tree))
        return tree

    def fuzz(self) -> str:
        """Produce a string from the grammar."""
        self.derivation_tree = self.fuzz_tree()
        return all_terminals(self.derivation_tree)
```

We can now apply this on all our defined grammars (and visualize the derivation tree along)

```python
f = GrammarFuzzer(EXPR_GRAMMAR)
f.fuzz()
```

After calling `fuzz()`, the produced derivation tree is accessible in the `derivation_tree` attribute:

```python
display_tree(f.derivation_tree)
```

Let us try out the grammar fuzzer (and its trees) on other grammar formats.

```python
f = GrammarFuzzer(URL_GRAMMAR)
f.fuzz()
```

```python
display_tree(f.derivation_tree)
```

```python
f = GrammarFuzzer(CGI_GRAMMAR, min_nonterminals=3, max_nonterminals=5)
f.fuzz()
```

```python
display_tree(f.derivation_tree)
```

How do we stack up against `simple_grammar_fuzzer()`?

```python
trials = 50
xs = []
ys = []
f = GrammarFuzzer(EXPR_GRAMMAR, max_nonterminals=20)
for i in range(trials):
    with Timer() as t:
        s = f.fuzz()
    xs.append(len(s))
    ys.append(t.elapsed_time())
    print(i, end=" ")
print()
```

```python
average_time = sum(ys) / trials
print("Average time:", average_time)
```

```python
%matplotlib inline

import matplotlib.pyplot as plt
plt.scatter(xs, ys)
plt.title('Time required for generating an output');
```

Our test generation is much faster, but also our inputs are much smaller.  We see that with derivation trees, we can get much better control over grammar production.

Finally, how does `GrammarFuzzer` work with `expr_grammar`, where `simple_grammar_fuzzer()` failed?  It works without any issue:

```python
f = GrammarFuzzer(expr_grammar, max_nonterminals=10)
f.fuzz()
```

With `GrammarFuzzer`, we now have a solid foundation on which to build further fuzzers and illustrate more exciting concepts from the world of generating software tests.  Many of these do not even require writing a grammar – instead, they _infer_ a grammar from the domain at hand, and thus allow using grammar-based fuzzing even without writing a grammar.  Stay tuned!

## Synopsis

### Efficient Grammar Fuzzing

This chapter introduces `GrammarFuzzer`, an efficient grammar fuzzer that takes a grammar to produce syntactically valid input strings.  Here's a typical usage:

```python
from Grammars import US_PHONE_GRAMMAR
```

```python
phone_fuzzer = GrammarFuzzer(US_PHONE_GRAMMAR)
phone_fuzzer.fuzz()
```

The `GrammarFuzzer` constructor takes a number of keyword arguments to control its behavior.  `start_symbol`, for instance, allows setting the symbol that expansion starts with (instead of `<start>`):

```python
area_fuzzer = GrammarFuzzer(US_PHONE_GRAMMAR, start_symbol='<area>')
area_fuzzer.fuzz()
```

Here's how to parameterize the `GrammarFuzzer` constructor:

```python
# ignore
import inspect
```

```python
# ignore
print(inspect.getdoc(GrammarFuzzer.__init__))
```

```python
# ignore
from ClassDiagram import display_class_hierarchy
```

```python
# ignore
display_class_hierarchy([GrammarFuzzer],
                        public_methods=[
                            Fuzzer.__init__,
                            Fuzzer.fuzz,
                            Fuzzer.run,
                            Fuzzer.runs,
                            GrammarFuzzer.__init__,
                            GrammarFuzzer.fuzz,
                            GrammarFuzzer.fuzz_tree,
                        ],
                        types={
                            'DerivationTree': DerivationTree,
                            'Expansion': Expansion,
                            'Grammar': Grammar
                        },
                        project='fuzzingbook')
```

### Derivation Trees

Internally, `GrammarFuzzer` makes use of [derivation trees](#Derivation-Trees), which it expands step by step.  After producing a string, the tree produced can be accessed in the `derivation_tree` attribute.

```python
display_tree(phone_fuzzer.derivation_tree)
```

In the internal representation of a derivation tree, a _node_ is a pair (`symbol`, `children`).  For nonterminals, `symbol` is the symbol that is being expanded, and `children` is a list of further nodes.  For terminals, `symbol` is the terminal string, and `children` is empty.

```python
phone_fuzzer.derivation_tree
```

The chapter contains various helpers to work with derivation trees, including visualization tools – notably, `display_tree()`, above.

## Lessons Learned

* _Derivation trees_ are important for expressing input structure
* _Grammar fuzzing based on derivation trees_ 
    1. is much more efficient than string-based grammar fuzzing,
    2. gives much better control over input generation, and
    3. effectively avoids running into infinite expansions.

## Next Steps

Congratulations!  You have reached one of the central "hubs" of the book.  From here, there is a wide range of techniques that build on grammar fuzzing.

### Extending Grammars

First, we have a number of techniques that all _extend_ grammars in some form:

* [Parsing and recombining inputs](Parser.ipynb) allows making use of existing inputs, again using derivation trees
* [Covering grammar expansions](GrammarCoverageFuzzer.ipynb) allows for _combinatorial_ coverage
* [Assigning _probabilities_ to individual expansions](ProbabilisticGrammarFuzzer.ipynb) gives additional control over expansions
* [Assigning _constraints_ to individual expansions](GeneratorGrammarFuzzer.ipynb) allows expressing _semantic constraints_ on individual rules.

### Applying Grammars

Second, we can _apply_ grammars in a variety of contexts that all involve some form of learning it automatically:

* [Fuzzing APIs](APIFuzzer.ipynb), learning a grammar from APIs
* [Fuzzing graphical user interfaces](WebFuzzer.ipynb), learning a grammar from user interfaces for subsequent fuzzing
* [Mining grammars](GrammarMiner.ipynb), learning a grammar for arbitrary input formats

Keep on expanding!

## Background

Derivation trees (then frequently called _parse trees_) are a standard data structure into which *parsers* decompose inputs.  The *Dragon Book* (also known as *Compilers: Principles, Techniques, and Tools*) \cite{Aho2006} discusses parsing into derivation trees as part of compiling programs.  We also use derivation trees [when parsing and recombining inputs](Parser.ipynb).

The key idea in this chapter, namely expanding until a limit of symbols is reached, and then always choosing the shortest path, stems from Luke \cite{Luke2000}.

## Exercises

### Exercise 1: Caching Method Results

Tracking `GrammarFuzzer` reveals that some methods are called again and again, always with the same values.  

Set up a class `FasterGrammarFuzzer` with a _cache_ that checks whether the method has been called before, and if so, return the previously computed "memoized" value.  Do this for `expansion_to_children()`.  Compare the number of invocations before and after the optimization.

**Important**: For `expansion_to_children()`, make sure that each list returned is an individual copy.  If you return the same (cached) list, this will interfere with the in-place modification of `GrammarFuzzer`.  Use the Python `copy.deepcopy()` function for this purpose.

**Solution.** Let us demonstrate this for `expansion_to_children()`:

```python
import copy
```

```python
class FasterGrammarFuzzer(GrammarFuzzer):
    """Variant of `GrammarFuzzer` with memoized values"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._expansion_cache: Dict[Expansion, List[DerivationTree]] = {}
        self._expansion_invocations = 0
        self._expansion_invocations_cached = 0

    def expansion_to_children(self, expansion: Expansion) \
            -> List[DerivationTree]:
        self._expansion_invocations += 1
        if expansion in self._expansion_cache:
            self._expansion_invocations_cached += 1
            cached_result = copy.deepcopy(self._expansion_cache[expansion])
            return cached_result

        result = super().expansion_to_children(expansion)
        self._expansion_cache[expansion] = copy.deepcopy(result)
        return result
```

```python
f = FasterGrammarFuzzer(EXPR_GRAMMAR, min_nonterminals=3, max_nonterminals=5)
f.fuzz()
```

```python
f._expansion_invocations
```

```python
f._expansion_invocations_cached
```

```python
print("%.2f%% of invocations can be cached" %
      (f._expansion_invocations_cached * 100 / f._expansion_invocations))
```

### Exercise 2: Grammar Pre-Compilation

Some methods such as `symbol_cost()` or `expansion_cost()` return a value that is dependent on the grammar only.  Set up a class `EvenFasterGrammarFuzzer()` that pre-computes these values once upon initialization, such that later invocations of `symbol_cost()` or `expansion_cost()` need only look up these values.

**Solution.** Here's a possible solution, using a hack to substitute the `symbol_cost()` and `expansion_cost()` functions once the pre-computed values are set up.

```python
class EvenFasterGrammarFuzzer(GrammarFuzzer):
    """Variant of `GrammarFuzzer` with precomputed costs"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._symbol_costs: Dict[str, Union[int, float]] = {}
        self._expansion_costs: Dict[Expansion, Union[int, float]] = {}
        self.precompute_costs()

    def new_symbol_cost(self, symbol: str,
                        seen: Set[str] = set()) -> Union[int, float]:
        return self._symbol_costs[symbol]

    def new_expansion_cost(self, expansion: Expansion,
                           seen: Set[str] = set()) -> Union[int, float]:
        return self._expansion_costs[expansion]

    def precompute_costs(self) -> None:
        for symbol in self.grammar:
            self._symbol_costs[symbol] = super().symbol_cost(symbol)
            for expansion in self.grammar[symbol]:
                self._expansion_costs[expansion] = \
                    super().expansion_cost(expansion)

        # Make sure we now call the caching methods
        self.symbol_cost = self.new_symbol_cost  # type: ignore
        self.expansion_cost = self.new_expansion_cost  # type: ignore
```

```python
f = EvenFasterGrammarFuzzer(EXPR_GRAMMAR)
```

Here are the individual costs:

```python
f._symbol_costs
```

```python
f._expansion_costs
```

```python
f = EvenFasterGrammarFuzzer(EXPR_GRAMMAR)
f.fuzz()
```

### Exercise 3: Maintaining Trees to be Expanded

In `expand_tree_once()`, the algorithm traverses the tree again and again to find nonterminals that still can be extended.  Speed up the process by keeping a list of nonterminal symbols in the tree that still can be expanded.

**Solution.** Left as exercise for the reader.

### Exercise 4: Alternate Random Expansions

We could define `expand_node_randomly()` such that it simply invokes `expand_node_by_cost(node, random.choice)`:

```python
class ExerciseGrammarFuzzer(GrammarFuzzer):
    def expand_node_randomly(self, node: DerivationTree) -> DerivationTree:
        if self.log:
            print("Expanding", all_terminals(node), "randomly by cost")

        return self.expand_node_by_cost(node, random.choice)
```

What is the difference between the original implementation and this alternative?

**Solution.** The alternative in `ExerciseGrammarFuzzer` has another probability distribution.  In the original `GrammarFuzzer`, all expansions have the same likelihood of being expanded.  In `ExerciseGrammarFuzzer`, first, a cost is chosen (randomly); then, one of the expansions with this cost is chosen (again randomly).  This means that expansions whose cost is unique have a higher chance of being selected.
