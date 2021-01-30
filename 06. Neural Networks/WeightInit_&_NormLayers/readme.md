<h1 align="center">Weight initialization & Normalization layers</h1>


## Introduction

Is very important that each layer output has
- **Mean = 0** (or at least stay the same across every layer)
- **Std = 1** (or at least stay the same across every layer)

```python
# Comprobación de que nuestro modelo está bien inicializado
input = torch.randn(DIMENS)
output = model(input)
output.mean(), output.std()
```

The **problem**: If we dont have that, we have problems:

- A too-small initialization leads to **vanishing gradients**
- A too-large initialization leads to **exploding gradients**

**Solution** to this problem are the following:

- Good weight initialization.
- Add Normalization layers.


## Weight initialization

- [Jeremy howard explaining inits video](https://www.youtube.com/watch?v=AcA8HAYh7IE)
- https://madaan.github.io/init/

| Layer                        | Best init for weight.data               | bias.data | Notes |
|------------------------------|-----------------------------------------|-----------|-------|
| Linear(IN,OUT)               | normal(mean=0, std=sqrt(1/IN))          | fill(0)   |       |
| Linear(IN,OUT) -> Sigmoid    | normal(mean=0, std=sqrt(1/IN))          | fill(0)   |       |
| Linear(IN,OUT) -> tanh       | normal(mean=0, std=sqrt(1/IN))          | fill(0)   | Xavier Glorot |
| Linear(IN,OUT) -> ReLU       | normal(mean=0, std=sqrt(2/IN))          | fill(0)   | Kaiming He. Replace Relu(x) by: `x.clamp_min(0) - 0.5` to get mean=0 |
| Linear(IN,OUT) -> Swish      | ?                                       | ?         |       |
| Embedding(VOCAB,EMB)         | normal(mean=0, std=sqrt(1/EMB           |           |       |
| Conv(IN_CH,OUT_CH,K) -> ReLU | normal(mean=0, std=sqrt(2/(IN_CH·K·K))) | fill(0)   |       |
| Residual custom model        | Fixup                                   |           |       |
| Transformer model            | T-Fixup                                 |           |       |


> Note:
> torch.randn(IN,OUT) / math.sqrt(IN) == torch.randn(IN,OUT) * math.sqrt(1/IN)
> nn.init.kaiming_normal_(w, mode='fan_in',  nonlinearity='relu') == torch.randn(IN,OUT) * math.sqrt(2/IN)


| Initialization         | Paper                                    | Notes |
|------------------------|------------------------------------------|-------|
| Xavier (aka Glorot)    | [2010](http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf) |
| Exact solutions to ... | [2013](https://arxiv.org/abs/1312.6120)  |       |
| Kaiming (aka He)       | [2015](https://arxiv.org/abs/1502.01852) |       |
| LSUV                   | [2015](https://arxiv.org/abs/1511.06422) | Indiferente del tipo de capa. Proceso iterativo. |
| SELU                   | [2017](https://arxiv.org/abs/1706.02515) | NO USAR |
| Delta-Orthogonal       | [2018](https://arxiv.org/abs/1806.05393) | Good for CNNs |
| Fixup                  | [2019](https://arxiv.org/abs/1901.09321) | Indiferente del tipo de capa |
| T-Fixup                | [2020](http://www.cs.toronto.edu/~mvolkovs/ICML2020_tfixup.pdf) | Good for Transformer |
| DeepMind paper         | [2021](https://arxiv.org/abs/2101.08692) | Andres Torrubia recomeadation for CNNs. [TWIT](https://twitter.com/ajmooch/status/1352614051352899585) |


> ### Layer-sequential unit-variance (LSUV)
>
> We initialize our neural net with the usual technique, then we pass a batch through the model and check the outputs of the linear and convolutional layers. We can normalize the activations by:
> - rescale the weights according to the actual variance we observe on the activations,
> - and subtract the mean we observe from the initial bias.
>
> We repeat this process until we are satisfied with the mean/variance we observe.
>
> Psudocode:
>
> ```python
> for layer in layers:
>
>    while abs(layer.mean)  > 1e-3: m.bias -= h.mean
>    while abs(layer.std-1) > 1e-3: m.weight.data /= h.std
> ```
> Reference: [Fastai notebook](https://github.com/fastai/course-v3/blob/master/nbs/dl2/07a_lsuv.ipynb)


### Fixed-update initialization (Fixup)



## Normalization layers

