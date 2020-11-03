<p align="center"><img src="../img/miniaturas YT/1-Pandas.png" height="200px"></p>

<table>
  <tr>
    <th width="200"><a href="https://www.python.org"><img src="../img/logos/Python.png"/></a></th>
    <td>Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Aprende más en <a href="https://www.kaggle.com/learn/python">Kaggle learn</a></td>
  </tr>
  <tr>
    <th><a href="https://jupyter.org"><img height="100" src="../img/logos/Jupyter.png"/></a></th>
    <td>Jupyter Notebook es un entorno interactivo de Python, que se ejecuta de forma local en el navegador. En los cuadernos de Jupyter se puede incluir (en forma de celdas) tanto código Python, como gráficas y documentación en formato markdown que te ayuden en el análisis e explicación de tus datos.</td>
  </tr>
  <tr>
    <th><a href="https://colab.research.google.com/notebooks/welcome.ipynb"><img src="../img/logos/Colab.png"/></a></th>
    <td>Google Colab es un entorno gratuito de Jupyter Notebook que no requiere configuración y que se ejecuta completamente en la nube. Colabo te permite escribir y ejecutar código, guardar y compartir tus análisis y tener acceso a recursos informáticos muy potentes (GPUs y TPUs por tiempo limitado), todo de forma gratuita desde el navegador.</td>
  </tr>
  <tr>
    <th width="200"><a href="https://www.python.org"><img src="../img/logos/NumPy.png"/></a></th>
    <td>Numpy es una librería de Python para crear y operar con vectores y matrices. Esta librería (programada en C) ofrece a Python eficiencia en la computación numérica.</td>
  </tr>
  <tr>
    <th width="200"><a href="https://pandas.pydata.org"><img src="../img/logos/Pandas.png"/></a></th>
    <td>Pandas es un paquete de Python que proporciona estructuras de datos para el manejo de datasets o dataframes. Pandas depende de Numpy, la librería que añade eficiencia numérica en Python. Los principales tipos de datos que pueden representarse con pandas son los datos tabulares con columnas (llamadas variables) y muchas filas. También se pueden representar series temporales.
<br><br>
Pandas permiten leer y escribir datos en diferentes formatos (CSV, Excel, SQL,...) y la  manipulacion de datos como seleccionar y filtrar datos en función de posición, valor o etiquetas, fusionar y unir datos, transformar datos aplicando funciones tanto en global como por ventanas, manipulación de series temporales, hacer gráficas y mucho más. Aprende más en <a href="https://www.kaggle.com/learn/pandas">Kaggle learn</a>
</td>
  </tr>
</table>




# Resumen de Pandas
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
- Seleccionar varias variables: `df[["miVariable", "otraVariable", "terceraVar"]`
- Seleccionar una celda por variable y fila: `df["miVariable"][0]` 
- Selección filtrando:
  - Recuerda que una condición nos devuelve para cada fila `True` o `False`:
    - Condición de *igualdad*: `df.pais == "España"`
    - Condicion de *mayor que*: `df.edad > 18`
    - Condicion de *está en*: `df.pais.isin(["España", "Italia"])`
    - Condición de *missing*: `df.price.isnull()` (el contrario es `.notnull()`)
  - Selección con filtro: `df[ df.pais=="España" ]`
  - Selección con varios filtros: `df[ (df.pais == "España") & (df.edad > 18")]` (`&` para AND, `|` para OR)


### Añadir y modificar
- Poner un valor constante en una variable: `df['var'] = 'valor constante'`
- Poner un contador en una variable: `df['index'] = range(len(df))`


### Variables numéricas
- Mínimo `df.num_var.min()`
- Máximo `df.num_var.max()`
- Media `df.num_var.mean()`
- Mediana `df.num_var.median()`
- Desviación estándar `df.variable.std()`
- Varianza `df.num_var.var()`
- Error estándar de la media `df.num_var.sem()`
- Primero `df.num_var.first()`
- Último `df.num_var.last()`
- Enesimo `df.num_var.nth(NUMERO)`
- Cuartiles `df.num_var.describe()`
- Recuento `df.num_var.count()`
- Recuento `df.num_var.size()`
- Ranking `df.num_var.rank()`


### Variables categórias
- Categorías (recuento): `df.cat_var.value_counts()`
- Categorías (porcentaje): `df.cat_var.value_counts(normalize=True)`
- Categorías (solo nombres) `df.cat_var.unique()`
- Cruzar 2 variables categóricas: `pd.crosstab(df.cat_var1, df.cat_var2)`
  - Con márgenes `pd.crosstab(df.cat_var1, df.cat_var2, margins=True)`
  - En porcentajes totales `pd.crosstab(df.cat_var1, df.cat_var2, normalize=True)`
  - En porcentajes por fila `pd.crosstab(df.cat_var1, df.cat_var2, normalize="index")`
  - En porcentajes por columna `pd.crosstab(df.cat_var1, df.cat_var2, normalize="columns")`

### Variables numéricas + categóricas
- **Group by**: `df.groupby([cat_var1, cat_var2, ...])[[num_var1, num_var2, ...]].agg(["min", "max", "mean", "std", "first"])`
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

---
  
> ## Material adicional
> - [Curso Kaggle de Python](https://www.kaggle.com/learn/python)
> - [Curso Kaggle de Pandas](https://www.kaggle.com/learn/pandas)
> - [28 Jupyter Notebook tips, tricks and shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts)
