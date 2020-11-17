

<h1 align="center">Recommendation<br>Systems</h1>

### Collaborative Filtering

Se basa en la idea de que con unas pocas interacciones de USER + ITEM (por ejemplo un espectador que califica una pelicula). Poder predecir el resto de pares USER + ITEM (caunto le gustará esta pelicula a este espectador).


<p align="center"><img width="100%" src="img/matrix1.png" /></p>

Los datos que se disponen incialmente son unos pocos ejemplos. A este tipo de información se le denomina **matriz dispersa** (sparse matrix).

<p align="center"><img width="60%" src="img/matrix2.png" /></p>

La idea es para cada usuario e item crear su vector semantico que lo identifique.

<p align="center"><img width="100%" src="img/matrix3.png" /></p>


### Cómo se entrena?

Se crea una red neuronal con los 2 embeddings de entrada (user e item). Y se entrena con los datos (no ceros) que disponemos en la matriz dispersa.


<p align="center"><img width="75%" src="img/nn.png" /></p>


### Referencias
- https://github.com/fastai/fastbook/blob/master/08_collab.ipynb
- https://keras.io/examples/structured_data/collaborative_filtering_movielens/
- https://nipunbatra.github.io/blog/ml/2017/12/29/neural-collaborative-filtering.html