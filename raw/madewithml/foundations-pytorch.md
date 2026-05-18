[ ]
[ ]

[Skip to content](#set-up)

Try Ray with $100 credit — [Start Now](https://console.anyscale.com/register/ha?utm_source=made_with_ml&utm_medium=website&utm_campaign=banner)

[![logo](../../../static/images/logo.png)](../../.. "Made With ML by Anyscale")

Made With ML by Anyscale

PyTorch Fundamentals

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
    - [Python](../python/)
    - [NumPy](../numpy/)
    - [Pandas](../pandas/)
    - [ ]

      PyTorch
      [PyTorch](./)

      Table of contents
      * [Set up](#set-up)
      * [Basics](#basics)
      * [Operations](#operations)
      * [Indexing](#indexing)
      * [Slicing](#slicing)
      * [Joining](#joining)
      * [Gradients](#gradients)
      * [CUDA](#cuda)
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
* [Basics](#basics)
* [Operations](#operations)
* [Indexing](#indexing)
* [Slicing](#slicing)
* [Joining](#joining)
* [Gradients](#gradients)
* [CUDA](#cuda)

# PyTorch Fundamentals

[View all lessons](/courses/foundations)

---

Learn how to use the PyTorch machine learning framework.

![Goku Mohandas](/static/images/goku_circle.png)

Goku Mohandas

·
 ·
 ·

[Repository](https://github.com/GokuMohandas/Made-With-ML)
 ·

[Notebook](https://github.com/GokuMohandas/Made-With-ML/blob/main/notebooks/05_PyTorch.ipynb)

×

Subscribe to our newsletter

📬  Receive new lessons straight to your inbox (once a month) and join **40K+**
developers in learning how to responsibly deliver value with ML.

Subscribe

---

## Set up

We'll import PyTorch and set seeds for reproducibility. Note that PyTorch also required a seed since we will be generating random tensors.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` import numpy as np import torch ``` |

|  |  |
| --- | --- |
| ``` 1 ``` | ``` SEED = 1234 ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Set seed for reproducibility np.random.seed(seed=SEED) torch.manual_seed(SEED) ``` |

```

```

## Basics

We'll first cover some basics with PyTorch such as creating tensors and converting from common data structures (lists, arrays, etc.) to tensors.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Creating a random tensor x = torch.randn(2, 3) # normal distribution (rand(2,3) -> uniform distribution) print(f"Type: {x.type()}") print(f"Size: {x.shape}") print(f"Values: \n{x}") ``` |

```
Type: torch.FloatTensor
Size: torch.Size([2, 3])
Values:
tensor([[ 0.0461,  0.4024, -1.0115],
        [ 0.2167, -0.6123,  0.5036]])
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Zero and Ones tensor x = torch.zeros(2, 3) print (x) x = torch.ones(2, 3) print (x) ``` |

```
tensor([[0., 0., 0.],
        [0., 0., 0.]])
tensor([[1., 1., 1.],
        [1., 1., 1.]])
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # List → Tensor x = torch.Tensor([[1, 2, 3],[4, 5, 6]]) print(f"Size: {x.shape}") print(f"Values: \n{x}") ``` |

```
Size: torch.Size([2, 3])
Values:
tensor([[1., 2., 3.],
        [4., 5., 6.]])
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # NumPy array → Tensor x = torch.Tensor(np.random.rand(2, 3)) print(f"Size: {x.shape}") print(f"Values: \n{x}") ``` |

```
Size: torch.Size([2, 3])
Values:
tensor([[0.1915, 0.6221, 0.4377],
        [0.7854, 0.7800, 0.2726]])
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Changing tensor type x = torch.Tensor(3, 4) print(f"Type: {x.type()}") x = x.long() print(f"Type: {x.type()}") ``` |

```
Type: torch.FloatTensor
Type: torch.LongTensor
```

## Operations

Now we'll explore some basic operations with tensors.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` # Addition x = torch.randn(2, 3) y = torch.randn(2, 3) z = x + y print(f"Size: {z.shape}") print(f"Values: \n{z}") ``` |

```
Size: torch.Size([2, 3])
Values:
tensor([[ 0.0761, -0.6775, -0.3988],
        [ 3.0633, -0.1589,  0.3514]])
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` # Dot product x = torch.randn(2, 3) y = torch.randn(3, 2) z = torch.mm(x, y) print(f"Size: {z.shape}") print(f"Values: \n{z}") ``` |

```
Size: torch.Size([2, 2])
Values:
tensor([[ 1.0796, -0.0759],
        [ 1.2746, -0.5134]])
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` # Transpose x = torch.randn(2, 3) print(f"Size: {x.shape}") print(f"Values: \n{x}") y = torch.t(x) print(f"Size: {y.shape}") print(f"Values: \n{y}") ``` |

```
Size: torch.Size([2, 3])
Values:
tensor([[ 0.8042, -0.1383,  0.3196],
        [-1.0187, -1.3147,  2.5228]])
Size: torch.Size([3, 2])
Values:
tensor([[ 0.8042, -1.0187],
        [-0.1383, -1.3147],
        [ 0.3196,  2.5228]])
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Reshape x = torch.randn(2, 3) z = x.view(3, 2) print(f"Size: {z.shape}") print(f"Values: \n{z}") ``` |

```
Size: torch.Size([3, 2])
Values:
tensor([[ 0.4501,  0.2709],
        [-0.8087, -0.0217],
        [-1.0413,  0.0702]])
```

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 ``` | ``` # Dangers of reshaping (unintended consequences) x = torch.tensor([     [[1,1,1,1], [2,2,2,2], [3,3,3,3]],     [[10,10,10,10], [20,20,20,20], [30,30,30,30]] ]) print(f"Size: {x.shape}") print(f"x: \n{x}\n")  a = x.view(x.size(1), -1) print(f"\nSize: {a.shape}") print(f"a: \n{a}\n")  b = x.transpose(0,1).contiguous() print(f"\nSize: {b.shape}") print(f"b: \n{b}\n")  c = b.view(b.size(0), -1) print(f"\nSize: {c.shape}") print(f"c: \n{c}") ``` |

```
Size: torch.Size([2, 3, 4])
x:
tensor([[[ 1,  1,  1,  1],
         [ 2,  2,  2,  2],
         [ 3,  3,  3,  3]],

        [[10, 10, 10, 10],
         [20, 20, 20, 20],
         [30, 30, 30, 30]]])

Size: torch.Size([3, 8])
a:
tensor([[ 1,  1,  1,  1,  2,  2,  2,  2],
        [ 3,  3,  3,  3, 10, 10, 10, 10],
        [20, 20, 20, 20, 30, 30, 30, 30]])

Size: torch.Size([3, 2, 4])
b:
tensor([[[ 1,  1,  1,  1],
         [10, 10, 10, 10]],

        [[ 2,  2,  2,  2],
         [20, 20, 20, 20]],

        [[ 3,  3,  3,  3],
         [30, 30, 30, 30]]])

Size: torch.Size([3, 8])
c:
tensor([[ 1,  1,  1,  1, 10, 10, 10, 10],
        [ 2,  2,  2,  2, 20, 20, 20, 20],
        [ 3,  3,  3,  3, 30, 30, 30, 30]])
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` # Dimensional operations x = torch.randn(2, 3) print(f"Values: \n{x}") y = torch.sum(x, dim=0) # add each row's value for every column print(f"Values: \n{y}") z = torch.sum(x, dim=1) # add each columns's value for every row print(f"Values: \n{z}") ``` |

```
Values:
tensor([[ 0.5797, -0.0599,  0.1816],
        [-0.6797, -0.2567, -1.8189]])
Values:
tensor([-0.1000, -0.3166, -1.6373])
Values:
tensor([ 0.7013, -2.7553])
```

## Indexing

Now we'll look at how to extract, separate and join values from our tensors.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` x = torch.randn(3, 4) print (f"x: \n{x}") print (f"x[:1]: \n{x[:1]}") print (f"x[:1, 1:3]: \n{x[:1, 1:3]}") ``` |

```
x:
tensor([[ 0.2111,  0.3372,  0.6638,  1.0397],
        [ 1.8434,  0.6588, -0.2349, -0.0306],
        [ 1.7462, -0.0722, -1.6794, -1.7010]])
x[:1]:
tensor([[0.2111, 0.3372, 0.6638, 1.0397]])
x[:1, 1:3]:
tensor([[0.3372, 0.6638]])
```

## Slicing

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 ``` | ``` # Select with dimensional indices x = torch.randn(2, 3) print(f"Values: \n{x}")  col_indices = torch.LongTensor([0, 2]) chosen = torch.index_select(x, dim=1, index=col_indices) # values from column 0 & 2 print(f"Values: \n{chosen}")  row_indices = torch.LongTensor([0, 1]) col_indices = torch.LongTensor([0, 2]) chosen = x[row_indices, col_indices] # values from (0, 0) & (1, 2) print(f"Values: \n{chosen}") ``` |

```
Values:
tensor([[ 0.6486,  1.7653,  1.0812],
        [ 1.2436,  0.8971, -0.0784]])
Values:
tensor([[ 0.6486,  1.0812],
        [ 1.2436, -0.0784]])
Values:
tensor([ 0.6486, -0.0784])
```

## Joining

We can also combine our tensors via concatenation or stacking operations, which are consistent with [NumPy's joining functions'](../numpy/#joining) behaviors as well.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` x = torch.randn(2, 3) print (x) print (x.shape) ``` |

```
tensor([[-1.5944, -0.4218, -1.8219],
        [ 1.7446,  1.2058, -0.7753]])
torch.Size([2, 3])
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Concatenation y = torch.cat([x, x], dim=0) # concat on a specified dimension print (y) print (y.shape) ``` |

```
tensor([[-1.5944, -0.4218, -1.8219],
        [ 1.7446,  1.2058, -0.7753],
        [-1.5944, -0.4218, -1.8219],
        [ 1.7446,  1.2058, -0.7753]])
torch.Size([4, 3])
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Stacking z = torch.stack([x, x], dim=0) # stack on new dimension print (z) print (z.shape) ``` |

```
tensor([[[-1.5944, -0.4218, -1.8219],
         [ 1.7446,  1.2058, -0.7753]],

        [[-1.5944, -0.4218, -1.8219],
         [ 1.7446,  1.2058, -0.7753]]])
torch.Size([2, 2, 3])
```

## Gradients

We can determine gradients (rate of change) of our tensors with respect to their constituents using gradient bookkeeping. The gradient is a vector that points in the direction of greatest increase of a function. We'll be using gradients in the [next lesson](../linear-regression/#gradients) to determine how to change our weights to affect a particular objective function (ex. loss).

\[ y = 3x + 2 \]

\[ z = \sum{y}/N \]

\[ \frac{\partial(z)}{\partial(x)} = \frac{\partial(z)}{\partial(y)} \frac{\partial(y)}{\partial(x)} = \frac{1}{N} \* 3 = \frac{1}{12} \* 3 = 0.25 \]

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` # Tensors with gradient bookkeeping x = torch.rand(3, 4, requires_grad=True) y = 3*x + 2 z = y.mean() z.backward() # z has to be scalar print(f"x: \n{x}") print(f"x.grad: \n{x.grad}") ``` |

```
x:
tensor([[0.7379, 0.0846, 0.4245, 0.9778],
        [0.6800, 0.3151, 0.3911, 0.8943],
        [0.6889, 0.8389, 0.1780, 0.6442]], requires_grad=True)
x.grad:
tensor([[0.2500, 0.2500, 0.2500, 0.2500],
        [0.2500, 0.2500, 0.2500, 0.2500],
        [0.2500, 0.2500, 0.2500, 0.2500]])
```

## CUDA

We also load our tensors onto the GPU for parallelized computation using CUDA (a parallel computing platform and API from Nvidia).

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Is CUDA available? print (torch.cuda.is_available()) ``` |

```
False
```

If False (CUDA is not available), let's change that by following these steps: Go to *Runtime* > *Change runtime type* > Change *Hardware accelerator* to *GPU* > Click *Save*

|  |  |
| --- | --- |
| ``` 1 ``` | ``` import torch ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Is CUDA available now? print (torch.cuda.is_available()) ``` |

```
True
```

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Set device device = torch.device("cuda" if torch.cuda.is_available() else "cpu") print (device) ``` |

```
cuda
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` x = torch.rand(2,3) print (x.is_cuda) x = torch.rand(2,3).to(device) # Tensor is stored on the GPU print (x.is_cuda) ``` |

```
False
True
```

---

To cite this content, please use:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` @article{madewithml,     author       = {Goku Mohandas},     title        = { PyTorch - Made With ML },     howpublished = {\url{https://madewithml.com/}},     year         = {2023} } ``` |

[![](/static/images/anyscale-white-text.svg)](https://www.anyscale.com?utm_source=madewithmml&utm_medium=website&utm_campaign=footer) © 2025 Anyscale, Inc.
 [Anyscale Privacy Policy](https://www.anyscale.com/privacy-policy)

Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
