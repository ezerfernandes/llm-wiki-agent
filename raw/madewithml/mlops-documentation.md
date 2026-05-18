[ ]
[ ]

[Skip to content](#intuition)

Try Ray with $100 credit — [Start Now](https://console.anyscale.com/register/ha?utm_source=made_with_ml&utm_medium=website&utm_campaign=banner)

[![logo](../../../static/images/logo.png)](../../.. "Made With ML by Anyscale")

Made With ML by Anyscale

Documenting Code

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
* [x]

  Course

  Course
  + [Lessons](/#course)
  + [ ]

    🎨   Design

    🎨   Design
    - [Setup](../setup/)
    - [Product](../product-design/)
    - [Systems](../systems-design/)
  + [ ]

    🔢   Data

    🔢   Data
    - [Preparation](../preparation/)
    - [Exploration](../exploratory-data-analysis/)
    - [Preprocessing](../preprocessing/)
    - [Distributed](../distributed-data/)
  + [ ]

    📈   Model

    📈   Model
    - [Training](../training/)
    - [Tracking](../experiment-tracking/)
    - [Tuning](../tuning/)
    - [Evaluation](../evaluation/)
    - [Serving](../serving/)
  + [ ]

    💻   Developing

    💻   Developing
    - [Scripting](../scripting/)
    - [CLI](../cli/)
  + [x]

    📦   Utilities

    📦   Utilities
    - [Logging](../logging/)
    - [ ]

      Documentation
      [Documentation](./)

      Table of contents
      * [Intuition](#intuition)
      * [Typing](#typing)
      * [Docstrings](#docstrings)
      * [Docs](#docs)
      * [Publishing](#publishing)
    - [Styling](../styling/)
    - [Pre-commit](../pre-commit/)
  + [ ]

    ✅   Testing

    ✅   Testing
    - [Code](../testing/)
    - [Data](../testing/#data)
    - [Models](../testing/#models)
  + [ ]

    ♻️   Reproducibility

    ♻️   Reproducibility
    - [Versioning](../versioning/)
  + [ ]

    🚀   Production

    🚀   Production
    - [Jobs & Services](../jobs-and-services/)
    - [CI/CD workflows](../cicd/)
    - [Monitoring](../monitoring/)
    - [Data engineering](../data-engineering/)
* [ ]

  Foundations

  Foundations
  + [Lessons](/courses/foundations/)
  + [ ]

    🛠   Toolkit

    🛠   Toolkit
    - [Notebooks](../../foundations/notebooks/)
    - [Python](../../foundations/python/)
    - [NumPy](../../foundations/numpy/)
    - [Pandas](../../foundations/pandas/)
    - [PyTorch](../../foundations/pytorch/)
  + [ ]

    🔥   Machine Learning

    🔥   Machine Learning
    - [Linear regression](../../foundations/linear-regression/)
    - [Logistic regression](../../foundations/logistic-regression/)
    - [Neural networks](../../foundations/neural-networks/)
    - [Data quality](../../foundations/data-quality/)
    - [Utilities](../../foundations/utilities/)
  + [ ]

    🤖   Deep Learning

    🤖   Deep Learning
    - [CNNs](../../foundations/convolutional-neural-networks/)
    - [Embeddings](../../foundations/embeddings/)
    - [RNNs](../../foundations/recurrent-neural-networks/)
    - [Attention](../../foundations/attention/)
    - [Transformers](../../foundations/transformers/)
* [Subscribe](../../../misc/newsletter/)
* [Community](https://discord.com/channels/1078171187609337896/1078171189169635472)

Table of contents

* [Intuition](#intuition)
* [Typing](#typing)
* [Docstrings](#docstrings)
* [Docs](#docs)
* [Publishing](#publishing)

# Documenting Code

[View all lessons](/courses/mlops)

---

Documenting our code to automatically generate documentation.

![Goku Mohandas](/static/images/goku_circle.png)

Goku Mohandas

·
 ·
 ·

[Repository](https://github.com/GokuMohandas/Made-With-ML)
 ·

[Documentation](https://gokumohandas.github.io/Made-With-ML)

×

Subscribe to our newsletter

📬  Receive new lessons straight to your inbox (once a month) and join **40K+**
developers in learning how to responsibly deliver value with ML.

Subscribe

---

## Intuition

> Code tells you *how*, comments tell you *why*. -- [Jeff Atwood](https://en.wikipedia.org/wiki/Jeff_Atwood)

We can really improve the quality of our codebase by documenting it to make it easier for others (and our future selves) to easily navigate and extend it. We know our code base best the moment we finish writing it but fortunately documenting it will allow us to quickly get back to that familiar state of mind. Documentation can mean many different things to developers, so let's define the most common components:

* `comments`: short descriptions as to why a piece of code exists.
* `typing`: specification of a function's inputs and outputs' data types, providing information pertaining to what a function consumes and produces.
* `docstrings`: meaningful descriptions for functions and classes that describe overall utility, arguments, returns, etc.
* `docs`: rendered webpage that summarizes all the functions, classes, workflows, examples, etc.

## Typing

It's important to be as explicit as possible with our code. We've already discussed choosing explicit names for variables, functions but another way we can be explicit is by defining the types for our function's inputs and outputs by using the [typing library](https://docs.python.org/3/library/typing.html).

So far, our functions have looked like this:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` def some_function(a, b):     return c ``` |

But we can incorporate so much more information using typing:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` from typing import List def some_function(a: List, b: int = 0) -> np.ndarray:     return c ``` |

Here we've defined:

* input parameter `a` is a list
* input parameter `b` is an integer with default value 0
* output parameter `c` is a NumPy array

There are many other data types that we can work with, including `List`, `Set`, `Dict`, `Tuple`, `Sequence` and [more](https://docs.python.org/3/library/typing.html), as well as included types such as `int`, `float`, etc. You can also use types from packages we install (ex. `np.ndarray`) and even from our own defined classes (ex. `LabelEncoder`).

> Starting from Python 3.9+, common types are [built in](https://docs.python.org/3/whatsnew/3.9.html#type-hinting-generics-in-standard-collections) so we don't need to import them with `from typing import List, Set, Dict, Tuple, Sequence` anymore.

## Docstrings

We can make our code even more explicit by adding docstrings to describe overall utility, arguments, returns, exceptions and more. Let's take a look at an example:

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ``` from typing import List def some_function(a: List, b: int = 0) -> np.ndarray:     """Function description.      ```python     c = some_function(a=[], b=0)     print (c)     ```     <pre>     [[1 2]      [3 4]]     </pre>      Args:         a (List): description of `a`.         b (int, optional): description of `b`. Defaults to 0.      Raises:         ValueError: Input list is not one-dimensional.      Returns:         np.ndarray: Description of `c`.      """     return c ``` |

Let's unpack the different parts of this function's docstring:

* `[Line 3]`: Summary of the overall utility of the function.
* `[Lines 5-12]`: Example of how to use our function.
* `[Lines 14-16]`: Description of the function's input arguments.
* `[Lines 18-19]`: Any exceptions that may be raised in the function.
* `[Lines 21-22]`: Description of the function's output(s).

We'll render these docstrings in the [docs](#docs) section below to produce this:

![docstrings](/static/images/mlops/documentation/docstrings.png)

Take a look at the docstrings of different functions and classes in our repository.

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 ``` | ``` # madewithml/data.py from typing import List  def clean_text(text: str, stopwords: List = STOPWORDS) -> str:     """Clean raw text string.      Args:         text (str): Raw text to clean.         stopwords (List, optional): list of words to filter out. Defaults to STOPWORDS.      Returns:         str: cleaned text.     """     pass ``` |

Tip

If using [Visual Studio Code](https://code.visualstudio.com/), be sure to use the [Python Docstrings Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) extension so you can type `"""` under a function and then hit the `Shift` key to generate a template docstring. It will autofill parts of the docstring using the typing information and even exception in your code!

![vscode docstring generation](https://github.com/NilsJPWerner/autoDocstring/blob/13875f7e5d3a2ad2a2a7e42bad6a10d09fed7472/images/demo.gif?raw=true)

## Docs

So we're going through all this effort of including typing and docstrings to our functions but it's all tucked away inside our scripts. What if we can collect all this effort and **automatically** surface it as documentation? Well that's exactly what we'll do with the following open-source packages → final result [here](https://gokumohandas.github.io/Made-With-ML).

1. Initialize mkdocs

   ```
   python3 -m mkdocs new .
   ```

   This will create the following files:

   ```
   .
   ├─ docs/
   │  └─ index.md
   └─ mkdocs.yml
   ```
2. We'll start by overwriting the default `index.md` file in our `docs` directory with information specific to our project:

   | index.md | |
   | --- | --- |
   | ``` 1 2 3 4 5 6 7 8 ``` | ``` ## Documentation - [madewithml](madewithml/config.md): documentation for functions and classes.  ## Course Learn how to combine machine learning with software engineering to design, develop, deploy and iterate on production ML applications.  - Lessons: [https://madewithml.com/](https://madewithml.com/#course) - Code: [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) ``` |
3. Next we'll create documentation files for each script in our `madewithml` directory:

   ```
   mkdir docs/madewithml
   cd docs/madewithml
   touch config.md data.md evaluate.md models.md predict.md serve.md train.md tune.md util.md
   cd ../../
   ```

Tip

It's helpful to have the `docs` directory structure mimic our project's structure as much as possible.

1. Next we'll add `madewithml.<SCRIPT_NAME>` to each file under `docs/madewithml`. This will populate the file with information about the functions and classes (using their docstrings) from `madewithml/<SCRIPT_NAME>.py` thanks to the `mkdocstrings` plugin.

   > Be sure to check out the complete list of [mkdocs plugins](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins).
   >
   > ```
   > # docs/madewithml/data.md
   > ::: madewithml.data
   > ```
2. Finally, we'll add some configurations to our `mkdocs.yml` file that mkdocs automatically created:

   ```
   site_name: Made With ML
   site_url: https://madewithml.com/
   repo_url: https://github.com/GokuMohandas/Made-With-ML/
   nav:
     - Home: index.md
     - madewithml:
       - data: madewithml/data.md
       - models: madewithml/models.md
       - train: madewithml/train.md
       - tune: madewithml/tune.md
       - evaluate: madewithml/evaluate.md
       - predict: madewithml/predict.md
       - serve: madewithml/serve.md
       - utils: madewithml/utils.md
   theme: readthedocs
   plugins:
     - mkdocstrings
   watch:
     - .  # reload docs for any file changes
   ```
3. Serve our documentation locally:

   ```
   python3 -m mkdocs serve
   ```

This will serve our docs at <http://localhost:8000/>:

[![mkdocs](/static/images/mlops/documentation/mkdocs.png)](https://gokumohandas.github.io/Made-With-ML)

## Publishing

We can easily serve our documentation for free using [GitHub pages](https://www.mkdocs.org/user-guide/deploying-your-docs/) for public repositories as wells as [private documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site) for private repositories. And we can even host it on a [custom domain](https://docs.github.com/en/github/working-with-github-pages/configuring-a-custom-domain-for-your-github-pages-site) (ex. company's subdomain).

> Be sure to check out the auto-generated [documentation page](https://gokumohandas.github.io/Made-With-ML) for our [repository](https://github.com/GokuMohandas/Made-With-ML). We'll learn how to automatically generate and update this docs page every time we make changes to our codebase later in our [CI/CD](../cicd/#documentation) lesson.

In the next lesson, we'll learn how to [style and format](../styling/) our codebase in a consistent manner.

---

Upcoming live cohorts

Sign up for our upcoming live cohort, where we'll provide **live lessons + QA**, **compute (GPUs)** and **community** to learn everything in one day.

Learn more

---

To cite this content, please use:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` @article{madewithml,     author       = {Goku Mohandas},     title        = { Documentation - Made With ML },     howpublished = {\url{https://madewithml.com/}},     year         = {2023} } ``` |

[![](/static/images/anyscale-white-text.svg)](https://www.anyscale.com?utm_source=madewithmml&utm_medium=website&utm_campaign=footer) © 2025 Anyscale, Inc.
 [Anyscale Privacy Policy](https://www.anyscale.com/privacy-policy)

Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
