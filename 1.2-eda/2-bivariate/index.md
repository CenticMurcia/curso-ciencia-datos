---
layout: page

parent_id: 1.2-eda
id: 2-bivariate
title: 📈 Análisis Bivariante
---



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