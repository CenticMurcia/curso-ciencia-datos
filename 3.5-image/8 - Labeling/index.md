---
layout: page

parent_id: 3.5-image
id: "8 - Labeling"
title: 🏷️ Labeling
---



## Labeling Formats for Bounding Boxes


- JSON
  - COCO
  - CreateML
- XML
  - Pascal VOC
- TXT
  - YOLO Darknet
  - YOLO v3 Keras
  - YOLO v4 PyTorch
  - Scaled-YOLOv4
  - YOLO v5 PyTorch
- CSV
  - Tensorflow Object Detection
  - RetinaNet Keras
  - Multiclass Classification
- Others
  - OpenAI CLIP Classification
  - Tensorflow TFRecord (binary format)


## YOLO labeling format

- One `.txt` file per image.
- If no objects in image, no `.txt` file is required.
- One row per bounding box (`class_id` `center_x` `center_y` `width` `height`).
- XYWH numbers must be normalized from 0 to 1.
- Class numbers are zero-indexed (start from 0).

<p align="center"> <img width="90%" src="img/YOLO-image.jpg"/> </p>

<p align="center"> <img width="90%" src="img/YOLO-label.png"/> </p>

> Source:
> - [Roboflow Formats for Bounding Boxes](https://roboflow.com/formats)
> - [YOLOv5: Train Custom Data](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)


## Labeling Tools

- [labelImg](https://github.com/tzutalin/labelImg)
  - https://blog.roboflow.com/labelimg/
- [Computer Vision Annotation Tool (CVAT)](https://github.com/openvinotoolkit/cvat)
  - https://blog.roboflow.com/cvat/
- [Roboflow Annotate](https://docs.roboflow.com/annotate)
