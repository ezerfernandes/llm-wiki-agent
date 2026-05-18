---
title: "Dive into Deep Learning — Convolutional Neural Networks"
type: source
tags: [textbook, d2l, cnn, convolution, lenet, computer-vision]
date: 2026-05-16
source_file: raw/d2l-en/chapter_convolutional-neural-networks/
---

## Summary

[[AstonZhang|Zhang]], [[ZacharyLipton|Lipton]], [[MuLi|Li]] & [[AlexanderSmola|Smola]]'s six-section [[CNN]] chapter — D2L's first genuinely *vision-shaped* chapter. The chapter *derives* the [[ConvolutionalLayer|convolutional layer]] from two priors on image data ([[TranslationInvariance|translation invariance]] and [[Locality|locality]]) imposed on a generic [[MultilayerPerceptron|MLP]] — collapsing a $10^{12}$-parameter fully-connected layer over a $1000\times1000$ image into a few hundred shared weights. It then walks the operational stack — [[CrossCorrelation|cross-correlation]] (what frameworks actually compute and call "convolution"), [[Padding|padding]] / [[Stride|stride]] output-shape arithmetic, multi-channel kernels including the [[OneByOneConvolution|$1\times1$ conv]], [[MaxPooling|max-]] / [[AveragePooling|average-pooling]], and [[ReceptiveField|receptive fields]] — and culminates in a from-scratch implementation of [[LeNet|LeNet-5]] ([[YannLeCun|LeCun]] et al. 1989/1998), the first CNN to match SVMs on a real task ([[MNIST]] OCR; <1% per-digit error; deployed in ATMs).

## Key Claims

