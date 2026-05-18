[ ]
[ ]

[Skip to content](#intuition)

Try Ray with $100 credit — [Start Now](https://console.anyscale.com/register/ha?utm_source=made_with_ml&utm_medium=website&utm_campaign=banner)

[![logo](../../../static/images/logo.png)](../../.. "Made With ML by Anyscale")

Made With ML by Anyscale

Moving from Notebooks to Scripts

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
  + [x]

    💻   Developing

    💻   Developing
    - [ ]

      Scripting
      [Scripting](./)

      Table of contents
      * [Intuition](#intuition)
      * [Setup](#setup)
      * [README](#readme)
      * [Scripts](#scripts)

        + [Functions and classes](#functions-and-classes)
        + [Workloads](#workloads)
        + [Config](#config)
        + [Utilities](#utilities)
      * [Ray](#ray)
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
* [Setup](#setup)
* [README](#readme)
* [Scripts](#scripts)

  + [Functions and classes](#functions-and-classes)
  + [Workloads](#workloads)
  + [Config](#config)
  + [Utilities](#utilities)
* [Ray](#ray)

# Moving from Notebooks to Scripts

[View all lessons](/courses/mlops)

---

Organizing Machine Learning Code into individual Python scripts.

![Goku Mohandas](/static/images/goku_circle.png)

Goku Mohandas

·
 ·
 ·

[Repository](https://github.com/GokuMohandas/Made-With-ML)

×

Subscribe to our newsletter

📬  Receive new lessons straight to your inbox (once a month) and join **40K+**
developers in learning how to responsibly deliver value with ML.

Subscribe

---

## Intuition

In this lesson, we'll discuss how to migrate and organize code from our [notebook](https://github.com/GokuMohandas/Made-With-ML/blob/main/notebooks/madewithml.ipynb) to Python scripts. We'll be using [VSCode](https://code.visualstudio.com/) in this course, but feel free to use any editor you feel comfortable with.

Notebooks have been great so far for development. They're interactive, stateful (don't have to rerun code), and allow us to visualize outputs. However, when we want to a develop quality codebase, we need to move to scripts. Here are some reasons why:

* **stateless**: when we run code in a notebook, it's automatically saved to the global state (memory). This is great for experimentation because code and variables will be readily available across different cells. However, this can be very problematic as well because there can be hidden state that we're not aware of. Scripts, on the other hand, are stateless and we have to explicitly pass variables to functions and classes.
* **linear**: in notebooks, the order in which we execute cells matter. This can be problematic because we can easily execute cells out of order. Scripts, on the other hand, are linear and we have to explicitly execute code for each workload.
* **testing**: As we'll see in our [testing lesson](../testing/), it's significantly easier to compose and run tests on scripts, as opposed to Jupyter notebooks. This is crucial for ensuring that we have quality code that works as expected.

## Setup

We already have all the scripts provided in our [repository](https://github.com/GokuMohandas/Made-With-ML) so let's discuss how this was all organized.

## README

It's always a good idea to start organizing our scripts with a `README.md` file. This is where we can organize all of the instructions necessary to walkthrough our codebase. Our README has information on how to set up our environment, how to run our scripts, etc.

> The contents of the `README.md` file is what everyone will see when they visit your [repository](https://github.com/GokuMohandas/Made-With-ML) on GitHub. So, it's a good idea to keep it updated with the latest information.

## Scripts

Let's start by moving our code from notebooks to scripts. We're going to start by creating the different files and directories that we'll need for our project. The exact number and name of these scripts is entirely up to us, however, it's best to organize and choose names that relate to a specific workload. For example, `data.py` will have all of our data related functions and classes. And we can also have scripts for configurations (`config.py`), shared utilities (`utils.py`), etc.

```
madewithml/
├── config.py
├── data.py
├── evaluate.py
├── models.py
├── predict.py
├── serve.py
├── train.py
├── tune.py
└── utils.py
```

> Don't worry about the contents in these files that aren't from our notebooks just yet or if our code looks significantly more [documented](../documentation/). We'll be taking a closer look at those in the respective lessons.

### Functions and classes

Once we have these ready, we can start moving code from our notebooks to the appropriate scripts. It should intuitive in which script a particular function or class belongs to. If not, we need to rethink how the names of our scripts. For example, `train.py` has functions from our notebook such as `train_step`, `val_step`, `train_loop_per_worker`, etc.

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 ``` | ``` # madewithml/train.py def train_step(...):     pass  def val_step(...):     pass  def train_loop_per_worker(...):     pass  ... ``` |

### Workloads

Recall that for training a model, we wrote code in our notebook for setting [configurations](../training/#configurations), [training](../training/#training), etc. that was freeform in a code cell:

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 ``` | ``` # Scaling config scaling_config = ScalingConfig(     num_workers=num_workers,     use_gpu=bool(resources_per_worker["GPU"]),     resources_per_worker=resources_per_worker,     _max_cpu_fraction_per_node=0.8, )  # Checkpoint config checkpoint_config = CheckpointConfig(     num_to_keep=1,     checkpoint_score_attribute="val_loss",     checkpoint_score_order="min", )  ... ``` |

These code cells are not part of a function or class, so we need to wrap them around a function so that we can easily execute that workload. For example, all of this training logic is wrapped inside a `train_model` function in `train.py` that has all the required inputs to execute the workload:

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` # madewithml/train.py def train_model(experiment_name, dataset_loc, ...):     ...      # Scaling config     scaling_config = ScalingConfig(         num_workers=num_workers,         use_gpu=bool(gpu_per_worker),         resources_per_worker={"CPU": cpu_per_worker, "GPU": gpu_per_worker},         _max_cpu_fraction_per_node=0.8,     )      # Checkpoint config     checkpoint_config = CheckpointConfig(         num_to_keep=1,         checkpoint_score_attribute="val_loss",         checkpoint_score_order="min",     )      ... ``` |

> In the next lesson on [command-line interfaces (CLI)](../cli/), we'll learn how to execute these main workloads in our scripts from the command line.

### Config

In addition to our core workload scripts, recall that we also have a `config.py` script. This file will include all of the setup and configuration that all/most of our workloads depend on. For example, setting up our model registry:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Config MLflow MODEL_REGISTRY = Path("/tmp/mlflow") Path(MODEL_REGISTRY).mkdir(parents=True, exist_ok=True) MLFLOW_TRACKING_URI = "file://" + str(MODEL_REGISTRY.absolute()) mlflow.set_tracking_uri(MLFLOW_TRACKING_URI) ``` |

> We wouldn't have configurations like our `ScalingConfig` here because that's specific to our training workload. The `config.py` script is for configurations that are shared across different workloads.

### Utilities

Similarly, we also have a `utils.py` script to include components that will be reused across different scripts. It's a good idea to organize these shared components here as opposed to the core scripts to avoid circular dependency conflicts (two scripts call on functions from each other). Here is an example of one of our utility functions, `set_seeds`, that's used in both our `train.py` and `tune.py` scripts.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` def set_seeds(seed: int = 42):     """Set seeds for reproducibility."""     np.random.seed(seed)     random.seed(seed)     torch.manual_seed(seed)     torch.cuda.manual_seed(seed)     eval("setattr(torch.backends.cudnn, 'deterministic', True)")     eval("setattr(torch.backends.cudnn, 'benchmark', False)")     os.environ["PYTHONHASHSEED"] = str(seed) ``` |

## Ray

Recall in our setup lesson that we initialized Ray inside our notebooks. We still need to initialize Ray before executing our ML workloads via scripts but we can decide to do this only for the scripts with Ray dependent workloads. For example, at the bottom of our `train.py` script, we have:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` # madewithml/train.py if __name__ == "__main__":     if ray.is_initialized():         ray.shutdown()     ray.init()     app()  # initialize Typer app ``` |

Now that we've set up our scripts, we can start executing them from the command line. In the next lesson, we'll learn how to do this with [command-line interfaces (CLI)](../cli/).

---

Upcoming live cohorts

Sign up for our upcoming live cohort, where we'll provide **live lessons + QA**, **compute (GPUs)** and **community** to learn everything in one day.

Learn more

---

To cite this content, please use:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` @article{madewithml,     author       = {Goku Mohandas},     title        = { Scripting - Made With ML },     howpublished = {\url{https://madewithml.com/}},     year         = {2023} } ``` |

[![](/static/images/anyscale-white-text.svg)](https://www.anyscale.com?utm_source=madewithmml&utm_medium=website&utm_campaign=footer) © 2025 Anyscale, Inc.
 [Anyscale Privacy Policy](https://www.anyscale.com/privacy-policy)

Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
