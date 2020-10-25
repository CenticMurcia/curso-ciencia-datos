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
- Podemos obtener información sobre el dataframe:
  - Primeras 10 filas: `df.head(10)`
  - Últimas 7 filas: `df.tail(7)`
  - Number of rows & variables: `df.shape`
  - Names of variables: `df.columns`
  - Types of variables: `df.info()`
  - Stats of numerical variables: `df.describe()`
  - Stats of numerical variables: `df.describe(include=['object', 'bool'])`
- Information of **numerical variables**:
  - Minimum `df.num_var.min()`
  - Maximun `df.num_var.max()`
  - Mean `df.num_var.mean()`
  - Median `df.num_var.median()`
  - Std `df.variable.std()`
- Information of **categorial variables**:
  - Unique values (count): `df.cat_var.value_counts()`
  - Unique values (percen): `df.cat_var.value_counts(normalize=True)`
  - 2 categorial vars (count): `pd.crosstab(df.cat_var1, df.cat_var2, margins=True)`
  - 2 categorial vars (percen): `pd.crosstab(df.cat_var1, df.cat_var2, margins=True, normalize=True)`
- Information of **numerical & categorial variables**:
  - Pivot table: `df.pivot_table([num_var1, num_var2, ...], [cat_var1, cat_var2], aggfunc='mean')`
- **Fitering rows**:
  - One filter: `df[ condition ]`
  - Multiple filters: `df[ (condition1) & (condition2)]`
