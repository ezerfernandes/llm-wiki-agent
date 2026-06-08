---
title: "Convolutional Neural Network"
type: concept
tags: [deep-learning, architectures, cnn, computer-vision]
sources: [d2l-convolutional-neural-networks, madewithml-foundations-cnn, imlbook-cnn-features, mlsysbook-ch06-network-architectures]
last_updated: 2026-06-05
---

# CNN

A **convolutional neural network** is a neural network whose hidden layers are predominantly [[ConvolutionalLayer|convolutional layers]] — operators that slide a small learnable [[Filter|kernel]] over a spatially-structured input and produce a feature map per output channel. CNNs dominate [[ComputerVision]] (and increasingly audio, time series, graphs) because their architecture *bakes in* two priors that natural images satisfy: [[TranslationInvariance|translation invariance]] (the same pattern means the same thing at any location) and [[Locality|locality]] (nearby pixels matter more than distant ones).

## Why CNNs exist — derivation from an MLP

[[d2l-convolutional-neural-networks]] §why-conv derives the convolutional layer as a *constrained* fully-connected layer:

1. **Fully-connected layer on images:** $[\mathbf{H}]_{i,j}=u+\sum_{a,b}[\mathsf V]_{i,j,a,b}[\mathbf X]_{i+a,j+b}$. A $1000\times1000$ image to a $1000\times1000$ hidden layer needs **$10^{12}$ parameters** — infeasible.
2. **Impose [[TranslationInvariance|translation invariance]]:** weights cannot depend on position. $\mathsf V_{i,j,a,b}\to V_{a,b}$. *This is now a [[Convolution|convolution]].* Down to $4\times10^6$ parameters.
3. **Impose [[Locality|locality]]:** $V_{a,b}=0$ for $|a|,|b|>\Delta$. Down to $4\Delta^2$ — typically a few hundred.

CNNs are not arbitrary engineering — they are the *unique* architecture you get from applying two reasonable priors. As D2L puts it: "all learning depends on imposing inductive bias. When that bias agrees with reality, we get sample-efficient models that generalize well."

## Components

- **[[ConvolutionalLayer|Convolutional layer]]** — learned [[Filter|filter]] applied via [[CrossCorrelation|cross-correlation]]; the workhorse.
- **Nonlinearity** — typically [[ReLU]] (modern) or [[Sigmoid]] (LeNet-era).
- **[[Pooling|Pooling layer]]** — parameter-free aggregation ([[MaxPooling|max]] or [[AveragePooling|average]]) over a window; provides downsampling + a degree of translation invariance.
- **[[Channels]]** — input/output channel axes; multi-channel kernels of shape $c_o\times c_i\times k_h\times k_w$.
- **[[Padding]] / [[Stride]]** — output-shape control knobs.
- **[[OneByOneConvolution|$1\times1$ convolution]]** — per-pixel fully-connected over the channel axis; cheap channel mixing.
- **Final dense block** — flatten + a few [[LinearLayer|FC layers]] + softmax for classification. (Modern fully-convolutional nets skip this in favor of global average pooling.)
- **Training** — [[Backpropagation]] + [[MinibatchSGD]] + [[CrossEntropyLoss]] (or task-specific loss). [[XavierInitialization|Xavier]]/[[HeInitialization|He]] init.

## Why CNNs are computationally friendly

- **Parameter count:** orders of magnitude fewer than an MLP at the same input resolution (the whole derivation point).
- **Parallelism:** the same kernel applied independently at every spatial location maps perfectly to GPU SIMT; Chetlur et al. 2014 ([[cuDNN]]) is the canonical reference for this.
- **Cost per layer:** $\mathcal O(h\cdot w\cdot k^2\cdot c_i\cdot c_o)$. A $256\times256$ image with $5\times5$ kernel and 128↔128 channels = >53 billion ops/layer — motivates [[ResNeXt|grouped]] / [[DepthwiseConvolution|depth-wise]] convolutions in modern designs.

## Receptive fields, biology, and depth

- Each output element has a [[ReceptiveField|receptive field]] on the input — the set of input pixels that can affect it. Two stacked $2\times2$ convs give a $3\times3$ receptive field; deeper networks see more.
- Hubel & Wiesel's 1959–1968 cat-visual-cortex experiments inspired both the term *receptive field* and the architectural choice. Field 1987 illustrated that natural-image statistics line up with convolutional kernels. CNNs are "biologically plausible" in this loose sense.

## Historical arc

- **[[Neocognitron]] (Fukushima 1982)** — earliest CNN-shaped architecture.
- **[[LeNet|LeNet-5]] ([[YannLeCun|LeCun]] et al. 1989/1998)** — first CNN trained with [[Backpropagation]] to match SVMs on real OCR; deployed to ATMs.
- **[[AlexNet]] (Krizhevsky, Sutskever, [[GeoffreyHinton|Hinton]] 2012)** — CNN wins [[ImageNet]] by a wide margin; ignites the deep-learning revival.
- **VGG / [[GoogLeNet]] / [[ResNet]] / [[ResNeXt]] / [[EfficientNet]]** — depth, residual connections, and channel-efficiency innovations.
- **[[VisionTransformer|ViT]] (2020)** — first credible non-convolutional architecture for vision at scale; CNNs still competitive (and dominant at low data).

## Beyond images

The locality + translation-invariance prior is not vision-only: 1-D convolutions for audio (TDNNs, [[WaveNet]]), text ([[Kalchbrenner|Kalchbrenner et al. 2014]]), time series; graph convolutions for non-Euclidean data (Kipf & Welling 2016); convolutional collaborative filters in recommender systems.

## Connections

- [[d2l-convolutional-neural-networks]] — canonical pedagogical derivation.
- [[madewithml-foundations-cnn]] — applied-NLP CNN walkthrough.
- [[imlbook-cnn-features]] — interpretability lens on learned CNN features.
- [[Convolution]] / [[CrossCorrelation]] — the core operation.
- [[ConvolutionalLayer]] — the parameterized building block.
- [[Filter]] — the learnable weights.
- [[Padding]] / [[Stride]] / [[Pooling]] / [[Channels]] / [[ReceptiveField]] / [[OneByOneConvolution]] — siblings.
- [[LeNet]] / [[AlexNet]] / [[ResNet]] / [[VisionTransformer]] — architectures.
- [[ComputerVision]] — primary application domain.
- [[TranslationInvariance]] / [[Locality]] / [[InductiveBias]] — conceptual frame.
- [[Backpropagation]] / [[XavierInitialization]] / [[CrossEntropyLoss]] / [[MinibatchSGD]] — training stack.
- [[mlsysbook-ch06-network-architectures]] — systems view: CNNs are the *compute-bound* family (high [[ArithmeticIntensity|arithmetic intensity]], ~40 FLOP/byte for [[ResNet|ResNet-50]]) thanks to [[WeightSharing|weight sharing]], which decouples parameter count from input resolution (~5,500× fewer params than the equivalent FC layer); implemented on hardware via [[Im2col|im2col]]→[[GEMM]]; the spatial-locality [[InductiveBias|inductive bias]] gives ~47× fewer params than an MLP on MNIST.
