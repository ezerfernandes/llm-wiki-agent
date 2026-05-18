---
title: "Ross Girshick"
type: entity
tags: [person, researcher, computer-vision]
sources: [d2l-computer-vision]
last_updated: 2026-05-16
---

# Ross Girshick

Computer-vision researcher; the architect of the **R-CNN family** of object detectors — the canonical two-stage detector lineage. At UC Berkeley (PhD with [[JitendraMalik|Jitendra Malik]]) → Microsoft Research → [[FAIR|Facebook AI Research]]. Per [[d2l-computer-vision]] §`rcnn`.

## Key papers (chronological)

- **[[RCNN|R-CNN]]** (Girshick, Donahue, Darrell & Malik 2014) — `Girshick.Donahue.Darrell.ea.2014` — first CNN-based object detector to dramatically outperform handcrafted features. Selective search → 2000 region proposals → per-region CNN → per-class SVMs + bbox regression. ~30%+ mAP jump on Pascal VOC.
- **[[FastRCNN|Fast R-CNN]]** (Girshick 2015) — `Girshick.2015` — single CNN forward pass over the whole image + [[ROIPooling|RoI pooling]] per proposal. End-to-end trainable. ~10× speedup over R-CNN.
- **[[FasterRCNN|Faster R-CNN]]** ([[ShaoqingRen|Ren]], [[KaimingHe|He]], Girshick & Sun 2015) — `Ren.He.Girshick.ea.2015` — learned [[RegionProposalNetwork|RPN]] replaces [[SelectiveSearch]]. Real-time two-stage detection.
- **[[MaskRCNN|Mask R-CNN]]** ([[KaimingHe|He]], Gkioxari, Dollár & Girshick 2017) — `He.Gkioxari.Dollar.ea.2017` — adds [[ROIAlign]] + per-RoI pixel-mask head; extends Faster R-CNN to instance segmentation. De facto baseline on COCO for years.
- **Detectron / Detectron2** — FAIR's reference codebase implementing the R-CNN family and many CV models; Girshick was a central contributor.

## Impact

Defined the **two-stage detector** paradigm that dominated object detection from 2014 until the rise of DETR (2020). His R-CNN → Fast → Faster → Mask lineage is the textbook arc in [[d2l-computer-vision]] §`rcnn`; every variant builds on the previous one's core insights (selective search → RPN, RoI pooling → RoI align, bbox → mask).

## Connections

- [[RCNN]] / [[FastRCNN]] / [[FasterRCNN]] / [[MaskRCNN]] / [[ROIPooling]] / [[ROIAlign]] / [[RegionProposalNetwork]] / [[ObjectDetection]] / [[InstanceSegmentation]].
- Collaborators: [[KaimingHe]], [[ShaoqingRen]], [[JitendraMalik]], Trevor Darrell, Piotr Dollár, Georgia Gkioxari.
- [[FAIR]] / [[MicrosoftResearch]] / [[UniversityOfCaliforniaBerkeley|UC Berkeley]] — institutional affiliations.
