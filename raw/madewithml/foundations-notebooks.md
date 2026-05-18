[ ]
[ ]

[Skip to content](#set-up)

Try Ray with $100 credit — [Start Now](https://console.anyscale.com/register/ha?utm_source=made_with_ml&utm_medium=website&utm_campaign=banner)

[![logo](../../../static/images/logo.png)](../../.. "Made With ML by Anyscale")

Made With ML by Anyscale

Working in Notebooks

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
    - [ ]

      Notebooks
      [Notebooks](./)

      Table of contents
      * [Set up](#set-up)
      * [Types of cells](#types-of-cells)
      * [Text cells](#text-cells)
      * [Run a cell](#run-a-cell)
      * [Edit a cell](#edit-a-cell)
      * [Move a cell](#move-a-cell)
      * [Delete a cell](#delete-a-cell)
      * [Code cells](#code-cells)
    - [Python](../python/)
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

* [Set up](#set-up)
* [Types of cells](#types-of-cells)
* [Text cells](#text-cells)
* [Run a cell](#run-a-cell)
* [Edit a cell](#edit-a-cell)
* [Move a cell](#move-a-cell)
* [Delete a cell](#delete-a-cell)
* [Code cells](#code-cells)

# Working in Notebooks

[View all lessons](/courses/foundations)

---

Learn how to use interactive notebooks for developing in Python.

![Goku Mohandas](/static/images/goku_circle.png)

Goku Mohandas

·
 ·
 ·

[Repository](https://github.com/GokuMohandas/Made-With-ML)
 ·

[Notebook](https://github.com/GokuMohandas/Made-With-ML/blob/main/notebooks/01_Notebooks.ipynb)

×

Subscribe to our newsletter

📬  Receive new lessons straight to your inbox (once a month) and join **40K+**
developers in learning how to responsibly deliver value with ML.

Subscribe

---

## Set up

1. Click on this link to open the accompanying [notebook](https://github.com/GokuMohandas/Made-With-ML/blob/main/notebooks/01_Notebooks.ipynb) for this lesson or create a blank one on [Google Colab](https://colab.research.google.com/).
2. Sign into your [Google account](https://accounts.google.com/signin) to start using the notebook. If you don't want to save your work, you can skip the steps below. If you do not have access to Google, you can follow along using [Jupyter Lab](https://jupyter.org/).
3. If you do want to save your work, click the **COPY TO DRIVE** button on the toolbar. This will open a new notebook in a new tab. Rename this new notebook by removing the words Copy of from the title (change `Copy of 01_Notebooks` to `1_Notebooks`).

![copy to google drive](/static/images/foundations/notebooks/copy_to_drive.png)
  ![rename file](/static/images/foundations/notebooks/rename.png)

Alternatives to Google Colab

Alternatively, you can run these notebooks locally by using [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html). You should first set up a directory for our project, create a [virtual environment](../mlops/packaging.md#virtual-environment) and install jupyterlab.

```
mkdir mlops
python3 -m venv venv
source venv/bin/activate
pip install jupyterlab
jupyter lab
```

## Types of cells

Notebooks are made up of cells. There are two types of cells:

* `code cell`: used for writing and executing code.
* `text cell`: used for writing text, HTML, Markdown, etc.

## Text cells

Click on a desired location in the notebook and create the cell by clicking on the `➕ TEXT` (located in the top left corner).

![text cell](/static/images/foundations/notebooks/text_cell.png)

Once you create the cell, click on it and type the following text inside it:

```
### This is a header
Hello world!
```

## Run a cell

Once you type inside the cell, press the `SHIFT` and `RETURN` (enter key) together to run the cell.

## Edit a cell

To edit a cell, double click on it and make any changes.

## Move a cell

Move a cell up and down by clicking on the cell and then pressing the ⬆ and ⬇ button on the top right of the cell.

![move cell](/static/images/foundations/notebooks/move_cell.png)

## Delete a cell

Delete the cell by clicking on it and pressing the trash can button 🗑️ on the top right corner of the cell. Alternatively, you can also press ⌘/Ctrl + M + D.

![delete cell](/static/images/foundations/notebooks/delete_cell.png)

## Code cells

Repeat the steps above to create and edit a code cell. You can create a code cell by clicking on the `➕ CODE` (located in the top left corner).

![code cell](/static/images/foundations/notebooks/code_cell.png)

Once you've created the code cell, double click on it, type the following inside it and then press Shift + Enter to execute the code.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` print ("Hello world!") ``` |

```
Hello world!
```

These are the basic concepts we'll need to use these notebooks but we'll learn few more tricks in subsequent lessons.

---

To cite this content, please use:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` @article{madewithml,     author       = {Goku Mohandas},     title        = { Notebooks - Made With ML },     howpublished = {\url{https://madewithml.com/}},     year         = {2023} } ``` |

[![](/static/images/anyscale-white-text.svg)](https://www.anyscale.com?utm_source=madewithmml&utm_medium=website&utm_campaign=footer) © 2025 Anyscale, Inc.
 [Anyscale Privacy Policy](https://www.anyscale.com/privacy-policy)

Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
