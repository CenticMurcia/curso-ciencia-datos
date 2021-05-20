
<p align="center"><img src="../img/miniaturas YT/2-EDA.png" height="200px"></p>



El Análisis Exploratorio de Datos (por sus siglas EDA en inglés) es una parte fundamental de cualquier proyecto de análisis de datos. En este capítulo veremos cuáles son las técnicas y herramientas más comunes para realizar nuestras visualizacionbes en Python.


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


<h1 align="center">Análisis Univariante</h1>

## Variable numérica: Distribución

<table>
<tr>
    <td><a href="https://python-graph-gallery.com/histogram">
        <img src="https://python-graph-gallery.com/wp-content/uploads/HistogramBig-150x150.png" width="100px"/></td>
    <td><a href="https://python-graph-gallery.com/density-plot">
        <img src="https://python-graph-gallery.com/wp-content/uploads/DensityBig-150x150.png"   width="100px"/></td>
    <td><a href="https://python-graph-gallery.com/boxplot">
        <img src="https://python-graph-gallery.com/wp-content/uploads/Box1Big-150x150.png"      width="100px"/></td>
    <td><a href="https://python-graph-gallery.com/violin-plot">
        <img src="https://python-graph-gallery.com/wp-content/uploads/ViolinBig-150x150.png"    width="100px"/></td>
    <td><img src="https://www.data-to-viz.com/img/section/Joyplot150.png"        width="100px"/></td>
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

> ### Probplots
> Una forma más avanzada de ver si la distribucion sigue una distribución normal, son los probability plots (o simplemente probplots). Existen 2 tipos
> - QQ plot: "Quantile-Quantile" plot
> - PP plot:
>
> ![](img/probplot.png)
>
> ```python
> import scipy.stats as stats
> stats.probplot(x=df.variable, dist=stats.norm(), plot=plt)
> ```
> Ejercicio: Coger una varible con distribucion no normal, palicarle el **log** y el **boxcox** para ver cual ajusta mejor a una distr normal.

> ### Skewness `.skew()`
> Otra forma de ver si la variable no sigue una distribucion normal es ver su Skewness.
>
> ```python
> skewed_feats = df[num_feats].apply(lambda x: x.dropna().skew()).sort_values(ascending=False)
> ```

## Variable Numérica: Evolución
<table>
  <tr>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/LineBig-150x150.png"        width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/AreaBig-150x150.png"        width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/StackedAreaBig-150x150.png" width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/StreamBig-150x150.png"      width="100px"/></td>
  </tr>
  <tr>
    <th>Line chart</th>
    <th>Area chart</th>
    <th>Stacked area chart</th>
    <th>Stream graph</th>
  </tr>
</table>

El grafico de index vs value, es decir, el numero de la fila contra el valor de la variable es especialmente util para:
- Ver la evolucion de una variable, si hay alg'un patron temporal
- Ver si el dataset fue mezlado o no (shuffled)

<table>
  <tr>
    <td><img src="img/index1.png"/></td>
    <td><img src="img/index2.png"/></td>
    <td><img src="img/index3.png"/></td>
  </tr>
  <tr>
    <td>plt.plot(x,".")</td>
    <td>plt.scatter(range(len(x)), x, c=y)</td>
  </tr>
</table>






<h1 align="center">Análisis Bivariante</h1>


## Variable numérica + variable numérica
<table>
  <tr>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/ScatterPlotBig-150x150.png"      width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/ScatterConnectedBig-150x150.png" width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/BubblePlotBig-150x150.png"       width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/HeatmapBig-150x150.png"          width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/2dDensityBig-150x150.png"        width="100px"/></td>
    <td><img src="https://python-graph-gallery.com/wp-content/uploads/CorrelogramBig-150x150.png"      width="100px"/></td>
  </tr>
  <tr>
    <th>Scatter plot</th>
    <th>Line plot</th>
    <th>Bubble plot</th>
    <th>Heatmap</th>
    <th>Density plot 2D</th>
    <th>Correlogram</th>
  </tr>
  <tr>
    <td>df.plot.scatter()<br>plt.scatter()<br>sns.scatterplot()</td>
    <td></td>
    <td></td>
    <td>plt.matshow(np)<br>plt.imshow(np)<br>sns.heatmap(df)</td>
    <td>df.plot.hexbin()</td>
    <td>scatter_matrix(df)<br>sns.pairplot()</td>
  </tr>
</table>

<h1 align="center">Análisis Multivariante</h1>


## Matriz de correlación

**Correlación**: cuánto se paracen las variables entre sí. Es decir, calcular **distancias entre N variables** y guardarlas en una matriz de tamaño NxN. Existen distintas formas de calcularla:

| Entre variables                                 | Método                               | Rango   |
|-------------------------------------------------|--------------------------------------|---------|
| **numérica**   vs **numérica**                  |  Pearson, Spearman, Kendall          | [-1, 1] |
| **categórica** vs **categórica** (simétrica)    |  Cramér's V (Cramér's phi)           | [0, 1]  |
| **categórica** vs **categórica** (no simétrica) |  Theil’s U (Uncertainty coefficient) | [0, 1]  |
| **categórica** vs **numérica**                  |  Correlation ratio                   | [0, 1]  |