- **Two priors collapse a fully-connected layer into a convolution.** A $1000\times1000$ image mapped to a $1000\times1000$ hidden layer via [[MultilayerPerceptron|MLP]] needs $10^{12}$ parameters. Imposing [[TranslationInvariance|translation invariance]] ($\mathsf V$ no longer depends on position $(i,j)$ — only on offsets $(a,b)$) gives a [[Convolution|convolution]] with $4\times10^6$ parameters. Imposing [[Locality|locality]] (zero weight outside $|a|,|b|\le\Delta$) cuts that to $4\Delta^2$ — typically a few hundred. This dramatic reduction is the inductive bias CNNs trade for fitting power.
- **What frameworks call "convolution" is actually cross-correlation.** True mathematical convolution flips the kernel: $(f*g)(i,j)=\sum_{a,b} f(a,b)\,g(i-a,j-b)$. The deep-learning operator uses $g(i+a,j+b)$ instead — i.e., [[CrossCorrelation|cross-correlation]]. Because kernels are *learned*, the distinction is cosmetic: the network learns the flipped-kernel version. The literature calls both "convolution" for convenience.
- **Output-shape arithmetic.** Without padding, a $k_h\times k_w$ kernel on an $n_h\times n_w$ input yields $(n_h-k_h+1)\times(n_w-k_w+1)$ output. With total padding $p_h\times p_w$ and stride $s_h\times s_w$: $\lfloor(n_h-k_h+p_h+s_h)/s_h\rfloor\times\lfloor(n_w-k_w+p_w+s_w)/s_w\rfloor$. Setting $p=k-1$ preserves dimensions when $s=1$; doubling the stride halves resolution. Odd kernel sizes ($1,3,5,7$) preferred to allow symmetric padding.
- **Boundary loss is real.** Ten layers of $5\times5$ convolutions on a $240\times240$ image without padding strip the output down to $200\times200$ — 30% of the image gone, with boundary features destroyed. Padding (typically zero-fill) is the standard fix and lets operators be engineered around the zero pattern without allocating extra memory. Padding also lets CNNs implicitly encode position information by "learning where the whitespace is."
- **Multi-channel kernels: input channels sum, output channels stack.** For $c_i$ input channels and $c_o$ output channels the kernel is a $c_o\times c_i\times k_h\times k_w$ tensor. Per output channel, each input channel is cross-correlated with its slice and the $c_i$ results are summed. Output channel intuition: channels learn jointly-useful directions in feature-space, not strictly one-feature-per-channel.
- **The $1\times1$ convolution is a per-pixel fully-connected layer.** A $1\times1$ kernel has no spatial extent — its only computation is a linear combination over the channel axis at each pixel, using $c_o\cdot c_i$ weights. Combined with a nonlinearity it cannot be folded into adjacent convs. Used to cheaply mix channels in [[NetworkInNetwork]] and [[Inception]]-family designs.
- **Compute cost of a conv layer.** For an $h\times w$ image with $k\times k$ kernel and $c_i,c_o$ channels: $\mathcal O(h\cdot w\cdot k^2\cdot c_i\cdot c_o)$. A $256\times256$ image with a $5\times5$ kernel and 128↔128 channels is >53 billion ops per layer — motivates depth-wise / [[ResNeXt|grouped]] convolutions.
- **Pooling has no parameters.** A [[Pooling|pooling]] layer slides a fixed-shape window with stride; at each position it returns the max ([[MaxPooling]]) or mean ([[AveragePooling]]) of the window. No kernel is learned. Pooling applies *per channel* (unlike convolution which sums over channels), so it leaves channel count unchanged. Defaults: window size = stride (non-overlapping); typical $2\times2$ quarters spatial resolution.
- **Max-pooling beats average-pooling.** Max-pooling — introduced by [[RiesenhuberPoggio|Riesenhuber & Poggio (1999)]] in cognitive-neuroscience modeling — confers some translation invariance to small shifts. Average-pooling is "as old as CNNs"; max-pooling is preferred "in almost all cases." Average pooling persists in older architectures (LeNet) and global-average-pooling at network end.
- **Receptive field grows with depth.** The [[ReceptiveField|receptive field]] of an element in a feature map is all the input elements that can affect it via forward propagation. Two stacked $2\times2$ convs give the second-layer output a $3\times3$ receptive field on the original input; deeper networks see more. Hubel & Wiesel's 1959–1968 neurophysiology of the visual cortex inspired the term and convolutional kernels' biological plausibility.
- **LeNet-5 architecture** ([[YannLeCun|LeCun]], [[LeonBottou|Bottou]], Bengio, Haffner 1998). Two-block design: (1) **convolutional encoder** — Conv($6$, $5\times5$, pad $2$) → sigmoid → AvgPool($2\times2$, stride $2$) → Conv($16$, $5\times5$) → sigmoid → AvgPool($2\times2$, stride $2$); (2) **dense block** — Flatten → FC($120$) → sigmoid → FC($84$) → sigmoid → FC($10$) → softmax. Trained with cross-entropy + minibatch SGD + [[XavierInitialization|Xavier init]]. Modernization swaps sigmoid→ReLU and AvgPool→MaxPool.
- **LeNet matched SVMs on MNIST and shipped to ATMs.** At publication LeNet achieved <1% per-digit error on [[MNIST]], matching support-vector-machine SOTA. The model was adopted for ATM check-deposit OCR; some ATMs *still* run LeCun/Bottou's 1990s code. Stands as proof-of-concept that *learned* feature hierarchies could rival hand-engineered features a decade before the [[ImageNet]]-era CNN revival.
- **CNNs as the bridge between MLPs and modern deep learning.** "We moved from the MLPs of the 1980s to the CNNs of the 1990s and early 2000s. The architectures proposed, e.g., in the form of LeNet-5 remain meaningful, even to this day. ... LeNet is much more similar to [ResNet] than to [MLPs]." The chapter explicitly frames CNNs as the recognizable ancestor of every subsequent computer-vision architecture.
- **CNNs are not vision-only.** While derived for images, the same inductive bias (locality + translation invariance) applies to 1-D sequences ([[Audio]], text via TDNNs, time series), to graph-structured data (Kipf & Welling 2016), and to recommender systems. The chapter flags this generality before pivoting to vision.

## Key Quotes

> "Convolutional neural networks (CNNs) are one creative way that machine learning has embraced for exploiting some of the known structure in natural images." — §why-conv, framing CNNs as *prior-driven* not just empirical

