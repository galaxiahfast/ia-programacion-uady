# Ruta rápida para ver las clases 1 a 9

Esta selección evita configuraciones, pausas, dudas repetidas y resolución mecánica de ejercicios que ya están terminados en el repositorio. Conserva las explicaciones que ayudan a entender el curso.

## Cómo verla

- Usa velocidad `1.5x`. Baja a `1.25x` solamente en Pydantic, concurrencia, NumPy o PyTorch si algo no queda claro.
- Después de cada clase lee su resumen; no regreses al video si el concepto ya quedó claro.
- No copies el código mientras ves el video. Las prácticas resueltas sirven para revisarlo después.

La ruta contiene aproximadamente **7 horas y 7 minutos** de video. A `1.5x` toma cerca de **4 horas y 45 minutos**; a `1.75x`, unas **4 horas y 4 minutos**.

## Tramos indispensables

### Clase 1 · Python básico — 24 minutos

- `44:46 a 53:35`: listas mutables, alias y copias.
- `1:05:01 a 1:12:03`: cero, valores vacíos y `None`.
- `1:32:19 a 1:40:38`: comprehensions, `enumerate` y `zip`.

Puedes saltar la introducción de la materia, la preparación de Colab y las instrucciones de entrega.

### Clase 2 · Funciones, errores y objetos — 41 minutos

- `09:23 a 18:42`: funciones, parámetros, `return` y `assert`.
- `49:22 a 1:02:14`: excepciones, `try`, `except` y `raise`.
- `1:02:22 a 1:21:09`: clases, objetos, `self` y estado por instancia.

Si ya entiendes agrupaciones puedes omitir `29:20 a 41:10`; si no, míralo como complemento.

### Clase 3 · Tipado y Pydantic — 37 minutos

- `1:03:48 a 1:17:16`: anotaciones modernas y propósito de los type hints.
- `1:17:16 a 1:23:43`: diferencia entre anotaciones, mypy y validación.
- `1:23:43 a 1:41:15`: modelos de Pydantic y `ValidationError`.

El bloque anterior del Zen puede sustituirse con el resumen escrito. Mira `45:01 a 1:03:06` únicamente si quieres ver la refactorización completa.

### Clase 4 · Pydantic en práctica — 28 minutos

- `45:11 a 1:03:19`: modelos, modo estricto, `Field`, `Literal` y campos extra.
- `1:11:22 a 1:21:17`: normalización mediante `field_validator`.

Los demás minutos resuelven ejercicios que ya están completos. Vuelve a `1:37:36 a 1:49:29` solo si quieres repasar casos límite y configuración de lotes.

### Clase 5 · Generadores, archivos y concurrencia — 45 minutos

- `37:53 a 49:51`: iterables, iteradores, generadores y context managers.
- `1:26:25 a 1:40:48`: archivos con `with` y limpieza cuando ocurre un error.
- `1:41:15 a 2:00:01`: `async`, `await`, tareas, `gather`, `TaskGroup` y timeout.

El tramo `50:07 a 1:21:45` es una práctica detallada de `iter`, `next` y `yield`; úsalo solamente si la primera explicación no fue suficiente.

### Clase 6 · uv y MCP — 39 minutos

- `20:44 a 43:08`: reproducibilidad, uv, `pyproject.toml`, lockfile y entorno virtual.
- `1:35:00 a 1:52:00`: dependencias, servidor MCP local y estructura de la entrega.

Puedes saltar la creación del proyecto comando por comando y el recorrido completo del catálogo; el proyecto resuelto conserva esa estructura.

### Clase 7 · NumPy — 1 hora 12 minutos

- `17:44 a 36:47`: diferencia entre listas y arreglos; `ndim`, `shape`, `size` y `dtype`.
- `44:15 a 1:21:04`: índices, slices y selección de filas y columnas.
- `1:31:00 a 1:47:28`: máscaras booleanas y combinación de condiciones.

Esta es una de las clases que menos conviene recortar. El bloque inicial sobre pytest, Ruff y mypy puede omitirse porque esas herramientas ya aparecen en la clase 6 y en los proyectos.

### Clase 8 · Proyecto final y pandas — 1 hora 13 minutos

- `00:30 a 13:40`: proyecto final, embeddings, búsqueda semántica y herramientas MCP.
- `23:40 a 33:25`: carga del Titanic, forma, tipos e información general.
- `33:25 a 48:40`: selección, `loc`, condiciones y máscaras.
- `48:40 a 1:08:30`: datos faltantes, `dropna`, `fillna` y agrupaciones.
- `1:08:30 a 1:23:30`: `merge` y preparación de arreglos para NumPy.

Omite la introducción a PyTorch del final: la clase 9 la retoma con más detalle.

### Clase 9 · DataLoader y CIFAR-10 — 1 hora 6 minutos

- `35:30 a 48:55`: `TensorDataset`, `DataLoader`, lotes y `drop_last`.
- `1:07:20 a 1:28:55`: `shuffle` reproducible con generadores y semillas.
- `1:28:55 a 1:49:15`: CIFAR-10, imágenes, tensores y transformaciones.
- `1:49:15 a 2:00:16`: dataset propio y carga bajo demanda.

El repaso de tensores entre `15:06 y 35:30` es opcional porque ya se introdujeron en la clase 8. Los primeros 15 minutos son soporte técnico y cambios de fechas.

## Orden recomendado por días

Para no saturarte, divide la ruta así:

1. **Python:** clases 1 y 2 — aproximadamente 44 minutos a `1.5x`.
2. **Validación:** clases 3 y 4 — aproximadamente 44 minutos a `1.5x`.
3. **Concurrencia y proyectos:** clases 5 y 6 — aproximadamente 56 minutos a `1.5x`.
4. **NumPy:** clase 7 — aproximadamente 48 minutos a `1.5x`.
5. **pandas y proyecto final:** clase 8 — aproximadamente 49 minutos a `1.5x`.
6. **PyTorch:** clase 9 — aproximadamente 44 minutos a `1.5x`.

## Qué puedes omitir sin preocupación

- Problemas para compartir pantalla o seleccionar el kernel, salvo que tengas el mismo error.
- Lectura en voz alta de instrucciones que ya están en los README.
- Negociación de fechas; las fechas vigentes están en `ENTREGAS.md`.
- Ejecución repetida de celdas y esperas por instalaciones o descargas.
- Preguntas administrativas y despedidas.
- Resolución completa de ejercicios que ya puedes inspeccionar en `unidades/*/tareas/`.

