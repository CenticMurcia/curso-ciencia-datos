---
layout: page

id: 3-pandas
title: Pandas

topic: Tools
---


### Resumen de Pandas
- Una tabla es un **dataframe** en Pandas.
- Una columna es una **serie** en Pandas.
- [Leer y guardar dataframes](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html):
  - Leer desde CSV: `df = pd.read_csv("filepath o url")`

### Información sobre el dataframe:
- Primeras 10 filas: `df.head(10)`
- Últimas 7 filas: `df.tail(7)`
- 13 filas aleatorias: `df.sample(13)`
- Número de filas y variables: `df.shape`
- Nombres de las variables: `df.columns`
- Tipos de datos de las variables: `df.info()`
- Estadísticas de las variables numéricas: `df.describe()`
- Estadísticas de las variables categóricas: `df.describe(include=['object', 'bool'])`

### Selección
- Seleccionar una variable (columna): `df["miVariable"]` o `df.miVariable`
- Seleccionar varias variables: `df[["miVariable", "otraVariable", "terceraVar"]]`
- Seleccionar una celda por variable y fila: `df["miVariable"][0]` 
- Recuerda que una condición nos devuelve para cada fila `True` o `False`:
  - Condición de *igualdad*: `df.pais == "España"`
  - Condición de *mayor que*: `df.edad > 18`
  - Condición de *está en*: `df.pais.isin(["España", "Italia"])`
  - Condición de *missing*: `df.price.isnull()` (el contrario es `.notnull()`)
- Seleccionar ciertas filas (1 filtro): `df[ df.pais=="España" ]`
- Seleccionar ciertas filas (N filtros): `df[ (df.pais == "España") & (df.edad > 18")]` (`&` para AND, `|` para OR)

### Añadir y modificar
- Nueva variable con valor constante: `df['var'] = 'valor constante'`
- Nueva variable con un rango: `df['index'] = range(len(df))`
- Modificar una celda: `df.at[4, 'B'] = 10`


### Distinguir vars numérica/categorias/fechas/texto
1. Mediante `select_dtypes` 
   - Lista de las vars categórias:   `cat_vars  = list(df.select_dtypes(include=["category", "object", "bool"]).columns)`
   - Lista de las vars numéricas:    `num_vars  = list(df.select_dtypes(exclude=["category", "object", "bool", "datetime64"]).columns)`
   - Lista de las vars fecha y hora: `time_vars = list(df.select_dtypes(include=['datetime64']).columns)`
2. Mediante `dtypes` 
   - Lista de las vars categórias:    `cat_vars  = df.dtypes[df.dtypes == "object"].index`
   - Lista de las vars numéricas:     `num_vars  = df.dtypes[df.dtypes != "object"].index`

### Variables numéricas
- Agregaciones escalares
  - Mínimo: `df.num_var.min()`
  - Máximo: `df.num_var.max()`
  - Media: `df.num_var.mean()`
  - Mediana: `df.num_var.median()`
  - Desviación estándar: `df.variable.std()`
  - Varianza: `df.num_var.var()`
  - Error estándar de la media: `df.num_var.sem()`
  - Skewness: `df.num_var.skew()`
  - Kurtosis: `df.num_var.kurt()`
  - Primero: `df.num_var.first()`
  - Último: `df.num_var.last()`
  - Enesimo: `df.num_var.nth(NUMERO)`
- Cuartiles: `df.num_var.describe()`
- Recuento: `df.num_var.count()` o `df.num_var.size()`
- Ranking: `df.num_var.rank()`


### Variables categórias
- Categorías (recuento): `df.cat_var.value_counts()`
  - Categorías (porcentaje): `df.cat_var.value_counts(normalize=True)`
- Categorías (cuantas hay para cada var) `df.nunique()`
  - Plot `df.nunique().sort_values().plot.barh()`
  - Categorías (cuantas hay respecto al maximo) `df.nunique()/len(df)`
  - Categorías (cuantas hay de una var) `df.cat_var.nunique()`
- Categorías (solo nombres) `df.cat_var.unique()`  
- Cruzar 2 variables categóricas: `pd.crosstab(df.cat_var1, df.cat_var2)`
  - Con márgenes `pd.crosstab(df.cat_var1, df.cat_var2, margins=True)`
  - En porcentajes totales `pd.crosstab(df.cat_var1, df.cat_var2, normalize=True)`
  - En porcentajes por fila `pd.crosstab(df.cat_var1, df.cat_var2, normalize="index")`
  - En porcentajes por columna `pd.crosstab(df.cat_var1, df.cat_var2, normalize="columns")`

### Variables numéricas + categóricas = agregaciones
- **Group by**: `df.groupby([cat_var1, cat_var2,...])[[num_var1, num_var2,...]].agg(["min", "max", "mean", "std", "first"])`
- **Pivot table**: `df.pivot_table([num_var1, num_var2, ...], [cat_var1, cat_var2], aggfunc='mean')`


### [Aplicar estilo](https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html)
- Colorear celdas según su valor (heatmap): `df.style.background_gradient()`
- Pintar barras: `df.style.bar(subset=['Var1', 'Var2'], color='#d65f5f')`

### Big Data

Cuando los datos son muy grandes y tardan mucho en ser procesados o directamente no caben en memoria (más gigas en el CSV que en la memoria RAM) estas son las recomendaciones a seguir:

- Una manera de aligerar los cálculos es disminuir el tamaño que ocupa nuestro dataframe. Convirtiendo enteros y floats de 32 y 64 bits a 8 y 16 bits, podemos reducir mucho el tamaño. `.astype('int32')`, `.astype('flaot32')`
- Si guardas los datos en formato binario (como `.npy`) serán más rápidos de leer que en texto planto (como `.csv`).
- Más consejos en [Enhancing performance](https://pandas.pydata.org/pandas-docs/stable/user_guide/enhancingperf.html) y [Scaling to large datasets](https://pandas.pydata.org/pandas-docs/stable/user_guide/scale.html).
- H20 dispone de un paquete llamado [datatable](https://github.com/h2oai/datatable) que es un poco más eficiente que pandas.

  
> ## Material adicional
> - [100 pandas tricks](https://www.dataschool.io/python-pandas-tips-and-tricks/)
> - [Curso Kaggle de Python](https://www.kaggle.com/learn/python)
> - [Curso Kaggle de Pandas](https://www.kaggle.com/learn/pandas)
> - [28 Jupyter Notebook tips, tricks and shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts)