> "All learning depends on imposing inductive bias. When that bias agrees with reality, we get sample-efficient models that generalize well to unseen data. But of course, if those biases do not agree with reality, e.g., if images turned out not to be translation invariant, our models might struggle even to fit our training data." — §why-conv, the core CNN trade-off

> "It is noteworthy that since kernels are learned from data in deep learning, the outputs of convolutional layers remain unaffected no matter such layers perform either the strict convolution operations or the cross-correlation operations." — §conv-layer, dissolving the cross-correlation vs. convolution distinction

> "Pooling is an exceedingly simple operation. It does exactly what its name indicates, aggregate results over a window of values. ... pooling is indifferent to channels, i.e., it leaves the number of channels unchanged and it applies to each channel separately." — §pooling summary

> "We moved from the MLPs of the 1980s to the CNNs of the 1990s and early 2000s. The architectures proposed, e.g., in the form of LeNet-5 remain meaningful, even to this day. ... LeNet is much more similar to [ResNet] than to [MLPs]." — §lenet summary

> "To this day, some ATMs still run the code that Yann LeCun and his colleague Leon Bottou wrote in the 1990s!" — §lenet, on LeNet's deployment longevity

## Connections

- [[AstonZhang]] / [[ZacharyLipton]] / [[MuLi]] / [[AlexanderSmola]] — D2L co-authors.
- [[d2l-preface]] — pedagogical context.
- [[YannLeCun]] — LeNet inventor; CNN pioneer (new entity page).
- [[LeonBottou]] — co-author on LeNet papers; co-deployed ATM OCR.
- [[CNN]] — the architecture family this chapter introduces.
- [[Convolution]] / [[CrossCorrelation]] — the core operation and its (cross-correlation) deep-learning incarnation.
- [[ConvolutionalLayer]] — the parameterized layer derived from MLP + priors.
- [[Filter]] / [[ConvolutionKernel]] — the learnable weights.
- [[TranslationInvariance]] / [[Locality]] — the two priors that motivate the convolution.
- [[Padding]] / [[Stride]] — output-shape control knobs.
- [[Channels]] / [[OneByOneConvolution]] — multi-channel arithmetic and the $1\times1$ special case.
- [[Pooling]] / [[MaxPooling]] / [[AveragePooling]] — parameter-free aggregation.
- [[ReceptiveField]] — what a deep layer "sees" on the input.
- [[LeNet]] — the worked example.
- [[MNIST]] — LeNet's benchmark; the "first CNN beats SVM" dataset.
- [[FashionMNIST]] — what D2L actually trains LeNet on (drop-in replacement).
- [[ImageNet]] / [[AlexNet]] — the post-2012 CNN revival (later D2L chapter).
- [[BackpropagationThroughConvolutions]] — implicitly via [[Autograd]]; LeCun's 1989 paper "first to train CNNs via backprop."
- [[XavierInitialization]] — LeNet's init scheme.
- [[Sigmoid]] / [[CrossEntropyLoss]] / [[MinibatchSGD]] — LeNet's activation/loss/optimizer triple.
- [[ComputerVision]] — application domain CNNs dominate.
- [[InductiveBias]] — the conceptual frame.
- [[d2l-multilayer-perceptrons]] — what CNNs *replace* (FC over flattened pixels).
- [[d2l-builders-guide]] — module / `state_dict` / GPU infrastructure LeNet uses.
- [[madewithml-foundations-cnn]] — Mohandas' applied take on the same operations.

## Contradictions

- *None direct.* The chapter reinforces the wiki's existing CNN coverage:
  - [[madewithml-foundations-cnn]] introduces the same operations from an applied-NLP angle; D2L derives them from first principles. Complementary.
  - [[imlbook-cnn-features]] inspects *learned* CNN features (interpretability lens); D2L sits one layer below — how the features are computed, not what they mean. No conflict.
  - [[CNN]] / [[Convolution]] / [[Pooling]] stubs are *expanded*, not contradicted, by this ingest.
- Minor framing note: D2L emphasizes that "in almost all cases, max-pooling is preferable to average pooling" — slightly stronger than the wiki's prior neutrality. Logged on [[MaxPooling]] vs [[AveragePooling]]; not a contradiction.
