---
layout: home

parent_id: 2-models
id: 2.1-tree
title: Tree-based models

img_icon: 4-tree.svg
---


<p align="center"><img src="../img/miniaturas YT/4-Árbol.png" height="200px"></p>

> TODO:
> - https://medium.com/ai-in-plain-english/hyperparameter-tuning-of-decision-tree-classifier-using-gridsearchcv-2a6ebcaffeda
> - Puesta en producción

## Software


<table>
  <tr>
    <th width="200"><a href="https://scikit-learn.org"><img src="../img/logos/Scikitlearn.png"/></a></th>
    <td>Sklearn proprocina muchos modelos de árbol como DecisionTree, RandomForest, ExtraTrees, AdaBoost y GradientBoosting. Lo malo de esta librería es que todos lo modelos corren sobre CPU y no GPU</td>
  </tr>
  <tr>
    <th width="200"><h1><a href="https://github.com/parrt/dtreeviz">dtreeviz</a></h1></th>
    <td>dtreeviz es una librería para dibujar árboles de decisión. Actualmente tiene soporte para scikit-learn y XGBoost.</td>
  </tr>
  <tr>
    <th width="200"><a href="https://github.com/rapidsai/cuml"><img src="../img/logos/Rapids.png"/></a></th>
    <td>La librería CuML de RAPIDS ofrece una implentación de RandomForest haciendo uso de la GPU para construir varios árboles en paralelo.</td>
  </tr>
  <tr>
    <th><a href="https://xgboost.readthedocs.io"><img src="../img/logos/XGBoost.png"/></a></th>
    <td>XGBoost significa eXtreme Gradient Boosting, y es una implementación de Gradient boosting diseñada para minimizar la velocidad de ejecución y maximizar el rendimiento. Es uno de los algoritmos que más domina recientemente en los problemas Machine Learning y las competiciones de Kaggle con datos estructurados o tabulares.</td>
  </tr>
  <tr>
    <th><a href="https://lightgbm.readthedocs.io"><img src="../img/logos/LightGBM.svg"/></a></th>
    <td>LightGBM es la implementación de Gradient boosting de Microsoft. Suele ofrecer buenos resultados en precisión y sobre todo en rendimiento (entrena más rapido que XGBoost).</td>
  </tr>
  <tr>
    <th><a href="https://catboost.ai"><img src="../img/logos/CatBoost.png"/></a></th>
    <td>CatBoost es una implementación de Gradient boosting desarrollada por Yandex especializada para trabajar con datasets con variables categóricas. Ofrece excelentes resultados gracias a sus métodos de codificación de categorías.</td>
  </tr>
</table>


## Modelos basados en Árboles

|          | Model                     | Import                                                                             |
|:--------:|---------------------------|------------------------------------------------------------------------------------|
| **DT**   | Decision Tree             | from sklearn.tree     import DecisionTreeClassifier,     DecisionTreeRegressor     |
| **RF**   | Random Forest             | from sklearn.ensemble import RandomForestClassifier,     RandomForestRegressor     |
| **RF**   | Random Forest (RAPIDS)    | from cuml.ensemble    import RandomForestClassifier,     RandomForestRegressor     |
| **ET**   | Extra (Randomized) Trees  | from sklearn.ensemble import ExtraTreesClassifier,       ExtraTreesRegressor       |
| **AB**   | AdaBoost                  | from sklearn.ensemble import AdaBoostClassifier,         AdaBoostRegressor         |
| **GB**   | Gradient Boosting         | from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor |
| **XGB**  | XGBoost                   | from xgboost          import XGBClassifier,              XGBRegressor              |
| **LGBM** | LightGBM                  | from lightgbm         import LGBMClassifier,             LGBMRegressor             |
| **CB**   | CatBoost                  | from catboost         import CatBoostClassifier,         CatBoostRegressor         |
| **NGB**  | NGBoost                   | from ngboost          import NGBClassifier,              NGBRegressor              |
| **RGF**  | Regularized Greedy Forest | from rgf.sklearn      import RGFClassifier,              RGFRegressor              |
|          |                           | from rgf.sklearn      import FastRGFClassifier,          FastRGFRegressor          |

---



# [Microsoft Hummingbird](https://github.com/microsoft/hummingbird)

**Converts Tree models into Neural Nets**.
```python
from sklearn.ensemble import RandomForestClassifier
from hummingbird.ml import convert

# Create and train a model (scikit-learn RandomForestClassifier in this case)
tree_model = RandomForestClassifier(n_estimators=10, max_depth=10)
tree_model.fit(x, y)

# Use Hummingbird to convert the model to PyTorch
nn_model = convert(tree_model, 'pytorch')

# Run predictions on CPU
nn_model.predict(X)

# Run predictions on GPU
nn_model.to('cuda')
nn_model.predict(X)
```
