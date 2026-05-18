---
title: "Dive into Deep Learning — Modern Convolutional Neural Networks"
type: source
tags: [textbook, d2l, cnn, alexnet, vgg, resnet, batchnorm, inception, densenet]
date: 2026-05-16
source_file: raw/d2l-en/chapter_convolutional-modern/
---

## Summary

[[AstonZhang|Zhang]], [[ZacharyLipton|Lipton]], [[MuLi|Li]] & [[AlexanderSmola|Smola]]'s eight-section *Modern CNN* chapter — a chronological tour of the post-[[LeNet|LeNet]] architectures that dominated [[ImageNet]] from 2012 through the [[VisionTransformer|ViT]] era: [[AlexNet]] (2012), [[VGG]] (2014), [[NetworkInNetwork|NiN]] (2013), [[GoogLeNet]] / [[Inception]] (2014), [[BatchNormalization|batch normalization]] (2015), [[ResNet]] + [[ResNeXt]] (2015–2017), [[DenseNet]] (2017), and a closing **design-spaces** section culminating in [[RegNet]]. The chapter's thesis is that CNN design has progressed from *individual neurons → layers → repeating blocks → families of networks → distributions of networks* — and that two interventions ([[BatchNormalization|batch normalization]] and [[ResidualConnection|residual connections]]) made training networks with >100 layers routine, with influence that subsequently propagated into [[transformer|Transformers]] and other non-vision architectures.

## Key Claims

