[ ]
[ ]

[Skip to content](#variables)

Try Ray with $100 credit — [Start Now](https://console.anyscale.com/register/ha?utm_source=made_with_ml&utm_medium=website&utm_campaign=banner)

[![logo](../../../static/images/logo.png)](../../.. "Made With ML by Anyscale")

Made With ML by Anyscale

Python for Machine Learning

Initializing search

[GokuMohandas/MadeWithML](https://github.com/GokuMohandas/Made-With-ML "Go to repository")

* [Home](../../..)
* [About](../../../about/)
* [Course](/#course)
* [Foundations](/courses/foundations/)
* [Subscribe](../../../misc/newsletter/)
* [Community](https://discord.com/channels/1078171187609337896/1078171189169635472)

[![logo](../../../static/images/logo.png)](../../.. "Made With ML by Anyscale")
Made With ML by Anyscale

[GokuMohandas/MadeWithML](https://github.com/GokuMohandas/Made-With-ML "Go to repository")

* [Home](../../..)
* [About](../../../about/)
* [ ]

  Course

  Course
  + [Lessons](/#course)
  + [ ]

    🎨   Design

    🎨   Design
    - [Setup](../../mlops/setup/)
    - [Product](../../mlops/product-design/)
    - [Systems](../../mlops/systems-design/)
  + [ ]

    🔢   Data

    🔢   Data
    - [Preparation](../../mlops/preparation/)
    - [Exploration](../../mlops/exploratory-data-analysis/)
    - [Preprocessing](../../mlops/preprocessing/)
    - [Distributed](../../mlops/distributed-data/)
  + [ ]

    📈   Model

    📈   Model
    - [Training](../../mlops/training/)
    - [Tracking](../../mlops/experiment-tracking/)
    - [Tuning](../../mlops/tuning/)
    - [Evaluation](../../mlops/evaluation/)
    - [Serving](../../mlops/serving/)
  + [ ]

    💻   Developing

    💻   Developing
    - [Scripting](../../mlops/scripting/)
    - [CLI](../../mlops/cli/)
  + [ ]

    📦   Utilities

    📦   Utilities
    - [Logging](../../mlops/logging/)
    - [Documentation](../../mlops/documentation/)
    - [Styling](../../mlops/styling/)
    - [Pre-commit](../../mlops/pre-commit/)
  + [ ]

    ✅   Testing

    ✅   Testing
    - [Code](../../mlops/testing/)
    - [Data](../../mlops/testing/#data)
    - [Models](../../mlops/testing/#models)
  + [ ]

    ♻️   Reproducibility

    ♻️   Reproducibility
    - [Versioning](../../mlops/versioning/)
  + [ ]

    🚀   Production

    🚀   Production
    - [Jobs & Services](../../mlops/jobs-and-services/)
    - [CI/CD workflows](../../mlops/cicd/)
    - [Monitoring](../../mlops/monitoring/)
    - [Data engineering](../../mlops/data-engineering/)
* [x]

  Foundations

  Foundations
  + [Lessons](/courses/foundations/)
  + [x]

    🛠   Toolkit

    🛠   Toolkit
    - [Notebooks](../notebooks/)
    - [ ]

      Python
      [Python](./)

      Table of contents
      * [Variables](#variables)
      * [Lists](#lists)
      * [Tuples](#tuples)
      * [Sets](#sets)
      * [Indexing](#indexing)
      * [Dictionaries](#dictionaries)
      * [If statements](#if-statements)
      * [Loops](#loops)

        + [For loops](#for-loops)
        + [While loops](#while-loops)
      * [List comprehension](#list-comprehension)
      * [Functions](#functions)
      * [Classes](#classes)

        + [Magic methods](#magic-methods)
        + [Object functions](#object-functions)
        + [Inheritance](#inheritance)
        + [Methods](#methods)
      * [Decorators](#decorators)

        + [Creating a decorator](#creating-a-decorator)
        + [Callbacks](#callbacks)
        + [Putting it all together](#putting-it-all-together)
    - [NumPy](../numpy/)
    - [Pandas](../pandas/)
    - [PyTorch](../pytorch/)
  + [ ]

    🔥   Machine Learning

    🔥   Machine Learning
    - [Linear regression](../linear-regression/)
    - [Logistic regression](../logistic-regression/)
    - [Neural networks](../neural-networks/)
    - [Data quality](../data-quality/)
    - [Utilities](../utilities/)
  + [ ]

    🤖   Deep Learning

    🤖   Deep Learning
    - [CNNs](../convolutional-neural-networks/)
    - [Embeddings](../embeddings/)
    - [RNNs](../recurrent-neural-networks/)
    - [Attention](../attention/)
    - [Transformers](../transformers/)
* [Subscribe](../../../misc/newsletter/)
* [Community](https://discord.com/channels/1078171187609337896/1078171189169635472)

Table of contents

* [Variables](#variables)
* [Lists](#lists)
* [Tuples](#tuples)
* [Sets](#sets)
* [Indexing](#indexing)
* [Dictionaries](#dictionaries)
* [If statements](#if-statements)
* [Loops](#loops)

  + [For loops](#for-loops)
  + [While loops](#while-loops)
* [List comprehension](#list-comprehension)
* [Functions](#functions)
* [Classes](#classes)

  + [Magic methods](#magic-methods)
  + [Object functions](#object-functions)
  + [Inheritance](#inheritance)
  + [Methods](#methods)
* [Decorators](#decorators)

  + [Creating a decorator](#creating-a-decorator)
  + [Callbacks](#callbacks)
  + [Putting it all together](#putting-it-all-together)

# Python for Machine Learning

[View all lessons](/courses/foundations)

---

The fundamentals of Python programming for machine learning.

![Goku Mohandas](/static/images/goku_circle.png)

Goku Mohandas

·
 ·
 ·

[Repository](https://github.com/GokuMohandas/Made-With-ML)
 ·

[Notebook](https://github.com/GokuMohandas/Made-With-ML/blob/main/notebooks/02_Python.ipynb)

×

Subscribe to our newsletter

📬  Receive new lessons straight to your inbox (once a month) and join **40K+**
developers in learning how to responsibly deliver value with ML.

Subscribe

---

## Variables

Variables are containers for holding data and they're defined by a name and value.

![python variables](/static/images/foundations/python/variables.png)

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Integer variable x = 5 print (x) print (type(x)) ``` |

```
5
<class 'int'>
```

> Here we use the variable name `x` in our examples but when you're working on a specific task, be sure to be explicit (ex. `first_name`) when creating variables (applies to functions, classes, etc. as well).

We can change the value of a variable by simply assigning a new value to it.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # String variable x = "hello" print (x) print (type(x)) ``` |

```
hello
<class 'str'>
```

There are many different types of variables: integers, floats, strings, boolean etc.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # int variable x = 5 print (x, type(x)) ``` |

```
5 <class 'int'>
```

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # float variable x = 5.0 print (x, type(x)) ``` |

```
5.0 <class 'float'>
```

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # text variable x = "5" print (x, type(x)) ``` |

```
5 <class 'str'>
```

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # boolean variable x = True print (x, type(x)) ``` |

```
True <class 'bool'>
```

We can also do operations with variables:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Variables can be used with each other a = 1 b = 2 c = a + b print (c) ``` |

```
3
```

Know your types!

We should always know what types of variables we're dealing with so we can do the right operations with them. Here's a common mistake that can happen if we're using the wrong variable type.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # int variables a = 5 b = 3 print (a + b) ``` |

Show answer

```
8
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # string variables a = "5" b = "3" print (a + b) ``` |

Show answer

```
53
```

## Lists

Lists are an ordered, mutable (changeable) collection of values that are comma separated and enclosed by square brackets. A list can be comprised of many different types of variables. Below is a list with an integer, string and a float:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Creating a list x = [3, "hello", 1.2] print (x) ``` |

```
[3, 'hello', 1.2]
```

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Length of a list len(x) ``` |

```
3
```

We can add to a list by using the append function:

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Adding to a list x.append(7) print (x) print (len(x)) ``` |

```
[3, 'hello', 1.2, 7]
4
```

and just as easily replace existing items:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Replacing items in a list x[1] = "bye" print (x) ``` |

```
[3, 'bye', 1.2, 7]
```

and perform operations with lists:

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Operations y = [2.4, "world"] z = x + y print (z) ``` |

```
[3, 'bye', 1.2, 7, 2.4, 'world']
```

## Tuples

Tuples are collections that are ordered and immutable (unchangeable). We will use tuples to store values that will never be changed.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Creating a tuple x = (3.0, "hello") # tuples start and end with () print (x) ``` |

```
(3.0, 'hello')
```

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Adding values to a tuple x = x + (5.6, 4) print (x) ``` |

```
(3.0, 'hello', 5.6, 4)
```

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Try to change (it won't work and we get an error) x[0] = 1.2 ``` |

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
----> 1 x[0] = 1.2
TypeError: 'tuple' object does not support item assignment
```

## Sets

Sets are collections that are unordered and mutable. However, every item in a set much be unique.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Sets text = "Learn ML with Made With ML" print (set(text)) print (set(text.split(" "))) ``` |

```
{'e', 'M', ' ', "r", "w", 'd', 'a', 'h', 't', 'i', 'L', 'n', "w"}
{'with', 'Learn', 'ML', 'Made', 'With'}
```

## Indexing

Indexing and slicing from lists allow us to retrieve specific values within lists. Note that indices can be positive (starting from 0) or negative (-1 and lower, where -1 is the last item in the list).

![indexing in python](/static/images/foundations/python/indexing.png)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` # Indexing x = [3, "hello", 1.2] print ("x[0]: ", x[0]) print ("x[1]: ", x[1]) print ("x[-1]: ", x[-1]) # the last item print ("x[-2]: ", x[-2]) # the second to last item ``` |

```
x[0]:  3
x[1]:  hello
x[-1]:  1.2
x[-2]:  hello
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Slicing print ("x[:]: ", x[:]) # all indices print ("x[1:]: ", x[1:]) # index 1 to the end of the list print ("x[1:2]: ", x[1:2]) # index 1 to index 2 (not including index 2) print ("x[:-1]: ", x[:-1]) # index 0 to last index (not including last index) ``` |

```
x[:]:  [3, 'hello', 1.2]
x[1:]:  ['hello', 1.2]
x[1:2]:  ['hello']
x[:-1]:  [3, 'hello']
```

Indexing beyond length

What happens if we try to index beyond the length of a list?

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` x = [3, "hello", 1.2] print (x[:100]) print (len(x[:100])) ``` |

Show answer

```
[3, 'hello', 1.2]
3
```

Though this does produce results, we should always explicitly use the length of the list to index items from it to avoid incorrect assumptions for downstream processes.

## Dictionaries

Dictionaries are an unordered, mutable collection of key-value pairs. You can retrieve values based on the key and a dictionary cannot have two of the same keys.

![python dictionaries](/static/images/foundations/python/dictionaries.png)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` # Creating a dictionary person = {"name": "Goku",           "eye_color": "brown"} print (person) print (person["name"]) print (person["eye_color"]) ``` |

```
{"name": "Goku", "eye_color": "brown"}
Goku
brown
```

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Changing the value for a key person["eye_color"] = "green" print (person) ``` |

```
{"name": "Goku", "eye_color": "green"}
```

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Adding new key-value pairs person["age"] = 24 print (person) ``` |

```
{"name": "Goku", "eye_color": "green", "age": 24}
```

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Length of a dictionary print (len(person)) ``` |

```
3
```

Sort of the structures

See if you can recall and sort out the similarities and differences of the foundational data structures we've seen so far.

|  | Mutable | Ordered | Indexable | Unique |
| --- | --- | --- | --- | --- |
| List | ❓ | ❓ | ❓ | ❓ |
| Tuple | ❓ | ❓ | ❓ | ❓ |
| Set | ❓ | ❓ | ❓ | ❓ |
| Dictionary | ❓ | ❓ | ❓ | ❓ |

Show answer

|  | Mutable | Ordered | Indexable | Unique |
| --- | --- | --- | --- | --- |
| List | ✅ | ✅ | ✅ | ❌ |
| Tuple | ❌ | ✅ | ✅ | ❌ |
| Set | ✅ | ❌ | ❌ | ✅ |
| Dictionary | ✅ | ❌ | ❌ | ✅  keys ❌  values |

But of course, there is pretty much a way to do accomplish anything with Python. For example, even though native dictionaries are unordered, we can leverage the [OrderedDict](https://docs.python.org/3/library/collections.html) data structure to change that (useful if we want to iterate through keys in a certain order, etc.).

|  |  |
| --- | --- |
| ``` 1 ``` | ``` from collections import OrderedDict ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` # Native dict d = {} d["a"] = 2 d["c"] = 3 d["b"] = 1 print (d) ``` |

```
{'a': 2, 'c': 3, 'b': 1}
```

> After Python 3.7+, native dictionaries are insertion ordered.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Dictionary items print (d.items()) ``` |

```
dict_items([('a', 2), ('c', 3), ('b', 1)])
```

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Order by keys print (OrderedDict(sorted(d.items()))) ``` |

```
OrderedDict([('a', 2), ('b', 1), ('c', 3)])
```

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Order by values print (OrderedDict(sorted(d.items(), key=lambda x: x[1]))) ``` |

```
OrderedDict([('b', 1), ('a', 2), ('c', 3)])
```

## If statements

We can use `if` statements to conditionally do something. The conditions are defined by the words `if`, `elif` (which stands for else if) and `else`. We can have as many `elif` statements as we want. The indented code below each condition is the code that will execute if the condition is `True`.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` # If statement x = 4 if x < 1:     score = "low" elif x <= 4: # elif = else if     score = "medium" else:     score = "high" print (score) ``` |

```
medium
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # If statement with a boolean x = True if x:     print ("it worked") ``` |

```
it worked
```

## Loops

### For loops

A `for` loop can iterate over a collection of values (lists, tuples, dictionaries, etc.) The indented code is executed for each item in the collection of values.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # For loop veggies = ["carrots", "broccoli", "beans"] for veggie in veggies:     print (veggie) ``` |

```
carrots
broccoli
beans
```

When the loop encounters the break command, the loop will terminate immediately. If there were more items in the list, they will not be processed.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` # `break` from a for loop veggies = ["carrots", "broccoli", "beans"] for veggie in veggies:     if veggie == "broccoli":         break     print (veggie) ``` |

```
carrots
```

When the loop encounters the `continue` command, the loop will skip all other operations for that item in the list only. If there were more items in the list, the loop will continue normally.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` # `continue` to the next iteration veggies = ["carrots", "broccoli", "beans"] for veggie in veggies:     if veggie == "broccoli":         continue     print (veggie) ``` |

```
carrots
beans
```

### While loops

A `while` loop can perform repeatedly as long as a condition is `True`. We can use `continue` and `break` commands in `while` loops as well.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # While loop x = 3 while x > 0:     x -= 1 # same as x = x - 1     print (x) ``` |

```
2
1
0
```

## List comprehension

We can combine our knowledge of lists and for loops to leverage list comprehensions to create succinct code.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` # For loop x = [1, 2, 3, 4, 5] y = [] for item in x:     if item > 2:         y.append(item) print (y) ``` |

```
[3, 4, 5]
```

![python list comprehension](/static/images/foundations/python/comprehension.png)

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # List comprehension y = [item for item in x if item > 2] print (y) ``` |

```
[3, 4, 5]
```

List comprehension for nested for loops

For the nested for loop below, which list comprehension is correct?

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` # Nested for loops words = [["Am", "ate", "ATOM", "apple"], ["bE", "boy", "ball", "bloom"]] small_words = [] for letter_list in words:     for word in letter_list:         if len(word) < 3:             small_words.append(word.lower()) print (small_words) ``` |

```
['am', 'be']
```

* [ ]  `[word.lower() if len(word) < 3 for word in letter_list for letter_list in words]`
* [ ]  `[word.lower() for word in letter_list for letter_list in words if len(word) < 3]`
* [ ]  `[word.lower() for letter_list in words for word in letter_list if len(word) < 3]`

Show answer

Python syntax is usually very straight forward, so the correct answer involves just directly copying the statements from the nested for loop from top to bottom!

* [ ]  `[word.lower() if len(word) < 3 for word in letter_list for letter_list in words]`
* [ ]  `[word.lower() for word in letter_list for letter_list in words if len(word) < 3]`
* [x]  `[word.lower() for letter_list in words for word in letter_list if len(word) < 3]`

## Functions

Functions are a way to modularize reusable pieces of code. They're defined by the keyword `def` which stands for definition and they can have the following components.

![python functions](/static/images/foundations/python/functions.png)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Define the function def add_two(x):     """Increase x by 2."""     x += 2     return x ``` |

Here are the components that may be required when we want to use the function. we need to ensure that the function name and the input parameters match with how we defined the function above.

![using python functions](/static/images/foundations/python/calling_functions.png)

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Use the function score = 0 new_score = add_two(x=score) print (new_score) ``` |

```
2
```

A function can have as many input parameters and outputs as we want.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Function with multiple inputs def join_name(first_name, last_name):     """Combine first name and last name."""     joined_name = first_name + " " + last_name     return joined_name ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` # Use the function first_name = "Goku" last_name = "Mohandas" joined_name = join_name(     first_name=first_name, last_name=last_name) print (joined_name) ``` |

```
Goku Mohandas
```

> We can be even more explicit with our function definitions by specifying the [types](../../mlops/documentation/#typing) of our input and output arguments. We cover this in our [documentation lesson](../../mlops/documentation/) because the typing information is automatically leveraged to create very intuitive [documentation](https://gokumohandas.github.io/Made-With-ML).

It's good practice to always use keyword argument when using a function so that it's very clear what input variable belongs to what function input parameter. On a related note, you will often see the terms `*args` and `**kwargs` which stand for arguments and keyword arguments. You can extract them when they are passed into a function. The significance of the `*` is that any number of arguments and keyword arguments can be passed into the function.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` def f(*args, **kwargs):     x = args[0]     y = kwargs.get("y")     print (f"x: {x}, y: {y}") ``` |

|  |  |
| --- | --- |
| ``` 1 ``` | ``` f(5, y=2) ``` |

```
x: 5, y: 2
```

## Classes

Classes are object constructors and are a fundamental component of object oriented programming in Python. They are composed of a set of functions that define the class and it's operations.

### Magic methods

Classes can be customized with magic methods like `__init__` and `__str__`, to enable powerful operations. These are also known as dunder methods (ex. dunder init), which stands for `d`ouble `under`scores due to the leading and trailing underscores.

The `__init__` function is used when an instance of the class is initialized.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` # Creating the class class Pet(object):     """Class object for a pet."""      def __init__(self, species, name):         """Initialize a Pet."""         self.species = species         self.name = name ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Creating an instance of a class my_dog = Pet(species="dog",              name="Scooby") print (my_dog) print (my_dog.name) ``` |

```
<__main__.Pet object at 0x7fe487e9c358>
Scooby
```

The `print (my_dog)` command printed something not so relevant to us. Let's fix that with the `__str__` function.

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 ``` | ``` # Creating the class # Creating the class class Pet(object):     """Class object for a pet."""      def __init__(self, species, name):         """Initialize a Pet."""         self.species = species         self.name = name      def __str__(self):         """Output when printing an instance of a Pet."""         return f"{self.species} named {self.name}" ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Creating an instance of a class my_dog = Pet(species="dog",              name="Scooby") print (my_dog) print (my_dog.name) ``` |

```
dog named Scooby
Scooby
```

> We'll be exploring additional built-in functions in subsequent notebooks (like `__len__`, `__iter__` and `__getitem__`, etc.) but if you're curious, here is a [tutorial](https://rszalski.github.io/magicmethods/) on more magic methods.

### Object functions

Besides these magic functions, classes can also have *object* functions.

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 ``` | ``` # Creating the class class Pet(object):     """Class object for a pet."""      def __init__(self, species, name):         """Initialize a Pet."""         self.species = species         self.name = name      def __str__(self):         """Output when printing an instance of a Pet."""         return f"{self.species} named {self.name}"      def change_name(self, new_name):         """Change the name of your Pet."""         self.name = new_name ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Creating an instance of a class my_dog = Pet(species="dog", name="Scooby") print (my_dog) print (my_dog.name) ``` |

```
dog named Scooby
Scooby
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Using a class's function my_dog.change_name(new_name="Scrappy") print (my_dog) print (my_dog.name) ``` |

```
dog named Scrappy
Scrappy
```

### Inheritance

We can also build classes on top of one another using inheritance, which allows us to inherit all the properties and methods from another class (the parent).

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` class Dog(Pet):     def __init__(self, name, breed):         super().__init__(species="dog", name=name)         self.breed = breed      def __str__(self):         return f"A {self.breed} doggo named {self.name}" ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` scooby = Dog(species="dog", breed="Great Dane", name="Scooby") print (scooby) ``` |

```
A Great Dane doggo named Scooby
```

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` scooby.change_name("Scooby Doo") print (scooby) ``` |

```
A Great Dane doggo named Scooby Doo
```

Notice how we inherited the initialized variables from the parent `Pet` class like species and name. We also inherited functions such as `change_name()`.

Which function is executed?

Which function is executed if the parent and child functions have functions with the same name?

Show answer

As you can see, both our parent class (`Pet`) and the child class (`Dog`) have different `__str__` functions defined but share the same function name. The child class inherits everything from the parent classes but when there is conflict between function names, the child class' functions take precedence and overwrite the parent class' functions.

### Methods

There are two important decorator methods to know about when it comes to classes: `@classmethod` and `@staticmethod`. We'll learn about decorators in the next section below but these specific methods pertain to classes so we'll cover them here.

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 ``` | ``` class Dog(Pet):     def __init__(self, name, breed):         super().__init__(species="dog", name=name)         self.breed = breed      def __str__(self):         return f"{self.breed} named {self.name}"      @classmethod     def from_dict(cls, d):         return cls(name=d["name"], breed=d["breed"])      @staticmethod     def is_cute(breed):         return True  # all animals are cute! ``` |

A `@classmethod` allows us to create class instances by passing in the uninstantiated class itself (`cls`). This is a great way to create (or load) classes from objects (ie. dictionaries).

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Create instance d = {"name": "Cassie", "breed": "Border Collie"} cassie = Dog.from_dict(d=d) print(cassie) ``` |

```
Border Collie named Cassie
```

A `@staticmethod` can be called from an uninstantiated class object so we can do things like this:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Static method Dog.is_cute(breed="Border Collie") ``` |

```
True
```

## Decorators

Recall that functions allow us to modularize code and reuse them. However, we'll often want to add some functionality before or after the main function executes and we may want to do this for many different functions. Instead of adding more code to the original function, we can use decorators!

* **decorators**: augment a function with pre/post-processing. Decorators wrap around the main function and allow us to operate on the inputs and or outputs.

Suppose we have a function called operations which increments the input value x by 1.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` def operations(x):     """Basic operations."""     x += 1     return x ``` |

|  |  |
| --- | --- |
| ``` 1 ``` | ``` operations(x=1) ``` |

```
2
```

Now let's say we want to increment our input x by 1 before and after the operations function executes and, to illustrate this example, let's say the increments have to be separate steps. Here's how we would do it by changing the original code:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` def operations(x):     """Basic operations."""     x += 1     x += 1     x += 1     return x ``` |

|  |  |
| --- | --- |
| ``` 1 ``` | ``` operations(x=1) ``` |

```
4
```

We were able to achieve what we want but we now increased the size of our `operations` function and if we want to do the same incrementing for any other function, we have to add the same code to all of those as well ... not very efficient. To solve this, let's create a decorator called `add` which increments `x` by 1 before and after the main function `f` executes.

### Creating a decorator

The decorator function accepts a function `f` which is the function we wish to wrap around, in our case, it's `operations()`. The output of the decorator is its `wrapper` function which receives the arguments and keyword arguments passed to function `f`.

Inside the `wrapper` function, we can:

1. extract the input parameters passed to function `f`.
2. make any changes we want to the function inputs.
3. function `f` is executed
4. make any changes to the function outputs
5. `wrapper` function returns some value(s), which is what the decorator returns as well since it returns `wrapper`.

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 ``` | ``` # Decorator def add(f):     def wrapper(*args, **kwargs):         """Wrapper function for @add."""         x = kwargs.pop("x") # .get() if not altering x         x += 1 # executes before function f         x = f(*args, **kwargs, x=x)         x += 1 # executes after function f         return x     return wrapper ``` |

We can use this decorator by simply adding it to the top of our main function preceded by the `@` symbol.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` @add def operations(x):     """Basic operations."""     x += 1     return x ``` |

|  |  |
| --- | --- |
| ``` 1 ``` | ``` operations(x=1) ``` |

```
4
```

Suppose we wanted to debug and see what function actually executed with `operations()`.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` operations.__name__, operations.__doc__ ``` |

```
('wrapper', 'Wrapper function for @add.')
```

The function name and docstring are not what we're looking for but it appears this way because the `wrapper` function is what was executed. In order to fix this, Python offers `functools.wraps` which carries the main function's metadata.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` from functools import wraps ``` |

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 ``` | ``` # Decorator def add(f):     @wraps(f)     def wrap(*args, **kwargs):         """Wrapper function for @add."""         x = kwargs.pop("x")         x += 1         x = f(*args, **kwargs, x=x)         x += 1         return x     return wrap ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` @add def operations(x):     """Basic operations."""     x += 1     return x ``` |

|  |  |
| --- | --- |
| ``` 1 ``` | ``` operations.__name__, operations.__doc__ ``` |

```
('operations', 'Basic operations.')
```

Awesome! We were able to decorate our main function `operation()` to achieve the customization we wanted without actually altering the function. We can reuse our decorator for other functions that may need the same customization!

> This was a dummy example to show how decorators work but we'll be using them heavily during our [MLOps](https://madewithml.com/courses/mlops/) lessons. A simple scenario would be using decorators to create uniform JSON responses from each API endpoint without including the bulky code in each endpoint.

### Callbacks

Decorators allow for customized operations before and after the main function's execution but what about in between? Suppose we want to conditionally/situationally do some operations. Instead of writing a whole bunch of if-statements and make our functions bulky, we can use callbacks!

* **callbacks**: conditional/situational processing within the function.

Our callbacks will be classes that have functions with key names that will execute at various periods during the main function's execution. The function names are up to us but we need to invoke the same callback functions within our main function.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` # Callback class x_tracker(object):     def __init__(self, x):         self.history = []     def at_start(self, x):         self.history.append(x)     def at_end(self, x):         self.history.append(x) ``` |

We can pass in as many callbacks as we want and because they have appropriately named functions, they will be invoked at the appropriate times.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` def operations(x, callbacks=[]):     """Basic operations."""     for callback in callbacks:         callback.at_start(x)     x += 1     for callback in callbacks:         callback.at_end(x)     return x ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` x = 1 tracker = x_tracker(x=x) operations(x=x, callbacks=[tracker]) ``` |

```
2
```

|  |  |
| --- | --- |
| ``` 1 ``` | ``` tracker.history ``` |

```
[1, 2]
```

What's the difference compared to a decorator?

It seems like we've just done some operations before and after the function's main process? Isn't that what a decorator is for?

Show answer

With callbacks, it's easier to keep track of objects since it's all defined in a separate callback class. It's also now possible to interact with our function, not just before or after but throughout the entire process! Imagine a function with:

* multiple processes where we want to execute operations in between them
* execute operations repeatedly when loops are involved in functions

### Putting it all together

decorators + callbacks = powerful customization before, during and after the main function’s execution without increasing its complexity. We will be using this duo to create powerful ML training scripts that are highly customizable in future lessons.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` from functools import wraps ``` |

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 ``` | ``` # Decorator def add(f):     @wraps(f)     def wrap(*args, **kwargs):         """Wrapper function for @add."""         x = kwargs.pop("x") # .get() if not altering x         x += 1 # executes before function f         x = f(*args, **kwargs, x=x)         # can do things post function f as well         return x     return wrap ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` # Callback class x_tracker(object):     def __init__(self, x):         self.history = [x]     def at_start(self, x):         self.history.append(x)     def at_end(self, x):         self.history.append(x) ``` |

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 ``` | ``` # Main function @add def operations(x, callbacks=[]):     """Basic operations."""     for callback in callbacks:         callback.at_start(x)     x += 1     for callback in callbacks:         callback.at_end(x)     return x ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` x = 1 tracker = x_tracker(x=x) operations(x=x, callbacks=[tracker]) ``` |

```
3
```

|  |  |
| --- | --- |
| ``` 1 ``` | ``` tracker.history ``` |

```
[1, 2, 3]
```

---

To cite this content, please use:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` @article{madewithml,     author       = {Goku Mohandas},     title        = { Python - Made With ML },     howpublished = {\url{https://madewithml.com/}},     year         = {2023} } ``` |

[![](/static/images/anyscale-white-text.svg)](https://www.anyscale.com?utm_source=madewithmml&utm_medium=website&utm_campaign=footer) © 2025 Anyscale, Inc.
 [Anyscale Privacy Policy](https://www.anyscale.com/privacy-policy)

Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
