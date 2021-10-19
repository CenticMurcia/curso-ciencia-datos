---
layout: page

parent_id: 2.1-tree
id: 2-random-forest
title: 🌳 Random Forest

notebook: notebook-adult-dataset.ipynb
---


Are the easiest to train, because they are extremely resilient to hyperparameter choices, and require very little preprocessing. They are very fast to train, and should not overfit, if you have enough trees. But, they can be a little less accurate, especially if extrapolation is required, such as predicting future time periods

<p align="center"><img width="75%" src="../img/RF.png" /></p>


## Variant 1: Extremely randomized Trees (ET)

In extremely randomized trees (see `ExtraTreesClassifier` and `ExtraTreesRegressor` classes), randomness goes one step further in the way splits are computed. As in random forests, a random subset of candidate features is used, but instead of looking for the most discriminative thresholds, **thresholds are drawn at random for each candidate feature** and the best of these randomly-generated thresholds is picked as the splitting rule. This usually allows to reduce the variance of the model a bit more, at the expense of a slightly greater increase in bias:

## Variant 2: Regularized Greedy Forest (RGF)

- Paper: [Learning Nonlinear Functions Using Regularized Greedy Forest](https://arxiv.org/pdf/1109.0887.pdf)
- https://www.kaggle.com/carlmcbrideellis/introduction-to-the-regularized-greedy-forest

