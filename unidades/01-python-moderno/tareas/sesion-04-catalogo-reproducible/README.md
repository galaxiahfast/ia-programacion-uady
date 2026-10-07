# Catálogo de cursos reproducible con MCP

En esta carpeta resolví los nueve ejercicios de la sesión 4. La búsqueda funciona desde la terminal y también como herramienta MCP local.

## Preparación

```bash
uv sync --locked
```

Lo probé con Python 3.12.3. No incluí `.venv` porque uv puede volver a crearla con los archivos del proyecto.

## Uso

Consulta directa:

```bash
uv run --locked python main.py python
uv run --locked python main.py astronomy
uv run --locked python main.py python --catalog data/extra_courses.json
```

Consulta por MCP:

```bash
uv run --locked python client.py python
uv run --locked python client.py astronomy
uv run --locked python client.py " "
```

El cliente inicia y detiene `server.py`; no hace falta abrir el servidor en otra terminal.

## Ejercicios de aplicación

### 1. Punto de entrada

`python -c "import main"` no consulta el catálogo porque al importar un archivo su `__name__` no es `"__main__"`. La misma condición al final de `server.py` impide iniciar el transporte durante el import.

El decorador `@mcp.tool()` registra `find_courses` al importar el módulo. Registrar la función solo la deja disponible para el servidor; `mcp.run(transport="stdio")` es la llamada que inicia el transporte.

### 2. Datos y argumentos

En `data/extra_courses.json` agregué `PY03`, **Automatización práctica con Python**. La consulta con `--catalog` devuelve `PY01`, `PY02` y `PY03`. Una ruta inexistente termina con código 1 y no escribe resultados en stdout.

El servidor MCP conserva `data/courses.json` como catálogo predeterminado.

### 3. Niveles y destinos

- DEBUG muestra la ruta leída y el resumen de la búsqueda.
- INFO muestra solo el resumen.
- ERROR no muestra mensajes durante una consulta exitosa.

Con `--log-level ERROR --log-file logs/app.log`, la consola oculta DEBUG e INFO, pero esos mensajes sí se guardan en el archivo. El JSON usa stdout y los logs usan stderr; así no se mezclan con la comunicación de MCP.

### 4. Diagnóstico

El mensaje INFO ahora incluye coincidencias y total de cursos leídos:

```text
INFO | catalog.search | Search completed: 2 of 3 courses matched
```

La consulta directa y la herramienta MCP siguen devolviendo `PY01` y `PY02` para `python`.

### 5. Reproducción y llamada MCP

La herramienta descubierta es `find_courses`. Resultados comprobados:

| Consulta | Resultado | Código |
| --- | --- | ---: |
| `python` | `PY01` y `PY02` | 0 |
| `astronomy` | lista vacía válida | 0 |
| espacios | respuesta MCP con `is_error: true` | 1 |

Una lista vacía significa que la búsqueda fue válida pero no encontró coincidencias. La consulta en blanco es un error de entrada.

`pyproject.toml` declara el proyecto y las dependencias; `uv.lock` fija la resolución completa; `.python-version` selecciona Python 3.12. `.venv` no se entrega porque depende del equipo y se reconstruye con uv.

## Ejercicios de calidad

Para los ejercicios de calidad agregué dos pruebas:

- un curso con horas negativas debe ser rechazado;
- una ejecución de consola con catálogo inexistente debe salir con código 1 y stdout vacío.

También probé un `import json` sin usar. Ruff marcó `F401` y, después de quitarlo, la revisión volvió a pasar.

```bash
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy --strict main.py server.py client.py catalog
uv run --locked python -m pytest
```

Resultado final:

```text
All checks passed!
10 files already formatted
Success: no issues found in 6 source files
8 passed
```

Finalmente ejecuté `uv sync --locked`, el cliente MCP y las cuatro comprobaciones desde una copia limpia. Todo terminó con código 0.

## Estado

**Terminado y probado; todavía no enviado al formulario.**
