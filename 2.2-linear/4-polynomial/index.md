---
layout: page

parent_id: 2.2-linear
id: 4-polynomial
title: Polynomial Regression

notebook: notebook.ipynb
---


```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

# creating pipeline and fitting it on data
poly_regr = Pipeline([('polynomial',PolynomialFeatures(degree=2)),
                      ('model', LinearRegression())])

pipe.fit(x, y)
```

<p align="center"><img src="https://cdn.analyticsvidhya.com/wp-content/uploads/2020/03/pr8.png" width="500px"></p>


## Regresión local (LOESS o LOWESS)

Se crean muchas regresesione lineales, donde cada una se entrena con los puntos de su región. Luego se sueviza. **Desventaja: solo vale para x con 1 varaible**.

<p align="center"><img src="img/lowess.png"></p>

```python
from statsmodels.nonparametric.smoothers_lowess import lowess

smooth = lowess(endog=y, exog=x)
index, pred = np.transpose(smooth)
```

[Video explicativo](https://www.youtube.com/watch?v=Vf7oJ6z2LCc)
