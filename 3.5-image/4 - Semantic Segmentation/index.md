---
layout: page

parent_id: 3.5-image
id: 4 - Semantic Segmentation
title: ✂️ Semantic Segmentatition
---



<p align="center"><img width="50%" src="img/segmentationInstance.png" /></p>

Get pixel-level classes. Note that the model backbone can be a resnet, densenet, inception...


| Name                                              | Description                           | Date     | Instances |
|:-------------------------------------------------:|---------------------------------------|:--------:|:---------:|
| [**FCN**      ]()                                 | Fully Convolutional Network           | 2014     |           |
| [**SegNet**   ](https://arxiv.org/abs/1511.00561) | Encoder-decorder                      | 2015     |           |
| [**Unet**     ](https://arxiv.org/abs/1505.04597) | Concatenate like a densenet           | 2015     |           |
| [**ENet**     ](https://arxiv.org/abs/1606.02147) | Real-time **video** segmentation      | 2016     |           |
| [**PSPNet**   ](https://arxiv.org/abs/1612.01105) | Pyramid Scene Parsing Net             | 2016     |           |
| [**FPN**      ](https://arxiv.org/abs/1612.03144) | Feature Pyramid Networks              | 2016     | Yes       |
| [**DeepLabv3**](https://arxiv.org/abs/1706.05587) | Increasing dilatation & field-of-view | 2017     |           |
| [**LinkNet**  ](https://arxiv.org/abs/1707.03718) | Adds like a resnet                    | 2017     |           |
| [**PANet**    ](https://arxiv.org/abs/1803.01534) | Path Aggregation Network              | 2018     | Yes       |
| [**Panop FPN**](https://arxiv.org/abs/1901.02446) | Panoptic Feature Pyramid Networks     | 2019     | ?         |
| [**PointRend**](https://arxiv.org/abs/1912.08193) | Image Segmentation as Rendering       | 2019     | ?         |


> **Feature Pyramid Networks (FPN): [slides](http://presentations.cocodataset.org/COCO17-Stuff-FAIR.pdf)**


## Depth segmentation
Learning the Depths of Moving People by Watching Frozen People (mannequin challenge) [paper](https://arxiv.org/abs/1904.11111)
<p align="center"><img src="img/segmentationDepth.jpg"/></p>

## Surface normal segmentation
<p align="center"><img width="60%" src="img/segmentationOthers.png" /></p>

- [paper](https://arxiv.org/abs/1411.4958) (2014)

## Reference

- [Image Segmentation Using Deep Learning: A Survey](https://arxiv.org/abs/2001.05566)  Nov 2020
- https://www.jeremyjordan.me/semantic-segmentation
- https://www.jeremyjordan.me/evaluating-image-segmentation-models
- Check [Res2Net](https://arxiv.org/abs/1904.01169)
- Check [catalyst segmentation tutorial (Ranger opt, albumentations, ...)](https://colab.research.google.com/github/catalyst-team/catalyst/blob/master/examples/notebooks/segmentation-tutorial.ipynb#scrollTo=Zm7JsNrczOQG)
- [this repo](https://github.com/qubvel/segmentation_models)