---
layout: page

parent_id: 1.2-eda
id: 5-dimred
title: 🌀 Dimensionality Red. (PCA, tSNE, UMAP)
---

**Dimensionality Reduction** is a type of **multivariate analysis** based on plotting all the variables into a 2D or 3D scatter plot.

## Why reduce dimensions?
- Remove multicollinearity
- Deal with the curse of dimensionality
- Remove redundant features
- Interpretation & Visualization
- Make computations easier
- Identify Outliers


| Method       | Name                                          | Based in                   | Duration |
|:------------:|:----------------------------------------------|----------------------------|----- |
| **PCA**      | **P**rincipal **C**omponent **A**nalysis      | Linear (maximize variance) | Fast |
| **t-SNE**    | t Stochastic Neighbor Embedding               | Neighbors | |
| **LargeVis** | LargeVis                                      | Neighbors | |
| **ISOMAP**   | t Stochastic Neighbor Embedding               | Neighbors | |
| **UMAP**     | Uniform Manifold Approximation and Projection | Neighbors | |
| **AE**       | Autoencoder (2 or 3 at hidden layer)          | Neural    | |
| **VAE**      | Variational Autoencoder                       | Neural    | |
| **LSA**      | Latent Semantic Analysis                      |           | |
| **SVD**      | Singular Value decomposition                  | Linear?   | |
| **LDA**      | Linear Discriminant Analysis                  | Linear    | |
| **MDS**      | Multidimensional Scaling                      |           | |




#### Principal Component Analysis (PCA)
a statistical procedure that uses an orthogonal transformation to convert a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components. The first component is the most important one, followed by the second, then the third, and so on.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(X)
```

#### T-SNE
Read [How to use t-SNE effectively](https://distill.pub/2016/misread-tsne)

```python
from sklearn.manifold import TSNE

tsne   = TSNE(random_state=0)
x_tsne = tsne.fit_transform(x)

# And plot it:
plt.scatter(x_tsne[:, 0], x_tsne[:, 1]);
```

#### Independent Component Analysis (ICA)
a statistical technique for revealing hidden factors that underlie sets of random variables, measurements, or signals.

#### Principal Component Regression (PCR)
a technique for analyzing multiple regression data that suffer from multicollinearity. The basic idea behind PCR is to calculate the principal components and then use some of these components as predictors in a linear regression model fitted using the typical least squares procedure.

#### Partial Least Squares Regression (PLSR)
PCR creates components to explain the observed variability in the predictor variables, without considering the response variable at all. On the other hand, PLSR does take the response variable into account, and therefore often leads to models that are able to fit the response variable with fewer components.

#### Sammon Mapping
an algorithm that maps a high-dimensional space to a space of lower dimensionality by trying to preserve the structure of inter-point distances in high-dimensional space in the lower-dimension projection. sometimes we have to ask the question “what non-linear transformation is optimal for some given dataset”. While PCA simply maximizes variance, sometimes we need to maximize some other measure that represents the degree to which complex structure is preserved by the transformation. Various such measures exist, and one of these defines the so-called Sammon Mapping. It is particularly suited for use in exploratory data analysis.

#### Multidimensional Scaling (MDS)
a means of visualizing the level of similarity of individual cases of a dataset.

#### Projection Pursuit
a type of statistical technique that involves finding the most “interesting” possible projections in multidimensional data. Often, projections which deviate more from a normal distribution are considered to be more interesting.

#### Linear Discriminant Analysis (LDA)
if you need a classification algorithm you should start with logistic regression. However, LR is traditionally limited to only two class classification problems. Now, if your problem involves more than two classes you should use LDA. LDA also works as a dimensionality reduction algorithm; it reduces the number of dimension from original to C — 1 number of features where C is the number of classes.

#### Mixture Discriminant Analysis (MDA) — It is an extension of linear discriminant analysis. Its a supervised method for classification that is based on mixture models.

#### Quadratic Discriminant Analysis (QDA)
Linear Discriminant Analysis can only learn linear boundaries, while Quadratic Discriminant Analysis is capable of learning quadratic boundaries (hence it is more flexible). Unlike LDA however, in QDA there is no assumption that the covariance of each of the classes is identical.

#### Flexible Discriminant Analysis (FDA)
a classification model based on a mixture of linear regression models, which uses optimal scoring to transform the response variable so that the data are in a better form for linear separation, and multiple adaptive regression splines to generate the discriminant surface.



## Reference

- https://www.analyticsvidhya.com/blog/2018/08/dimensionality-reduction-techniques-python/
- Read [Curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality)
- [Manifold learning](https://scikit-learn.org/stable/modules/manifold.html)
- [Matrix factorization](https://scikit-learn.org/stable/modules/decomposition.html)