> [The Search for Categorical Correlation](https://towardsdatascience.com/the-search-for-categorical-correlation-a1cf7f1888c9)

La funcion `df.corr()` de `pandas` sólo calcula la correlacion entre las variables numéricas:
- Standard correlation coefficient: `df.corr()` o `df.corr(method='pearson')`
- Spearman rank correlation: `df.corr(method='spearman')`
- Kendall Tau correlation coefficient: `df.corr(method='kendall')`
  
La funcion `associations(df)` del paquete `dython` calcula todas las correlaciones de la siguiente manera:
- **Pearson** para los pares continuous-continuous.
- **Correlation Ratio** para los pares categorical-continuous.
- **Cramer's V** o **Theil's U** para los pares categorical-categorical.

```python
from dython.nominal import associations

associations(df, theil_u=True, figsize=(15, 15), mark_columns=True);
```

Otra forma de calcualar la corrlacion de variables categ'oricas como numérricas es convertiral a OneHot con `df_oh = pd.get_dummies(df)`

- A parte de la correlación, se pueden calcular otras matrices:
  - Cuántas veces una variable es más grande que otra. `fn = mean(feat1 > feat2)`
  - Cuántas combinaciones distintas tienen 2 variables.

Una vez calculada la matriz de correlación se puede **ordenar por grupos** gracias al clustering. Seaborn lo hace por nosostros con `clustermap`.

| Matriz de correlación    | Matriz de correlación ordenada por grupos |
|--------------------------|-------------------------------------------|
| ![](img/corr.png)        | ![](img/corr_sorted.png)                  |
| `sb.heatmap(df.corr())`  | `clustermap(df.corr())`                   |


## Plot de una agragación

| Media de cada variable      | Media de cada variable (ordenada)         |
|-----------------------------|-------------------------------------------|
| ![](img/agg.png)            | ![](img/agg_sorted.png)                   |
| `df.mean().plot(style=".")` | `df.mean().sort_values().plot(style=".")` |


## Reducción dimensional





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


# ❓ Missing values

- Missings de cada **celda** `df.isnull()`
  - Plot `sb.heatmap(df.isnull())`
- Missings de cada **variable** `df.isnull().sum(axis=0)` o `df.isnull().sum()`
  - Ordenados: `df.isnull().sum().sort_values(ascending=False)`
  - En porcentaje: `df.isnull().sum() / len(df) * 100`
- Missings de cada **fila** `df.isnull().sum(axis=1)`

### Paquete [missingno](https://github.com/ResidentMario/missingno)
```python
import missingno
```

<table>
<tr>
  <td><img src="https://camo.githubusercontent.com/d59ba9e511fd42dd078b8c8829d3de3f6a7e1585/68747470733a2f2f692e696d6775722e636f6d2f675775584b45722e706e67"/></td>
  <td><img src="https://camo.githubusercontent.com/ce48f2e7236c83739baaf4885a93deb115970512/68747470733a2f2f692e696d6775722e636f6d2f32427845664f722e706e67"/></td>
</tr>
  <tr>
    <th>missingno.matrix(df)</th>
    <th>missingno.bar(df)</th>
  </tr>
</table>

<table>
<tr>
  <td><img src="https://camo.githubusercontent.com/196fbc6986234a1d6289ee2bcd7e72c82531433e/68747470733a2f2f692e696d6775722e636f6d2f4a616c534b79452e706e67"/></td>
  <td><img src="https://camo.githubusercontent.com/a3a6db2d24520a2a21318a1918f6d276566a41e4/68747470733a2f2f692e696d6775722e636f6d2f6f4969523463742e706e67"/></td>
</tr>
  <tr>
    <th>missingno.heatmap(df)</th>
    <th>missingno.dendrogram(df)</th>
  </tr>
</table>


## EDA automático

- Ver variables de forma individual (histogramas, valores mas comunes, media, etc)
- Correlaciones
- Valores perdidos

|         | [Pandas profiling](https://github.com/pandas-profiling/pandas-profiling) | <a href="https://github.com/fbdesignpro/sweetviz"><img src="../img/logos/Sweetviz.png"/></a> |
|---------|--------------------------------------------------------------------------|-----------------------------------------------------|
| Import  | `from pandas_profiling import ProfileReport`                             | `import sweetviz as sv`                             |
| Crear   | `report = ProfileReport(df)`                                             | `report = sv.analyze(df)`                           |
| Ver     | `report.to_notebook_iframe() `                                           | `report.show_html()`                                |
| Guardar | `report.to_file("report.html")`                                          |                                                     |
|  | ![](http://jaipancholi.com/static/automating-eda/variable-1.png) | ![](https://miro.medium.com/max/700/1*jx_ShECen95-F_M5PH9HCA.png) |


**[PandasGUI](https://github.com/adamerose/pandasgui)** es otra opción.




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
