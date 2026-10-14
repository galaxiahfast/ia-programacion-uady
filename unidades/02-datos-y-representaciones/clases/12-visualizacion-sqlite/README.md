# Clase 12 - Visualización y SQLite

Esta clase corresponde al 9 de octubre. Termina la Unidad 2 con Matplotlib y comienza la Unidad 3 mostrando cómo consultar una base SQLite desde Python.

## Minutos que revisaría

- `01:30 a 18:30`: estructura de Matplotlib, diferencia entre `Figure` y `Axes`, y personalización de una gráfica.
- `27:00 a 42:30`: histogramas, barras y comparación de porcentajes por grupo.
- `50:45 a 53:15`: guardar figuras y cierre de los dos ejercicios de visualización.
- `1:05:20 a 1:26:15`: SQLite, conexión, consultas parametrizadas, inserciones y lectura de resultados.
- `1:30:00 a 1:46:55`: transacciones, `commit`, rollback y carga de una consulta SQL en pandas.

## Lo principal de Matplotlib

Una `Figure` contiene el lienzo completo y cada `Axes` es una zona donde se dibuja. Conviene conservar esas variables para añadir títulos, etiquetas, límites y varias gráficas sin depender del estado global de `pyplot`.

Los histogramas agrupan valores numéricos en intervalos. Cambiar `bins` modifica el detalle visual, no la cantidad de observaciones. Las barras sirven para comparar categorías; si muestran porcentajes, hay que explicar cuál es el total usado como denominador.

## Lo principal de SQLite

SQLite almacena una base de datos local en un archivo. Desde Python se abre una conexión, se ejecutan consultas con parámetros y se cierran los recursos al terminar. Los parámetros deben enviarse por separado y no armarse dentro del texto SQL.

El bloque de transacción confirma los cambios si todo sale bien y los revierte cuando ocurre un error. `pandas.read_sql_query()` permite convertir directamente el resultado de un `SELECT` en un `DataFrame`.

## Actividades

- Los dos ejercicios de visualización están resueltos en [la sesión de Matplotlib](../../tareas/sesion-04-visualizacion/).
- Los tres ejercicios de SQLite están resueltos en [la sesión 1 de la Unidad 3](../../../03-integracion-de-componentes/tareas/sesion-01-sql-nosql/).
- Neo4j se presentó como material opcional y no añade una tarea en esta clase.

Ningún archivo se ha enviado todavía al formulario.
