[ ]
[ ]

[Skip to content](#intuition)

Try Ray with $100 credit — [Start Now](https://console.anyscale.com/register/ha?utm_source=made_with_ml&utm_medium=website&utm_campaign=banner)

[![logo](../../../static/images/logo.png)](../../.. "Made With ML by Anyscale")

Made With ML by Anyscale

Versioning Code, Data and Models

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
  + [x]

    ♻️   Reproducibility

    ♻️   Reproducibility
    - [ ]

      Versioning
      [Versioning](./)

      Table of contents
      * [Intuition](#intuition)
      * [Code](#code)
      * [Artifacts](#artifacts)

        + [Data](#data)
        + [Models](#models)
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
* [Code](#code)
* [Artifacts](#artifacts)

  + [Data](#data)
  + [Models](#models)

# Versioning Code, Data and Models

[View all lessons](/courses/mlops)

---

Versioning code, data and models to ensure reproducible behavior in ML systems.

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

In this lesson, we're going to learn how to version our code, data and models to ensure reproducible behavior in our ML systems. It's imperative that we can reproduce our results and track changes to our system so we can debug and improve our application. Without it, it would be difficult to share our work, recreate our models in the event of system failures and fallback to previous versions in the event of regressions.

## Code

To version our code, we'll be using [git](https://git-scm.com/), which is a widely adopted version control system. In fact, when we cloned our repository in the [setup lesson](../setup/), we pulled code from a git repository that we had prepared for you.

```
git clone https://github.com/GokuMohandas/Made-With-ML.git .
```

We can then make changes to the code and Git, which is running locally on our computer, will keep track of our files and it's versions as we `add` and `commit` our changes. But it's not enough to just version our code locally, we need to `push` our work to a central location that can be `pull`ed by us and others we want to grant access to. This is where remote repositories like [GitHub](https://github.com/), [GitLab](https://gitlab.com/), [BitBucket](https://bitbucket.org/), etc. provide a remote location to hold our versioned code in.

![git environment](/static/images/mlops/git/environments.png)

Here's a simplified workflow for how we version our code using GitHub:

```
[make changes to code]
git add .
git commit -m "message"
git push origin <branch-name>
```

Tip

If you're not familiar with Git, we highly recommend going through our [Git lesson](../git/) to learn the basics.

## Artifacts

While Git is ideal for saving our code, it's not ideal for saving artifacts like our datasets (especially unstructured data like text or images) and models. Also, recall that Git stores every version of our files and so large files that change frequently can very quickly take up space. So instead, it would be ideal if we can save locations (pointers) to these large artifacts in our code as opposed to the artifacts themselves. This way, we can version the locations of our artifacts and pull them as they're needed.

![data versioning](/static/images/mlops/versioning/versioning.png)

### Data

While we're saving our dataset on GitHub for easy course access (and because our dataset is small), in a production setting, we would use a remote blob storage like S3 or a data warehouse like Snowflake. There are also many tools available for versioning our data, such as [GitLFS](https://git-lfs.github.com/), [Dolt](https://github.com/dolthub/dolt), [Pachyderm](https://www.pachyderm.com/), [DVC](https://dvc.org/), etc. With any of these solutions, we would be pointing to our remote storage location and versioning the pointer locations (ex. S3 bucket path) to our data instead of the data itself.

### Models

And similarly, we currently store our models locally where the [MLflow](../experiment-tracking/#setup) artifact and backend store are local directories.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` # Config MLflow MODEL_REGISTRY = Path("/tmp/mlflow") Path(MODEL_REGISTRY).mkdir(parents=True, exist_ok=True) MLFLOW_TRACKING_URI = "file://" + str(MODEL_REGISTRY.absolute()) mlflow.set_tracking_uri(MLFLOW_TRACKING_URI) print (mlflow.get_tracking_uri()) ``` |

In a production setting, these would be remote such as S3 for the artifact store and a database service (ex. [PostgreSQL RDS](https://aws.amazon.com/rds/postgresql/)) as our backend store. This way, our models can be versioned and others, with the appropriate access credentials, can pull the model artifacts and deploy them.

---

Upcoming live cohorts

Sign up for our upcoming live cohort, where we'll provide **live lessons + QA**, **compute (GPUs)** and **community** to learn everything in one day.

Learn more

---

To cite this content, please use:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` @article{madewithml,     author       = {Goku Mohandas},     title        = { Versioning - Made With ML },     howpublished = {\url{https://madewithml.com/}},     year         = {2023} } ``` |

[![](/static/images/anyscale-white-text.svg)](https://www.anyscale.com?utm_source=madewithmml&utm_medium=website&utm_campaign=footer) © 2025 Anyscale, Inc.
 [Anyscale Privacy Policy](https://www.anyscale.com/privacy-policy)

Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
