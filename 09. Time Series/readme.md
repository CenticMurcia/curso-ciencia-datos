<h1 align="center">🔮 Time Series</h1>


## 🛠 Feature engeeering del tiempo

```python
# Simple
def featEng_date(df, varName):
    df['year']         = df[varName].dt.year.astype(np.int16)
    df['month']        = df[varName].dt.month.astype(np.int8)
    df['week']         = df[varName].dt.weekofyear.astype(np.int8)
    df['day_of_year']  = df[varName].dt.dayofyear.astype(np.int16)
    df['day_of_month'] = df[varName].dt.day.astype(np.int8)
    df['day_of_week']  = df[varName].dt.dayofweek.astype(np.int8)
    df['hour']         = df[varName].dt.hour.astype(np.int8)
    df['minute']       = df[varName].dt.minute.astype(np.int8)
    df['is_weekend']   = # To do
    df['is_vacation']  = # To do

# Advanced: Agregregates
periods   = ["15T", "1H", "3H"]
agregates = ["count", "mean", "std", "min", "max", "sum", "median"]
```

> - [Tsfresh](https://tsfresh.readthedocs.io): Automatic calculates time series features
> - [Trane](https://github.com/HDI-Project/Trane)




## Modelos especificos
- GAM
- ARIMA
- ARIMAX
- Facebook Prophet
- LSTM
- Fractal Analysis



---

<h1 align="center">Competición<br><a href="https://www.kaggle.com/c/competitive-data-science-predict-future-sales">Predict future sales</a></h1>

Se dan los datos de las ventas de distintas tiendas desde Enero de 2013 hasta Octubre 2015. El objetivo es predecir la cantidad de productos que se venderán en cada tienda en el mese de Noviembre de 2015.

- [Link de la competición en Kaggle](https://www.kaggle.com/c/competitive-data-science-predict-future-sales)
- [1a version InClass de la competición](https://www.kaggle.com/c/competitive-data-science-final-project)


## Datos

- **`sales_train.csv`** Filas: 2935849 ventas (Enero 2013 --> Octubre 2015)
  - **date**: date in format dd/mm/yyyy
  - **date_block_num**: a consecutive month number. January 2013 is 0, February 2013 is 1,..., October 2015 is 33
  - **shop_id**: unique identifier of a shop
  - **item_id**: unique identifier of a product
  - **item_price**: current price of an item
  - **item_cnt_day**: number of products sold. You are predicting a monthly amount of this measure.
- **`shops.csv`** Filas: 60 tiendas
  - **shop_id**
  - **shop_name**: name of shop (EN RUSO 🇷🇺)
- **`items.csv`** Filas: 22170 productos
  - **item_id**
  - **item_name**: name of item (EN RUSO 🇷🇺)
  - **item_category_id**: unique identifier of item category
- **`item_categories.csv`** Filas: 84 categorías de producto
  - **item_category_id**
  - **item_category_name**: name of item category (EN RUSO 🇷🇺)
- **`test.csv`** Filas 214200 pares unicos de (Shop, Item)
  - **ID**: an Id that represents a (Shop, Item) tuple within the test set
  - **shop_id**
  - **item_id**



### Paso 1: EDA

Familiarizate con los datos entiende todas las variables y la relación que existe entre las tablas. Si tienes dudas genera algún plot (gráfica). Los plots nos ayudan a encontrar nuevas pistas.


### Paso 2: Baseline

Empieza con un baseline rápido y sencillo. No hace falta ni siquiera que sea un modelo. Coge el sample_submission.csv y envíalo. Luego cambia el 0.5 por otras constantes. Tambien puedes probar constantes específicas por producto o tienda.

Un buen ejercicio es copiar las ventas del último mes disponible (Octubre 2015) para predecir Noviembre 2015.
Lo más dificil aquí es generar los agregados para que se vea a nivel de mes y no de día. Tendrás que:
- Genera valores lagged
- Rellena los NaNs con ceros
- Limita las predicciones al rango [0,...,20]

Si lo haces bien conseguirás exactamente 1.16777 en el public leaderboard.


Generar features será necesario para nuestros futuros modelos más complejos. Además si decides limitar las cantidades de las predicciones al rango [0,...,20] notarás una gran diferencia.



### Paso 3: Primer modelo

Puedes obtener muy buena puntuación al crear lag-based features y entrenando un Gradient Boosting.

Busca la mejor forma de validar (ya que es mas rápido que enviar los resultados a Kaggle). Probablemente sea buena idea validar con los meses futuros que tienes disponibles. Así que el cross-validation no es muy recomendable para cuando se predice el futuro.



### Paso 4: Mejorar

Basicamente las mejoras vendrán si bien mejoras tus datos o bien mejoras tus modelos:


#### Mejora tus datos. Genera nuevas variables
- item lags
- shop lags
- lagged values of total shop or total item sales (which are essentially mean-encodings).
- Extrae características de las variables de texto (text descriptions)
- item categories
- Componente estacional (seasonal trends)
- Coge ideas de algun framwork [tsfresh](https://tsfresh.readthedocs.io), [featuretools](https://www.featuretools.com/)


#### Mejora tu modelo

1. Prueba modelos diferentes
   - Modelo lineal (Linear regression, SVM, perceptron)
   - Random Forest
   - Gradient Boosting (XGBoost, LightGBM, CatBoost)
   - Redes neuronales
2. Optimiza sus hiperparámetros
   - No gastes mucho tiempo aquí.
   - Prueba [optuna](https://optuna.org).
3. Ensembles
   - Empieza haciendo la media de un modelo lineal con un Gradient Boosting
      - Puedes darle mas peso al Gradient Boosting con una media ponderada.
   - Luego salta directamente al stacking.



---

# Aprende a extrapolar

[Kaggle discussion](https://www.kaggle.com/questions-and-answers/72639)

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(low=-10, high=10, size=1000) # np.arange(-10, 10, 0.1)
y = np.sin(x) + np.random.normal(scale=0.2, size=x.shape)
plt.scatter(x,y, s=5)
```

Read this article: [Caution with Random Forest](https://medium.com/datadriveninvestor/why-wont-time-series-data-and-random-forests-work-very-well-together-3c9f7b271631)
