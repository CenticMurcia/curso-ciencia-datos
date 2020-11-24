
<h1 align="center">Competición<br><a href="https://www.kaggle.com/c/competitive-data-science-predict-future-sales">Predict future sales</a></h1>

Se dan los datos de las ventas de distintas tiendas desde Enero de 2013 hasta Octubre 2015. El objetivo es predecir la cantidad de productos que se venderán en cada tienda en el mese de Noviembre de 2015.

- [Link de la competición en Kaggle](https://www.kaggle.com/c/competitive-data-science-predict-future-sales)
- [1a version InClass de la competición](https://www.kaggle.com/c/competitive-data-science-final-project)


## Datos

- **`sales_train.csv`** Filas: 2935849 ventas (Enero 2013 --> Octubre 2015)
  - **date**: date in format dd/mm/yyyy.
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
1. Quedate solo con las ventas de Octubre 2015: `date_block_num==33`
2. Genera valores agregados: `groupby`
3. Quedate con los pares de shop-item que te pidan en test: `merge`
4. Rellena los NaNs con ceros: `.fillna(0)`
5. Limita las predicciones al rango [0,...,20]: `.clip(lower=0, upper=20)`

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



# EDA: Distribuciones

### Tiendas en TRAIN y TEST
- Tiendas en train: 60
- Tiendas en test:  42
- Tiendas solo en train: 18 {0, 1, 8, 9, 11, 13, 17, 20, 23, 27, 29, 30, 32, 33, 40, 43, 51, 54}
- Mismas tiendas en train y test: 42
- Tiendas solo en test: 0

### Productos en TRAIN y TEST
- Productos en train:          21806
- Productos en test:           5100
- Productos solo en train:     17069
- Mismos prod en train y test: 4737
- Productos solo en test:      363



## Limpiar datos

#### Outliers
- Valores muy grandes
  - Quitar ventas con precios MUY caros (>100.000)
  - Quitar ventas con cantidades muy grandes (>1.000)
- Precios negativos
  - A los precios negativos asignar la media de los no negativos (mismo producto, misma tienda, mismo mes)
- Cantidades negativas (NO ES UN OUTLIER!)
  - Una venta con cantidad negativa no es una venta, es una DEVOLUCION.

#### Duplicados
- Tiendas duplicadas
  - Las tiendas con `shop_id` 0 y 57 son la misma.
  - Las tiendas con `shop_id` 1 y 58 son la misma.
  - Las tiendas con `shop_id` 10 y 11 son la misma.


## Extraer datos ocultos

- **`shops.csv`**: Sacar ciudad y tipo de tienda
  - `shop_city`: La primera palabra del shop_name es la ciudad.
  - `shop_type`: La segunda palabra del shop_name es tipo.
  - Se podría sacar las coordenadas (latitud y longitud) de cada tienda.
- **`item_categories.csv`**: Sacar tipo y subtipo
  - `item_type`: El tipo es lo antes del guión.
  - `item_subtype`: El subtipo es lo de despues del guión.
- **`items.csv`**:
  - No hacemos uso del nombre del producto, pero se podría crear un diccionario de palabras



## Creación del dataset

## Unificar todas las tablas en 1 (JOINS)

1. Crear una única tabla cuyo índice es el producto cartesiano de MES + SHOP + ITEM.
   - Hay productos que no aparecen para algunos meses y tiendas, y se deben rellenar con cero


### Añadir variable (TARGET)
- Calcular la suma de ventas por mes - trabajamos por meses
- Recortar a 20 es una recondemación de los organizadores del concurso
- Rellenar a cero los valores nulos

