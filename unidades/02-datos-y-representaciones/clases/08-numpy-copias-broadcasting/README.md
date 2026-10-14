# Clase 8 - Copias, broadcasting e inicio de pandas

Esta clase corresponde al 2 de octubre. Continúa directamente la sesión anterior de NumPy, termina sus ejercicios y dedica los últimos minutos a presentar pandas con el conjunto de datos del Titanic.

## Minutos que revisaría

- `00:00 a 21:30`: diferencia entre una vista y una copia; efecto de los slices, las máscaras y `copy()` sobre el arreglo original.
- `21:30 a 33:40`: operaciones vectorizadas y comparación con ciclos o comprensiones.
- `33:40 a 46:20`: reglas de broadcasting, dimensiones compatibles, transposición y errores por formas incompatibles.
- `47:15 a 1:15:10`: datos finitos, `NaN`, infinito y combinación de máscaras con `all`, `any` y negaciones.
- `1:18:30 a 1:37:45`: repaso de los ejercicios de NumPy y función para seleccionar filas según un umbral.
- `1:38:00 al final`: inicio de pandas, diferencias con NumPy, `DataFrame`, `Series`, lectura de CSV y revisión inicial del Titanic.

## Lo principal

Un slice básico suele ser una vista del mismo bloque de memoria. Si se modifica esa vista, puede cambiar también el arreglo original. `copy()` crea datos independientes. En cambio, una selección hecha con una máscara booleana produce una copia, aunque una asignación con máscara sí modifica el arreglo al que se aplica.

La vectorización permite operar sobre arreglos completos sin recorrerlos elemento por elemento. El broadcasting extiende arreglos de formas compatibles: las dimensiones se comparan desde la derecha y deben ser iguales o una de ellas debe valer uno.

Para revisar calidad de datos se combinaron `isfinite`, `isnan`, comparaciones y máscaras. `all` exige que se cumpla una condición en todos los elementos del eje elegido; `any` basta con que se cumpla en uno.

Al final se explicó que pandas está construido sobre NumPy y resulta más práctico para tablas con columnas de distintos tipos. Un `DataFrame` representa la tabla completa y una `Series`, una columna con índice.

## Actividades

No se dejó una tarea distinta. Se terminó la práctica de NumPy que había comenzado en la clase 7, incluidos los ejercicios de calidad de datos y selección por temperatura. Esa práctica ya está resuelta en [la carpeta de NumPy](../../tareas/sesion-01-numpy/), pero no se ha enviado a Forms.

## Material

- [Sesión oficial de NumPy](https://github.com/oscarnavmac/programacion_ai/tree/main/unidad-02-procesamiento-datos/sesion-01-numpy)
- [Sesión oficial de pandas](https://github.com/oscarnavmac/programacion_ai/tree/main/unidad-02-procesamiento-datos/sesion-02-pandas)
