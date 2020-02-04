# Tree based models

- Single tree -> Decission Tree
- Average of trees -> Random Forest & Extra Trees
- Concatenation of trees -> Gradient boosting

## [Jeremy Howard on twitter](https://twitter.com/jeremyphoward/status/1223777020934361088): Our advice for tabular modeling

We have two approaches to tabular modelling: decision tree ensembles, and neural networks. And we have mentioned two different decision tree ensembles: random forests, and gradient boosting machines. Each is very effective, but each also has compromises:

**Random forests** are the easiest to train, because they are extremely resilient to hyperparameter choices, and require very little preprocessing. They are very fast to train, and should not overfit, if you have enough trees. But, they can be a little less accurate, especially if extrapolation is required, such as predicting future time periods

**Gradient boosting machines** in theory are just as fast to train as random forests, but in practice you will have to try lots of different hyperparameters. They can overfit. At inference time they will be less fast, because they cannot operate in parallel. But they are often a little bit more accurate than random forests.

**Neural networks** take the longest time to train, and require extra preprocessing such as normalisation; this normalisation needs to be used at inference time as well. They can provide great results, and extrapolate well, but only if you are careful with your hyperparameters, and are careful to avoid overfitting.

We suggest starting your analysis with a random forest. This will give you a strong baseline, and you can be confident that it's a reasonable starting point. You can then use that model for feature selection and partial dependence analysis, to get a better understanding of your data.

From that foundation, you can try neural nets and GBMs, and if they give you significantly better results on your validation set in a reasonable amount of time, you can use them.