- **AlexNet (2012) won [[ImageNet]] by a wide margin and broke the hand-engineered-features paradigm.** [[AlexKrizhevsky|Krizhevsky]], [[IlyaSutskever|Sutskever]] & [[GeoffreyHinton|Hinton]] (2012) trained an 8-layer CNN (5 conv + 3 FC) on two NVIDIA GTX 580 GPUs (3 GB each, 1.5 TFLOPs each, dual-data-stream split). "This network showed, for the first time, that the features obtained by learning can transcend manually-designed features, breaking the previous paradigm in computer vision." Key ingredients absent in the LeNet era: scale ([[ImageNet]]: 1M images × 1000 categories, $224\times224$ resolution), GPU compute (cuda-convnet), [[ReLU]] in place of sigmoid (no exponential, non-saturating gradient in the positive interval), [[Dropout]] for FC-layer regularization, image augmentation (flips / crops / color jitter).
- **VGG (2014): depth via small kernels and repeated blocks.** [[KarenSimonyan|Simonyan]] & [[AndrewZisserman|Zisserman]] (Visual Geometry Group, Oxford) introduce the **VGG block**: a sequence of $3\times3$ convolutions (padding 1, preserving resolution) followed by a $2\times2$ max-pool (stride 2, halving resolution). Two stacked $3\times3$ convs cover the same receptive field as one $5\times5$ conv but use $2\cdot9c^2=18c^2$ parameters instead of $25c^2$ — and add a nonlinearity in between. "Deep and narrow networks significantly outperform their shallow counterparts." VGG-11 / VGG-16 / VGG-19 are members of a *family* parameterized by `(num_convs, num_channels)` tuples per block — the modern norm of proposing families rather than single models.
- **NiN (2013): $1\times1$ convolutions and global average pooling.** [[MinLin|Lin]], Chen & Yan introduce two innovations that propagate through every subsequent design: (i) **$1\times1$ convolutions** as per-pixel fully-connected layers over the channel axis — adding local nonlinearity across channels without spatial mixing; (ii) **[[GlobalAveragePooling|global average pooling]]** to replace the parameter-hungry FC head (VGG-11's first FC layer alone is ~400 MB in FP32). The NiN block is (initial $k\times k$ conv) → ($1\times1$ conv + ReLU) × 2; the network ends with a NiN block whose output channels equal the number of classes, then global average pooling, then flatten — no FC head at all. Dramatically fewer parameters than AlexNet/VGG with comparable accuracy.
- **GoogLeNet (2014): multi-branch Inception blocks.** [[ChristianSzegedy|Szegedy]] et al. won [[ImageNet]] 2014 with the **Inception block** — four parallel branches concatenated along the channel axis: ($1\times1$), ($1\times1\to3\times3$), ($1\times1\to5\times5$), ($3\times3$ max-pool $\to 1\times1$). Rather than choosing *which* kernel size, GoogLeNet uses *all* of them and lets training allocate capacity across branches. The $1\times1$ convs in branches 2 and 3 act as channel-reduction bottlenecks. GoogLeNet was the first CNN with a clear **stem / body / head** distinction — a design pattern persistent ever since: stem ingests image (2–3 convs), body processes (9 Inception blocks in 3 max-pool-separated groups), head emits classification (global average pool + dense). Cheaper to compute than VGG yet more accurate.
- **Batch normalization (2015) reparametrizes layer activations to stabilize training.** [[SergeyIoffe|Ioffe]] & [[ChristianSzegedy|Szegedy]] (2015) define $\textrm{BN}(\mathbf{x})=\boldsymbol{\gamma}\odot\frac{\mathbf{x}-\hat{\boldsymbol{\mu}}_\mathcal{B}}{\hat{\boldsymbol{\sigma}}_\mathcal{B}}+\boldsymbol{\beta}$, where $\hat{\boldsymbol{\mu}}_\mathcal{B}$, $\hat{\boldsymbol{\sigma}}_\mathcal{B}$ are minibatch statistics and $\boldsymbol{\gamma},\boldsymbol{\beta}$ are learned scale/shift parameters that recover the lost degrees of freedom. For convolutional layers BN is per-channel across the $m\cdot p\cdot q$ elements per channel (compatible with translation invariance); for FC layers it's per-feature. Three combined benefits: preprocessing-like rescaling, regularization via minibatch-statistic noise (works best at batch size 50–100), and numerical stability allowing more aggressive learning rates. Behavior differs in *training mode* (minibatch statistics) vs *prediction mode* (dataset statistics from moving averages).
- **Batch norm's original "internal covariate shift" explanation is now disputed.** The Ioffe & Szegedy motivation — that BN works by reducing distribution drift of intermediate activations — has been challenged ([[Santurkar|Santurkar et al. 2018]] argue BN *increases* covariate shift while still improving optimization). [[AliRahimi|Ali Rahimi]]'s 2017 NeurIPS Test-of-Time speech invoked internal covariate shift as a focal example of "alchemy" in deep learning. D2L's verdict: BN is indispensable in practice (tens of thousands of citations; "applied in nearly all deployed image classifiers"), but the *why* remains an open question; the regularization-through-noise-injection framing is the safer intuition.
- **Layer normalization is BN applied per-observation, not per-minibatch.** [[Ba|Ba]], [[JamieKiros|Kiros]] & [[GeoffreyHinton|Hinton]] (2016): $\textrm{LN}(\mathbf{x})=(\mathbf{x}-\hat{\mu})/\hat{\sigma}$ where statistics are computed *within* a single observation. Independent of batch size; identical at train and test time; scale-independent (approximately). LN becomes the default in [[transformer|Transformers]] where minibatch composition is variable.
- **ResNet (2015): residual connections make the identity easy to learn.** [[KaimingHe|He]], [[XiangyuZhang|Zhang]], [[ShaoqingRen|Ren]] & [[JianSun|Sun]] (2015) won ILSVRC 2015 with depths up to 152 layers. Core insight: for non-nested function classes, adding capacity does not guarantee strictly better fits; if the *added layer* can learn the identity, the new class contains the old. The **residual block** computes $f(\mathbf{x})=\mathbf{x}+g(\mathbf{x})$ — two $3\times3$ convs + BN + ReLU, with the input *added* before the final ReLU. Learning the identity reduces to driving $g\to 0$ (pushing one conv layer's weights to zero). Inputs forward-propagate faster through the shortcut path; gradients backward-propagate without compounding multiplicative attenuation. ResNet-18 / 34 / 50 / 101 / 152 are a depth-parameterized family.
- **The degradation problem ResNet solved.** Prior to residual connections, simply stacking more layers in a CNN *degraded* training accuracy — not from overfitting but from optimization difficulty (the degradation problem). [[ResNet]] showed that 152-layer networks can be trained to lower training error than 20-layer counterparts when residual connections are used. Highway networks ([[Srivastava|Srivastava]] et al. 2015) anticipated the idea with gated bypass paths but lacked the elegant identity parametrization. Residual blocks have since been adopted in RNNs, Transformers, graph neural networks, and beyond.
- **ResNet's first two layers mirror GoogLeNet's stem.** $7\times7$ conv (64 channels, stride 2) → BN → ReLU → $3\times3$ max-pool (stride 2). Body = four modules, each containing two residual blocks; the first block of each module after the first uses `use_1x1conv=True, strides=2` to halve resolution and double channels. Head = global average pool + FC. The structure "is similar to GoogLeNet but ResNet's structure is simpler and easier to modify" — a major driver of its adoption.
- **ResNeXt: grouped convolutions trade channels for parameters.** [[Xie|Xie]], [[RossGirshick|Girshick]], [[PiotrDollar|Dollár]] et al. (2017) generalize ResNet by sandwiching a *grouped* $3\times3$ conv between two $1\times1$ convs (bottleneck). Splitting $c_i\to c_o$ into $g$ groups of $c_i/g\to c_o/g$ reduces both parameters and FLOPs by factor $g$. ResNeXt adopts the *same* transformation in all branches (vs. Inception's heterogeneous branches) — minimizing manual tuning. The bottleneck design also predates ResNeXt: it's used in deep ResNet-50/101/152 variants.
- **DenseNet (2017): concatenate features instead of adding them.** [[GaoHuang|Huang]], [[ZhuangLiu|Liu]], [[KilianWeinberger|Weinberger]] & [[LaurensVanDerMaaten|van der Maaten]] generalize ResNet by *concatenating* each layer's output to all previous layers' outputs: $\mathbf{x}\to[\mathbf{x},f_1(\mathbf{x}),f_2([\mathbf{x},f_1(\mathbf{x})]),\ldots]$. Each layer sees all prior features and contributes `growth_rate` new channels. Two block types: **dense blocks** (concat-on-channel within a stage) and **transition layers** (BN → ReLU → $1\times1$ conv → average pool, halving channels and resolution between stages). Strong feature reuse; smaller parameter counts than equivalent ResNets — but heavy GPU memory consumption from the concatenations.
- **Design-spaces > single best networks (RegNet).** [[IliaRadosavovic|Radosavovic]] et al. (2020) reject the [[NeuralArchitectureSearch|NAS]] paradigm of "find the single best network" in favor of **design spaces** — parameterized distributions of networks. Starting from AnyNet (stem + body of 4 stages × $d_i$ ResNeXt blocks + head; 17 hyperparameters) they progressively constrain via empirical CDF comparisons: tie bottleneck ratios across stages (no accuracy loss), tie group widths (no loss), require channels and depths to increase across stages (improves). Best-performing networks satisfy $c_j\approx c_0+c_a j$ (linear width growth with block index) and $k=1$ (no bottleneck). The output is a family (RegNetX / RegNetY) with explicit design principles — "scientific insights on the way" — instead of one architecture.
- **Generic modern CNN template: stem / body / head, body in stages.** Every architecture from VGG through RegNet shares: **stem** (initial conv with larger window to halve resolution and produce $c_0$ channels), **body** of multiple **stages** at decreasing resolution (each stage halves spatial resolution and increases channel count via stride-2 downsampling block + repeated same-resolution blocks), **head** (global average pool + FC). The chapter explicitly extracts this template as the generic AnyNet design space.
- **The CNN-to-Transformer transition: scalability trumps inductive biases.** The chapter closes by noting that [[VisionTransformer|ViT]] ([[Dosovitskiy|Dosovitskiy]] et al. 2021) and Swin Transformer ([[Liu|Liu]] et al. 2021) have displaced CNNs at the very top of [[ImageNet]] leaderboards. Transformers have *less* locality / translation-invariance inductive bias than CNNs, but at LAION-400m / LAION-5B scale, learned structures prevail. [[Liu|Liu]] et al. (2022) ConvNeXt show CNNs can recover competitive accuracy via modern training recipes, but only at higher computational cost; NVIDIA Ampere / Hopper hardware further widens the gap in Transformers' favor.

## Key Quotes

> "AlexNet, which employed an 8-layer CNN, won the ImageNet Large Scale Visual Recognition Challenge 2012 by a large margin. This network showed, for the first time, that the features obtained by learning can transcend manually-designed features, breaking the previous paradigm in computer vision." — §alexnet, the watershed claim

> "The successive application of two $3 \times 3$ convolutions touches the same pixels as a single $5 \times 5$ convolution does. ... In a rather detailed analysis they showed that deep and narrow networks significantly outperform their shallow counterparts. This set deep learning on a quest for ever deeper networks with over 100 layers for typical applications." — §vgg, the small-kernel doctrine

> "The idea behind NiN is to apply a fully connected layer at each pixel location (for each height and width). The resulting $1 \times 1$ convolution can be thought of as a fully connected layer acting independently on each pixel location." — §nin, the channel-mixing reframe of $1\times1$ convs

> "Together with residual blocks — covered later — batch normalization has made it possible for practitioners to routinely train networks with over 100 layers. A secondary (serendipitous) benefit of batch normalization lies in its inherent regularization." — §batch-norm, the practical bottom line

> "At the heart of their proposed *residual network* (*ResNet*) is the idea that every additional layer should more easily contain the identity function as one of its elements. These considerations are rather profound but they led to a surprisingly simple solution, a *residual block*." — §resnet, the function-class argument distilled

> "ResNeXt is an example for how the design of convolutional neural networks has evolved over time: by being more frugal with computation and trading it off against the size of the activations (number of channels), it allows for faster and more accurate networks at lower cost." — §resnext, the channel-vs-compute trade-off

> "Scalability trumps inductive biases." — §cnn-design discussion, the chapter's parting verdict on the CNN-to-Transformer transition (citing Dosovitskiy et al. 2021)

## Connections

- [[AstonZhang]] / [[ZacharyLipton]] / [[MuLi]] / [[AlexanderSmola]] — D2L co-authors.
- [[d2l-preface]] — pedagogical context.
- [[d2l-convolutional-neural-networks]] — direct prerequisite (LeNet, conv layer, pooling, $1\times1$ convs, channels).
- [[d2l-multilayer-perceptrons]] — Dropout, ReLU, vanishing gradients motivate this chapter.
- [[CNN]] — parent concept; this chapter is the post-LeNet history of CNN design.
- [[AlexKrizhevsky]] / [[IlyaSutskever]] / [[GeoffreyHinton]] — AlexNet authors (new entities).
- [[KarenSimonyan]] / [[AndrewZisserman]] — VGG authors (new entities).
- [[ChristianSzegedy]] — GoogLeNet / Inception / batch-norm co-author (new entity).
- [[SergeyIoffe]] — batch-norm co-author (new entity).
- [[KaimingHe]] — ResNet first author (new entity).
- [[AlexNet]] — 2012 ImageNet winner (new concept).
- [[VGG]] — Oxford / Simonyan-Zisserman (new concept).
- [[NetworkInNetwork]] — Lin et al. 2013, $1\times1$ + global avg pool (new concept).
- [[GoogLeNet]] / [[Inception]] — Szegedy et al. 2014, multi-branch (new concept).
- [[ResNet]] — He et al. 2015, residual blocks (new concept).
- [[ResNeXt]] — Xie et al. 2017, grouped convolutions (new concept).
- [[DenseNet]] — Huang et al. 2017, concatenation-not-addition (new concept).
- [[RegNet]] — Radosavovic et al. 2020, design-space output (new concept).
- [[ResidualConnection]] / [[SkipConnection]] — the core ResNet primitive; ubiquitous (new concept).
- [[ResidualBlock]] — two $3\times3$ + BN + ReLU + add (new concept).
- [[GlobalAveragePooling]] — NiN's FC-head replacement; ubiquitous (new concept).
- [[GroupedConvolution]] — ResNeXt's bottleneck primitive (new concept).
- [[Bottleneck]] — $1\times1\to k\times k\to 1\times1$ pattern (new concept).
- [[Stem]] / [[NetworkHead]] — the body/head terminology GoogLeNet popularized (new concepts).
- [[BatchNormalization]] — Ioffe & Szegedy 2015 (existing — substantial expansion).
- [[LayerNormalization]] — Ba/Kiros/Hinton 2016 (new concept).
- [[Dropout]] — AlexNet was the first deployed system to use it at scale (existing).
- [[ReLU]] — AlexNet replaced sigmoid with ReLU (existing — flagged).
- [[OneByOneConvolution]] — NiN's signature primitive; ResNet/Inception bottleneck workhorse (existing — flagged).
- [[Pooling]] / [[MaxPooling]] / [[AveragePooling]] — global average pooling joins the family (existing).
- [[NeuralArchitectureSearch]] — RegNet positions itself against NAS (new concept).
- [[InductiveBias]] — chapter closes with "scalability trumps inductive biases."
- [[ImageNet]] — every architecture in the chapter is dated by its ILSVRC year.
- [[VisionTransformer]] — the post-CNN successor flagged in the closing discussion.
- [[google]] / [[googledeepmind]] — GoogLeNet, batch-norm, Inception authoring.
- [[Microsoft|Microsoft Research]] — ResNet's institutional home (He, Zhang, Ren, Sun were at MSRA in 2015).
- [[oxforduniversity]] — VGG's home; Visual Geometry Group.
- [[fair]] / [[meta]] — Xie, Girshick, Dollár were at FAIR for ResNeXt.

## Contradictions

- *None direct.* The chapter reinforces and extends existing wiki coverage:
  - [[d2l-convolutional-neural-networks]] introduced the conv layer + LeNet; this chapter is the strict next step (post-LeNet architectures).
  - [[BatchNormalization]] stub gains substantial body — the "BN ≡ reduces internal covariate shift" framing the stub implicitly endorses is now flagged as *historically motivating but empirically disputed* per [[Santurkar|Santurkar et al. 2018]].
  - [[Dropout]]'s page already names AlexKrizhevsky as a co-author of [[Dropout]] (Srivastava et al. 2014); this chapter is where Dropout's role *in AlexNet* (the deployment that put it on the map) is documented.
  - [[OneByOneConvolution]] already credits [[NetworkInNetwork]] (Lin et al. 2013) as the source; this chapter is the canonical narrative reference for that history.
  - Minor framing note: the wiki's [[CNN]] page lists VGG, GoogLeNet, ResNet, ResNeXt, EfficientNet as the post-AlexNet arc; this chapter expands NiN, DenseNet, and RegNet onto that lineage without contradicting it.
