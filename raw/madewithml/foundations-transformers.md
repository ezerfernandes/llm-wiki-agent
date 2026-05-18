[ ]
[ ]

[Skip to content](#overview)

Try Ray with $100 credit — [Start Now](https://console.anyscale.com/register/ha?utm_source=made_with_ml&utm_medium=website&utm_campaign=banner)

[![logo](../../../static/images/logo.png)](../../.. "Made With ML by Anyscale")

Made With ML by Anyscale

Transformers

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
  + [ ]

    🛠   Toolkit

    🛠   Toolkit
    - [Notebooks](../notebooks/)
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
  + [x]

    🤖   Deep Learning

    🤖   Deep Learning
    - [CNNs](../convolutional-neural-networks/)
    - [Embeddings](../embeddings/)
    - [RNNs](../recurrent-neural-networks/)
    - [Attention](../attention/)
    - [ ]

      Transformers
      [Transformers](./)

      Table of contents
      * [Overview](#overview)
      * [Set up](#set-up)

        + [Load data](#load-data)
        + [Preprocessing](#preprocessing)
        + [Split data](#split-data)
        + [Label encoding](#label-encoding)
        + [Tokenizer](#tokenizer)
        + [Datasets](#datasets)
        + [Trainer](#trainer)
      * [Transformer](#transformer)

        + [Scaled dot-product attention](#scaled-dot-product-attention)
        + [Multi-head attention](#multi-head-attention)
        + [Positional encoding](#positional-encoding)
        + [Architecture](#architecture)
        + [Model](#model)
        + [Training](#training)
        + [Evaluation](#evaluation)
      * [Inference](#inference)
      * [Interpretability](#interpretability)
* [Subscribe](../../../misc/newsletter/)
* [Community](https://discord.com/channels/1078171187609337896/1078171189169635472)

Table of contents

* [Overview](#overview)
* [Set up](#set-up)

  + [Load data](#load-data)
  + [Preprocessing](#preprocessing)
  + [Split data](#split-data)
  + [Label encoding](#label-encoding)
  + [Tokenizer](#tokenizer)
  + [Datasets](#datasets)
  + [Trainer](#trainer)
* [Transformer](#transformer)

  + [Scaled dot-product attention](#scaled-dot-product-attention)
  + [Multi-head attention](#multi-head-attention)
  + [Positional encoding](#positional-encoding)
  + [Architecture](#architecture)
  + [Model](#model)
  + [Training](#training)
  + [Evaluation](#evaluation)
* [Inference](#inference)
* [Interpretability](#interpretability)

# Transformers

[View all lessons](/courses/foundations)

---

Implementing the Transformer architecture to extract contextual embeddings for our text classification task.

![Goku Mohandas](/static/images/goku_circle.png)

Goku Mohandas

·
 ·
 ·

[Repository](https://github.com/GokuMohandas/Made-With-ML)
 ·

[Notebook](https://github.com/GokuMohandas/Made-With-ML/blob/main/notebooks/15_Transformers.ipynb)

×

Subscribe to our newsletter

📬  Receive new lessons straight to your inbox (once a month) and join **40K+**
developers in learning how to responsibly deliver value with ML.

Subscribe

---

## Overview

Transformers are a very popular architecture that leverage and extend the concept of self-attention to create very useful representations of our input data for a downstream task.

* **advantages**:

  + better representation for our input tokens via contextual embeddings where the token representation is based on the specific neighboring tokens using self-attention.
  + sub-word tokens, as opposed to character tokens, since they can hold more meaningful representation for many of our keywords, prefixes, suffixes, etc.
  + attend (in parallel) to all the tokens in our input, as opposed to being limited by filter spans (CNNs) or memory issues from sequential processing (RNNs).
* **disadvantages**:

  + computationally intensive
  + required large amounts of data (mitigated using pretrained models)

![transformers](/static/images/foundations/transformers/architecture.png)

[Attention Is All You Need](https://arxiv.org/abs/1706.03762)

## Set up

Let's set our seed and device for our main task.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` import numpy as np import pandas as pd import random import torch import torch.nn as nn ``` |

|  |  |
| --- | --- |
| ``` 1 ``` | ``` SEED = 1234 ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` def set_seeds(seed=1234):     """Set seeds for reproducibility."""     np.random.seed(seed)     random.seed(seed)     torch.manual_seed(seed)     torch.cuda.manual_seed(seed)     torch.cuda.manual_seed_all(seed) # multi-GPU ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Set seeds for reproducibility set_seeds(seed=SEED) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` # Set device cuda = True device = torch.device("cuda" if (     torch.cuda.is_available() and cuda) else "cpu") torch.set_default_tensor_type("torch.FloatTensor") if device.type == "cuda":     torch.set_default_tensor_type("torch.cuda.FloatTensor") print (device) ``` |

```
cuda
```

### Load data

We will download the [AG News dataset](http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html), which consists of 120K text samples from 4 unique classes (`Business`, `Sci/Tech`, `Sports`, `World`)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Load data url = "https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/news.csv" df = pd.read_csv(url, header=0) # load df = df.sample(frac=1).reset_index(drop=True) # shuffle df.head() ``` |

|  | title | category |
| --- | --- | --- |
| 0 | Sharon Accepts Plan to Reduce Gaza Army Operation... | World |
| 1 | Internet Key Battleground in Wildlife Crime Fight | Sci/Tech |
| 2 | July Durable Good Orders Rise 1.7 Percent | Business |
| 3 | Growing Signs of a Slowing on Wall Street | Business |
| 4 | The New Faces of Reality TV | World |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Reduce data size (too large to fit in Colab's limited memory) df = df[:10000] print (len(df)) ``` |

```
10000
```

### Preprocessing

We're going to clean up our input data first by doing operations such as lower text, removing stop (filler) words, filters using regular expressions, etc.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` import nltk from nltk.corpus import stopwords from nltk.stem import PorterStemmer import re ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` nltk.download("stopwords") STOPWORDS = stopwords.words("english") print (STOPWORDS[:5]) porter = PorterStemmer() ``` |

```
[nltk_data] Downloading package stopwords to /root/nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
['i', 'me', 'my', 'myself', 'we']
```

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 ``` | ``` def preprocess(text, stopwords=STOPWORDS):     """Conditional preprocessing on our text unique to our task."""     # Lower     text = text.lower()      # Remove stopwords     pattern = re.compile(r"\b(" + r"|".join(stopwords) + r")\b\s*")     text = pattern.sub("", text)      # Remove words in parenthesis     text = re.sub(r"\([^)]*\)", "", text)      # Spacing and filters     text = re.sub(r"([-;;.,!?<=>])", r" \1 ", text)     text = re.sub("[^A-Za-z0-9]+", " ", text) # remove non alphanumeric chars     text = re.sub(" +", " ", text)  # remove multiple spaces     text = text.strip()      return text ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Sample text = "Great week for the NYSE!" preprocess(text=text) ``` |

```
great week nyse
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Apply to dataframe preprocessed_df = df.copy() preprocessed_df.title = preprocessed_df.title.apply(preprocess) print (f"{df.title.values[0]}\n\n{preprocessed_df.title.values[0]}") ``` |

```
Sharon Accepts Plan to Reduce Gaza Army Operation, Haaretz Says

sharon accepts plan reduce gaza army operation haaretz says
```

Warning

If you have preprocessing steps like standardization, etc. that are calculated, you need to separate the training and test set first before applying those operations. This is because we cannot apply any knowledge gained from the test set accidentally (data leak) during preprocessing/training. However for global preprocessing steps like the function above where we aren't learning anything from the data itself, we can perform before splitting the data.

### Split data

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` import collections from sklearn.model_selection import train_test_split ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` TRAIN_SIZE = 0.7 VAL_SIZE = 0.15 TEST_SIZE = 0.15 ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` def train_val_test_split(X, y, train_size):     """Split dataset into data splits."""     X_train, X_, y_train, y_ = train_test_split(X, y, train_size=TRAIN_SIZE, stratify=y)     X_val, X_test, y_val, y_test = train_test_split(X_, y_, train_size=0.5, stratify=y_)     return X_train, X_val, X_test, y_train, y_val, y_test ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Data X = preprocessed_df["title"].values y = preprocessed_df["category"].values ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` # Create data splits X_train, X_val, X_test, y_train, y_val, y_test = train_val_test_split(     X=X, y=y, train_size=TRAIN_SIZE) print (f"X_train: {X_train.shape}, y_train: {y_train.shape}") print (f"X_val: {X_val.shape}, y_val: {y_val.shape}") print (f"X_test: {X_test.shape}, y_test: {y_test.shape}") print (f"Sample point: {X_train[0]} → {y_train[0]}") ``` |

```
X_train: (7000,), y_train: (7000,)
X_val: (1500,), y_val: (1500,)
X_test: (1500,), y_test: (1500,)
Sample point: lost flu paydays → Business
```

### Label encoding

Next we'll define a `LabelEncoder` to encode our text labels into unique indices

|  |  |
| --- | --- |
| ``` 1 ``` | ``` import itertools ``` |

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 ``` | ``` class LabelEncoder(object):     """Label encoder for tag labels."""     def __init__(self, class_to_index={}):         self.class_to_index = class_to_index or {}  # mutable defaults ;)         self.index_to_class = {v: k for k, v in self.class_to_index.items()}         self.classes = list(self.class_to_index.keys())      def __len__(self):         return len(self.class_to_index)      def __str__(self):         return f"<LabelEncoder(num_classes={len(self)})>"      def fit(self, y):         classes = np.unique(y)         for i, class_ in enumerate(classes):             self.class_to_index[class_] = i         self.index_to_class = {v: k for k, v in self.class_to_index.items()}         self.classes = list(self.class_to_index.keys())         return self      def encode(self, y):         y_one_hot = np.zeros((len(y), len(self.class_to_index)), dtype=int)         for i, item in enumerate(y):             y_one_hot[i][self.class_to_index[item]] = 1         return y_one_hot      def decode(self, y):         classes = []         for i, item in enumerate(y):             index = np.where(item == 1)[0][0]             classes.append(self.index_to_class[index])         return classes      def save(self, fp):         with open(fp, "w") as fp:             contents = {'class_to_index': self.class_to_index}             json.dump(contents, fp, indent=4, sort_keys=False)      @classmethod     def load(cls, fp):         with open(fp, "r") as fp:             kwargs = json.load(fp=fp)         return cls(**kwargs) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Encode label_encoder = LabelEncoder() label_encoder.fit(y_train) NUM_CLASSES = len(label_encoder) label_encoder.class_to_index ``` |

```
{'Business': 0, 'Sci/Tech': 1, 'Sports': 2, 'World': 3}
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Class weights counts = np.bincount([label_encoder.class_to_index[class_] for class_ in y_train]) class_weights = {i: 1.0/count for i, count in enumerate(counts)} print (f"counts: {counts}\nweights: {class_weights}") ``` |

```
counts: [1746 1723 1725 1806]
weights: {0: 0.000572737686139748, 1: 0.0005803830528148578, 2: 0.0005797101449275362, 3: 0.0005537098560354374}
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` # Convert labels to tokens print (f"y_train[0]: {y_train[0]}") y_train = label_encoder.encode(y_train) y_val = label_encoder.encode(y_val) y_test = label_encoder.encode(y_test) print (f"y_train[0]: {y_train[0]}") print (f"decode([y_train[0]]): {label_encoder.decode([y_train[0]])}") ``` |

```
y_train[0]: Business
y_train[0]: [1 0 0 0]
decode([y_train[0]]): ['Business']
```

### Tokenizer

We'll be using the [BertTokenizer](https://huggingface.co/transformers/model_doc/bert.html#berttokenizer) to tokenize our input text in to sub-word tokens.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` from transformers import DistilBertTokenizer from transformers import BertTokenizer ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Load tokenizer and model # tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased") tokenizer = BertTokenizer.from_pretrained("allenai/scibert_scivocab_uncased") vocab_size = len(tokenizer) print (vocab_size) ``` |

```
31090
```

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 ``` | ``` # Tokenize inputs encoded_input = tokenizer(X_train.tolist(), return_tensors="pt", padding=True) X_train_ids = encoded_input["input_ids"] X_train_masks = encoded_input["attention_mask"] print (X_train_ids.shape, X_train_masks.shape) encoded_input = tokenizer(X_val.tolist(), return_tensors="pt", padding=True) X_val_ids = encoded_input["input_ids"] X_val_masks = encoded_input["attention_mask"] print (X_val_ids.shape, X_val_masks.shape) encoded_input = tokenizer(X_test.tolist(), return_tensors="pt", padding=True) X_test_ids = encoded_input["input_ids"] X_test_masks = encoded_input["attention_mask"] print (X_test_ids.shape, X_test_masks.shape) ``` |

```
torch.Size([7000, 27]) torch.Size([7000, 27])
torch.Size([1500, 21]) torch.Size([1500, 21])
torch.Size([1500, 26]) torch.Size([1500, 26])
```

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Decode print (f"{X_train_ids[0]}\n{tokenizer.decode(X_train_ids[0])}") ``` |

```
tensor([  102,  6677,  1441,  3982, 17973,   103,     0,     0,     0,     0,
            0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
            0,     0,     0,     0,     0,     0,     0])
[CLS] lost flu paydays [SEP] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD] [PAD]
```

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Sub-word tokens print (tokenizer.convert_ids_to_tokens(ids=X_train_ids[0])) ``` |

```
['[CLS]', 'lost', 'flu', 'pay', '##days', '[SEP]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]', '[PAD]']
```

### Datasets

We're going to create Datasets and DataLoaders to be able to efficiently create batches with our data splits.

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ``` class TransformerTextDataset(torch.utils.data.Dataset):     def __init__(self, ids, masks, targets):         self.ids = ids         self.masks = masks         self.targets = targets      def __len__(self):         return len(self.targets)      def __str__(self):         return f"<Dataset(N={len(self)})>"      def __getitem__(self, index):         ids = torch.tensor(self.ids[index], dtype=torch.long)         masks = torch.tensor(self.masks[index], dtype=torch.long)         targets = torch.FloatTensor(self.targets[index])         return ids, masks, targets      def create_dataloader(self, batch_size, shuffle=False, drop_last=False):         return torch.utils.data.DataLoader(             dataset=self,             batch_size=batch_size,             shuffle=shuffle,             drop_last=drop_last,             pin_memory=False) ``` |

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 ``` | ``` # Create datasets train_dataset = TransformerTextDataset(ids=X_train_ids, masks=X_train_masks, targets=y_train) val_dataset = TransformerTextDataset(ids=X_val_ids, masks=X_val_masks, targets=y_val) test_dataset = TransformerTextDataset(ids=X_test_ids, masks=X_test_masks, targets=y_test) print ("Data splits:\n"     f"  Train dataset:{train_dataset.__str__()}\n"     f"  Val dataset: {val_dataset.__str__()}\n"     f"  Test dataset: {test_dataset.__str__()}\n"     "Sample point:\n"     f"  ids: {train_dataset[0][0]}\n"     f"  masks: {train_dataset[0][1]}\n"     f"  targets: {train_dataset[0][2]}") ``` |

```
Data splits:
  Train dataset: <Dataset(N=7000)>
  Val dataset: <Dataset(N=1500)>
  Test dataset: <Dataset(N=1500)>
Sample point:
  ids: tensor([  102,  6677,  1441,  3982, 17973,   103,     0,     0,     0,     0,
            0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
            0,     0,     0,     0,     0,     0,     0])
  masks: tensor([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0])
  targets: tensor([1., 0., 0., 0.], device="cpu")
```

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 ``` | ``` # Create dataloaders batch_size = 128 train_dataloader = train_dataset.create_dataloader(     batch_size=batch_size) val_dataloader = val_dataset.create_dataloader(     batch_size=batch_size) test_dataloader = test_dataset.create_dataloader(     batch_size=batch_size) batch = next(iter(train_dataloader)) print ("Sample batch:\n"     f"  ids: {batch[0].size()}\n"     f"  masks: {batch[1].size()}\n"     f"  targets: {batch[2].size()}") ``` |

```
Sample batch:
  ids: torch.Size([128, 27])
  masks: torch.Size([128, 27])
  targets: torch.Size([128, 4])
```

### Trainer

Let's create the `Trainer` class that we'll use to facilitate training for our experiments.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` import torch.nn.functional as F ``` |

|  |  |
| --- | --- |
| ```   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 106 107 108 ``` | ``` class Trainer(object):     def __init__(self, model, device, loss_fn=None, optimizer=None, scheduler=None):          # Set params         self.model = model         self.device = device         self.loss_fn = loss_fn         self.optimizer = optimizer         self.scheduler = scheduler      def train_step(self, dataloader):         """Train step."""         # Set model to train mode         self.model.train()         loss = 0.0          # Iterate over train batches         for i, batch in enumerate(dataloader):              # Step             batch = [item.to(self.device) for item in batch]  # Set device             inputs, targets = batch[:-1], batch[-1]             self.optimizer.zero_grad()  # Reset gradients             z = self.model(inputs)  # Forward pass             J = self.loss_fn(z, targets)  # Define loss             J.backward()  # Backward pass             self.optimizer.step()  # Update weights              # Cumulative Metrics             loss += (J.detach().item() - loss) / (i + 1)          return loss      def eval_step(self, dataloader):         """Validation or test step."""         # Set model to eval mode         self.model.eval()         loss = 0.0         y_trues, y_probs = [], []          # Iterate over val batches         with torch.inference_mode():             for i, batch in enumerate(dataloader):                  # Step                 batch = [item.to(self.device) for item in batch]  # Set device                 inputs, y_true = batch[:-1], batch[-1]                 z = self.model(inputs)  # Forward pass                 J = self.loss_fn(z, y_true).item()                  # Cumulative Metrics                 loss += (J - loss) / (i + 1)                  # Store outputs                 y_prob = F.softmax(z).cpu().numpy()                 y_probs.extend(y_prob)                 y_trues.extend(y_true.cpu().numpy())          return loss, np.vstack(y_trues), np.vstack(y_probs)      def predict_step(self, dataloader):         """Prediction step."""         # Set model to eval mode         self.model.eval()         y_probs = []          # Iterate over val batches         with torch.inference_mode():             for i, batch in enumerate(dataloader):                  # Forward pass w/ inputs                 inputs, targets = batch[:-1], batch[-1]                 z = self.model(inputs)                  # Store outputs                 y_prob = F.softmax(z).cpu().numpy()                 y_probs.extend(y_prob)          return np.vstack(y_probs)      def train(self, num_epochs, patience, train_dataloader, val_dataloader):         best_val_loss = np.inf         for epoch in range(num_epochs):             # Steps             train_loss = self.train_step(dataloader=train_dataloader)             val_loss, _, _ = self.eval_step(dataloader=val_dataloader)             self.scheduler.step(val_loss)              # Early stopping             if val_loss < best_val_loss:                 best_val_loss = val_loss                 best_model = self.model                 _patience = patience  # reset _patience             else:                 _patience -= 1             if not _patience:  # 0                 print("Stopping early!")                 break              # Logging             print(                 f"Epoch: {epoch+1} | "                 f"train_loss: {train_loss:.5f}, "                 f"val_loss: {val_loss:.5f}, "                 f"lr: {self.optimizer.param_groups[0]['lr']:.2E}, "                 f"_patience: {_patience}"             )         return best_model ``` |

## Transformer

We'll first learn about the unique components within the Transformer architecture and then implement one for our text classification task.

### Scaled dot-product attention

The most popular type of self-attention is scaled dot-product attention from the widely-cited [Attention is all you need](https://arxiv.org/abs/1706.03762) paper. This type of attention involves projecting our encoded input sequences onto three matrices, queries (Q), keys (K) and values (V), whose weights we learn.

\[ Q = XW\_q \text{ where } W\_q \in \mathbb{R}^{HXd\_q} \]

\[ K = XW\_k \text{ where } W\_k \in \mathbb{R}^{HXd\_k} \]

\[ V = XW\_v \text{ where } W\_v \in \mathbb{R}^{HXd\_v} \]

\[ attention (Q, K, V) = softmax( \frac{Q K^{T}}{\sqrt{d\_k}} ) V \in \mathbb{R}^{MXd\_v} \]

| Variable | Description |
| --- | --- |
| \(X\) | encoded inputs \(\in \mathbb{R}^{NXMXH}\) |
| \(N\) | batch size |
| \(M\) | max sequence length in the batch |
| \(H\) | hidden dim, model dim, etc. |
| \(W\_q\) | query weights \(\in \mathbb{R}^{HXd\_q}\) |
| \(W\_k\) | key weights \(\in \mathbb{R}^{HXd\_k}\) |
| \(W\_v\) | value weights \(\in \mathbb{R}^{HXd\_v}\) |

### Multi-head attention

Instead of applying self-attention only once across the entire encoded input, we can also separate the input and apply self-attention in parallel (heads) to each input section and concatenate them. This allows the different head to learn unique representations while maintaining the complexity since we split the input into smaller subspaces.

\[ MultiHead(Q, K, V) = concat({head}\_1, ..., {head}\_{h})W\_O \]

\[ {head}\_i = attention(Q\_i, K\_i, V\_i) \]

| Variable | Description |
| --- | --- |
| \(h\) | number of attention heads |
| \(W\_O\) | multi-head attention weights \(\in \mathbb{R}^{hd\_vXH}\) |
| \(H\) | hidden dim (or dimension of the model \(d\_{model}\)) |

### Positional encoding

With self-attention, we aren't able to account for the sequential position of our input tokens. To address this, we can use positional encoding to create a representation of the location of each token with respect to the entire sequence. This can either be learned (with weights) or we can use a fixed function that can better extend to create positional encoding for lengths during inference that were not observed during training.

\[ PE\_{(pos,2i)} = sin({pos}/{10000^{2i/H}}) \]

\[ PE\_{(pos,2i+1)} = cos({pos}/{10000^{2i/H}}) \]

| Variable | Description |
| --- | --- |
| \(pos\) | position of the token \((1...M)\) |
| \(i\) | hidden dim \((1..H)\) |

This effectively allows us to represent each token's relative position using a fixed function for very large sequences. And because we've constrained the positional encodings to have the same dimensions as our encoded inputs, we can simply concatenate them before feeding them into the multi-head attention heads.

### Architecture

And here's how it all fits together! It's an end-to-end architecture that creates these contextual representations and uses an encoder-decoder architecture to predict the outcomes (one-to-one, many-to-one, many-to-many, etc.) Due to the complexity of the architecture, they require massive amounts of data for training without overfitting, however, they can be leveraged as pretrained models to finetune with smaller datasets that are similar to the larger set it was initially trained on.

![transformers architecture](/static/images/foundations/transformers/architecture.png)

[Attention Is All You Need](https://arxiv.org/abs/1706.03762)

> We're not going to the implement the Transformer [from scratch](https://nlp.seas.harvard.edu/2018/04/03/attention.html) but we will use the [Hugging Face library](https://github.com/huggingface/transformers) to do so in the [training](https://madewithml.com/courses/mlops/training/#transformers-w-contextual-embeddings) lesson!

### Model

We're going to use a pretrained [BertModel](https://huggingface.co/transformers/model_doc/bert.html#bertmodel) to act as a feature extractor. We'll only use the encoder to receive sequential and pooled outputs (`is_decoder=False` is default).

|  |  |
| --- | --- |
| ``` 1 ``` | ``` from transformers import BertModel ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # transformer = BertModel.from_pretrained("distilbert-base-uncased") # embedding_dim = transformer.config.dim transformer = BertModel.from_pretrained("allenai/scibert_scivocab_uncased") embedding_dim = transformer.config.hidden_size ``` |

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 ``` | ``` class Transformer(nn.Module):     def __init__(self, transformer, dropout_p, embedding_dim, num_classes):         super(Transformer, self).__init__()         self.transformer = transformer         self.dropout = torch.nn.Dropout(dropout_p)         self.fc1 = torch.nn.Linear(embedding_dim, num_classes)      def forward(self, inputs):         ids, masks = inputs         seq, pool = self.transformer(input_ids=ids, attention_mask=masks)         z = self.dropout(pool)         z = self.fc1(z)         return z ``` |

> We decided to work with the pooled output, but we could have just as easily worked with the sequential output (encoder representation for each sub-token) and applied a CNN (or other decoder options) on top of it.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` # Initialize model dropout_p = 0.5 model = Transformer(     transformer=transformer, dropout_p=dropout_p,     embedding_dim=embedding_dim, num_classes=num_classes) model = model.to(device) print (model.named_parameters) ``` |

```
<bound method Module.named_parameters of Transformer(
  (transformer): BertModel(
    (embeddings): BertEmbeddings(
      (word_embeddings): Embedding(31090, 768, padding_idx=0)
      (position_embeddings): Embedding(512, 768)
      (token_type_embeddings): Embedding(2, 768)
      (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
      (dropout): Dropout(p=0.1, inplace=False)
    )
    (encoder): BertEncoder(
      (layer): ModuleList(
        (0): BertLayer(
          (attention): BertAttention(
            (self): BertSelfAttention(
              (query): Linear(in_features=768, out_features=768, bias=True)
              (key): Linear(in_features=768, out_features=768, bias=True)
              (value): Linear(in_features=768, out_features=768, bias=True)
              (dropout): Dropout(p=0.1, inplace=False)
            )
            (output): BertSelfOutput(
              (dense): Linear(in_features=768, out_features=768, bias=True)
              (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (dropout): Dropout(p=0.1, inplace=False)
            )
          )
          (intermediate): BertIntermediate(
            (dense): Linear(in_features=768, out_features=3072, bias=True)
          )
          (output): BertOutput(
            (dense): Linear(in_features=3072, out_features=768, bias=True)
            (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            (dropout): Dropout(p=0.1, inplace=False)
          )
        )
        (1): BertLayer(
          (attention): BertAttention(
            (self): BertSelfAttention(
              (query): Linear(in_features=768, out_features=768, bias=True)
              (key): Linear(in_features=768, out_features=768, bias=True)
              (value): Linear(in_features=768, out_features=768, bias=True)
              (dropout): Dropout(p=0.1, inplace=False)
            )
            (output): BertSelfOutput(
              (dense): Linear(in_features=768, out_features=768, bias=True)
              (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (dropout): Dropout(p=0.1, inplace=False)
            )
          )
          (intermediate): BertIntermediate(
            (dense): Linear(in_features=768, out_features=3072, bias=True)
          )
          (output): BertOutput(
            (dense): Linear(in_features=3072, out_features=768, bias=True)
            (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            (dropout): Dropout(p=0.1, inplace=False)
          )
        )
        ...
        11 more BertLayers
        ...
      )
    )
    (pooler): BertPooler(
      (dense): Linear(in_features=768, out_features=768, bias=True)
      (activation): Tanh()
    )
  )
  (dropout): Dropout(p=0.5, inplace=False)
  (fc1): Linear(in_features=768, out_features=4, bias=True)
)>
```

### Training

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Arguments lr = 1e-4 num_epochs = 10 patience = 10 ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Define loss class_weights_tensor = torch.Tensor(np.array(list(class_weights.values()))) loss_fn = nn.BCEWithLogitsLoss(weight=class_weights_tensor) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Define optimizer & scheduler optimizer = torch.optim.Adam(model.parameters(), lr=lr) scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(     optimizer, mode="min", factor=0.1, patience=5) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Trainer module trainer = Trainer(     model=model, device=device, loss_fn=loss_fn,     optimizer=optimizer, scheduler=scheduler) ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Train best_model = trainer.train(num_epochs, patience, train_dataloader, val_dataloader) ``` |

```
Epoch: 1 | train_loss: 0.00022, val_loss: 0.00017, lr: 1.00E-04, _patience: 10
Epoch: 2 | train_loss: 0.00014, val_loss: 0.00016, lr: 1.00E-04, _patience: 10
Epoch: 3 | train_loss: 0.00010, val_loss: 0.00017, lr: 1.00E-04, _patience: 9
...
Epoch: 9 | train_loss: 0.00002, val_loss: 0.00022, lr: 1.00E-05, _patience: 3
Epoch: 10 | train_loss: 0.00002, val_loss: 0.00022, lr: 1.00E-05, _patience: 2
Epoch: 11 | train_loss: 0.00001, val_loss: 0.00022, lr: 1.00E-05, _patience: 1
Stopping early!
```

### Evaluation

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` import json from sklearn.metrics import precision_recall_fscore_support ``` |

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` | ``` def get_performance(y_true, y_pred, classes):     """Per-class performance metrics."""     # Performance     performance = {"overall": {}, "class": {}}      # Overall performance     metrics = precision_recall_fscore_support(y_true, y_pred, average="weighted")     performance["overall"]["precision"] = metrics[0]     performance["overall"]["recall"] = metrics[1]     performance["overall"]["f1"] = metrics[2]     performance["overall"]["num_samples"] = np.float64(len(y_true))      # Per-class performance     metrics = precision_recall_fscore_support(y_true, y_pred, average=None)     for i in range(len(classes)):         performance["class"][classes[i]] = {             "precision": metrics[0][i],             "recall": metrics[1][i],             "f1": metrics[2][i],             "num_samples": np.float64(metrics[3][i]),         }      return performance ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Get predictions test_loss, y_true, y_prob = trainer.eval_step(dataloader=test_dataloader) y_pred = np.argmax(y_prob, axis=1) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Determine performance performance = get_performance(     y_true=np.argmax(y_true, axis=1), y_pred=y_pred, classes=label_encoder.classes) print (json.dumps(performance["overall"], indent=2)) ``` |

```
{
  "precision": 0.8085194951783808,
  "recall": 0.8086666666666666,
  "f1": 0.8083051845125695,
  "num_samples": 1500.0
}
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` # Save artifacts from pathlib import Path dir = Path("transformers") dir.mkdir(parents=True, exist_ok=True) label_encoder.save(fp=Path(dir, "label_encoder.json")) torch.save(best_model.state_dict(), Path(dir, "model.pt")) with open(Path(dir, "performance.json"), "w") as fp:     json.dump(performance, indent=2, sort_keys=False, fp=fp) ``` |

## Inference

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` def get_probability_distribution(y_prob, classes):     """Create a dict of class probabilities from an array."""     results = {}     for i, class_ in enumerate(classes):         results[class_] = np.float64(y_prob[i])     sorted_results = {k: v for k, v in sorted(         results.items(), key=lambda item: item[1], reverse=True)}     return sorted_results ``` |

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 ``` | ``` # Load artifacts device = torch.device("cpu") tokenizer = BertTokenizer.from_pretrained("allenai/scibert_scivocab_uncased") label_encoder = LabelEncoder.load(fp=Path(dir, "label_encoder.json")) transformer = BertModel.from_pretrained("allenai/scibert_scivocab_uncased") embedding_dim = transformer.config.hidden_size model = Transformer(     transformer=transformer, dropout_p=dropout_p,     embedding_dim=embedding_dim, num_classes=num_classes) model.load_state_dict(torch.load(Path(dir, "model.pt"), map_location=device)) model.to(device); ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Initialize trainer trainer = Trainer(model=model, device=device) ``` |

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 ``` | ``` # Create datasets train_dataset = TransformerTextDataset(ids=X_train_ids, masks=X_train_masks, targets=y_train) val_dataset = TransformerTextDataset(ids=X_val_ids, masks=X_val_masks, targets=y_val) test_dataset = TransformerTextDataset(ids=X_test_ids, masks=X_test_masks, targets=y_test) print ("Data splits:\n"     f"  Train dataset:{train_dataset.__str__()}\n"     f"  Val dataset: {val_dataset.__str__()}\n"     f"  Test dataset: {test_dataset.__str__()}\n"     "Sample point:\n"     f"  ids: {train_dataset[0][0]}\n"     f"  masks: {train_dataset[0][1]}\n"     f"  targets: {train_dataset[0][2]}") ``` |

```
Data splits:
  Train dataset: <Dataset(N=7000)>
  Val dataset: <Dataset(N=1500)>
  Test dataset: <Dataset(N=1500)>
Sample point:
  ids: tensor([  102,  6677,  1441,  3982, 17973,   103,     0,     0,     0,     0,
            0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
            0,     0,     0,     0,     0,     0,     0])
  masks: tensor([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0])
  targets: tensor([1., 0., 0., 0.], device="cpu")
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` # Dataloader text = "The final tennis tournament starts next week." X = preprocess(text) encoded_input = tokenizer(X, return_tensors="pt", padding=True).to(torch.device("cpu")) ids = encoded_input["input_ids"] masks = encoded_input["attention_mask"] y_filler = label_encoder.encode([label_encoder.classes[0]]*len(ids)) dataset = TransformerTextDataset(ids=ids, masks=masks, targets=y_filler) dataloader = dataset.create_dataloader(batch_size=int(batch_size)) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Inference y_prob = trainer.predict_step(dataloader) y_pred = np.argmax(y_prob, axis=1) label_encoder.index_to_class[y_pred[0]] ``` |

```
Sports
```

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Class distributions prob_dist = get_probability_distribution(y_prob=y_prob[0], classes=label_encoder.classes) print (json.dumps(prob_dist, indent=2)) ``` |

```
{
  "Sports": 0.9999359846115112,
  "World": 4.0660612285137177e-05,
  "Sci/Tech": 1.1774928680097219e-05,
  "Business": 1.1545793313416652e-05
}
```

## Interpretability

Let's visualize the self-attention weights from each of the attention heads in the encoder.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` import sys !rm -r bertviz_repo !test -d bertviz_repo || git clone https://github.com/jessevig/bertviz bertviz_repo if not "bertviz_repo" in sys.path:   sys.path += ["bertviz_repo"] ``` |

|  |  |
| --- | --- |
| ``` 1 ``` | ``` from bertviz import head_view ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Print input ids print (ids) print (tokenizer.batch_decode(ids)) ``` |

```
tensor([[  102,  2531,  3617,  8869, 23589,  4972,  8553,  2205,  4082,   103]],
       device="cpu")
['[CLS] final tennis tournament starts next week [SEP]']
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Get encoder attentions seq, pool, attn = model.transformer(input_ids=ids, attention_mask=masks, output_attentions=True) print (len(attn)) # 12 attention layers (heads) print (attn[0].shape) ``` |

```
12
torch.Size([1, 12, 10, 10])
```

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 ``` | ``` # HTML set up def call_html():   import IPython   display(IPython.core.display.HTML('''         <script src="/static/components/requirejs/require.js"></script>         <script>           requirejs.config({             paths: {               base: '/static/base',               "d3": "https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.8/d3.min",               jquery: '//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min',             },           });         </script>         ''')) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Visualize self-attention weights call_html() tokens = tokenizer.convert_ids_to_tokens(ids[0]) head_view(attention=attn, tokens=tokens) ``` |

![interpretability with transformers](/static/images/foundations/transformers/interpretability.png)

Now we're ready to start the [MLOps course](https://madewithml.com/#course) to learn how to apply all this foundational modeling knowledge to responsibly develop, deploy and maintain production machine learning applications.

---

To cite this content, please use:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` @article{madewithml,     author       = {Goku Mohandas},     title        = { Transformers - Made With ML },     howpublished = {\url{https://madewithml.com/}},     year         = {2023} } ``` |

[![](/static/images/anyscale-white-text.svg)](https://www.anyscale.com?utm_source=madewithmml&utm_medium=website&utm_campaign=footer) © 2025 Anyscale, Inc.
 [Anyscale Privacy Policy](https://www.anyscale.com/privacy-policy)

Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
