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


<h1 align="center">📊 Gráficas</h1>
<h4 align="center">Ver <a href="https://python-graph-gallery.com">Python Graph Gallery</a> y <a href="https://www.data-to-viz.com">From Data to Viz</a></h4>

### Variable numérica: Distribución

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

### Variable numérica + variable numérica
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
    <td>plt.imshow(np)<br>sns.heatmap(df)
    </td>
    <td>df.plot.hexbin()</td>
    <td>scatter_matrix(df)<br>sns.pairplot()</td>
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

### Evolución temporal
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



> ## Referencias
> - [**Kaggle learn: data visualization**](https://www.kaggle.com/learn/data-visualization)
