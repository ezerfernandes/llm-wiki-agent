[ ]
[ ]

[Skip to content](#overview)

Try Ray with $100 credit — [Start Now](https://console.anyscale.com/register/ha?utm_source=made_with_ml&utm_medium=website&utm_campaign=banner)

[![logo](../../../static/images/logo.png)](../../.. "Made With ML by Anyscale")

Made With ML by Anyscale

Machine Learning Product Design

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
  + [x]

    🎨   Design

    🎨   Design
    - [Setup](../setup/)
    - [ ]

      Product
      [Product](./)

      Table of contents
      * [Overview](#overview)
      * [Template](#template)
      * [Product design](#product-design)

        + [Background](#background)
        + [Value proposition](#value-proposition)
        + [Objectives](#objectives)
        + [Solution](#solution)
        + [Feasibility](#feasibility)
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
  + [ ]

    📦   Utilities

    📦   Utilities
    - [Logging](../logging/)
    - [Documentation](../documentation/)
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

* [Overview](#overview)
* [Template](#template)
* [Product design](#product-design)

  + [Background](#background)
  + [Value proposition](#value-proposition)
  + [Objectives](#objectives)
  + [Solution](#solution)
  + [Feasibility](#feasibility)

# Machine Learning Product Design

[View all lessons](/courses/ml_canvas)

---

An overview of the machine learning product design process.

![Goku Mohandas](/static/images/goku_circle.png)

Goku Mohandas

·
 ·
 ·

×

Subscribe to our newsletter

📬  Receive new lessons straight to your inbox (once a month) and join **40K+**
developers in learning how to responsibly deliver value with ML.

Subscribe

---

## Overview

Before we start developing any machine learning models, we need to first motivate and design our application. While this is a technical course, this initial product design process is extremely crucial for creating great products. We'll focus on the product design aspects of our application in this lesson and the systems design aspects in the [next lesson](../systems-design/).

## Template

The template below is designed to guide machine learning product development. It involves both the product and systems design ([next lesson](../systems-design/)) aspects of our application:

[Product design](./) (*What* & *Why*) → [Systems design](../systems-design/) (*How*)

[![machine learning canvas](/static/images/mlops/design/ml_canvas.png)](/static/templates/ml-canvas.pdf)

> 👉   Download a PDF of the ML canvas to use for your own products → [ml-canvas.pdf](/static/templates/ml-canvas.pdf) (right click the link and hit "Save Link As...")

## Product design

Motivate the need for the product and outline the objectives and impact.

Note

Each section below has a part called "Our task", which will discuss how the specific topic relates to the application that we will be building.

### Background

Set the scene for what we're trying to do through a user-centric approach:

* `users`: profile/persona of our users
* `goals`: our users' main goals
* `pains`: obstacles preventing our users from achieving their goals

Our task

* `users`: machine learning developers and researchers.
* `goals`: stay up-to-date on ML content for work, knowledge, etc.
* `pains`: too much unlabeled content scattered around the internet.

### Value proposition

Propose the value we can create through a product-centric approach:

* `product`: what needs to be built to help our users reach their goals?
* `alleviates`: how will the product reduce pains?
* `advantages`: how will the product create gains?

Our task

We will build a platform that helps machine learning developers and researchers stay up-to-date on ML content. We'll do this by discovering and categorizing content from popular sources (Reddit, Twitter, etc.) and displaying it on our platform. For simplicity, assume that we already have a pipeline that delivers ML content from popular sources to our platform. We will just focus on developing the ML service that can correctly categorize the content.

* `product`: a service that discovers and categorizes ML content from popular sources.
* `alleviates`: display categorized content for users to discover.
* `advantages`: when users visit our platform to stay up-to-date on ML content, they don't waste time searching for that content themselves in the noisy internet.

![product mockup](/static/images/mlops/design/product.png)

### Objectives

Breakdown the product into key objectives that we want to focus on.

Our task

* Discover ML content from trusted sources to bring into our platform.
* Classify incoming content for our users to easily discover. **[OUR FOCUS]**
* Display categorized content on our platform (recent, popular, recommended, etc.)

### Solution

Describe the solution required to meet our objectives, including its:

* `core features`: key features that will be developed.
* `integration`: how the product will integrate with other services.
* `alternatives`: alternative solutions that we should considered.
* `constraints`: limitations that we need to be aware of.
* `out-of-scope.`: features that we will not be developing for now.

Our task

Develop a model that can classify the content so that it can be organized by category (tag) on our platform.

`Core features`:

* predict the correct tag for a given content. **[OUR FOCUS]**
* user feedback process for incorrectly classified content.
* workflows to categorize ML content that our model is incorrect / unsure about.

`Integrations`:

* ML content from reliable sources will be sent to our service for classification.

`Alternatives`:

* allow users to add content manually and classify them (noisy, cold start, etc.)

`Constraints`:

* maintain low latency (>100ms) when classifying incoming content. **[Latency]**
* only recommend tags from our list of approved tags. **[Security]**
* avoid duplicate content from being added to the platform. **[UI/UX]**

`Out-of-scope`:

* identify relevant tags beyond our approved list of tags (`natural-language-processing`, `computer-vision`, `mlops` and `other`).
* using full-text HTML from content links to aid in classification.

### Feasibility

How feasible is our solution and do we have the required resources to deliver it (data, $, team, etc.)?

Our task

We have a [dataset](https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/dataset.csv) with ML content that has been labeled. We'll need to assess if it has the necessary signals to meet our [objectives](#objectives).

| Sample data point | |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` {     "id": 443,     "created_on": "2020-04-10 17:51:39",     "title": "AllenNLP Interpret",     "description": "A Framework for Explaining Predictions of NLP Models",     "tag": "natural-language-processing" } ``` |

Now that we've set up the product design requirements for our ML service, let's move on to the systems design requirements in the [next lesson](../systems-design/).

---

Upcoming live cohorts

Sign up for our upcoming live cohort, where we'll provide **live lessons + QA**, **compute (GPUs)** and **community** to learn everything in one day.

Learn more

---

To cite this content, please use:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` @article{madewithml,     author       = {Goku Mohandas},     title        = { Product - Made With ML },     howpublished = {\url{https://madewithml.com/}},     year         = {2023} } ``` |

[![](/static/images/anyscale-white-text.svg)](https://www.anyscale.com?utm_source=madewithmml&utm_medium=website&utm_campaign=footer) © 2025 Anyscale, Inc.
 [Anyscale Privacy Policy](https://www.anyscale.com/privacy-policy)

Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
