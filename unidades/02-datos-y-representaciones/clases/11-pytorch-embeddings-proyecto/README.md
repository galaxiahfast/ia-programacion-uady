# Clase 11 - PyTorch, embeddings y proyecto final

Esta clase corresponde al 8 de octubre. Primero aclara cuáles ejercicios se entregan, después concluye la práctica de PyTorch con CIFAR-10 y finalmente explica los embeddings y la búsqueda semántica que se usarán en el proyecto final.

## Minutos que revisaría

- `00:32 a 10:45`: aclaraciones de las entregas y de cuáles ejercicios forman parte de cada práctica.
- `11:00 a 28:30`: repaso de `from_numpy`, memoria compartida, `TensorDataset`, `DataLoader`, transformaciones y CIFAR-10.
- `31:30 a 46:30`: medias por imagen y canal, reducción por ejes y normalización.
- `46:30 a 59:00`: operaciones útiles con tensores: `min`, `max`, `cat`, `item`, `tolist` y conteos por clase.
- `1:00:00 a 1:09:00`: qué es un embedding y cómo obtener tensores con Sentence Transformers.
- `1:20:00 a 1:43:30`: búsqueda semántica, normalización, similitud mediante producto matricial y selección de los mejores resultados.
- `1:43:30 a 1:54:15`: cómo trasladar esas operaciones al proyecto final.

## Lo principal de PyTorch

Al reducir un tensor es importante elegir los ejes correctos. En un lote de imágenes, conservar la dimensión del canal permite obtener una media distinta para rojo, verde y azul. La normalización resta la media y divide entre la desviación estándar.

`torch.cat` concatena tensores en el eje indicado. `item()` extrae un solo valor de un tensor y `tolist()` convierte un tensor en estructuras normales de Python. Estas conversiones son útiles para preparar resultados que después se guardarán o mostrarán.

## Embeddings y búsqueda semántica

Un embedding representa un texto mediante un vector numérico. Textos de significado parecido deben quedar cerca en ese espacio, aunque no utilicen exactamente las mismas palabras.

Para comparar una consulta con varios documentos se generan sus embeddings, se normalizan y se calcula su similitud. En la demostración se obtuvo el mismo resultado con una operación directa y con producto matricial usando `@`. Después se toman las puntuaciones mayores para devolver los documentos más relacionados.

Esta es la base del proyecto final: crear representaciones de productos y reseñas, compararlas con la consulta del usuario y organizar el código en funciones y módulos reutilizables.

## Actividades y entregas

No se asignó una práctica nueva. La clase continuó los ejercicios ya incluidos en la sesión de PyTorch y explicó código que será necesario para el proyecto final.

También se aclaró que deben entregarse únicamente los ejercicios señalados en cada `PRACTICA.md`; las explicaciones adicionales de las guías no se convierten automáticamente en entregables. Las tareas siguen resueltas en el repositorio y pendientes de envío.

## Materiales

- [Sesión oficial de PyTorch](https://github.com/oscarnavmac/programacion_ai/tree/main/unidad-02-procesamiento-datos/sesion-03-pytorch)
- [Consigna del proyecto final](https://github.com/oscarnavmac/programacion_ai/tree/main/proyecto-final)
