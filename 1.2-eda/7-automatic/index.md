---
layout: page

parent_id: 1.2-eda
id: 7-automatic
title: 🤖 EDA automático (Pandas Profile y SweetViz)

notebook: pandas_profile.ipynb
---

- Ver variables de forma individual (histogramas, valores mas comunes, media, etc)
- Correlaciones
- Valores perdidos

|         | [Pandas profiling](https://github.com/pandas-profiling/pandas-profiling) | <a href="https://github.com/fbdesignpro/sweetviz"><img src="../img/logos/Sweetviz.png"/></a> |
|---------|--------------------------------------------------------------------------|-----------------------------------------------------|
| Import  | `from pandas_profiling import ProfileReport`                             | `import sweetviz as sv`                             |
| Crear   | `report = ProfileReport(df)`                                             | `report = sv.analyze(df)`                           |
| Ver     | `report.to_notebook_iframe() `                                           | `report.show_html()`                                |
| Guardar | `report.to_file("report.html")`                                          |                                                     |
|         | ![](http://jaipancholi.com/static/automating-eda/variable-1.png) | ![](https://miro.medium.com/max/700/1*jx_ShECen95-F_M5PH9HCA.png) |


**[PandasGUI](https://github.com/adamerose/pandasgui)** es otra opción.

