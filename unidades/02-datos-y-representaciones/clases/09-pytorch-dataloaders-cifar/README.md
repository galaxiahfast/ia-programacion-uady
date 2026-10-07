# Clase 9 - PyTorch, DataLoader y CIFAR-10

Esta grabación sí es nueva y dura cerca de 2 horas. Primero se resolvió un problema con el kernel de VS Code y se acordaron nuevas fechas de entrega. Después se retomó PyTorch: tensores, datasets, lotes, orden aleatorio reproducible y transformaciones de imágenes.

## Minutos que revisaría

- `00:00 a 06:30`: solución cuando VS Code no encuentra el kernel creado con uv.
- `06:39 a 15:06`: conversación y acuerdo final sobre las nuevas fechas de entrega.
- `15:06 a 35:30`: repaso de tensores, conversión desde NumPy, memoria compartida y uso de `clone` o una copia.
- `35:30 a 48:55`: `TensorDataset`, subconjuntos, `DataLoader`, tamaño de lote y `drop_last`.
- `48:55 a 1:07:20`: dudas sobre muestras, columnas, etiquetas y forma de los lotes.
- `1:07:20 a 1:28:55`: `shuffle` y uso de un generador con semilla para repetir el mismo orden.
- `1:28:55 a 1:49:15`: CIFAR-10, imágenes de Pillow, tensores y transformaciones.
- `1:49:15 al final`: dataset propio, transformación al leer cada elemento y recorrido por lotes sin cargar todo en memoria.

## Nuevas fechas

Las fechas acordadas en esta clase y publicadas después en el repositorio del profesor son:

- Unidad 1: **12 de octubre de 2026**.
- Unidades 2 y 3: **19 de octubre de 2026**.
- Proyecto final: **26 de octubre de 2026**.

Estas fechas reemplazan las que aparecían en las clases anteriores.

## Lo principal de PyTorch

`torch.from_numpy` crea un tensor que comparte memoria con el arreglo original. Si se modifica uno, el otro también puede cambiar. Cuando se necesita una copia independiente se debe copiar el arreglo o clonar el tensor.

`TensorDataset` agrupa tensores que representan las partes de cada muestra, por ejemplo características y etiquetas. `DataLoader` recorre ese dataset por lotes. Si el número de muestras no es múltiplo del tamaño del lote, el último lote puede ser más pequeño; con `drop_last=True` se descarta.

Con `shuffle=True` el orden cambia. Para repetirlo se pasa un `torch.Generator` con una semilla fija al crear el `DataLoader`. La semilla no elimina la aleatoriedad: permite producir la misma secuencia otra vez.

## CIFAR-10 y transformaciones

CIFAR-10 contiene imágenes pequeñas repartidas en diez clases. La imagen original se obtiene como objeto de Pillow y debe transformarse antes de trabajar con ella en PyTorch. La secuencia mostrada convierte la imagen, cambia su tipo y escala sus valores.

También se explicó cómo crear una clase `Dataset` que guarda rutas y etiquetas, pero abre y transforma cada imagen únicamente cuando `__getitem__` la solicita. Esto sirve cuando los datos completos no caben en memoria.

## Actividades

No se asignó una tarea adicional. La clase continúa los ejercicios de la sesión de PyTorch:

- conversión de NumPy a tensor y comprobación de memoria compartida;
- uso de una copia independiente;
- `TensorDataset`, `DataLoader`, `drop_last` y lotes;
- CIFAR-10 y transformaciones;
- proporciones por clase en el proyecto.

Los cinco ejercicios ya están resueltos en [la tarea de PyTorch](../../tareas/sesion-03-pytorch/). La entrega sigue marcada como **no enviada**.

## Material

- [Sesión oficial de PyTorch](https://github.com/oscarnavmac/programacion_ai/tree/main/unidad-02-procesamiento-datos/sesion-03-pytorch)

