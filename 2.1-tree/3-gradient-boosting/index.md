---
layout: page

parent_id: 2.1-tree
id: 3-gradient-boosting
title: 🌳 Gradient Boosting (XGBoost, LGBM, CatBoot)

notebook: notebook-adult-dataset.ipynb
---



# Gradient Boosting (GBM)

In theory are just as fast to train as random forests, but in practice you will have to try lots of different hyperparameters. They can overfit. At inference time they will be less fast, because they cannot operate in parallel. But they are often a little bit more accurate than random forests.

<p align="center"><img width="100%" src="../img/GB.png" /></p>

<p align="center"><img width="50%" src="../img/GradientBoosting.png" /></p>


# 🔧 Hyperparameters


|           | sklearn<br>Random Forest | XGBoost<br>Gradient Boosting | LightGBM<br>Gradient Boosting | Try |
|--------------------------------------|:--------------------:|:----------------:|:----------------:|-------------|
| 🔷 Number of trees                   | N_estimators         | num_round 💡     | num_iterations 💡| [10,...,1000] |
| 🔷 Max depth of the tree             | max_depth            | max_depth        | max_depth        | 3,...,10    |
| 🔶 Min cases per final tree leaf     | min_samples_leaf     | min_child_weight | min_data_in_leaf |             |
| 🔷 % of rows used to build the tree  | max_samples          | subsample        | bagging_fraction | 0.8         |
| 🔷 % of feats used to build the tree | max_features         | colsample_bytree | feature_fraction |             |
| 🔷 Speed of training                 | NOT IN FOREST        | eta              | learning_rate    |             |
| 🔶 L1 regularization                 | NOT IN FOREST        | lambda           | lambda_l1        |             |
| 🔶 L2 regularization                 | NOT IN FOREST        | alpha            | lambda_l2        |             |
| Random seed                          | random_state         | seed             | _seed            |             |


> - 🔷: Increase parameter for overfit,  decrease for underfit.
> - 🔶: Increase parameter for underfit, decrease for overfit. (regularization)
> - 💡: For Gradient Boosting maybe is better to do early stopping rather than set a fixed number of trees.


