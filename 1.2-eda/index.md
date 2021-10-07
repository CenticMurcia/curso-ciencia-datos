---
layout: home

parent_id: 1-intro
id: 1.2-eda
title: Exploratory Data Analysis
description: El Análisis Exploratorio de Datos (por sus siglas EDA en inglés) se encarga de explicar y visualizar con gráficas todo lo posible acerca de los datos. Es casi obligatoria realizar este EDA en cualquier proyecto de análisis de datos. En este capítulo veremos cuáles son las técnicas y herramientas más comunes para realizar nuestras visualizacionbes en Python.

img_icon: 2-eda.svg
img_title: 2-EDA.png
---

<p align="center"><img src="{{site.baseurl}}/img/miniaturas YT/{{page.img_title}}" width="500px"></p>


{{page.description}}


## Librerías

<table>
  <tr>
    <th><a href="https://matplotlib.org/gallery"><img src="../img/logos/Matplotlib.svg"/></a></th>
    <td>Matplotlib es un paquete para la generación de gráficos. Es la librería más usada, pero necesita muchas líneas de código para generar gráficos más complejos</td>
  </tr>
  <tr>
    <th width="200"><a href="https://seaborn.pydata.org/examples"><img src="../img/logos/Seaborn.svg"/></a></th>
    <td>Seaborn es un paquete para Python que permite generar fácilmente elegantes gráficos estadísticos. Seaborn está basada en Matplotlib y proporciona una interfaz de alto nivel que es realmente sencilla de aprender.</td>
  </tr>
  <tr>
    <th ><a href="https://altair-viz.github.io/gallery"><img height="100" src="../img/logos/Altair.png"/></a></th>
    <td>Altair es un paquete de Python para la visualización de datos basado en Vega y Vega-Lite, que a su vez están basados en D3. Altair utiliza lo que se conoce como “grammar of graphics”, donde se pone énfasis es en describir la apariencia visual y el comportamiento interactivo de la visualización.</td>
  </tr>
  <tr>
    <th><a href="https://plot.ly/python"><img src="../img/logos/Plotly.png"/></a></th>
    <td>Plotly es una librería para gráficos interactivos. Es particularmente útil para cuando queremos hacer gráficos en 3 dimensiones. Plotly está disponible como una biblioteca para Python, R, JavaScript, Julia y MATLAB.</td>
  </tr>
  <tr>
    <th><a href="https://github.com/pandas-profiling/pandas-profiling"><img src="../img/logos/Pandasprofiling.png"/></a></th>
    <td>Una librería que nos permite realizar un EDA completo de nuestro dataframe con tan solo un par de lineas de código.</td>
  </tr>
    <tr>
    <th><a href="https://github.com/fbdesignpro/sweetviz"><img src="../img/logos/Sweetviz.png"/></a></th>
    <td>Otra librería al igual que Pandas Profiling que nos permite realizar un EDA con pocas líneas.</td>
  </tr>
</table>

