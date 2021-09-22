---
layout: home

id: 04-dl
title: Deep Learning

type: topic
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


## Hiperparámetros comunes

|                       | Impact | Notes                                          |
|-----------------------|--------|------------------------------------------------|
| Layer size            | High   |                                                |
| Num of layers (depth) | Medium |                                                |
| Weight Initialization | Medium | Xavier (Dense+tanh), Kaiming He (Dense+ReLU)   |
| Transfer Learning     | High   | Pretrained model frozen, new layers unfrozen   |
| Nonlinearity (act fn) | Low    | ReLU, GELU, Swish, Mish, GLU                   |
| Residual connections  | Low    | Needed if there are a lot of layers (>3)       |
| - Stochastic Depth    | Low    | If there are residual cons, add this.          |
| Input data            | High   | Input data representation is very important    |
| - Normalization       |        | StandardScaler, QuantileTransformer, RankGauss |
| - Embeddings          |        | Necessary for categorical data                 |
| - Image size          |        | We need high or low resolution?                |
| - CoordConv           |        | Encode sequence order for CNNs or tranformers  |
| - Positional Encoding |        | Encode sequence order for CNNs or tranformers  |
| Output data           | High   | Logits (-∞, ∞), sigmoid (0,1), softmax,...     |
| - Good for the loss   |        | Is good for the loss fn?                       |
| Regularization        | Medium |                                                |
| - Dropout             | Medium | Scale after dropout to maintain std=1          |
| - Dropconect          | Low    |                                                |
| Inner normalization   |        |                                                |
| - Batch normalization |        |                                                |
| - Layer normalization |        | Usually before each layer                      |
| Weght tiying          |        | If same input & output: Langmodel, Autoencoder |


> - [Stochastic Depth](https://arxiv.org/abs/1603.09382)
> - [Squeeze and Excitation](https://amaarora.github.io/2020/07/24/SeNet.html)


# Problems

| Problem                    | Description             | Output layer          | Loss                       | 
|----------------------------|-------------------------|-----------------------|----------------------------|
| Regression                 | Real number             | 1 neuron without act  | Mean Squared Error (MSE)   |
| Binary Classification      | 2 exclusive classes     | 1 neuron + Sigmoid    | Binary Cross Entropy (BCE) |
| Multi-Class Classification | N exclusive classes     | N neurons + Softmax   | Cross-Entropy (CE)         |
| Multi-Label Classification | N non-exclusive classes | N neurons + Sigmoid   | Binary Cross Entropy (BCE) |

You can just consider the multi-label classifier as a combination of multiple independent binary classifiers


Regression losses

| Loss                                  | Pytorch               | Tensorflow            | Keras
|---------------------------------------|-----------------------|-----------------------|--------------
| Mean Absolute Error (MAE)             | torch.nn.L1Loss       | tf.keras.losses.MAE   | "mean_absolute_error"
| Mean Squared Error (MSE)              | torch.nn.MSELoss      | tf.keras.losses.MSE   |
| Mean Absolute Percentage Error (MAPE) |                       | tf.keras.losses.MAPE  | "mean_absolute_percentage_error"
| Mean Squared Logarithmic Error (MSLE) |                       | tf.keras.losses.MSLE  |
| Huber loss                            | torch.nn.SmoothL1Loss | tf.keras.losses.Huber |


Classification losses

| Loss                          | Pytorch                 | Tensorflow            | Keras
|-------------------------------|-------------------------|-----------------------|--------------
| Binary Cross Entropy (y: 0,1) | nn.BCELoss()            | tf.keras.losses.BinaryCrossentropy              "binary_crossentropy"
| Cross Entropy (y: one hot)    | nn.CrossEntropyLoss()   | tf.keras.losses.CategoricalCrossentropy         "categorical_crossentropy" 
| Cross Entropy (y: integer)    |                         | tf.keras.losses.SparseCategoricalCrossentropy   "sparse_categorical_crossentropy" 
| Hinge                         | nn.HingeEmbeddingLoss() | tf.keras.losses.Hinge                           "hinge"
| Squared Hinge                                           | tf.keras.losses.SquaredHinge                    "squared_hinge"
| Focal loss                      -                       | tfa.losses.SigmoidFocalCrossEntropy



# Advice for Tabular data


### Neural Network

Take the longest time to train, and require extra preprocessing such as normalisation; this normalisation needs to be used at inference time as well. They can provide great results, and extrapolate well, but only if you are careful with your hyperparameters, and are careful to avoid overfitting.

<p align="center"><img width="80%" src="img/tabular2.png" /></p>

### Conclusion

We suggest starting your analysis with a random forest. This will give you a strong baseline, and you can be confident that it's a reasonable starting point. You can then use that model for feature selection and partial dependence analysis, to get a better understanding of your data.

From that foundation, you can try Gradient Boosting and Neural Nets, and if they give you significantly better results on your validation set in a reasonable amount of time, you can use them.


## Backpropagation
![](img/update-weights.png)
<br>

## Learning Rate
![](img/lr.png)
<br>

## Early stopping
![](img/early-stopping.png)
<br>

![](img/overffiting.jpg)
<br>


## EXTRA: Learning Rate Finder
![](img/lr-finder.png)
<br>

### Aprende más
- [Ejemplos oficiales de Keras](https://keras.io/examples)
