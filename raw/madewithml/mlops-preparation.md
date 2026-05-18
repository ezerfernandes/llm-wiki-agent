[ ]
[ ]

[Skip to content](#intuition)

Try Ray with $100 credit — [Start Now](https://console.anyscale.com/register/ha?utm_source=made_with_ml&utm_medium=website&utm_campaign=banner)

[![logo](../../../static/images/logo.png)](../../.. "Made With ML by Anyscale")

Made With ML by Anyscale

Data Preparation

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
  + [x]

    🔢   Data

    🔢   Data
    - [ ]

      Preparation
      [Preparation](./)

      Table of contents
      * [Intuition](#intuition)

        + [Ingestion](#ingestion)
        + [Splitting](#splitting)
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

* [Intuition](#intuition)

  + [Ingestion](#ingestion)
  + [Splitting](#splitting)

# Data Preparation

[View all lessons](/courses/mlops)

---

Preparing our dataset by ingesting and splitting it.

![Goku Mohandas](/static/images/goku_circle.png)

Goku Mohandas

·
 ·
 ·

[Repository](https://github.com/GokuMohandas/Made-With-ML)
 ·

[Notebook](https://github.com/GokuMohandas/Made-With-ML/blob/main/notebooks/madewithml.ipynb)

×

Subscribe to our newsletter

📬  Receive new lessons straight to your inbox (once a month) and join **40K+**
developers in learning how to responsibly deliver value with ML.

Subscribe

---

## Intuition

We'll start by first preparing our data by ingesting it from source and splitting it into training, validation and test data splits.

### Ingestion

Our data could reside in many different places (databases, files, etc.) and exist in different formats (CSV, JSON, Parquet, etc.). For our application, we'll load the data from a CSV file to a [Pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) using the [`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) function.

> Here is a quick refresher on the [Pandas](../../foundations/pandas/) library.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` import pandas as pd ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Data ingestion DATASET_LOC = "https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/dataset.csv" df = pd.read_csv(DATASET_LOC) df.head() ``` |

|  | id | created\_on | title | description | tag |
| --- | --- | --- | --- | --- | --- |
| 0 | 6 | 2020-02-20 06:43:18 | Comparison between YOLO and RCNN on real world... | Bringing theory to experiment is cool. We can ... | computer-vision |
| 1 | 7 | 2020-02-20 06:47:21 | Show, Infer & Tell: Contextual Inference for C... | The beauty of the work lies in the way it arch... | computer-vision |
| 2 | 9 | 2020-02-24 16:24:45 | Awesome Graph Classification | A collection of important graph embedding, cla... | other |
| 3 | 15 | 2020-02-28 23:55:26 | Awesome Monte Carlo Tree Search | A curated list of Monte Carlo tree search pape... | other |
| 4 | 25 | 2020-03-07 23:04:31 | AttentionWalk | A PyTorch Implementation of "Watch Your Step: ... | other |

> In our [data engineering lesson](../data-engineering/) we'll look at how to continually ingest data from more complex sources (ex. data warehouses)

### Splitting

Next, we need to split our training dataset into `train` and `val` data splits.

1. Use the `train` split to train the model.
   > Here the model will have access to both inputs (features) and outputs (labels) to optimize its internal weights.
2. After each iteration (epoch) through the training split, we will use the `val` split to determine the model's performance.
   > Here the model will not use the labels to optimize its weights but instead, we will use the validation performance to optimize training hyperparameters such as the learning rate, etc.
3. Finally, we will use a separate holdout [`test` dataset](https://github.com/GokuMohandas/Made-With-ML/blob/main/datasets/holdout.csv) to determine the model's performance after training.
   > This is our best measure of how the model may behave on new, unseen data that is from a similar distribution to our training dataset.

Tip

For our application, we will have a [training dataset](https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/dataset.csv) to split into `train` and `val` splits and a **separate** [testing dataset](https://github.com/GokuMohandas/Made-With-ML/blob/main/datasets/holdout.csv) for the `test` set. While we could have one large dataset and split that into the three splits, it's a good idea to have a separate test dataset. Over time, our training data may grow and our test splits will look different every time. This will make it difficult to compare models against other models and against each other.

We can view the class counts in our dataset by using the [`pandas.DataFrame.value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html) function:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` from sklearn.model_selection import train_test_split ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Value counts df.tag.value_counts() ``` |

```
tag
natural-language-processing    310
computer-vision                285
other                          106
mlops                           63
Name: count, dtype: int64
```

For our multi-class task (where each project has exactly one tag), we want to ensure that the data splits have similar class distributions. We can achieve this by specifying how to stratify the split by using the [`stratify`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) keyword argument with sklearn's [`train_test_split()`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) function.

Creating proper data splits

What are the criteria we should focus on to ensure proper data splits?

Show answer

* the dataset (and each data split) should be representative of data we will encounter
* equal distributions of output values across all splits
* shuffle your data if it's organized in a way that prevents input variance
* avoid random shuffles if your task can suffer from data leaks (ex. `time-series`)

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Split dataset test_size = 0.2 train_df, val_df = train_test_split(df, stratify=df.tag, test_size=test_size, random_state=1234) ``` |

How can we validate that our data splits have similar class distributions? We can view the frequency of each class in each split:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Train value counts train_df.tag.value_counts() ``` |

```
tag
natural-language-processing    248
computer-vision                228
other                           85
mlops                           50
Name: count, dtype: int64
```

Before we view our validation split's class counts, recall that our validation split is only `test_size` of the entire dataset. So we need to adjust the value counts so that we can compare it to the training split's class counts.

\[ \alpha \* N\_{test} = N\_{train} \]

\[ N\_{train} = 1 - N\_{test} \]

\[ \alpha = \frac{N\_{train}}{N\_{test}} = \frac{1 - N\_{test}}{N\_{test}} \]

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Validation (adjusted) value counts val_df.tag.value_counts() * int((1-test_size) / test_size) ``` |

```
tag
natural-language-processing    248
computer-vision                228
other                           84
mlops                           52
Name: count, dtype: int64
```

These adjusted counts looks very similar to our train split's counts. Now we're ready to [explore](../exploratory-data-analysis/) our dataset!

---

Upcoming live cohorts

Sign up for our upcoming live cohort, where we'll provide **live lessons + QA**, **compute (GPUs)** and **community** to learn everything in one day.

Learn more

---

To cite this content, please use:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` @article{madewithml,     author       = {Goku Mohandas},     title        = { Preparation - Made With ML },     howpublished = {\url{https://madewithml.com/}},     year         = {2023} } ``` |

[![](/static/images/anyscale-white-text.svg)](https://www.anyscale.com?utm_source=madewithmml&utm_medium=website&utm_campaign=footer) © 2025 Anyscale, Inc.
 [Anyscale Privacy Policy](https://www.anyscale.com/privacy-policy)

Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
