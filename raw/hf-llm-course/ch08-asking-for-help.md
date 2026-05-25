# HuggingFace LLM Course — Chapter 8: How to ask for help
Source: https://huggingface.co/learn/llm-course/chapter8/
Sections: 1,2,3,4,5,6
---

## Section 1: Introduction

# Introduction[[introduction]]

Now that you know how to tackle the most common NLP tasks with 🤗 Transformers, you should be able to get started on your own projects! In this chapter we will explore what to do when you hit a problem. You'll learn how to successfully debug your code or your training, and how to ask the community for help if you don't manage to solve the problem by yourself. And if you think you've found a bug in one of the Hugging Face libraries, we'll show you the best way to report it so that the issue is resolved as quickly as possible.

More precisely, in this chapter you will learn:

- The first thing to do when you get an error
- How to ask for help on the [forums](https://discuss.huggingface.co/)
- How to debug your training pipeline
- How to write a good issue

None of this is specifically related to 🤗 Transformers or the Hugging Face ecosystem, of course; the lessons from this chapter are applicable to most open source projects!

---

## Section 2: What to do when you get an error

# What to do when you get an error[[what-to-do-when-you-get-an-error]]

In this section we'll look at some common errors that can occur when you're trying to generate predictions from your freshly tuned Transformer model. This will prepare you for [section 4](/course/chapter8/section4), where we'll explore how to debug the training phase itself.

We've prepared a [template model repository](https://huggingface.co/lewtun/distilbert-base-uncased-finetuned-squad-d5716d28) for this section, and if you want to run the code in this chapter you'll first need to copy the model to your account on the [Hugging Face Hub](https://huggingface.co). To do so, first log in by running either the following in a Jupyter notebook:

```python
from huggingface_hub import notebook_login

notebook_login()
```

or the following in your favorite terminal:

```bash
huggingface-cli login
```

This will prompt you to enter your username and password, and will save a token under *~/.cache/huggingface/*. Once you've logged in, you can copy the template repository with the following function:

```python
from distutils.dir_util import copy_tree
from huggingface_hub import Repository, snapshot_download, create_repo, get_full_repo_name

def copy_repository_template():
    # Clone the repo and extract the local path
    template_repo_id = "lewtun/distilbert-base-uncased-finetuned-squad-d5716d28"
    commit_hash = "be3eaffc28669d7932492681cd5f3e8905e358b4"
    template_repo_dir = snapshot_download(template_repo_id, revision=commit_hash)
    # Create an empty repo on the Hub
    model_name = template_repo_id.split("/")[1]
    create_repo(model_name, exist_ok=True)
    # Clone the empty repo
    new_repo_id = get_full_repo_name(model_name)
    new_repo_dir = model_name
    repo = Repository(local_dir=new_repo_dir, clone_from=new_repo_id)
    # Copy files
    copy_tree(template_repo_dir, new_repo_dir)
    # Push to Hub
    repo.push_to_hub()
```

Now when you call `copy_repository_template()`, it will create a copy of the template repository under your account.

## Debugging the pipeline from 🤗 Transformers[[debugging-the-pipeline-from-transformers]]

To kick off our journey into the wonderful world of debugging Transformer models, consider the following scenario: you're working with a colleague on a question answering project to help the customers of an e-commerce website find answers about consumer products. Your colleague shoots you a message like:

> G'day! I just ran an experiment using the techniques in [Chapter 7](/course/chapter7/7) of the Hugging Face course and got some great results on SQuAD! I think we can use this model as a starting point for our project. The model ID on the Hub is "lewtun/distillbert-base-uncased-finetuned-squad-d5716d28". Feel free to test it out :)

and the first thing you think of is to load the model using the `pipeline` from 🤗 Transformers:

```python
from transformers import pipeline

model_checkpoint = get_full_repo_name("distillbert-base-uncased-finetuned-squad-d5716d28")
reader = pipeline("question-answering", model=model_checkpoint)
```

```python out
"""
OSError: Can't load config for 'lewtun/distillbert-base-uncased-finetuned-squad-d5716d28'. Make sure that:

- 'lewtun/distillbert-base-uncased-finetuned-squad-d5716d28' is a correct model identifier listed on 'https://huggingface.co/models'

- or 'lewtun/distillbert-base-uncased-finetuned-squad-d5716d28' is the correct path to a directory containing a config.json file
"""
```

Oh no, something seems to have gone wrong! If you're new to programming, these kind of errors can seem a bit cryptic at first (what even is an `OSError`?!). The error displayed here is just the last part of a much larger error report called a _Python traceback_ (aka stack trace). For example, if you're running this code on Google Colab, you should see something like the following screenshot:

There's a lot of information contained in these reports, so let's walk through the key parts together. The first thing to note is that tracebacks should be read _from bottom to top_. This might sound weird if you're used to reading English text from top to bottom, but it reflects the fact that the traceback shows the sequence of function calls that the `pipeline` makes when downloading the model and tokenizer. (Check out [Chapter 2](/course/chapter2) for more details on how the `pipeline` works under the hood.)

> [!TIP]
> 🚨 See that blue box around "6 frames" in the traceback from Google Colab? That's a special feature of Colab, which  compresses the traceback into "frames." If you can't seem to find the source of an error, make sure you expand the full traceback by clicking on those two little arrows.

This means that the last line of the traceback indicates the last error message and gives the name of the exception that was raised. In this case, the exception type is `OSError`, which indicates a system-related error. If we read the accompanying error message, we can see that there seems to be a problem with the model's *config.json* file, and we're given two suggestions to fix it:

```python out
"""
Make sure that:

- 'lewtun/distillbert-base-uncased-finetuned-squad-d5716d28' is a correct model identifier listed on 'https://huggingface.co/models'

- or 'lewtun/distillbert-base-uncased-finetuned-squad-d5716d28' is the correct path to a directory containing a config.json file
"""
```

> [!TIP]
> 💡 If you encounter an error message that is difficult to understand, just copy and paste the message into the Google or [Stack Overflow](https://stackoverflow.com/) search bar (yes, really!). There's a good chance that you're not the first person to encounter the error, and this is a good way to find solutions that others in the community have posted. For example, searching for `OSError: Can't load config for` on Stack Overflow gives several [hits](https://stackoverflow.com/search?q=OSError%3A+Can%27t+load+config+for+) that could be used as a starting point for solving the problem.

The first suggestion is asking us to check whether the model ID is actually correct, so the first order of business is to copy the identifier and paste it into the Hub's search bar:

Hmm, it indeed looks like our colleague's model is not on the Hub... aha, but there's a typo in the name of the model! DistilBERT only has one "l" in its name, so let's fix that and look for "lewtun/distilbert-base-uncased-finetuned-squad-d5716d28" instead:

Okay, this got a hit. Now let's try to download the model again with the correct model ID:

```python
model_checkpoint = get_full_repo_name("distilbert-base-uncased-finetuned-squad-d5716d28")
reader = pipeline("question-answering", model=model_checkpoint)
```

```python out
"""
OSError: Can't load config for 'lewtun/distilbert-base-uncased-finetuned-squad-d5716d28'. Make sure that:

- 'lewtun/distilbert-base-uncased-finetuned-squad-d5716d28' is a correct model identifier listed on 'https://huggingface.co/models'

- or 'lewtun/distilbert-base-uncased-finetuned-squad-d5716d28' is the correct path to a directory containing a config.json file
"""
```

Argh, foiled again -- welcome to the daily life of a machine learning engineer! Since we've fixed the model ID, the problem must lie in the repository itself. A quick way to access the contents of a repository on the 🤗 Hub is via the `list_repo_files()` function of the `huggingface_hub` library:

```python
from huggingface_hub import list_repo_files

list_repo_files(repo_id=model_checkpoint)
```

```python out
['.gitattributes', 'README.md', 'pytorch_model.bin', 'special_tokens_map.json', 'tokenizer_config.json', 'training_args.bin', 'vocab.txt']
```

Interesting -- there doesn't seem to be a *config.json* file in the repository! No wonder our `pipeline` couldn't load the model; our colleague must have forgotten to push this file to the Hub after they fine-tuned it. In this case, the problem seems pretty straightforward to fix: we could ask them to add the file, or, since we can see from the model ID that the pretrained model used was [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased), we can download the config for this model and push it to our repo to see if that resolves the problem. Let's try that. Using the techniques we learned in [Chapter 2](/course/chapter2), we can download the model's configuration with the `AutoConfig` class:

```python
from transformers import AutoConfig

pretrained_checkpoint = "distilbert-base-uncased"
config = AutoConfig.from_pretrained(pretrained_checkpoint)
```

> [!WARNING]
> 🚨 The approach we're taking here is not foolproof, since our colleague may have tweaked the configuration of `distilbert-base-uncased` before fine-tuning the model. In real life, we'd want to check with them first, but for the purposes of this section we'll assume they used the default configuration.

We can then push this to our model repository with the configuration's `push_to_hub()` function:

```python
config.push_to_hub(model_checkpoint, commit_message="Add config.json")
```

Now we can test if this worked by loading the model from the latest commit on the `main` branch:

```python
reader = pipeline("question-answering", model=model_checkpoint, revision="main")

context = r"""
Extractive Question Answering is the task of extracting an answer from a text
given a question. An example of a question answering dataset is the SQuAD
dataset, which is entirely based on that task. If you would like to fine-tune a
model on a SQuAD task, you may leverage the
examples/pytorch/question-answering/run_squad.py script.

🤗 Transformers is interoperable with the PyTorch, TensorFlow, and JAX
frameworks, so you can use your favourite tools for a wide variety of tasks!
"""

question = "What is extractive question answering?"
reader(question=question, context=context)
```

```python out
{'score': 0.38669535517692566,
 'start': 34,
 'end': 95,
 'answer': 'the task of extracting an answer from a text given a question'}
```

Woohoo, it worked! Let's recap what you've just learned:

- The error messages in Python are known as _tracebacks_ and are read from bottom to top. The last line of the error message usually contains the information you need to locate the source of the problem.
- If the last line does not contain sufficient information, work your way up the traceback and see if you can identify where in the source code the error occurs.
- If none of the error messages can help you debug the problem, try searching online for a solution to a similar issue.
- The `huggingface_hub` library provides a suite of tools that you can use to interact with and debug repositories on the Hub.

Now that you know how to debug a pipeline, let's take a look at a trickier example in the forward pass of the model itself.

## Debugging the forward pass of your model[[debugging-the-forward-pass-of-your-model]]

Although the `pipeline` is great for most applications where you need to quickly generate predictions, sometimes you'll need to access the model's logits (say, if you have some custom post-processing that you'd like to apply). To see what can go wrong in this case, let's first grab the model and tokenizer from our `pipeline`:

```python
tokenizer = reader.tokenizer
model = reader.model
```

Next we need a question, so let's see if our favorite frameworks are supported:

```python
question = "Which frameworks can I use?"
```

As we saw in [Chapter 7](/course/chapter7), the usual steps we need to take are tokenizing the inputs, extracting the logits of the start and end tokens, and then decoding the answer span:

```python
import torch

inputs = tokenizer(question, context, add_special_tokens=True)
input_ids = inputs["input_ids"][0]
outputs = model(**inputs)
answer_start_scores = outputs.start_logits
answer_end_scores = outputs.end_logits
# Get the most likely beginning of answer with the argmax of the score
answer_start = torch.argmax(answer_start_scores)
# Get the most likely end of answer with the argmax of the score
answer_end = torch.argmax(answer_end_scores) + 1
answer = tokenizer.convert_tokens_to_string(
    tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end])
)
print(f"Question: {question}")
print(f"Answer: {answer}")
```

```python out
"""
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
/var/folders/28/k4cy5q7s2hs92xq7_h89_vgm0000gn/T/ipykernel_75743/2725838073.py in 
      1 inputs = tokenizer(question, text, add_special_tokens=True)
      2 input_ids = inputs["input_ids"]
----> 3 outputs = model(**inputs)
      4 answer_start_scores = outputs.start_logits
      5 answer_end_scores = outputs.end_logits

~/miniconda3/envs/huggingface/lib/python3.8/site-packages/torch/nn/modules/module.py in _call_impl(self, *input, **kwargs)
   1049         if not (self._backward_hooks or self._forward_hooks or self._forward_pre_hooks or _global_backward_hooks
   1050                 or _global_forward_hooks or _global_forward_pre_hooks):
-> 1051             return forward_call(*input, **kwargs)
   1052         # Do not call functions when jit is used
   1053         full_backward_hooks, non_full_backward_hooks = [], []

~/miniconda3/envs/huggingface/lib/python3.8/site-packages/transformers/models/distilbert/modeling_distilbert.py in forward(self, input_ids, attention_mask, head_mask, inputs_embeds, start_positions, end_positions, output_attentions, output_hidden_states, return_dict)
    723         return_dict = return_dict if return_dict is not None else self.config.use_return_dict
    724
--> 725         distilbert_output = self.distilbert(
    726             input_ids=input_ids,
    727             attention_mask=attention_mask,

~/miniconda3/envs/huggingface/lib/python3.8/site-packages/torch/nn/modules/module.py in _call_impl(self, *input, **kwargs)
   1049         if not (self._backward_hooks or self._forward_hooks or self._forward_pre_hooks or _global_backward_hooks
   1050                 or _global_forward_hooks or _global_forward_pre_hooks):
-> 1051             return forward_call(*input, **kwargs)
   1052         # Do not call functions when jit is used
   1053         full_backward_hooks, non_full_backward_hooks = [], []

~/miniconda3/envs/huggingface/lib/python3.8/site-packages/transformers/models/distilbert/modeling_distilbert.py in forward(self, input_ids, attention_mask, head_mask, inputs_embeds, output_attentions, output_hidden_states, return_dict)
    471             raise ValueError("You cannot specify both input_ids and inputs_embeds at the same time")
    472         elif input_ids is not None:
--> 473             input_shape = input_ids.size()
    474         elif inputs_embeds is not None:
    475             input_shape = inputs_embeds.size()[:-1]

AttributeError: 'list' object has no attribute 'size'
"""
```

Oh dear, it looks like we have a bug in our code! But we're not afraid of a little debugging. You can use the Python debugger in a notebook:

or in a terminal:

Here, reading the error message tells us that `'list' object has no attribute 'size'`, and we can see a `-->` arrow pointing to the line where the problem was raised in `model(**inputs)`. You can debug this interactively using the Python debugger, but for now we'll simply print out a slice of `inputs` to see what we have:

```python
inputs["input_ids"][:5]
```

```python out
[101, 2029, 7705, 2015, 2064]
```

This certainly looks like an ordinary Python `list`, but let's double-check the type:

```python
type(inputs["input_ids"])
```

```python out
list
```

Yep, that's a Python `list` for sure. So what went wrong? Recall from [Chapter 2](/course/chapter2) that the `AutoModelForXxx` classes in 🤗 Transformers operate on _tensors_ (either in PyTorch or TensorFlow), and a common operation is to extract the dimensions of a tensor using `Tensor.size()` in, say, PyTorch. Let's take another look at the traceback, to see which line triggered the exception:

```
~/miniconda3/envs/huggingface/lib/python3.8/site-packages/transformers/models/distilbert/modeling_distilbert.py in forward(self, input_ids, attention_mask, head_mask, inputs_embeds, output_attentions, output_hidden_states, return_dict)
    471             raise ValueError("You cannot specify both input_ids and inputs_embeds at the same time")
    472         elif input_ids is not None:
--> 473             input_shape = input_ids.size()
    474         elif inputs_embeds is not None:
    475             input_shape = inputs_embeds.size()[:-1]

AttributeError: 'list' object has no attribute 'size'
```

It looks like our code tried to call `input_ids.size()`, but this clearly won't work for a Python `list`, which is just a container. How can we solve this problem? Searching for the error message on Stack Overflow gives quite a few relevant [hits](https://stackoverflow.com/search?q=AttributeError%3A+%27list%27+object+has+no+attribute+%27size%27&s=c15ec54c-63cb-481d-a749-408920073e8f). Clicking on the first one displays a similar question to ours, with the answer shown in the screenshot below:

The answer recommends that we add `return_tensors='pt'` to the tokenizer, so let's see if that works for us:

```python out
inputs = tokenizer(question, context, add_special_tokens=True, return_tensors="pt")
input_ids = inputs["input_ids"][0]
outputs = model(**inputs)
answer_start_scores = outputs.start_logits
answer_end_scores = outputs.end_logits
# Get the most likely beginning of answer with the argmax of the score
answer_start = torch.argmax(answer_start_scores)
# Get the most likely end of answer with the argmax of the score
answer_end = torch.argmax(answer_end_scores) + 1
answer = tokenizer.convert_tokens_to_string(
    tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end])
)
print(f"Question: {question}")
print(f"Answer: {answer}")
```

```python out
"""
Question: Which frameworks can I use?
Answer: pytorch, tensorflow, and jax
"""
```

Nice, it worked! This is a great example of how useful Stack Overflow can be: by identifying a similar problem, we were able to benefit from the experience of others in the community. However, a search like this won't always yield a relevant answer, so what can you do in such cases? Fortunately, there is a welcoming community of developers on the [Hugging Face forums](https://discuss.huggingface.co/) that can help you out! In the next section, we'll take a look at how you can craft good forum questions that are likely to get answered.

---

## Section 3: Asking for help on the forums

# Asking for help on the forums[[asking-for-help-on-the-forums]]

The [Hugging Face forums](https://discuss.huggingface.co) are a great place to get help from the open source team and wider Hugging Face community. Here's what the main page looks like on any given day:

On the lefthand side you can see all the categories that the various topics are grouped into, while the righthand side shows the most recent topics. A topic is a post that contains a title, category, and description; it's quite similar to the GitHub issues format that we saw when creating our own dataset in [Chapter 5](/course/chapter5). As the name suggests, the [Beginners](https://discuss.huggingface.co/c/beginners/5) category is primarily intended for people just starting out with the Hugging Face libraries and ecosystem. Any question on any of the libraries is welcome there, be it to debug some code or to ask for help about how to do something. (That said, if your question concerns one library in particular, you should probably head to the corresponding library category on the forum.)

Similarly, the [Intermediate](https://discuss.huggingface.co/c/intermediate/6) and [Research](https://discuss.huggingface.co/c/research/7) categories are for more advanced questions, for example about the libraries or some cool new NLP research that you'd like to discuss.

And naturally, we should also mention the [Course](https://discuss.huggingface.co/c/course/20) category, where you can ask any questions you have that are related to the Hugging Face course!

Once you have selected a category, you'll be ready to write your first topic. You can find some [guidelines](https://discuss.huggingface.co/t/how-to-request-support/3128) in the forum on how to do this, and in this section we'll take a look at some features that make up a good topic.

## Writing a good forum post[[writing-a-good-forum-post]]

As a running example, let's suppose that we're trying to generate embeddings from Wikipedia articles to create a custom search engine. As usual, we load the tokenizer and model as follows:

```python
from transformers import AutoTokenizer, AutoModel

model_checkpoint = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModel.from_pretrained(model_checkpoint)
```

Now suppose we try to embed a whole section of the [Wikipedia article](https://en.wikipedia.org/wiki/Transformers) on Transformers (the franchise, not the library!):

```python
text = """
Generation One is a retroactive term for the Transformers characters that
appeared between 1984 and 1993. The Transformers began with the 1980s Japanese
toy lines Micro Change and Diaclone. They presented robots able to transform
into everyday vehicles, electronic items or weapons. Hasbro bought the Micro
Change and Diaclone toys, and partnered with Takara. Marvel Comics was hired by
Hasbro to create the backstory; editor-in-chief Jim Shooter wrote an overall
story, and gave the task of creating the characthers to writer Dennis O'Neil.
Unhappy with O'Neil's work (although O'Neil created the name "Optimus Prime"),
Shooter chose Bob Budiansky to create the characters.

The Transformers mecha were largely designed by Shōji Kawamori, the creator of
the Japanese mecha anime franchise Macross (which was adapted into the Robotech
franchise in North America). Kawamori came up with the idea of transforming
mechs while working on the Diaclone and Macross franchises in the early 1980s
(such as the VF-1 Valkyrie in Macross and Robotech), with his Diaclone mechs
later providing the basis for Transformers.

The primary concept of Generation One is that the heroic Optimus Prime, the
villainous Megatron, and their finest soldiers crash land on pre-historic Earth
in the Ark and the Nemesis before awakening in 1985, Cybertron hurtling through
the Neutral zone as an effect of the war. The Marvel comic was originally part
of the main Marvel Universe, with appearances from Spider-Man and Nick Fury,
plus some cameos, as well as a visit to the Savage Land.

The Transformers TV series began around the same time. Produced by Sunbow
Productions and Marvel Productions, later Hasbro Productions, from the start it
contradicted Budiansky's backstories. The TV series shows the Autobots looking
for new energy sources, and crash landing as the Decepticons attack. Marvel
interpreted the Autobots as destroying a rogue asteroid approaching Cybertron.
Shockwave is loyal to Megatron in the TV series, keeping Cybertron in a
stalemate during his absence, but in the comic book he attempts to take command
of the Decepticons. The TV series would also differ wildly from the origins
Budiansky had created for the Dinobots, the Decepticon turned Autobot Jetfire
(known as Skyfire on TV), the Constructicons (who combine to form
Devastator),[19][20] and Omega Supreme. The Marvel comic establishes early on
that Prime wields the Creation Matrix, which gives life to machines. In the
second season, the two-part episode The Key to Vector Sigma introduced the
ancient Vector Sigma computer, which served the same original purpose as the
Creation Matrix (giving life to Transformers), and its guardian Alpha Trion.
"""

inputs = tokenizer(text, return_tensors="pt")
logits = model(**inputs).logits
```

```python output
IndexError: index out of range in self
```

Uh-oh, we've hit a problem -- and the error message is far more cryptic than the ones we saw in [section 2](/course/chapter8/section2)! We can't make head or tails of the full traceback, so we decide to turn to the Hugging Face forums for help. How might we craft the topic?

To get started, we need to click the "New Topic" button at the upper-right corner (note that to create a topic, we'll need to be logged in):

This brings up a writing interface where we can input the title of our topic, select a category, and draft the content:

Since the error seems to be exclusively about 🤗 Transformers, we'll select this for the category. Our first attempt at explaining the problem might look something like this:

Although this topic contains the error message we need help with, there are a few problems with the way it is written:

1. The title is not very descriptive, so anyone browsing the forum won't be able to tell what the topic is about without reading the body as well.
2. The body doesn't provide enough information about _where_ the error is coming from and _how_ to reproduce it.
3. The topic tags a few people directly with a somewhat demanding tone.

Topics like this one are not likely to get a fast answer (if they get one at all), so let's look at how we can improve it. We'll start with the first issue of picking a good title.

### Choosing a descriptive title[[choosing-a-descriptive-title]]

If you're trying to get help with a bug in your code, a good rule of thumb is to include enough information in the title so that others can quickly determine whether they think they can answer your question or not. In our running example, we know the name of the exception that's being raised and have some hints that it's triggered in the forward pass of the model, where we call `model(**inputs)`. To communicate this, one possible title could be:

> Source of IndexError in the AutoModel forward pass?

This title tells the reader _where_ you think the bug is coming from, and if they've encountered an `IndexError` before, there's a good chance they'll know how to debug it. Of course, the title can be anything you want, and other variations like:

> Why does my model produce an IndexError?

could also be fine. Now that we've got a descriptive title, let's take a look at improving the body.

### Formatting your code snippets[[formatting-your-code-snippets]]

Reading source code is hard enough in an IDE, but it's even harder when the code is copied and pasted as plain text! Fortunately, the Hugging Face forums support the use of Markdown, so you should always enclose your code blocks with three backticks (```) so it's more easily readable. Let's do this to prettify the error message -- and while we're at it, let's make the body a bit more polite than our original version:

As you can see in the screenshot, enclosing the code blocks in backticks converts the raw text into formatted code, complete with color styling! Also note that single backticks can be used to format inline variables, like we've done for `distilbert-base-uncased`. This topic is looking much better, and with a bit of luck we might find someone in the community who can guess what the error is about. However, instead of relying on luck, let's make life easier by including the traceback in its full gory detail!

### Including the full traceback[[including-the-full-traceback]]

Since the last line of the traceback is often enough to debug your own code, it can be tempting to just provide that in your topic to "save space." Although well intentioned, this actually makes it _harder_ for others to debug the problem since the information that's higher up in the traceback can be really useful too. So, a good practice is to copy and paste the _whole_ traceback, while making sure that it's nicely formatted. Since these tracebacks can get rather long, some people prefer to show them after they've explained the source code. Let's do this. Now, our forum topic looks like the following:

This is much more informative, and a careful reader might be able to point out that the problem seems to be due to passing a long input because of this line in the traceback:

> Token indices sequence length is longer than the specified maximum sequence length for this model (583 > 512).

However, we can make things even easier for them by providing the actual code that triggered the error. Let's do that now.

### Providing a reproducible example[[providing-a-reproducible-example]]

If you've ever tried to debug someone else's code, you've probably first tried to recreate the problem they've reported so you can start working your way through the traceback to pinpoint the error. It's no different when it comes to getting (or giving) assistance on the forums, so it really helps if you can provide a small example that reproduces the error. Half the time, simply walking through this exercise will help you figure out what's going wrong. In any case, the missing piece of our example is to show the _inputs_ that we provided to the model. Doing that gives us something like the following completed example:

This topic now contains quite a lot of information, and it's written in a way that is much more likely to attract the attention of the community and get a helpful answer. With these basic guidelines, you can now create great topics to find the answers to your 🤗 Transformers questions!

---

## Section 4: Debugging the training pipeline

# Debugging the training pipeline[[debugging-the-training-pipeline]]

You've written a beautiful script to train or fine-tune a model on a given task, dutifully following the advice from [Chapter 7](/course/chapter7). But when you launch the command `trainer.train()`, something horrible happens: you get an error 😱! Or worse, everything seems to be fine and the training runs without error, but the resulting model is crappy. In this section, we will show you what you can do to debug these kinds of issues.

## Debugging the training pipeline[[debugging-the-training-pipeline]]

The problem when you encounter an error in `trainer.train()` is that it could come from multiple sources, as the `Trainer` usually puts together lots of things. It converts datasets to dataloaders, so the problem could be something wrong in your dataset, or some issue when trying to batch elements of the datasets together. Then it takes a batch of data and feeds it to the model, so the problem could be in the model code. After that, it computes the gradients and performs the optimization step, so the problem could also be in your optimizer. And even if everything goes well for training, something could still go wrong during the evaluation if there is a problem with your metric.

The best way to debug an error that arises in `trainer.train()` is to manually go through this whole pipeline to see where things went awry. The error is then often very easy to solve.

To demonstrate this, we will use the following script that (tries to) fine-tune a DistilBERT model on the [MNLI dataset](https://huggingface.co/datasets/glue):

```py
from datasets import load_dataset
import evaluate
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
)

raw_datasets = load_dataset("glue", "mnli")

model_checkpoint = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

def preprocess_function(examples):
    return tokenizer(examples["premise"], examples["hypothesis"], truncation=True)

tokenized_datasets = raw_datasets.map(preprocess_function, batched=True)
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)

args = TrainingArguments(
    f"distilbert-finetuned-mnli",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    num_train_epochs=3,
    weight_decay=0.01,
)

metric = evaluate.load("glue", "mnli")

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    return metric.compute(predictions=predictions, references=labels)

trainer = Trainer(
    model,
    args,
    train_dataset=raw_datasets["train"],
    eval_dataset=raw_datasets["validation_matched"],
    compute_metrics=compute_metrics,
)
trainer.train()
```

If you try to execute it, you will be met with a rather cryptic error:

```python out
'ValueError: You have to specify either input_ids or inputs_embeds'
```

### Check your data[[check-your-data]]

This goes without saying, but if your data is corrupted, the `Trainer` is not going to be able to form batches, let alone train your model. So first things first, you need to have a look at what is inside your training set.

To avoid countless hours spent trying to fix something that is not the source of the bug, we recommend you use `trainer.train_dataset` for your checks and nothing else. So let's do that here:

```py
trainer.train_dataset[0]
```

```python out
{'hypothesis': 'Product and geography are what make cream skimming work. ',
 'idx': 0,
 'label': 1,
 'premise': 'Conceptually cream skimming has two basic dimensions - product and geography.'}
```

Do you notice something wrong? This, in conjunction with the error message about `input_ids` missing, should make you realize those are texts, not numbers the model can make sense of. Here, the original error is very misleading because the `Trainer` automatically removes the columns that don't match the model signature (that is, the arguments expected by the model). That means here, everything apart from the labels was discarded. There was thus no issue with creating batches and then sending them to the model, which in turn complained it didn't receive the proper input.

Why wasn't the data processed? We did use the `Dataset.map()` method on the datasets to apply the tokenizer on each sample. But if you look closely at the code, you will see that we made a mistake when passing the training and evaluation sets to the `Trainer`. Instead of using `tokenized_datasets` here, we used `raw_datasets` 🤦. So let's fix this!

```py
from datasets import load_dataset
import evaluate
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
)

raw_datasets = load_dataset("glue", "mnli")

model_checkpoint = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

def preprocess_function(examples):
    return tokenizer(examples["premise"], examples["hypothesis"], truncation=True)

tokenized_datasets = raw_datasets.map(preprocess_function, batched=True)
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)

args = TrainingArguments(
    f"distilbert-finetuned-mnli",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    num_train_epochs=3,
    weight_decay=0.01,
)

metric = evaluate.load("glue", "mnli")

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    return metric.compute(predictions=predictions, references=labels)

trainer = Trainer(
    model,
    args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation_matched"],
    compute_metrics=compute_metrics,
)
trainer.train()
```

This new code will now give a different error (progress!):

```python out
'ValueError: expected sequence of length 43 at dim 1 (got 37)'
```

Looking at the traceback, we can see the error happens in the data collation step:

```python out
~/git/transformers/src/transformers/data/data_collator.py in torch_default_data_collator(features)
    105                 batch[k] = torch.stack([f[k] for f in features])
    106             else:
--> 107                 batch[k] = torch.tensor([f[k] for f in features])
    108 
    109     return batch
```

So, we should move to that. Before we do, however, let's finish inspecting our data, just to be 100% sure it's correct.

One thing you should always do when debugging a training session is have a look at the decoded inputs of your model. We can't make sense of the numbers that we feed it directly, so we should look at what those numbers represent. In computer vision, for example, that means looking at the decoded pictures of the pixels you pass, in speech it means listening to the decoded audio samples, and for our NLP example here it means using our tokenizer to decode the inputs:

```py
tokenizer.decode(trainer.train_dataset[0]["input_ids"])
```

```python out
'[CLS] conceptually cream skimming has two basic dimensions - product and geography. [SEP] product and geography are what make cream skimming work. [SEP]'
```

So that seems correct. You should do this for all the keys in the inputs: 

```py
trainer.train_dataset[0].keys()
```

```python out
dict_keys(['attention_mask', 'hypothesis', 'idx', 'input_ids', 'label', 'premise'])
```

Note that the keys that don't correspond to inputs accepted by the model will be automatically discarded, so here we will only keep `input_ids`, `attention_mask`, and `label` (which will be renamed `labels`). To double-check the model signature, you can print the class of your model, then go check its documentation:

```py
type(trainer.model)
```

```python out
transformers.models.distilbert.modeling_distilbert.DistilBertForSequenceClassification
```

So in our case, we can check the parameters accepted on [this page](https://huggingface.co/transformers/model_doc/distilbert.html#distilbertforsequenceclassification). The `Trainer` will also log the columns it's discarding.

We have checked that the input IDs are correct by decoding them. Next is the `attention_mask`:

```py
trainer.train_dataset[0]["attention_mask"]
```

```python out
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

Since we didn't apply padding in our preprocessing, this seems perfectly natural. To be sure there is no issue with that attention mask, let's check it is the same length as our input IDs:

```py
len(trainer.train_dataset[0]["attention_mask"]) == len(
    trainer.train_dataset[0]["input_ids"]
)
```

```python out
True
```

That's good! Lastly, let's check our label:

```py
trainer.train_dataset[0]["label"]
```

```python out
1
```

Like the input IDs, this is a number that doesn't really make sense on its own. As we saw before, the map between integers and label names is stored inside the `names` attribute of the corresponding *feature* of the dataset:

```py
trainer.train_dataset.features["label"].names
```

```python out
['entailment', 'neutral', 'contradiction']
```

So `1` means `neutral`, which means the two sentences we saw above are not in contradiction, and the first one does not imply the second one. That seems correct!

We don't have token type IDs here, since DistilBERT does not expect them; if you have some in your model, you should also make sure that they properly match where the first and second sentences are in the input.

> [!TIP]
> ✏️ **Your turn!** Check that everything seems correct with the second element of the training dataset.

We are only doing the check on the training set here, but you should of course double-check the validation and test sets the same way.

Now that we know our datasets look good, it's time to check the next step of the training pipeline.

### From datasets to dataloaders[[from-datasets-to-dataloaders]]

The next thing that can go wrong in the training pipeline is when the `Trainer` tries to form batches from the training or validation set. Once you are sure the `Trainer`'s datasets are correct, you can try to manually form a batch by executing the following (replace `train` with `eval` for the validation dataloader):

```py
for batch in trainer.get_train_dataloader():
    break
```

This code creates the training dataloader, then iterates through it, stopping at the first iteration. If the code executes without error, you have the first training batch that you can inspect, and if the code errors out, you know for sure the problem is in the dataloader, as is the case here:

```python out
~/git/transformers/src/transformers/data/data_collator.py in torch_default_data_collator(features)
    105                 batch[k] = torch.stack([f[k] for f in features])
    106             else:
--> 107                 batch[k] = torch.tensor([f[k] for f in features])
    108 
    109     return batch

ValueError: expected sequence of length 45 at dim 1 (got 76)
```

Inspecting the last frame of the traceback should be enough to give you a clue, but let's do a bit more digging. Most of the problems during batch creation arise because of the collation of examples into a single batch, so the first thing to check when in doubt is what `collate_fn` your `DataLoader` is using:

```py
data_collator = trainer.get_train_dataloader().collate_fn
data_collator
```

```python out
<function default_data_collator at 0x7fc0d2cb1e50>
```

So this is the `default_data_collator`, but that's not what we want in this case. We want to pad our examples to the longest sentence in the batch, which is done by the `DataCollatorWithPadding` collator. And this data collator is supposed to be used by default by the `Trainer`, so why is it not used here?

The answer is because we did not pass the `tokenizer` to the `Trainer`, so it couldn't create the `DataCollatorWithPadding` we want. In practice, you should never hesitate to explicitly pass along the data collator you want to use, to make sure you avoid these kinds of errors. Let's adapt our code to do exactly that:

```py
from datasets import load_dataset
import evaluate
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    DataCollatorWithPadding,
    TrainingArguments,
    Trainer,
)

raw_datasets = load_dataset("glue", "mnli")

model_checkpoint = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

def preprocess_function(examples):
    return tokenizer(examples["premise"], examples["hypothesis"], truncation=True)

tokenized_datasets = raw_datasets.map(preprocess_function, batched=True)
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)

args = TrainingArguments(
    f"distilbert-finetuned-mnli",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    num_train_epochs=3,
    weight_decay=0.01,
)

metric = evaluate.load("glue", "mnli")

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    return metric.compute(predictions=predictions, references=labels)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

trainer = Trainer(
    model,
    args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation_matched"],
    compute_metrics=compute_metrics,
    data_collator=data_collator,
    tokenizer=tokenizer,
)
trainer.train()
```

The good news? We don't get the same error as before, which is definitely progress. The bad news? We get an infamous CUDA error instead:

```python out
RuntimeError: CUDA error: CUBLAS_STATUS_ALLOC_FAILED when calling `cublasCreate(handle)`
```

This is bad because CUDA errors are extremely hard to debug in general. We will see in a minute how to solve this, but first let's finish our analysis of batch creation.

If you are sure your data collator is the right one, you should try to apply it on a couple of samples of your dataset:

```py
data_collator = trainer.get_train_dataloader().collate_fn
batch = data_collator([trainer.train_dataset[i] for i in range(4)])
```

This code will fail because the `train_dataset` contains string columns, which the `Trainer` usually removes. You can remove them manually, or if you want to replicate exactly what the `Trainer` is doing behind the scenes, you can call the private `Trainer._remove_unused_columns()` method that does that:

```py
data_collator = trainer.get_train_dataloader().collate_fn
actual_train_set = trainer._remove_unused_columns(trainer.train_dataset)
batch = data_collator([actual_train_set[i] for i in range(4)])
```

You should then be able to manually debug what happens inside the data collator if the error persists.

Now that we've debugged the batch creation process, it's time to pass one through the model!

### Going through the model[[going-through-the-model]]

You should be able to get a batch by executing the following command:

```py
for batch in trainer.get_train_dataloader():
    break
```

If you're running this code in a notebook, you may get a CUDA error that's similar to the one we saw earlier, in which case you need to restart your notebook and reexecute the last snippet without the `trainer.train()` line. That's the second most annoying thing about CUDA errors: they irremediably break your kernel. The most annoying thing about them is the fact that they are hard to debug.

Why is that? It has to do with the way GPUs work. They are extremely efficient at executing a lot of operations in parallel, but the drawback is that when one of those instructions results in an error, you don't know it instantly. It's only when the program calls a synchronization of the multiple processes on the GPU that it will realize something went wrong, so the error is actually raised at a place that has nothing to do with what created it. For instance, if we look at our previous traceback, the error was raised during the backward pass, but we will see in a minute that it actually stems from something in the forward pass.

So how do we debug those errors? The answer is easy: we don't. Unless your CUDA error is an out-of-memory error (which means there is not enough memory in your GPU), you should always go back to the CPU to debug it.

To do this in our case, we just have to put the model back on the CPU and call it on our batch -- the batch returned by the `DataLoader` has not been moved to the GPU yet:

```python
outputs = trainer.model.cpu()(**batch)
```

```python out
~/.pyenv/versions/3.7.9/envs/base/lib/python3.7/site-packages/torch/nn/functional.py in nll_loss(input, target, weight, size_average, ignore_index, reduce, reduction)
   2386         )
   2387     if dim == 2:
-> 2388         ret = torch._C._nn.nll_loss(input, target, weight, _Reduction.get_enum(reduction), ignore_index)
   2389     elif dim == 4:
   2390         ret = torch._C._nn.nll_loss2d(input, target, weight, _Reduction.get_enum(reduction), ignore_index)

IndexError: Target 2 is out of bounds.
```

So, the picture is getting clearer. Instead of having a CUDA error, we now have an `IndexError` in the loss computation (so nothing to do with the backward pass, as we said earlier). More precisely, we can see that it's target 2 that creates the error, so this is a very good moment to check the number of labels of our model:

```python
trainer.model.config.num_labels
```

```python out
2
```

With two labels, only 0s and 1s are allowed as targets, but according to the error message we got a 2. Getting a 2 is actually normal: if we remember the label names we extracted earlier, there were three, so we have indices 0, 1, and 2 in our dataset. The problem is that we didn't tell that to our model, which should have been created with three labels. So let's fix that!

```py
from datasets import load_dataset
import evaluate
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    DataCollatorWithPadding,
    TrainingArguments,
    Trainer,
)

raw_datasets = load_dataset("glue", "mnli")

model_checkpoint = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

def preprocess_function(examples):
    return tokenizer(examples["premise"], examples["hypothesis"], truncation=True)

tokenized_datasets = raw_datasets.map(preprocess_function, batched=True)
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint, num_labels=3)

args = TrainingArguments(
    f"distilbert-finetuned-mnli",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    num_train_epochs=3,
    weight_decay=0.01,
)

metric = evaluate.load("glue", "mnli")

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    return metric.compute(predictions=predictions, references=labels)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

trainer = Trainer(
    model,
    args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation_matched"],
    compute_metrics=compute_metrics,
    data_collator=data_collator,
    tokenizer=tokenizer,
)
```

We aren't including the `trainer.train()` line yet, to take the time to check that everything looks good. If we request a batch and pass it to our model, it now works without error!

```py
for batch in trainer.get_train_dataloader():
    break

outputs = trainer.model.cpu()(**batch)
```

The next step is then to move back to the GPU and check that everything still works:

```py
import torch

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
batch = {k: v.to(device) for k, v in batch.items()}

outputs = trainer.model.to(device)(**batch)
```

If you still get an error, make sure you restart your notebook and only execute the last version of the script.

### Performing one optimization step[[performing-one-optimization-step]]

Now that we know that we can build batches that actually go through the model, we are ready for the next step of the training pipeline: computing the gradients and performing an optimization step.

The first part is just a matter of calling the `backward()` method on the loss:

```py
loss = outputs.loss
loss.backward()
```

It's pretty rare to get an error at this stage, but if you do get one, make sure to go back to the CPU to get a helpful error message.

To perform the optimization step, we just need to create the `optimizer` and call its `step()` method:

```py
trainer.create_optimizer()
trainer.optimizer.step()
```

Again, if you're using the default optimizer in the `Trainer`, you shouldn't get an error at this stage, but if you have a custom optimizer, there might be some problems to debug here. Don't forget to go back to the CPU if you get a weird CUDA error at this stage. Speaking of CUDA errors, earlier we mentioned a special case. Let's have a look at that now.

### Dealing with CUDA out-of-memory errors[[dealing-with-cuda-out-of-memory-errors]]

Whenever you get an error message that starts with `RuntimeError: CUDA out of memory`, this indicates that you are out of GPU memory. This is not directly linked to your code, and it can happen with a script that runs perfectly fine. This error means that you tried to put too many things in the internal memory of your GPU, and that resulted in an error. Like with other CUDA errors, you will need to restart your kernel to be in a spot where you can run your training again.

To solve this issue, you just need to use less GPU space -- something that is often easier said than done. First, make sure you don't have two models on the GPU at the same time (unless that's required for your problem, of course). Then, you should probably reduce your batch size, as it directly affects the sizes of all the intermediate outputs of the model and their gradients. If the problem persists, consider using a smaller version of your model.

> [!TIP]
> In the next part of the course, we'll look at more advanced techniques that can help you reduce your memory footprint and let you fine-tune the biggest models.

### Evaluating the model[[evaluating-the-model]]

Now that we've solved all the issues with our code, everything is perfect and the training should run smoothly, right? Not so fast! If you run the `trainer.train()` command, everything will look good at first, but after a while you will get the following:

```py
# This will take a long time and error out, so you shouldn't run this cell
trainer.train()
```

```python out
TypeError: only size-1 arrays can be converted to Python scalars
```

You will realize this error appears during the evaluation phase, so this is the last thing we will need to debug.

You can run the evaluation loop of the `Trainer` independently form the training like this:

```py
trainer.evaluate()
```

```python out
TypeError: only size-1 arrays can be converted to Python scalars
```

> [!TIP]
> 💡 You should always make sure you can run `trainer.evaluate()` before launching `trainer.train()`, to avoid wasting lots of compute resources before hitting an error.

Before attempting to debug a problem in the evaluation loop, you should first make sure that you've had a look at the data, are able to form a batch properly, and can run your model on it. We've completed all of those steps, so the following code can be executed without error:

```py
for batch in trainer.get_eval_dataloader():
    break

batch = {k: v.to(device) for k, v in batch.items()}

with torch.no_grad():
    outputs = trainer.model(**batch)
```

The error comes later, at the end of the evaluation phase, and if we look at the traceback we see this:

```python trace
~/git/datasets/src/datasets/metric.py in add_batch(self, predictions, references)
    431         """
    432         batch = {"predictions": predictions, "references": references}
--> 433         batch = self.info.features.encode_batch(batch)
    434         if self.writer is None:
    435             self._init_writer()
```

This tells us that the error originates in the `datasets/metric.py` module -- so this is a problem with our `compute_metrics()` function. It takes a tuple with the logits and the labels as NumPy arrays, so let's try to feed it that:

```py
predictions = outputs.logits.cpu().numpy()
labels = batch["labels"].cpu().numpy()

compute_metrics((predictions, labels))
```

```python out
TypeError: only size-1 arrays can be converted to Python scalars
```

We get the same error, so the problem definitely lies with that function. If we look back at its code, we see it's just forwarding the `predictions` and the `labels` to `metric.compute()`. So is there a problem with that method? Not really. Let's have a quick look at the shapes:

```py
predictions.shape, labels.shape
```

```python out
((8, 3), (8,))
```

Our predictions are still logits, not the actual predictions, which is why the metric is returning this (somewhat obscure) error. The fix is pretty easy; we just have to add an argmax in the `compute_metrics()` function:

```py
import numpy as np

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return metric.compute(predictions=predictions, references=labels)

compute_metrics((predictions, labels))
```

```python out
{'accuracy': 0.625}
```

Now our error is fixed! This was the last one, so our script will now train a model properly.

For reference, here is the completely fixed script:

```py
import numpy as np
from datasets import load_dataset
import evaluate
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    DataCollatorWithPadding,
    TrainingArguments,
    Trainer,
)

raw_datasets = load_dataset("glue", "mnli")

model_checkpoint = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

def preprocess_function(examples):
    return tokenizer(examples["premise"], examples["hypothesis"], truncation=True)

tokenized_datasets = raw_datasets.map(preprocess_function, batched=True)
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint, num_labels=3)

args = TrainingArguments(
    f"distilbert-finetuned-mnli",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    num_train_epochs=3,
    weight_decay=0.01,
)

metric = evaluate.load("glue", "mnli")

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return metric.compute(predictions=predictions, references=labels)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

trainer = Trainer(
    model,
    args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation_matched"],
    compute_metrics=compute_metrics,
    data_collator=data_collator,
    tokenizer=tokenizer,
)
trainer.train()
```

In this instance, there are no more problems, and our script will fine-tune a model that should give reasonable results. But what can we do when the training proceeds without any error, and the model trained does not perform well at all? That's the hardest part of machine learning, and we'll show you a few techniques that can help.

> [!TIP]
> 💡 If you're using a manual training loop, the same steps apply to debug your training pipeline, but it's easier to separate them. Make sure you have not forgotten the `model.eval()` or `model.train()` at the right places, or the `zero_grad()` at each step, however!

## Debugging silent errors during training[[debugging-silent-errors-during-training]]

What can we do to debug a training that completes without error but doesn't get good results? We'll give you some pointers here, but be aware that this kind of debugging is the hardest part of machine learning, and there is no magical answer.

### Check your data (again!)[[check-your-data-again]]

Your model will only learn something if it's actually possible to learn anything from your data. If there is a bug that corrupts the data or the labels are attributed randomly, it's very likely you won't get any model training on your dataset. So always start by double-checking your decoded inputs and labels, and ask yourself the following questions:

- Is the decoded data understandable?
- Do you agree with the labels?
- Is there one label that's more common than the others?
- What should the loss/metric be if the model predicted a random answer/always the same answer?

> [!WARNING]
> ⚠️ If you are doing distributed training, print samples of your dataset in each process and triple-check that you get the same thing. One common bug is to have some source of randomness in the data creation that makes each process have a different version of the dataset.

After looking at your data, go through a few of the model's predictions and decode them too. If the model is always predicting the same thing, it might be because your dataset is biased toward one category (for classification problems); techniques like oversampling rare classes might help.

If the loss/metric you get on your initial model is very different from the loss/metric you would expect for random predictions, double-check the way your loss or metric is computed, as there is probably a bug there. If you are using several losses that you add at the end, make sure they are of the same scale.

When you are sure your data is perfect, you can see if the model is capable of training on it with one simple test.

### Overfit your model on one batch[[overfit-your-model-on-one-batch]]

Overfitting is usually something we try to avoid when training, as it means the model is not learning to recognize the general features we want it to but is instead just memorizing the training samples. However, trying to train your model on one batch over and over again is a good test to check if the problem as you framed it can be solved by the model you are attempting to train. It will also help you see if your initial learning rate is too high.

Doing this once you have defined your `Trainer` is really easy; just grab a batch of training data, then run a small manual training loop only using that batch for something like 20 steps:

```py
for batch in trainer.get_train_dataloader():
    break

batch = {k: v.to(device) for k, v in batch.items()}
trainer.create_optimizer()

for _ in range(20):
    outputs = trainer.model(**batch)
    loss = outputs.loss
    loss.backward()
    trainer.optimizer.step()
    trainer.optimizer.zero_grad()
```

> [!TIP]
> 💡 If your training data is unbalanced, make sure to build a batch of training data containing all the labels.

The resulting model should have close-to-perfect results on the same `batch`. Let's compute the metric on the resulting predictions:

```py
with torch.no_grad():
    outputs = trainer.model(**batch)
preds = outputs.logits
labels = batch["labels"]

compute_metrics((preds.cpu().numpy(), labels.cpu().numpy()))
```

```python out
{'accuracy': 1.0}
```

100% accuracy, now this is a nice example of overfitting (meaning that if you try your model on any other sentence, it will very likely give you a wrong answer)!

If you don't manage to have your model obtain perfect results like this, it means there is something wrong with the way you framed the problem or your data, so you should fix that. Only when you manage to pass the overfitting test can you be sure that your model can actually learn something.

> [!WARNING]
> ⚠️ You will have to recreate your model and your `Trainer` after this test, as the model obtained probably won't be able to recover and learn something useful on your full dataset.

### Don't tune anything until you have a first baseline[[dont-tune-anything-until-you-have-a-first-baseline]]

Hyperparameter tuning is always emphasized as being the hardest part of machine learning, but it's just the last step to help you gain a little bit on the metric. Most of the time, the default hyperparameters of the `Trainer` will work just fine to give you good results, so don't launch into a time-consuming and costly hyperparameter search until you have something that beats the baseline you have on your dataset.

Once you have a good enough model, you can start tweaking a bit. Don't try launching a thousand runs with different hyperparameters, but compare a couple of runs with different values for one hyperparameter to get an idea of which has the greatest impact.

If you are tweaking the model itself, keep it simple and don't try anything you can't reasonably justify. Always make sure you go back to the overfitting test to verify that your change hasn't had any unintended consequences.

### Ask for help[[ask-for-help]]

Hopefully you will have found some advice in this section that helped you solve your issue, but if that's not the case, remember you can always ask the community on the [forums](https://discuss.huggingface.co/). 

Here are some additional resources that may prove helpful:

- ["Reproducibility as a vehicle for engineering best practices"](https://docs.google.com/presentation/d/1yHLPvPhUs2KGI5ZWo0sU-PKU3GimAk3iTsI38Z-B5Gw/edit#slide=id.p) by Joel Grus
- ["Checklist for debugging neural networks"](https://towardsdatascience.com/checklist-for-debugging-neural-networks-d8b2a9434f21) by Cecelia Shao
- ["How to unit test machine learning code"](https://medium.com/@keeper6928/how-to-unit-test-machine-learning-code-57cf6fd81765) by Chase Roberts
- ["A Recipe for Training Neural Networks"](http://karpathy.github.io/2019/04/25/recipe/) by Andrej Karpathy

Of course, not every problem you encounter when training neural nets is your own fault! If you encounter something in the 🤗 Transformers or 🤗 Datasets library that does not seem right, you may have encountered a bug. You should definitely tell us all about it, and in the next section we'll explain exactly how to do that.

---

## Section 5: How to write a good issue

# How to write a good issue[[how-to-write-a-good-issue]]

When you encounter something that doesn't seem right with one of the Hugging Face libraries, you should definitely let us know so we can fix it (the same goes for any open source library, for that matter). If you are not completely certain whether the bug lies in your own code or one of our libraries, the first place to check is the [forums](https://discuss.huggingface.co/). The community will help you figure this out, and the Hugging Face team also closely watches the discussions there.

When you are sure you have a bug in your hand, the first step is to build a minimal reproducible example.

## Creating a minimal reproducible example[[creating-a-minimal-reproducible-example]]

It's very important to isolate the piece of code that produces the bug, as no one in the Hugging Face team is a magician (yet), and they can't fix what they can't see. A minimal reproducible example should, as the name indicates, be reproducible. This means that it should not rely on any external files or data you may have. Try to replace the data you are using with some dummy values that look like your real ones and still produce the same error.

> [!TIP]
> 🚨 Many issues in the 🤗 Transformers repository are unsolved because the data used to reproduce them is not accessible.

Once you have something that is self-contained, you can try to reduce it into even less lines of code, building what we call a _minimal reproducible example_. While this requires a bit more work on your side, you will almost be guaranteed to get help and a fix if you provide a nice, short bug reproducer.

If you feel comfortable enough, go inspect the source code where your bug happens. You might find a solution to your problem (in which case you can even suggest a pull request to fix it), but more generally, this can help the maintainers better understand the source when they read your report.

## Filling out the issue template[[filling-out-the-issue-template]]

When you file your issue, you will notice there is a template to fill out. We will follow the one for [🤗 Transformers issues](https://github.com/huggingface/transformers/issues/new/choose) here, but the same kind of information will be required if you report an issue in another repository. Don't leave the template blank: taking the time to fill it in will maximize your chances of getting an answer and solving your problem.

In general, when filing an issue, always stay courteous. This is an open source project, so you are using free software, and no one has any obligation to help you. You may include what you feel is justified criticism in your issue, but then the maintainers may very well take it badly and not be in a rush help you. Make sure you read the [code of conduct](https://github.com/huggingface/transformers/blob/master/CODE_OF_CONDUCT.md) of the project.

### Including your environment information[[including-your-environment-information]]

🤗 Transformers provides a utility to get all the information we need about your environment. Just type the following in your terminal:

```
transformers-cli env
```

and you should get something like this:

```out
Copy-and-paste the text below in your GitHub issue and FILL OUT the two last points.

- `transformers` version: 4.12.0.dev0
- Platform: Linux-5.10.61-1-MANJARO-x86_64-with-arch-Manjaro-Linux
- Python version: 3.7.9
- PyTorch version (GPU?): 1.8.1+cu111 (True)
- Tensorflow version (GPU?): 2.5.0 (True)
- Flax version (CPU?/GPU?/TPU?): 0.3.4 (cpu)
- Jax version: 0.2.13
- JaxLib version: 0.1.65
- Using GPU in script?: 
- Using distributed or parallel set-up in script?: 
```

You can also add a `!` at the beginning of the `transformers-cli env` command to execute it from a notebook cell, and then copy and paste the result at the beginning of your issue.

### Tagging people[[tagging-people]]

Tagging people by typing an `@` followed by their GitHub handle will send them a notification so they will see your issue and might reply quicker. Use this with moderation, because the people you tag might not appreciate being notified if it's something they have no direct link to. If you have looked at the source files related to your bug, you should tag the last person that made changes at the line you think is responsible for your problem (you can find this information by looking at said line on GitHub, selecting it, then clicking "View git blame").

Otherwise, the template offers suggestions of people to tag. In general, never tag more than three people!

### Including a reproducible example[[including-a-reproducible-example]]

If you have managed to create a self-contained example that produces the bug, now is the time to include it! Type a line with three backticks followed by `python`, like this:

````
```python
````

then paste in your minimal reproducible example and type a new line with three backticks. This will ensure your code is properly formatted.

If you didn't manage to create a reproducible example, explain in clear steps how you got to your issue. Include a link to a Google Colab notebook where you got the error if you can. The more information you share, the better able the maintainers will be to reply to you.

In all cases, you should copy and paste the whole error message you are getting. If you're working in Colab, remember that some of the frames may be automatically collapsed in the stack trace, so make sure you expand them before copying. Like with the code sample, put that error message between two lines with three backticks, so it's properly formatted.

### Describing the expected behavior[[describing-the-expected-behavior]]

Explain in a few lines what you expected to get, so that the maintainers get a full grasp of the problem. This part is generally pretty obvious, so it should fit in one sentence, but in some cases you may have a lot to say.

## And then what?[[and-then-what]]

Once your issue is filed, make sure to quickly check everything looks okay. You can edit the issue if you made a mistake, or even change its title if you realize the problem is different from what you initially thought.

There is no point pinging people if you don't get an answer. If no one helps you in a few days, it's likely that no one could make sense of your problem. Don't hesitate to go back to the reproducible example. Can you make it shorter and more to the point? If you don't get an answer in a week, you can leave a message gently asking for help, especially if you've edited your issue to include more information on the problem.

---

## Section 6: Part 2 completed!

# Part 2 completed![[part-2-completed]]

Congratulations, you've made it through the second part of the course! We're actively working on the third one, so subscribe to our [newsletter](https://huggingface.curated.co/) to make sure you don't miss its release.

You should now be able to tackle a range of NLP tasks, and fine-tune or pretrain a model on them. Don't forget to share your results with the community on the [Model Hub](https://huggingface.co/models).

We can't wait to see what you will build with the knowledge that you've gained!
