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



# Limpiar datos

### Outliers (valores muy grandes)
- Quitar ventas con precios MUY caros (>100.000)
- Quitar ventas con cantidades muy grandes (>1.000)

### Precios negativos
- A los precios negativos asignar la media de los no negativos
(mismo producto, misma tienda, mismo mes)

### Tiendas duplicadas
las tiendas (0 y 57), (1 y 58), (10 y 11) son las mismas



# Extraer datos ocultos

### Tiendas: Sacar ciudad
La primera palabra del nombre de la tienda es la ciudad.

### Categorías: Sacar tipo y subtipo
El tipo es lo antes del guión. El subtipo es lo de despues del guión.

### Productos
No hacemos uso del nombre del producto, pero se podría crear un diccionario de palabras





# Unificar todas las tablas en 1

Única tabla cuyo índice es el producto cartesiano de MES + SHOP + ITEM.

- Hay productos que no aparecen para algunos meses y tiendas, y se deben rellenar con cero


### Añadir variable (TARGET)
- Calcular la suma de ventas por mes - trabajamos por meses
- Recortar a 20 es una recondemación de los organizadores del concurso
- Rellenar a cero los valores nulos

