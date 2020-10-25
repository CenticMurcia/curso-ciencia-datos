# EDA


## EDA automático

- Ver variables de forma individual (histogramas, valores mas comunes, media, etc)
- Correlaciones
- Valores perdidos

|         | [Pandas profiling](https://github.com/pandas-profiling/pandas-profiling) | [Sweetviz](https://github.com/fbdesignpro/sweetviz) |
|---------|--------------------------------------------------------------------------|-----------------------------------------------------|
| Import  | `from pandas_profiling import ProfileReport`                             | `import sweetviz as sv`                             |
| Crear   | `report = ProfileReport(df)`                                             | `report = sv.analyze(df)`                           |
| Ver     | `report.to_notebook_iframe() `                                           | `report.show_html()`                                |
| Guardar | `report.to_file("report.html")`                                          |                                                     |
|  | ![](http://jaipancholi.com/static/automating-eda/variable-1.png) | ![](https://miro.medium.com/max/700/1*jx_ShECen95-F_M5PH9HCA.png) |
