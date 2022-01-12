---
layout: page

parent_id: 3.6-img2img
id: 2-instance-seg
title: 🔲✂️ Instance Segmentatition
---





## 🔲 -> ✂️

Traditional approach. First detect bboxes, then segment each box.

|                                                    |                            | Date     |
|----------------------------------------------------|----------------------------|----------|
| [**Mask R-CNN**](https://arxiv.org/abs/1703.06870) |                            | Mar 2017 |
| [**PANet**     ](https://arxiv.org/abs/1803.01534) | Path Aggregation Network   | Mar 2018 |
| [**HTC**       ](https://arxiv.org/abs/1901.07518) | Hybrid Task Cascade        | Jan 2019 | 


## Single-Shot

|                                                   |                                                             | Date     |
|---------------------------------------------------|-------------------------------------------------------------|----------|
| [YOLACT       ](https://arxiv.org/abs/1904.02689) | Real-time Instance Segmentation                             | Apr 2019 |
| [SSAP         ](https://arxiv.org/abs/1909.01616) | Single-Shot Instance Segmentation With Affinity Pyramid     | Sep 2019 |
| [PolarMask    ](https://arxiv.org/abs/1909.13226) | Single Shot Instance Segmentation with Polar Representation | Sep 2019 |
| [SOLO         ](https://arxiv.org/abs/1912.04488) | Segmenting Objects by Locations                             | Dec 2019 |
| [YOLACT++     ](https://arxiv.org/abs/1912.06218) | Better real-time instance segmentation                      | Dec 2019 |
| [BlendMask    ](https://arxiv.org/abs/2001.00309) | Top-Down Meets Bottom-Up for Instance Segmentation          | Jan 2020 |
| [SOLOv2       ](https://arxiv.org/abs/2003.10152) | Dynamic and fast instance segmentation                      | Mar 2020 |
| [CenterMask   ](https://arxiv.org/abs/2004.04446) | Single shot instance segmentation with point representation | Apr 2020 |

> #### Unet predicting boundaries
> - This method works very well for round obects (microscopic cells, cars, ...) 
> - This method works very bad for complex shapes (persons, occussions, etc.)
> - Paper [Deep Watershed Transform for Instance Segmentation](https://arxiv.org/abs/1611.08303) Nov 2016
> - https://on-demand.gputechconf.com/gtc/2017/presentation/s7588-min-bai-deep-watershed-transform-for-instance-segmentation.pdf
> - https://www.kaggle.com/c/data-science-bowl-2018/discussion/55118



> #### Unet predicting embedding per piexel
> - Trained with a metric learning approach, pixels of the same instace wil have sililar embeddings
> - Paper [Semantic Instance Segmentation via Deep Metric Learning](https://arxiv.org/abs/1703.10277) Mar 2017



## Resorces

- [Review of object instance segmentation based on deep learning](https://www.spiedigitallibrary.org/journals/journal-of-electronic-imaging/volume-31/issue-4/041205/Review-of-object-instance-segmentation-based-on-deep-learning/10.1117/1.JEI.31.4.041205.full) 6 December 2021
