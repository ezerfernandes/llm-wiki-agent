# HuggingFace LLM Course — Chapter 10: Curate high-quality datasets with Argilla
Source: https://huggingface.co/learn/llm-course/chapter10/
Sections: 1,2,3,4,5,6

---

## Section 1: Introduction to Argilla

# Introduction to Argilla[[introduction-to-argilla]]

In Chapter 5 you learnt how to build a dataset using the 🤗 Datasets library and in Chapter 6 you explored how to fine-tune models for some common NLP tasks. In this chapter, you will learn how to use [Argilla](https://argilla.io) to **annotate and curate datasets** that you can use to train and evaluate your models.

The key to training models that perform well is to have high-quality data. Although there are some good datasets in the Hub that you could use to train and evaluate your models, these may not be relevant for your specific application or use case. In this scenario, you may want to build and curate a dataset of your own. Argilla will help you to do this efficiently.

With Argilla you can:

- turn unstructured data into **structured data** to be used in NLP tasks.
- curate a dataset to go from a low-quality dataset to a **high-quality dataset**.
- gather **human feedback** for LLMs and multi-modal models.
- invite experts to collaborate with you in Argilla, or crowdsource annotations!

Here are some of the things that you will learn in this chapter:

- How to set up your own Argilla instance.
- How to load a dataset and configure it based on some popular NLP tasks.
- How to use the Argilla UI to annotate your dataset.
- How to use your curated dataset and export it to the Hub.

---

## Section 2: Set up your Argilla instance

# Set up your Argilla instance[[set-up-your-argilla-instance]]

To start using Argilla, you will need to set up your own Argilla instance first. Then you will need to install the Python SDK so that you can manage Argilla using Python code.

## Deploy the Argilla UI

The easiest way to set up your Argilla instance is through Hugging Face Spaces. To create your Argilla Space, simply follow [this form](https://huggingface.co/new-space?template=argilla%2Fargilla-template-space). If you need further guidance, check the [Argilla quickstart](https://docs.argilla.io/latest/getting_started/quickstart/).

>[!WARNING]
> ⚠️ You may want to enable **Persistent storage** so the data isn't lost if the Space is paused or restarted.
> You can do that from the Settings of your Space.

Once Argilla is up and running, you can log in with your credentials.

## Install and connect the Python SDK

Now you can go to your Python environment or notebook and install the argilla library:

`!pip install argilla`

Let's connect with our Argilla instance. To do that you will need the following information:

- **Your API URL**: This is the URL where Argilla is running. If you are using a Space, you can open the Space, click on the three dots in the top right corner, then "Embed this Space" and copy the **Direct URL**. It should look something like `https://..hf.space`.
- **Your API key**: To get your key, log in to your Argilla instance and go to "My Settings", then copy the API key.
- **Your HF token**: If your Space is private, you will need to an Access Token in your Hugging Face Hub account with writing permissions.

```python
import argilla as rg

HF_TOKEN = "..."  # only for private spaces

client = rg.Argilla(
    api_url="...",
    api_key="...",
    headers={"Authorization": f"Bearer {HF_TOKEN}"},  # only for private spaces
)
```

To check that everything is working properly, we'll call `me`. This should return our user:

```python
client.me
```

If this worked, your Argilla instance is up and running and you're connected to it! Congrats!

We can now get started with loading our first dataset to Argilla.

---

## Section 3: Load your dataset to Argilla

# Load your dataset to Argilla[[load-your-dataset-to-argilla]]

Depending on the NLP task that you're working with and the specific use case or application, your data and the annotation task will look differently. For this section of the course, we'll use [a dataset collecting news](https://huggingface.co/datasets/SetFit/ag_news) to complete two tasks: a text classification on the topic of each text and a token classification to identify the named entities mentioned.

It is possible to import datasets from the Hub using the Argilla UI directly, but we'll be using the SDK to learn how we can make further edits to the data if needed.

## Configure your dataset

The first step is to connect to our Argilla instance as we did in the previous section:

```python
import argilla as rg

HF_TOKEN = "..."  # only for private spaces

client = rg.Argilla(
    api_url="...",
    api_key="...",
    headers={"Authorization": f"Bearer {HF_TOKEN}"},  # only for private spaces
)
```

We can now think about the settings of our dataset in Argilla. These represent the annotation task we'll do over our data. First, we can load the dataset from the Hub and inspect its features, so that we can make sure that we configure the dataset correctly.

```python
from datasets import load_dataset

data = load_dataset("SetFit/ag_news", split="train")
data.features
```

These are the features of our dataset:

```python out
{'text': Value(dtype='string', id=None),
 'label': Value(dtype='int64', id=None),
 'label_text': Value(dtype='string', id=None)}
```

It contains a `text` and also some initial labels for the text classification. We'll add those to our dataset settings together with a `spans` question for the named entities:

```python
settings = rg.Settings(
    fields=[rg.TextField(name="text")],
    questions=[
        rg.LabelQuestion(
            name="label", title="Classify the text:", labels=data.unique("label_text")
        ),
        rg.SpanQuestion(
            name="entities",
            title="Highlight all the entities in the text:",
            labels=["PERSON", "ORG", "LOC", "EVENT"],
            field="text",
        ),
    ],
)
```

Let's dive a bit deeper into what these settings mean. First, we've defined **fields**, these include the information that we'll be annotating. In this case, we only have one field and it comes in the form of a text, so we've choosen a `TextField`.

Then, we define **questions** that represent the tasks that we want to perform on our data:

- For the text classification task we've chosen a `LabelQuestion` and we used the unique values of the `label_text` column as our labels, to make sure that the question is compatible with the labels that already exist in the dataset.
- For the token classification task, we'll need a `SpanQuestion`. We've defined a set of labels that we'll be using for that task, plus the field on which we'll be drawing the spans.

To learn more about all the available types of fields and questions and other advanced settings, like metadata and vectors, go to the [Argilla docs](https://docs.argilla.io/latest/how_to_guides/dataset/#define-dataset-settings).

## Upload the dataset

Now that we've defined some settings, we can create the dataset:

```python
dataset = rg.Dataset(name="ag_news", settings=settings)

dataset.create()
```

The dataset now appears in our Argilla instance, but you will see that it's empty:

Now we need to add the records that we'll be annotating i.e., the rows in our dataset. To do that, we'll simply need to log the data as records and provide a mapping for those elements that don't have the same name in the hub and Argilla datasets:

```python
dataset.records.log(data, mapping={"label_text": "label"})
```

In our mapping, we've specified that the `label_text` column in the dataset should be mapped to the question with the name `label`. In this way, we'll use the existing labels in the dataset as pre-annotations so we can annotate faster.

While the records continue to log, you can already start working with your dataset in the Argilla UI. At this point, it should look like this:

Now our dataset is ready to start annotating!

---

## Section 4: Annotate your dataset

# Annotate your dataset[[annotate-your-dataset]]

Now it is time to start working from the Argilla UI to annotate our dataset.

## Align your team with annotation guidelines

Before you start annotating your dataset, it is always good practice to write some guidelines, especially if you're working as part of a team. This will help you align on the task and the use of the different labels, and resolve questions or conflicts when they come up.

In Argilla, you can go to your dataset settings page in the UI and modify the guidelines and the descriptions of your questions to help with alignment.

If you want to dive deeper into the topic of how to write good guidelines, we recommend reading [this blogpost](https://argilla.io/blog/annotation-guidelines-practices) and the bibliographical references mentioned there.

## Distribute the task

In the dataset settings page, you can also change the dataset distribution settings. This will help you annotate more efficiently when you're working as part of a team. The default value for the minimum submitted responses is 1, meaning that as soon as a record has 1 submitted response it will be considered complete and count towards the progress in your dataset.

Sometimes, you want to have more than one submitted response per record, for example, if you want to analyze the inter-annotator agreement in your task. In that case, make sure to change this setting to a higher number, but always smaller or equal to the total number of annotators. If you're working on the task alone, you want this setting to be 1.

## Annotate records

>[!TIP]
>💡 If you are deploying Argilla in a Hugging Face Space, any team members will be able to log in using the Hugging Face OAuth. Otherwise, you may need to create users for them following [this guide](https://docs.argilla.io/latest/how_to_guides/user/).

When you open your dataset, you will realize that the first question is already filled in with some suggested labels. That's because in the previous section we mapped our question called `label` to the `label_text` column in the dataset, so that we simply need to review and correct the already existing labels:

For the token classification, we'll need to add all labels manually, as we didn't include any suggestions. This is how it might look after the span annotations:

As you move through the different records, there are different actions you can take:
- submit your responses, once you're done with the record.
- save them as a draft, in case you want to come back to them later.
- discard them, if the record souldn't be part of the dataset or you won't give responses to it.

In the next section, you will learn how you can export and use those annotations.

---

## Section 5: Use your annotated dataset

# Use your annotated dataset[[use-your-annotated-dataset]]

We will learn now how to export and use the annotated data that we have in Argilla.

## Load the dataset

First, we'll need to make sure that we're connected to our Argilla instance as in the previous steps:

```python
import argilla as rg

HF_TOKEN = "..."  # only for private spaces

client = rg.Argilla(
    api_url="...",
    api_key="...",
    headers={"Authorization": f"Bearer {HF_TOKEN}"},  # only for private spaces
)
```

And now, we'll load the dataset that we'll be working with:

```python
dataset = client.datasets(name="ag_news")
```

Loading the dataset and calling its records with `dataset.records` is enough to start using your dataset and records for your own purposes and pipelines. However, we'll also learn how to do a few optional operations, like filtering the records and exporting your dataset to the Hugging Face Hub.

## Filter the dataset

Sometimes you only want to use the records that have been completed, so we will first filter the records in our dataset based on their status:

```python
status_filter = rg.Query(filter=rg.Filter([("status", "==", "completed")]))

filtered_records = dataset.records(status_filter)
```

>[!TIP]
>⚠️ Note that the records with `completed` status (i.e., records that meet the minimum submitted responses configured in the task distribution settings) could have more than one response and that each response can have any status from `submitted`, `draft` or `discarded`.

Learn more about querying and filtering records in the [Argilla docs](https://docs.argilla.io/latest/how_to_guides/query/).

## Export to the Hub

We can now export our annotations to the Hugging Face Hub, so we can share them with others. To do this, we'll need to convert the records into a 🤗 Dataset and then push it to the Hub:

```python
filtered_records.to_datasets().push_to_hub("argilla/ag_news_annotated")
```

Alternatively, we can export directly the complete Argilla dataset (including pending records) like this:

```python
dataset.to_hub(repo_id="argilla/ag_news_annotated")
```

This is an interesting choice in case others want to open the dataset in their Argilla instances, as the settings are automatically saved and they can simply import the full dataset using a single line of code:

```python
dataset = rg.Dataset.from_hub(repo_id="argilla/ag_news_annotated")
```

---

## Section 6: Argilla, check!

# Argilla, check![[argilla-check]]

That's all! Congrats! 👏

In this chapter, you learnt the basic steps to:
- set up Argilla.
- annotate to improve the quality of your dataset.
- adapt an existing dataset and re-use it for a different NLP task.
- share your annotated dataset with the community in the Hugging Face Hub.

## What's next?
- Check more step-by-step tutorials for other popular tasks in the [tutorials page](https://docs.argilla.io/latest/tutorials/).
- You can also explore other examples of datasets in this [demo](https://demo.argilla.io/sign-in?auth=ZGVtbzoxMjM0NTY3OA==).
- If you'd like to keep learning about Argilla and more advanced features, check the [Argilla documentation](https://docs.argilla.io/latest/).
