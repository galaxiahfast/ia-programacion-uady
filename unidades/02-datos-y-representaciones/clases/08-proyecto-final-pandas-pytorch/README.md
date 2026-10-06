# Clase 8 - Proyecto final, pandas y PyTorch

La grabación dura cerca de 2 horas. Al principio se explica el proyecto final; después se trabaja con el Titanic en pandas y al final se inicia el tema de tensores y conjuntos de datos en PyTorch.

## Minutos que revisaría

- `00:30 a 05:30`: alcance del proyecto final, datos elegidos y organización del código.
- `05:30 a 13:40`: embeddings de productos y reseñas, búsqueda semántica y herramientas del servidor MCP.
- `13:40 a 16:20`: requisitos de entrega y fechas de las unidades.
- `16:28 a 23:40`: Series, DataFrames y primeras operaciones con el Titanic.
- `23:40 a 33:25`: lectura del CSV, `shape`, tipos de datos, índice e información general.
- `33:25 a 48:40`: selección con columnas, `loc`, condiciones y máscaras.
- `48:40 a 1:08:30`: datos faltantes, `dropna`, `fillna` y agrupaciones.
- `1:08:30 a 1:23:30`: cruces con `merge` y preparación de arreglos para NumPy.
- `1:28:00 a 1:40:00`: inicio de PyTorch, tensores y conjuntos de datos.
- `1:40:00 a 1:56:00`: forma y operaciones de tensores; uso de los datos preparados del Titanic.
- `1:56:00 al final`: cierre de la demostración. La práctica de PyTorch queda para continuarla en la siguiente clase.

## Proyecto final

El proyecto consiste en construir un buscador semántico de productos de la categoría Electronics de Amazon Reviews 2023. El conjunto preparado contiene 600 productos y 6,992 reseñas.

La idea es generar dos representaciones por producto con `sentence-transformers/all-MiniLM-L6-v2`: una a partir del catálogo y otra con el promedio de sus reseñas. Ambas se normalizan, se combinan con el mismo peso y se vuelven a normalizar.

El resultado se expone mediante un servidor MCP por HTTP en `http://127.0.0.1:8000/mcp`, con tres herramientas:

- `search_products(query, top_k=5)`: busca productos por significado;
- `analyze_product(product_id)`: resume la información y reseñas de un producto;
- `compare_products(product_ids)`: compara varios productos.

No basta con que funcione en la notebook. El código debe separarse en módulos, tener errores claros, pasar mypy en modo estricto e incluir instrucciones de instalación, ejemplos y limitaciones. La fecha límite indicada es el **19 de octubre de 2026**.

## Lo principal de pandas

Una `Series` representa una columna con índice y un `DataFrame` una tabla completa. Antes de analizar un CSV conviene revisar su forma, nombres de columnas, tipos y valores faltantes.

Para filtrar se crea una condición booleana y se aplica con `loc`. Las agrupaciones con `groupby` permiten calcular estadísticas por categoría; `merge` sirve para combinar tablas mediante una llave compartida.

Con datos faltantes no hay una solución universal: se pueden conservar, eliminar o sustituir, pero la decisión debe corresponder al análisis. En la práctica se pide medir, por clase de pasajero, cuántas edades faltan y qué proporción representan.

## Inicio de PyTorch

Un tensor es una estructura numérica parecida a un arreglo de NumPy, preparada para trabajar con PyTorch y, cuando existe, con aceleración por GPU. Su forma sigue siendo importante porque determina qué operaciones son compatibles.

La sesión también introduce `Dataset` y `DataLoader`: el primero representa los ejemplos disponibles y el segundo los recorre por lotes. Al inspeccionar etiquetas se deben conservar incluso las clases que aparecen cero veces en una muestra, ya que siguen formando parte del problema.

## Actividades detectadas

- La práctica de pandas tiene cinco ejercicios. Los primeros cuatro están en la notebook y el quinto agrega un reporte de edades faltantes por clase, pruebas y un CSV.
- La práctica de PyTorch tiene cinco ejercicios. Los primeros cuatro están en la notebook y el quinto amplía el resumen de clases con proporciones, incluyendo clases con conteo cero.
- El proyecto final queda asignado con fecha límite del 19 de octubre.

Las prácticas se resolverán aquí y quedarán marcadas como **resueltas, no enviadas**. No se hará ningún envío a Forms.

## Materiales

- [Sesión oficial de pandas](https://github.com/oscarnavmac/programacion_ai/tree/main/unidad-02-procesamiento-datos/sesion-02-pandas)
- [Sesión oficial de PyTorch](https://github.com/oscarnavmac/programacion_ai/tree/main/unidad-02-procesamiento-datos/sesion-03-pytorch)
- [Consigna del proyecto final](https://github.com/oscarnavmac/programacion_ai/tree/main/proyecto-final)

