<h1 align="center">Metric Learning</h1>

> Note that **Metric Learning** is also known as:
> - **Similarity learning**
> - **Contrastive Learning**
> - **Embedding learning**

Metric learning is the task of **training a similarity function that measures how similar or related two (or 3) objects are**.

Metric learning is very **useful for classifications problems when the data is unbalanced** or there are very few samples.

The input data becomes from 1 sample (classification) to 2 samples (metric learning) by using **Siamese Networks**

This augment your dataset a lot (Combinations of N objets in pairs formula). If you have 100 images, your net sees 4950 cases!



## Clasification VS Metric learning


| Classification | Metric learning |
|----------------|-----------------|
| Embeddings from different classes need to be easily separable. | Embedding from the same class need to be close together, and embedding from different classes need to be far from each others. |



## Mining
Mining is the process of finding the best pairs or triplets to train on. T



## Clasification Losses
- Categorical Cross-Entropy Loss,
- Binary Cross-Entropy Loss,
- Softmax Loss,
- Logistic Loss,
- Focal Loss


## Metric Learning Losses

Cross-entropy is valid choice of loss function, same as contrastive or triplet on L2 distance.

- Pairwise Losses (Parejas de datos de entrada)
  - Concat embs                 -> Binary classification (fastai siamese)
    - Downside: The model is not "symmetrical", (the input of [img A, img B] will give a different output from [img B, img A]
  - Absolute difference of embs -> Binary classification
  - Cosine similarity of embs   -> Regression
- Triplet Loss (Trios como datos de entrada)
  1. Anchor: represents a reference
  2. Positive: same class as the anchor
  3. Negative: a different class
- Contrastive Loss
  - ArcFace
  - CosFace
  - SphereFace
- Margin Loss
- Hinge Loss

## SimCLR: Metric Learning for unsupervised data

<p align="center"><img width="66%" src="img/SimCLR.gif"/></p>


## Reference

- Metric learning have won Kaggle classification competitions of unbalanced data:
  - [Human Protein Atlas Image Classification](https://kaggle.com/c/human-protein-atlas-image-classification)
    - [1st place solution](https://kaggle.com/c/human-protein-atlas-image-classification/discussion/78109)
  - [Humpback Whale Identification](https://www.kaggle.com/c/humpback-whale-identification)
     - [1st place solution](https://www.kaggle.com/c/humpback-whale-identification/discussion/82366)
     - https://medium.com/datadriveninvestor/a-hackers-guide-to-efficiently-train-deep-learning-models-b2cccbd1bc0a
- Keras Examples
  - [Metric learning for image similarity search](https://keras.io/examples/vision/metric_learning)
  - [Supervised Contrastive Learning](https://keras.io/examples/vision/supervised-contrastive-learning/)