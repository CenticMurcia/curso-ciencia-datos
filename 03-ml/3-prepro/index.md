---
layout: page

id: 3-prepro
title: Preprocesar datos

topic: Machine Learning
---



<h1 align="center">Preprocesamiento</h1>

<table>
  <tr>
    <tD></tD>
    <tD>
      <h3>Modelos basados en árbol</h3>
      <ul>
        <li>Decission Tree</li>
        <li>Random Forest</li>
        <li>Extra Trees</li>
        <li>Adaboost</li>
        <li>Gradient Boosting</li>
        <li>XGBoost</li>
        <li>LightGBM</li>
        <li>CatBoost</li>
      </ul>
    </tD>
    <td>
      <h3>Modelos "mutiplicativos"</h3>
      <ul>
        <li>Linear Models (LM)</li>
        <li>Generalized Additive Model (GAM)</li>
        <li>Neural Networks (NN)</li>
        <li>K-Nearest Neighbors (KNN)</li>
        <li>Suport Vector Machines (SVM)</li>
        <li>Naive Bayes (NB)</li>
        <li>Dimensionality Reduction models
          <ul>
            <li>PCA</li>
            <li>t-SNE</li>
            <li>UMAP</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <th>Variable<br>Categórica<br>Ordinal</th>
    <td>
      <ul>
        <li><b><a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html">Ordinal encoding</a></b></li>
        <li>Other: Frequency encoding</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b><a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html">One Hot encoding</a></b></li>
        <li>Other: Embedding</li>
      </ul>
    </td>
  </tr>
  <tr>
    <th>Variable<br>Numérica</th>
    <td align=Center><b>Nada</b></td>
    <td>
      <ul>
        <li><b><a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandarScaler.html">StandarScaler</a></b> (Normalizar)</li>
        <li>MinMaxScaler</li>
        <li>Si no sigue una distribución norma (Skewed):
          <ul>
            <li>np.log(1+x)</li>
            <li>np.sqrt(x+2/3)</li>
            <li>Box-Cox</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
  <tr>
    <th>Texto</th>
    <td colspan="2" align=Center>
        <b><a href="https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html">CountVectorizer</a></b>,
        <b><a href="https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html">TfidfVectorizer</a></b>,
        <b><a href="https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html">HashingVectorizer</a></b>,
        Word embeddings
    </td>
  </tr>
</table>

```python
from sklearn import preprocessing, compose

x_preprocessing_tree = compose.ColumnTransformer(transformers=[
    ('cat', preprocessing.OrdinalEncoder(),  cat_vars),
], remainder='passthrough')

x_preprocessing_mult = compose.ColumnTransformer(transformers=[
    ('cat', preprocessing.OneHotEncoder(),  cat_vars),
    ('num', preprocessing.StandardScaler(), num_vars),
], remainder='drop') 
```

## Variables numéricas
TO-DO: Scaling and Normalization
> - [Feature Scaling and the effect of standardization for machine learning algorithms](https://sebastianraschka.com/Articles/2014_about_feature_scaling.html)

### RankGauss (aka QuantileTransformer)

Its based on rank transformation.

1. Assign a linspace to the sorted features from 0..1,
2. Apply the inverse of error function ErfInv to shape them like gaussians,
3. Substract the mean.

This works usually much better than standard mean/std scaler or min/max.

`RankGauss = QuantileTransformer(n_quantiles=100, random_state=0, output_distribution="normal")`

### Variance Threshold

- VarianceThreshold is a method of feature selection.
- It removes all features whose variance doesn’t meet some threshold. 

### [Map data to a normal distribution](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_map_data_to_normal.html): Box-Cox
A Box Cox transformation is a generic way to transform non-normal variables into a **normal shape**.

| Lambda value (λ) | Transformed data |
|------------------|------------------|
| -3               | Y⁻³ = 1/Y³       |
| -2               | Y⁻² = 1/Y²       |
| -1               | Y⁻¹ = 1/Y¹       |
| -0.5             | Y⁻⁰·⁵ = 1/√Y      |
| 0                | log(Y)           |
| 0.5              | Y⁰·⁵ = √Y         |
| 1                | Y¹               |
| 2                | Y²               |
| 3                | Y³               |


## Categorical features

| Ordinal Encoding o Label Encoding    | One-Hot Encoding        |
|--------------------------------------|-------------------------|
| ![](img/enc-ord.png)                 | ![](img/enc-onehot.png) |

> ## Target Encoding o Mean Encoding
> ![](img/enc-target.png)




## Ingeniería de características = CREATIVIDAD + CONOCIMIENTO DEL DOMINIO

La ingeniería de características (Feature Engineering) es la **generación** de nuevas características en base a las ya existentes. Esto facilita el trabajo a nuestros modelos.

- Si tienes el precio de la casa y los metros cuadrados, puedes añadir el precio del metro cuadrado.
- Si tines la distancia en el eje x e y, puedes añadir la distancia directa por pitagoras.
- Si tines precios, puedes añanir la parte fraccionaria pq es muy subjetiva en la gente.

> - [Discover Feature Engineering, How to Engineer Features and How to Get Good at It](https://machinelearningmastery.com/discover-feature-engineering-how-to-engineer-features-and-how-to-get-good-at-it/)
> - [Discussion of feature engineering on Quora](https://www.quora.com/What-are-some-best-practices-in-Feature-Engineering)

