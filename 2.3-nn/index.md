---
layout: home

parent_id: 2-models
id: 2.3-nn
title: Neural Networks

img_icon: 6-nn.svg
---


## Software

<table>
  <tr>
    <th ><a href="https://www.tensorflow.org"><img src="../img/logos/TensorFlow.svg"/></a></th>
    <td>TensorFlow es la librería de código abierto para el aprendizaje profundo desarrollada por Google.</td>
  </tr>
  <tr>
    <th ><a href="https://keras.io"><img src="../img/logos/Keras.png"/></a></th>
    <td>Keras es una librería popular de redes neuronales basada en TensorFlow. Está especialmente diseñada para facilitar la creación de redes neuronales. Actualmente forma parte de la librería TensorFlow.</td>
  </tr>
  <tr>
    <th><a href="https://pytorch.org/"><img src="../img/logos/Pytorch.png"/></a></th>
    <td>Es una librería de Deep Learning diseñada por Facebook. Muchos la consideran superior a Tensorflow por su flexibilidad y facilidad. Además permite su ejecución en GPU (y varias GPUs) para acelerar los cálculos. Es la libreria más usada entre investigadores para probar sus experimentos.</td>
  </tr>
  <tr>
    <th width="200"><a href="https://www.fast.ai"><img src="../img/logos/Fastai.png"/></a></th>
    <td>Fast.ai es una librería ¡y un curso! dirigido por Jeremy Howard donde se pretende hacer el Deep Learning accesible a todo el mundo. Su librería, basada en Pytorch, tiene como máxima la simplicidad y facilitar el uso de los modelos más avanzados de redes neuronales.</td>
  </tr>
</table>



## Problems

| Problem                           | Description             | Output layer          | Loss                          | 
|:---------------------------------:|:-----------------------:|:---------------------:|:-----------------------------:|
| **Regression**                    | Real number (-∞, ∞)     | 1 neuron without act  | Mean Squared Error<br>(MSE)   |
| **Binary<br>Classification**      | 2 exclusive classes     | 1 neuron + Sigmoid    | Binary Cross Entropy<br>(BCE) |
| **Multi-Class<br>Classification** | N exclusive classes     | N neurons + Softmax   | Cross-Entropy<br>(CE)         |
| **Multi-Label<br>Classification** | N non-exclusive classes | N neurons + Sigmoid   | Binary Cross Entropy<br>(BCE) |

> - You can just consider the multi-label classifier as a combination of multiple independent binary classifiers.
> - Cross-Entropy is called Categorical CrossEntropy in Keras.


## Backpropagation
![](img/update-weights.png)
<br>


## References
- [Ejemplos oficiales de Keras](https://keras.io/examples)
