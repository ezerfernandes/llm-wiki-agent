[ ]
[ ]

[Skip to content](#overview)

Try Ray with $100 credit — [Start Now](https://console.anyscale.com/register/ha?utm_source=made_with_ml&utm_medium=website&utm_campaign=banner)

[![logo](../../../static/images/logo.png)](../../.. "Made With ML by Anyscale")

Made With ML by Anyscale

Linear Regression

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
  + [x]

    🔥   Machine Learning

    🔥   Machine Learning
    - [ ]

      Linear regression
      [Linear regression](./)

      Table of contents
      * [Overview](#overview)
      * [Generate data](#generate-data)
      * [NumPy](#numpy)

        + [Split data](#split-data)
        + [Standardize data](#standardize-data)
        + [Weights](#weights)
        + [Model](#model)
        + [Loss](#loss)
        + [Gradients](#gradients)
        + [Update weights](#update-weights)
        + [Training](#training)
        + [Evaluation](#evaluation)
        + [Interpretability](#interpretability)
      * [PyTorch](#pytorch)

        + [Split data](#split-data_1)
        + [Standardize data](#standardize-data_1)
        + [Weights](#weights_1)
        + [Model](#model_1)
        + [Loss](#loss_1)
        + [Optimizer](#optimizer)
        + [Training](#training_1)
        + [Evaluation](#evaluation_1)
        + [Inference](#inference)
        + [Interpretability](#interpretability_1)
        + [Regularization](#regularization)
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

* [Overview](#overview)
* [Generate data](#generate-data)
* [NumPy](#numpy)

  + [Split data](#split-data)
  + [Standardize data](#standardize-data)
  + [Weights](#weights)
  + [Model](#model)
  + [Loss](#loss)
  + [Gradients](#gradients)
  + [Update weights](#update-weights)
  + [Training](#training)
  + [Evaluation](#evaluation)
  + [Interpretability](#interpretability)
* [PyTorch](#pytorch)

  + [Split data](#split-data_1)
  + [Standardize data](#standardize-data_1)
  + [Weights](#weights_1)
  + [Model](#model_1)
  + [Loss](#loss_1)
  + [Optimizer](#optimizer)
  + [Training](#training_1)
  + [Evaluation](#evaluation_1)
  + [Inference](#inference)
  + [Interpretability](#interpretability_1)
  + [Regularization](#regularization)

# Linear Regression

[View all lessons](/courses/foundations)

---

Implement linear regression from scratch using NumPy and then using PyTorch.

![Goku Mohandas](/static/images/goku_circle.png)

Goku Mohandas

·
 ·
 ·

[Repository](https://github.com/GokuMohandas/Made-With-ML)
 ·

[Notebook](https://github.com/GokuMohandas/Made-With-ML/blob/main/notebooks/06_Linear_Regression.ipynb)

×

Subscribe to our newsletter

📬  Receive new lessons straight to your inbox (once a month) and join **40K+**
developers in learning how to responsibly deliver value with ML.

Subscribe

---

## Overview

Our goal is to learn a linear model \(\hat{y}\) that models \(y\) given \(X\) using weights \(W\) and bias \(b\):

\[ \hat{y} = XW + b \]

| Variable | Description |
| --- | --- |
| \(N\) | total numbers of samples |
| \(\hat{y}\) | predictions \(\in \mathbb{R}^{NX1}\) |
| \(X\) | inputs \(\in \mathbb{R}^{NXD}\) |
| \(W\) | weights \(\in \mathbb{R}^{DX1}\) |
| \(b\) | bias \(\in \mathbb{R}^{1}\) |

* **Objective**:
  + Use inputs \(X\) to predict the output \(\hat{y}\) using a linear model. The model will be a line of best fit that minimizes the distance between the predicted (model's output) and target (ground truth) values. Training data \((X, y)\) is used to train the model and learn the weights \(W\) using gradient descent.
* **Advantages**:
  + Computationally simple.
  + Highly interpretable.
  + Can account for continuous and categorical features.
* **Disadvantages**:
  + The model will perform well only when the data is linearly separable (for classification).
* **Miscellaneous**:
  + You can also use linear regression for binary classification tasks where if the predicted continuous value is above a threshold, it belongs to a certain class. But we will cover better techniques for classification in future lessons and will focus on linear regression for continuous regression tasks only.

## Generate data

We're going to generate some simple dummy data to apply linear regression on. It's going to create roughly linear data (`y = 3.5X + noise`); the random noise is added to create realistic data that doesn't perfectly align in a line. Our goal is to have the model converge to a similar linear equation (there will be slight variance since we added some noise).

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` import numpy as np import pandas as pd import matplotlib.pyplot as plt ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` SEED = 1234 NUM_SAMPLES = 50 ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Set seed for reproducibility np.random.seed(SEED) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` # Generate synthetic data def generate_data(num_samples):     """Generate dummy data for linear regression."""     X = np.array(range(num_samples))     random_noise = np.random.uniform(-10, 20, size=num_samples)     y = 3.5*X + random_noise # add some noise     return X, y ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Generate random (linear) data X, y = generate_data(num_samples=NUM_SAMPLES) data = np.vstack([X, y]).T print (data[:5]) ``` |

```
[[ 0.         -4.25441649]
 [ 1.         12.16326313]
 [ 2.         10.13183217]
 [ 3.         24.06075751]
 [ 4.         27.39927424]]
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Load into a Pandas DataFrame df = pd.DataFrame(data, columns=["X", "y"]) X = df[["X"]].values y = df[["y"]].values df.head() ``` |

|  | X | y |
| --- | --- | --- |
| 0 | 0.0 | -4.254416 |
| 1 | 1.0 | 12.163263 |
| 2 | 2.0 | 10.131832 |
| 3 | 3.0 | 24.060758 |
| 4 | 4.0 | 27.399274 |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Scatter plot plt.title("Generated data") plt.scatter(x=df["X"], y=df["y"]) plt.show() ``` |

![dataset](/static/images/foundations/linear_regression/dataset.png)

## NumPy

Now that we have our data prepared, we'll first implement linear regression using just NumPy. This will let us really understand the underlying operations.

### Split data

Since our task is a regression task, we will randomly split our dataset into three sets: train, validation and test data splits.

* `train`: used to train our model.
* `val` : used to validate our model's performance during training.
* `test`: used to do an evaluation of our fully trained model.

> Be sure to check out our entire lesson focused on *properly* [splitting](https://madewithml.com/courses/mlops/splitting/) data in our [MLOps](https://madewithml.com/courses/mlops/) course.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` TRAIN_SIZE = 0.7 VAL_SIZE = 0.15 TEST_SIZE = 0.15 ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Shuffle data indices = list(range(NUM_SAMPLES)) np.random.shuffle(indices) X = X[indices] y = y[indices] ``` |

Warning

Be careful not to shuffle \(X\) and \(y\) separately because then the inputs won't correspond to the outputs!

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` # Split indices train_start = 0 train_end = int(0.7*NUM_SAMPLES) val_start = train_end val_end = int((TRAIN_SIZE+VAL_SIZE)*NUM_SAMPLES) test_start = val_end ``` |

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 ``` | ``` # Split data X_train = X[train_start:train_end] y_train = y[train_start:train_end] X_val = X[val_start:val_end] y_val = y[val_start:val_end] X_test = X[test_start:] y_test = y[test_start:] print (f"X_train: {X_train.shape}, y_train: {y_train.shape}") print (f"X_val: {X_val.shape}, y_test: {y_val.shape}") print (f"X_test: {X_test.shape}, y_test: {y_test.shape}") ``` |

```
X_train: (35, 1), y_train: (35, 1)
X_val: (7, 1), y_test: (7, 1)
X_test: (8, 1), y_test: (8, 1)
```

### Standardize data

We need to standardize our data (zero mean and unit variance) so a specific feature's magnitude doesn't affect how the model learns its weights.

\[ z = \frac{x\_i - \mu}{\sigma} \]

| Variable | Description |
| --- | --- |
| \(z\) | standardized value |
| \(x\_i\) | inputs |
| \(\mu\) | mean |
| \(\sigma\) | standard deviation |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` def standardize_data(data, mean, std):     return (data - mean)/std ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Determine means and stds X_mean = np.mean(X_train) X_std = np.std(X_train) y_mean = np.mean(y_train) y_std = np.std(y_train) ``` |

We need to treat the validation and test sets as if they were hidden datasets. So we only use the train set to determine the mean and std to avoid biasing our training process.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` # Standardize X_train = standardize_data(X_train, X_mean, X_std) y_train = standardize_data(y_train, y_mean, y_std) X_val = standardize_data(X_val, X_mean, X_std) y_val = standardize_data(y_val, y_mean, y_std) X_test = standardize_data(X_test, X_mean, X_std) y_test = standardize_data(y_test, y_mean, y_std) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Check (means should be ~0 and std should be ~1) # Check (means should be ~0 and std should be ~1) print (f"mean: {np.mean(X_test, axis=0)[0]:.1f}, std: {np.std(X_test, axis=0)[0]:.1f}") print (f"mean: {np.mean(y_test, axis=0)[0]:.1f}, std: {np.std(y_test, axis=0)[0]:.1f}") ``` |

```
mean: -0.4, std: 0.9
mean: -0.3, std: 1.0
```

### Weights

Our goal is to learn a linear model \(\hat{y}\) that models \(y\) given \(X\) using weights \(W\) and bias \(b\) → \(\hat{y} = XW + b\)

`Step 1`: Randomly initialize the model's weights \(W\).

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` INPUT_DIM = X_train.shape[1] # X is 1-dimensional OUTPUT_DIM = y_train.shape[1] # y is 1-dimensional ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Initialize random weights W = 0.01 * np.random.randn(INPUT_DIM, OUTPUT_DIM) b = np.zeros((1, 1)) print (f"W: {W.shape}") print (f"b: {b.shape}") ``` |

```
W: (1, 1)
b: (1, 1)
```

### Model

`Step 2`: Feed inputs \(X\) into the model to receive the predictions \(\hat{y}\)

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Forward pass [NX1] · [1X1] = [NX1] y_pred = np.dot(X_train, W) + b print (f"y_pred: {y_pred.shape}") ``` |

```
y_pred: (35, 1)
```

### Loss

`Step 3`: Compare the predictions \(\hat{y}\) with the actual target values \(y\) using the objective (cost) function to determine the loss \(J\). A common objective function for linear regression is mean squared error (MSE). This function calculates the difference between the predicted and target values and squares it.

\[ J(\theta) = \frac{1}{N} \sum\_i (y\_i - \hat{y}\_i)^2 = \frac{1}{N}\sum\_i (y\_i - X\_iW)^2 \]

bias term (\(b\)) excluded to avoid crowding the notations

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Loss N = len(y_train) loss = (1/N) * np.sum((y_train - y_pred)**2) print (f"loss: {loss:.2f}") ``` |

```
loss: 0.99
```

### Gradients

`Step 4`: Calculate the gradient of loss \(J(\theta)\) w.r.t to the model weights.

\[ → \frac{\partial{J}}{\partial{W}} = -\frac{2}{N} \sum\_i (y\_i - X\_iW) X\_i = -\frac{2}{N} \sum\_i (y\_i - \hat{y}\_i) X\_i \]

\[ → \frac{\partial{J}}{\partial{b}} = -\frac{2}{N} \sum\_i (y\_i - X\_iW)1 = -\frac{2}{N} \sum\_i (y\_i - \hat{y}\_i)1 \]

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Backpropagation dW = -(2/N) * np.sum((y_train - y_pred) * X_train) db = -(2/N) * np.sum((y_train - y_pred) * 1) ``` |

The gradient is the derivative, or the rate of change of a function. It's a vector that points in the direction of greatest increase of a function. For example the gradient of our loss function (\(J\)) with respect to our weights (\(W\)) will tell us how to change \(W\) so we can maximize \(J\). However, we want to minimize our loss so we subtract the gradient from \(W\).

### Update weights

`Step 5`: Update the weights \(W\) using a small learning rate \(\alpha\).

\[ W = W - \alpha\frac{\partial{J}}{\partial{W}} \]

\[ b = b - \alpha\frac{\partial{J}}{\partial{b}} \]

|  |  |
| --- | --- |
| ``` 1 ``` | ``` LEARNING_RATE = 1e-1 ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Update weights W += -LEARNING_RATE * dW b += -LEARNING_RATE * db ``` |

> The learning rate \(\alpha\) is a way to control how much we update the weights by. If we choose a small learning rate, it may take a long time for our model to train. However, if we choose a large learning rate, we may overshoot and our training will never converge. The specific learning rate depends on our data and the type of models we use but it's typically good to explore in the range of \([1e^{-8}, 1e^{-1}]\). We'll explore learning rate update strategies in later lessons.

### Training

`Step 6`: Repeat steps 2 - 5 to minimize the loss and train the model.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` NUM_EPOCHS = 100 ``` |

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` | ``` # Initialize random weights W = 0.01 * np.random.randn(INPUT_DIM, OUTPUT_DIM) b = np.zeros((1, ))  # Training loop for epoch_num in range(NUM_EPOCHS):      # Forward pass [NX1] · [1X1] = [NX1]     y_pred = np.dot(X_train, W) + b      # Loss     loss = (1/len(y_train)) * np.sum((y_train - y_pred)**2)      # Show progress     if epoch_num%10 == 0:         print (f"Epoch: {epoch_num}, loss: {loss:.3f}")      # Backpropagation     dW = -(2/N) * np.sum((y_train - y_pred) * X_train)     db = -(2/N) * np.sum((y_train - y_pred) * 1)      # Update weights     W += -LEARNING_RATE * dW     b += -LEARNING_RATE * db ``` |

```
Epoch: 0, loss: 0.990
Epoch: 10, loss: 0.039
Epoch: 20, loss: 0.028
Epoch: 30, loss: 0.028
Epoch: 40, loss: 0.028
Epoch: 50, loss: 0.028
Epoch: 60, loss: 0.028
Epoch: 70, loss: 0.028
Epoch: 80, loss: 0.028
Epoch: 90, loss: 0.028
```

> To keep the code simple, we're not calculating and displaying the validation loss after each epoch here. But in [later lessons](../convolutional-neural-networks/#training), the performance on the validation set will be crucial in influencing the learning process (learning rate, when to stop training, etc.).

### Evaluation

Now we're ready to see how well our trained model will perform on our test (hold-out) data split. This will be our best measure on how well the model would perform on the real world, given that our dataset's distribution is close to unseen data.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Predictions pred_train = W*X_train + b pred_test = W*X_test + b ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Train and test MSE train_mse = np.mean((y_train - pred_train) ** 2) test_mse = np.mean((y_test - pred_test) ** 2) print (f"train_MSE: {train_mse:.2f}, test_MSE: {test_mse:.2f}") ``` |

```
train_MSE: 0.03, test_MSE: 0.01
```

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 ``` | ``` # Figure size plt.figure(figsize=(15,5))  # Plot train data plt.subplot(1, 2, 1) plt.title("Train") plt.scatter(X_train, y_train, label="y_train") plt.plot(X_train, pred_train, color="red", linewidth=1, linestyle="-", label="model") plt.legend(loc="lower right")  # Plot test data plt.subplot(1, 2, 2) plt.title("Test") plt.scatter(X_test, y_test, label='y_test') plt.plot(X_test, pred_test, color="red", linewidth=1, linestyle="-", label="model") plt.legend(loc="lower right")  # Show plots plt.show() ``` |

![evaluation for numpy implementation](/static/images/foundations/linear_regression/evaluation_np.png)

### Interpretability

Since we standardized our inputs and outputs, our weights were fit to those standardized values. So we need to unstandardize our weights so we can compare it to our true weight (3.5).

> Note that both \(X\) and \(y\) were standardized.

\[ \hat{y}\_{scaled} = b\_{scaled} + \sum\_{j=1}^{k}{W\_{scaled}}\_j{x\_{scaled}}\_j \]

| Variable | Description |
| --- | --- |
| \(y\_{scaled}\) | \(\frac{\hat{y} - \bar{y}}{\sigma\_y}\) |
| \(x\_{scaled}\) | \(\frac{x\_j - \bar{x}\_j}{\sigma\_j}\) |

\[ \frac{\hat{y} - \bar{y}}{\sigma\_y} = b\_{scaled} + \sum\_{j=1}^{k}{W\_{scaled}}\_j\frac{x\_j - \bar{x}\_j}{\sigma\_j} \]

\[ \hat{y}\_{scaled} = \frac{\hat{y}\_{unscaled} - \bar{y}}{\sigma\_y} = {b\_{scaled}} + \sum\_{j=1}^{k} {W\_{scaled}}\_j (\frac{x\_j - \bar{x}\_j}{\sigma\_j}) \]

\[ \hat{y}\_{unscaled} = b\_{scaled}\sigma\_y + \bar{y} - \sum\_{j=1}^{k} {W\_{scaled}}\_j(\frac{\sigma\_y}{\sigma\_j})\bar{x}\_j + \sum\_{j=1}^{k}{W\_{scaled}}\_j(\frac{\sigma\_y}{\sigma\_j})x\_j \]

In the expression above, we can see the expression:

\[ \hat{y}\_{unscaled} = b\_{unscaled} + W\_{unscaled}x \]

| Variable | Description |
| --- | --- |
| \(W\_{unscaled}\) | \({W}\_j(\frac{\sigma\_y}{\sigma\_j})\) |
| \(b\_{unscaled}\) | \(b\_{scaled}\sigma\_y + \bar{y} - \sum\_{j=1}^{k} {W}\_j(\frac{\sigma\_y}{\sigma\_j})\bar{x}\_j\) |

By substituting \(W\_{unscaled}\) in \(b\_{unscaled}\), it now becomes:

\[ b\_{unscaled} = b\_{scaled}\sigma\_y + \bar{y} - \sum\_{j=1}^{k} W\_{unscaled}\bar{x}\_j \]

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Unscaled weights W_unscaled = W * (y_std/X_std) b_unscaled = b * y_std + y_mean - np.sum(W_unscaled*X_mean) print ("[actual] y = 3.5X + noise") print (f"[model] y_hat = {W_unscaled[0][0]:.1f}X + {b_unscaled[0]:.1f}") ``` |

```
[actual] y = 3.5X + noise
[model] y_hat = 3.4X + 7.8
```

## PyTorch

Now that we've implemented linear regression with Numpy, let's do the same with PyTorch.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` import torch ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Set seed for reproducibility torch.manual_seed(SEED) ``` |

```

```

### Split data

This time, instead of splitting data using indices, let's use scikit-learn's built in [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split) function.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` from sklearn.model_selection import train_test_split ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` TRAIN_SIZE = 0.7 VAL_SIZE = 0.15 TEST_SIZE = 0.15 ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Split (train) X_train, X_, y_train, y_ = train_test_split(X, y, train_size=TRAIN_SIZE) ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` print (f"train: {len(X_train)} ({(len(X_train) / len(X)):.2f})\n"        f"remaining: {len(X_)} ({(len(X_) / len(X)):.2f})") ``` |

```
train: 35 (0.70)
remaining: 15 (0.30)
```

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Split (test) X_val, X_test, y_val, y_test = train_test_split(     X_, y_, train_size=0.5) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` print(f"train: {len(X_train)} ({len(X_train)/len(X):.2f})\n"       f"val: {len(X_val)} ({len(X_val)/len(X):.2f})\n"       f"test: {len(X_test)} ({len(X_test)/len(X):.2f})") ``` |

```
train: 35 (0.70)
val: 7 (0.14)
test: 8 (0.16)
```

### Standardize data

This time we'll use scikit-learn's [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler) to standardize our data.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` from sklearn.preprocessing import StandardScaler ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Standardize the data (mean=0, std=1) using training data X_scaler = StandardScaler().fit(X_train) y_scaler = StandardScaler().fit(y_train) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` # Apply scaler on training and test data X_train = X_scaler.transform(X_train) y_train = y_scaler.transform(y_train).ravel().reshape(-1, 1) X_val = X_scaler.transform(X_val) y_val = y_scaler.transform(y_val).ravel().reshape(-1, 1) X_test = X_scaler.transform(X_test) y_test = y_scaler.transform(y_test).ravel().reshape(-1, 1) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Check (means should be ~0 and std should be ~1) print (f"mean: {np.mean(X_test, axis=0)[0]:.1f}, std: {np.std(X_test, axis=0)[0]:.1f}") print (f"mean: {np.mean(y_test, axis=0)[0]:.1f}, std: {np.std(y_test, axis=0)[0]:.1f}") ``` |

```
mean: -0.3, std: 0.7
mean: -0.3, std: 0.6
```

### Weights

We will be using PyTorch's [Linear layers](https://pytorch.org/docs/stable/nn.html#linear-layers) in our MLP implementation. These layers will act as out weights (and biases).

\[ z = XW \]

|  |  |
| --- | --- |
| ``` 1 ``` | ``` from torch import nn ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Inputs N = 3 # num samples x = torch.randn(N, INPUT_DIM) print (x.shape) print (x.numpy()) ``` |

```
torch.Size([3, 1])
[[ 0.04613046]
 [ 0.40240282]
 [-1.0115291 ]]
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Weights m = nn.Linear(INPUT_DIM, OUTPUT_DIM) print (m) print (f"weights ({m.weight.shape}): {m.weight[0][0]}") print (f"bias ({m.bias.shape}): {m.bias[0]}") ``` |

```
Linear(in_features=1, out_features=1, bias=True)
weights (torch.Size([1, 1])): 0.35
bias (torch.Size([1])): -0.34
```

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Forward pass z = m(x) print (z.shape) print (z.detach().numpy()) ``` |

```
torch.Size([3, 1])
[[-0.32104054]
 [-0.19719592]
 [-0.68869597]]
```

### Model

\[ \hat{y} = XW + b \]

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` class LinearRegression(nn.Module):     def __init__(self, input_dim, output_dim):         super(LinearRegression, self).__init__()         self.fc1 = nn.Linear(input_dim, output_dim)      def forward(self, x_in):         y_pred = self.fc1(x_in)         return y_pred ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Initialize model model = LinearRegression(input_dim=INPUT_DIM, output_dim=OUTPUT_DIM) print (model.named_parameters) ``` |

```
Model:
<bound method Module.named_parameters of LinearRegression(
  (fc1): Linear(in_features=1, out_features=1, bias=True)
)>
```

### Loss

This time we're using PyTorch's [loss functions](https://pytorch.org/docs/stable/nn.html#loss-functions), specifically [`MSELoss`](https://pytorch.org/docs/stable/generated/torch.nn.MSELoss.html#torch.nn.MSELoss).

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` loss_fn = nn.MSELoss() y_pred = torch.Tensor([0., 0., 1., 1.]) y_true =  torch.Tensor([1., 1., 1., 0.]) loss = loss_fn(y_pred, y_true) print("Loss: ", loss.numpy()) ``` |

```
Loss:  0.75
```

### Optimizer

When we implemented linear regression with just NumPy, we used batch gradient descent to update our weights (used entire training set). But there are actually many different gradient descent [optimization algorithms](https://pytorch.org/docs/stable/optim.html) to choose from and it depends on the situation. However, the [ADAM optimizer](https://pytorch.org/docs/stable/optim.html#torch.optim.Adam) has become a standard algorithm for most cases.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` from torch.optim import Adam ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Optimizer optimizer = Adam(model.parameters(), lr=LEARNING_RATE) ``` |

### Training

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` # Convert data to tensors X_train = torch.Tensor(X_train) y_train = torch.Tensor(y_train) X_val = torch.Tensor(X_val) y_val = torch.Tensor(y_val) X_test = torch.Tensor(X_test) y_test = torch.Tensor(y_test) ``` |

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 ``` | ``` # Training for epoch in range(NUM_EPOCHS):     # Forward pass     y_pred = model(X_train)      # Loss     loss = loss_fn(y_pred, y_train)      # Zero all gradients     optimizer.zero_grad()      # Backward pass     loss.backward()      # Update weights     optimizer.step()      if epoch%20==0:         print (f"Epoch: {epoch} | loss: {loss:.2f}") ``` |

```
Epoch: 0 | loss: 0.22
Epoch: 20 | loss: 0.03
Epoch: 40 | loss: 0.02
Epoch: 60 | loss: 0.02
Epoch: 80 | loss: 0.02
```

### Evaluation

Now we're ready to evaluate our trained model.

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Predictions pred_train = model(X_train) pred_test = model(X_test) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Performance train_error = loss_fn(pred_train, y_train) test_error = loss_fn(pred_test, y_test) print(f"train_error: {train_error:.2f}") print(f"test_error: {test_error:.2f}") ``` |

```
train_error: 0.02
test_error: 0.01
```

Since we only have one feature, it's easy to visually inspect the model.

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 ``` | ``` # Figure size plt.figure(figsize=(15,5))  # Plot train data plt.subplot(1, 2, 1) plt.title("Train") plt.scatter(X_train, y_train, label="y_train") plt.plot(X_train, pred_train.detach().numpy(), color="red", linewidth=1, linestyle="-", label="model") plt.legend(loc="lower right")  # Plot test data plt.subplot(1, 2, 2) plt.title("Test") plt.scatter(X_test, y_test, label='y_test') plt.plot(X_test, pred_test.detach().numpy(), color="red", linewidth=1, linestyle="-", label="model") plt.legend(loc="lower right")  # Show plots plt.show() ``` |

![evaluation for pytorch implementation](/static/images/foundations/linear_regression/evaluation_pt.png)

### Inference

After training a model, we can use it to predict on new data.

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Feed in your own inputs sample_indices = [10, 15, 25] X_infer = np.array(sample_indices, dtype=np.float32) X_infer = torch.Tensor(X_scaler.transform(X_infer.reshape(-1, 1))) ``` |

Recall that we need to unstandardize our predictions.

\[ \hat{y}\_{scaled} = \frac{\hat{y} - \mu\_{\hat{y}}}{\sigma\_{\hat{y}}} \]

\[ \hat{y} = \hat{y}\_{scaled} \* \sigma\_{\hat{y}} + \mu\_{\hat{y}} \]

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # Unstandardize predictions pred_infer = model(X_infer).detach().numpy() * np.sqrt(y_scaler.var_) + y_scaler.mean_ for i, index in enumerate(sample_indices):     print (f"{df.iloc[index]["y"]:.2f} (actual) → {pred_infer[i][0]:.2f} (predicted)") ``` |

```
35.73 (actual) → 42.11 (predicted)
59.34 (actual) → 59.17 (predicted)
97.04 (actual) → 93.30 (predicted)
```

### Interpretability

Linear regression offers the great advantage of being highly interpretable. Each feature has a coefficient which signifies its importance/impact on the output variable y. We can interpret our coefficient as follows: by increasing X by 1 unit, we increase y by \(W\) (~3.65) units.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` # Unstandardize coefficients W = model.fc1.weight.data.numpy()[0][0] b = model.fc1.bias.data.numpy()[0] W_unscaled = W * (y_scaler.scale_/X_scaler.scale_) b_unscaled = b * y_scaler.scale_ + y_scaler.mean_ - np.sum(W_unscaled*X_scaler.mean_) print ("[actual] y = 3.5X + noise") print (f"[model] y_hat = {W_unscaled[0]:.1f}X + {b_unscaled[0]:.1f}") ``` |

```
[actual] y = 3.5X + noise
[model] y_hat = 3.4X + 8.0
```

### Regularization

Regularization helps decrease overfitting. Below is `L2` regularization (ridge regression). There are many forms of regularization but they all work to reduce overfitting in our models. With `L2` regularization, we are penalizing large weight values by decaying them because having large weights will lead to preferential bias with the respective inputs and we want the model to work with all the inputs and not just a select few. There are also other types of regularization like `L1` (lasso regression) which is useful for creating sparse models where some feature coefficients are zeroed out, or elastic which combines `L1` and `L2` penalties.

> Regularization is not just for linear regression. You can use it to regularize any model's weights including the ones we will look at in future lessons.

\[ J(\theta) = \frac{1}{2}\sum\_{i}(X\_iW - y\_i)^2 + \frac{\lambda}{2}W^TW \]

\[ \frac{\partial{J}}{\partial{W}} = X (\hat{y} - y) + \lambda W \]

\[ W = W - \alpha\frac{\partial{J}}{\partial{W}} \]

| Variable | Description |
| --- | --- |
| \(\lambda\) | regularization coefficient |
| \(\alpha\) | learning rate |

In PyTorch, we can add L2 regularization by adjusting our optimizer. The Adam optimizer has a `weight_decay` parameter which to control the L2 penalty.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` L2_LAMBDA = 1e-2 ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Initialize model model = LinearRegression(input_dim=INPUT_DIM, output_dim=OUTPUT_DIM) ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` # Optimizer (w/ L2 regularization) optimizer = Adam(model.parameters(), lr=LEARNING_RATE, weight_decay=L2_LAMBDA) ``` |

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 ``` | ``` # Training for epoch in range(NUM_EPOCHS):     # Forward pass     y_pred = model(X_train)      # Loss     loss = loss_fn(y_pred, y_train)      # Zero all gradients     optimizer.zero_grad()      # Backward pass     loss.backward()      # Update weights     optimizer.step()      if epoch%20==0:         print (f"Epoch: {epoch} | loss: {loss:.2f}") ``` |

```
Epoch: 0 | loss: 2.20
Epoch: 20 | loss: 0.06
Epoch: 40 | loss: 0.03
Epoch: 60 | loss: 0.02
Epoch: 80 | loss: 0.02
```

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` # Predictions pred_train = model(X_train) pred_test = model(X_test) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # Performance train_error = loss_fn(pred_train, y_train) test_error = loss_fn(pred_test, y_test) print(f"train_error: {train_error:.2f}") print(f"test_error: {test_error:.2f}") ``` |

```
train_error: 0.02
test_error: 0.01
```

Regularization didn't make a difference in performance with this specific example because our data is generated from a perfect linear equation but for large realistic data, regularization can help our model generalize well.

---

To cite this content, please use:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` @article{madewithml,     author       = {Goku Mohandas},     title        = { Linear regression - Made With ML },     howpublished = {\url{https://madewithml.com/}},     year         = {2023} } ``` |

[![](/static/images/anyscale-white-text.svg)](https://www.anyscale.com?utm_source=madewithmml&utm_medium=website&utm_campaign=footer) © 2025 Anyscale, Inc.
 [Anyscale Privacy Policy](https://www.anyscale.com/privacy-policy)

Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