Otros
- Bokeh
- [ggplot](http://ggplot.yhathq.com/) for Python
- Graph visualization with [NetworkX](https://networkx.org)

<h1 align="center">📊 Gráficas</h1>
<h4 align="center">Ver <a href="https://python-graph-gallery.com">Python Graph Gallery</a> y <a href="https://www.data-to-viz.com">From Data to Viz</a></h4>





## Distribution


<table>
<tr>
  <td> <a href="https://python-graph-gallery.com/histogram">    <img src="img/icons150/yellow-histogram.png" width="100px"/> </a> </td>
  <td> <a href="https://python-graph-gallery.com/density-plot"> <img src="img/icons150/yellow-density.png"   width="100px"/> </a> </td>
  <td> <a href="https://python-graph-gallery.com/boxplot">      <img src="img/icons150/yellow-box.png"       width="100px"/> </a> </td>
  <td> <a href="https://python-graph-gallery.com/violin-plot">  <img src="img/icons150/yellow-violin.png"    width="100px"/> </a> </td>
</tr>
<tr>
  <th>Histogram</th>
  <th>Density plot</th>
  <th>Box plot</th>
  <th>Violin plot</th>
</tr>
<tr>
  <td>df.plot.hist()<br>sns.distplot()</td>
  <td>df.plot.kde()<br>sns.kdeplot()</td>
  <td>df.plot.box()<br>sns.boxplot()</td>
  <td>sns.violinplot()</td>
</tr>
</table>


## Correlation

<table>
<tr>
  <td width="16%"> <img src="img/icons150/grey-scatter.png"/>     </td>
  <td width="16%"> <img src="img/icons150/grey-heatmap.png"/>     </td>
  <td width="16%"> <img src="img/icons150/grey-correlogram.png"/> </td>
  <td width="16%"> <img src="img/icons150/grey-bubble.png"/>      </td>
  <td width="16%"> <img src="img/icons150/grey-connected.png"/>   </td>
  <td width="16%"> <img src="img/icons150/grey-density.png"/>     </td>
</tr>
<tr>
  <th>Scatterplot</th>
  <th>Heatmap</th>
  <th>Correlogram</th>
  <th>Bubble</th>
  <th>Connected Scatter</th>
  <th>2D Density</th>
</tr>
<tr>
  <td>plt.scatter()<br>sns.scatterplot()</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
</tr>
</table>


### Ranking
<table>
  <tr>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/BarBig-150x150.png"      width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/LollipopBig-150x150.png" width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/Parallel1Big-150x150.png"       width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/SpiderBig-150x150.png"          width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/WordcloudBig-150x150.png"        width="100px"/></td>
  </tr>
  <tr>
    <th>Bar plot</th>
    <th>Lollipop plot</th>
    <th>Parallel coords.</th>
    <th>Radar chart</th>
    <th>Word cloud</th>
  </tr>
    <tr>
    <td>plt.scatter()<br>sns.scatterplot()</td>
    <td></td>
    <td>parallel_coordinates(df, 'cls')</td>
    <td></td>
    <td></td>
  </tr>
</table>

### Grupos
<table>
  <tr>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/StackedBig-150x150.png"    width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/PieBig-150x150.png"        width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/DoughnutBig-150x150.png"   width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/DendrogramBig-150x150.png" width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/TreeBig-150x150.png"       width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/VennBig-150x150.png"       width="100px"/></td>
  </tr>
  <tr>
    <th>Stacked bar plot</th>
    <th>Pie chart</th>
    <th>Donut chart</th>
    <th>Dendrogram</th>
    <th>Treemap</th>
    <th>Venn diagram</th>
  </tr>
</table>




## EDA no supervisado

> - [Unsupervised Learning in Sklearn](https://scikit-learn.org/stable/unsupervised_learning.html)
> - Matrix Factorization:
>   - [Overview of Matrix Decomposition methods in Sklearn (PCA, etc)](https://scikit-learn.org/stable/modules/decomposition.html)
> - t-SNE:
>   - [Comparison of Manifold Learning methods (sklearn)](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html) (sklearn example)
>   - [tSNE with different perplexities](https://scikit-learn.org/stable/auto_examples/manifold/plot_t_sne_perplexity.html) (sklearn example)
>   - [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne): distill.pub blog
>   - [tSNE homepage](https://lvdmaaten.github.io/tsne/) (Laurens van der Maaten)
>   - [Multicore t-SNE implementation](https://github.com/DmitryUlyanov/Multicore-TSNE)
> - Interactions:
>   - [Facebook Research's paper about extracting categorical features from trees](https://research.fb.com/publications/practical-lessons-from-predicting-clicks-on-ads-at-facebook)
>   - [Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html) (sklearn example) Creo que es parecido a M5





> ## Referencias
> - [**Kaggle learn: data visualization**](https://www.kaggle.com/learn/data-visualization)
