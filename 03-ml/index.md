---
layout: home

id: 03-ml
title: Machine Learning

type: topic
img_icon: 3-prepro.svg
---


<h1 align="center">Introducción al Machine Learning</h1>



## Software

<table>
  <tr>
    <th width="200"><a href="https://scikit-learn.org"><img src="../img/logos/Scikitlearn.png"/></a></th>
    <td>Scikit-learn es probablemente la librería más útil para Machine Learning en Python, es de código abierto y es reutilizable en con otras librerías. Proporciona una gran gama de algoritmos para el preprocesado de datos, aprendizaje supervisado, análisis no supervisado, y mucho más.</td>
  </tr>
</table>









<h1 align="center">Validación</h1>

La selección del **conjunto de validación** es una de la cosas más importantes. Recuerda:

<h3 align="center">NUNCA USES LOS DATOS DE ENTRENAMIENTO PARA MEDIR LO BUENO QUE ES TU MODELO</h3>

- Train test split (Holdout)
- Cross validation (K-Fold)
  - Stratified K-Fold
  - Grouped K-Fold
  - Repeated K-Fold
- Leave One Out (LOO)
- Leave P Out (LPO)

> - [Validación en Sklearn](https://scikit-learn.org/stable/modules/cross_validation.html)
> - [Consejos para validar en una competición](http://www.chioka.in/how-to-select-your-final-models-in-a-kaggle-competitio/)





## Ingeniería de características = CREATIVIDAD + CONOCIMIENTO DEL DOMINIO

La ingeniería de características (Feature Engineering) es la **generación** de nuevas características en base a las ya existentes. Esto facilita el trabajo a nuestros modelos.

- Si tienes el precio de la casa y los metros cuadrados, puedes añadir el precio del metro cuadrado.
- Si tines la distancia en el eje x e y, puedes añadir la distancia directa por pitagoras.
- Si tines precios, puedes añanir la parte fraccionaria pq es muy subjetiva en la gente.

> - [Discover Feature Engineering, How to Engineer Features and How to Get Good at It](https://machinelearningmastery.com/discover-feature-engineering-how-to-engineer-features-and-how-to-get-good-at-it/)
> - [Discussion of feature engineering on Quora](https://www.quora.com/What-are-some-best-practices-in-Feature-Engineering)


<h1 align="center">Fuga de datos</h1>

La fuga de datos conocida como **Data Leakage** en inglés, es cuando se introducen datos los cuales son imposibles de disponer en la vida real.

> - [Perfect score script](https://www.kaggle.com/olegtrott/the-perfect-score-script) used to probe leaderboard
> - [Page about data leakages on Kaggle](https://www.kaggle.com/docs/competitions#leakage)
> - [Another page about data leakages on Kaggle](https://www.kaggle.com/dansbecker/data-leakage)
