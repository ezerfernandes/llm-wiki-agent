---
title: "Wei Liu"
type: entity
tags: [person, researcher, computer-vision]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Wei Liu

Computer-vision researcher; lead author of [[SSD|Single-Shot Multibox Detection]] (Liu, Anguelov, Erhan, Szegedy, Reed, Fu & Berg 2016, `Liu.Anguelov.Erhan.ea.2016`) — the canonical **single-stage** object detector, and the architectural counterpart to [[RossGirshick|Girshick]]'s two-stage [[RCNN]] family. At UNC Chapel Hill (PhD) and Google at time of SSD; subsequently in industry research roles. Per [[d2l-computer-vision]] §`ssd`.

## SSD's place in the field

SSD established the **single-stage detector** template: base CNN (truncated [[VGG]] or [[ResNet]]) + multiscale feature-map blocks + per-pixel anchor-based class + bbox prediction heads → concatenate across scales → [[NonMaxSuppression|NMS]]. One forward pass, no separate region-proposal step. Per [[d2l-computer-vision]]: "This model is simple, fast, and widely used."

The single-stage / two-stage split that defines pre-DETR object detection:
- **Two-stage:** [[RCNN]] / [[FastRCNN]] / [[FasterRCNN]] / [[MaskRCNN]] (Girshick et al.) — higher accuracy, slower.
- **Single-stage:** SSD (Liu et al.), YOLO (Redmon et al.), RetinaNet (Lin et al.) — faster, originally lower accuracy on small objects (closed by focal loss + FPN).

## Connections

- [[SSD]] / [[ObjectDetection]] / [[AnchorBox]] / [[MultiscaleObjectDetection]] / [[NonMaxSuppression]].
- Co-authors include Dragomir Anguelov, Dumitru Erhan, [[ChristianSzegedy]], Scott Reed, Cheng-Yang Fu, [[AlexanderBerg|Alexander C. Berg]].
- Architectural cousins: YOLO (Redmon et al.), RetinaNet, EfficientDet.
