---
layout: page

parent_id: 2.3-nn
id: 2-cnn
title: "Convolutional Neural Network (CNN, ResNet)"
---




## Variable image size -> use **global pooling**:
- Option 1: `GlobalPool2d` -> `Linear(num_features, num_classes)` (less computation)
- Option 2: `Conv2d(num_features, num_classes, 3, padding=1)` -> `GlobalPool2d`

> Note in Pytorch. global pooling is done by `AdaptiveAvgPool2d`


## Separable convolution (less computation)



| [MobileNet](https://arxiv.org/abs/1704.04861) style | [Xception](https://arxiv.org/abs/1610.02357) style |
|:---------------------------------------------------:|:--------------------------------------------------:|
|          ![](img/SC_MobileNet.png)                  |            ![](img/SC_Xception.png)                |


## Sota CNNs

|                         | Description                               | Paper                                        |
|:-----------------------:|:------------------------------------------|:--------------------------------------------:|
| **Inception v3**        |                                           | [Dec 2015](https://arxiv.org/abs/1512.00567) |
| **Resnet**              | After 2 convs (3x3->3x3) sum block input  | [Dec 2015](https://arxiv.org/abs/1512.03385) |
| **SqueezeNet**          |                                           | [Feb 2016](https://arxiv.org/abs/1602.07360) |
| **Densenet**            | Concatenate previous layers               | [Aug 2016](https://arxiv.org/abs/1608.06993) |
| **Xception**            | Depthwise Separable Convolutions          | [Oct 2016](https://arxiv.org/abs/1610.02357) |
| **ResNext**             |                                           | [Nov 2016](https://arxiv.org/abs/1611.05431) |
| **DPN**                 | Dual Path Network                         | [Jul 2017](https://arxiv.org/abs/1707.01629) |
| **SENet**               | Squeeze and Excitation (channels weights) | [Sep 2017](https://arxiv.org/abs/1709.01507) |
| **EfficientNet**        | Rethinking Model Scaling                  | [May 2019](https://arxiv.org/abs/1905.11946) |
| **Noisy Student**       | Self-training                             | [Nov 2019](https://arxiv.org/abs/1911.04252) |
| **EfficientNetV2**      | Smaller Models and Faster Training        | [Apr 2021](https://arxiv.org/abs/2104.00298) |
| **ResNet strikes back** | An improved training procedure in timm    | [Oct 2021](https://arxiv.org/abs/2110.00476) |
| **ConvNeXt**            | A ConvNet for the 2020s                   | [Jan 2022](https://arxiv.org/abs/2201.03545) | 

![](img/NoisyStudent.png)

![](img/convnext.jpeg)
