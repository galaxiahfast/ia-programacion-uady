# Clase 7 - Calidad de código y primeros pasos con NumPy

La grabación dura cerca de 1 hora con 56 minutos. Los primeros 18 minutos cierran la Unidad 1 y el resto inicia NumPy con arreglos, dimensiones, selección y máscaras.

## Minutos que revisaría

- `00:07 a 05:25`: para qué sirven pytest, Ruff y mypy y cómo se ejecutan.
- `05:26 a 11:30`: archivos de pruebas, casos válidos e inválidos y comprobaciones de calidad.
- `11:30 a 17:33`: dudas sobre calidad y aclaración de los entregables de la sesión 4.
- `17:44 a 26:30`: inicio de la Unidad 2, diferencia entre listas y arreglos y preparación del proyecto de NumPy.
- `26:30 a 36:47`: carga del CSV y significado de `ndim`, `shape`, `size` y `dtype`.
- `36:48 a 44:15`: ejercicio 1, vectores frente a matrices de una fila y tipos numéricos.
- `44:15 a 1:21:04`: índices, slices, selección de filas y columnas y ejercicio 3.
- `1:21:45 a 1:31:00`: ejercicio 4 y diferencia entre una columna con forma `(8,)` y `(8, 1)`.
- `1:31:00 a 1:47:28`: máscaras booleanas, selección de filas completas y combinación de condiciones.
- `1:47:29 a 1:51:25`: ejercicio 5, intervalo de temperatura de la sala sur.
- `1:52:11 a 1:56:18`: ubicación de prácticas, entregables por unidad y aclaraciones del formulario.

## Cierre de calidad de código

Las herramientas cumplen funciones distintas:

- **pytest** ejecuta casos que comprueban el comportamiento del programa;
- **Ruff** detecta problemas frecuentes y revisa el formato;
- **mypy** contrasta el código con sus anotaciones sin ejecutarlo;
- el **Makefile** reúne varios comandos bajo nombres como `check`.

Una prueba debe dejar claro qué entrada usa y qué resultado espera. También conviene cubrir errores y límites, no solo el caso normal. El profesor confirmó que la sesión 4 de la Unidad 1 se entrega como proyecto, siguiendo únicamente lo indicado en `PRACTICA.md` y `CALIDAD.md`.

## Listas y arreglos

Una lista de Python es una colección flexible. Un `ndarray` guarda elementos de un tipo común y permite operar sobre grupos completos de valores.

Multiplicar una lista por dos repite sus elementos; multiplicar un arreglo por dos multiplica cada valor. La diferencia no es solo sintáctica: el arreglo representa explícitamente ejes, forma y tipo numérico.

## Propiedades de un arreglo

La matriz de la clase contiene ocho rondas y tres salas:

- `ndim == 2`: tiene dos ejes;
- `shape == (8, 3)`: ocho filas y tres columnas;
- `size == 24`: contiene 24 valores;
- `dtype == float64`: cada medición se representa como número decimal.

`shape` siempre es una tupla. Un vector de tres valores tiene forma `(3,)`; una matriz de una fila con los mismos valores tiene forma `(1, 3)`. Ambos contienen tres elementos, pero no tienen el mismo número de ejes.

El `dtype` importa: si el arreglo es entero, asignar `22.75` puede truncar el decimal. Para mediciones se utiliza `float64`. Mezclar texto con números puede producir un arreglo de cadenas que ya no sirve directamente para cálculos numéricos.

## Índices y slices

En `readings[fila, columna]`, el primer índice identifica la ronda y el segundo la sala. Un índice entero elimina el eje seleccionado; un slice lo conserva.

Por ejemplo:

```python
south_vector = readings[:, 1]    # (8,)
south_column = readings[:, 1:2]  # (8, 1)
```

La elección depende de lo que espere la siguiente operación. Para seleccionar columnas no consecutivas se puede usar una lista de índices, por ejemplo `readings[-3:, [0, 2]]`.

## Máscaras booleanas

Una comparación como `readings[:, 1] >= 26` produce un booleano por fila. Al aplicar esa máscara al arreglo se conservan las filas marcadas con `True`.

Las condiciones se combinan con `&` y cada comparación debe ir entre paréntesis:

```python
mask = (readings[:, 1] >= 26) & (readings[:, 1] < 29)
selected = readings[mask]
```

Una máscara de longitud ocho selecciona filas completas de una matriz con ocho filas. Una máscara con la misma forma que toda la matriz seleccionaría valores individuales y el resultado ya no conservaría necesariamente la estructura por rondas.

## Tareas detectadas

La sesión 1 de la Unidad 2 reúne **11 ejercicios**:

1. Ocho ejercicios en la notebook de exploración.
2. Un ejercicio adicional de broadcasting: restar la media de cada sala.
3. Dos ejercicios en la notebook del reporte.
4. El ejercicio 11 además requiere `measurements/selection.py` y pruebas.

En esta clase se explican los ejercicios 1 a 5. Vistas, copias, vectorización, broadcasting y el proyecto de reporte quedan para la siguiente grabación. La fecha límite actualizada de la Unidad 2 es el **19 de octubre de 2026**.

Los ejercicios se resolverán en este repositorio, pero **no se enviarán al formulario**.

## Materiales

- [Sesión oficial de NumPy](https://github.com/oscarnavmac/programacion_ai/tree/main/unidad-02-procesamiento-datos/sesion-01-numpy)
- [Práctica con los 11 ejercicios](https://github.com/oscarnavmac/programacion_ai/blob/main/unidad-02-procesamiento-datos/sesion-01-numpy/PRACTICA.md)
- [Guía de trabajo](https://github.com/oscarnavmac/programacion_ai/blob/main/unidad-02-procesamiento-datos/sesion-01-numpy/GUIA.md)
- [Presentación](https://drive.google.com/file/d/1nd5-nHeYSDUZgLEwXG9WLvCaIF-c_oPl/view?usp=drivesdk)
