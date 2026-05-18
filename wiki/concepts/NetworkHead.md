---
title: "Network head (CNN)"
type: concept
tags: [deep-learning, cnn, architecture]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# Network head

The **head** is the final section of a modern CNN — the layers that convert the body's feature map into a task-specific output (classification logits, detection boxes, segmentation masks, …). Popularized as a named architectural section by [[GoogLeNet]] ([[ChristianSzegedy|Szegedy]] et al. 2015) and standard in every subsequent design ([[d2l-convolutional-modern]] §googlenet).

## Typical classification head (post-2014)

```
GlobalAvgPool          # [N, C, H, W] → [N, C, 1, 1]
Flatten                # [N, C, 1, 1] → [N, C]
FC(C → num_classes)    # final linear layer
```

The pre-2014 head (AlexNet / VGG-era) was much heavier:

```
Flatten
FC(num_features → 4096) + ReLU + Dropout 0.5
FC(4096 → 4096)        + ReLU + Dropout 0.5
FC(4096 → num_classes)
```

— hundreds of megabytes of parameters. [[NetworkInNetwork|NiN]]'s global-average-pooling trick eliminated this and is now universal.

## Other task heads

| Task | Head |
|---|---|
| Classification | GlobalAvgPool → FC |
| Object detection | RPN + ROI heads ([[Mask R-CNN]] family) |
| Semantic segmentation | Upsampling + per-pixel softmax (U-Net, DeepLab) |
| Instance segmentation | Mask R-CNN's per-ROI mask head |
| Self-supervised pretraining | Projection MLP (SimCLR, MoCo) |

## Stem / body / head — see [[Stem]]

The body produces a "universal" feature map; the head specializes it to the task. This decoupling is what makes pretrained CNN backbones useful for transfer learning — you train a new head on a new task while keeping the body frozen or lightly fine-tuned.

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[Stem]] — sibling section.
- [[GlobalAveragePooling]] — the modern classification-head primitive.
- [[GoogLeNet]] / [[ResNet]] / [[DenseNet]] / [[RegNet]] — all use the stem/body/head template.
- [[Dropout]] — used in the heavy pre-2014 heads.
- [[CNN]] / [[TransferLearning]] / [[FineTuning]] — context.
