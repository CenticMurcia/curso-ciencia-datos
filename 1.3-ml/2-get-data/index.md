---
layout: page

parent_id: 1.3-ml
id: 2-get-data
title: Obtener datos de entrenamiento y validación
---

La selección del **conjunto de validación** es una de la cosas más importantes. Recuerda: **NUNCA USES LOS DATOS DE ENTRENAMIENTO PARA MEDIR LO BUENO QUE ES TU MODELO**.

- Train test split (Holdout)
- Cross validation (K-Fold)
  - Stratified K-Fold
  - Grouped K-Fold
  - Repeated K-Fold
- Leave One Out (LOO)
- Leave P Out (LPO)


### Train test split

Split data into x, y for training and testing

```python
from sklearn.model_selection import train_test_split
## make a train test split
x_train, x_valid, y_train, y_valid = train_test_split(x, y)
```

### Cross Validation
Check: https://scikit-learn.org/stable/modules/cross_validation.html



### Stratified Cross Validation

```python
from sklearn.model_selection import StratifiedKFold

cv = StratifiedKFold(n_splits=5)
for train_idx, test_idx, in cv.split(x, y):
    x_train, y_train = x[train_idx], y[train_idx]
    x_valid, y_valid = x[valid_idx], y[valid_idx]
    ...
```

> - [Validación en Sklearn](https://scikit-learn.org/stable/modules/cross_validation.html)
> - [Consejos para validar en una competición](http://www.chioka.in/how-to-select-your-final-models-in-a-kaggle-competitio/)


