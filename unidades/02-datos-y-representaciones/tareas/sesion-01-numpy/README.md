# Sesión 1 - NumPy y vectorización

Práctica completa de la primera sesión de la Unidad 2. Incluye las dos notebooks ejecutadas, los 11 ejercicios, el módulo de selección y sus pruebas.

## Contenido

```text
sesion-01-numpy/
├── datos/
├── 01-exploracion/
│   └── u2_n1_arreglos_numpy.ipynb
└── 02-reporte-mediciones/
    ├── measurements/
    │   ├── processing.py
    │   └── selection.py
    ├── tests/
    └── u2_n2_reporte_mediciones.ipynb
```

## Ejercicios resueltos

La notebook de exploración contiene:

1. Vector de una dimensión y matriz de una fila.
2. Arreglo flotante que conserva `22.75`.
3. Últimas tres rondas de sala norte y almacén.
4. Diferencia entre formas `(8,)` y `(8, 1)`.
5. Máscara para temperaturas de sala sur entre 26 y 29.
6. Copia independiente de las últimas rondas.
7. Conversión vectorizada de Celsius a Fahrenheit.
8. Conteo y media de filas con mediciones completas.
9. Diferencias respecto de la media de cada sala mediante broadcasting.

La notebook del reporte contiene:

10. Comparación entre las ocho rondas originales y las dos filas completas del archivo con errores.
11. Selección independiente de rondas cuya sala norte alcanza el umbral.

`measurements/selection.py` rechaza formas incorrectas, mediciones no finitas y umbrales no finitos. Con umbral 27 devuelve:

```text
[[27, 29, 25],
 [28, 30, 26],
 [29, 31, 27]]
```

Con umbral 100 devuelve una matriz vacía de forma `(0, 3)`. No se calcula su media porque no contiene observaciones.

## Ejecutar

Proyecto de exploración:

```bash
cd 01-exploracion
uv sync --locked
uv run --locked python main.py
```

Proyecto del reporte:

```bash
cd 02-reporte-mediciones
uv sync --locked
uv run --locked python main.py
uv run --locked python -m pytest
uv run --locked ruff check .
uv run --locked ruff format --check .
```

## Comprobaciones

Las dos notebooks se reiniciaron y ejecutaron completas:

```text
u2_n1_arreglos_numpy.ipynb: 25 de 25 celdas, 0 errores
u2_n2_reporte_mediciones.ipynb: 7 de 7 celdas, 0 errores
```

El proyecto del reporte terminó con:

```text
All checks passed!
8 files already formatted
25 passed
```

También se copiaron los archivos a una carpeta temporal limpia. Ahí se ejecutaron `uv sync --locked`, ambos scripts, las dos notebooks, Ruff y pytest. Todos los comandos terminaron con código 0.

## Estado

**Resuelta y verificada; no enviada al formulario.**
